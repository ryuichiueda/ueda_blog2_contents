---
Keywords: どうでもいい,危険シェル芸,帰る,日記,フォーク爆弾,シェル芸,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 時間差フォーク爆弾の提案と実行 #危険シェル芸
本日は大変痛ましい事故が起こりました。私を訪ねてきた学生さんが一人、危険シェル芸の犠牲になりました。最大のリスクは生きることです。社会人になったら誰も守ってくれません。強く生きましょう。

さて、その後始末の時に、時間差危険シェル芸（より正確には時間差フォーク爆弾）を思いつきました。

アイデアはこんな感じ。過去に同じことを考えた人はいるでしょうが・・・。

<ul>
 <li>ステップ1: .bashrc等にフォーク爆弾の関数を仕込んでおく（lsとかそういう人気のある名前で）</li>
 <li>ステップ2: lsと打つ。</li>
 <li>ステップ3: 死ぬ。</li>
</ul>


<h2>検証</h2>

やってみました。VMで・・・と言いたいところですが、ノートPCを買い換えた時にVMを消してしまいました。某Ubuntu環境でやります。<span style="color:red">ツッコミは厳禁。</span>

ログインしたら、.bashrcの一番下に次のように書きます。書き間違えると不発弾になって後世に迷惑がかかるのでやめましょう（消せよ）。

```bash
ueda@remote:~$ tail -n 1 .bashrc 
alias ls='ls(){ ls | ls &} ; ls'
```

一度ログアウト。sourceしてもいいのですが、ログイン即身成仏を狙います。

ということでログインして即実行。

```bash
ueda@remote:~$ ls
[1] 18531
ueda@remote:~$ 
[1]+ 終了 ls | ls
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 

ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ 
ueda@remote:~$ vi .bashr
（消息を断つ。）
```

大成功。ちょっとログ等で確認が取れませんが・・・。

<span style="color:red">.bashrcからエイリアスを消した直後、まだ設定が残っているのに間違ってlsを打ってしまい再度死んだのは秘密にする。</span>


帰る。というか今横須賀線車内・・・。


何をやっているのか。
