---
Keywords: コマンド,glue,GlueLang,シェル芸,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# glueで年末年始シェル芸問題集を解いた雑感（Q4まで）
私以外のコントリビュータも出現し、<a href="http://cordea.hatenadiary.com/entry/2015/01/09/160647" target="_blank">試してくださる方</a>も出て引くに引けない状況の<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>ですが、ちょっと使った例と、自分で使ってみたフィードバックが必要かなと思い、自分で出題した<a href="http://blog.ueda.asia/?p=4821" title="【解答】年末年始シェル芸問題集" target="_blank">年末年始シェル芸問題集</a>の問題をGlueLangで解いてみようと思いました。

答えはMac用です。

<h1>Q1</h1>

今のところPATHをGlueLangに読ませていないので、コマンドを使うときはimportでパスを指定するか、フルパスで呼び出す必要がありますが、xargsに渡したgmd5sumではフルパスでしか指定できない問題が発覚（というよりウスウス気づいてましたが・・・）。あとはオプションをいちいちシングルクォートするのはやはり面倒かなと。

あとは、importの後の空行にスペースを入れるとちゃんとパースしてくれませんね・・・。

```hs
import /usr/bin/ as ub
import /usr/local/bin/ as ulb

ub.find '/Users/ueda/' '-type' 'f' &gt;&gt;=
ub.grep '-i' '\\.jpg$' &gt;&gt;=
ub.sed 's/.*/&quot;&amp;&quot;/' &gt;&gt;=
ub.xargs '-n' '1' '/usr/local/bin/gmd5sum' &gt;&gt;=
ub.sort '-s' '-k1,1' &gt;&gt;=
ulb.awk '{if(a==$1){print b;print $0}a=$1;b=$0}'
```

パスやその他環境変数については、

```hs
import PATH
import LANG
```

というように簡単に読み込めるようにしようかと思います。

オプションについてはハイフンで始まったり数字で始まるものはクォートを省略できる方がいいかも。


<h1>Q2</h1>

ワンライナーなのでほとんど普通のシェルスクリプトと変わりません。しかし、標準エラー出力の制御を今のところ実装していないというのはやはり使いづらい。

```hs
import /usr/local/bin/ as ulb
import /usr/bin/ as ub

ub.curl 'http://www.flightradar24.com/_json/airports.php' &gt;&gt;=
ulb.jq '.' &gt;&gt;= ub.grep '-C' '6' 'HND'
```

エラーは普通にリダイレクトでとれるようにしておけば良いか・・・。次のような感じで。
```hs
ub.curl 'http://www.flightradar24.com/_json/airports.php' log&gt; '/dev/null' &gt;&gt;= ...
```

ログを見るだけなら上の書式にして、標準エラー出力をGlueLang内で積極的に使うときは、fileの後に二つファイルを並べる方式になると思います。
```hs

# ファイルオブジェクトfにcurlの標準出力、errにエラー出力が入る
file f err = ub.curl 'http://www.flightradar24.com/_json/airports.php'
```

<h1>Q3</h1>

基本的にはワンライナーをGlueLangの方法に書き換えるだけです。

```hs
import /usr/local/bin/ as ulb
import /usr/bin/ as ub

ub.seq '1' '1000' &gt;&gt;=
ulb.awk '{for(i=1;i<=$1;i++){printf(&quot;%d &quot;,i)}{print &quot;&quot;}}' &gt;&gt;=
ub.tr ' ' '*' &gt;&gt;=
ub.sed 's/\\*$/)/' &gt;&gt;=
ub.sed 's:^:1/(:' &gt;&gt;=
ub.bc '-l' &gt;&gt;= 
ub.tr '\\n' '+' &gt;&gt;=
ub.sed 's/$/1/' &gt;&gt;=
ub.bc '-l' 
```

しかし、もとがワンライナーなので意味不明なのは、GlueLangの宣伝としてはどうなのか？？


ということで、別解をいただきましたので、実装してみたいと思います。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>2015!の階乗はいろいろ試したけど、結局これだけで済むようだ。<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> $ clisp -x &#39;(! 2015)&#39; -q</p>&mdash; 本名 (\@tamago_girai) <a href="https://twitter.com/tamago_girai/status/551668213277138945">January 4, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

はい。

```hs
/usr/local/bin/clisp '-x' '(! 2015)' '-q'
```

<h1>Q4</h1>

このbashのワンライナーを書き直せばよいのですが・・・

```bash
uedambp:~ ueda$ a=$(curl http://blog.ueda.asia/misc/message2015.txt) ; 
while a=$(echo $a | base64 -D) &amp;&amp; echo $a ; do : ; done
```

・・・さて、whileがないGlueLangでどうやって処理しよう・・・。コマンド作っちゃえ。ということで、次のようなGlueLang用のコマンドを作りました。

```bash
uedambp:GlueLang ueda$ cat ./stdcom/loop-serial 
#!/bin/bash

# loopserial command

# usage: loopserial <commmand&gt; <args...&gt;

# Multiapply trys the command until the command

# is failed, and outputs the output of the last successful trial.


# version: &quot;Sat Jan 10 16:58:28 JST 2015&quot;


# This command should be rewritten with C/C++.

[ &quot;$#&quot; -lt 1 ] &amp;&amp; exit 1

tmp=/tmp/$$
&quot;$\@&quot; &gt; $tmp-keep

while [ $? -eq 0 ] ; do
	mv $tmp-keep $tmp-out
	cat $tmp-out | &quot;$\@&quot; &gt; $tmp-keep 2&gt; /dev/null
done

cat $tmp-out

rm -f $tmp-*
exit 0
```

んで、Glueで使ってみます。

```hs
uedambp:SHELL_GEI_2015SP ueda$ cat Q4.mac.glue 
import /usr/bin/ as ub
import /bin/ as b
import /Users/ueda/GIT/GlueLang/stdcom/ as std

ub.curl 'http://blog.ueda.asia/misc/message2015.txt' &gt;&gt;=
std.loop-serial '/usr/bin/base64' '-D'
```

はい実行。

```hs
uedambp:SHELL_GEI_2015SP ueda$ ../../glue Q4.mac.glue 2&gt; /dev/null
:(){: | : &amp;};:
```

bashで書いているコマンドを実行していることで他力本願極まりないですが、bashで書いたコマンドをCで書き直して、GlueLangの付属コマンドにしてしまうつもりです。GlueLangを作るにあたり、もともと制御構文をなくしたいという動機があったので、これでいいんでないかと思います。

ただ、whileがないと初心者向けにはならないので、ゆくゆくは実装するつもりです。しかし、コマンドを繰り返し実行するパターンにはあまりバリエーションがないので、loop-serialのようなコマンドをいくつか作ってそっちを使うことを推奨したいと考えています。

 <h1>おわりに</h1>

今回は4問しか解きませんでしたが、これだけでも改善点がいろいろ出てきたので、開発に移りたいと思います・・・。やっぱりPATH周りは早くなんとかしたいかなと。


おしまい。
