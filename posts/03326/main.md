---
Keywords: どうでもいい,シェルスクリプト,実験は大切
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルスクリプト内ではエイリアスは効かないのでは・・・
こんなエントリーを見つけたので・・・

<a href="http://d.hatena.ne.jp/syohex/20140703/1404379630" target="_blank">シェルスクリプトを公開するとき, コマンド前にバックスラッシュをつけるべき</a>

私も勘違いがあるかもしれませんが。

<!--more-->

追記: 「シェルスクリプト」と表現されているものがシェルスクリプトなのかワンライナーになるのか、そこらへんがはっきりしません。あと、zshの話なので他のシェルだとどうなのか、そこらへんもよく分かりません。タイトルはインパクトがありますね。そのためTwitterでかなり出回っているので気になった次第です。

ちょっと実験してみましょう。

私のUbuntuのaliasです。

```bash
ueda\@remote:~$ alias
alias alert='notify-send --urgency=low -i &quot;$([ $? = 0 ] &amp;&amp; echo terminal || echo error)&quot; &quot;$(history|tail -n1|sed -e '\\''s/^\\s*[0-9]\\+\\s*//;s/[;&amp;|]\\s*alert$//'\\'')&quot;'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
```

lと打つとこんな出力が。

```bash
ueda\@remote:~$ l
123456789012.eps db/ id_rsa.pub takashi tmpvisit
123456789012.png death_hato.bash* ipv6 test.bash* trackback.cgi*
GIT/ dummy.pdf kenpinsiru.bash* test2.bash* ueda.png
TESTDATA.gz env.bash komakai_suuji tmp/ usppub
```

これをシェルスクリプトで起動してみます。

```bash
ueda\@remote:~$ cat hoge.bash 
#!/bin/bash 

l
```

このようにエラーが出ます。
```bash
ueda\@remote:~$ ./hoge.bash 
./hoge.bash: 行 3: l: コマンドが見つかりません
```


私の方に勘違いがあるかもしれません。あとまあ、人のコードを試すときはバックアップは必須です。と言いますか、バックアップはいつも必須です。


以上です。
