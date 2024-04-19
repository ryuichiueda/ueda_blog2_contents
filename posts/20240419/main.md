---
Keywords: ROS 2
Copyright: (C) 2024 Ryuichi Ueda
---

# ROS 2でTurtleBot3のナビゲーションのサンプルを動かすまでのつまづき

　科研費で「[位置情報の不足や誤りに強い自律移動ロボット用次世代ナビゲーションソフトウェア群](https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-24K15127/)」
を作ると大風呂敷を広げてしまったので泣きながら作業を開始しました。
んで、準備でTurtleBot3のシミュレータを動かそうとして、
ROS 1との違いでいくつかつまづいた点があったので備忘録を書いておきます。

　ROS 2のインストールとかパッケージのインストールとかの方法は、また別のところを参考にお願いします。
ROS 2のバージョンはhumbleです。何を動かしたのか上の作文だとわかりにくいかもしれませんが、↓これですこれ。


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">いろいろつまづいた（そして今更だ）けどROS 2でうごいた <a href="https://t.co/7326uLN646">pic.twitter.com/7326uLN646</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1781202302126391381?ref_src=twsrc%5Etfw">April 19, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

地図を用意して、（つまづかなければ）
[この資料](https://brain.cc.kogakuin.ac.jp/~kanamaru/lecture/ROS2/index5.html)に書いてあるふたつのコマンドを実行すると立ち上がります。地図は私の作ったのを使えます（下に記述あり）。

## ROS 2でのカンチョーのしかた

　まず、ROS 1でたまに必要だったフレームの設定のこのコマンド（自分は「カンチョー」と呼んでる）

```bash
$ rosrun tf static_transform_publisher 0 0 0 0 0 0 1 map my_frame 10
```

がROS 2でも必要になったので、調べたけど分からなくて死にました。が、[roboticskey](https://mi0.robotician.jp/)で聞いたら[としぞーさんにおしえていただけました](https://mi0.robotician.jp/notes/9s8mz0m7q2)。ありがとうございました。

## 機種の指定

　これは久々にやると忘れるやつですが、`~/.bashrc`に

```bash
export TURTLEBOT3_MODEL=burger #burgerのところに使いたい機種を書く
```

と1行書いて、`source ~/.bashrc`しましょう。

## amclが`nav2_amcl::MotionModel does not exist`と言う

　カンチョーしてもまだ動かなかったのでログを真面目に読んだらこんなエラーが出てました。

```bash
[component_container_isolated-1] [ERROR] [1713503168.774420684] [amcl]: Original error: According to the loaded plugin descriptions the class differential with base class type nav2_amcl::MotionModel does not exist. Declared types are nav2_amcl::DifferentialMotionModel nav2_amcl::OmniMotionModel
```

　で、調べたらここにしれっと解決法が書いてありました。

* https://github.com/ROBOTIS-GIT/turtlebot3/issues/884

　ということで、次のように`/opt/`で`grep`して修正すべきファイルを探し、

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">grep使えないと死ぬやつ <a href="https://t.co/xqMClfMtc5">pic.twitter.com/xqMClfMtc5</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1781203280355570079?ref_src=twsrc%5Etfw">April 19, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

当該部分を書き直しました。

```bash

ueda@uedaP1g6:/opt$ vi ros/humble/share/turtlebot3_navigation2/param/burger.yaml 
・・・
 29     robot_model_type: "nav2_amcl::DifferentialMotionModel"  ←この行を加える
 30       # robot_model_type: "differential"                    ←この行は#でコメントアウト
```

## マップ作るのめんどくさい

　ROS 1のやつで大丈夫でした。[私の作ったのがここにあります](https://github.com/ryuichiueda/value_iteration/tree/main/maps)。冒頭のスクショの亀型の環境なら`map.yaml`と`map.pgm`を使うといいです。マップ（yamlファイルとpgmファイル）をダウンロードしたディレクトリで、`ros2 launch turtlebot3_navigation2`の立ち上げ時に`map:=map.yaml`を指定すると使えます。

## Gazebo立ち上がらん

 初期設定に時間がかかるので気長に待ちましょう。


## 立ち上がったら

　RVizでロボットの位置とゴールの位置を指定すると、ロボットが動き出します。


　現場からは以上です。
