---
Keywords: Linux,Mac,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】年末年始シェル芸問題集
12月の<a href="/?post=04671" title="【問題のみ】第14回東京居残りシェル芸勉強会">シェル芸勉強会</a>よりもひどい問題を準備しましたので、時間をかけてお楽しみください。

追記: <a href="/?post=04821" title="【解答】年末年始シェル芸問題集" target="_blank">解答はコチラ</a>

解答はMacで作りました。ただし、Coreutilsが必要なので、
```bash
$ brew install coreutils
```
をお願いします。Q1以外の解答は1/2頃に公開します（Q1は便利なので早めに公開しておきます）。解答はハッシュタグ「#シェル芸」でワイワイやっていただければと。

良いお年を。


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

<h2>Q3</h2>


任意の級数からネイピア数（自然対数の底の数）を求めてください。精度が良いほど良いこととします。

<a href="http://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%A4%E3%83%94%E3%82%A2%E6%95%B0%E3%81%AE%E8%A1%A8%E7%8F%BE" target="_blank">こちらを参考に。</a>

<h2>Q4</h2>

<a href="http://file.ueda.tech/message2015.txt" target="_blank">message2015.txt</a>は、あるメッセージにbase64を多重にかけたものです。解読してください。ワンライナーでなくても構いません。

<h2>Q5</h2>

円周率をなるべく精度よく求めてみてください。

<h2>Q6</h2>

集合{a,b,c,d,e}から全ての組み合わせ（部分集合）を列挙してください。（ヒント: すごく簡単です）

<h2>Q7</h2>

8128が完全数であることを確認してください。

私はギブアップしてますが、挑戦したい人は
```bash
14474011154664524427946373126085988481573677491474835889066354349131199152128
```
が完全数であることを確認してください。（解けても商品は出ないのでほどほどに・・・）


<h2>Q8</h2>

「シェル芸」あるいは好きなキーワードを含んだツイートをなるべく集めてリストにしてみてください。

ちなみに私は以下の解答で力尽きましたので、何か良いアイデアがあれば。

```bash
uedambp:~ ueda$ w3m -dump 'https://twitter.com/search?f=realtime&q=%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8&src=typd' |
sed -n '/ 1\\./,$p' | sed -n '1,/^No Tweet/p'
```
