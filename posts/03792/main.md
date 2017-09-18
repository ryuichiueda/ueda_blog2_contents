---
Keywords: CLI,Linux,Mac,Unix,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第13回危険でない方のシェル芸勉強会
<h2>環境</h2><br />
<br />
Macで解答を作ったのでLinuxな方は次のようにコマンドの読み替えを。<br />
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
 <tr><br />
 <td>gtr</td><br />
 <td>tr</td><br />
 </tr><br />
 <tr><br />
 <td>gfold</td><br />
 <td>fold</td><br />
 </tr><br />
</table><br />
<br />
<h2>Q1</h2><br />
<br />
次のようにShift JISのファイルを作り、Shift JISで「きく」と書いてあるファイルを探すワンライナーを考えてください。（答えは「b」ですね。）<br />
<br />
[bash]<br />
uedambp:q1 ueda$ echo あいうえお | nkf -xLws &gt; a<br />
uedambp:q1 ueda$ echo かきくけこ | nkf -xLws &gt; b<br />
uedambp:q1 ueda$ echo さしすせそ | nkf -xLws &gt; c<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q1 ueda$ for f in * ; do nkf -w $f | grep -q きく &amp;&amp; echo $f ; done<br />
b<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
次のようにディレクトリa,b,c,dに1,2,...,9というファイルがあります。各ディレクトリ内のファイル数をワンライナーで数えてください。<br />
<br />
[bash]<br />
uedambp:q2 ueda$ tree<br />
.<br />
├── a<br />
│   ├── 1<br />
│   ├── 2<br />
│   └── 3<br />
├── b<br />
│   ├── 4<br />
│   └── 5<br />
├── c<br />
└── d<br />
 ├── 6<br />
 ├── 7<br />
 ├── 8<br />
 └── 9<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q2 ueda$ find . | tr / ' ' | awk 'NF==3{print $2}' | uniq <br />
c- 3 a<br />
 2 b<br />
 4 d<br />
uedambp:q2 ueda$ find . -type f | awk -F/ '{print $2}' | uniq <br />
c- 3 a<br />
 2 b<br />
 4 d<br />
###cも出したければ・・・###<br />
uedambp:q2 ueda$ find . | awk -F/ '{print $2}' |<br />
uniq -c | awk 'NF==2{print $2,$1-1}'<br />
a 3<br />
b 2<br />
c 0<br />
d 4<br />
uedambp:q2 ueda$ ls * | xargs | gsed 's/.:/\\n&amp;/g' | awk '{print $1,NF-1}'<br />
 -1<br />
a: 3<br />
b: 2<br />
c: 0<br />
d: 4<br />
uedambp:q2 ueda$ ls -d * |<br />
while read d ; do echo -n $d&quot; &quot; ; ls $d | gyo ; done<br />
a 3<br />
b 2<br />
c 0<br />
d 4<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
今度は次のような配置でファイル1,2,...,9が置かれているときに、ワンライナーでa、cの下のファイルの総数をカウントしてください（ディレクトリを除く）。つまりaなら5個、cなら4個が正解です。<br />
<br />
[bash]<br />
uedambp:q3 ueda$ tree<br />
.<br />
├── a<br />
│   ├── 1<br />
│   ├── 2<br />
│   ├── 3<br />
│   └── b<br />
│   ├── 4<br />
│   └── 5<br />
└── c<br />
 └── d<br />
 ├── 6<br />
 ├── 7<br />
 ├── 8<br />
 └── 9<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q3 ueda$ find . -type f | awk -F/ '{print $2}' | uniq <br />
c- 5 a<br />
 4 c<br />
[/bash]<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
まず、次のように8桁日付のファイルを作ります。<br />
<br />
[bash]<br />
uedambp:q4 ueda$ seq -w 1 31 | xargs -I\@ touch 201401\@<br />
uedambp:q4 ueda$ ls<br />
20140101 20140107 20140113 20140119 20140125 20140131<br />
20140102 20140108 20140114 20140120 20140126<br />
20140103 20140109 20140115 20140121 20140127<br />
20140104 20140110 20140116 20140122 20140128<br />
20140105 20140111 20140117 20140123 20140129<br />
20140106 20140112 20140118 20140124 20140130<br />
[/bash]<br />
<br />
曜日別にディレクトリを作り、その中に当該するファイルを放り込んでください。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q4 ueda$ ls | gdate -f - '+%Y%m%d %a' |<br />
while read d w ; do mkdir -p $w ; mv $d $w ; done<br />
###英語のディレクトリにする###<br />
uedambp:q4 ueda$ ls | LANG=C gdate -f - '+%Y%m%d %a' |<br />
while read d w ; do mkdir -p $w ; mv $d $w ; done<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
以下のようにa,b,cというディレクトリを作り、その下に「{a,b,c}数字」というファイルを作ります。ファイル名の1文字目とディレクトリ名が一致するようにファイルを移動してください。<br />
<br />
[bash]<br />
uedambp:q5 ueda$ tree<br />
.<br />
├── a<br />
│   ├── a01<br />
│   └── b01<br />
├── b<br />
│   ├── a02<br />
│   ├── a03<br />
│   └── c01<br />
└── c<br />
 └── a04<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q5 ueda$ find . -type f |<br />
