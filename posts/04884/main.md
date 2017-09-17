# glueで年末年始シェル芸問題集を解いた雑感（Q4まで）
私以外のコントリビュータも出現し、<a href="http://cordea.hatenadiary.com/entry/2015/01/09/160647" target="_blank">試してくださる方</a>も出て引くに引けない状況の<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>ですが、ちょっと使った例と、自分で使ってみたフィードバックが必要かなと思い、自分で出題した<a href="http://blog.ueda.asia/?p=4821" title="【解答】年末年始シェル芸問題集" target="_blank">年末年始シェル芸問題集</a>の問題をGlueLangで解いてみようと思いました。<br />
<br />
答えはMac用です。<br />
<br />
<h1>Q1</h1><br />
<br />
今のところPATHをGlueLangに読ませていないので、コマンドを使うときはimportでパスを指定するか、フルパスで呼び出す必要がありますが、xargsに渡したgmd5sumではフルパスでしか指定できない問題が発覚（というよりウスウス気づいてましたが・・・）。あとはオプションをいちいちシングルクォートするのはやはり面倒かなと。<br />
<br />
あとは、importの後の空行にスペースを入れるとちゃんとパースしてくれませんね・・・。<br />
<br />
[hs]<br />
import /usr/bin/ as ub<br />
import /usr/local/bin/ as ulb<br />
<br />
ub.find '/Users/ueda/' '-type' 'f' &gt;&gt;=<br />
ub.grep '-i' '\\.jpg$' &gt;&gt;=<br />
ub.sed 's/.*/&quot;&amp;&quot;/' &gt;&gt;=<br />
ub.xargs '-n' '1' '/usr/local/bin/gmd5sum' &gt;&gt;=<br />
ub.sort '-s' '-k1,1' &gt;&gt;=<br />
ulb.awk '{if(a==$1){print b;print $0}a=$1;b=$0}'<br />
[/hs]<br />
<br />
パスやその他環境変数については、<br />
<br />
[hs]<br />
import PATH<br />
import LANG<br />
[/hs]<br />
<br />
というように簡単に読み込めるようにしようかと思います。<br />
<br />
オプションについてはハイフンで始まったり数字で始まるものはクォートを省略できる方がいいかも。<br />
<br />
<br />
<h1>Q2</h1><br />
<br />
ワンライナーなのでほとんど普通のシェルスクリプトと変わりません。しかし、標準エラー出力の制御を今のところ実装していないというのはやはり使いづらい。<br />
<br />
[hs]<br />
import /usr/local/bin/ as ulb<br />
import /usr/bin/ as ub<br />
<br />
ub.curl 'http://www.flightradar24.com/_json/airports.php' &gt;&gt;=<br />
ulb.jq '.' &gt;&gt;= ub.grep '-C' '6' 'HND'<br />
[/hs]<br />
<br />
エラーは普通にリダイレクトでとれるようにしておけば良いか・・・。次のような感じで。<br />
[hs]<br />
ub.curl 'http://www.flightradar24.com/_json/airports.php' log&gt; '/dev/null' &gt;&gt;= ...<br />
[/hs]<br />
<br />
ログを見るだけなら上の書式にして、標準エラー出力をGlueLang内で積極的に使うときは、fileの後に二つファイルを並べる方式になると思います。<br />
[hs]<br />
# ファイルオブジェクトfにcurlの標準出力、errにエラー出力が入る<br />
file f err = ub.curl 'http://www.flightradar24.com/_json/airports.php'<br />
[/hs]<br />
<br />
<h1>Q3</h1><br />
<br />
基本的にはワンライナーをGlueLangの方法に書き換えるだけです。<br />
<br />
[hs]<br />
import /usr/local/bin/ as ulb<br />
import /usr/bin/ as ub<br />
<br />
ub.seq '1' '1000' &gt;&gt;=<br />
ulb.awk '{for(i=1;i&lt;=$1;i++){printf(&quot;%d &quot;,i)}{print &quot;&quot;}}' &gt;&gt;=<br />
ub.tr ' ' '*' &gt;&gt;=<br />
ub.sed 's/\\*$/)/' &gt;&gt;=<br />
ub.sed 's:^:1/(:' &gt;&gt;=<br />
ub.bc '-l' &gt;&gt;= <br />
ub.tr '\\n' '+' &gt;&gt;=<br />
ub.sed 's/$/1/' &gt;&gt;=<br />
ub.bc '-l' <br />
[/hs]<br />
<br />
しかし、もとがワンライナーなので意味不明なのは、GlueLangの宣伝としてはどうなのか？？<br />
<br />
<br />
ということで、別解をいただきましたので、実装してみたいと思います。<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>2015!の階乗はいろいろ試したけど、結局これだけで済むようだ。<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> $ clisp -x &#39;(! 2015)&#39; -q</p>&mdash; 本名 (\@tamago_girai) <a href="https://twitter.com/tamago_girai/status/551668213277138945">January 4, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
はい。<br />
<br />
[hs]<br />
/usr/local/bin/clisp '-x' '(! 2015)' '-q'<br />
[/hs]<br />
<br />
<h1>Q4</h1><br />
<br />
このbashのワンライナーを書き直せばよいのですが・・・<br />
<br />
[bash]<br />
uedambp:~ ueda$ a=$(curl http://blog.ueda.asia/misc/message2015.txt) ; <br />
while a=$(echo $a | base64 -D) &amp;&amp; echo $a ; do : ; done<br />
[/bash]<br />
<br />
・・・さて、whileがないGlueLangでどうやって処理しよう・・・。コマンド作っちゃえ。ということで、次のようなGlueLang用のコマンドを作りました。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat ./stdcom/loop-serial <br />
#!/bin/bash<br />
# loopserial command<br />
# usage: loopserial &lt;commmand&gt; &lt;args...&gt;<br />
# Multiapply trys the command until the command<br />
# is failed, and outputs the output of the last successful trial.<br />
<br />
# version: &quot;Sat Jan 10 16:58:28 JST 2015&quot;<br />
<br />
# This command should be rewritten with C/C++.<br />
<br />
[ &quot;$#&quot; -lt 1 ] &amp;&amp; exit 1<br />
<br />
tmp=/tmp/$$<br />
&quot;$\@&quot; &gt; $tmp-keep<br />
<br />
while [ $? -eq 0 ] ; do<br />
	mv $tmp-keep $tmp-out<br />
	cat $tmp-out | &quot;$\@&quot; &gt; $tmp-keep 2&gt; /dev/null<br />
done<br />
<br />
cat $tmp-out<br />
<br />
rm -f $tmp-*<br />
exit 0<br />
[/bash]<br />
<br />
んで、Glueで使ってみます。<br />
<br />
[hs]<br />
uedambp:SHELL_GEI_2015SP ueda$ cat Q4.mac.glue <br />
import /usr/bin/ as ub<br />
import /bin/ as b<br />
import /Users/ueda/GIT/GlueLang/stdcom/ as std<br />
<br />
ub.curl 'http://blog.ueda.asia/misc/message2015.txt' &gt;&gt;=<br />
std.loop-serial '/usr/bin/base64' '-D'<br />
[/hs]<br />
<br />
はい実行。<br />
<br />
[hs]<br />
uedambp:SHELL_GEI_2015SP ueda$ ../../glue Q4.mac.glue 2&gt; /dev/null<br />
:(){: | : &amp;};:<br />
[/hs]<br />
<br />
bashで書いているコマンドを実行していることで他力本願極まりないですが、bashで書いたコマンドをCで書き直して、GlueLangの付属コマンドにしてしまうつもりです。GlueLangを作るにあたり、もともと制御構文をなくしたいという動機があったので、これでいいんでないかと思います。<br />
<br />
ただ、whileがないと初心者向けにはならないので、ゆくゆくは実装するつもりです。しかし、コマンドを繰り返し実行するパターンにはあまりバリエーションがないので、loop-serialのようなコマンドをいくつか作ってそっちを使うことを推奨したいと考えています。<br />
<br />
 <h1>おわりに</h1><br />
<br />
今回は4問しか解きませんでしたが、これだけでも改善点がいろいろ出てきたので、開発に移りたいと思います・・・。やっぱりPATH周りは早くなんとかしたいかなと。<br />
<br />
<br />
おしまい。
