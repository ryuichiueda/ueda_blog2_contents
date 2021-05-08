---
Keywords: ROS,Docker,GitHub,CI
Copyright: (C) 2021 Ryuichi Ueda
---

# GitHub Actions内でGazeboを動かす

という変態行為に成功したので手順を書いておきます。


## なにがしたかったのか

自分の作った自己位置推定パッケージをGitHub Actions上でテストしたい。

## なんでrosbag使わないの？

どのトピックを記録していいのかようわからん。（ダメじゃん）

## 手口

まず、Gazebo上でTurtleBot3が動くDockerのイメージを作ります。Dockerfileはこんな感じです。

```
FROM ryuichiueda/ubuntu18.04-ros-image   #私の作ったサーバ用ROS環境イメージ
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y ros-melodic-desktop-full   #デスクトップ版を追加でインストール
RUN apt-get install -y ros-melodic-tf ros-melodic-tf2 ros-melodic-tf2-geometry-msgs ros-melodic-urdf ros-melodic-map-server xvfb vim psmisc #注意：いらないものもインストールしてるかも

# 必要なものをcatkin_ws/src下に置く
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



