---
Keywords:コマンド,セルリアンタワー,シェルリアンタワー,CLI,Linux,Mac,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->【本番資料】第10回シェル芸勉強会<!--:-->
<!--:ja--><h2>他の回の問題はこちら</h2><br />
<br />
<a href="http://blog.ueda.asia/?page_id=684">シェル芸勉強会スライド一覧</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<iframe src="http://www.slideshare.net/slideshow/embed_code/33228155" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br />
<br />
<!--:--><!--more--><!--:ja--><br />
<br />
<h2>環境</h2><br />
<br />
Linuxで解答を作ったのでMacな方は次のようにコマンドの読み替えを。<br />
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
次の数字の列を足し算してください。（できる人はなるべく変態的に）<br />
<br />
[bash]<br />
$ echo 2 5 9 8 1 3 7 4<br />
2 5 9 8 1 3 7 4<br />
[/bash]<br />
<br />
<h2>A1</h2><br />
<br />
[bash]<br />
$ echo 2 5 9 8 1 3 7 4 | tr ' ' '+' | bc<br />
39<br />
$ echo 2 5 9 8 1 3 7 4 | awk '{for(i=1;i&lt;=NF;i++){a+=$i}}END{print a}'<br />
39<br />
$ echo 2 5 9 8 1 3 7 4 | tr ' ' '\\n' | awk '{a+=$1}END{print a}'<br />
39<br />
###Tukubai###<br />
$ echo 2 5 9 8 1 3 7 4 | ysum<br />
2 5 9 8 1 3 7 4 39<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
スペースと数字と改行を使って次のようなファイルを作り、書いた数を足し算してください。<br />
<br />
[bash]<br />
$ cat nums <br />
 1<br />
<br />
2 3 <br />
 4 5<br />
 6 7<br />
<br />
8 9<br />
[/bash]<br />
<br />
<h2>A2</h2><br />
<br />
[bash]<br />
$ cat nums | tr ' ' '\\n' | awk 'NF==1' | awk '{a+=$1}END{print a}'<br />
45<br />
ueda\@remote:~$ cat nums | xargs | tr ' ' '+' | bc<br />
45<br />
ueda\@remote:~$ cat nums | xargs | ysum<br />
1 2 3 4 5 6 7 8 9 45<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
文字数を数えてください。改行記号は数えないでください。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat genkou<br />
筆者は朝、目玉焼きを食べた。<br />
昼、著者は卵がけごはんを食べた。<br />
そして夜、著者はマンハッタンの夜景を<br />
見ながらゆで玉子を食べた。<br />
[/bash]<br />
<br />
<h2>A3</h2><br />
<br />
（注意：ロケールで出力が違うことがあります。）<br />
<br />
[bash]<br />
###これはNG###<br />
ueda\@remote:~$ wc -m genkou<br />
65 genkou<br />
ueda\@remote:~$ cat genkou | tr -d '\\n' | wc -m<br />
61<br />
ueda\@remote:~$ sed 's/./&amp;\\n/g' genkou | awk 'NF==1' | wc -l<br />
61<br />
ueda\@remote:~$ cat genkou | awk '{a+=length($1)}END{print a}'<br />
61<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
次のようなファイルを作り、ファイルの中に三個存在する文字を出力してください。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge<br />
aabbcdabbcccdd<br />
[/bash]<br />
<br />
<h2>A4</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge | sed 's/./&amp;\\n/g' | awk 'NF==1' |<br />
 sort | uniq -c | awk '$1==3{print $2}'<br />
a<br />
d<br />
ueda\@remote:~$ cat hoge | sed 's/./&amp;\\n/g' | sort |<br />
 awk 'NF==1' | count 1 1 | awk '$2==3{print $1}'<br />
a<br />
d<br />
ueda\@remote:~$ cat hoge | sed 's/./&amp; /g' |<br />
 awk '{for(i=1;i&lt;=NF;i++){x[$i]++};for(k in x){print k,x[k]}}' |<br />
 awk '$2==3{print $1}'<br />
