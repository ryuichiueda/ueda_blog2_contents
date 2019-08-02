---
Keywords: 日記,SGWeb
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年8月2日）

　仕事はベトナムと台湾からのお客様相手の集中講義で1コマ分実習。適当英語。半年ぶりに英語話したのに上達してた。意味不明。そして後期の実習のため、下記のWSLへのROSインストール。

## WSL + ROS

　2年生がCADソフトの関係でWindowsを使っているにもかかわらずROSの実習をしなければならなくなったので、Windows Subsystem for LinuxでROSを動かすことに。朝から挑戦して、上記のように実習で中断したけど夕方までにうまくいった。[講義用に資料](https://ryuichiueda.github.io/manipulator_practice_b3/lesson1.html#/1)をまとめている最中。

　ハマったのはRVizのところで、私の環境だとOpenGLの間接レンダリングを強制しない設定にしないといけなかった模様。この設定がないとセグメンテーションフォルトが起こりました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">~/.bashrcに<br><br>export LIBGL_ALWAYS_INDIRECT=0<br><br>を書き込むと立ち上がりましたー</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1157174673295101952?ref_src=twsrc%5Etfw">August 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

* 参考: 出村先生のページ: https://demura.net/lecture/15304.html

　で、RVizは問題なく動くようになったけど、今度はGazeboに映像が出ないことに気づきました。が、やはり出村先生のページを参考にして解決。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">gazebo も出ました〜<br><br>export GAZEBO_IP=127.0.0.1<br>が必要でした。<br><br>参考: <a href="https://t.co/YotmJkJnKi">https://t.co/YotmJkJnKi</a> <a href="https://t.co/MKcyQ9DLwP">pic.twitter.com/MKcyQ9DLwP</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1157192348222156800?ref_src=twsrc%5Etfw">August 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　で、マニピュレータを動かしてみました。動きました。ぐんにゃりしたけど。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">マニピュレータが力尽きた・・・寝てしまった・・・ <a href="https://t.co/ILmZB9ZG9K">pic.twitter.com/ILmZB9ZG9K</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1157195258951680000?ref_src=twsrc%5Etfw">August 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
