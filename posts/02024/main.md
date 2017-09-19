---
Keywords: CLI,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題集】第9回寒中シェル芸勉強会
<span style="size:32px"><a href="http://blog.ueda.asia/?p=1955" target="_blank">解答はコッチ</a></span>

<h2>環境</h2>

Macで解答を作ったのでLinuxな方は次のようにコマンドの読み替えを

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
</table>


<h2>第1問</h2>

まず、次のようにファイルを作ってください。

```bash
$ touch apple avocado banana cinnamon melon
$ ls
apple avocado banana cinnamon melon

```

<!--more-->

「a,b,c,m」というディレクトリを作って、1文字目が対応するファイルをそれぞれのディレクトリに移動してください。

```bash
###こうなったらOK###
$ ls *
a:
apple avocado
 
b:
banana
 
c:
cinnamon
 
m:
melon
```
<h2>第2問</h2>

まず、次のように名前にスペースが入ったファイルを作ります。

```bash
$ touch &quot;私は 蟹&quot; &quot;オシャレな 蟹&quot; &quot;足が 10本&quot;
$ ls -l
total 0
-rw-r--r-- 1 ueda staff 0 2 14 11:22 私は 蟹
-rw-r--r-- 1 ueda staff 0 2 14 11:22 足が 10本
-rw-r--r-- 1 ueda staff 0 2 14 11:22 オシャレな 蟹
```

このままでは何かと扱いづらいので、間にアンダーバーを入れて次のように名前を変更してください。

```bash
$ ls -l
total 0
-rw-r--r-- 1 ueda staff 0 2 14 11:25 私は_蟹
-rw-r--r-- 1 ueda staff 0 2 14 11:25 足が_10本
-rw-r--r-- 1 ueda staff 0 2 14 11:25 オシャレな_蟹
```

<h2>第3問</h2>

ディレクトリを適当に作って、20140101から20141231まで、日付に対応したファイルを作って下さい。各ファイルの中には各日付に対応するdateコマンドの出力を書き込んで下さい。

（ワンライナーが思いつかない場合は、とりあえず手作業でやってみてください。）

```bash
###こんな感じでどうぞ###
uedambp:20140214USPSTUDY ueda$ ls -l | head
total 1460
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140101
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140102
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140103
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140104
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140105
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140106
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140107
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140108
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140109
uedambp:20140214USPSTUDY ueda$ cat 20140101
水 1 1 00:00:00 JST 2014
```

<h2>第4問</h2>

次のように4個ファイルを作って、a_ramenとa_curry、b_appleとb_tomatoのファイルの中身を入れ替えてください。

```bash
$ echo カレー &gt; a_ramen
$ echo ラーメン &gt; a_curry
$ echo トマト &gt; b_apple
$ echo リンゴ &gt; b_tomato
###（余談）各ファイルと中身は次のようにgrepで確認できる###
$ grep &quot;&quot; *
a_curry:ラーメン
a_ramen:カレー
b_apple:トマト
b_tomato:リンゴ
```


<h2>第5問</h2>

各月ごとにtar.gzファイルにしてください。

```bash
###こんな感じで###
uedambp:20140214USPSTUDY ueda$ ls *.tar.gz
201401.tar.gz 201404.tar.gz 201407.tar.gz 201410.tar.gz
201402.tar.gz 201405.tar.gz 201408.tar.gz 201411.tar.gz
201403.tar.gz 201406.tar.gz 201409.tar.gz 201412.tar.gz
```

<h2>第6問</h2>

次のようなディレクトリ・ファイル操作を行って下さい。

```bash
###小問1: ディレクトリを作る###
 ~/a/a/a/.../a/a/ （aが百個）
###小問2: ファイルを作る###
 ~/a/a/a/.../a/a/b （aが百個、bはファイル）
###小問3: ~/a/a/a/.../a/a/の底に移動###
uedambp:a ueda$ pwd
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
```



<h2>第7問</h2>

先ほど作ったファイルbを、50番目のaディレクトリに移動して下さい。

↓うまくできたかどうかの確認方法
```bash
###~から50番目のaに移動###
uedambp:~ ueda$ for a in {1..50} ; do cd a ; done
###bがあるか確認###
uedambp:a ueda$ pwd
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a
uedambp:a ueda$ ls
a b
###さらに50個aを下る###
uedambp:a ueda$ for a in {1..50} ; do cd a ; done
uedambp:a ueda$ pwd
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a
###なにもない###
uedambp:a ueda$ ls
uedambp:a ueda$ 
```

<h2>第8問</h2>

先ほど作ったディレクトリについて、rm -rを使わずに~/a以下のディレクトリを消去してください。


以上。
