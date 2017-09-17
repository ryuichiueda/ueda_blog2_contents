# 【問題のみ】第21回未経験者大歓迎！誰でも働けるアットホームな職場ですシェル芸勉強会
<a href="https://blog.ueda.asia/?p=7608">解答はこちら。</a><br />
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
<h2>Q3</h2><br />
<br />
2016年の日曜日を全て列挙してください。<br />
<br />
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
<h2>Q6</h2><br />
<br />
次の拡張正規表現をワンライナーで基本正規表現に変換してください。括弧の中の数字は数字の回数の文字列の繰り返しに展開してください。<br />
<br />
[bash]<br />
$ cat extended <br />
a+h{5}(ho){10}[0-9]+<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
GitHubのvol.21/Q7にあるテキストについて、各段落の文字数を数えてください。<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
GitHubのvol.21/Q8にある1350369599.Vfc03I4682c8M940114.remoteから添付ファイルを抽出して画像を復元してください。二つありますが別々に処理して構いません。<br />
<br />

