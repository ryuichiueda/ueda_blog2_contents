---
Keywords: はまった,Hadoop,pig,UNIX/Linuxサーバ,辛い
Copyright: (C) 2017 Ryuichi Ueda
---

# Hadoopのpigを使うときに設定ではまったところメモ
上田です。あいの風とやま鉄道車中です。

必要なので金曜日からHadoopをpigでいじっています。手順は全部のっけませんが、「Hadoop初心者&シェルについてはそこそこ詳しい」という立ち位置で、はまった2点をメモします。

<!--more-->
<h2>基本、hdfsというユーザでなんでも動かすと・・・</h2>

無難なようです。しかしhdfsユーザでなんでも動かすのならば、hdfsユーザでjava等の環境変数がきっちり設定されている必要があります。

ということなんですが、パスを通したり何したりというのが結構ややこしいので、こうやって使うのがとりあえず手っ取り早いみたいです。

まず、bashを使うなら自分のユーザの.bashrcにこう書いてパスを通しておく。（書いたらsourceするか一度ログアウト、ログインを）。

[bash]
export JAVA_HOME=/usr/java/jdk1.7.0_75/
###PIG_CLASSPATHはこれ、不要か間違ってるかもしれません###
export PIG_CLASSPATH=/etc/hadoop/conf.cluster/
[/bash]

んで、sudo -Eu hdfs <コマンド> で作業。sudo -Eで今いじっているユーザの環境変数を引き継げます。

[bash]
[usp\@boabs005 ~]$ sudo -Eu hdfs hdfs dfs -ls
Found 9 items
drwxr-xr-x - hdfs hadoop 0 2015-02-28 04:12 input
drwxr-xr-x - hdfs hadoop 0 2015-02-28 04:19 output
-rw-r--r-- 3 hdfs hadoop 427 2015-04-04 02:01 tenline
...
[/bash]

面倒なので、こんなスクリプトを書きました。

[bash]
[usp\@boabs005 ueda]$ cat ./do-pig 
#!/bin/bash

sudo -Eu hdfs ./pig-0.12.0-cdh5.3.1/bin/pig $1
[/bash]


<h2>cdhのバージョンがpigとhadoopで合ってないといけないらしい</h2>

yumで入れたのが違う・・・

[bash]
[usp\@boabs005 ueda]$ hadoop version
Hadoop 2.5.0-cdh5.3.1
...
[usp\@boabs005 ueda]$ pig --version
Apache Pig version 0.8.1-cdh3u6 (rexported) 
compiled Mar 20 2013, 13:45:59
[/bash]

ということで、<a href="http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cdh_vd_cdh_package_previous.html#concept_cb1_dhz_dr_unique_2">ココ</a>からpigをダウソロードして解凍しました。解凍したところのbin/pigを起動したら普通に使えました。


めでたしめでたし。


<h2>肝心のpigですが・・・</h2>

遅い・・・。やっぱり4ノード（クライアント1, マスター1, スレーブ4）じゃあHadoopは効果無いし、スピードだけが欲しいなら自分でファイルをノードに分散させてシェル芸したほうが速いに決まってます。チューニングとかそういう次元の話ではありません。


<h2>参考サイト</h2>

参考にしたサイトですが、以下でインストールを行い、あとは断片的な情報を集めて総合してOさんと一緒に考えました。


<span class="hatena-bookmark-title"><a href="http://blog.livedoor.jp/sasata299/archives/51461548.html">CentOS に Hadoop, Pig, Hive, HBase をインストール - (ﾟ∀ﾟ)o彡 sasata299's blog</a></span> <span class="hatena-bookmark-users"><a href="http://b.hatena.ne.jp/entry/blog.livedoor.jp/sasata299/archives/51461548.html"><img title="CentOS に Hadoop, Pig, Hive, HBase をインストール - (ﾟ∀ﾟ)o彡 sasata299's blog" alt="CentOS に Hadoop, Pig, Hive, HBase をインストール - (ﾟ∀ﾟ)o彡 sasata299's blog" src="http://b.hatena.ne.jp/entry/image/http://blog.livedoor.jp/sasata299/archives/51461548.html"></a></span>


以上。めでたしめ・・・んどくせえ・・・。
