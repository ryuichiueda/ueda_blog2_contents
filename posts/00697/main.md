---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# pmat version 0.001
この前のこの件（<a href="/?post=00674" title="こういう行列計算コマンドを考えついた">こういう行列計算コマンドを考えついた</a>）、とりあえずは行動ということで、まだかけ算しかできないもののコードを晒してみました。

<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/a56e77cf8416da50b0f75a9bfddcfe1e48989c1d/pmat.hs" title="pmat.hs">GitHubに晒したコード。荒削り風味。</a>

hmatrixというライブラリを入れるのに一苦労。使いこなすのに一苦労。

これから数式のパーサをゴリゴリ書く予定デス。

```bash
ueda@ubuntuonmac:~/GIT/PMAT$ cat data
A 1 2 3
A 1 2 3
B -1 2 3.0
B 1 -2 3.1
B 1 2 -3.2
ueda@ubuntuonmac:~/GIT/PMAT$ cat data | ./pmat "式はまだパースしないよーん"
A 1 2 3
A 1 2 3
B -1 2 3.0
B 1 -2 3.1
B 1 2 -3.2
A*B 4.0 4.0 -0.40000000000000213
A*B 4.0 4.0 -0.40000000000000213
```

コードをダウンロードしてもコンパイルまで辿り着ける人は皆無と思われるので、ある程度動くようになったらコンパイル済みのバイナリをGitHubに置く事にします。
