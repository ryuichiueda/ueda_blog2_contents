---
Keywords:ログ,apache,CLI,Linux,shellshock,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---
# 【問題のみ】第16回春だからログ解析するぞシェル芸勉強会
<a href="http://blog.ueda.asia/?p=5644" title="【問題と解答例】第16回春だからログ解析するぞシェル芸勉強会">解答はコチラ</a><br />
<br />
<h1>始める前に</h1><br />
<br />
<h2>イントロのスライド</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/6Z4FO3TXgFiUjA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150418-16" title="20150418 第16回シェル芸勉強会スライド" target="_blank">20150418 第16回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h2>使用するログ</h2><br />
<br />
<a href="http://blog.ueda.asia/?page_id=5649" target="_blank">http://blog.ueda.asia/?page_id=5649</a>内の、access.log_.shellshock.gzとaccess_log.nasa.gzです。<br />
<br />
<!--more--> <br />
<br />
<h2>環境</h2><br />
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
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
<h2>準備0</h2><br />
<br />
ログをとってきましょう。<br />
<br />
[bash]<br />
$ wget http://blog.ueda.asia/misc/access_log.nasa.gz<br />
$ wget http://blog.ueda.asia/wp-content/uploads/2015/04/access.log_.shellshock.gz<br />
[/bash]<br />
<br />
<h2>準備1</h2><br />
<br />
access.log.shellshock.gzとaccess_log.nasa.gzについて、日付と時刻を次のように正規化しておきましょう。<br />
<br />
[bash]<br />
###修正前###<br />
ueda\@tencore:~/tmp/nasa$ zcat access_log.nasa.gz | head -n 1<br />
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245<br />
###修正後###<br />
ueda\@tencore:~/tmp/nasa$ cat access_log | head -n 1<br />
19950701 000001 199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245<br />
[/bash]<br />
<br />
<br />
<h2>準備2</h2><br />
<br />
NASAのログを各日付のファイルに分けておきましょう。ログはQ1で作ったものを使います。1,2行目の8桁日付、6桁時刻は残っていても構いません。<br />
<br />
<h2>Q1</h2><br />
<br />
NASAのログについて、ステータスコードを抽出して、どのコードがいくつあるか数えてみましょう。<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
NASAのログについて、ファイルを開かずに、ログの多い日を探しだしてみましょう。<br />
<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
NASAのログについて、（Q3-1）ログの件数が一番多い曜日はどれでしょうか。（Q3-2）ログの件数が一番多い時間帯（時間帯というのは0時台、1時台、・・・、23時台のこと）はどれでしょうか。<br />
<br />
Q3-2については高速な方法を考えてみてください。<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
ShellShockログ内にあるIPアドレス（IPv4）がすべて192.168.から始まることを確認して下さい。IPアドレスはレコードの先頭だけでなく、インジェクションするコードの中にもあるのでご注意ねがいます。<br />
<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
ShellShockログについて、レスポンスのデータ送信量が大きいものを、IPアドレスと共に上から10件を挙げてみましょう。<br />
<br />
<h2>Q6</h2><br />
<br />
NASAのログについて、7月8月のうち、ゼロ件の日を列挙してみてください。<br />
<br />
<h2>Q7</h2><br />
<br />
ShellShockのログから、（Q7-1）インジェクションが試みられたコード（「() { :;};」から後ろ）を抽出してみて傾向を話あってみましょう。（Q7-2）出来る人はエスケープも掃除してコードを復元してみましょう。（Q7-3）更にできる人は最後の行のコードを実行してみてください。<span style="color:red">このログはIPアドレスを変換しているので安全ですが、普通のログでやると死にますのでご注意を。</span><br />
<br />

