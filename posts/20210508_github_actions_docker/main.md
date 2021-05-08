---
Keywords: ROS,Docker,GitHub,CI
Copyright: (C) 2021 Ryuichi Ueda
---

# GitHub Actions内でGazeboを動かす

変態行為に成功したので手順を書いておきます。


## なにがしたいのか

[自分の作った自己位置推定パッケージ](https://github.com/ryuichiueda/emcl)をGitHub Actions上でテストしたい。この動画のように、間違った位置を`emcl`という自己位置推定器に渡して、`emcl`がそれを修正できることをテストで確認したい。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">mclに膨張リセットを実装してemclというパッケージを作りました。パーティクルの場所をずらしても少しなら収束します。こっちは実用を目指します。<br><br>（たぶんamclより使い勝手は良いはず。）<a href="https://t.co/u6MQhjRRuN">https://t.co/u6MQhjRRuN</a> <a href="https://t.co/sxPFCd0IzF">pic.twitter.com/sxPFCd0IzF</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1389450563503280128?ref_src=twsrc%5Etfw">May 4, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## なんでrosbag使わないの？

どのトピックを記録していいのかようわからん。（ダメじゃん）

## この記事で説明するファイル

* [test.yml](https://github.com/ryuichiueda/emcl/blob/4daeaef61ce22c675779db087f387c8f853a5daf/.github/workflows/test.yml)
* [その他のファイル](https://github.com/ryuichiueda/emcl/tree/4daeaef61ce22c675779db087f387c8f853a5daf/test)

## Dockerまわりの準備

テストには、環境用と、環境用に`emcl`をインストールしたのDockerのイメージを使います。環境用はDocker Hubに置いて、もうひとつはGitHub Actions上で作ります。

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


### `emcl`をインストールするDockerfileを作成

GitHub ActionsでビルドするためのDockerfile（`docker`ディレクトリにあります）です。テスト対象のリポジトリをクローンしてビルドするだけです。

```bash
FROM ryuichiueda/emcl-test-env:latest  #上で作ったテスト環境のイメージを利用
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN cd /catkin_ws/src && \
    git clone https://github.com/ryuichiueda/emcl.git  #これだとマスターブランチのテストになるのであとから編集

RUN source ~/.bashrc && \
    cd /catkin_ws && \
    catkin_make
```

## GitHub Actionsの設定

GitHub Actionsには、次のYAMLファイル（`test.yaml`）を使います。上で作った`emcl`インストール用のDockerfileについて、テストしたいブランチをcloneするように`sed`で書き換えてイメージを作り、その後、コンテナ内のテストスクリプトを実行します。テストスクリプト（`er_test.bash`）についてはあとで説明します。

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
      - name: Build image              #emclをインストールしたイメージの作成
        run: |
         git clone -b "${GITHUB_REF#refs/heads/}" https://github.com/ryuichiueda/emcl.git
         cd emcl/test/docker
         sed -i "s;clone;clone -b ${GITHUB_REF#refs/heads/};" Dockerfile #いま扱っているブランチをcloneするよう改竄
         docker build -t test .
      - name: Reset test on Gazebo     #テストスクリプトの実行
        run: |
         docker run test /bin/bash -c 'source ~/.bashrc && /catkin_ws/src/emcl/test/er_test.bash'
```


## テストの手順の作成

### launchファイル

こんどはROSまわりの設定です。テスト用のlaunchファイル（`test.launch`）はこんな感じです。GazeboにTurtleBot3を置いて自己位置推定させます。2行目の`<arg name="gui" default="false"/>`以外は、TurtleBot3のシミュレーションを動かすときのものと同じです。2行目は、（うろ覚えなのですが）`rviz`がGUIなしで立ち上げる設定だったと思います。

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


### テストスクリプト

ROSの機能を使ってテストを走らせてもいいのですが、シェルスクリプトで十分なので、シェルスクリプトです。`roslaunch`は、ダミーのディスプレイの役をするソフトXvfbで実行します。


```bash
#!/bin/bash -evx

### ノードの実行（xvfbで）
export TURTLEBOT3_MODEL=burger
xvfb-run --auto-servernum -s "-screen 0 1400x900x24" roslaunch emcl test.launch &
sleep 15

### 間違った自己位置をemclに伝える

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

### emclが間違いを修正するのを待つ

rostopic echo /mcl_pose -n 1000 |
grep -A2 position:             |
awk '/x:/{printf $2" "}/y:/{print $2}' |
awk '{print $0}
     sqrt( ($1+2.0)^2 + ($2+0.5)^2 ) < 0.15 {print "OK";exit(0)}
     NR==1000{print "TIMEOUT";exit(1)}'  #自己位置が正しい地点から15cm以内に収まったらexit(0)する

RESULT=$?              #ここにテストの成否が入る

killall rosmaster &    #マスタを止める（手元で試すとき用） 

exit $RESULT           #結果を返す
```

実はXvfbで動かさなくてもGazeboのフロントエンドが死ぬだけでテストは実行できるのですが、こうやっておくとGazeboはGUI環境がないことが分からず、何のエラーも出さずに動きます。


## 実行結果

https://github.com/ryuichiueda/emcl/runs/2532961704 のようになりました。「`Reset test on Gazebo`」を開くと、シェルスクリプトで実行したテストがうまくいっていることが分かります。


## まとめ

* GitHub ActionsでGazebo（とかRvizとかROS一式）が動いた


## 今後

ALSA（音声関係のソフト）がエラーを出しているので、なんとかする。



以上です。
