---
Keywords: サブシェル,GlueLang,OR記号,寝る,研究,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangのif文相当の処理をガラッと変えてみた
今日は息抜きにGlueLangをいじっておりました。といっても言語の開発なので、処理系のバグと、スクリプトのバグの両方に気をつけなければならず、なかなかイライラするものですが・・・

<h2>機能追加1: 複合コマンド</h2>

<!--more-->
今までGlueにはカッコがなかったのですが、bash同様にコマンドをまとめられるようにしました。次の例は２つのechoの出力をrevに渡しているものです。

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

<h2>機能追加2: OR</h2>

もう一つ、ORを表す「!>」という記号を作ってみました。もともとAND演算子「>>」がありますが、「!>」はその逆で、左側のコマンドがエラーを起こしたときだけ右側以降のコマンドが実行されます。例を示します。最初のecho 'a'とfalseの右側のecho 'b'だけ実行されます。echo 'b'が成功してしまうので、echo 'c'は実行されません。

[bash]
uedambp:SRC ueda$ cat hoge 
#!/usr/local/bin/glue
import PATH

echo 'a' &gt;&gt; false !&gt; echo 'b' !&gt; echo 'c'
uedambp:SRC ueda$ ./hoge 
a
b
[/bash]

diffやgrepのように正常でも終了ステータス1を返してくるコマンドでスクリプトが止まらないようにする用途にも使えます。

[bash]
uedambp:GlueLang ueda$ cat hoge 
#!/usr/local/bin/glue
import PATH

file a = seq 1 3
file b = seq 1 2

diff a b !&gt; true
uedambp:GlueLang ueda$ ./hoge 
3d2
&lt; 3
[/bash]

<h2>ifをわざわざ作らなくてもよくなった</h2>

んで面白いことに、上の２つの拡張のお陰でif文が不要になったので思い切って削除しました。今までは、

[hs]
? false
 echo 'hoge'
| true
 echo 'foo'
| otherwise
 echo 'bar'
[/hs]

という書き方にしていましたが複合コマンドとORで、

[hs]
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
[/hs]

でif文みたいになります。実行すると、最初のカッコでfalseがエラーを出すので、二番目のカッコの中に処理が移ります。最後のカッコは２番目のカッコが正常終了するので実行されません。

[bash]
uedambp:SRC ueda$ ./hoge 
foo
[/bash]

カッコ内でコマンドがエラーを起こすと次のカッコに処理が移ります。カッコ内で全コマンドが正常終了すれば、!>でつながっている後ろのカッコ内は実行されません。

少し癖があるのは、{}内のコマンド全てがif文の条件判定として扱われてしまうことでしょうか。そして、if文でエラーが起きてもそれまでの出力は出てしまいます。

[bash]
uedambp:SRC ueda$ cat hoge 
#!/usr/local/bin/glue
import PATH

file x = {
	echo 'aaa'
	false
	echo 'bbb'
} !&gt; {
	echo 'ccc'
}

cat x
###実行するとaaaもファイルに保存されてしまう###
uedambp:SRC ueda$ ./hoge 
aaa
ccc
[/bash]

これを回避したい場合は、こんな書き方をするんでしょうか。もうちょっとうまい書き方があるかもしれません。

[bash]
uedambp:SRC ueda$ cat hoge 
#!/usr/local/bin/glue
import PATH

file x = {
	file y = echo 'aaa' &gt;&gt; false
	cat y
	echo 'bbb'
} !&gt; {
	echo 'ccc'
}

cat x
uedambp:SRC ueda$ ./hoge 
ccc
[/bash]


眠いので寝る。
