---
Keywords: ディレクトリ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【本番資料】第9回寒中シェル芸勉強会
<!--:ja-->問題です。スライドシェアから単なるHTMLにします。加工面倒なので。

ダブルクォートが「& quot;」に化けている・・・orz（2014/4/1修正）

<a href="http://www.usptomo.com/?PAGE=20140217USPSTUDY" target="_blank">USP友の会の公式ページに手抜き講評とリンク集を書きました。Ustreamもありますよ。</a>


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

<h2>イントロ</h2>
<iframe src="http://www.slideshare.net/slideshow/embed_code/31290888" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px 1px 0; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/ryuichiueda/20140215-9" title="20140215 第9回シェル芸勉強会スライド（イントロ）" target="_blank">20140215 第9回シェル芸勉強会スライド（イントロ）</a> </strong> from <strong><a href="http://www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h2>第1問</h2>

まず、次のようにファイルを作ってください。

```bash
$ touch apple avocado banana cinnamon melon
$ ls
apple avocado banana cinnamon melon
```

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

<h3>解答</h3>
```bash
$ ls | while read f ; do mkdir -p &quot;${f:0:1}&quot; ;
 mv $f &quot;${f:0:1}&quot; ; done
uedambp:20140214USPSTUDY ueda$ ls *
a:
apple avocado

b:
banana

c:
cinnamon

m:
melon
###別解###
uedambp:20140214USPSTUDY ueda$ ls |
 awk '{print substr($1,1,1),$1}' |
 awk '{print &quot;mkdir -p&quot;,$1, &quot;;mv&quot;,$2,$1}' | sh
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

<h2>解答</h2>

エスケープを正しく理解しているかがミソ。

```bash
$ ls | while read f ;
 do mv &quot;$f&quot; &quot;$(echo $f | sed 's/ /_/g')&quot; ; done
###別解###
$ ls |
 awk '{f=&quot;\\&quot;&quot; $0 &quot;\\&quot;&quot;;t=gensub(/ /,&quot;_&quot;,$0);print &quot;mv&quot;,f,t}' |
 sh
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

<h3>解答</h3>

```bash
uedambp:20140214USPSTUDY ueda$ d=20140101 ;
 while [ $d -lt 20150101 ] ;
 do echo $d; d=$(gdate -d &quot;$d 1 day&quot; +%Y%m%d) ; done |
 while read d ; do gdate -d $d &gt; $d ; done
###Tukubaiのmdateを使う###
uedambp:20140214USPSTUDY ueda$ for d
 in $(mdate -e 20140101 20141231) ;
 do gdate -d $d &gt; $d ; done 
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

<h3>解答</h3>

```bash
$ grep &quot;&quot; * | tr ':' ' ' | xargs -n 4 |
 awk '{print $1,$4,$3,$2}' |
 xargs -n 2 | awk '{print &quot;echo&quot;,$2,&quot;&gt;&quot;,$1}' | sh
$ grep &quot;&quot; *
a_curry:カレー
a_ramen:ラーメン
b_apple:リンゴ
b_tomato:トマト
###別解###
$ echo * | gsed 's/b_/\\nb_/' |
 while read f1 f2 ; do cat $f1 &gt; tmp ;
 cat $f2 &gt; $f1 ; cat tmp &gt; $f2 ; done
$ grep &quot;&quot; *
a_curry:カレー
a_ramen:ラーメン
b_apple:リンゴ
b_tomato:トマト
tmp:トマト
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

<h3>解答</h3>

```bash
uedambp:20140214USPSTUDY ueda$ seq 201401 201412 |
 while read m ; do tar zcvf $m.tar.gz $m* ; done
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

<h3>解答</h3>

```bash
###小問1### 
uedambp:~ ueda$ seq 1 100 | awk '{print &quot;a&quot;}' | tr '\\n' '/' |
 xargs mkdir -p
###小問2### 
uedambp:~ ueda$ seq 1 100 | awk '{print &quot;a&quot;}END{print &quot;b&quot;}' |
 xargs | tr ' ' '/' | xargs touch
###小問1,2を一気に###
uedambp:~ ueda$ seq 1 100 | awk '{print &quot;a&quot;}' |
 tr '\\n' '/' | sed '1p' |
 awk 'NR==1{print &quot;mkdir -p&quot;,$0}NR==2{print &quot;touch&quot;,$0 &quot;b&quot;}' |
 sh
###小問3###
uedambp:~ ueda$ for x in {1..100} ; do cd a ; done
uedambp:a ueda$ pwd
/Users/ueda/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a
###参考: サブシェルを起動すると移動できない###
uedambp:~ ueda$ seq 1 100 | while read n ; do cd a ; done
uedambp:~ ueda$ 
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

<h3>解問</h3>
```bash
uedambp:~ ueda$ seq 1 150 | xargs | gsed 's/100 /100\\n/g' |
 sed 's/[0-9][0-9]*/a/g' | tr ' ' '/' |
 awk 'BEGIN{print &quot;mv&quot;}{print $0 &quot;/b&quot;}' | xargs | sh
```

<h2>第8問</h2>

先ほど作ったディレクトリについて、rm -rを使わずに~/a以下のディレクトリを消去してください。

<h3>解答</h3>

```bash
uedambp:~ ueda$ seq 1 100 |
 awk '{for(i=0;i&lt;$1;i++){printf &quot;a/&quot;};print &quot;&quot;}' | tail -r |
 while read d ; do rm -f $d/b ; rmdir $d ; done
uedambp:~ ueda$ ls a
gls: cannot access a: No such file or directory
```
<!--:-->
