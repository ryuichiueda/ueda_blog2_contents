---
Keywords: CLI,Linux,Mac,Unix,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第13回危険でない方のシェル芸勉強会
<h2>環境</h2>

Macで解答を作ったのでLinuxな方は次のようにコマンドの読み替えを。

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

次のようにShift JISのファイルを作り、Shift JISで「きく」と書いてあるファイルを探すワンライナーを考えてください。（答えは「b」ですね。）

```bash
uedambp:q1 ueda$ echo あいうえお | nkf -xLws > a
uedambp:q1 ueda$ echo かきくけこ | nkf -xLws > b
uedambp:q1 ueda$ echo さしすせそ | nkf -xLws > c
```

<h2>解答</h2>

```bash
uedambp:q1 ueda$ for f in * ; do nkf -w $f | grep -q きく && echo $f ; done
b
```

<h2>Q2</h2>

次のようにディレクトリa,b,c,dに1,2,...,9というファイルがあります。各ディレクトリ内のファイル数をワンライナーで数えてください。

```bash
uedambp:q2 ueda$ tree
.
├── a
│   ├── 1
│   ├── 2
│   └── 3
├── b
│   ├── 4
│   └── 5
├── c
└── d
 ├── 6
 ├── 7
 ├── 8
 └── 9
```

<h2>解答</h2>

```bash
uedambp:q2 ueda$ find . | tr / ' ' | awk 'NF==3{print $2}' | uniq 
c- 3 a
 2 b
 4 d
uedambp:q2 ueda$ find . -type f | awk -F/ '{print $2}' | uniq 
c- 3 a
 2 b
 4 d
###cも出したければ・・・###
uedambp:q2 ueda$ find . | awk -F/ '{print $2}' |
uniq -c | awk 'NF==2{print $2,$1-1}'
a 3
b 2
c 0
d 4
uedambp:q2 ueda$ ls * | xargs | gsed 's/.:/\\n&/g' | awk '{print $1,NF-1}'
 -1
a: 3
b: 2
c: 0
d: 4
uedambp:q2 ueda$ ls -d * |
while read d ; do echo -n $d" " ; ls $d | gyo ; done
a 3
b 2
c 0
d 4
```

<h2>Q3</h2>

今度は次のような配置でファイル1,2,...,9が置かれているときに、ワンライナーでa、cの下のファイルの総数をカウントしてください（ディレクトリを除く）。つまりaなら5個、cなら4個が正解です。

```bash
uedambp:q3 ueda$ tree
.
├── a
│   ├── 1
│   ├── 2
│   ├── 3
│   └── b
│   ├── 4
│   └── 5
└── c
 └── d
 ├── 6
 ├── 7
 ├── 8
 └── 9
```

<h2>解答</h2>

```bash
uedambp:q3 ueda$ find . -type f | awk -F/ '{print $2}' | uniq 
c- 5 a
 4 c
```


<h2>Q4</h2>

まず、次のように8桁日付のファイルを作ります。

```bash
uedambp:q4 ueda$ seq -w 1 31 | xargs -I\@ touch 201401\@
uedambp:q4 ueda$ ls
20140101 20140107 20140113 20140119 20140125 20140131
20140102 20140108 20140114 20140120 20140126
20140103 20140109 20140115 20140121 20140127
20140104 20140110 20140116 20140122 20140128
20140105 20140111 20140117 20140123 20140129
20140106 20140112 20140118 20140124 20140130
```

曜日別にディレクトリを作り、その中に当該するファイルを放り込んでください。

<h2>解答</h2>

```bash
uedambp:q4 ueda$ ls | gdate -f - '+%Y%m%d %a' |
while read d w ; do mkdir -p $w ; mv $d $w ; done
###英語のディレクトリにする###
uedambp:q4 ueda$ ls | LANG=C gdate -f - '+%Y%m%d %a' |
while read d w ; do mkdir -p $w ; mv $d $w ; done
```

<h2>Q5</h2>

以下のようにa,b,cというディレクトリを作り、その下に「{a,b,c}数字」というファイルを作ります。ファイル名の1文字目とディレクトリ名が一致するようにファイルを移動してください。

```bash
uedambp:q5 ueda$ tree
.
├── a
│   ├── a01
│   └── b01
├── b
│   ├── a02
│   ├── a03
│   └── c01
└── c
 └── a04
```

<h2>解答</h2>

```bash
uedambp:q5 ueda$ find . -type f |
awk '{print "mv",$1,substr($1,5,1)}' | sh
mv: ./a/a01 and a/a01 are identical ←エラーが出るけど大丈夫
uedambp:q5 ueda$ tree
.
├── a
│   ├── a01
│   ├── a02
│   ├── a03
│   └── a04
├── b
│   └── b01
└── c
 └── c01
```


<h2>Q6</h2>

次のようにディレクトリa, b, cの下に、8桁日付のファイルをいくつか置きます。

```bash
uedambp:q6 ueda$ tree
.
├── a
│   ├── 20130120
│   ├── 20140901
│   └── 20141021
├── b
│   ├── 20131011
│   └── 20140202
└── c
 ├── 20110202
 ├── 20130224
 └── 20141224
```

各ディレクトリの最新日付のファイルをカレントディレクトリ（a,b,cのあるディレクトリ）にコピーしてください。各ディレクトリの最新ファイルの日付はそれぞれ違い、コピーの際に衝突しないこととします。

<h2>解答</h2>

```bash
uedambp:q6 ueda$ for d in * ; do ls $d | tail -n 1 |
 xargs -n 1 -I\@ cp $d/\@ ./ ; done
###確認###
uedambp:q6 ueda$ ls
20140202 20141021 20141224 a b c
uedambp:q6 ueda$ find . -type f | tr '/' ' ' |
 awk '{f[$2]=f[$2]<$3?$3:f[$2]}END{for(k in f){print k,f[k]}}' |
 tr ' ' '/' | xargs -n 1 -I\@ cp \@ ./
###Tukubai等###
uedambp:q6 ueda$ find . -type f | tr '/' ' ' | sort | getlast 1 2 |
 tr '/' ' ' | awk '{print "cp", "./" $2 "/" $3 " ./"}' | sh
```


<h2>Q7</h2>

Q6について、適当にファイルをtouchします。今度はタイムスタンプが最新のファイルを、a, b, cそれぞれからカレントディレクトリにコピーしてください。コピーの際にタイムスタンプを変えない事。

<h2>解答</h2>

```bash
uedambp:q7 ueda$ for d in * ; do ls -t $d | head -n 1 |
 xargs -I\@ -n 1 cp -p $d/\@ ./ ; done
```


<h2>Q8</h2>

次のように5個ファイルを作ります。file1をfile2, file2をfile3, file3をfile4, file4をfile5, file5をfile1にmvしてください。

```bash
uedambp:q8 ueda$ for i in 1 2 3 4 5 ; do echo $i > file$i ; done
uedambp:q8 ueda$ head *
==> file1 <==
1

==> file2 <==
2

==> file3 <==
3

==> file4 <==
4

==> file5 <==
5
```

<h2>解答</h2>

```bash
uedambp:q8 ueda$ ls | 
awk 'BEGIN{a="tmp"}{print a,$1;a=$1}END{print a,"tmp"}' | 
tail -r | awk '{print "mv",$1,$2}' | sh
uedambp:q8 ueda$ head *
==> file1 <==
5

==> file2 <==
1

==> file3 <==
2

==> file4 <==
3

==> file5 <==
4
```

