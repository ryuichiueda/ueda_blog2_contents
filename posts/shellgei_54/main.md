---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2021 Ryuichi Ueda
---

# 【問題と解答】jus共催 第54回生ぬるいシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.54)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu 20.04 LTSで作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

つぎの`oraora.txt`から、「おらおら」など、ある2文字が2回繰り返される単語が2個ある行を、行番号とともに抽出してください。3個以上ある行は抽出しないでください。

```
$ cat oraora.txt
おらおらほいへいおらおらへいおらへい
へいへいおらへいおらへいへいおらおら
ぺいぺいぽいぺいぽいぺいぽいぺいぽい
ぺぺいぺいぽいぽいおらほらぺぺいぽい
ぺいぺいぽいぽいおらおらおらおらおら
```

### 解答例

```
$ cat oraora.txt | grep -Pn '(..)\1.*(..)\2' | grep -Pv '(..)\1.*(..)\2.*(..)\3'
1:おらおらほいへいおらおらへいおらへい
4:ぺぺいぺいぽいぽいおらほらぺぺいぽい
```

## Q2

つぎの`kouun.txt`から、矢印が向いている単語だけを抽出してください。順番は変わっても構いません。

```
$ cat kouun.txt
耕運
↑
幸運
↓
運行
↑
運賃
↓
沈降
↓
うんこ
↑
ウコン
```

### 解答例

```
$ cat kouun.txt | pee 'grep -A1 ↓ ' 'grep -B1 ↑' | grep -v '[-↓↑]' | sort -u
うんこ
運行
耕運
沈降
$ cat kouun.txt | xargs | awk '{for(i=1;i<=NF;i++)if($(i+1)=="↑" || $(i-1)=="↓")print $i}'
耕運
運行
沈降
うんこ
$ cat kouun.txt | grep -zPo -e  '(.*\n↑|↓\n.*)' | sed 's/[↑↓]//g' | tr -d \\0 | awk NF
耕運
運行
沈降
うんこ
```

## Q3

`human.txt`について、男性を表すアイコン、女性を表すアイコンの数をそれぞれ数えてください。

```
$ cat human.txt
👩‍👩‍👧‍👦👨‍👨‍👧‍👦👨‍👩‍👧👨‍👩‍👦‍👦👨‍👨‍👦
```

### 解答例

```
$ cat human.txt | uniname 2> /dev/null | grep ' 01' |
awk '{print substr($3,6)}' | awk '$1%2{print "female"}!($1%2){print "male"}' | sort | uniq -c
      7 female
     11 male
```

## Q4

あ行、か行、さ行・・・わ行の文字の数をそれぞれ求めてください。0個の行は出力する必要はありません。

```
$ cat yoko.txt
よこはまよこすかかみおおおかほりのうちこやす
```

### 解答例


```
$ cat yoko.txt | uniname 2> /dev/null | awk 'NF==10{print substr($10,1,1)}' |
tr IUEO AAAA | sort | uniq -c | sed 'y/AKSTNHMYRW/あかさたなはまやらわ/' | sort -k2,2
      4 あ
      6 か
      2 さ
      1 た
      1 な
      2 は
      2 ま
      3 や
      1 ら
```

## Q5 


### 小問1

https://github.com/NAalytics/Assemblies-of-putative-SARS-CoV2-spike-encoding-mRNA-sequences-for-vaccines-BNT-162b2-and-mRNA-1273/blob/main/Figure1Figure2_032321.fasta
にあるファイルから、同じ記号が最も長く続いている部分が何行目にあるか、探してください。行をまたいでいるデータをつなぎあわせて探す必要はありません。

ただし、行をまたいでいる可能性も考慮してください。そして、最後にAが続いている部分は無視してください。

ファイルは、次のようにダウンロードしましょう。ファイルは、

