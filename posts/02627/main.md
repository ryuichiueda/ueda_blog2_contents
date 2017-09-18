---
Keywords:セルリアンタワー,シェルリアンタワー,CLI,Linux,Mac,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->【問題集】第10回シェル芸勉強会<!--:-->
<!--:ja--><h2>他の回の問題はこちら</h2><br />
<br />
<a href="http://blog.ueda.asia/?page_id=684">シェル芸勉強会スライド一覧</a><br />
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
<h2>Q8</h2><br />
<br />
0から999999までの数字の一様乱数を無限に出力し続けてください。<br />
<br />
<!--:-->