awk '{print &quot;mv&quot;,$1,substr($1,5,1)}' | sh<br />
mv: ./a/a01 and a/a01 are identical ←エラーが出るけど大丈夫<br />
uedambp:q5 ueda$ tree<br />
.<br />
├── a<br />
│   ├── a01<br />
│   ├── a02<br />
│   ├── a03<br />
│   └── a04<br />
├── b<br />
│   └── b01<br />
└── c<br />
 └── c01<br />
[/bash]<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
次のようにディレクトリa, b, cの下に、8桁日付のファイルをいくつか置きます。<br />
<br />
[bash]<br />
uedambp:q6 ueda$ tree<br />
.<br />
├── a<br />
│   ├── 20130120<br />
│   ├── 20140901<br />
│   └── 20141021<br />
├── b<br />
│   ├── 20131011<br />
│   └── 20140202<br />
└── c<br />
 ├── 20110202<br />
 ├── 20130224<br />
 └── 20141224<br />
[/bash]<br />
<br />
各ディレクトリの最新日付のファイルをカレントディレクトリ（a,b,cのあるディレクトリ）にコピーしてください。各ディレクトリの最新ファイルの日付はそれぞれ違い、コピーの際に衝突しないこととします。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q6 ueda$ for d in * ; do ls $d | tail -n 1 |<br />
 xargs -n 1 -I\@ cp $d/\@ ./ ; done<br />
###確認###<br />
uedambp:q6 ueda$ ls<br />
20140202 20141021 20141224 a b c<br />
uedambp:q6 ueda$ find . -type f | tr '/' ' ' |<br />
 awk '{f[$2]=f[$2]&lt;$3?$3:f[$2]}END{for(k in f){print k,f[k]}}' |<br />
 tr ' ' '/' | xargs -n 1 -I\@ cp \@ ./<br />
###Tukubai等###<br />
uedambp:q6 ueda$ find . -type f | tr '/' ' ' | sort | getlast 1 2 |<br />
 tr '/' ' ' | awk '{print &quot;cp&quot;, &quot;./&quot; $2 &quot;/&quot; $3 &quot; ./&quot;}' | sh<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
Q6について、適当にファイルをtouchします。今度はタイムスタンプが最新のファイルを、a, b, cそれぞれからカレントディレクトリにコピーしてください。コピーの際にタイムスタンプを変えない事。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q7 ueda$ for d in * ; do ls -t $d | head -n 1 |<br />
 xargs -I\@ -n 1 cp -p $d/\@ ./ ; done<br />
[/bash]<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
次のように5個ファイルを作ります。file1をfile2, file2をfile3, file3をfile4, file4をfile5, file5をfile1にmvしてください。<br />
<br />
[bash]<br />
uedambp:q8 ueda$ for i in 1 2 3 4 5 ; do echo $i &gt; file$i ; done<br />
uedambp:q8 ueda$ head *<br />
==&gt; file1 &lt;==<br />
1<br />
<br />
==&gt; file2 &lt;==<br />
2<br />
<br />
==&gt; file3 &lt;==<br />
3<br />
<br />
==&gt; file4 &lt;==<br />
4<br />
<br />
==&gt; file5 &lt;==<br />
5<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
uedambp:q8 ueda$ ls | <br />
awk 'BEGIN{a=&quot;tmp&quot;}{print a,$1;a=$1}END{print a,&quot;tmp&quot;}' | <br />
tail -r | awk '{print &quot;mv&quot;,$1,$2}' | sh<br />
uedambp:q8 ueda$ head *<br />
==&gt; file1 &lt;==<br />
5<br />
<br />
==&gt; file2 &lt;==<br />
1<br />
<br />
==&gt; file3 &lt;==<br />
2<br />
<br />
==&gt; file4 &lt;==<br />
3<br />
<br />
==&gt; file5 &lt;==<br />
4<br />
[/bash]<br />

