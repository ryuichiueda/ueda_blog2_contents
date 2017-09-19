---
Keywords: エディタ,プログラミング,GlueLang,rumin,寝る,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# ruminとGlueLangについての日記
日曜月曜は研究そっちのけでGlueLangの実装をしていました。

GlueLangはさておき、某所でrubyでプラグインを書ける<a href="https://github.com/ncq/rumin" target="_blank">rumin</a>というmruby製のエディタを作っている人たちがいます。誰かは、このように広告付きのブログである等の理由から（といっても当然サーバ代にもならない稼ぎですが）言いませんが、通りすがりのフリーソフト好きとして、ruminを試してみようかと。

結論から言うと、俺の環境ではうごかんだお！これ見てたらちゃんと対応していただきたく。GlueLangはC++11のコンパイラさえあれば（そして最新ならば）MacでもLinuxでもちゃんと動くど。たぶん。

<!--more-->

日記なので、どんな風に動かなかったかメモしておく。日記なので、誤植は敢えて直さない。

<h1>とりあえずMacで動かしてみました動きませんデイsた</h1>

rubyは・・・入っている。この前、ちょっとしたシミュレーションをするために久しぶりに書いてみた。
```bash
uedambp:GIT ueda$ ruby -v
ruby 2.1.5p273 (2014-11-13 revision 48405) [x86_64-darwin14.0]
uedambp:~ ueda$ uname -a
Darwin uedambp.local 14.0.0 Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64 x86_64
```

んでgit clone。

```bash
uedambp:GIT ueda$ git clone https://github.com/ncq/rumin.git
Cloning into 'rumin'...
（略）
Checking connectivity... done.
```

はいはい。rakerake。

```bash
uedambp:GIT ueda$ cd rumin/
uedambp:rumin ueda$ rake
```

<span style="color:red">エラー出てやがる。</span>

```bash
Command failed with status (1): [clang -Iruntime/include src/rumin.c runtim...]
/Users/ueda/GIT/rumin/Rakefile:29:in `block in &lt;top (required)&gt;'
Tasks: TOP =&gt; default =&gt; build =&gt; rumin
(See full trace by running task with --trace)
```

しかしテストは通る。

```bash
uedambp:rumin ueda$ rake mtest
...
uedambp:rumin ueda$ echo $?
0
```

しかし何もbuildできない。

```bash
uedambp:rumin ueda$ cd build/
uedambp:build ueda$ ls
uedambp:build ueda$ 
```

<h1>次、Ubuntu</h1>

```bash
ueda\@remote:~$ uname -a
Linux remote 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

まずはrubyのインストールから。（そこからかよ。）
```bash
ueda\@remote:~$ sudo apt-get install ruby
```

くろーん。

```bash
ueda\@remote:~$ git clone https://github.com/ncq/rumin.git
...
```

はいはい。rakerake。

```bash
ueda\@remote:~$ cd rumin/
ueda\@remote:~/rumin$ rake
プログラム 'rake' はまだインストールされていません。 次のように入力することでインストールできます:
sudo apt-get install rake
ueda\@remote:~/rumin$ sudo apt-get install rake
ueda\@remote:~/rumin$ rake
...
fatal: destination path 'runtime' already exists and is not an empty directory.
rake aborted!
Command failed with status (128): [git clone https://github.com/mruby/mruby.g...]
/home/ueda/rumin/Rakefile:10:in `block in &lt;top (required)&gt;'
Tasks: TOP =&gt; default =&gt; mruby
(See full trace by running task with --trace)
```

・・・ダメか・・・。<span style="color:red">なんとかしてくだあらい！！！</span>

プラグインが最新の言語で書けるというのはvimmerの私からは非常に魅力的に映るので、もうちょっと体裁は整えたいところ。しかし、外のライブラリをたくさん使うとなかなか大変なんだよなあ。だからコマンドとシェルスクリプトでモボモボgコ・・・

それから、周囲の方は生暖かく見守っていただきたく。できれば助けていただきたく。


<h1>今週末のGlueLang作業日誌</h1>

では次。ちゃんと動くやつ。次世代シェルスクリプティング言語（？）GlueLangはとうとうbashの関数に相当するものが実装できました。また、<a href="http://blog.ueda.asia/?p=4884" title="glueで年末年始シェル芸問題集を解いた雑感（Q4まで）" target="_blank">この事態</a>を受けてコマンドのオプションの一部はシングルクォートを省略できるようにしました。具体的にはこんな感じ。

```bash
uedambp:GlueLang ueda$ cat hoge.glue 
import /bin/ as b

###procに処理を書くと子供のプロセスで動く###
proc turn90 =
 import /usr/bin/ as ub
 ub.rev &gt;&gt;= ub.grep -o '.' #-oにクォート不要

###インデントの終わりがprocの終わり###
b.echo 'ウコンの力' &gt;&gt;= this.turn90
```

procについては、proc <名前> = の後ろにインデントつきで処理を書くと、インデントを取り去って中間ファイルに保存し、別のglueを立ち上げてそいつにファイルを渡して処理させるという、超手抜きな実装になってます。外から突っつかれたら弱いのですが、ある意味UNIXらしい潔さがあるとも言え。proc宣言の次の行のインデントの数をオフサイドラインにしています。

実行。

```bash
uedambp:GlueLang ueda$ ./glue hoge.glue 
力
の
ン
コ
ウ
```

問題は親のimportをまだ子に渡す処理を書いていないということで、これは環境変数使わんといかんのかなとか、ファイルで渡してやればよいかとか、いろいろ考えてます。おそらく環境変数になると思われます。

procに引数を渡すために、後回しにしていた引数の読み取りも実装しました。やっぱり自分は$1, $2, ...とかよりargv[1], argv[2], ...と書くほうが好きなのでとりあえずそのようにしましたが、別の案もあってしかるべきかと。

```bash
uedambp:GlueLang ueda$ cat hoge.glue 
/bin/echo argv[2] argv[3] argv[1]
uedambp:GlueLang ueda$ ./glue hoge.glue う こ ん
こ ん う
```

それから、こんな書き方もできるようにしました。複数のコマンドの出力を一つのファイルや文字列に叩き込むためのもので、bashだと{}や()で書く複合コマンドに相当します。Haskellからヒントを得ました。

```bash
uedambp:GlueLang ueda$ cat hoge.glue 
import /bin/ as b

###echoを「&gt;&gt;」でつなぐ###
str mojiretu = b.echo 'お前は' &gt;&gt; b.echo 'もう' &gt;&gt; b.echo 'すでに' &gt;&gt; b.echo '死んでいる'

b.echo mojiretu
###実行###
uedambp:GlueLang ueda$ ./glue hoge.glue 
お前は
もう
すでに
死んでいる
```

しかし、おそらくstrに関しては次のような書き方もできるようにしないといけないでしょう。今まで全部コマンドに任せっきりだった文字列処理を独自に実装しようかなと。これはbashよりも充実したいところです。

```bash
###Haskell風###
str mojiretu = unlines ['お前は', 'もう', 'すでに', '死んでいる']
###あるいはPython風（文法的に無理？？？）###
str mojiretu = '¥n'.join ['お前は', 'もう', 'すでに', '死んでいる']
```

明日からは平日なので、GlueLangについてはまた来週末に。


寝る。