```
$ curl https://raw.githubusercontent.com/NAalytics/Assemblies-of-putative-SARS-CoV2-spike-encoding-mRNA-sequences-for-vaccines-BNT-162b2-and-mRNA-1273/main/Figure1Figure2_032321.fasta > a
```

と保存してから解答をしましょう。

### 小問2

データが行をまたいでいることも考慮して、同じ記号が最も長く続いている部分が何行目（〜何行目）か、探してください。

### 解答例

#### 小問1

```
$ nkf -wLux a | grep -Eo '(.)\1+' | awk '{print length,$0}' | sort -n |
sed -n '$s/.* //p' | xargs -I@ grep -n @ <(nkf -wLux a)
106:GGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAA
```

#### 小問2

```
$ nkf -wLux a | tr -d \\n | grep -Eo '(.)\1+' | awk '{print length,$0}' |
sort -n | sed -n '$s/.* //p' | sed 's/./&\\\\n?[0-9]*:?/g' | sed 's/^/\[0-9\]*:.*/'  |
xargs -I@ grep -zPo @ <(nkf -wLux a | grep -n '') | sed '$d'
106:GGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAA
107:AAAA
```

## Q6

次の`jugem.txt`から、


```
$ cat jugem.txt
寿限無寿限無五劫のすりきれ海砂利水魚の水行末雲来末風来末食う寝るところに住むところやぶらこうじのぶらこうじパイポパイポパイポのシューリンガンシューリンガンのグーリンダイグーリンダイのポンポコピーのポンポコナの長久命の長助
```

次のような出力を得てください。

```
寿水行ころパイーリンポ
限の末とやポポグンポコ
無魚雲むぶイののダのナ
寿水来住らパシンイーの
限利末にこポュガグピ長
無砂風ろうイーンーコ久
五海来こじパリリリポ命
劫れ末とのじンーンンの
のき食るぶうガュダポ長
すりう寝らこンシイの助
```

### 解答例

```
$ cat jugem.txt | grep -oE '.{10}' | sed -n '1~2p;2~2s/.*/echo & |
rev/ep' | sed 's/./& /g' | rs -T | tr -d ' '
寿水行ころパイーリンポ
限の末とやポポグンポコ
無魚雲むぶイののダのナ
寿水来住らパシンイーの
限利末にこポュガグピ長
無砂風ろうイーンーコ久
五海来こじパリリリポ命
劫れ末とのじンーンンの
のき食るぶうガュダポ長
すりう寝らこンシイの助
```


## Q7

次の`nejineji.txt`の文を1行にしてください。

```
$ cat nejineji.txt
寿限無寿限無五劫のすりきれ
　　　　　　　　　　　　海
じのぶらこうじパイポパ　砂
う　　　　　　　　　イ　利
こ　グーリンダイグ　ポ　水
ら　の　　　　　ー　パ　魚
ぶ　ン　コピー　リ　イ　の
や　ガ　ポ　　　ン　ポ　水
ろ　ン　ンポのイダ　の　行
こ　リ　　　　　　　シ　末
と　ーュシンガンリーュ　雲
む　　　　　　　　　　　来
住にろことる寝う食末来風末
```


### 解答例

AWKの再帰を使います。

```
$ cat nejineji.txt | sed '1i　　　　　　　　　　　　　　　' |
sed '$a　　　　 　　　　　　　　　' | sed 's/^/　/;s/$/　/' |
awk -F '' 'function f(x,y){if(a[x][y]!="　"){printf a[x][y];a[x][y]="　";
f(x-1,y);f(x+1,y);f(x,y-1);f(x,y+1)}}
{for(i=1;i<=NF;i++)a[i][NR]=$i}END{f(2,2)}' | awk 4
寿限無寿限無五劫のすりきれ海砂利水魚の水行末雲来末風来末食う寝るところに住むところやぶらこうじのぶらこうじパイポパイポパイポのシューリンガンシューリンガンのグーリンダイグーリンダイのポンポコピー
```
