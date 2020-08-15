---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2020 Ryuichi Ueda
---

# 【問題と解答】jus共催 第49回ボンバイエシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.49)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu 20.04で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

なるべく自身が変態的だと思う方法で「あ」と1字出力してください。

### 解答例

```bash
$ echo a | uconv -x hiragana
あ
$ ls aaaaa |& awk -F '' '{print $(NF-4)}'
あ
echo -n い | xxd -ps | awk -F '' '{$NF-=2;print}' | tr -d ' '  |xxd -p -r
あ
$ echo -e \\U$((2*3*3*13*13))
あ
$ echo -e \\U$(dc <<< '2 3*3*13*13*p')
あ
```



## Q2

適当なディレクトリのファイルについて、ファイルの名前と更新時刻を`ls`を使わないで列挙してください。1列目にファイル名、2列目以降に時刻情報を並べてください（細かいフォーマットは任意です）。


### 解答例

```bash
$ echo *  | xargs -n 1 stat | grep -e '^ *File' -e '^Modify' | awk '$1=" "' | xargs -n 4
hoge 2020-08-12 11:21:53.941829189 +0900
howtouse.pdf 2020-06-25 16:04:08.335740178 +0900
howtouse.tex 2020-06-25 16:03:56.287740308 +0900
jrsj.cls 2020-06-25 16:03:09.899740812 +0900
rsjarrow.eps 2020-06-25 16:04:44.867739781 +0900
template.log 2020-06-25 16:08:25.287737388 +0900
template.tex 2020-06-25 16:04:19.659740055 +0900
```

## Q3

`seq 30`の出力から、なるべく自身が変態的だと思う方法で`3`のつく数だけ検索して表示してください。

### 解答例

```bash
$ seq 30 | xargs touch ; echo *3*
13 23 3 30
$ seq 30 | pee 'tail -n 21 | while read n ; do echo ${n#[^3][^3]} ; done ' 'head -n 9 | while read n ; do echo ${n#[^3]}; done' | xargs
13 3 23 30
$ seq 30 | while read n ; do case $n in *3* ) echo $n ;; esac ; done
3
13
23
30
$ seq 30 | while read n ; do if [[ $n =~ 3 ]] ; then echo $n ; fi ; done
3
13
23
30
```

## Q4

なるべく自身が変態的だと思う方法で、つぎの`echo`からワンライナーで3+4+5+6を計算してください。

```bash
echo 3+4+5+6
```

### 解答例

```bash
$ echo 3+4+5+6 | sed 's/^/echo $((/' | sed 's/$/))/' | bash
18
$ echo 3+4+5+6 | tr + \\n | xargs -n 1 seq | wc -l
18
$ echo 3+4+5+6 | tr + \\n | time xargs -n 1 sleep |& head -n 1 | sed -r 's/.*:([0-9]+)\...elapsed.*/\1/'
18
```

## Q5

なるべく自身が変態的だと思う方法で、`echo てぶくろ`から出力`ろくぶて`を得てください。

### 解答例

```bash
$ echo てぶくろ | grep -o . | while read w ; do a=$w$a ; echo $a ; done | tail -n 1
ろくぶて
$ echo てぶくろ | grep -o . | while read w ; do mkdir $w ; mv ./* $w/ 2> /dev/null ; done ; find ./ | tail -n 1 | tr -d './'
ろくぶて
```

## Q6

なるべく自身が変態的だと思う方法で、数字も`factor`も使わないで素数を小さい方から順にいくつか（10個くらいで十分）出力してください。

### 解答例


```bash
### 「^文字」はCtrl+V+文字で打ち込みます ###
$ echo -n ^B^C^E^G^K^M^Q^S^W^]^_ | xxd -ps | grep -o .. | awk 'BEGIN{a=NR}{print a"x"$NF}' | xargs printf "%d\n"
2
3
5
7
11
13
17
19
23
29
31
```

## Q7

なるべく自身が変態的だと思う方法で、0から9までの数字を順番に出力してください。前の解答例の方法は使わないでください。ワンライナー中で数字は使わないでください。余計な文字は出力しないでください。

### 解答例

```bash
### 失敗する可能性がありますが ###
$ ls /proc/ | grep -o .$ | sort -u | head 
$ cat /etc/passwd | nl | grep -oP '.\t' | head | sort
$ cat /etc/services | tr -dc '[:digit:]' | grep -o . | sort -u
```

## Q8

次の`unko`ファイルから、「うんこ」とある行の行番号を、なるべく自身が変態的だと思う方法で出力してください。ワンライナー内で日本語の文字を使うことは禁止です。

```bash
$ cat unko 
んこうんこううんうこうんんこうこんんこう
んこここんこうこうんこうこうんんこうんこ
うこううんうここうこんんんうんううんんこ
んんんこここううううんこんこんうこうこう
んこうんんんううこううううこうここうんん
んここうこんうここうんううんこうんこうう
うこうんここここんんうこここここここんこ
うこうこここうんんううううんここうこんう
ここうんうんんんんこうこんううんんこんう
んうううここんここここううこんんんうんう
んこうんんこんううんうんこんんうんこんん
んんうここうこううこううんんうこうこうん
こううこううここんんこんううんうんんんう
こうこうんんんこんこんんううんんんこんこ
んんんこうんうこうここうんこここうんこん
```

### 解答例

```bash
$ cat unko | awk -F '' '{for(i=1;i<=NF-2;i++)if($i<$(i+1) && $i<$(i+2) && $(i+2)<$(i+1))print NR}' | uniq
1
2
4
6
7
8
11
15
$ head -c 9 unko | xargs -I@ sed 'y/@/abc/' unko | grep -n cab | sed 's/:.*//'
1
2
4
6
7
8
11
15
```
