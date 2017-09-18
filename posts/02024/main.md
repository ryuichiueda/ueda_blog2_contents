---
Keywords:CLI,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題集】第9回寒中シェル芸勉強会
<span style="size:32px"><a href="http://blog.ueda.asia/?p=1955" target="_blank">解答はコッチ</a></span><br />
<br />
<h2>環境</h2><br />
<br />
Macで解答を作ったのでLinuxな方は次のようにコマンドの読み替えを<br />
<br />
<table><br />
 <tr><br />
 <th>Mac,BSD系</th><br />
 <th>Linux</th><br />
 </tr><br />
 <tr><br />
 <td>gdate</td><br />
 <td>date</td><br />
 </tr><br />
 <tr><br />
 <td>gsed</td><br />
 <td>sed</td><br />
 </tr><br />
 <tr><br />
 <td>tail -r</td><br />
 <td>tac</td><br />
 </tr><br />
</table><br />
<br />
<br />
<h2>第1問</h2><br />
<br />
まず、次のようにファイルを作ってください。<br />
<br />
[bash]<br />
$ touch apple avocado banana cinnamon melon<br />
$ ls<br />
apple avocado banana cinnamon melon<br />
<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
「a,b,c,m」というディレクトリを作って、1文字目が対応するファイルをそれぞれのディレクトリに移動してください。<br />
<br />
[bash]<br />
###こうなったらOK###<br />
$ ls *<br />
a:<br />
apple avocado<br />
 <br />
b:<br />
banana<br />
 <br />
c:<br />
cinnamon<br />
 <br />
m:<br />
melon<br />
[/bash]<br />
<h2>第2問</h2><br />
<br />
まず、次のように名前にスペースが入ったファイルを作ります。<br />
<br />
[bash]<br />
$ touch &quot;私は 蟹&quot; &quot;オシャレな 蟹&quot; &quot;足が 10本&quot;<br />
$ ls -l<br />
total 0<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:22 私は 蟹<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:22 足が 10本<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:22 オシャレな 蟹<br />
[/bash]<br />
<br />
このままでは何かと扱いづらいので、間にアンダーバーを入れて次のように名前を変更してください。<br />
<br />
[bash]<br />
$ ls -l<br />
total 0<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:25 私は_蟹<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:25 足が_10本<br />
-rw-r--r-- 1 ueda staff 0 2 14 11:25 オシャレな_蟹<br />
[/bash]<br />
<br />
<h2>第3問</h2><br />
<br />
ディレクトリを適当に作って、20140101から20141231まで、日付に対応したファイルを作って下さい。各ファイルの中には各日付に対応するdateコマンドの出力を書き込んで下さい。<br />
<br />
（ワンライナーが思いつかない場合は、とりあえず手作業でやってみてください。）<br />
<br />
[bash]<br />
###こんな感じでどうぞ###<br />
uedambp:20140214USPSTUDY ueda$ ls -l | head<br />
total 1460<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140101<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140102<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140103<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140104<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140105<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140106<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140107<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140108<br />
-rw-r--r-- 1 ueda staff 28 2 14 10:23 20140109<br />
uedambp:20140214USPSTUDY ueda$ cat 20140101<br />
水 1 1 00:00:00 JST 2014<br />
[/bash]<br />
<br />
<h2>第4問</h2><br />
<br />
次のように4個ファイルを作って、a_ramenとa_curry、b_appleとb_tomatoのファイルの中身を入れ替えてください。<br />
<br />
[bash]<br />
$ echo カレー &gt; a_ramen<br />
$ echo ラーメン &gt; a_curry<br />
$ echo トマト &gt; b_apple<br />
$ echo リンゴ &gt; b_tomato<br />
###（余談）各ファイルと中身は次のようにgrepで確認できる###<br />
$ grep &quot;&quot; *<br />
a_curry:ラーメン<br />
a_ramen:カレー<br />
b_apple:トマト<br />
b_tomato:リンゴ<br />
[/bash]<br />
<br />
<br />
<h2>第5問</h2><br />
<br />
各月ごとにtar.gzファイルにしてください。<br />
<br />
[bash]<br />
###こんな感じで###<br />
uedambp:20140214USPSTUDY ueda$ ls *.tar.gz<br />
201401.tar.gz 201404.tar.gz 201407.tar.gz 201410.tar.gz<br />
201402.tar.gz 201405.tar.gz 201408.tar.gz 201411.tar.gz<br />
201403.tar.gz 201406.tar.gz 201409.tar.gz 201412.tar.gz<br />
[/bash]<br />
<br />
<h2>第6問</h2><br />
<br />
次のようなディレクトリ・ファイル操作を行って下さい。<br />
<br />
[bash]<br />
###小問1: ディレクトリを作る###<br />
 ~/a/a/a/.../a/a/ （aが百個）<br />
###小問2: ファイルを作る###<br />
 ~/a/a/a/.../a/a/b （aが百個、bはファイル）<br />
###小問3: ~/a/a/a/.../a/a/の底に移動###<br />
uedambp:a ueda$ pwd<br />
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
[/bash]<br />
<br />
<br />
<br />
<h2>第7問</h2><br />
<br />
先ほど作ったファイルbを、50番目のaディレクトリに移動して下さい。<br />
<br />
↓うまくできたかどうかの確認方法<br />
[bash]<br />
###~から50番目のaに移動###<br />
uedambp:~ ueda$ for a in {1..50} ; do cd a ; done<br />
###bがあるか確認###<br />
uedambp:a ueda$ pwd<br />
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a<br />
uedambp:a ueda$ ls<br />
a b<br />
###さらに50個aを下る###<br />
uedambp:a ueda$ for a in {1..50} ; do cd a ; done<br />
uedambp:a ueda$ pwd<br />
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a<br />
/a/a<br />
###なにもない###<br />
uedambp:a ueda$ ls<br />
uedambp:a ueda$ <br />
[/bash]<br />
<br />
<h2>第8問</h2><br />
<br />
先ほど作ったディレクトリについて、rm -rを使わずに~/a以下のディレクトリを消去してください。<br />
<br />
<br />
以上。
