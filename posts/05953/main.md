---
Keywords: ごめんなさい,bash,Linux,Mac,pipefail,ご報告,シェルプログラミング実用テクニック,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# bashのpipefailで確実にスクリプトを止める
<a href="http://gihyo.jp/book/2015/978-4-7741-7344-3" title="シェルプログラミング実用テクニックの目次が公開されました（エクシェル芸、斉藤さん、and 鳩）" target="_blank">シェルプログラミング実用テクニック</a>、出版される前からもう補足ですが、私めがbashのpipefailというオプションをすっかり見落としていたのでフォローしておきます。<br />
<br />
<ul><br />
 <li>カンニング先: <a href="http://d.hatena.ne.jp/iww/20130409/pipefail">パイプの途中のエラーを取る | 揮発性のメモ</a></li><br />
</ul><br />
<br />
本文ではbashに-e（エラーがあったら止める）をつけてもパイプラインの左側のコマンドにエラーがあったときに処理が止まらないと書きました。<br />
<br />
例です。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
###false | true###でfalseが終了ステータス1を返すが・・・###<br />
uedambp:~ ueda$ cat hoge.bash <br />
#!/bin/bash -e<br />
<br />
false | true<br />
echo do not stop<br />
###-eがあるにもかかわらずechoが実行される###<br />
uedambp:~ ueda$ ./hoge.bash <br />
do not stop<br />
[/bash]<br />
<br />
が、次のようにpipefailというオプションをセットしておくと（シバンの横には引数を一個しか渡せないと考えた方がよいので、下でsetを使って指定する）、次のように止まります。あらびっくり。<br />
<br />
[bash]<br />
uedambp:~ ueda$ cat pipefail.bash <br />
#!/bin/bash -e<br />
<br />
set -o pipefail<br />
<br />
false | true<br />
echo do not stop<br />
uedambp:~ ueda$ ./pipefail.bash <br />
uedambp:~ ueda$ &lt;- echoは実行されない<br />
[/bash]<br />
<br />
執筆する前にもうちょっとちゃんとmanをしっかり読んでおけよと自分に鋭いツッコミを入れましたが、bashの文法解説書というよりはコマンドの使い方解説書という感じで書いていたのでちょっと手薄になっておりました・・・。<br />
<br />
manにはこう書いてあります。（Linuxだとmanの出力はパイプに渡せます。）<br />
<br />
[bash]<br />
ueda\@ubuntu:~$ man bash 2&gt; /dev/null | grep -A 3 pipefail$<br />
 pipefail<br />
 設定されている場合、パイプラインの返り値は、 0 以外のステータスで終了した最後の<br />
 (一番右の) コマンドの値になります。 パイプラインの全てのコマンドが成功の状態で<br />
 終了すると 0 になります。 このオプションは、デフォルトで無効です。<br />
ueda\@ubuntu:~$ LANG=C man bash 2&gt; /dev/null | grep -A 3 pipefail$<br />
 pipefail<br />
 If set, the return value of a pipeline is the value of the last (rightmost)<br />
 command to exit with a non-zero status, or zero if all commands in the pipeline<br />
 exit successfully. This option is disabled by default.<br />
[/bash]<br />
<br />
<span style="color:red">しっかし、これ読んでも一回で正しい意味を読み取れるかどうか自信はありませぬ・・・。</span><br />
<br />
<h2>もうちょい補足</h2><br />
<br />
見落としに気づいたのは、やっぱりbashの場合、PIPESTATUSが実装されているんだからスクリプトを止める方があるんじゃないかということで、校了後に不安になっていろいろ調べているうちに上記カンニング先で「あっ！」となりました。<br />
<br />
「-eだと止まらないことがあるので自分で後始末は実装しましょう」みたいな文脈で-eを説明したのですが、pipefailがあるのでこれは知見の足らん説明となります。<br />
<br />
trapと組み合わると、後始末ができてしまいます・・・。<br />
<br />
[bash]<br />
uedambp:~ ueda$ cat pipefail_error.bash <br />
#!/bin/bash -e<br />
<br />
set -o pipefail<br />
<br />
error () {<br />
	echo &quot;ERROR&quot;<br />
	#うまくエラーをトラップできればhogeが消える###<br />
	rm hoge<br />
}<br />
<br />
#中間ファイルを作る###<br />
touch hoge<br />
<br />
trap error ERR<br />
<br />
false | true<br />
<br />
###これ以後は実行されない###<br />
echo do not stop<br />
[/bash]<br />
<br />
やってみましょう。<br />
<br />
[bash]<br />
uedambp:~ ueda$ ./pipefail_error.bash <br />
ERROR<br />
###ファイルが消えている###<br />
uedambp:~ ueda$ ls hoge<br />
gls: cannot access hoge: No such file or directory<br />
[/bash]<br />
<br />
ああああアホでした。自分で気がついてよかった。<br />
<br />
ということで、本書のシェルスクリプトが少し冗長ということが判明しましたが、シェルスクリプトよりワンライナーの方が圧倒的に多いのと、大半のスクリプトは書捨てなので、これを念頭に読んでいただければ大丈夫かと思います。<br />
<br />
<br />
以上。最後に宣伝。すんません・・・。<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4774173444" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
<br />
寝る。<br />

