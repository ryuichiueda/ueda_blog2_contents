---
Keywords: シェルスクリプト,GlueLang,研究,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# 煽られるように開発中の言語（Glue）について説明・・・
あわわわわ。

<blockquote class="twitter-tweet" lang="ja"><p><a href="https://twitter.com/okapies">\@okapies</a> 外部コマンドを起動しなくてもいい、マルチコア対応のシェルスクリプトを想定しています。ログ解析とかテキスト加工とか。</p>&mdash; Yukihiro Matsumoto (\@yukihiro_matz) <a href="https://twitter.com/yukihiro_matz/status/543059740473831424">2014, 12月 11</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

引用するのも何か申し訳ないのですが、ここ数日この件で2,3人の方から感想を求められたので、感想を・・・。

<!--more-->

<blockquote class="twitter-tweet" lang="ja"><p>なるほど</p>&mdash; Ryuichi UEDA (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/544363059586678784">2014, 12月 15</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

アホ丸出しです。でも、なるほどです。「そういう解釈になるのかー」と。

<h2>私もホソボソと・・・</h2>

言語を作っております。実は<a href="http://blog.ueda.asia/?p=2058" title="36歳の誕生日にグルー言語作る宣言をせざるを得なくなった">「36歳の誕生日にグルー言語作る宣言をせざるを得なくなった」</a>ということがありまして、作っております。「ある人」が誰かは・・・推して知るべしです。ちゃんと書けばいいのですが、どうも北陸の人間特有の引っ込み思案があり、ブログというものでインタラクションするのが失礼なのではないかと気が引け・・・。その割に人のツイートを引用してますが・・・。

<a href="https://github.com/ryuichiueda/GlueLang/tree/master/PROTOTYPE" target="_blank">https://github.com/ryuichiueda/GlueLang/tree/master/PROTOTYPE</a>

んで、現在の状況ですが、大学にこの件で紀要を書いて一旦ストップし、ロボットの方の研究をしています。これは決して消極的な理由と捉えていただきたくないのですが、こちらでもやりたいことだらけで・・・。年度内にはもう一度、まとまった日数を費やそうと考えています。

ただ、紀要を書いて満足してインターネット上に何も公表していなかったので、この際何をしているのかを書いておこうと思います。私個人がこのような状況なので、考え方だけでも何か貢献できないかと。

<h2>なぜ新言語か</h2>

コアが増えるとパイプライン処理が簡単に書けるようにしないといろいろ面倒で、ただ既存の言語だとパイプライン処理を持ち込むと異物感が甚だしいので、どうしても新しい言語を作るという発想になります。シェルも、インタラクティブ性が重視されすぎていて言語としては弱いので、新しいもの、という発想になります。ということで新言語を作り出しました。私がちゃんと作り切ることができるかどうかは分からないのですが、そういう発想には確信を持っています。


私の場合は言語の解釈以外のものを全て外部コマンドに任せてしまおうという考えでやっているので、たぶんMatzさんの<a href="https://github.com/matz/streem" target="_blank">Streem</a>とは直交する、すなわち用途が一緒のようで違ったものになると思います。ということで、言語といっても私の場合はシェルを作ることになります。最近もdashのコードのパーサの部分を読んでいますが、なかなか手ごわく・・・。

<h2>とりあえず何を作ったか。</h2>

次のようなコードを入力すると・・・

```hs
import /bin/ as b
import /usr/bin/ as ub

proc main file:
	file f = cattac $file
	b.cat $f

func cattac file:
	b.cat $file
	ub.tail -r
```

次のようなbashのコードに変換して実行するトランスレータを作ったところです。

```bash
ERROR_EXIT(){
	rm -f /tmp/$$-*
	exit 1
}

ERROR_CHECK(){
	[ &quot;$(tr -d ' 0' <<< ${PIPESTATUS[\@]})&quot; = &quot;&quot; ] &amp;&amp; return
	ERROR_EXIT
}

trap ERROR_EXIT 1 2 3 15

foreach(){

	while read line ; do
		&quot;$1&quot; $line
		ERROR_CHECK
	done
}

cattac(){
/bin/cat $1 | /usr/bin/tail -r
	ERROR_CHECK
}

main(){
	f=$(mktemp /tmp/$$-f)
ERROR_CHECK
 cattac $1 &gt; $f
ERROR_CHECK

	/bin/cat $f
ERROR_CHECK

}

main &quot;$1&quot;
ERROR_CHECK

rm -f /tmp/$$-*
```

やっていることは簡単で、単に「cat | tail -r」をしているだけです。

ちょっと動かしてみます。「./glue SAMPLE_SCRIPTS/io.glue」が変換前のスクリプトで、内部でbashに変換されて実行されます。（久しぶりに動かすので、ドキドキしましたがちゃんと動きました。）

```bash
uedambp:PROTOTYPE ueda$ seq 5 | ./glue SAMPLE_SCRIPTS/io.glue
5
4
3
2
1
```


<h2>仕様等</h2>

もう一度、新言語のスクリプトを示します。だいたいこのコードにやりたいことが凝縮されています。


```hs
import /bin/ as b
import /usr/bin/ as ub

proc main file:
	file f = cattac $file
	b.cat $f

func cattac file:
	b.cat $file
	ub.tail -r
```

<h3>PATHに代わるimport</h3>

まず、importですが、これはPATHに代わる仕組みです。この例では、/bin/下のコマンドに「b.」、/usr/bin/下のコマンドに「ub.」とつけています。これは移植性の改善を狙ってのことで、将来的には

```hs
import /usr/local/bin/posix/ as posix
```

というように、「移植性が本当に必要ならばPOSIX準拠のコマンドを置いてそれしか使わないようにすればいいんじゃないの？」ということができるようにしたいと。そんなコマンドあるんかということですが、作るしかありません。そしてそういうコマンドのパッケージが、この言語のライブラリに相当するものになるわけです。

移植するときは、コマンド（あるいはコマンドのソース）ごとコピーです。移植性はコマンドに任せます。いろんな人がシェルスクリプトの移植性に対してああだこうだ議論してますが、基本的に自分の考えはこのようなものです。

んで、「移植性なんか関係ない。書き散らかしたい」という普段の私みたいな奴のために、PATHが通ってるコマンドでは「b.」なんてプレフィックスはつけなくていいようにしています。VBか何かでOption Strictというのがありましたが、そういうオプションでコントロールしてもいいかもしれません。

<h3>中間ファイル</h3>

基本的に 「file hoge = コマンド」（io.glueの5行目）と書いておけば勝手にファイルができて、処理が終わったら勝手に消えるようになってます（変換後のbashスクリプトを参照のこと）。実際の中間ファイルにはランダムに名前がつけられますが、それを「hoge」で参照できるようになっています。

<ul>
 <li>中間ファイルの後始末が面倒</li>
 <li>置き場所やパーミッションを考えるのが面倒</li>
</ul>

という中間ファイルに関するシェルスクリプトの面倒さをこれで一網打尽にしたいと。

<h3>変数</h3>

別の例で、str.glueというコードを示します。基本的にはfileの代わりにstrと書けば、その変数にコマンドの出力が格納されます。日頃言っているように変数あんまり使ったらいけませんが。

```hs
import /bin/ as b
import /usr/bin/ as ub

proc main:
	str s = cattac
	echo $s

func cattac file:
	b.cat $file
	ub.tail -r
```

シェルの場合、変数は文字列しかないのでこれで十分です。他の型を作るつもりはありません。コマンドは字を出し入れするから分かりやすいのであって、別のものがあったら変換しないといけなくなり、ややこしくなります。ただ、作るかも・・・（どっちや）。

<h3>proc、funcとインデント</h3>

funcでは縦に並べたコマンドがパイプラインで接続されます。procだと普通のシェルスクリプトと同様に順にコマンドが実行されます。上のio.glueやstr.glueの例だと、b.catとub.tailがパイプで接続されます。そして、funcもまた、標準入出力を入出力とします。

この仕様はとても悩んだのですが、基本的に箇条書きをすればプログラムが書けるようにしたかったので、同じように書いてもprocとfuncで違う動きをするという選択をしています。ただ、ちょっとなーと悩んでいるところでもあります。

あと、procやfuncの一塊には「ブロック」と名前をつけていますが、他にawkのコードを書くようなブロック、ヒアドキュメントを書くようなブロックがあったら面白いなと。別にperlやrubyやpythonのブロックがあっても構わないと思います。

<h3>2段以上のインデント</h3>

書けないようにしたいです。ロジックは必ず1段の箇条書きでまとめてしまえないようでは（以下略。過激だ・・・）

<h3>条件分岐</h3>

2段インデント禁止と微妙に矛盾しますが、今のところifは次のように書きます。testというブロックを作ると、こいつが終了ステータスを返してくるので、それをprocでHaskell風に使っています。ただ、if文にもいろんなパターンがあるので、これで済まないんじゃないかなーとか悩んでますが。

```hs
import /bin/ as b
import /usr/bin/ as ub
import /usr/local/bin/ as ulb

test checkColnum a b:
	str c = ulb.retu < $a
	b.test &quot;$c&quot; = &quot;$b&quot;

proc main file num:
| checkColnum $file $num:
	b.echo &quot;OK&quot;
| othewise:
	b.false
```

<h3>.glueファイル同士のインクルード等</h3>

全部コマンドとしてimportで。基本、全部コマンドで実装しておけば簡単にくっつけられるし、bashからでもzshからでも使えます。ですから、あんまり困らんのじゃないかと思ってます。誰か困ったら慌てて仕組みを作ればいいんじゃないかと。

<h3>エラー処理</h3>

io.glueを変換したものをご覧いただければ分かりますが、コマンドがエラーを吐くと関数に飛んで止まります。

<h2>長いプログラムの例</h2>

どうぞ。

<a href="https://github.com/ryuichiueda/GlueLang/blob/master/PROTOTYPE/SAMPLE_KIYOU2014/index.glue" target="_blank">https://github.com/ryuichiueda/GlueLang/blob/master/PROTOTYPE/SAMPLE_KIYOU2014/index.glue</a>

↓この本で書いたindex.cgiのGlue版です。

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4048660683" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

動作検証もしました。しかし、シンタックスハイライトもなければシェルスクリプトに慣れ切っているので、ここまで長くなると自分でもピンとこなかったり・・・。

<h2>最後に</h2>

当然ですが、これからも研究課題として取り扱っていきます。腕利きの\@bsdhackさんあたり、手伝ってくれないかなあ・・・（ボソ）。あ、READMEとか、Streemのものを参考にさせていただいて書き直そうと思います・・・。
