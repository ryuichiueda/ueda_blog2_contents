---
Keywords: ROS,Docker,GitHub,CI
Copyright: (C) 2021 Ryuichi Ueda
---

# GitHub Actions内でGazeboを動かす

変態行為に成功したので手順を書いておきます。


## なにがしたかったのか

[自分の作った自己位置推定パッケージ](https://github.com/ryuichiueda/emcl)をGitHub Actions上でテストしたい。

## なんでrosbag使わないの？

どのトピックを記録していいのかようわからん。（ダメじゃん）

## 手口1（GitHub Actionsまわりの準備）

### テスト環境のDockerイメージの作成

まず、Gazebo上でTurtleBot3が動くDockerのイメージを作ります。私の作ったDockerfileはこんな感じです。もちろん、Gazeboで動かしたいものによってダウンロードするものは変わります。

```
FROM ryuichiueda/ubuntu18.04-ros-image   #私の作ったサーバ用ROS環境イメージ
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y ros-melodic-desktop-full   #デスクトップ版を追加でインストール
RUN apt-get install -y ros-melodic-tf ros-melodic-tf2 ros-melodic-tf2-geometry-msgs ros-melodic-urdf ros-melodic-map-server xvfb vim psmisc #注意：いらないものもインストールしてるかも

# 必要なものをcatkin_ws/src下に置く（最新のコミットだけ落とすようにしたほうがよいです）
RUN cd /catkin_ws/src && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_gazebo_plugin.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

# ビルド
RUN source ~/.bashrc && \
    cd /catkin_ws && \
    catkin_make
```


これをビルドしてDocker Hubにpushしておきます。私のpushしたのは↓です。

* https://hub.docker.com/repository/docker/ryuichiueda/emcl-test-env


### テストしたいパッケージをインストールするDockerfileを作成

GitHub ActionsでビルドするためのDockerfileです。テスト対象のリポジトリをクローンしてビルドするだけです。

```
FROM ryuichiueda/emcl-test-env:latest  #上で作ったテスト環境のイメージを利用
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN cd /catkin_ws/src && \
    git clone https://github.com/ryuichiueda/emcl.git  #これだとマスターブランチのテストになるので改良が必要

RUN source ~/.bashrc && \
    cd /catkin_ws && \
    catkin_make
```

### GitHub Actionsの設定

GitHub Actionsには、次のYAMLファイルを使います。上で作ったパッケージインストール用のDockerfileでイメージを作り、コンテナ内のテストスクリプトを実行します。このテストスクリプト（`er_test.bash`）内に、GazeboをGUIなしで実行するコードが書いてありますのであとで説明します。

```
name: vi_test

on:
  push:
    paths-ignore:
      - '**.md'

jobs:
  build:
    runs-on: ubuntu-18.04

    steps:
      - uses: actions/checkout@v2
      - name: Build image
        run: |
         git clone -b "${GITHUB_REF#refs/heads/}" https://github.com/ryuichiueda/emcl.git
         cd emcl/docker
         docker build -t test .                                   #上記の（ふたつめの）Dockerfileでイメージ作成
      - name: Reset test on Gazebo
        run: |
         docker run test /bin/bash -c 'source ~/.bashrc && /catkin_ws/src/emcl/test/er_test.bash' #テストスクリプトの実行
```

## 手口2（GazeboをGUIなしで実行）



