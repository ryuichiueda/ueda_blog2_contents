---
Keywords:サブシェル,グループコマンド,bash,未分類
Copyright: (C) 2017 Ryuichi Ueda
---

# bashで中括弧のグループコマンドをパイプでつなぐとサブシェルで実行されるので一応気をつける
どうも。寝不足太郎上田です。細かい話が嫌いなのですが、調べる必要があり、調べたことを書きます。<br />
<br />
{}で囲ったグループコマンドについてはシェルスクリプト本体と同じプロセスで動作するという記述がmanにあります。<br />
<br />
[bash]<br />
ueda\@remote:~$ man bash<br />
...<br />
 { list; }<br />
 list is simply executed in the current shell environment. <br />
...<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
私の場合、グループコマンドはパイプに複数のコマンドを渡すときに使います。こんな感じで。<br />
<br />
[bash]<br />
{<br />
 echo ファイルのヘッダだよーん<br />
 cat file<br />
 echo ファイルのフッタだよーん<br />
} |<br />
cat -n <br />
[/bash]<br />
<br />
ただ、こういうときはmanのとおりの同じプロセスでは動いていないんじゃないかと。なぜなら、パイプでグループコマンドをつなぐときに、別プロセスにする方がパイプを楽に繋げることができるからです。<br />
<br />
ということで実験。bash4からBASHPIDという変数があって、これがサブシェルのプロセスIDを持っているので、こいつをechoしてみます。$$だとサブシェルでもシェルスクリプト本体のプロセスIDを保持し続けるのでこの実験はできません。<br />
<br />
<h2>パイプでつながない場合</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge.bash <br />
#!/bin/bash<br />
<br />
echo 親: $BASHPID<br />
<br />
{<br />
	echo 子: $BASHPID<br />
}<br />
[/bash]<br />
<br />
[bash]<br />
ueda\@remote:~$ ./hoge.bash <br />
親: 1671<br />
子: 1671<br />
[/bash]<br />
<br />
同じプロセスです。<br />
<br />
<h2>パイプでつなぐ場合</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge2.bash <br />
#!/bin/bash<br />
<br />
echo 親: $BASHPID<br />
<br />
{<br />
	echo 子: $BASHPID<br />
} | cat<br />
[/bash]<br />
<br />
[bash]<br />
ueda\@remote:~$ ./hoge2.bash <br />
親: 1706<br />
子: 1707<br />
[/bash]<br />
<br />
<span style="color:red">サブシェルですね。</span><br />
<br />
ということは、次のように子供で定義した変数は親から見えません。こんな使い方しませんが、一応気をつけておいた方が良さそうです。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge2-2.bash <br />
#!/bin/bash<br />
<br />
echo 親: $BASHPID<br />
<br />
{<br />
	A=aaa<br />
	echo 子: $BASHPID<br />
} | cat<br />
<br />
echo $A<br />
ueda\@remote:~$ ./hoge2-2.bash <br />
親: 1836<br />
子: 1837<br />
 &lt;- aaaと出てこない<br />
<br />
[/bash]<br />
<h2>丸括弧だと</h2><br />
<br />
次のようにデフォルトでサブシェルです。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge3.bash <br />
#!/bin/bash<br />
<br />
echo 親: $BASHPID<br />
<br />
(<br />
	echo 子: $BASHPID<br />
) <br />
[/bash]<br />
<br />
[bash]<br />
ueda\@remote:~$ ./hoge3.bash <br />
親: 1758<br />
子: 1759<br />
[/bash]<br />
<br />
<h2>ご相談</h2><br />
<br />
これは自明だからmanに書かないんでよいんですかね？？in the current shell environmentというのがサブシェル云々の話とは違う話なのかな？？どうしよう・・・。<br />
<br />
<br />
気が小さいのでドキドキするだけで放置・・・。うーん。
