---
Keywords: コマンド,CLI,Linux,UNIX/Linuxサーバ,USP友の会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第21回未経験者大歓迎！誰でも働けるアットホームな職場ですシェル芸勉強会
<a href="https://blog.ueda.asia/?p=7655">問題だけのページはこちら</a>

<h2>問題で使うファイル等</h2>

GitHubにあります。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>


<h2>イントロ</h2>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/p6Q0l01GGEHtoT" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/21-58236819" title="第21回シェル芸勉強会イントロ" target="_blank">第21回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div>

<h2>補記</h2>

最近あまり本の宣伝をしていないのでシェルプログラミング実用テクニックから問題を持ってきました。

[amazonjs asin="4774173444" locale="JP" title="シェルプログラミング実用テクニック (Software Design plus)"]

<h2>Q1</h2>

ShellGeiData/vol.21/Q1のbba.pdfからテキストを抽出して標準出力に出してください。

<h3>解答例</h3>

例題のファイルの日本語にはFlateDecodeという圧縮がかかっていますが、これを解凍する一般的なコマンドは見つかりませんでした。ですのでpdf用のコマンドを紹介するだけで・・・。FlateDecodeの解凍コマンドはzlibを使うと自作はできる模様。

```bash
###poppler-utilsをインストール###
$ sudo apt-get install poppler-utils
###あとはlessとかpdftotextとか###
$ less bba.pdf | cat
 群馬のシャブばばあ




hoge.txt[2016/02/09 22:30:32]
$ pdftotext -q bba.pdf -
群馬のシャブばばあ

hoge.txt[2016/02/09 22:30:32]

```

<h2>Q2</h2>

次のデータはShift JIS（cp932）の固定長データです。

```bash
$ cat anydata.cp932 
00000001??ӹ޷?ݺ?*******214413051100000002ʰ????ݸ*********114413018800000003???ӷ?ݺ?********210413093100000004??ݷ?ݺ?*********234413000800000005???ް??׳??޷?ݺ?331413090000000006??Э????ݾ޲??ݺ?1234130981
```

次のようなUTF-8のテキストに変換してください。

```bash
00000001ﾊﾅﾓｹﾞｷﾞﾝｺｳ*******2144130511
00000002ﾊｰﾄﾞﾊﾞﾝｸ*********1144130188
00000003ｺﾄﾞﾓｷﾞﾝｺｳ********2104130931
00000004ﾊﾀﾝｷﾞﾝｺｳ*********2344130008
00000005ｱﾝﾀﾞｰｸﾞﾗｳﾝﾄﾞｷﾞﾝｺｳ3314130900
00000006ﾊﾞﾐｭｰﾀﾞﾒﾝｾﾞｲｷﾞﾝｺｳ1234130981


```

<h3>解答</h3>

```bash
###Shift JISの半角は1バイトなのでUTF-8に変換する前に折り返すと楽です。###
$ cat anydata.cp932 | fold -b35 | nkf -wLux
00000001ﾊﾅﾓｹﾞｷﾞﾝｺｳ*******2144130511
00000002ﾊｰﾄﾞﾊﾞﾝｸ*********1144130188
00000003ｺﾄﾞﾓｷﾞﾝｺｳ********2104130931
00000004ﾊﾀﾝｷﾞﾝｺｳ*********2344130008
00000005ｱﾝﾀﾞｰｸﾞﾗｳﾝﾄﾞｷﾞﾝｺｳ3314130900
00000006ﾊﾞﾐｭｰﾀﾞﾒﾝｾﾞｲｷﾞﾝｺｳ1234130981

###1行の長さを調べるときは仕様書を見るか、規則性を見つけて折り返して長さを調べる###
$ cat anydata.cp932 | sed 's/[0-9]\\{10\\}/&amp;\\n/g' |
 LANG=C awk '{print length($0)}'
35
35
35
35
35
35
1
1
```


<h2>Q3</h2>

2016年の日曜日を全て列挙してください。

<h3>解答</h3>

GNU dateの-fを使うと楽です。

```bash
$ seq 20160101 20161231 | date -f - 2&gt; /dev/null | grep 日曜日
2016年 1月 3日 日曜日 00:00:00 JST
2016年 1月 10日 日曜日 00:00:00 JST
2016年 1月 17日 日曜日 00:00:00 JST
...
2016年 12月 18日 日曜日 00:00:00 JST
2016年 12月 25日 日曜日 00:00:00 JST
###Tsukubaiを使う例###
$ mdate -e 20160101 20161231 | tr ' ' '\\n' | yobi 1 | awk '$2==0'
20160103 0
20160110 0
20160117 0
...
20161218 0
20161225 0
```


<h2>Q4</h2>

次のデータファイル

```bash
001 あみだばばあ
002 砂かけばばあ
003 ******
004 尾崎んちのババア
```

に、次の新しいデータ
```bash
002 *******
003 群馬のシャブばばあ
005 純愛ババア学園
```
を反映して

```bash
001 あみだばばあ
002 *******
003 群馬のシャブばばあ
004 尾崎んちのババア
005 純愛ババア学園
```
というデータを出力してください。


<h3>解答</h3>

