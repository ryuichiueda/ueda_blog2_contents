---
Keywords: コマンド,CLI,Linux,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第21回未経験者大歓迎！誰でも働けるアットホームな職場ですシェル芸勉強会
<a href="https://blog.ueda.asia/?p=7608">解答はこちら。</a>

<h2>問題で使うファイル等</h2>

GitHubにあります。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.21</a>

にあります。

クローンは以下のようにお願いします。

[bash]
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
[/bash]

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


<h2>Q2</h2>

次のデータはShift JIS（cp932）の固定長データです。

[bash]
$ cat anydata.cp932 
00000001??ӹ޷?ݺ?*******214413051100000002ʰ????ݸ*********114413018800000003???ӷ?ݺ?********210413093100000004??ݷ?ݺ?*********234413000800000005???ް??׳??޷?ݺ?331413090000000006??Э????ݾ޲??ݺ?1234130981
[/bash]

次のようなUTF-8のテキストに変換してください。

[bash]
00000001ﾊﾅﾓｹﾞｷﾞﾝｺｳ*******2144130511
00000002ﾊｰﾄﾞﾊﾞﾝｸ*********1144130188
00000003ｺﾄﾞﾓｷﾞﾝｺｳ********2104130931
00000004ﾊﾀﾝｷﾞﾝｺｳ*********2344130008
00000005ｱﾝﾀﾞｰｸﾞﾗｳﾝﾄﾞｷﾞﾝｺｳ3314130900
00000006ﾊﾞﾐｭｰﾀﾞﾒﾝｾﾞｲｷﾞﾝｺｳ1234130981


[/bash]

<h2>Q3</h2>

2016年の日曜日を全て列挙してください。



<h2>Q4</h2>

次のデータファイル

[bash]
001 あみだばばあ
002 砂かけばばあ
003 ******
004 尾崎んちのババア
[/bash]

に、次の新しいデータ
[bash]
002 *******
003 群馬のシャブばばあ
005 純愛ババア学園
[/bash]
を反映して

[bash]
001 あみだばばあ
002 *******
003 群馬のシャブばばあ
004 尾崎んちのババア
005 純愛ババア学園
[/bash]
というデータを出力してください。


<h2>Q5</h2>
GitHubのvol.21/Q5にある次の二つのシェルスクリプトのデバッグをしてください。

[bash]
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
[/bash]

<h2>Q6</h2>

次の拡張正規表現をワンライナーで基本正規表現に変換してください。括弧の中の数字は数字の回数の文字列の繰り返しに展開してください。

[bash]
$ cat extended 
a+h{5}(ho){10}[0-9]+
[/bash]


<h2>Q7</h2>

GitHubのvol.21/Q7にあるテキストについて、各段落の文字数を数えてください。


<h2>Q8</h2>

GitHubのvol.21/Q8にある1350369599.Vfc03I4682c8M940114.remoteから添付ファイルを抽出して画像を復元してください。二つありますが別々に処理して構いません。