a<br />
d<br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
次のようなファイル、ディレクトリを作ってください。そして、file1, file2, file3をカレントディレクトリに移動してください。<br />
<br />
[bash]<br />
$ mkdir -p a/b/c<br />
$ touch a/file1 a/b/file2 a/b/c/file3<br />
$ tree<br />
.<br />
└── a<br />
 ├── b<br />
 │   ├── c<br />
 │   │   └── file3<br />
 │   └── file2<br />
 └── file1<br />
<br />
3 directories, 3 files<br />
[/bash]<br />
<br />
<h2>A5</h2><br />
<br />
[bash]<br />
$ find . -type f | while read f ; do mv $f ./ ; done<br />
$ tree<br />
.<br />
├── a<br />
│   └── b<br />
│   └── c<br />
├── file1<br />
├── file2<br />
└── file3<br />
<br />
3 directories, 3 files<br />
###別解###<br />
$ find . -type f | xargs -I\@ mv \@ ./<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
次のようにファイルとディレクトリを作り、hogeと書いてあるファイルをディレクトリa、<br />
それ以外のファイルをディレクトリbに振り分けてください。<br />
<br />
[bash]<br />
$ echo hoge &gt; file1<br />
$ echo huge &gt; file2<br />
$ echo hoge &gt; file3<br />
$ echo hoge &gt; file4<br />
$ mkdir a b<br />
[/bash]<br />
<br />
<h2>A6</h2><br />
<br />
[bash]<br />
###2ライナーで###<br />
$ ls file* | while read f ; do grep -q hoge $f &amp;&amp; mv $f ./a ; done<br />
$ ls file* | while read f ; do grep -qv hoge $f &amp;&amp; mv $f ./b ; done<br />
###エクストリームな方法###<br />
$ ls file* | while read f ;¥<br />
 do grep -q hoge $f &amp;&amp; mv $f ./a || mv $f ./b ; done<br />
$ tree<br />
.<br />
├── a<br />
│   ├── file1<br />
│   ├── file3<br />
│   └── file4<br />
└── b<br />
 └── file2<br />
<br />
2 directories, 4 files<br />
$ for f in file* ; do grep -q hoge $f &amp;&amp; mv $f ./a || mv $f ./b ; done<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
以下の9つのファイルについて、二つのファイルの組み合わせを全て列挙してください。ただし、重複してはいけません。<br />
<br />
[bash]<br />
uedambp:~ ueda$ touch file{1..9}<br />
uedambp:~ ueda$ ls file{1..9}<br />
file1 file2 file3 file4 file5 file6 file7 file8 file9<br />
[/bash]<br />
<br />
出力例<br />
<br />
[bash]<br />
file1 file2<br />
file1 file3<br />
file1 file4<br />
file1 file5<br />
file1 file6<br />
file1 file7<br />
file1 file8<br />
file1 file9<br />
file2 file3 &lt;- file2 file1 の組み合わせは既出なので出力しない<br />
file2 file4<br />
file2 file5<br />
file2 file6<br />
...<br />
[/bash]<br />
<br />
<h2>A7</h2><br />
<br />
[bash]<br />
$ ls | while read f ; do echo $f file* ; done | awk '{for(i=2;i&lt;=NF;i++){print $1,$i}}' | sort | awk '$1&lt;$2'<br />
###別解1###<br />
$ echo file{1..9} | awk '{for(i=1;i&lt;=9;i++){for(j=i+1;j&lt;=9;j++){{print $i,$j}}}}' <br />
###別解2###<br />
ueda\@remote:~$ echo file{1..9} | awk '{for(i=1;i&lt;=9;i++){for(j=1;j&lt;=9;j++){{print $i,$j}}}}' | awk '$1&lt;$2'<br />
###ツーライナーになるが・・・###<br />
ueda\@remote:~$ ls file{1..9} &gt; hoge<br />
ueda\@remote:~$ loopx hoge hoge | awk '$1&lt;$2'<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
0から999999までの数字の一様乱数を無限に出力し続けてください。<br />
<br />
<h2>A8</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ cat /dev/urandom | tr -dc '0-9' | fold -b6 | sed 's/^0*//'<br />
###Macだとgtrとgfoldを使わないとコケる###<br />
uedambp:~ ueda$ cat /dev/urandom | gtr -dc '0-9' | gfold -b6 | sed 's/^0*//'<br />
[/bash]<!--:-->
