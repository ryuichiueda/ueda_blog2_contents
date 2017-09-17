# GlueLangのif文相当の処理をガラッと変えてみた
今日は息抜きにGlueLangをいじっておりました。といっても言語の開発なので、処理系のバグと、スクリプトのバグの両方に気をつけなければならず、なかなかイライラするものですが・・・<br />
<br />
<h2>機能追加1: 複合コマンド</h2><br />
<br />
<!--more--><br />
今までGlueにはカッコがなかったのですが、bash同様にコマンドをまとめられるようにしました。次の例は２つのechoの出力をrevに渡しているものです。<br />
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
<h2>機能追加2: OR</h2><br />
<br />
もう一つ、ORを表す「!>」という記号を作ってみました。もともとAND演算子「>>」がありますが、「!>」はその逆で、左側のコマンドがエラーを起こしたときだけ右側以降のコマンドが実行されます。例を示します。最初のecho 'a'とfalseの右側のecho 'b'だけ実行されます。echo 'b'が成功してしまうので、echo 'c'は実行されません。<br />
<br />
[bash]<br />
uedambp:SRC ueda$ cat hoge <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
echo 'a' &gt;&gt; false !&gt; echo 'b' !&gt; echo 'c'<br />
uedambp:SRC ueda$ ./hoge <br />
a<br />
b<br />
[/bash]<br />
<br />
diffやgrepのように正常でも終了ステータス1を返してくるコマンドでスクリプトが止まらないようにする用途にも使えます。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat hoge <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
file a = seq 1 3<br />
file b = seq 1 2<br />
<br />
diff a b !&gt; true<br />
uedambp:GlueLang ueda$ ./hoge <br />
3d2<br />
&lt; 3<br />
[/bash]<br />
<br />
<h2>ifをわざわざ作らなくてもよくなった</h2><br />
<br />
んで面白いことに、上の２つの拡張のお陰でif文が不要になったので思い切って削除しました。今までは、<br />
<br />
[hs]<br />
? false<br />
 echo 'hoge'<br />
| true<br />
 echo 'foo'<br />
| otherwise<br />
 echo 'bar'<br />
[/hs]<br />
<br />
という書き方にしていましたが複合コマンドとORで、<br />
<br />
[hs]<br />
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
[/hs]<br />
<br />
でif文みたいになります。実行すると、最初のカッコでfalseがエラーを出すので、二番目のカッコの中に処理が移ります。最後のカッコは２番目のカッコが正常終了するので実行されません。<br />
<br />
[bash]<br />
uedambp:SRC ueda$ ./hoge <br />
foo<br />
[/bash]<br />
<br />
カッコ内でコマンドがエラーを起こすと次のカッコに処理が移ります。カッコ内で全コマンドが正常終了すれば、!>でつながっている後ろのカッコ内は実行されません。<br />
<br />
少し癖があるのは、{}内のコマンド全てがif文の条件判定として扱われてしまうことでしょうか。そして、if文でエラーが起きてもそれまでの出力は出てしまいます。<br />
<br />
[bash]<br />
uedambp:SRC ueda$ cat hoge <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
file x = {<br />
	echo 'aaa'<br />
	false<br />
	echo 'bbb'<br />
} !&gt; {<br />
	echo 'ccc'<br />
}<br />
<br />
cat x<br />
###実行するとaaaもファイルに保存されてしまう###<br />
uedambp:SRC ueda$ ./hoge <br />
aaa<br />
ccc<br />
[/bash]<br />
<br />
これを回避したい場合は、こんな書き方をするんでしょうか。もうちょっとうまい書き方があるかもしれません。<br />
<br />
[bash]<br />
uedambp:SRC ueda$ cat hoge <br />
#!/usr/local/bin/glue<br />
import PATH<br />
<br />
file x = {<br />
	file y = echo 'aaa' &gt;&gt; false<br />
	cat y<br />
	echo 'bbb'<br />
} !&gt; {<br />
	echo 'ccc'<br />
}<br />
<br />
cat x<br />
uedambp:SRC ueda$ ./hoge <br />
ccc<br />
[/bash]<br />
<br />
<br />
眠いので寝る。
