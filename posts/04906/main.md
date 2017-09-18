---
Keywords:エディタ,プログラミング,GlueLang,rumin,寝る,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---
# ruminとGlueLangについての日記
日曜月曜は研究そっちのけでGlueLangの実装をしていました。<br />
<br />
GlueLangはさておき、某所でrubyでプラグインを書ける<a href="https://github.com/ncq/rumin" target="_blank">rumin</a>というmruby製のエディタを作っている人たちがいます。誰かは、このように広告付きのブログである等の理由から（といっても当然サーバ代にもならない稼ぎですが）言いませんが、通りすがりのフリーソフト好きとして、ruminを試してみようかと。<br />
<br />
結論から言うと、俺の環境ではうごかんだお！これ見てたらちゃんと対応していただきたく。GlueLangはC++11のコンパイラさえあれば（そして最新ならば）MacでもLinuxでもちゃんと動くど。たぶん。<br />
<br />
<!--more--><br />
<br />
日記なので、どんな風に動かなかったかメモしておく。日記なので、誤植は敢えて直さない。<br />
<br />
<h1>とりあえずMacで動かしてみました動きませんデイsた</h1><br />
<br />
rubyは・・・入っている。この前、ちょっとしたシミュレーションをするために久しぶりに書いてみた。<br />
[bash]<br />
uedambp:GIT ueda$ ruby -v<br />
ruby 2.1.5p273 (2014-11-13 revision 48405) [x86_64-darwin14.0]<br />
uedambp:~ ueda$ uname -a<br />
Darwin uedambp.local 14.0.0 Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64 x86_64<br />
[/bash]<br />
<br />
んでgit clone。<br />
<br />
[bash]<br />
uedambp:GIT ueda$ git clone https://github.com/ncq/rumin.git<br />
Cloning into 'rumin'...<br />
（略）<br />
Checking connectivity... done.<br />
[/bash]<br />
<br />
はいはい。rakerake。<br />
<br />
[bash]<br />
uedambp:GIT ueda$ cd rumin/<br />
uedambp:rumin ueda$ rake<br />
[/bash]<br />
<br />
<span style="color:red">エラー出てやがる。</span><br />
<br />
[bash]<br />
Command failed with status (1): [clang -Iruntime/include src/rumin.c runtim...]<br />
/Users/ueda/GIT/rumin/Rakefile:29:in `block in &lt;top (required)&gt;'<br />
Tasks: TOP =&gt; default =&gt; build =&gt; rumin<br />
(See full trace by running task with --trace)<br />
[/bash]<br />
<br />
しかしテストは通る。<br />
<br />
[bash]<br />
uedambp:rumin ueda$ rake mtest<br />
...<br />
uedambp:rumin ueda$ echo $?<br />
0<br />
[/bash]<br />
<br />
しかし何もbuildできない。<br />
<br />
[bash]<br />
uedambp:rumin ueda$ cd build/<br />
uedambp:build ueda$ ls<br />
uedambp:build ueda$ <br />
[/bash]<br />
<br />
<h1>次、Ubuntu</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ uname -a<br />
Linux remote 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux<br />
[/bash]<br />
<br />
まずはrubyのインストールから。（そこからかよ。）<br />
[bash]<br />
ueda\@remote:~$ sudo apt-get install ruby<br />
[/bash]<br />
<br />
くろーん。<br />
<br />
[bash]<br />
ueda\@remote:~$ git clone https://github.com/ncq/rumin.git<br />
...<br />
[/bash]<br />
<br />
はいはい。rakerake。<br />
<br />
[bash]<br />
ueda\@remote:~$ cd rumin/<br />
ueda\@remote:~/rumin$ rake<br />
プログラム 'rake' はまだインストールされていません。 次のように入力することでインストールできます:<br />
sudo apt-get install rake<br />
ueda\@remote:~/rumin$ sudo apt-get install rake<br />
ueda\@remote:~/rumin$ rake<br />
...<br />
fatal: destination path 'runtime' already exists and is not an empty directory.<br />
rake aborted!<br />
Command failed with status (128): [git clone https://github.com/mruby/mruby.g...]<br />
/home/ueda/rumin/Rakefile:10:in `block in &lt;top (required)&gt;'<br />
Tasks: TOP =&gt; default =&gt; mruby<br />
(See full trace by running task with --trace)<br />
[/bash]<br />
<br />
・・・ダメか・・・。<span style="color:red">なんとかしてくだあらい！！！</span><br />
<br />
プラグインが最新の言語で書けるというのはvimmerの私からは非常に魅力的に映るので、もうちょっと体裁は整えたいところ。しかし、外のライブラリをたくさん使うとなかなか大変なんだよなあ。だからコマンドとシェルスクリプトでモボモボgコ・・・<br />
<br />
それから、周囲の方は生暖かく見守っていただきたく。できれば助けていただきたく。<br />
<br />
<br />
<h1>今週末のGlueLang作業日誌</h1><br />
<br />
では次。ちゃんと動くやつ。次世代シェルスクリプティング言語（？）GlueLangはとうとうbashの関数に相当するものが実装できました。また、<a href="http://blog.ueda.asia/?p=4884" title="glueで年末年始シェル芸問題集を解いた雑感（Q4まで）" target="_blank">この事態</a>を受けてコマンドのオプションの一部はシングルクォートを省略できるようにしました。具体的にはこんな感じ。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
import /bin/ as b<br />
<br />
###procに処理を書くと子供のプロセスで動く###<br />
proc turn90 =<br />
 import /usr/bin/ as ub<br />
 ub.rev &gt;&gt;= ub.grep -o '.' #-oにクォート不要<br />
