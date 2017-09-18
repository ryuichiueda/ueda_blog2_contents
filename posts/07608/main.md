---
Keywords:コマンド,CLI,Linux,UNIX/Linuxサーバ,USP友の会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---
# 【問題と解答】第21回未経験者大歓迎！誰でも働けるアットホームな職場ですシェル芸勉強会
<a href="https://blog.ueda.asia/?p=7655">問題だけのページはこちら</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
GitHubにあります。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>環境</h2><br />
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
<br />
<table><br />
 <tr><br />
 <th>Mac,BSD系</th><br />
 <th>Linux</th><br />
 </tr><br />
 <tr><br />
 <td>gdate</td><br />
 <td>date</td><br />
 </tr><br />
 <tr><br />
 <td>gsed</td><br />
 <td>sed</td><br />
 </tr><br />
 <tr><br />
 <td>tail -r</td><br />
 <td>tac</td><br />
 </tr><br />
 <tr><br />
 <td>gtr</td><br />
 <td>tr</td><br />
 </tr><br />
 <tr><br />
 <td>gfold</td><br />
 <td>fold</td><br />
 </tr><br />
</table><br />
<br />
<br />
<h2>イントロ</h2><br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/p6Q0l01GGEHtoT" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/21-58236819" title="第21回シェル芸勉強会イントロ" target="_blank">第21回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div><br />
<br />
<h2>補記</h2><br />
<br />
最近あまり本の宣伝をしていないのでシェルプログラミング実用テクニックから問題を持ってきました。<br />
<br />
[amazonjs asin="4774173444" locale="JP" title="シェルプログラミング実用テクニック (Software Design plus)"]<br />
<br />
<h2>Q1</h2><br />
<br />
ShellGeiData/vol.21/Q1のbba.pdfからテキストを抽出して標準出力に出してください。<br />
<br />
<h3>解答例</h3><br />
<br />
例題のファイルの日本語にはFlateDecodeという圧縮がかかっていますが、これを解凍する一般的なコマンドは見つかりませんでした。ですのでpdf用のコマンドを紹介するだけで・・・。FlateDecodeの解凍コマンドはzlibを使うと自作はできる模様。<br />
<br />
[bash]<br />
###poppler-utilsをインストール###<br />
$ sudo apt-get install poppler-utils<br />
###あとはlessとかpdftotextとか###<br />
$ less bba.pdf | cat<br />
 群馬のシャブばばあ<br />
<br />
<br />
<br />
<br />
hoge.txt[2016/02/09 22:30:32]<br />
$ pdftotext -q bba.pdf -<br />
群馬のシャブばばあ<br />
<br />
hoge.txt[2016/02/09 22:30:32]<br />
<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
次のデータはShift JIS（cp932）の固定長データです。<br />
<br />
[bash]<br />
$ cat anydata.cp932 <br />
00000001??ӹ޷?ݺ?*******214413051100000002ʰ????ݸ*********114413018800000003???ӷ?ݺ?********210413093100000004??ݷ?ݺ?*********234413000800000005???ް??׳??޷?ݺ?331413090000000006??Э????ݾ޲??ݺ?1234130981<br />
[/bash]<br />
<br />
次のようなUTF-8のテキストに変換してください。<br />
<br />
[bash]<br />
00000001ﾊﾅﾓｹﾞｷﾞﾝｺｳ*******2144130511<br />
00000002ﾊｰﾄﾞﾊﾞﾝｸ*********1144130188<br />
00000003ｺﾄﾞﾓｷﾞﾝｺｳ********2104130931<br />
00000004ﾊﾀﾝｷﾞﾝｺｳ*********2344130008<br />
00000005ｱﾝﾀﾞｰｸﾞﾗｳﾝﾄﾞｷﾞﾝｺｳ3314130900<br />
00000006ﾊﾞﾐｭｰﾀﾞﾒﾝｾﾞｲｷﾞﾝｺｳ1234130981<br />
<br />
<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
###Shift JISの半角は1バイトなのでUTF-8に変換する前に折り返すと楽です。###<br />
$ cat anydata.cp932 | fold -b35 | nkf -wLux<br />
00000001ﾊﾅﾓｹﾞｷﾞﾝｺｳ*******2144130511<br />
00000002ﾊｰﾄﾞﾊﾞﾝｸ*********1144130188<br />
00000003ｺﾄﾞﾓｷﾞﾝｺｳ********2104130931<br />
00000004ﾊﾀﾝｷﾞﾝｺｳ*********2344130008<br />
00000005ｱﾝﾀﾞｰｸﾞﾗｳﾝﾄﾞｷﾞﾝｺｳ3314130900<br />
00000006ﾊﾞﾐｭｰﾀﾞﾒﾝｾﾞｲｷﾞﾝｺｳ1234130981<br />
<br />
###1行の長さを調べるときは仕様書を見るか、規則性を見つけて折り返して長さを調べる###<br />
$ cat anydata.cp932 | sed 's/[0-9]\\{10\\}/&amp;\\n/g' |<br />
 LANG=C awk '{print length($0)}'<br />
