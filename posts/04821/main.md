---
Keywords: シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【解答】年末年始シェル芸問題集
<a href="/?post=04852" title="【問題】年末年始シェル芸問題集" target="_blank">年末出したシェル芸の問題</a>の私の解答です。ただ、挑戦した皆さんの解答の方が面白いし鋭いので、「シェル芸」で検索してみてください。あとで下の方に皆さんの解答例を掲載していこうと思います。

<h2>Q1</h2>


年末年始はディレクトリの掃除をしましょう。ということで、ご自身のPCから重複しているデータを探してみてください。全てのファイルから探すのは大変なので、手始めに重複しているJPEG画像リストを作ってみてください。

<!--more-->

### 解答例

もし何も出てこなかったら適当なjpegファイルをコピーして検出できるか試してみてください。「sed 's/.*/"&"/'」はファイルに半角空白があるときのためにファイル名をダブルクォートで囲む処理です。sortのLANG=Cと-sオプションはファイル数が膨大なときに処理を速くするためにつけています。

注意: 時間がかかるかもしれません。とりあえずsortの前に一度ファイルに出した方がよいかもしれません。

```bash
###出力で1列目の数が同じものが重複の疑いのあるものです###
uedambp:~ ueda$ find ~/ -type f | grep -i '\\.jpg$' | sed 's/.*/"&"/' |
xargs -n 1 gmd5sum | LANG=C sort -s -k1,1 |
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'
###Linuxの場合（さらにルートから検索をかけてみる）###
ueda@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/"&"/' | 
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | 
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'
...
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/var/www/bashcms/pages/whats_bashCMS/chinjyu.jpg
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/chinjyu.jpg
f1c3a09b784cc5a55bb820aaa873c79f /var/tmp/GIT/SD_BOOK/IMAGE/noodle.jpg
f1c3a09b784cc5a55bb820aaa873c79f /home/ueda/GIT/SD_BOOK/IMAGE/noodle.jpg
###Open usp Tukubai使用###
ueda@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/"&"/' | 
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | yarr num=1 | awk 'NF>2'
```

<h2>Q2</h2>

羽田空港の緯度経度を求めてください。

### 解答例

いくつかWebAPIを提供しているサイトがあると思いますが、私はFlightRadar24から持ってきました。

<a href="http://blog.cykey.ca/post/88174516880/analyzing-flightradar24s-internal-api-structure" target="_blank">こちらを参考にしました。</a>

```bash
uedambp:~ ueda$ curl http://www.flightradar24.com/_json/airports.php 2> /dev/null | 
jq . | grep -C 6 HND
 "lon": "15.082770",
 "country": "Sweden",
 "alt": "1503"
 },
 {
 "name": "Tokyo Haneda International Airport",
 "iata": "HND",
 "icao": "RJTT",
 "lat": "35.552250",
 "lon": "139.779602",
 "country": "Japan",
 "alt": "21"
 },
```

<h2>Q3</h2>


任意の級数からネイピア数（自然対数の底の数）を求めてください。精度が良いほど良いこととします。

<a href="http://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%A4%E3%83%94%E3%82%A2%E6%95%B0%E3%81%AE%E8%A1%A8%E7%8F%BE" target="_blank">こちらを参考に。</a>

### 解答例

もっと簡単な解答がありそうですが。1/(0!)の項が抜けるので最後に1を足さなければいけないのが残念。

```bash
uedambp:~ ueda$ seq 1 1000 |
awk '{for(i=1;i<=$1;i++){printf("%d ",i)}{print ""}}' |
tr ' ' '*' | sed 's/\\*$/)/' | sed 's:^:1/(:' | bc -l | 
tr '\\n' '+' | sed 's/$/1/' | bc -l 
2.71828182845904523526
```

<h2>Q4</h2>

<a href="/misc/message2015.txt" target="_blank">/misc/message2015.txt</a>は、あるメッセージにbase64を多重にかけたものです。解読してください。ワンライナーでなくても構いません。


### 解答例

```bash
uedambp:~ ueda$ a=$(curl http://blog.ueda.asia/misc/message2015.txt) ; 
while a=$(echo $a | base64 -D) && echo $a ; do : ; done 
...
T2lncGV6b2dmQ0E2SUNaOU96b0sK
OigpezogfCA6ICZ9OzoK
:(){: | : &};:
Invalid character in input stream.
```

<h2>Q5</h2>

円周率をなるべく精度よく求めてみてください。

### 解答例

モンテカルロ法でささっと（なにがささっとだか・・・）。

```bash
uedambp:~ ueda$ cat /dev/urandom | gtr -dc '0-9' |
gfold -b10 | sed 's/^/0./' | sed 's/$/5/' |
awk 'NR%2==0{print $1}NR%2!=0{printf($1 " ")}' |
awk '{x=$1-0.5;y=$2-0.5;r=sqrt(x^2 + y^2);if(r < 0.5){n++};print NR, 4*n/NR}'
...
729078 3.14094
729079 3.14094
729080 3.14094
729081 3.14095
729082 3.14095
729083 3.14094
729084 3.14094
...
###だんだん収束していきます###
```

<h2>Q6</h2>

集合{a,b,c,d,e}から全ての組み合わせ（部分集合）を列挙してください。

### 解答例

```bash
uedambp:~ ueda$ echo {,a}{,b}{,c}{,d}{,e}
e d de c ce cd cde b be bd bde bc bce bcd bcde a ae ad ade ac ace acd acde ab abe abd abde abc abce abcd abcde
```

<h2>Q7</h2>

8128が完全数であることを確認してください。

### 解答例

```bash
uedambp:~ ueda$ seq 2 8128 | awk '{print 8128/$1}' | grep -Fv . | numsum
8128
```
