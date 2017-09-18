---
Keywords: シェルスクリプト,GlueLang,研究,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# 煽られるように開発中の言語（Glue）について説明・・・
あわわわわ。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p><a href="https://twitter.com/okapies">\@okapies</a> 外部コマンドを起動しなくてもいい、マルチコア対応のシェルスクリプトを想定しています。ログ解析とかテキスト加工とか。</p>&mdash; Yukihiro Matsumoto (\@yukihiro_matz) <a href="https://twitter.com/yukihiro_matz/status/543059740473831424">2014, 12月 11</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
引用するのも何か申し訳ないのですが、ここ数日この件で2,3人の方から感想を求められたので、感想を・・・。<br />
<br />
<!--more--><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>なるほど</p>&mdash; Ryuichi UEDA (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/544363059586678784">2014, 12月 15</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
アホ丸出しです。でも、なるほどです。「そういう解釈になるのかー」と。<br />
<br />
<h2>私もホソボソと・・・</h2><br />
<br />
言語を作っております。実は<a href="http://blog.ueda.asia/?p=2058" title="36歳の誕生日にグルー言語作る宣言をせざるを得なくなった">「36歳の誕生日にグルー言語作る宣言をせざるを得なくなった」</a>ということがありまして、作っております。「ある人」が誰かは・・・推して知るべしです。ちゃんと書けばいいのですが、どうも北陸の人間特有の引っ込み思案があり、ブログというものでインタラクションするのが失礼なのではないかと気が引け・・・。その割に人のツイートを引用してますが・・・。<br />
<br />
<a href="https://github.com/ryuichiueda/GlueLang/tree/master/PROTOTYPE" target="_blank">https://github.com/ryuichiueda/GlueLang/tree/master/PROTOTYPE</a><br />
<br />
んで、現在の状況ですが、大学にこの件で紀要を書いて一旦ストップし、ロボットの方の研究をしています。これは決して消極的な理由と捉えていただきたくないのですが、こちらでもやりたいことだらけで・・・。年度内にはもう一度、まとまった日数を費やそうと考えています。<br />
<br />
ただ、紀要を書いて満足してインターネット上に何も公表していなかったので、この際何をしているのかを書いておこうと思います。私個人がこのような状況なので、考え方だけでも何か貢献できないかと。<br />
<br />
<h2>なぜ新言語か</h2><br />
<br />
コアが増えるとパイプライン処理が簡単に書けるようにしないといろいろ面倒で、ただ既存の言語だとパイプライン処理を持ち込むと異物感が甚だしいので、どうしても新しい言語を作るという発想になります。シェルも、インタラクティブ性が重視されすぎていて言語としては弱いので、新しいもの、という発想になります。ということで新言語を作り出しました。私がちゃんと作り切ることができるかどうかは分からないのですが、そういう発想には確信を持っています。<br />
<br />
<br />
私の場合は言語の解釈以外のものを全て外部コマンドに任せてしまおうという考えでやっているので、たぶんMatzさんの<a href="https://github.com/matz/streem" target="_blank">Streem</a>とは直交する、すなわち用途が一緒のようで違ったものになると思います。ということで、言語といっても私の場合はシェルを作ることになります。最近もdashのコードのパーサの部分を読んでいますが、なかなか手ごわく・・・。<br />
<br />
<h2>とりあえず何を作ったか。</h2><br />
<br />
次のようなコードを入力すると・・・<br />
<br />
[hs]<br />
import /bin/ as b<br />
import /usr/bin/ as ub<br />
<br />
proc main file:<br />
	file f = cattac $file<br />
	b.cat $f<br />
<br />
func cattac file:<br />
	b.cat $file<br />
	ub.tail -r<br />
[/hs]<br />
<br />
次のようなbashのコードに変換して実行するトランスレータを作ったところです。<br />
<br />
[bash]<br />
ERROR_EXIT(){<br />
	rm -f /tmp/$$-*<br />
	exit 1<br />
}<br />
<br />
ERROR_CHECK(){<br />
	[ &quot;$(tr -d ' 0' &lt;&lt;&lt; ${PIPESTATUS[\@]})&quot; = &quot;&quot; ] &amp;&amp; return<br />
	ERROR_EXIT<br />
}<br />
<br />
trap ERROR_EXIT 1 2 3 15<br />
<br />
foreach(){<br />
<br />
	while read line ; do<br />
		&quot;$1&quot; $line<br />
		ERROR_CHECK<br />
	done<br />
}<br />
<br />
cattac(){<br />
/bin/cat $1 | /usr/bin/tail -r<br />
	ERROR_CHECK<br />
}<br />
<br />
main(){<br />
	f=$(mktemp /tmp/$$-f)<br />
ERROR_CHECK<br />
 cattac $1 &gt; $f<br />
ERROR_CHECK<br />
<br />
	/bin/cat $f<br />
ERROR_CHECK<br />
<br />
}<br />
<br />
main &quot;$1&quot;<br />
ERROR_CHECK<br />
<br />
rm -f /tmp/$$-*<br />
[/bash]<br />
<br />
やっていることは簡単で、単に「cat | tail -r」をしているだけです。<br />
<br />
ちょっと動かしてみます。「./glue SAMPLE_SCRIPTS/io.glue」が変換前のスクリプトで、内部でbashに変換されて実行されます。（久しぶりに動かすので、ドキドキしましたがちゃんと動きました。）<br />
<br />
[bash]<br />
uedambp:PROTOTYPE ueda$ seq 5 | ./glue SAMPLE_SCRIPTS/io.glue<br />
5<br />
4<br />
3<br />
2<br />
1<br />
[/bash]<br />
<br />
<br />
<h2>仕様等</h2><br />
<br />
もう一度、新言語のスクリプトを示します。だいたいこのコードにやりたいことが凝縮されています。<br />
<br />
<br />
[hs]<br />
import /bin/ as b<br />
import /usr/bin/ as ub<br />
<br />
proc main file:<br />
	file f = cattac $file<br />
	b.cat $f<br />
<br />
func cattac file:<br />
	b.cat $file<br />
	ub.tail -r<br />
[/hs]<br />
<br />
<h3>PATHに代わるimport</h3><br />
<br />
まず、importですが、これはPATHに代わる仕組みです。この例では、/bin/下のコマンドに「b.」、/usr/bin/下のコマンドに「ub.」とつけています。これは移植性の改善を狙ってのことで、将来的には<br />
<br />
[hs]<br />
import /usr/local/bin/posix/ as posix<br />
[/hs]<br />
<br />
というように、「移植性が本当に必要ならばPOSIX準拠のコマンドを置いてそれしか使わないようにすればいいんじゃないの？」ということができるようにしたいと。そんなコマンドあるんかということですが、作るしかありません。そしてそういうコマンドのパッケージが、この言語のライブラリに相当するものになるわけです。<br />
<br />
移植するときは、コマンド（あるいはコマンドのソース）ごとコピーです。移植性はコマンドに任せます。いろんな人がシェルスクリプトの移植性に対してああだこうだ議論してますが、基本的に自分の考えはこのようなものです。<br />
<br />
んで、「移植性なんか関係ない。書き散らかしたい」という普段の私みたいな奴のために、PATHが通ってるコマンドでは「b.」なんてプレフィックスはつけなくていいようにしています。VBか何かでOption Strictというのがありましたが、そういうオプションでコントロールしてもいいかもしれません。<br />
<br />
<h3>中間ファイル</h3><br />
<br />
基本的に 「file hoge = コマンド」（io.glueの5行目）と書いておけば勝手にファイルができて、処理が終わったら勝手に消えるようになってます（変換後のbashスクリプトを参照のこと）。実際の中間ファイルにはランダムに名前がつけられますが、それを「hoge」で参照できるようになっています。<br />
<br />
<ul><br />
 <li>中間ファイルの後始末が面倒</li><br />
 <li>置き場所やパーミッションを考えるのが面倒</li><br />
</ul><br />
<br />
という中間ファイルに関するシェルスクリプトの面倒さをこれで一網打尽にしたいと。<br />
<br />
<h3>変数</h3><br />
<br />
別の例で、str.glueというコードを示します。基本的にはfileの代わりにstrと書けば、その変数にコマンドの出力が格納されます。日頃言っているように変数あんまり使ったらいけませんが。<br />
<br />
[hs]<br />
import /bin/ as b<br />
import /usr/bin/ as ub<br />
<br />
proc main:<br />
	str s = cattac<br />
	echo $s<br />
<br />
func cattac file:<br />
	b.cat $file<br />
	ub.tail -r<br />
[/hs]<br />
<br />
シェルの場合、変数は文字列しかないのでこれで十分です。他の型を作るつもりはありません。コマンドは字を出し入れするから分かりやすいのであって、別のものがあったら変換しないといけなくなり、ややこしくなります。ただ、作るかも・・・（どっちや）。<br />
<br />
<h3>proc、funcとインデント</h3><br />
<br />
funcでは縦に並べたコマンドがパイプラインで接続されます。procだと普通のシェルスクリプトと同様に順にコマンドが実行されます。上のio.glueやstr.glueの例だと、b.catとub.tailがパイプで接続されます。そして、funcもまた、標準入出力を入出力とします。<br />
<br />
この仕様はとても悩んだのですが、基本的に箇条書きをすればプログラムが書けるようにしたかったので、同じように書いてもprocとfuncで違う動きをするという選択をしています。ただ、ちょっとなーと悩んでいるところでもあります。<br />
<br />
あと、procやfuncの一塊には「ブロック」と名前をつけていますが、他にawkのコードを書くようなブロック、ヒアドキュメントを書くようなブロックがあったら面白いなと。別にperlやrubyやpythonのブロックがあっても構わないと思います。<br />
<br />
<h3>2段以上のインデント</h3><br />
<br />
書けないようにしたいです。ロジックは必ず1段の箇条書きでまとめてしまえないようでは（以下略。過激だ・・・）<br />
<br />
<h3>条件分岐</h3><br />
<br />
2段インデント禁止と微妙に矛盾しますが、今のところifは次のように書きます。testというブロックを作ると、こいつが終了ステータスを返してくるので、それをprocでHaskell風に使っています。ただ、if文にもいろんなパターンがあるので、これで済まないんじゃないかなーとか悩んでますが。<br />
<br />
[hs]<br />
import /bin/ as b<br />
import /usr/bin/ as ub<br />
import /usr/local/bin/ as ulb<br />
<br />
test checkColnum a b:<br />
	str c = ulb.retu &lt; $a<br />
	b.test &quot;$c&quot; = &quot;$b&quot;<br />
<br />
proc main file num:<br />
| checkColnum $file $num:<br />
	b.echo &quot;OK&quot;<br />
| othewise:<br />
	b.false<br />
[/hs]<br />
<br />
<h3>.glueファイル同士のインクルード等</h3><br />
<br />
全部コマンドとしてimportで。基本、全部コマンドで実装しておけば簡単にくっつけられるし、bashからでもzshからでも使えます。ですから、あんまり困らんのじゃないかと思ってます。誰か困ったら慌てて仕組みを作ればいいんじゃないかと。<br />
<br />
<h3>エラー処理</h3><br />
<br />
io.glueを変換したものをご覧いただければ分かりますが、コマンドがエラーを吐くと関数に飛んで止まります。<br />
<br />
<h2>長いプログラムの例</h2><br />
<br />
どうぞ。<br />
<br />
<a href="https://github.com/ryuichiueda/GlueLang/blob/master/PROTOTYPE/SAMPLE_KIYOU2014/index.glue" target="_blank">https://github.com/ryuichiueda/GlueLang/blob/master/PROTOTYPE/SAMPLE_KIYOU2014/index.glue</a><br />
<br />
↓この本で書いたindex.cgiのGlue版です。<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4048660683" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
動作検証もしました。しかし、シンタックスハイライトもなければシェルスクリプトに慣れ切っているので、ここまで長くなると自分でもピンとこなかったり・・・。<br />
<br />
<h2>最後に</h2><br />
<br />
当然ですが、これからも研究課題として取り扱っていきます。腕利きの\@bsdhackさんあたり、手伝ってくれないかなあ・・・（ボソ）。あ、READMEとか、Streemのものを参考にさせていただいて書き直そうと思います・・・。