35<br />
35<br />
35<br />
35<br />
35<br />
35<br />
1<br />
1<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
2016年の日曜日を全て列挙してください。<br />
<br />
<h3>解答</h3><br />
<br />
GNU dateの-fを使うと楽です。<br />
<br />
[bash]<br />
$ seq 20160101 20161231 | date -f - 2&gt; /dev/null | grep 日曜日<br />
2016年 1月 3日 日曜日 00:00:00 JST<br />
2016年 1月 10日 日曜日 00:00:00 JST<br />
2016年 1月 17日 日曜日 00:00:00 JST<br />
...<br />
2016年 12月 18日 日曜日 00:00:00 JST<br />
2016年 12月 25日 日曜日 00:00:00 JST<br />
###Tsukubaiを使う例###<br />
$ mdate -e 20160101 20161231 | tr ' ' '\\n' | yobi 1 | awk '$2==0'<br />
20160103 0<br />
20160110 0<br />
20160117 0<br />
...<br />
20161218 0<br />
20161225 0<br />
[/bash]<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
次のデータファイル<br />
<br />
[bash]<br />
001 あみだばばあ<br />
002 砂かけばばあ<br />
003 ******<br />
004 尾崎んちのババア<br />
[/bash]<br />
<br />
に、次の新しいデータ<br />
[bash]<br />
002 *******<br />
003 群馬のシャブばばあ<br />
005 純愛ババア学園<br />
[/bash]<br />
を反映して<br />
<br />
[bash]<br />
001 あみだばばあ<br />
002 *******<br />
003 群馬のシャブばばあ<br />
004 尾崎んちのババア<br />
005 純愛ババア学園<br />
[/bash]<br />
というデータを出力してください。<br />
<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ sort -ms -k1,1 newdata data | uniq -w 3<br />
001 あみだばばあ<br />
002 *******<br />
003 群馬のシャブばばあ<br />
004 尾崎んちのババア<br />
005 純愛ババア学園<br />
[/bash]<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q4$ cat newdata data | sort -snuk1,1 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; 石井　久治 (\@hisaharu) <a href="https://twitter.com/hisaharu/status/698388070589018112">2016, 2月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hisaharu">\@hisaharu</a> <br>sort -u -k1,1 newdata data<br>でしたねー！勉強になります</p>&mdash; mollinaca (\@syoutin) <a href="https://twitter.com/syoutin/status/698392272677654528">2016, 2月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h2>Q5</h2><br />
GitHubのvol.21/Q5にある次の二つのシェルスクリプトのデバッグをしてください。<br />
<br />
[bash]<br />
$ cat ./a.bash <br />
#!/bin/bash<br />
<br />
echo Hell<br />
###実行すると変なバグ###<br />
$ ./a.bash <br />
./a.bash: 行 1: ﻿#!/bin/bash: そのようなファイルやディレクトリはありません<br />
Hell<br />
$ cat b.bash <br />
#!/bin/bash<br />
<br />
ls ˜/<br />
###ホームディレクトリが表示されない###<br />
$ ./b.bash <br />
ls: ˜/ にアクセスできません: そのようなファイルやディレクトリはありません<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
a.bashについては「BOM付きUTF-8」という凶悪なフォーマットなので発見はバイナリの理解が大きな助けになります。が、とりあえずnkfに通せばBOMは取れます。たまにWindowsからやってきます。<br />
<br />
[bash]<br />
###調べるとUTF-8と出るので発見が遅れる。###<br />
$ nkf -g a.bash <br />
UTF-8<br />
###xxdで見ると頭に変なバイト列。###<br />
$ xxd -ps a.bash <br />
efbbbf23212f62696e2f626173680a0a6563686f2048656c6c0a<br />
###ただし、見なくてもnkfで除去できる。###<br />
$ nkf -wLux a.bash &gt; a<br />
$ chmod +x a<br />
$ ./a<br />
Hell<br />
[/bash]<br />
<br />
b.bashは、チルダがUTF-8のマルチバイト文字になっていて、~/がホームディレクトリに変換されません。このスクリプトには他にマルチバイト文字がないので、次のようなワンライナーでチルダがおかしいことを発見できます。<br />
<br />
[bash]<br />
$ iconv -c -f utf-8 -t ascii b.bash | diff - b.bash <br />
3c3<br />
&lt; ls /<br />
---<br />
&gt; ls ˜/<br />
[/bash]<br />
<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
次の拡張正規表現をワンライナーで基本正規表現に変換してください。括弧の中の数字は数字の回数の文字列の繰り返しに展開してください。<br />
<br />
[bash]<br />
$ cat extended <br />
a+h{5}(ho){10}[0-9]+<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
ゴリゴリです。<br />
<br />
[bash]<br />
$ cat extended | sed 's/[+}]/&amp;\\n/g' | sed 's/\\(.*\\)+/\\1\\1*/' |<br />
 tr '{}()' ' ' |<br />
 awk 'NF==2{for(i=1;i&lt;=$2;i++){printf $1};print &quot;&quot;}NF==1' |<br />
 tr -d '\\n' | xargs<br />
