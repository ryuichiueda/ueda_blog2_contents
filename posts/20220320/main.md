---
Keywords: 日記, ROS, CMake
Copyright: (C) 2022 Ryuichi Ueda
---

# 日記（2022年3月20日）

　自己位置推定の[emclパッケージ](https://github.com/ryuichiueda/emcl)がごちゃごちゃしたので整理。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">emclパッケージ、性能を改善しようとしてゴチャゴチャになっていたのですが、屋内用と屋外用にパッケージを分けました。<br><br>屋内用: <a href="https://t.co/u6MQhjRRuN">https://t.co/u6MQhjRRuN</a><br><br>屋外用: <a href="https://t.co/i6adtf1wQq">https://t.co/i6adtf1wQq</a><a href="https://twitter.com/hashtag/emcl?src=hash&amp;ref_src=twsrc%5Etfw">#emcl</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1505416920396275716?ref_src=twsrc%5Etfw">March 20, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## catkin_makeのときに同じ名前のクラスが複数あってbuildできないとき

　emclの分離作業を進めていたら、`catkin_make`が「（emclとemcl2に）同じ名前のクラスがある」と言ってエラーを吐きました。

```
CMake Error at emcl2/CMakeLists.txt:18 (add_library):
  add_library cannot create target "Mcl" because another target with the same
  name already exists.  The existing target is a shared library created in
  source directory "/home/ueda/catkin_ws/src/emcl".  See documentation for
  policy CMP0002 for more details.
```

C++のコードでnamespaceを分けておけば大丈夫かと思ってたらどうやらそれではダメらしく、次のリンクのように`CMakeLists.txt`の`add_library`と`target_link_libraries`を変更しなければならないと分かりました。`add_library`の最初の引数の名前をユニークなものにしなければならないようです。

https://github.com/ryuichiueda/emcl2/commit/8b9919352e0951185df451d5a33be6a041c0bbdc#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20a

例えば上のリンクの例では、`add_library(Mcl src/Mcl.cpp)`の`Mcl`を`add_library(Mcl_emcl2 src/Mcl.cpp)`というように、`Mcl_emcl2`という固有の名前に変更しています。`target_link_libraries`では、`add_library`でつけた名前で当該のライブラリ（というよりは`src/Mcl.cpp`をコンパイルしたオブジェクト？）を参照します。


　本まで書いてるのに、ここらへんグダグダで大変申し訳なく・・・。


## シェル・ワンライナー160本ノック増刷

　ROSだけでなく、シェル芸人としても、本まで書いているのにシェルさっぱり分からんと日々悩んでますが、第4刷が出ます！

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">【ご報告】4刷出まーす！！🎉<br><br>1日1問、半年以内に習得 シェル・ワンライナー160本ノック (Software Design plusシリーズ)   上田 隆一 <a href="https://t.co/tl68IPNE7d">https://t.co/tl68IPNE7d</a> <a href="https://twitter.com/AmazonJP?ref_src=twsrc%5Etfw">@amazonJP</a>より</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1503691071464751110?ref_src=twsrc%5Etfw">March 15, 2022</a></blockquote>

シェルさっぱり分からんけど出るものは仕方ない。よろしくお願いいたしまーす。


## その他

　今日はなぜかいろいろ仕事が進んで、マンションのある会から依頼されていたポスターを完成させて提出。なぜか明日（祝日なんですけど）を締め切りにご指定いただいた報告書も完成。明日はなにをしよう・・・。



以上です。
