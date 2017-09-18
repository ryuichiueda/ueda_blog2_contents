---
Keywords:どうでもいい,シェルスクリプト,実験は大切
Copyright: (C) 2017 Ryuichi Ueda
---
# シェルスクリプト内ではエイリアスは効かないのでは・・・
こんなエントリーを見つけたので・・・<br />
<br />
<a href="http://d.hatena.ne.jp/syohex/20140703/1404379630" target="_blank">シェルスクリプトを公開するとき, コマンド前にバックスラッシュをつけるべき</a><br />
<br />
私も勘違いがあるかもしれませんが。<br />
<br />
<!--more--><br />
<br />
追記: 「シェルスクリプト」と表現されているものがシェルスクリプトなのかワンライナーになるのか、そこらへんがはっきりしません。あと、zshの話なので他のシェルだとどうなのか、そこらへんもよく分かりません。タイトルはインパクトがありますね。そのためTwitterでかなり出回っているので気になった次第です。<br />
<br />
ちょっと実験してみましょう。<br />
<br />
私のUbuntuのaliasです。<br />
<br />
[bash]<br />
ueda\@remote:~$ alias<br />
alias alert='notify-send --urgency=low -i &quot;$([ $? = 0 ] &amp;&amp; echo terminal || echo error)&quot; &quot;$(history|tail -n1|sed -e '\\''s/^\\s*[0-9]\\+\\s*//;s/[;&amp;|]\\s*alert$//'\\'')&quot;'<br />
alias egrep='egrep --color=auto'<br />
alias fgrep='fgrep --color=auto'<br />
alias grep='grep --color=auto'<br />
alias l='ls -CF'<br />
alias la='ls -A'<br />
alias ll='ls -alF'<br />
alias ls='ls --color=auto'<br />
[/bash]<br />
<br />
lと打つとこんな出力が。<br />
<br />
[bash]<br />
ueda\@remote:~$ l<br />
123456789012.eps db/ id_rsa.pub takashi tmpvisit<br />
123456789012.png death_hato.bash* ipv6 test.bash* trackback.cgi*<br />
GIT/ dummy.pdf kenpinsiru.bash* test2.bash* ueda.png<br />
TESTDATA.gz env.bash komakai_suuji tmp/ usppub<br />
[/bash]<br />
<br />
これをシェルスクリプトで起動してみます。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge.bash <br />
#!/bin/bash <br />
<br />
l<br />
[/bash]<br />
<br />
このようにエラーが出ます。<br />
[bash]<br />
ueda\@remote:~$ ./hoge.bash <br />
./hoge.bash: 行 3: l: コマンドが見つかりません<br />
[/bash]<br />
<br />
<br />
私の方に勘違いがあるかもしれません。あとまあ、人のコードを試すときはバックアップは必須です。と言いますか、バックアップはいつも必須です。<br />
<br />
<br />
以上です。
