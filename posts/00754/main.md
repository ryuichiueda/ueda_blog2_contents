---
Keywords: プログラミング,シェルスクリプト,&amp;&amp;,昼休みに書いた
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルスクリプトの&&スタイルプログラミング（仮称）<!--&& writing style shell programming-->
<!--:ja-->また小ネタ。コマンドをパイプでなくて && でつなぐと面白い事ができます。

例えばこんなスクリプト。

```bash
uedamac:~ ueda$ cat hoge.sh
#!/bin/bash -xv

#ダミーのファイル
echo aaa &gt; hoge

#新しいデータを作って差し替える
echo bbb &gt; hoge.new
#絶対にhogeファイルを壊したくない
cp -p hoge hoge.org
mv hoge.new hoge
```

普通、エラー処理を入れるとこうなります。はっきり言って汚い。
（補足：echo bbb > hoge.new || exit 1でもいいですね。いちいちテストコマンドを使うのは私の癖です。）

```bash
uedamac:~ ueda$ cat hoge2.sh
#!/bin/bash -xv

#ダミーのファイル
echo aaa &gt; hoge

#この hoge.new を hogeに置き換えたい
echo bbb &gt; hoge.new
[ $? -eq 0 ] || exit 1
#絶対にhogeファイルを壊したくない
cp -p hoge hoge.org
[ $? -eq 0 ] || exit 1
mv hoge.new hoge
[ $? -eq 0 ] || exit 1
```

でも、こういう書き方をすると汚さが減ります。


```bash
uedamac:~ ueda$ cat hoge3.sh 
#!/bin/bash -xv

#ダミーのファイル
echo aaa &gt; hoge

#この hoge.new を hogeに置き換えたい
echo bbb &gt; hoge.new &amp;&amp;
#絶対にhogeファイルを壊したくない
cp -p hoge hoge.org &amp;&amp;
mv hoge.new hoge
[ $? -eq 0 ] || exit 1
```

&& はコマンドが失敗したところで止まるので、echo, cp共に正常終了しないとmvに移行できません。

例えば次の例のようにcpでエラーを起こすとmvは実行されません。

```bash
uedamac:~ ueda$ ./hoge3.sh 
#!/bin/bash -xv

#ダミーのファイル
echo aaa &gt; hoge
+ echo aaa

#この hoge.new を hogeに置き換えたい
echo bbb &gt; hoge.new &amp;&amp;
#絶対に失敗したくない
cp -p huge hoge.org &amp;&amp;
mv hoge.new hoge
+ echo bbb
+ cp -p huge hoge.org
cp: huge: No such file or directory
[ $? -eq 0 ] || exit 1
+ '[' 1 -eq 0 ']'
+ exit 1
```

マシンの設定に使うシェルスクリプトの場合、パイプはあまり使わないでしょうから、&&でつなぐ事を覚えておけばエラーしたままスクリプトが暴走するのを簡単に止めることができるようになるでしょう。-eオプションもあるけど、私はこっちの方が好きです。細かい制御ができるので。


コマンドをつなぐのは何もパイプだけでない、ということで。
終わり。

<!--
Sometimes I connect more than two commands with &&, which is the and operator of bash scripts.

I show an example with the following script. 

```bash
uedamac:~ ueda$ cat hoge.sh
#!/bin/bash -xv

#hoge is a dummy file
echo aaa &gt; hoge

#I want to change the contents in the hoge file.
echo bbb &gt; hoge.new
cp -p hoge hoge.org
#this mv should be executed only when the previous commands got successful.
mv hoge.new hoge
```

When we want to stop mv after a failure of the previous commands, 
we can use "||" operator. 

```bash
uedamac:~ ueda$ cat hoge2.sh
#!/bin/bash -xv

echo aaa &gt; hoge

echo bbb &gt; hoge.new || exit 1
cp -p hoge hoge.org || exit 1
mv hoge.new hoge || exit 1
```

But I prefer to use && like this. When this sequence of commands is longer than this example, this way prevents it from being bothersome.

```bash
uedamac:~ ueda$ cat hoge3.sh 
#!/bin/bash -xv

echo aaa &gt; hoge

echo bbb &gt; hoge.new &amp;&amp;
cp -p hoge hoge.org &amp;&amp;
mv hoge.new hoge
[ $? -eq 0 ] || exit 1
```


We can see this writing method makes an intended result from the following log file.
Pipe is not the only one that connect commands.

```bash
uedamac:~ ueda$ ./hoge3.sh 
#!/bin/bash -xv

echo aaa &gt; hoge
+ echo aaa

echo bbb &gt; hoge.new &amp;&amp;z
#misspelling
cp -p huge hoge.org &amp;&amp;
mv hoge.new hoge
+ echo bbb
+ cp -p huge hoge.org
cp: huge: No such file or directory
[ $? -eq 0 ] || exit 1
+ '[' 1 -eq 0 ']'
+ exit 1
```

-->