```bash
$ sort -ms -k1,1 newdata data | uniq -w 3
001 あみだばばあ
002 *******
003 群馬のシャブばばあ
004 尾崎んちのババア
005 純愛ババア学園
```
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q4$ cat newdata data | sort -snuk1,1 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; 石井　久治 (\@hisaharu) <a href="https://twitter.com/hisaharu/status/698388070589018112">2016, 2月 13</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hisaharu">\@hisaharu</a> <br>sort -u -k1,1 newdata data<br>でしたねー！勉強になります</p>&mdash; mollinaca (\@syoutin) <a href="https://twitter.com/syoutin/status/698392272677654528">2016, 2月 13</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<h2>Q5</h2>
GitHubのvol.21/Q5にある次の二つのシェルスクリプトのデバッグをしてください。

```bash
$ cat ./a.bash 
#!/bin/bash

echo Hell
###実行すると変なバグ###
$ ./a.bash 
./a.bash: 行 1: ﻿#!/bin/bash: そのようなファイルやディレクトリはありません
Hell
$ cat b.bash 
#!/bin/bash

ls ˜/
###ホームディレクトリが表示されない###
$ ./b.bash 
ls: ˜/ にアクセスできません: そのようなファイルやディレクトリはありません
```

<h3>解答</h3>

a.bashについては「BOM付きUTF-8」という凶悪なフォーマットなので発見はバイナリの理解が大きな助けになります。が、とりあえずnkfに通せばBOMは取れます。たまにWindowsからやってきます。

```bash
###調べるとUTF-8と出るので発見が遅れる。###
$ nkf -g a.bash 
UTF-8
###xxdで見ると頭に変なバイト列。###
$ xxd -ps a.bash 
efbbbf23212f62696e2f626173680a0a6563686f2048656c6c0a
###ただし、見なくてもnkfで除去できる。###
$ nkf -wLux a.bash &gt; a
$ chmod +x a
$ ./a
Hell
```

b.bashは、チルダがUTF-8のマルチバイト文字になっていて、~/がホームディレクトリに変換されません。このスクリプトには他にマルチバイト文字がないので、次のようなワンライナーでチルダがおかしいことを発見できます。

```bash
$ iconv -c -f utf-8 -t ascii b.bash | diff - b.bash 
3c3
< ls /
---
&gt; ls ˜/
```



<h2>Q6</h2>

次の拡張正規表現をワンライナーで基本正規表現に変換してください。括弧の中の数字は数字の回数の文字列の繰り返しに展開してください。

```bash
$ cat extended 
a+h{5}(ho){10}[0-9]+
```

<h3>解答</h3>

ゴリゴリです。

```bash
$ cat extended | sed 's/[+}]/&amp;\\n/g' | sed 's/\\(.*\\)+/\\1\\1*/' |
 tr '{}()' ' ' |
 awk 'NF==2{for(i=1;i<=$2;i++){printf $1};print &quot;&quot;}NF==1' |
 tr -d '\\n' | xargs
aa*hhhhhhohohohohohohohohoho[0-9][0-9]*
```

<h2>Q7</h2>

GitHubのvol.21/Q7にあるテキストについて、各段落の文字数を数えてください。

<h3>解答</h3>

改行をとって数える対象を1行にまとめる方針が簡単です。解答例はロケールが日本語で、awkがgawkである等、いろいろ制約がありますが・・・。

```bash
$ cat text | tr -d '\\n' | sed 's/　/\\n/g' |
 awk '{print length($1),$1}'
0 
15 恥の多い生涯を送って来ました。
353 自分には、人間の生活というものが、...にわかに興が覚めました。
103 また、自分は子供の頃、...とばかり思っていました。
```



<h2>Q8</h2>

GitHubのvol.21/Q8にある1350369599.Vfc03I4682c8M940114.remoteから添付ファイルを抽出して画像を復元してください。二つありますが別々に処理して構いません。

<h3>解答</h3>

まず、何行目から何行目までがデータなのか調べます。

```bash
$ grep -n -C 1 -- -- 1350369599.Vfc03I4682c8M940114.remote 
（略）
59:--047d7b621ee6cf83c604cc276bb3
60-Content-Type: image/jpeg; name=&quot;CHINJYU.JPG&quot;
--
665-0000000000000000000000000000001//9k=
666:--047d7b621ee6cf83c604cc276bb3
667-Content-Type: image/jpeg; name=&quot;IMG_0965.JPG&quot;
--
77341-xk9On61jS6VNFJqFxdoIZYbWK6QALsnJbBjHYcc4GT2IHJrGhUevkZ1MNypPuf/Z
77342:--047d7b621ee6cf83c604cc276bb3--
```

で、その範囲を抽出して変換します。一つめの画像の切り出しの例だけ示しておきます。

```bash
###出力の範囲を見ながらデータを切り出す###
$ sed -n '60,665p' 1350369599.Vfc03I4682c8M940114.remote |
 sed -n '6,$p' | base64 -d &gt; a.jpg
###ImageMagickのidentifyコマンドでちゃんと画像になっているか確認###
ueda\@remote:~/GIT/ShellGeiData/vol.21/Q5$ identify a.jpg 
a.jpg JPEG 261x261 261x261+0+0 8-bit DirectClass 34.2KB 0.010u 0:00.019
###さらにavplayで画像を見る###
$ avplay a.jpg
```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q8 % uudeview -i 1350369599.Vfc03I4682c8M940114.remote<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/698408677804347392">2016, 2月 13</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
