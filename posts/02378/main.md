---
Keywords: コマンド,セルリアンタワー,シェルリアンタワー,CLI,Linux,Mac,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->【本番資料】第10回シェル芸勉強会<!--:-->
<!--:ja--><h2>他の回の問題はこちら</h2>

<a href="/?page=00684">シェル芸勉強会スライド一覧</a>

<h2>イントロ</h2>

<iframe src="http://www.slideshare.net/slideshow/embed_code/33228155" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>

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

<h2>A1</h2>

```bash
$ echo 2 5 9 8 1 3 7 4 | tr ' ' '+' | bc
39
$ echo 2 5 9 8 1 3 7 4 | awk '{for(i=1;i<=NF;i++){a+=$i}}END{print a}'
39
$ echo 2 5 9 8 1 3 7 4 | tr ' ' '\\n' | awk '{a+=$1}END{print a}'
39
###Tukubai###
$ echo 2 5 9 8 1 3 7 4 | ysum
2 5 9 8 1 3 7 4 39
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

<h2>A2</h2>

```bash
$ cat nums | tr ' ' '\\n' | awk 'NF==1' | awk '{a+=$1}END{print a}'
45
ueda@remote:~$ cat nums | xargs | tr ' ' '+' | bc
45
ueda@remote:~$ cat nums | xargs | ysum
1 2 3 4 5 6 7 8 9 45
```


<h2>Q3</h2>

文字数を数えてください。改行記号は数えないでください。

```bash
ueda@remote:~$ cat genkou
筆者は朝、目玉焼きを食べた。
昼、著者は卵がけごはんを食べた。
そして夜、著者はマンハッタンの夜景を
見ながらゆで玉子を食べた。
```

<h2>A3</h2>

（注意：ロケールで出力が違うことがあります。）

```bash
###これはNG###
ueda@remote:~$ wc -m genkou
65 genkou
ueda@remote:~$ cat genkou | tr -d '\\n' | wc -m
61
ueda@remote:~$ sed 's/./&\\n/g' genkou | awk 'NF==1' | wc -l
61
ueda@remote:~$ cat genkou | awk '{a+=length($1)}END{print a}'
61
```

<h2>Q4</h2>

次のようなファイルを作り、ファイルの中に三個存在する文字を出力してください。

```bash
ueda@remote:~$ cat hoge
aabbcdabbcccdd
```

<h2>A4</h2>

```bash
ueda@remote:~$ cat hoge | sed 's/./&\\n/g' | awk 'NF==1' |
 sort | uniq -c | awk '$1==3{print $2}'
a
d
ueda@remote:~$ cat hoge | sed 's/./&\\n/g' | sort |
 awk 'NF==1' | count 1 1 | awk '$2==3{print $1}'
a
d
ueda@remote:~$ cat hoge | sed 's/./& /g' |
 awk '{for(i=1;i<=NF;i++){x[$i]++};for(k in x){print k,x[k]}}' |
 awk '$2==3{print $1}'
a
d
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

<h2>A5</h2>

```bash
$ find . -type f | while read f ; do mv $f ./ ; done
$ tree
.
├── a
│   └── b
│   └── c
├── file1
├── file2
└── file3

3 directories, 3 files
###別解###
$ find . -type f | xargs -I@ mv @ ./
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

<h2>A6</h2>

```bash
###2ライナーで###
$ ls file* | while read f ; do grep -q hoge $f && mv $f ./a ; done
$ ls file* | while read f ; do grep -qv hoge $f && mv $f ./b ; done
###エクストリームな方法###
$ ls file* | while read f ;¥
 do grep -q hoge $f && mv $f ./a || mv $f ./b ; done
$ tree
.
├── a
│   ├── file1
│   ├── file3
│   └── file4
└── b
 └── file2

2 directories, 4 files
$ for f in file* ; do grep -q hoge $f && mv $f ./a || mv $f ./b ; done
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

<h2>A7</h2>

```bash
$ ls | while read f ; do echo $f file* ; done | awk '{for(i=2;i<=NF;i++){print $1,$i}}' | sort | awk '$1<$2'
###別解1###
$ echo file{1..9} | awk '{for(i=1;i<=9;i++){for(j=i+1;j<=9;j++){{print $i,$j}}}}' 
###別解2###
ueda@remote:~$ echo file{1..9} | awk '{for(i=1;i<=9;i++){for(j=1;j<=9;j++){{print $i,$j}}}}' | awk '$1<$2'
###ツーライナーになるが・・・###
ueda@remote:~$ ls file{1..9} > hoge
ueda@remote:~$ loopx hoge hoge | awk '$1<$2'
```

<h2>Q8</h2>

0から999999までの数字の一様乱数を無限に出力し続けてください。

<h2>A8</h2>

```bash
ueda@remote:~$ cat /dev/urandom | tr -dc '0-9' | fold -b6 | sed 's/^0*//'
###Macだとgtrとgfoldを使わないとコケる###
uedambp:~ ueda$ cat /dev/urandom | gtr -dc '0-9' | gfold -b6 | sed 's/^0*//'
```<!--:-->
