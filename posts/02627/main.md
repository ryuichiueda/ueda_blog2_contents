---
Keywords: セルリアンタワー,シェルリアンタワー,CLI,Linux,Mac,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->【問題集】第10回シェル芸勉強会<!--:-->
<!--:ja--><h2>他の回の問題はこちら</h2>

<a href="http://blog.ueda.asia/?page_id=684">シェル芸勉強会スライド一覧</a>

<!--:--><!--more--><!--:ja-->

<h2>環境</h2>

Linuxで解答を作ったのでMacな方は次のようにコマンドの読み替えを。

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
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>

<h2>Q1</h2>

次の数字の列を足し算してください。（できる人はなるべく変態的に）

```bash
$ echo 2 5 9 8 1 3 7 4
2 5 9 8 1 3 7 4
```

<h2>Q2</h2>

スペースと数字と改行を使って次のようなファイルを作り、書いた数を足し算してください。

```bash
$ cat nums 
 1

2 3 
 4 5
 6 7

8 9
```

<h2>Q3</h2>

文字数を数えてください。改行記号は数えないでください。

```bash
ueda\@remote:~$ cat genkou
筆者は朝、目玉焼きを食べた。
昼、著者は卵がけごはんを食べた。
そして夜、著者はマンハッタンの夜景を
見ながらゆで玉子を食べた。
```


<h2>Q4</h2>

次のようなファイルを作り、ファイルの中に三個存在する文字を出力してください。

```bash
ueda\@remote:~$ cat hoge
aabbcdabbcccdd
```

<h2>Q5</h2>

次のようなファイル、ディレクトリを作ってください。そして、file1, file2, file3をカレントディレクトリに移動してください。

```bash
$ mkdir -p a/b/c
$ touch a/file1 a/b/file2 a/b/c/file3
$ tree
.
└── a
 ├── b
 │   ├── c
 │   │   └── file3
 │   └── file2
 └── file1

3 directories, 3 files
```

<h2>Q6</h2>

次のようにファイルとディレクトリを作り、hogeと書いてあるファイルをディレクトリa、
それ以外のファイルをディレクトリbに振り分けてください。

```bash
$ echo hoge > file1
$ echo huge > file2
$ echo hoge > file3
$ echo hoge > file4
$ mkdir a b
```

<h2>Q7</h2>

以下の9つのファイルについて、二つのファイルの組み合わせを全て列挙してください。ただし、重複してはいけません。

```bash
uedambp:~ ueda$ touch file{1..9}
uedambp:~ ueda$ ls file{1..9}
file1 file2 file3 file4 file5 file6 file7 file8 file9
```

出力例

```bash
file1 file2
file1 file3
file1 file4
file1 file5
file1 file6
file1 file7
file1 file8
file1 file9
file2 file3 <- file2 file1 の組み合わせは既出なので出力しない
file2 file4
file2 file5
file2 file6
...
```

<h2>Q8</h2>

0から999999までの数字の一様乱数を無限に出力し続けてください。

<!--:-->
