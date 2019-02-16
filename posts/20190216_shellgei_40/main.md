---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2019 Ryuichi Ueda
---

# 【問題と解答】jus共催 第40回光明⭐️節シェル芸勉強会


* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.40)にあります。クローンは以下のようにお願いします。
* もっと良い解答例がTwitter上にあります。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

ウェブからデータを拝借して、金日成、金正日、金正恩の誕生日をワンライナーで列挙してください。

### 解答例

```
$ for kim in 金{正恩,正日,日成} 上田隆一;
do echo $kim ; w3m -dump https://www.google.com/search?q=$kim+誕生日 |
grep -o "生年月日：.*.*年.*月.*日" ; done | xargs -n 3 | awk '{print $1,$3}'
金正恩 1984年1月8日
金正日 1941年2月16日
金日成 1912年4月15日
上田隆一 1978年2月16日
```

## Q2

2月16日は、2も16も2のべき乗で、2と1と6を足すと3のべき乗になります。このような日付は他にあるでしょうか？（0乗になる数は除く）

### 解答例

次の通り他にはなく、2月16日の神聖さが分かるかと思います。

```
$ seq -w 9999 | awk '{print 2020$1}' |
date -f- "+%-m %-d" 2> /dev/null |
awk '{print $1,$2,log($1)/log(2), log($2)/log(2)}' |
grep -v -F . | awk '$3!=0&&$4!=0{print $1,$2}' |
sed 's/[0-9]/& /g' | awk '{print $1,$2$3,log($1+$2+$3)/log(3)}' |
grep -v -F . | awk '{print $1,$2}'
2 16
```


## Q3

イランを基準としたとき、北朝鮮時間が何時間進んでいるか、ワンライナーで求めてください。

### 解答例

```
$ echo -e Asia/Tokyo\\nAsia/Tehran |
while read a ; do TZ=$a date +%:z ; done |
sed -e 's/:00/.0/' -e 's/:30/.5/' |
sed 's/0//' | xargs | awk '{print $1-$2}'
5.5
```

## Q4

GitHubのリポジトリにあるファイル`name`はKPS 9566という文字コードで文字（2バイト文字）をいくつかバイナリで入れたものです（ヘッダやエスケープのようなバイナリは入っていません）。リポジトリには、`KPS9566-ISO2022KR`というファイルもあります。このファイルは、いくつかの文字について、KPS 9566とISO-2022-KRの対応を書いたものです。`name`に記録された文字を表示してください。

```
$ cat name | xxd -ps | fold -b4 | tr a-f A-F |
awk '{print $1,NR}' | sort | join - KPS9566-ISO2022KR |
sort -k2,2 | awk '{print $3}' | tr -d '\n' |
sed 's/^/0x1B2429430E/g'  | xxd -r | iconv -f ISO2022KR
김김김
```


## Q5

次の出力から始めて、ランダムに3文字を組み合わせて1つ出力するワンライナーを考えてください。毎回出力が違うようにしてください。また、同じ文字がちゃんと選ばれるようにしてください。

```
$ echo 正日金成恩男
```

### 解答例

```
$ echo 正日金成恩男 | grep -o . |
awk 'FILENAME=="-"{a[NR]=$1}
FILENAME!="-"{printf a[$1];if(NR>8){print "";exit(0)}}' \
- <(cat /dev/urandom | tr -dc '1-6' | fold -b1)
```

もう一つ。ちょっと手抜きしたもの。

```
$ echo 正日金成恩男 | awk '{for(i=1;i<100;i++)print}' |
grep -o . | shuf | head -n 3 | tr -d \\n | awk 4
```

## Q6

北朝鮮選手団が夏季オリンピックで獲得したメダル数について、
西暦年、オリンピック名、金銀銅の種別、枚数の一覧表を作ってください。
不参加の年はゼロ枚とします。
（ネットから情報を拝借するときは、
あんまりcurlしすぎないように一度ファイルに落としましょう。）

* 出力の例

```
1972 ミュンヘン 金 1
1972 ミュンヘン 銀 1
1972 ミュンヘン 銅 3
...
```

### 解答例

```
$ curl https://ja.wikipedia.org/wiki/オリンピックの北朝鮮選手団 > a
$ w3m -dump -T text/html < a | sed -n '/1972 ミュンヘン/,/2016 リオデ/p' |
sed 's/不参加/0 0 0/' |
awk '{k=$1" "$2;g[k]=$3;s[k]=$4;c[k]=$5}
END{for(k in g){print k,"金",g[k];print k,"銀",s[k];print k,"銅",c[k]}}' |
sort
```

## Q7

https://github.com/mandatoryprogrammer/NorthKoreaDNSLeak のファイルから.kpドメインを持つホストの一覧を作ってください。

### 解答例

```
$ git clone https://github.com/mandatoryprogrammer/NorthKoreaDNSLeak
$ cat NorthKoreaDNSLeak/* | tr '\t' ' ' |
grep 'IN A' | awk 'NF==5{print $1,$5}' | sort -u
```

## Q8

「朝鮮民主主義人民共和国」の総画数を求めてください。

### 解答例

* http://kanji-database.sourceforge.net/database/strokes.html

```
$ cvs -z3 -d:pserver:anonymous@a.cvs.sourceforge.net:/cvsroot/kanji-database co -P kanji-database
$ cat kanji-database/data/ucs-strokes.txt |
sed -r 's/U\+([0-9A-F]+)\t/\&#x\1; /g' |
nkf --numchar-input |
awk 'FILENAME=="-"{a[$1]=$2}FILENAME~/fd/{print a[$1]}
' - <(grep -o . <<< 朝鮮民主主義人民共和国) | numsum
86
```

