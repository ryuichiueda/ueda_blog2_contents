# GlueLangが変態言語になるかどうかの瀬戸際である
本日は久々に<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>を作りこんでいました。読んでてもほとんどの人が分からんと思いますが作業日誌です。いや、読んでも分からんとか言ってたら絶対普及しないので、この前LTやったスライドを貼り付けときます。<br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/44124260" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150201-gluelang-lt" title="20150201 シェル芸勉強会LT GlueLangについて（シェル書いてますが何か？）" target="_blank">20150201 シェル芸勉強会LT GlueLangについて（シェル書いてますが何か？）</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h1>ファイルや変数に直接文字列を指定可能に</h1><br />
<br />
今まではechoを書かないとファイルや文字列に文字が入って行きませんでしたが、要らなくなりました。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat fuge.glue <br />
import PATH<br />
<br />
file f = 'abc'<br />
str s = 'cde'<br />
<br />
cat f<br />
echo s<br />
[/hs]<br />
<br />
<!--more--><br />
<br />
実行するとこの通りに機能します。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ ./glue fuge.glue <br />
abc<br />
cde<br />
[/hs]<br />
<br />
たぶん今後、Pythonみたいに文字列をいじれるように改良すると思います。こんなふうに。<br />
<br />
[hs]<br />
file f = 'ab%sc%d' % 'hoge' 1234<br />
[/hs]<br />
<br />
<br />
<h1>リテラルの文字列の改行に対応</h1><br />
<br />
ということは、ヒアドキュメントは不要ということで、こんなふうにAWKのコードを書くことができます。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat fuga.glue <br />
import PATH<br />
<br />
file code = '<br />
	NF==2{print &quot;素数&quot;,$2}<br />
	NF!=2{print &quot;素数じゃねえ&quot;}<br />
'<br />
<br />
seq 1 10 &gt;&gt;= gfactor &gt;&gt;= awk -f code<br />
[/hs]<br />
<br />
<span style="color:red">これでglue自体には文字列処理を実装する必要がないなーと思ったり思わなかったり。</span><br />
<br />
一応実行しときます。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ ./glue fuga.glue <br />
素数じゃねえ<br />
素数 2<br />
素数 3<br />
素数じゃねえ<br />
素数 5<br />
素数じゃねえ<br />
素数 7<br />
素数じゃねえ<br />
素数じゃねえ<br />
素数じゃねえ<br />
[/hs]<br />
<br />
whereを使うとワンライナーにawkの長いコードをぶち込むことができます。しかしちょっと分かりにくいかなあ・・・<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat fuge.glue <br />
import PATH<br />
<br />
seq 1 10 &gt;&gt;= gfactor &gt;&gt;= awk -f awkcode<br />
	where file awkcode = '<br />
		NF==2{print &quot;素数&quot;,$2}<br />
		NF!=2{print &quot;素数じゃねえ&quot;}<br />
		'<br />
[/hs]<br />
<br />
<h1>procをサブシェル化</h1><br />
<br />
変数やimportの情報を引き継げるようになりました。ということで、上のコード（fuge.glue）は次のように書き直すことができます。awkのパスが通ります。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat fuge.glue <br />
import PATH<br />
<br />
proc awkcode = awk '<br />
	NF==2{print &quot;素数&quot;,$2}<br />
	NF!=2{print &quot;素数じゃねえ&quot;}<br />
	'<br />
<br />
seq 1 10 &gt;&gt;= gfactor &gt;&gt;= this.awkcode<br />
[/hs]<br />
<br />
<h1>文字列をそのままパイプラインに投入できるように</h1><br />
<br />
最後に変態機能について。次のように文字列をパイプラインに送り込めるようにしました。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
import PATH<br />
<br />
'abc<br />
def<br />
ghi' &gt;&gt;= rev<br />
### 実行 ###<br />
uedambp:GlueLang ueda$ ./glue hoge.glue <br />
cba<br />
fed<br />
ihg<br />
[/hs]<br />
<br />
改行がちょっと格好悪いので、リストで渡すこともできます。ただ、単に改行でjoinして渡すだけなので、紛らわしいかもしれません。<br />
<br />
[hs]<br />
uedambp:GlueLang ueda$ cat hoge2.glue <br />
import PATH<br />
<br />
['abc','def','ghi'] &gt;&gt;= rev<br />
###結果は同じ###<br />
uedambp:GlueLang ueda$ ./glue hoge2.glue <br />
cba<br />
fed<br />
ihg<br />
[/hs]<br />
<br />
だんだん変態フレーバーが漂い始めたような気がしないでもない。<br />
<br />
<br />
寝る。
