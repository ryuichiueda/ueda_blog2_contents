---
Keywords:サブシェル,プログラミング,GlueLang,OR記号,研究
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangのif文相当の処理をまたいじったがこれで最後にしたい
眠いです。<br />
<br />
GlueLangのif文及びその周辺、またいじりました。<br />
<br />
<h1>やっぱり波括弧やめた</h1><br />
<br />
<a href="http://blog.ueda.asia/?p=5519" title="GlueLangのif文相当の処理をガラッと変えてみた">前回</a>、複合コマンドをこんなふうに書くようにしましたが・・・<br />
<br />
[bash]<br />
uedambp:SRC ueda$ cat hoge <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
{<br />
	echo 'abc'<br />
	echo 'def'<br />
} &gt;&gt;= rev<br />
uedambp:SRC ueda$ ./hoge <br />
cba<br />
fed<br />
[/bash]<br />
<br />
こうしました。やっぱりHaskell, Python系の書き方にしようとしているのに波括弧はあまり合わんという判断。波括弧が最終行の最後にあったら認識しないようになってましたし・・・（アカン）。doの次の行からがサブシェル扱いされます。最初の行のインデントがオフサイドラインになります。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat huge.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
do<br />
	echo 'abc'<br />
	echo 'def'<br />
&gt;&gt;= rev<br />
uedambp:GlueLang ueda$ ./huge.glue <br />
cba<br />
fed<br />
[/bash]<br />
<br />
<br />
<h1>procにもdoが必要に</h1><br />
<br />
これに伴い、procで2行以上書くときにもdoが必要ということにしました。イコールの後に一行で書くときは不要です。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
proc hoge = do<br />
	echo 'abc'<br />
	echo 'def'<br />
<br />
hoge &gt;&gt;= rev<br />
uedambp:GlueLang ueda$ ./hoge.glue <br />
cba<br />
fed<br />
[/bash]<br />
<br />
<h1>if文の表現</h1><br />
<br />
んで、最終的にif文に相当する表現は次のようになりました。前回の<br />
<br />
[bash]<br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
{<br />
	false<br />
	echo 'hoge'<br />
} !&gt; {<br />
	echo 'foo'<br />
} !&gt; {<br />
	echo 'bar'<br />
}<br />
[/bash]<br />
<br />
は、<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
do<br />
	false<br />
	echo 'hoge'<br />
!&gt; do<br />
	echo 'foo'<br />
!&gt; do<br />
	echo 'bar'<br />
[/bash]<br />
<br />
となりました。<br />
<br />
ただ、この書き方だと前回言ったようにサブシェル内のコマンドが全て条件文になってしまう（if文というよりもtryみたいになる）ので、ちゃんと条件と条件が満たされたときに実行される部分を分けたいときは、<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat if1.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
test 1 -eq 2 ? do<br />
	echo 'first subshell'<br />
	echo '1 = 2'<br />
!&gt; test 1 -eq 1 ? do<br />
	echo 'second subshell'<br />
	echo '1 = 1'<br />
!&gt; echo 'third command'<br />
###実行###<br />
uedambp:GlueLang ueda$ ./if1.glue <br />
second subshell<br />
1 = 1<br />
[/bash]<br />
<br />
と書いてもらうことにしました。?の左側に条件、右側に条件がtrueのときに実行される部分を書きます。別にサブシェルを使う必要のないときは、<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat if2.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
test 1 -eq 2 ? echo '1 = 2'<br />
!&gt; test 1 -eq 1 ? echo '1 = 1'<br />
!&gt; echo 'third command'<br />
[/bash]<br />
<br />
となります。ちょっとスッキリしませんが、if文自体あんまり使うことは無いはずなので、これでよしとしたいです。<br />
<br />
実は「?」は、「!>, >>, >>=」と同じグループの演算子なので基本的にこれはif文でなくコマンドを接続しているだけです。ですので、<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat if3.glue <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
test 1 -eq 2 ? echo '1 = 2' !&gt; test 1 -eq 1 ? echo '1 = 1' !&gt; echo 'third command'<br />
[/bash]<br />
<br />
と書いても動きますが、さすがにインデント入れないと可読性皆無になりますね。<br />
<br />
ところで、だれかGlueLangの開発についてこれてますかね？？？<br />
<br />
あかん。孤立気味だ。<br />
<br />
<br />
寝る。
