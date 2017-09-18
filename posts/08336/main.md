---
Keywords: C/C++,ROS,価値反復,動的計画法,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# 価値反復のROSパッケージ作った
いつも研究で使っている価値反復のコードをROS化しました。オフライン計算をするためのものなんですが、わざわざROSにしました。なんか使ってもらえそうというアホな理由と、移動ロボットの経路計画くらいならそろそろ半リアルタイム（ロボットが動く前に数秒で計算するとかいう用途）に使えそうだという割と本気の理由から。<br />
<br />
<ul><br />
	<li><a href="https://github.com/ryuichiueda/simple_value_iteration_ros">https://github.com/ryuichiueda/simple_value_iteration_ros</a></li><br />
</ul><br />
<br />
使い方はREADMEに書きましたが、日本語でも書いておきます。ウリはマルチスレッドで一気に計算できることです。これを分散処理にまで持っていく（そしてGPU対応にする）のが当面の目標。何千もCPUがあれば並列処理が簡単な分、普通のリアルタイムな探索より速くなったりして（未確認）。<br />
<br />
<br />
まず、value_iterationというノードを立ち上げます。これがソルバです。<br />
<br />
[bash]<br />
$ rosrun simple_value_iteration_ros value_iteration <br />
[/bash]<br />
<br />
で立ち上がります。<br />
<br />
<br />
試しに下のような単純なタイルワールドでstate 2に前後左右に移動して到達するという問題を解いてみましょう。<br />
<br />
<pre><br />
|-----------------------|<br />
| | | |<br />
|state 0|state 1|state 2|<br />
| | | |<br />
|-----------------------|<br />
| | | |<br />
|state 3|state 4|state 5|<br />
| | | |<br />
|-------|-------|-------|<br />
| | | |<br />
|state 6|state 7|state 8|<br />
| | | |<br />
|-------|-------|-------|<br />
</pre><br />
<br />
<br />
解くときは、value_iterationノードに状態数がいくつでどんな行動があるか、状態遷移はどんなのがあるか、終端状態はどれかを書いたファイルを食わせて計算させます。そのファイルがこれ:<br />
<br />
<ul><br />
	<li><a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/example_state_trans">simple_value_iteration_ros/scripts/example_state_trans</a></li><br />
</ul><br />
<br />
なんとなく分かるような気もするけど、分からんような気もする。ちなみに確率的な状態遷移も扱えます。<a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/example_state_trans_prob">example_state_trans_prob</a>が例です。<br />
<br />
パッケージには、このファイルをvalue_iterationに食わせて結果を表示するサンプルコードがあります。<br />
<br />
<a href="https://github.com/ryuichiueda/simple_value_iteration_ros/blob/master/scripts/sample.py">simple_value_iteration_ros/scripts/sample.py</a><br />
<br />
です。実行してみます。すぐ収束してしまいますが、価値関数が収束して適切な方策が得られます。<br />
<br />
[bash]<br />
$ rosrun simple_value_iteration_ros sample.py <br />
### sweep 1 ###<br />
values:<br />
 0 70368744177664 1 1000 2 0 <br />
 3 70368744177664 4 2000 5 1000 <br />
 6 70368744177664 7 3000 8 2000 <br />
<br />
policy:<br />
 0 null 1 right 2 null <br />
 3 null 4 up 5 up <br />
 6 null 7 up 8 up <br />
<br />
### sweep 2 ###<br />
values:<br />
 0 2000 1 1000 2 0 <br />
 3 3000 4 2000 5 1000 <br />
 6 4000 7 3000 8 2000 <br />
<br />
policy:<br />
 0 right 1 right 2 null <br />
 3 up 4 up 5 up <br />
 6 up 7 up 8 up <br />
[/bash]<br />
<br />
<br />
・・・もっと詳しい説明が必要なんだけど・・・<br />
<br />
<br />
寝る。
