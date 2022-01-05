---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2021 Ryuichi Ueda
---

# 【問題と解答】jus共催 第57回シェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.57)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu 20.04 LTSで作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

次のファイルから今の元号の数を数えてください。

```bash
$ cat reiwa
令和昭和令和大正令和明治大正享保
令和昭和平成令和令和応和令和令和
令和大正大正昭和令和平成令和令和
令和元禄文久昭和大正天保令和令和
令和安政安永弘化慶応令和令和令和
令和平成平成明治宝暦元和正保慶安
```

### 解答例

「令」は2つUnicodeのコードポイントを持っています。

```bash
$ cat reiwa | grep -o '['$'\U4EE4\UF9A8'']和' | wc -l
20
```

## Q2

次のファイルの中の旧字体の漢字を、新字体に変換してください。

```bash
$ cat kanji2
寫眞
星圖
學校
鐵道
鐵砲彈
燈臺
兩腕
```

### 解答例

「星図」が「製図になっちゃいましたが、ご愛嬌ということで・・・。

```bash
$ cat kanji2 | nkf -s | kakasi -JH | nkf | kkc | sed -E 's;/[^<]+<;;g' | grep -oP '<.*?/' | tr -d '</'
写真
製図
学校
鉄道
鉄砲弾
灯台
両腕
```

## Q3

次のファイルから、日本語にない漢字を抽出してください。

```bash
$ cat kanji
无产阶级文化大革命，通称文化大革命、简称文革，是中华人民共和国历史上的一场政治運動

文化大革命 | Wikipedia（https://zh.wikipedia.org/wiki/文化大革命）
https://zh.wikipedia.org/wiki/Wikipedia:CC_BY-SA_3.0协议文本
```

### 解答例

```
cat kanji | grep -o . | mecab -Oyomi  | grep -P '\p{Han}'
```

## Q4

次のファイル内の漢字を簡体字に変換してください。


```
$ cat hongkong
西營盤站
香港大學站
荃灣站
黃大仙站
鑽石山站
觀塘站
```

### 解答例

```
$ bzcat /usr/share/unicode/Unihan_Variants.txt.bz2 | grep Simpli | sed 's/U+//g' | awk '{print "echo -e s/\\\\U"$1"/\\\\U"$3"/g"}' | bash | grep -v '#' | sed -f- hongkong
西营盘站
香港大学站
荃湾站
黄大仙站
钻石山站
观塘站
$ bzcat /usr/share/unicode/Unihan_Variants.txt.bz2 | sed 's/U+/0x/g' | grep -v '[#<]' | tr '\t' ' ' |awk NF| grep Simpli | opy '["s/"+chr(F1)+"/"+chr(F3)+"/"]' | sed -f- hongkong
西营盘站
香港大学站
荃湾站
黄大仙站
钻石山站
观塘站
```


## Q5

次のシェルスクリプトについて`./hoge.bash &`を実行の後、1番目の`date`の実行から2番目の`date`の実行を40秒以上あとに遅らせてください。

```
$ cat hoge.bash 
#!/bin/bash

date
sleep 30
date
```

### 解答例

```
$ kill -SIGSTOP $! ; sleep 40 ; kill -SIGCONT $!
```

## Q6

### 小問1

　次のような手続きを実行すると、ある時点で`grep`が終わらなくなります。

```bash
$ echo うんこ > unko
$ grep うんこ unko | cat >> unko
$ grep うんこ unko | cat >> unko
$ grep うんこ unko | cat >> unko
・・・
$ grep うんこ unko | cat >> unko
（止まらなくなる）
```

この`grep`を直接Ctrl+Cや`kill`せず、`unko`ファイルに細工をする方法で止めてください。

### 小問2

　できた人は、次の`while`文を止めてみてください。

```bash
$ echo うんこ > unko
$ while grep うんこ unko | cat >> unko ; do : ; done
```

### 解答例

　小問1のは、

```bash
$ echo : > unko
```

で止まります。`rm unko`では、ファイルの実体が消えないので止まりません。

　小問2のは、

```bash
$ chmod 000 unko
$ echo | sudo tee unko
```

で止まります。（環境によっては違うかもしれません。）

## Q7

`x^8 - y^8`を因数分解してください。できた人は`sin x`をテイラー展開でもしててください。

### 解答例

```bash
$ echo 'display2d:false;factor(x^8 - y^8);' | maxima

Maxima 5.43.2 http://maxima.sourceforge.net
using Lisp GNU Common Lisp (GCL) GCL 2.6.12
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1)
(%o1) false
(%o2) -(y-x)*(y+x)*(y^2+x^2)*(y^4+x^4)
$ echo 'factor(x^8 - y^8)' | gp -f -q

[    x - y 1]

[    x + y 1]

[x^2 + y^2 1]

[x^4 + y^4 1]
```

\\[sin x\\]のテイラー展開

```bash
$ echo 'sin(x)' | gp -f -q
x - 1/6*x^3 + 1/120*x^5 - 1/5040*x^7 + 1/362880*x^9 - 1/39916800*x^11 + 1/6227020800*x^13 - 1/1307674368000*x^15 + O(x^17)
```

## Q8

`7/17`を小数になおすと循環小数（ある桁以降が同じ数字の並びの繰り返しになる小数）になります。繰り返される数字の並びについて、最短のものを求めてください（循環の始まる先頭は捉えなくてかまいません）。

### 解答例

`7/17`の場合はこれで大丈夫です。最短一致で切り出した後、最長のものを求めます。

```bash
$ echo 'scale=100;7/17' | bc -l |tr -d '\\ \n'| awk 4 | grep -Po '(\d+?)\1' | awk '{print length,$0}' | sort -k1,1nr | head -n 1 | awk '{print $2}' | sed -E 's/([0-9]+)\1$/\1/'
4117647058823529
```
