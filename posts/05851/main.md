---
Keywords: ログ,apache,CLI,Linux,shellshock,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第16回春だからログ解析するぞシェル芸勉強会
<a href="http://blog.ueda.asia/?p=5644" title="【問題と解答例】第16回春だからログ解析するぞシェル芸勉強会">解答はコチラ</a>

<h1>始める前に</h1>

<h2>イントロのスライド</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/6Z4FO3TXgFiUjA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150418-16" title="20150418 第16回シェル芸勉強会スライド" target="_blank">20150418 第16回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h2>使用するログ</h2>

<a href="http://blog.ueda.asia/?page_id=5649" target="_blank">http://blog.ueda.asia/?page_id=5649</a>内の、access.log_.shellshock.gzとaccess_log.nasa.gzです。

<!--more--> 

<h2>環境</h2>
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

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

<h2>準備0</h2>

ログをとってきましょう。

[bash]
$ wget http://blog.ueda.asia/misc/access_log.nasa.gz
$ wget http://blog.ueda.asia/wp-content/uploads/2015/04/access.log_.shellshock.gz
[/bash]

<h2>準備1</h2>

access.log.shellshock.gzとaccess_log.nasa.gzについて、日付と時刻を次のように正規化しておきましょう。

[bash]
###修正前###
ueda\@tencore:~/tmp/nasa$ zcat access_log.nasa.gz | head -n 1
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245
###修正後###
ueda\@tencore:~/tmp/nasa$ cat access_log | head -n 1
19950701 000001 199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245
[/bash]


<h2>準備2</h2>

NASAのログを各日付のファイルに分けておきましょう。ログはQ1で作ったものを使います。1,2行目の8桁日付、6桁時刻は残っていても構いません。

<h2>Q1</h2>

NASAのログについて、ステータスコードを抽出して、どのコードがいくつあるか数えてみましょう。


<h2>Q2</h2>

NASAのログについて、ファイルを開かずに、ログの多い日を探しだしてみましょう。



<h2>Q3</h2>

NASAのログについて、（Q3-1）ログの件数が一番多い曜日はどれでしょうか。（Q3-2）ログの件数が一番多い時間帯（時間帯というのは0時台、1時台、・・・、23時台のこと）はどれでしょうか。

Q3-2については高速な方法を考えてみてください。


<h2>Q4</h2>

ShellShockログ内にあるIPアドレス（IPv4）がすべて192.168.から始まることを確認して下さい。IPアドレスはレコードの先頭だけでなく、インジェクションするコードの中にもあるのでご注意ねがいます。



<h2>Q5</h2>

ShellShockログについて、レスポンスのデータ送信量が大きいものを、IPアドレスと共に上から10件を挙げてみましょう。

<h2>Q6</h2>

NASAのログについて、7月8月のうち、ゼロ件の日を列挙してみてください。

<h2>Q7</h2>

ShellShockのログから、（Q7-1）インジェクションが試みられたコード（「() { :;};」から後ろ）を抽出してみて傾向を話あってみましょう。（Q7-2）出来る人はエスケープも掃除してコードを復元してみましょう。（Q7-3）更にできる人は最後の行のコードを実行してみてください。<span style="color:red">このログはIPアドレスを変換しているので安全ですが、普通のログでやると死にますのでご注意を。</span>


