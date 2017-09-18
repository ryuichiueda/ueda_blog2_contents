---
Keywords:ex,exない,Linux
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->Ubuntuにex(1)がないじゃないか<!--:-->
<!--:ja-->こんなことで怒る30代はいないと思うが・・・<br />
<br />
<span style="color:red">・・・と思ってたら本当に使いたいのはed(1)で頭の中で入れ替わっていた・・・。すんません。ところで、exないですかね？（しつこい）</span><br />
<br />
[bash]<br />
Welcome to Ubuntu 12.04.4 LTS (GNU/Linux 3.8.0-29-generic x86_64)<br />
ueda\@ubuntu0000:~$ which ex<br />
/usr/bin/ex<br />
ueda\@ubuntu0000:~$ ls -l /usr/bin/ex<br />
lrwxrwxrwx 1 root root 20 2月 1 21:59 /usr/bin/ex -&gt; /etc/alternatives/ex<br />
ueda\@ubuntu0000:~$ ls -l /etc/alternatives/ex<br />
lrwxrwxrwx 1 root root 18 2月 2 02:33 /etc/alternatives/ex -&gt; /usr/bin/vim.basic<br />
ueda\@ubuntu0000:~$ ls -l /usr/bin/vim.basic <br />
-rwxr-xr-x 1 root root 2015392 5月 4 2012 /usr/bin/vim.basic<br />
[/bash]<br />
<br />
<!--:--><!--more--><!--:ja--><br />
<br />
・・・というようにexがvim.basicに結びついておる。<br />
<br />
[bash]<br />
ueda\@ubuntu0000:~$ find / 2&gt; /dev/null | grep '/ex$' <br />
/etc/alternatives/ex<br />
/usr/bin/ex<br />
/var/lib/dpkg/alternatives/ex &lt;- これもvimだった<br />
[/bash]<br />
<br />
・・・うーん。ないないない。<!--:-->
