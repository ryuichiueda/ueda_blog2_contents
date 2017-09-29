---
Keywords: プログラミング,GlueLang,寝る,日記,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangが変態言語になるかどうかの瀬戸際である
本日は久々に<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>を作りこんでいました。読んでてもほとんどの人が分からんと思いますが作業日誌です。いや、読んでも分からんとか言ってたら絶対普及しないので、この前LTやったスライドを貼り付けときます。

<iframe src="//www.slideshare.net/slideshow/embed_code/44124260" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150201-gluelang-lt" title="20150201 シェル芸勉強会LT GlueLangについて（シェル書いてますが何か？）" target="_blank">20150201 シェル芸勉強会LT GlueLangについて（シェル書いてますが何か？）</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h1>ファイルや変数に直接文字列を指定可能に</h1>

今まではechoを書かないとファイルや文字列に文字が入って行きませんでしたが、要らなくなりました。

```hs
uedambp:GlueLang ueda$ cat fuge.glue 
import PATH

file f = 'abc'
str s = 'cde'

cat f
echo s
```

<!--more-->

実行するとこの通りに機能します。

```hs
uedambp:GlueLang ueda$ ./glue fuge.glue 
abc
cde
```

たぶん今後、Pythonみたいに文字列をいじれるように改良すると思います。こんなふうに。

```hs
file f = 'ab%sc%d' % 'hoge' 1234
```


<h1>リテラルの文字列の改行に対応</h1>

ということは、ヒアドキュメントは不要ということで、こんなふうにAWKのコードを書くことができます。

```hs
uedambp:GlueLang ueda$ cat fuga.glue 
import PATH

file code = '
	NF==2{print "素数",$2}
	NF!=2{print "素数じゃねえ"}
'

seq 1 10 >>= gfactor >>= awk -f code
```

<span style="color:red">これでglue自体には文字列処理を実装する必要がないなーと思ったり思わなかったり。</span>

一応実行しときます。

```hs
uedambp:GlueLang ueda$ ./glue fuga.glue 
素数じゃねえ
素数 2
素数 3
素数じゃねえ
素数 5
素数じゃねえ
素数 7
素数じゃねえ
素数じゃねえ
素数じゃねえ
```

whereを使うとワンライナーにawkの長いコードをぶち込むことができます。しかしちょっと分かりにくいかなあ・・・

```hs
uedambp:GlueLang ueda$ cat fuge.glue 
import PATH

seq 1 10 >>= gfactor >>= awk -f awkcode
	where file awkcode = '
		NF==2{print "素数",$2}
		NF!=2{print "素数じゃねえ"}
		'
```

<h1>procをサブシェル化</h1>

変数やimportの情報を引き継げるようになりました。ということで、上のコード（fuge.glue）は次のように書き直すことができます。awkのパスが通ります。

```hs
uedambp:GlueLang ueda$ cat fuge.glue 
import PATH

proc awkcode = awk '
	NF==2{print "素数",$2}
	NF!=2{print "素数じゃねえ"}
	'

seq 1 10 >>= gfactor >>= this.awkcode
```

<h1>文字列をそのままパイプラインに投入できるように</h1>

最後に変態機能について。次のように文字列をパイプラインに送り込めるようにしました。

```hs
uedambp:GlueLang ueda$ cat hoge.glue 
import PATH

'abc
def
ghi' >>= rev
### 実行 ###
uedambp:GlueLang ueda$ ./glue hoge.glue 
cba
fed
ihg
```

改行がちょっと格好悪いので、リストで渡すこともできます。ただ、単に改行でjoinして渡すだけなので、紛らわしいかもしれません。

```hs
uedambp:GlueLang ueda$ cat hoge2.glue 
import PATH

['abc','def','ghi'] >>= rev
###結果は同じ###
uedambp:GlueLang ueda$ ./glue hoge2.glue 
cba
fed
ihg
```

だんだん変態フレーバーが漂い始めたような気がしないでもない。


寝る。
