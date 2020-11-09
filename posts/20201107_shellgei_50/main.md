---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2020 Ryuichi Ueda
---

# 【問題と解答】jus共催 第50回記念我々は50回も何をやってるんだろうシェル芸勉強会

* もっとよい解答はTwitter上にあります。
    * https://togetter.com/li/1619847
* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.50)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 20.04で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

　`un.txt.gz`から、`UNITY, UNKO, unity, unko`の数をそれぞれなるべく短時間で数えてください。
単語の途中に改行が入っているものも数えてください。

### 解答例

　改行をとって`grep`すると、メモリに文字列を読みはじめて遅くなります。`a`を除去してからカウントすると早く処理できます。

```
$ time zcat un.txt.gz | grep -vE '^a+$' | sed -E 's/a+/@/g' | tr -d \\n | grep -Eio 'un(ity|ko)' | sort | uniq -c
      2 UNITY
      2 UNKO
      3 unity
      3 unko

real	0m3.585s
user	0m6.037s
sys	0m0.248s
```

## Q2

　`un.txt.gz`で`a`のみが書いてある行の行数をなるべく早くカウントしてください。

### 解答例

　`pee`などで並列処理すると時短できることができます。（ただし行が混ざることがあるので注意。）

```
### 並列なし ###
$ time zcat un.txt.gz | grep -cE ^a+$
9999985

real	0m3.445s
user	0m6.009s
sys	0m0.181s
### 並列あり ###
$ time zcat un.txt.gz | pee 'sed -n 1~2p | grep -cE ^a+$' 'sed -n 2~2p | grep -cE ^a+$' | numsum
9999985

real	0m2.739s
user	0m9.878s
sys	0m1.812s
```

## Q3


　`un.txt.gz`を展開しておきます。

```
$ zcat un.txt.gz > a
```

次のように`cat`して出力を捨てると一瞬で終わりますが、システムをワンライナーでいじって、この`cat`にかかる時間を遅くしてみてください。

```
### 普通にcatするとすぐ終わる ###
$ time cat a > /dev/null

real	0m0.124s
user	0m0.000s
sys	0m0.124s
### なにか細工をする ###
$ ワンライナー
$ time cat a > /dev/null

real	0m1.810s   ←遅くなる
user	0m0.000s
sys	0m0.413s
```

### 解答例

　ページキャッシュを開放します。

```
$ echo 1 | sudo tee /proc/sys/vm/drop_caches 
1
$ time cat a > /dev/null

real	0m1.810s
user	0m0.000s
sys	0m0.413s
```


## Q4

　1から1億までの数字をシャッフルして2列にしたデータ（ファイル名は`a`にしましょう）を作ってください。速いワンライナーを考えてください。例を示します。

```
$ head -n 5 a
30704298 56976301
61041738 68147433
99052527 91351967
63294008 15458140
3840917 37301114
```

### 解答例

　もっと速い方法があるかもしれませんが、手元の環境では`sort -R`より`shuf`、`awk`より`paste`という結果でした。

```
$ time seq 100000000 | shuf | awk 'NR%2{printf $1" "}!(NR%2)' > a

real	0m58.922s
user	1m15.053s
sys	0m3.069s
### awkよりpasteの方が速い ###
$ time seq 100000000 | shuf | paste - - | tr '\t' ' ' > a

real	0m29.393s
user	0m33.804s
sys	0m4.624s
```


## Q5

　このワンライナーを、出力の内容は変えずに高速になるように改良してください。

```
$ time cat a | sort -k2,2n > b

real	0m59.258s
user	0m54.078s
sys	0m3.841s
```


### 解答例

　`sort`にファイルを指定するだけで、`sort`がマルチスレッドで動作して速くなることがあります。


```
$ time sort -k2,2n a > b

real	0m29.940s
user	2m9.304s
sys	0m3.155s
```

## Q6

　`a`について、両方の数字が素数の行を抽出してファイルに保存してください。

### 解答例

```
$ time cat a | teip -f 2 -- factor | awk 'NF==3{print $3,$1}' | teip -f 2 -- factor | awk 'NF==3{print $3,$1}' > ans1

real	1m17.399s
user	3m1.450s
sys	0m8.649s
### 前処理して偶数のある行を消しておくと速くなります ###
$ time awk '$1%2 && $2%2' a | teip -f 2 -- factor | awk 'NF==3{print $3,$1}' | teip -f 2 -- factor | awk 'NF==3{print $3,$1}' > ans2

real	0m27.110s
user	1m14.817s
sys	0m1.727s
### teipなしの方法 ###
$ time ( awk '$1%2 && $2%2{print $1 > "b";print $2 > "c"}' a  && paste <(factor < b) <(factor < c) | awk 'NF==4{print $2,$4}' > ans3 )

real	0m32.634s
user	0m34.366s
sys	0m1.189s
```

## Q7

　`a`について、次の操作をしてください。

* 上の行からA, B, C, D, E, ..., Z, A, B, C, ...と記号をつける。
```
A 4796421 46315959
B 37830772 88906806
C 81382245 28729184
D 32681244 48378429
E 66092656 22445817
・・・
```
* 記号を与えられた数字を1行にまとめて`ans`というファイルに保存する。
```
$ awk '{print $1,$2,$3, "...", $(NF-1),$NF}' ans | head -n 3
A 4796421 46315959 ... 90741157 92659988
B 37830772 88906806 ... 70859873 22640999
C 81382245 28729184 ... 98481095 67292404
```

### 解答例

　ファイルに分けてあとからくっつけるという戦法の例を示します。

```
$ time ( yes {A..Z} | tr ' ' \\n | head -n 50000000 | paste - a | awk '{printf $2" " > $1; printf $3" " > $1}' ; grep . {A..Z} | tr : ' ' > ans)

real	0m36.832s
user	0m38.767s
sys	0m4.637s
```

## Q8

　Q7について、さらに各行の数字を小さい順にソートするという条件をつけてください。`ans2`というファイルに保存します。

```
$ awk '{print $1,$2,$3, "...", $(NF-1),$NF}' ans2 | head -n 3
A 21 41 ... 99999966 99999973
B 5 29 ... 99999946 99999958
C 11 105 ... 99999970 99999994
```

### 解答例

　`ans`のように一つにまとまったファイルをソートすると時間がかかるので、さきほど作った中間ファイルそれぞれに並列にソートをかけると早く終わります。

```
$ time ( echo {A..Z} | tr ' ' \\n | xargs -I@ -P0 bash -c "cat @ | tr ' ' '\n' | sort -n | paste -sd ' ' > s@" ; grep . s{A..Z} | tr -d s | tr : ' ' > ans2 )

real	0m22.454s
user	2m4.237s
sys	0m10.099s
```

