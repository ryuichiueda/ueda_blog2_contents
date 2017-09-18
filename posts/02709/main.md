---
Keywords:コマンド,flock,Linux,排他処理
Copyright: (C) 2017 Ryuichi Ueda
---
# 排他を実現するコマンドflock(1)の使い方メモ
排他をかけるコマンドです。Ubuntuので試しました。<br />
<br />
まず、排他区間を設けて処理したい内容をシェルスクリプトにします。ここでは、ひたすらプロセス番号をhogeというファイルに書き続けるシェルスクリプトchild.bashを準備しました。<br />
[bash]<br />
ueda\@remote:~$ cat child.bash <br />
#!/bin/bash<br />
<br />
for i in {1..10000} ; do<br />
	echo $$ &gt;&gt; hoge <br />
done<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
次に、child.bashを同時に何本も走らすシェルスクリプトparent.bashを次のように準備します。100個並列で走らせます。flockの使い方ですが、最初に鍵となるファイル（これはディレクトリでもよい）を適当に指定して、その次に実行したいコマンド（スクリプトやその他プログラム）を指定します。<br />
[bash]<br />
ueda\@remote:~$ cat parent.bash <br />
#!/bin/bash<br />
<br />
for i in {1..100} ; do<br />
	flock /home/ueda/lock ./child.bash &amp;<br />
done<br />
[/bash]<br />
<br />
で、実行。無慈悲な攻撃をUbuntuに食らわせます。<br />
[bash]<br />
ueda\@remote:~$ ./parent.bash <br />
ueda\@remote:~$ <br />
[/bash]<br />
<br />
できたファイルhogeを見てみましょう。プロセス番号が入れ違いになってたら排他失敗となりますが・・・。<br />
[bash]<br />
###プロセス番号が順番になっている###<br />
ueda\@remote:~$ uniq hoge | head<br />
27465<br />
27538<br />
27547<br />
27562<br />
27565<br />
27568<br />
27569<br />
27570<br />
27571<br />
27572<br />
###（プロセス番号が一周しなければ）ちゃんと順番になっていることがsort -cで分かる###<br />
ueda\@remote:~$ cat hoge | sort <br />
c-ueda\@remote:~$ echo $?<br />
0<br />
[/bash]<br />
なんかうまくいってます。プロセス番号が順番になるのは、鍵の取れたchild.bashのプロセスから順番にプロセス番号をもらっていくからでしょう。<br />
<br />
次に、もっと無慈悲なchild.bashを用意しました。echoに&をつけて、hogeへの書き込みを非同期にします。<br />
[bash]<br />
ueda\@remote:~$ cat child.bash <br />
#!/bin/bash<br />
<br />
for i in {1..10000} ; do<br />
	echo $$ &gt;&gt; hoge &amp; <br />
done<br />
[/bash]<br />
hogeを一度消去して再実行！<br />
[bash]<br />
ueda\@remote:~$ ./parent.bash <br />
###この場合はプロセス番号が何周もするので、一度uniqをかけてからソートして重複チェックを行う。###<br />
###ただ、運が悪いと別のプロセスのchild.bashに同じプロセスIDが渡る。###<br />
ueda\@remote:~$ cat hoge | uniq | sort | sort <br />
c-ueda\@remote:~$<br />
[/bash]<br />
これもうまくいったようです。<br />
<br />
ちなみにflockの部分を除くとこうなります。<br />
[bash]<br />
ueda\@remote:~$ sort -c hoge<br />
sort: hoge:9680: 順序が不規則: 4507<br />
[/bash]<br />
が、<span style="color:red">この後、プロセスの立ち上げ過ぎでUbuntuがしばらく気絶しましたとさ。</span><br />
<br />
<br />
それはさておき、flock便利だ・・・。
