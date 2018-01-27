---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】jus共催 第33回めでたいシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.33)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

適当にディレクトリを作り、その中で `tree` したら次のような出力が得られるようにしてください。（日本語環境でないとうまくいかないのでご了承ください。）

```bash
$ tree
.
└── 💩
    └── 💩
        └── 💩
            └── 💩
                └── 💩
                    └── 💩
                        └── 💩
                            └── 💩
                                └── 💩
                                    └── 💩
```

### 解答

```bash
$ echo '💩/' | perl -nle 'print $_ x 10' | xargs mkdir -p
```

## Q2

次のような出力を得てください。

```bash
合計 0
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06  ___________________
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06 < Eat American beef >
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06  -------------------
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06         \   ^__^
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06          \  (oo)\_______
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06             (__)\       )\/\
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06                 ||----w |
-rw-rw-r-- 1 ueda ueda 0  1月 26 12:06                 ||     ||
```

### 解答

```bash
$ cowsay 'Eat American beef' | sed "s/^/\'/" | sed "s/$/\'/" |
sed 's;/;@;' | awk '{print ;system("sleep 1")}' |
xargs -n1 touch ; ls -trl | sed 's;@;/;g'
```



## Q3

空のディレクトリを用意して、その中に、次のようにファイルを10個置いてください。中身は空で構いません。ちょっと都合が良い条件ですが、「`touch あいうえお・・・`」とベタ打ちするのは禁止でお願いします（数個ひらがなや全角文字を打つのは可）。

```bash
$ ls
あいうえお  さしすせそ  なにぬねの  まみむめも  らりるれろ
かきくけこ  たちつてと  はひふへほ  や　ゆ　よ  わをん
```

### 解答

```bash
$ echo {177..220} 166 221 | tr ' ' '\n' | xargs -n1 printf "\\\\\\\\x%x\n" 
| xargs echo -e | tr -d ' ' | nkf --hiragana | sed 's/[やゆ]/&　/g' |
sed 's/ら/\n&/' | fold -b15 | xargs touch
```

## Q4

https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.33/kiken
の中にあるファイルについて、ファイル名とファイルの中身を入れ替えてください。スラッシュがある場合にはディレクトリを作ってください。ワンライナー中でファイル名やファイルの中身を直接使わないでください。

### 解答


```bash
$ ls | while read f ; do echo $f > "$(cat $f)" ||
( mkdir -p $(dirname $(cat $f)) && echo $f > $(cat $f) ) ; rm $f ; done
```

## Q5

https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.33/yabai
の中にあるファイルの数を数えてください。

### 解答

普通にやろうとすると間違えます。（環境依存かもしれません。）

```bash
$ ls | wc -l
46
```

正解例はこちらです。

```bash
$ ls -b | wc -l
3
```


## Q6 

何かディレクトリを作って、その中に100万個ファイルを作ってください。ファイルの名前に使えるのはひらがな、漢字、カタカナのいずれかとします。

### 解答

```bash
$ seq 0 999999 | sed 'y/0123456789/あいうえおかきくけこ/' | xargs -P2 touch
```

## Q7 

ファイル名が半角スペース等、見えない字で構成されるファイルを100万個作ってください。

### 解答

sed yの置換後の空白は、半角スペース+全角スペースです。

```bash
$ seq 1000000 | sed '1iobase=2;ibase=10' | bc | sed 'y/01/ 　/' |
sed "s/^/\'/" | sed "s/$/\'/" | xargs touch
```

## Q8

yabaiディレクトリの中の各ファイルに、各ファイル名の改行の数（=ファイル名の長さ）を書き込んでください。ワンライナーなら何を使っても良いです。bashにこだわると解けないかもしれません。

### 解答

bashは断念。perlで。


```bash
$ perl -e '@a=glob("*"); foreach $v(@a){open(f,">",$v) or die "!";print f;print f length($v);print f "\n"}'
### 確認（・・・になってないような気もしないでもない） ###
$ cat *
4
7
32
$ ls -l
合計 12
-rw-rw-r-- 1 ueda ueda 2  1月 26 10:54 ????
-rw-rw-r-- 1 ueda ueda 2  1月 26 10:54 ???????
-rw-rw-r-- 1 ueda ueda 3  1月 26 10:54 ????????????????????????????????
```
