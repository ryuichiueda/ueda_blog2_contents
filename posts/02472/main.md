---
Keywords: コマンド,プログラミング,FreeBSD10,Python,UNIX/Linuxサーバ,寝る,真似しない方がいいかも
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->FreeBSD10にpython2.4から2.6までを無理矢理インストールした。<!--:-->
<!--:ja-->こんにちは。なんだかよく分からないのですが、頭の中でティモテの歌が流れっぱなしです。もうダメかもしれません。

<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai" target="_blank">Open usp Tukubai</a>の開発はFreeBSDでやっているのですが、この前、環境をFreeBSD10にしました。

<!--:--><!--more--><!--:ja-->

んで、環境の引っ越しのときに困るのがテストで、一応python2.4から2.7までサポートしているので2.4, 2.5, 2.6, 2.7それぞれのpythonでコマンドを試さなければなりません。

でも、FreeBSD10はすでに2.6すら標準で入らない始末です。なにを生き急いでいるのでしょう。

[bash]
[root\@freebsd10 /usr/ports/lang/python26]# make clean install
make: &amp;amp;amp;amp;amp;amp;quot;/usr/ports/Mk/bsd.python.mk&amp;amp;amp;amp;amp;amp;quot; line 558: Malformed conditional (${PYTHON_REL} &amp;amp;amp;amp;amp;amp;gt;= 320 &amp;amp;amp;amp;amp;amp;amp;&amp;amp;amp;amp;amp;amp;amp; defined(PYTHON_PY3K_PLIST_HACK))
make: Fatal errors encountered -- cannot continue
make: stopped in /usr/ports/lang/python26
[/bash]

なんか腹が立ったし所詮仮想環境なので、パッケージをダウンロードして解凍してそのまま/usr/localにブチ込むことにしました。

[bash]
freebsd10 /home/ueda$ fetch ftp://ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-10-12/Latest/python26.txz
python26.txz 100% of 8225 kB 1517 kBps 00m05s
freebsd10 /home/ueda$ fetch ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-05-10/Latest/python25.txz
freebsd10 /home/ueda$ fetch ftp.naist.jp/pub/FreeBSD-pkgbeta/freebsd:10:x86:64/2012-05-10/Latest/python24.txz
freebsd10 /home/ueda$ sudo -s
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python26.txz
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python25.txz
[root\@freebsd10 /usr/home/ueda]# tar -C / -xvzf python24.txz
[/bash]

・・・大丈夫でしょうか。

大丈夫でありませんでした。pythonを起動したらこんな風に2.4になってしまいました。

[bash]
[root\@freebsd10 /usr/home/ueda]# python
Python 2.4.5 (#2, May 9 2012, 13:34:32) 
[GCC 4.2.1 20070831 patched [FreeBSD]] on freebsd10
Type &amp;amp;amp;amp;amp;amp;quot;help&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;copyright&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;credits&amp;amp;amp;amp;amp;amp;quot; or &amp;amp;amp;amp;amp;amp;quot;license&amp;amp;amp;amp;amp;amp;quot; for more information.
&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt; 
[/bash]

なんかもう無理矢理2.7に戻します。

[bash]
[root\@freebsd10 /usr/home/ueda]# cd /usr/local/bin/
[root\@freebsd10 /usr/local/bin]# cp python2.7 python
[root\@freebsd10 /usr/home/ueda]# python
Python 2.7.6 (default, Feb 28 2014, 16:10:49) 
[GCC 4.2.1 Compatible FreeBSD Clang 3.3 (tags/RELEASE_33/final 183502)] on freebsd10
Type &amp;amp;amp;amp;amp;amp;quot;help&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;copyright&amp;amp;amp;amp;amp;amp;quot;, &amp;amp;amp;amp;amp;amp;quot;credits&amp;amp;amp;amp;amp;amp;quot; or &amp;amp;amp;amp;amp;amp;quot;license&amp;amp;amp;amp;amp;amp;quot; for more information.
&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;gt; 
[/bash]

Linuxだったらpythonに依存しているので大騒ぎですが、FreeBSDなのでおそらく大丈夫でしょう（超適当）。

とりあえずテストしてみました。

[bash]
freebsd10 /home/ueda$ ./GIT/Open-usp-Tukubai/TEST/regress.all 
...
python2.7 ./COMMANDS/calclock OK
python2.7 ./COMMANDS/cjoin0 OK
python2.7 ./COMMANDS/cjoin1 OK

...
python2.5 ./COMMANDS/mdate OK
python2.5 ./COMMANDS/nameread OK
python2.5 ./COMMANDS/numchar OK
python2.4 ./COMMANDS/calclock OK
python2.4 ./COMMANDS/cjoin0 OK
python2.4 ./COMMANDS/cjoin1 OK
...
[/bash]

・・・いいじゃありませんか！

[bash]
...
python3.1 ./COMMANDS/dayslash OK
python3.1 ./COMMANDS/filehame OK
python3.1 ./COMMANDS/formhame OK
0a1,5
&amp;amp;amp;amp;amp;amp;gt; 浜地______ F
&amp;amp;amp;amp;amp;amp;gt; 鈴田______ F
&amp;amp;amp;amp;amp;amp;gt; 江頭______ F
&amp;amp;amp;amp;amp;amp;gt; 白土______ M
&amp;amp;amp;amp;amp;amp;gt; 崎村______ F
TEST1 error
python3.1 ./COMMANDS/self NG
[/bash]

え？3.1？あ、さっきコードの修正したところだ・・・。

ところで、もう2.4, 2.5のサポートはやめた方がいいと思う・・・


眠い。寝る。<!--:-->
