---
Keywords: ごめんなさい,bash,Linux,Mac,pipefail,ご報告,シェルプログラミング実用テクニック,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# bashのpipefailで確実にスクリプトを止める
<a href="http://gihyo.jp/book/2015/978-4-7741-7344-3" title="シェルプログラミング実用テクニックの目次が公開されました（エクシェル芸、斉藤さん、and 鳩）" target="_blank">シェルプログラミング実用テクニック</a>、出版される前からもう補足ですが、私めがbashのpipefailというオプションをすっかり見落としていたのでフォローしておきます。

<ul>
 <li>カンニング先: <a href="http://d.hatena.ne.jp/iww/20130409/pipefail">パイプの途中のエラーを取る | 揮発性のメモ</a></li>
</ul>

本文ではbashに-e（エラーがあったら止める）をつけてもパイプラインの左側のコマンドにエラーがあったときに処理が止まらないと書きました。

例です。

<!--more-->

```bash
###false | true###でfalseが終了ステータス1を返すが・・・###
uedambp:~ ueda$ cat hoge.bash 
#!/bin/bash -e

false | true
echo do not stop
###-eがあるにもかかわらずechoが実行される###
uedambp:~ ueda$ ./hoge.bash 
do not stop
```

が、次のようにpipefailというオプションをセットしておくと（シバンの横には引数を一個しか渡せないと考えた方がよいので、下でsetを使って指定する）、次のように止まります。あらびっくり。

```bash
uedambp:~ ueda$ cat pipefail.bash 
#!/bin/bash -e

set -o pipefail

false | true
echo do not stop
uedambp:~ ueda$ ./pipefail.bash 
uedambp:~ ueda$ <- echoは実行されない
```

執筆する前にもうちょっとちゃんとmanをしっかり読んでおけよと自分に鋭いツッコミを入れましたが、bashの文法解説書というよりはコマンドの使い方解説書という感じで書いていたのでちょっと手薄になっておりました・・・。

manにはこう書いてあります。（Linuxだとmanの出力はパイプに渡せます。）

```bash
ueda\@ubuntu:~$ man bash 2&gt; /dev/null | grep -A 3 pipefail$
 pipefail
 設定されている場合、パイプラインの返り値は、 0 以外のステータスで終了した最後の
 (一番右の) コマンドの値になります。 パイプラインの全てのコマンドが成功の状態で
 終了すると 0 になります。 このオプションは、デフォルトで無効です。
ueda\@ubuntu:~$ LANG=C man bash 2&gt; /dev/null | grep -A 3 pipefail$
 pipefail
 If set, the return value of a pipeline is the value of the last (rightmost)
 command to exit with a non-zero status, or zero if all commands in the pipeline
 exit successfully. This option is disabled by default.
```

<span style="color:red">しっかし、これ読んでも一回で正しい意味を読み取れるかどうか自信はありませぬ・・・。</span>

<h2>もうちょい補足</h2>

見落としに気づいたのは、やっぱりbashの場合、PIPESTATUSが実装されているんだからスクリプトを止める方があるんじゃないかということで、校了後に不安になっていろいろ調べているうちに上記カンニング先で「あっ！」となりました。

「-eだと止まらないことがあるので自分で後始末は実装しましょう」みたいな文脈で-eを説明したのですが、pipefailがあるのでこれは知見の足らん説明となります。

trapと組み合わると、後始末ができてしまいます・・・。

```bash
uedambp:~ ueda$ cat pipefail_error.bash 
#!/bin/bash -e

set -o pipefail

error () {
	echo &quot;ERROR&quot;
	#うまくエラーをトラップできればhogeが消える###
	rm hoge
}

#中間ファイルを作る###
touch hoge

trap error ERR

false | true

###これ以後は実行されない###
echo do not stop
```

やってみましょう。

```bash
uedambp:~ ueda$ ./pipefail_error.bash 
ERROR
###ファイルが消えている###
uedambp:~ ueda$ ls hoge
gls: cannot access hoge: No such file or directory
```

ああああアホでした。自分で気がついてよかった。

ということで、本書のシェルスクリプトが少し冗長ということが判明しましたが、シェルスクリプトよりワンライナーの方が圧倒的に多いのと、大半のスクリプトは書捨てなので、これを念頭に読んでいただければ大丈夫かと思います。


以上。最後に宣伝。すんません・・・。

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4774173444" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>


寝る。

