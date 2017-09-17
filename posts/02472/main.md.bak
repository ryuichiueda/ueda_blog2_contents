# <!--:ja-->FreeBSD10にpython2.4から2.6までを無理矢理インストールした。<!--:-->
<!--:ja-->こんにちは。なんだかよく分からないのですが、頭の中でティモテの歌が流れっぱなしです。もうダメかもしれません。<br />
<br />
<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai" target="_blank">Open usp Tukubai</a>の開発はFreeBSDでやっているのですが、この前、環境をFreeBSD10にしました。<br />
<br />
<!--:--><!--more--><!--:ja--><br />
<br />
んで、環境の引っ越しのときに困るのがテストで、一応python2.4から2.7までサポートしているので2.4, 2.5, 2.6, 2.7それぞれのpythonでコマンドを試さなければなりません。<br />
<br />
でも、FreeBSD10はすでに2.6すら標準で入らない始末です。なにを生き急いでいるのでしょう。<br />
<br />
[bash]<br />
[root\@freebsd10 /usr/ports/lang/python26]# make clean install<br />
make: &amp;amp;amp;amp;amp;amp;quot;/usr/ports/Mk/bsd.python.mk&amp;amp;amp;amp;amp;amp;quot; line 558: Malformed conditional (${PYTHON_REL} &amp;amp;amp;amp;amp;amp;gt;= 320 &amp;amp;amp;amp;amp;amp;amp;&amp;amp;amp;amp;amp;amp;amp; defined(PYTHON_PY3K_PLIST_HACK))<br />
make: Fatal errors encountered -- cannot continue<br />
make: stopped in /usr/ports/lang/python26<br />
[/bash]<br />
<br />
なんか腹が立ったし所詮仮想環境なので、パッケージをダウンロードして解凍してそのまま/usr/localにブチ込むことにしました。<br />
<br />
[bash]<br />
freebsd10 /home/ueda$ fetch ftp://ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-10-12/Latest/python26.txz<br />
python26.txz 100% of 8225 kB 1517 kBps 00m05s<br />
freebsd10 /home/ueda$ fetch ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-05-10/Latest/python25.txz<br />
freebsd10 /home/ueda$ fetch ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-05-10/Latest/python24.txz<br />
freebsd10 /home/ueda$ sudo -s<br />
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python26.txz<br />
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python25.txz<br />
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python24.txz<br />
[/bash]<br />
<br />
・・・大丈夫でしょうか。<br />
<br />
大丈夫でありませんでした。pythonを起動したらこんな風に2.4になってしまいました。<br />
<br />
[bash]<br />
[root\@freebsd10 /usr/home/ueda]# python<br />
Python 2.4.5 (#2, May 9 2012, 13:34:32) <br />
[GCC 4.2.1 20070831 patched [FreeBSD]] on freebsd10<br />
Type &amp;amp;amp;amp;amp;amp;quot;help&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;copyright&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;credits&amp;amp;amp;amp;amp;amp;quot; or &amp;amp;amp;amp;amp;amp;quot;license&amp;amp;amp;amp;amp;amp;quot; for more information.<br />
&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt; <br />
[/bash]<br />
<br />
なんかもう無理矢理2.7に戻します。<br />
<br />
[bash]<br />
[root\@freebsd10 /usr/home/ueda]# cd /usr/local/bin/<br />
[root\@freebsd10 /usr/local/bin]# cp python2.7 python<br />
[root\@freebsd10 /usr/home/ueda]# python<br />
Python 2.7.6 (default, Feb 28 2014, 16:10:49) <br />
[GCC 4.2.1 Compatible FreeBSD Clang 3.3 (tags/RELEASE_33/final 183502)] on freebsd10<br />
Type &amp;amp;amp;amp;amp;amp;quot;help&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;copyright&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;credits&amp;amp;amp;amp;amp;amp;quot; or &amp;amp;amp;amp;amp;amp;quot;license&amp;amp;amp;amp;amp;amp;quot; for more information.<br />
&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt; <br />
[/bash]<br />
<br />
Linuxだったらpythonに依存しているので大騒ぎですが、FreeBSDなのでおそらく大丈夫でしょう（超適当）。<br />
<br />
とりあえずテストしてみました。<br />
<br />
[bash]<br />
freebsd10 /home/ueda$ ./GIT/Open-usp-Tukubai/TEST/regress.all <br />
...<br />
python2.7 ./COMMANDS/calclock OK<br />
python2.7 ./COMMANDS/cjoin0 OK<br />
python2.7 ./COMMANDS/cjoin1 OK<br />
<br />
...<br />
python2.5 ./COMMANDS/mdate OK<br />
python2.5 ./COMMANDS/nameread OK<br />
python2.5 ./COMMANDS/numchar OK<br />
python2.4 ./COMMANDS/calclock OK<br />
python2.4 ./COMMANDS/cjoin0 OK<br />
python2.4 ./COMMANDS/cjoin1 OK<br />
...<br />
[/bash]<br />
<br />
・・・いいじゃありませんか！<br />
<br />
[bash]<br />
...<br />
python3.1 ./COMMANDS/dayslash OK<br />
python3.1 ./COMMANDS/filehame OK<br />
python3.1 ./COMMANDS/formhame OK<br />
0a1,5<br />
&amp;amp;amp;amp;amp;amp;gt; 浜地______ F<br />
&amp;amp;amp;amp;amp;amp;gt; 鈴田______ F<br />
&amp;amp;amp;amp;amp;amp;gt; 江頭______ F<br />
&amp;amp;amp;amp;amp;amp;gt; 白土______ M<br />
&amp;amp;amp;amp;amp;amp;gt; 崎村______ F<br />
TEST1 error<br />
python3.1 ./COMMANDS/self NG<br />
[/bash]<br />
<br />
え？3.1？あ、さっきコードの修正したところだ・・・。<br />
<br />
ところで、もう2.4, 2.5のサポートはやめた方がいいと思う・・・<br />
<br />
<br />
眠い。寝る。<!--:-->
