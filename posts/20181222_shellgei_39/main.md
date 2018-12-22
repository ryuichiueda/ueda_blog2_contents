---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2018 Ryuichi Ueda
---

# 【問題と解答】jus共催 第39回コートなしで自宅から締め出されたりしないでね年末シェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.39)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

つぎのマークダウンの原稿`wrong.md`は、画像やURLのリンク方法が間違っています。修正してください。一般解は考えなくていいです。
（例: `![fig5.png](図5)` を`![図5](fig5.png)に変換`）

```wrong.md
# わたしはマークダウソちょっとできる

## 軍馬県高崎市

[https://ja.wikipedia.org/wiki/%E7%BE%A4%E9%A6%AC%E7%9C%8C](軍魔県)は、日本の県庁所在地の一つ。県庁所在地は(高崎市)[https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B4%8E%E5%B8%82]

* (https://ja.wikipedia.org/wiki/%E6%9D%BE%E4%BA%95%E5%B8%B8%E6%9D%BE)[松井常松]
* [http://takasakiham.com/?transactionid=8e5164a76108c8411e7547d69e0dd0fd443f072a](高崎ハム)


![群馬県高崎市市章.svg](たかさきしししょう)
```

### 解答例

```
$ cat wrong.md | sed 's;\(([^(]*)\)\(\[.*\]\);\2\1;g' |
sed 's/\[\([h群][^[]*\)\](\([^[]*\))/[\2](\1)/g' 
```

## Q2

次のファイル`attendee.md`について、34回から38回の順に並び替え、さらに各回のデータを福岡、大阪、東京の順に並び替えてください。

```attendee.md

* 第38回シェル芸勉強会
    * 東京: 26
    * 大阪: 8
    * 福岡: 3
* 第36回シェル芸勉強会
    * 東京: 38
* 第35回シェル芸勉強会
    * 大阪: 10
    * 東京: 27
* 第34回シェル芸勉強会
    * 大阪: 16
    * 東京: 19
* 第37回シェル芸勉強会
    * 東京: 21
    * 大阪: 10
    * 福岡: 8
```

### 解答

```
$ cat attendee.md |
awk '/第/{n=gensub(/[^0-9]+/,"", "g");print n, 0, $0}!/第/{print n, /福岡/?1:/大阪/?2:3, $0}' |
sort -k1,2n | sed 's/.....//'
* 第34回シェル芸勉強会
    * 大阪: 16
    * 東京: 19
* 第35回シェル芸勉強会
    * 大阪: 10
    * 東京: 27
* 第36回シェル芸勉強会
    * 東京: 38
* 第37回シェル芸勉強会
    * 福岡: 8
    * 大阪: 10
    * 東京: 21
* 第38回シェル芸勉強会
    * 福岡: 3
    * 大阪: 8
    * 東京: 26
```

## Q3

`wget 'https://www.google.com/'`して`index.html`をダウンロードしましょう。上の方に

```
<meta content="&#19990;&#30028;&#20013;&#12398;&...
```
というmeta要素があるので、このメッセージを読んでみてください。（日本語環境でないと簡単かもしれません。）

### 解答

```
$ cat index.html  | sed 's/</\n</g' | grep -m1 '<meta' | nkf --numchar-input
```

## Q4

`index.html`からstyle要素を`index.css`、script要素を`index.js`ファイルに保存してください。タグは取り払ってください。適切な場所に改行が入っても構いません。無理にワンライナーでやる必要はありません。

```
$ cat index.html | sed 's/<[^<]*>/\n&\n/g'  |
awk '/^<script/,/^<\/script>/{print > "index.js"}/^<style/,/^<\/style/{print > "index.css"}' ;
sed -i 's/<[^<]*>//' index.css index.js
```


## Q5

さらに、`index.html`からこれらの要素を取り除いた`index_no_cssjs.html`を作ってください。今度は改行等、余計な文字は入れないでください。

### 解答

script要素内に`<`がひとつ居るので、`<script[^<]*>[^<]*</script>`だとダメです。（`perl`を使えば`<script`から`</script>`までを最短一致させられるので一般解が得られると思いますが、私は力尽きました・・・）


```
$ cat index.html | sed -z 's;<script[^<]*>[^>]*</script>;;g' |
sed -z 's;<style[^<]*>[^<]*</style>;;g' > index.no_cssjs.html
```

## Q6

`main.js`において16進数等でエスケープされている字を復元してください。余力のある人はインデント等をつけて整形してみてください。（便利なツールがあったらそれも教えてください...）


### 解答

```
$ sed 's/\\\\u\(....\)/\&#x\1;/g' index.js | nkf --numchar-input | nkf --numchar-input | sed 's/\\x22/"/g' | sed 's/\\x3d/=/g' | sed 's/\\\\/\\/g'
```

## Q7

次のマークダウンのテーブル`table.md`について、縦と横を入れ替えたマークダウンのテーブルを作ってください。

```table.md
|回       |年月    |人数   |
|---------|--------|------:|
|38回     |201811  |37     |
|37回     |201809  |39     |
|36回     |201807  |38     |
|35回     |201804  |37     |
|34回     |201803  |35     |
|33回     |201801  |40    |
|32回     |201712  |39    |
|31回     |201710  |37     |
|30回     |201708  |46     |
|29回     |201706  |55    |
```


### 解答

```
$ cat table.md | awk -F'|' '!/-/{print $2,$3,$4}' | sed 's/  */\t/g' | datamash transpose | awk NF | sed 's/\t/|/g' | sed 's/^/|/;s/$/|/' | awk 'NR==1{print;gsub(/[^|]/,"-");print}NR>1'
```

## Q8 

ファイル`yabatanien`を使って、色を変えて次のように表示してみてください。色を厳密に合わせる必要はありません。

![yabatanien](yabatanien.mov)

### 解答

```
$ seq 0 7 | awk '{print "s/"$1"m/"($1+1)%8"m/g"}' | tac  |
sed -f - yabatanien > b ; while sleep 1 ; do clear ; cat yabatanien ; sleep 1 ; clear ; cat b ; done
```
