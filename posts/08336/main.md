---
Keywords: C/C++,ROS,価値反復,動的計画法,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# 価値反復のROSパッケージ作った
いつも研究で使っている価値反復のコードをROS化しました。オフライン計算をするためのものなんですが、わざわざROSにしました。なんか使ってもらえそうというアホな理由と、移動ロボットの経路計画くらいならそろそろ半リアルタイム（ロボットが動く前に数秒で計算するとかいう用途）に使えそうだという割と本気の理由から。

<ul>
	<li><a href="https://github.com/ryuichiueda/simple_value_iteration_ros">https://github.com/ryuichiueda/simple_value_iteration_ros</a></li>
</ul>

使い方はREADMEに書きましたが、日本語でも書いておきます。ウリはマルチスレッドで一気に計算できることです。これを分散処理にまで持っていく（そしてGPU対応にする）のが当面の目標。何千もCPUがあれば並列処理が簡単な分、普通のリアルタイムな探索より速くなったりして（未確認）。


まず、value_iterationというノードを立ち上げます。これがソルバです。

[bash]
$ rosrun simple_value_iteration_ros value_iteration 
[/bash]

で立ち上がります。


試しに下のような単純なタイルワールドでstate 2に前後左右に移動して到達するという問題を解いてみましょう。

<pre>
|-----------------------|
| | | |
|state 0|state 1|state 2|
| | | |
|-----------------------|
| | | |
|state 3|state 4|state 5|
| | | |
|-------|-------|-------|
| | | |
|state 6|state 7|state 8|
| | | |
|-------|-------|-------|
</pre>


解くときは、value_iterationノードに状態数がいくつでどんな行動があるか、状態遷移はどんなのがあるか、終端状態はどれかを書いたファイルを食わせて計算させます。そのファイルがこれ:

<ul>
	<li><a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/example_state_trans">simple_value_iteration_ros/scripts/example_state_trans</a></li>
</ul>

なんとなく分かるような気もするけど、分からんような気もする。ちなみに確率的な状態遷移も扱えます。<a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/example_state_trans_prob">example_state_trans_prob</a>が例です。

パッケージには、このファイルをvalue_iterationに食わせて結果を表示するサンプルコードがあります。

<a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/sample.py">simple_value_iteration_ros/scripts/sample.py</a>

です。実行してみます。すぐ収束してしまいますが、価値関数が収束して適切な方策が得られます。

[bash]
$ rosrun simple_value_iteration_ros sample.py 
### sweep 1 ###
values:
 0 70368744177664 1 1000 2 0 
 3 70368744177664 4 2000 5 1000 
 6 70368744177664 7 3000 8 2000 

policy:
 0 null 1 right 2 null 
 3 null 4 up 5 up 
 6 null 7 up 8 up 

### sweep 2 ###
values:
 0 2000 1 1000 2 0 
 3 3000 4 2000 5 1000 
 6 4000 7 3000 8 2000 

policy:
 0 right 1 right 2 null 
 3 up 4 up 5 up 
 6 up 7 up 8 up 
[/bash]


・・・もっと詳しい説明が必要なんだけど・・・


寝る。
