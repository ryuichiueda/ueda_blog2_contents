---
Keywords: Family,Kinect,Linux,TurtleBot2
Copyright: (C) 2017 Ryuichi Ueda
---

# TurtleBot2動かしたときのメモ
後追いになっちまったけど、<a href="http://www.familyrobotics.org/?page_id=86" target="_blank">http://www.familyrobotics.org/?page_id=86</a>の内容をおさらい。文章は内輪向けです。

<h2>構成</h2>

<ul>
 <li>ロボット: TurtleBot2</li>
 <li>ロボットを動作させるPC: ThinkPad x201</li>
 <li>OS: Ubuntu 14.04 → 12.04</li>
</ul>

<h2>とりあえず動かしてみた</h2>

こんな感じでした。Kinectで人を感知して追いかけるという動作をします。外からは操作しておらず自律です。ROSをはじめいろんな人が書いたコードをダウンロードして組み合わせて動かしております。うーん。オープンソースっていいですねー。（←誰の真似だ？）

<!--more-->

<iframe width="420" height="315" src="//www.youtube.com/embed/izqbouITHh0" frameborder="0" allowfullscreen></iframe>


<iframe width="420" height="315" src="//www.youtube.com/embed/AMJO_QKLoGk" frameborder="0" allowfullscreen></iframe>

人を追っかける核心のところのコードは確かジェフリーさんが作ったんだと記憶してますが、結局ネットからインストールしてしまったのでちゃんと確かめてません。たぶんジェフリーさんですが・・・。便利になるとリスペクトが足らなくなるなあというのは反省しないと（今度聞いておきます）。

<h2>メモ</h2>

OSを12.04にダウングレード（再インストール）したのはKinectの信号が読めないという症状が出たからでした。lsusb(1)するとデバイスが見えましたが、画像や距離データが読めませんでした。ただ、内部情報で解決できたという話が回ってきているので、解決者の公表を待ちたいと思います。

12.04で冒頭のサイトの手順を追ったら、すんなりインストールできました。ただ、Kinectと通信するにはパーミッションを変えないといけません。
[bash]
$ sudo chmod 777 -R /dev/bus/usb/
[/bash]
が必要かと。修正するには確信がないのでとりあえずここに書いておきます。

それから、私の買った中古のThinkPad x201の電池が10分しか持ちません・・・。それは電池を買うとして、台車とPCの電池を両方気にしなければいけないのは大変だなあ・・・。


とりあえずこんなところで。自分でコードを書かないとなあ・・・。
