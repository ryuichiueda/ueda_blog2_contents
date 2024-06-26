---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2019 Ryuichi Ueda
---

# 【問題と解答】jus共催 第41回{ウン,ガク,}{チ,ト,}{,ン}{,コイン}{ブ,}{ラブラ,ハ,}{,イブ}{無,有}罪シェル芸勉強会


* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.41)にあります。クローンは以下のようにお願いします。
* もっと良い解答例がTwitter上にあります。（本ページのリンク集を参照のこと。まだ作ってませんが。）

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

　次のファイルについて、2列目をキーにしてエクセルの横列の記号（A, B, ..., Z, AA, AB, ...のやつ）順に並べ替えてください。

```
$ cat excel
114514 B
1192296 AA
593195 CEZ
4120 TZ
999 QQQ
```

### 解答例

```
$ cat excel | awk '{print $1,$2,length($2)}' |
sort -k3,3n -k2,2 | awk '{print $1,$2}'114514 B
593195 AA
4120 TZ
1192296 CEZ
999 QQQ
```

## Q2

　次のファイルのレコードを干支順にソートしてください。

```
$ cat eto_yomi
申 さる
子 ね
寅 とら
卯 う
巳 み
辰 たつ
丑 うし
酉 とり
戌 いぬ
亥 い
午 うま
未 ひつじ
```

ただし、次のファイルを補助に使って良いこととします。


```
$ cat eto
子丑寅卯辰巳午未申酉戌亥
```

### 解答例

```
$ grep -o . eto | awk '{print $1,NR}' |
awk '{a[$1]=a[$1]" "$2}END{for(k in a){print k,a[k]}}' - eto_yomi |
sort -k2,2n | awk '{print $1,$3}'
子 ね
丑 うし
寅 とら
卯 う
辰 たつ
巳 み
午 うま
未 ひつじ
申 さる
酉 とり
戌 いぬ
亥 い
```

## Q3

　次のファイルのレコードを数字（第一フィールドの計算結果）が小さい順に並べてください。

```
$ cat kim_calc
1+2+4 金正日
4*3 金正男
3-1-5 金日成
495/3 金正恩
0x1F 金正哲
```

### 解答例

```
$ cat kim_calc |
while read a b ;
do [ ${a:0:2} = 0x ] && printf "%d %s %s\n" $a $a $b || echo $(bc <<< $a) $a $b ;
done | sort -k1,1n | awk '{print $2,$3}'
3-1-5 金日成
1+2+4 金正日
4*3 金正男
0x1F 金正哲
495/3 金正恩
```

## Q4

　次のファイルはシフトJISのテキストですが、これを1) 辞書順、2) 数字の小さい順、にソートしてください。出力もシフトJISとします。

```
$ cat sjis | nkf -g
Shift_JIS
$ cat sjis | nkf -wLux
１２３ ずんごるももう
３１ こきたてひーひー
９ ほじぱんふんじこみ
２２４２ たまもとやろう
```

* ケツダイラ出典: http://sledge-hammer-web.my.coocan.jp/ketsu-gaward.htm

### 解答例

#### 小問1

　辞書順は`LANG=C`などでバイナリの順にソートすれば大丈夫です。

```
$ cat sjis | LANG=C sort
?P?Q?R ???񂲂??????
?Q?O ?ق??ς?ӂ񂶂???
?Q?Q?S?Q ???????Ă???????Ƃ?܂?
?R?P ???????ĂЁ[?Ё[
$ cat sjis | LANG=C sort | nkf -wLux  #確認
１２３ ずんごるももう
２０ ほじぱんふんじこみ
２２４２ うえってきたかるとらまん
３１ こきたてひーひー
```

#### 小問2

　全角から半角を`nkf`、半角から全角を`uconv`で変換した例です。

```
$ cat sjis | nkf -Z | sort -n |
uconv -x Halfwidth-Fullwidth |
sed 's/　/ /' | nkf -sLwx
?Q?O ?ق??ς?ӂ񂶂???
?R?P ???????ĂЁ[?Ё[
?P?Q?R ???񂲂??????
?Q?Q?S?Q ???????Ă???????Ƃ?܂?
$ cat sjis | nkf -Z | sort -n |
uconv -x Halfwidth-Fullwidth |
sed 's/　/ /' | nkf -sLwx | nkf  #確認
２０ ほじぱんふんじこみ
３１ こきたてひーひー
１２３ ずんごるももう
２２４２ うえってきたかるとらまん
```

## Q5

　サイズの小さい順にソートしてください。

```
$ cat size 
2GB
1.2GB
40000MB
1000000000kB
0.4GB
410MB
```

### 解答例

　もっといい解答ないですかっ？（`sort -h`は使えないっぽいです）

```
$ cat size | sed -r 's/([0-9.]+)(..)/\1\2 \1 \2/' |
sed -e 's/ kB/*1000/' -e 's/ MB/*1000000/g' -e 's/ GB/*1000000000/' |
while read a b; do echo $a $(bc <<< $b) ; done | sort -k2,2n | sed 's/ .*//'
0.4GB
410MB
1.2GB
2GB
40000MB
1000000000kB
```

## Q6

　`sleep`と内部コマンドだけを使って次の数を小さい順にソートしてください。

```
$ cat nums
5.4
0.34
2.3
0.9
6
```

### 解答例

``` 
$ while read n ; do ( sleep $n && echo $n & ) ; done < nums
``` 

## Q7

　次のローマ数字をソートしてください。

```
$ cat roman
IV
XI
LXXXIX
IX
XLIII
XX
VIII
```

### 解答例

```
$ cat roman | sed 's/.*/& &/' |
awk '{sub(/IV/,"IIII",$2);sub(/IX/,"VIIII",$2);sub(/XL/,"XXXX",$2);print}' |
awk '{sub(/L/,"Y",$2);print}' | sort -k2,2 | awk '{print $1}'
```


## Q8

　次のファイルを辞書順にソートしてください。ただし、濁点がついているものが先に来るようにしてください。できる人はワンライナー中で「かきくけこがぎぐげご」の文字を使わないでください。

```
$ cat gagigugego 
かき氷
ぎ・おなら吸い込み隊
きつねうどん
ぐりこもりなが事件
きききりん
がきの使い
くその役にも立たない
げんしりょく発電
ごりらいも
こじんてきにはクソ
```


* 例

```
がきの使い
かき氷
ぎ・おなら吸い込み隊
きききりん
きつねうどん
ぐりこもりなが事件
くその役にも立たない
げんしりょく発電
ごりらいも
こじんてきにはクソ
```

### 解答例

```
$ cat gagigugego |
python3 -c 'import unicodedata, sys;[print(unicodedata.normalize("NFD", s.rstrip())) for s in sys.stdin]' |
sort | nkf --ic=UTF8-MAC
がきの使い
かき氷
ぎ・おなら吸い込み隊
きききりん
きつねうどん
ぐりこもりなが事件
くその役にも立たない
げんしりょく発電
ごりらいも
こじんてきにはクソ
```
