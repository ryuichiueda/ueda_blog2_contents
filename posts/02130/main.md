---
Keywords: ex,exない,Linux
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->Ubuntuにex(1)がないじゃないか<!--:-->
<!--:ja-->こんなことで怒る30代はいないと思うが・・・

<span style="color:red">・・・と思ってたら本当に使いたいのはed(1)で頭の中で入れ替わっていた・・・。すんません。ところで、exないですかね？（しつこい）</span>

```bash
Welcome to Ubuntu 12.04.4 LTS (GNU/Linux 3.8.0-29-generic x86_64)
ueda\@ubuntu0000:~$ which ex
/usr/bin/ex
ueda\@ubuntu0000:~$ ls -l /usr/bin/ex
lrwxrwxrwx 1 root root 20 2月 1 21:59 /usr/bin/ex -> /etc/alternatives/ex
ueda\@ubuntu0000:~$ ls -l /etc/alternatives/ex
lrwxrwxrwx 1 root root 18 2月 2 02:33 /etc/alternatives/ex -> /usr/bin/vim.basic
ueda\@ubuntu0000:~$ ls -l /usr/bin/vim.basic 
-rwxr-xr-x 1 root root 2015392 5月 4 2012 /usr/bin/vim.basic
```

<!--:--><!--more--><!--:ja-->

・・・というようにexがvim.basicに結びついておる。

```bash
ueda\@ubuntu0000:~$ find / 2> /dev/null | grep '/ex$' 
/etc/alternatives/ex
/usr/bin/ex
/var/lib/dpkg/alternatives/ex <- これもvimだった
```

・・・うーん。ないないない。<!--:-->
