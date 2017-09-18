---
Keywords:シェルスクリプト,Linux,PPID,/proc/$$/stat,UNIX/Linuxサーバ
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルスクリプトで親のいなくなったプロセスがinitにぶら下がるのを確認してみる
人に教えなければいけなくてUnderstanding the Linux Kernelという分厚い本をざーっと読んでいます。↓この本です。<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=B0043D2E54" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
んで、親のプロセスが居なくなった子供のプロセスはinitにぶらさがるという記述があったので、読書ばっかりで手を動かすのはいかんとシェルスクリプトで実験してみました。<br />
<br />
<h2>/proc/$$/stat</h2><br />
<br />
親のプロセスはbashだとPPIDという変数で調べられるのですが、どうやら途中で親が変わっても変わらないらしいので、/proc/$$/statというファイルの4列目で調べます。<br />
<br />
あ、環境はUbuntu 12.04LTSです。<br />
<br />
<!--more--><br />
<br />
例えばこういうシェルスクリプトを書きます。$$は自分のプロセスIDで、その下のstatというファイルをcatする単純なものです。<br />
[bash]<br />
ueda\@remote:~/tmp$ cat hoge.bash<br />
#!/bin/bash<br />
<br />
cat /proc/$$/stat<br />
[/bash]<br />
<br />
動かす前にシェルのプロセスIDを調べてみましょう。<br />
[bash]<br />
ueda\@remote:~/tmp$ echo $$<br />
30202<br />
[/bash]<br />
30202です。<br />
<br />
ではシェルスクリプトを実行してみます。<br />
[bash]<br />
ueda\@remote:~/tmp$ ./hoge.bash <br />
32722 (hoge.bash) S 30202 32722 30202 34816 32722 4202496 437 0 0 0 0 0 0 0 20 0 1 0 465549287 12263424 300 18446744073709551615 4194304 5111460 140734168949024 140734168947600 140156932455566 0 65536 4 65538 18446744071579287524 0 0 17 1 0 0 0 0 0<br />
[/bash]<br />
4列目に30202がいます。<br />
<br />
<h2>では実験</h2><br />
<br />
次のような二つのシェルスクリプトを準備します。parent.bashはchild.bashを立ち上げた後、5秒後に終わっちまいます。一方、child.bashは1秒置きに自分のプロセスのstatファイルを監視します。本に書いている通りなら5秒後に親のプロセスIDがinitの1に変化するはずです。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat parent.bash <br />
#!/bin/bash<br />
<br />
echo PARENT_ID: $$<br />
./child.bash &amp;<br />
<br />
sleep 5<br />
ueda\@remote:~/tmp$ cat child.bash <br />
#!/bin/bash<br />
<br />
for n in {1..10} ; do<br />
	awk '{print $4}' /proc/$$/stat<br />
	sleep 1<br />
done<br />
[/bash]<br />
<br />
実行！<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ ./parent.bash <br />
PARENT_ID: 619<br />
619<br />
619<br />
619<br />
619<br />
619<br />
ueda\@remote:~/tmp$ 1 &lt;- parent.bashが終わる<br />
1<br />
1<br />
1<br />
1<br />
<br />
ueda\@remote:~/tmp$ <br />
[/bash]<br />
<br />
うまくいった！！！！<br />
<br />
・・・だから何だという気もしないでもないが。<br />
<br />
あと数日であと850ページくらいを読み、だいたいどこに何が書いてあるか頭に詰め込まなければならぬ。死ぬ。<br />
<br />
<br />
おしまい。<br />

