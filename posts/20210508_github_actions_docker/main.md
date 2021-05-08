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

## この記事で説明するファイル

* [test.yml](https://github.com/ryuichiueda/emcl/blob/e7decb3251154097d22dd621d2108283f0a3c8a5/.github/workflows/test.yml)
* [その他のファイル](https://github.com/ryuichiueda/emcl/tree/e7decb3251154097d22dd621d2108283f0a3c8a5/test)

## 手口1（GitHub Actionsまわりの準備）

### テスト環境のDockerイメージの作成

まず、Gazebo上でTurtleBot3が動くDockerのイメージを作ります。私の作ったDockerfile（`docker_env`ディレクトリにあるやつ）はこんな感じです。もちろん、Gazeboで動かしたいものによってダウンロードするものは変わります。

```bash
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

GitHub ActionsでビルドするためのDockerfile（`docker`ディレクトリにあります）です。テスト対象のリポジトリをクローンしてビルドするだけです。

```bash
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

GitHub Actionsには、次のYAMLファイル（`test.yaml`）を使います。上で作ったパッケージインストール用のDockerfileでイメージを作り、コンテナ内のテストスクリプトを実行します。テストスクリプト（`er_test.bash`）についてはあとで説明します。

```yaml
name: er_test

on:
  push:
    paths-ignore:
      - '**.md'

jobs:
  build:
    runs-on: ubuntu-18.04

    steps:
      - uses: actions/checkout@v2
      - name: Build image                                                 #イメージを作成
        run: |
         git clone -b "${GITHUB_REF#refs/heads/}" https://github.com/ryuichiueda/emcl.git
         cd emcl/test/docker
         sed -i "s;clone;clone -b ${GITHUB_REF#refs/heads/};" Dockerfile  #Dockerfileの中のcloneを当該のブランチに
         docker build -t test .
      - name: Reset test on Gazebo                                        #コンテナ内のテストスクリプトを実行
        run: |
         docker run test /bin/bash -c 'source ~/.bashrc && /catkin_ws/src/emcl/test/er_test.bash'
```


## 手口2（テストの実行）

### launchファイル

こんどはROSまわりの設定です。テスト用のlaunchファイル（`test.launch`）はこんな感じです。GazeboにTurtleBot3を置いて自己位置推定させます。

```xml
<launch>
  <arg name="gui" default="false"/>
  <!-- Set tf -->
  <node pkg="tf" type="static_transform_publisher" name="world_to_map" args="0 0 0 0 0 0 world map 100" />

  <!-- Launch other launch files -->
  <include file="$(find turtlebot3_gazebo)/launch/turtlebot3_world.launch"/>

  <!-- Arguments -->
  <arg name="model" default="burger" doc="model type [burger, waffle, waffle_pi]"/>
  <arg name="map_file" default="$(find turtlebot3_navigation)/maps/map.yaml"/>
  <arg name="open_rviz" default="false"/>
  <arg name="move_forward_only" default="false"/>

  <!-- Turtlebot3 -->
  <include file="$(find turtlebot3_bringup)/launch/turtlebot3_remote.launch">
    <arg name="model" value="$(arg model)" />
  </include>

  <!-- Map server -->
  <node pkg="map_server" name="map_server" type="map_server" args="$(arg map_file)"/>

  <!-- EMCL -->
  <include file="$(find emcl)/launch/emcl.launch"/>

  <!-- rviz -->
  <group if="$(arg open_rviz)">
    <node pkg="rviz" type="rviz" name="rviz" required="true"
          args="-d $(find turtlebot3_navigation)/rviz/turtlebot3_navigation.rviz"/>
  </group>

</launch>
```

2行目の`<arg name="gui" default="false"/>`が、（うろ覚えなのですが）`rviz`がGUIなしで立ち上げる設定だったと思います。ただ、後述のとおり、これはいらないかもしれません。

### テストスクリプト

ROSの機能を使ってテストを走らせてもいいのですが、シェルスクリプトで十分なので、シェルスクリプトです。


```bash
#!/bin/bash -evx

export TURTLEBOT3_MODEL=burger
# ノードの立ち上げ
roslaunch emcl test.launch &

sleep 15

# 自己位置推定関係のトピックを出す（間違った自己位置を自己位置推定器に伝える）
rostopic pub /initialpose geometry_msgs/PoseWithCovarianceStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
pose:
  pose:
    position: {x: -2.5, y: 0.0, z: 0.0}
    orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}
  covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0]" --once

# 自己位置推定器が間違いを訂正できるかどうかを評価
rostopic echo /mcl_pose -n 1000 |
grep -A2 position:             |
awk '/x:/{printf $2" "}/y:/{print $2}' |
awk '{print $0}
     sqrt( ($1+2.0)^2 + ($2+0.5)^2 ) < 0.15 {print "OK";exit(0)}
     NR==1000{print "TIMEOUT";exit(1)}'   #このawkの終了ステータスがテスト結果に
```

で、書いていて気がついたのですが、もともとこのスクリプトでは、ダミーのディスプレイを立ちあげる`xvfb`を使っていたのですが、いろいろ試しているときに抜けてしまいました。ですので、GUIを使う設定でも、GitHub ActionsではGazeboもRvizも実行できている・・・ような気がします。


## 実行結果

https://github.com/ryuichiueda/emcl/runs/2532476169 のようになりました。「`Reset test on Gazebo`」を開くと、（いろいろエラーが出た後）、Gazeboが立ちあがって、`rostopic`のあと、自己位置推定器が反応してテストが成功した様子が見れます。


## まとめ

* GitHub ActionsでGazebo（とかRvizとかROS一式）が動いた
* Gazebo、GUIを使う設定なのにテストはできた（`xvfb`使っているつもりだったのにいつのまにか抜けてた）


## 今後

```
[gazebo_gui-4] process has died [pid 97, exit code 134, cmd /opt/ros/melodic/lib/gazebo_ros/gzclient __name:=gazebo_gui __log:=/root/.ros/log/47b17752-afa5-11eb-bf21-0242ac110002/gazebo_gui-4.log].
```

というように叱られが発生しているので、なんとかする。



以上です。
