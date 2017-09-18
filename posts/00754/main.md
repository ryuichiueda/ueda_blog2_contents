---
Keywords: プログラミング,シェルスクリプト,&amp;&amp;,昼休みに書いた
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルスクリプトの&&スタイルプログラミング（仮称）<!--&& writing style shell programming-->
<!--:ja-->また小ネタ。コマンドをパイプでなくて && でつなぐと面白い事ができます。<br />
<br />
例えばこんなスクリプト。<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge.sh<br />
#!/bin/bash -xv<br />
<br />
#ダミーのファイル<br />
echo aaa &gt; hoge<br />
<br />
#新しいデータを作って差し替える<br />
echo bbb &gt; hoge.new<br />
#絶対にhogeファイルを壊したくない<br />
cp -p hoge hoge.org<br />
mv hoge.new hoge<br />
[/bash]<br />
<br />
普通、エラー処理を入れるとこうなります。はっきり言って汚い。<br />
（補足：echo bbb > hoge.new || exit 1でもいいですね。いちいちテストコマンドを使うのは私の癖です。）<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge2.sh<br />
#!/bin/bash -xv<br />
<br />
#ダミーのファイル<br />
echo aaa &gt; hoge<br />
<br />
#この hoge.new を hogeに置き換えたい<br />
echo bbb &gt; hoge.new<br />
[ $? -eq 0 ] || exit 1<br />
#絶対にhogeファイルを壊したくない<br />
cp -p hoge hoge.org<br />
[ $? -eq 0 ] || exit 1<br />
mv hoge.new hoge<br />
[ $? -eq 0 ] || exit 1<br />
[/bash]<br />
<br />
でも、こういう書き方をすると汚さが減ります。<br />
<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge3.sh <br />
#!/bin/bash -xv<br />
<br />
#ダミーのファイル<br />
echo aaa &gt; hoge<br />
<br />
#この hoge.new を hogeに置き換えたい<br />
echo bbb &gt; hoge.new &amp;&amp;<br />
#絶対にhogeファイルを壊したくない<br />
cp -p hoge hoge.org &amp;&amp;<br />
mv hoge.new hoge<br />
[ $? -eq 0 ] || exit 1<br />
[/bash]<br />
<br />
&& はコマンドが失敗したところで止まるので、echo, cp共に正常終了しないとmvに移行できません。<br />
<br />
例えば次の例のようにcpでエラーを起こすとmvは実行されません。<br />
<br />
[bash]<br />
uedamac:~ ueda$ ./hoge3.sh <br />
#!/bin/bash -xv<br />
<br />
#ダミーのファイル<br />
echo aaa &gt; hoge<br />
+ echo aaa<br />
<br />
#この hoge.new を hogeに置き換えたい<br />
echo bbb &gt; hoge.new &amp;&amp;<br />
#絶対に失敗したくない<br />
cp -p huge hoge.org &amp;&amp;<br />
mv hoge.new hoge<br />
+ echo bbb<br />
+ cp -p huge hoge.org<br />
cp: huge: No such file or directory<br />
[ $? -eq 0 ] || exit 1<br />
+ '[' 1 -eq 0 ']'<br />
+ exit 1<br />
[/bash]<br />
<br />
マシンの設定に使うシェルスクリプトの場合、パイプはあまり使わないでしょうから、&&でつなぐ事を覚えておけばエラーしたままスクリプトが暴走するのを簡単に止めることができるようになるでしょう。-eオプションもあるけど、私はこっちの方が好きです。細かい制御ができるので。<br />
<br />
<br />
コマンドをつなぐのは何もパイプだけでない、ということで。<br />
終わり。<br />
<br />
<!--<br />
Sometimes I connect more than two commands with &&, which is the and operator of bash scripts.<br />
<br />
I show an example with the following script. <br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge.sh<br />
#!/bin/bash -xv<br />
<br />
#hoge is a dummy file<br />
echo aaa &gt; hoge<br />
<br />
#I want to change the contents in the hoge file.<br />
echo bbb &gt; hoge.new<br />
cp -p hoge hoge.org<br />
#this mv should be executed only when the previous commands got successful.<br />
mv hoge.new hoge<br />
[/bash]<br />
<br />
When we want to stop mv after a failure of the previous commands, <br />
we can use "||" operator. <br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge2.sh<br />
#!/bin/bash -xv<br />
<br />
echo aaa &gt; hoge<br />
<br />
echo bbb &gt; hoge.new || exit 1<br />
cp -p hoge hoge.org || exit 1<br />
mv hoge.new hoge || exit 1<br />
[/bash]<br />
<br />
But I prefer to use && like this. When this sequence of commands is longer than this example, this way prevents it from being bothersome.<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge3.sh <br />
#!/bin/bash -xv<br />
<br />
echo aaa &gt; hoge<br />
<br />
echo bbb &gt; hoge.new &amp;&amp;<br />
cp -p hoge hoge.org &amp;&amp;<br />
mv hoge.new hoge<br />
[ $? -eq 0 ] || exit 1<br />
[/bash]<br />
<br />
<br />
We can see this writing method makes an intended result from the following log file.<br />
Pipe is not the only one that connect commands.<br />
<br />
[bash]<br />
uedamac:~ ueda$ ./hoge3.sh <br />
#!/bin/bash -xv<br />
<br />
echo aaa &gt; hoge<br />
+ echo aaa<br />
<br />
echo bbb &gt; hoge.new &amp;&amp;z<br />
#misspelling<br />
cp -p huge hoge.org &amp;&amp;<br />
mv hoge.new hoge<br />
+ echo bbb<br />
+ cp -p huge hoge.org<br />
cp: huge: No such file or directory<br />
[ $? -eq 0 ] || exit 1<br />
+ '[' 1 -eq 0 ']'<br />
+ exit 1<br />
[/bash]<br />
<br />
-->
