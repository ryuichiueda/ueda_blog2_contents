---
Keywords: サブシェル,プログラミング,GlueLang,OR記号,研究
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangのif文相当の処理をまたいじったがこれで最後にしたい
眠いです。

GlueLangのif文及びその周辺、またいじりました。

<h1>やっぱり波括弧やめた</h1>

<a href="http://blog.ueda.asia/?p=5519" title="GlueLangのif文相当の処理をガラッと変えてみた">前回</a>、複合コマンドをこんなふうに書くようにしましたが・・・

[bash]
uedambp:SRC ueda$ cat hoge 
#!/usr/local/bin/glue
import PATH

{
	echo 'abc'
	echo 'def'
} &gt;&gt;= rev
uedambp:SRC ueda$ ./hoge 
cba
fed
[/bash]

こうしました。やっぱりHaskell, Python系の書き方にしようとしているのに波括弧はあまり合わんという判断。波括弧が最終行の最後にあったら認識しないようになってましたし・・・（アカン）。doの次の行からがサブシェル扱いされます。最初の行のインデントがオフサイドラインになります。

[bash]
uedambp:GlueLang ueda$ cat huge.glue 
#!/usr/local/bin/glue
import PATH

do
	echo 'abc'
	echo 'def'
&gt;&gt;= rev
uedambp:GlueLang ueda$ ./huge.glue 
cba
fed
[/bash]


<h1>procにもdoが必要に</h1>

これに伴い、procで2行以上書くときにもdoが必要ということにしました。イコールの後に一行で書くときは不要です。

[bash]
uedambp:GlueLang ueda$ cat hoge.glue 
#!/usr/local/bin/glue
import PATH

proc hoge = do
	echo 'abc'
	echo 'def'

hoge &gt;&gt;= rev
uedambp:GlueLang ueda$ ./hoge.glue 
cba
fed
[/bash]

<h1>if文の表現</h1>

んで、最終的にif文に相当する表現は次のようになりました。前回の

[bash]
#!/usr/local/bin/glue
import PATH

{
	false
	echo 'hoge'
} !&gt; {
	echo 'foo'
} !&gt; {
	echo 'bar'
}
[/bash]

は、

[bash]
uedambp:GlueLang ueda$ cat hoge.glue 
#!/usr/local/bin/glue
import PATH

do
	false
	echo 'hoge'
!&gt; do
	echo 'foo'
!&gt; do
	echo 'bar'
[/bash]

となりました。

ただ、この書き方だと前回言ったようにサブシェル内のコマンドが全て条件文になってしまう（if文というよりもtryみたいになる）ので、ちゃんと条件と条件が満たされたときに実行される部分を分けたいときは、

[bash]
uedambp:GlueLang ueda$ cat if1.glue 
#!/usr/local/bin/glue
import PATH

test 1 -eq 2 ? do
	echo 'first subshell'
	echo '1 = 2'
!&gt; test 1 -eq 1 ? do
	echo 'second subshell'
	echo '1 = 1'
!&gt; echo 'third command'
###実行###
uedambp:GlueLang ueda$ ./if1.glue 
second subshell
1 = 1
[/bash]

と書いてもらうことにしました。?の左側に条件、右側に条件がtrueのときに実行される部分を書きます。別にサブシェルを使う必要のないときは、

[bash]
uedambp:GlueLang ueda$ cat if2.glue 
#!/usr/local/bin/glue
import PATH

test 1 -eq 2 ? echo '1 = 2'
!&gt; test 1 -eq 1 ? echo '1 = 1'
!&gt; echo 'third command'
[/bash]

となります。ちょっとスッキリしませんが、if文自体あんまり使うことは無いはずなので、これでよしとしたいです。

実は「?」は、「!>, >>, >>=」と同じグループの演算子なので基本的にこれはif文でなくコマンドを接続しているだけです。ですので、

[bash]
uedambp:GlueLang ueda$ cat if3.glue 
#!/usr/local/bin/glue
import PATH

test 1 -eq 2 ? echo '1 = 2' !&gt; test 1 -eq 1 ? echo '1 = 1' !&gt; echo 'third command'
[/bash]

と書いても動きますが、さすがにインデント入れないと可読性皆無になりますね。

ところで、だれかGlueLangの開発についてこれてますかね？？？

あかん。孤立気味だ。


寝る。