<br />
###インデントの終わりがprocの終わり###<br />
b.echo 'ウコンの力' &gt;&gt;= this.turn90<br />
[/bash]<br />
<br />
procについては、proc <名前> = の後ろにインデントつきで処理を書くと、インデントを取り去って中間ファイルに保存し、別のglueを立ち上げてそいつにファイルを渡して処理させるという、超手抜きな実装になってます。外から突っつかれたら弱いのですが、ある意味UNIXらしい潔さがあるとも言え。proc宣言の次の行のインデントの数をオフサイドラインにしています。<br />
<br />
実行。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ ./glue hoge.glue <br />
力<br />
の<br />
ン<br />
コ<br />
ウ<br />
[/bash]<br />
<br />
問題は親のimportをまだ子に渡す処理を書いていないということで、これは環境変数使わんといかんのかなとか、ファイルで渡してやればよいかとか、いろいろ考えてます。おそらく環境変数になると思われます。<br />
<br />
procに引数を渡すために、後回しにしていた引数の読み取りも実装しました。やっぱり自分は$1, $2, ...とかよりargv[1], argv[2], ...と書くほうが好きなのでとりあえずそのようにしましたが、別の案もあってしかるべきかと。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
/bin/echo argv[2] argv[3] argv[1]<br />
uedambp:GlueLang ueda$ ./glue hoge.glue う こ ん<br />
こ ん う<br />
[/bash]<br />
<br />
それから、こんな書き方もできるようにしました。複数のコマンドの出力を一つのファイルや文字列に叩き込むためのもので、bashだと{}や()で書く複合コマンドに相当します。Haskellからヒントを得ました。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
import /bin/ as b<br />
<br />
###echoを「&gt;&gt;」でつなぐ###<br />
str mojiretu = b.echo 'お前は' &gt;&gt; b.echo 'もう' &gt;&gt; b.echo 'すでに' &gt;&gt; b.echo '死んでいる'<br />
<br />
b.echo mojiretu<br />
###実行###<br />
uedambp:GlueLang ueda$ ./glue hoge.glue <br />
お前は<br />
もう<br />
すでに<br />
死んでいる<br />
[/bash]<br />
<br />
しかし、おそらくstrに関しては次のような書き方もできるようにしないといけないでしょう。今まで全部コマンドに任せっきりだった文字列処理を独自に実装しようかなと。これはbashよりも充実したいところです。<br />
<br />
[bash]<br />
###Haskell風###<br />
str mojiretu = unlines ['お前は', 'もう', 'すでに', '死んでいる']<br />
###あるいはPython風（文法的に無理？？？）###<br />
str mojiretu = '¥n'.join ['お前は', 'もう', 'すでに', '死んでいる']<br />
[/bash]<br />
<br />
明日からは平日なので、GlueLangについてはまた来週末に。<br />
<br />
<br />
寝る。
