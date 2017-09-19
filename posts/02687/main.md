---
Keywords: サブシェル,グループコマンド,bash,未分類
Copyright: (C) 2017 Ryuichi Ueda
---

# bashで中括弧のグループコマンドをパイプでつなぐとサブシェルで実行されるので一応気をつける
どうも。寝不足太郎上田です。細かい話が嫌いなのですが、調べる必要があり、調べたことを書きます。

{}で囲ったグループコマンドについてはシェルスクリプト本体と同じプロセスで動作するという記述がmanにあります。

[bash]
ueda\@remote:~$ man bash
...
 { list; }
 list is simply executed in the current shell environment. 
...
[/bash]

<!--more-->

私の場合、グループコマンドはパイプに複数のコマンドを渡すときに使います。こんな感じで。

[bash]
{
 echo ファイルのヘッダだよーん
 cat file
 echo ファイルのフッタだよーん
} |
cat -n 
[/bash]

ただ、こういうときはmanのとおりの同じプロセスでは動いていないんじゃないかと。なぜなら、パイプでグループコマンドをつなぐときに、別プロセスにする方がパイプを楽に繋げることができるからです。

ということで実験。bash4からBASHPIDという変数があって、これがサブシェルのプロセスIDを持っているので、こいつをechoしてみます。$$だとサブシェルでもシェルスクリプト本体のプロセスIDを保持し続けるのでこの実験はできません。

<h2>パイプでつながない場合</h2>

[bash]
ueda\@remote:~$ cat hoge.bash 
#!/bin/bash

echo 親: $BASHPID

{
	echo 子: $BASHPID
}
[/bash]

[bash]
ueda\@remote:~$ ./hoge.bash 
親: 1671
子: 1671
[/bash]

同じプロセスです。

<h2>パイプでつなぐ場合</h2>

[bash]
ueda\@remote:~$ cat hoge2.bash 
#!/bin/bash

echo 親: $BASHPID

{
	echo 子: $BASHPID
} | cat
[/bash]

[bash]
ueda\@remote:~$ ./hoge2.bash 
親: 1706
子: 1707
[/bash]

<span style="color:red">サブシェルですね。</span>

ということは、次のように子供で定義した変数は親から見えません。こんな使い方しませんが、一応気をつけておいた方が良さそうです。

[bash]
ueda\@remote:~$ cat hoge2-2.bash 
#!/bin/bash

echo 親: $BASHPID

{
	A=aaa
	echo 子: $BASHPID
} | cat

echo $A
ueda\@remote:~$ ./hoge2-2.bash 
親: 1836
子: 1837
 &lt;- aaaと出てこない

[/bash]
<h2>丸括弧だと</h2>

次のようにデフォルトでサブシェルです。

[bash]
ueda\@remote:~$ cat hoge3.bash 
#!/bin/bash

echo 親: $BASHPID

(
	echo 子: $BASHPID
) 
[/bash]

[bash]
ueda\@remote:~$ ./hoge3.bash 
親: 1758
子: 1759
[/bash]

<h2>ご相談</h2>

これは自明だからmanに書かないんでよいんですかね？？in the current shell environmentというのがサブシェル云々の話とは違う話なのかな？？どうしよう・・・。


気が小さいのでドキドキするだけで放置・・・。うーん。