aa*hhhhhhohohohohohohohohoho[0-9][0-9]*<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
GitHubのvol.21/Q7にあるテキストについて、各段落の文字数を数えてください。<br />
<br />
<h3>解答</h3><br />
<br />
改行をとって数える対象を1行にまとめる方針が簡単です。解答例はロケールが日本語で、awkがgawkである等、いろいろ制約がありますが・・・。<br />
<br />
[bash]<br />
$ cat text | tr -d '\\n' | sed 's/　/\\n/g' |<br />
 awk '{print length($1),$1}'<br />
0 <br />
15 恥の多い生涯を送って来ました。<br />
353 自分には、人間の生活というものが、...にわかに興が覚めました。<br />
103 また、自分は子供の頃、...とばかり思っていました。<br />
[/bash]<br />
<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
GitHubのvol.21/Q8にある1350369599.Vfc03I4682c8M940114.remoteから添付ファイルを抽出して画像を復元してください。二つありますが別々に処理して構いません。<br />
<br />
<h3>解答</h3><br />
<br />
まず、何行目から何行目までがデータなのか調べます。<br />
<br />
[bash]<br />
$ grep -n -C 1 -- -- 1350369599.Vfc03I4682c8M940114.remote <br />
（略）<br />
59:--047d7b621ee6cf83c604cc276bb3<br />
60-Content-Type: image/jpeg; name=&quot;CHINJYU.JPG&quot;<br />
--<br />
665-0000000000000000000000000000001//9k=<br />
666:--047d7b621ee6cf83c604cc276bb3<br />
667-Content-Type: image/jpeg; name=&quot;IMG_0965.JPG&quot;<br />
--<br />
77341-xk9On61jS6VNFJqFxdoIZYbWK6QALsnJbBjHYcc4GT2IHJrGhUevkZ1MNypPuf/Z<br />
77342:--047d7b621ee6cf83c604cc276bb3--<br />
[/bash]<br />
<br />
で、その範囲を抽出して変換します。一つめの画像の切り出しの例だけ示しておきます。<br />
<br />
[bash]<br />
###出力の範囲を見ながらデータを切り出す###<br />
$ sed -n '60,665p' 1350369599.Vfc03I4682c8M940114.remote |<br />
 sed -n '6,$p' | base64 -d &gt; a.jpg<br />
###ImageMagickのidentifyコマンドでちゃんと画像になっているか確認###<br />
ueda\@remote:~/GIT/ShellGeiData/vol.21/Q5$ identify a.jpg <br />
a.jpg JPEG 261x261 261x261+0+0 8-bit DirectClass 34.2KB 0.010u 0:00.019<br />
###さらにavplayで画像を見る###<br />
$ avplay a.jpg<br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q8 % uudeview -i 1350369599.Vfc03I4682c8M940114.remote<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/698408677804347392">2016, 2月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
