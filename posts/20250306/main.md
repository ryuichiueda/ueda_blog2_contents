---
Keywords: 自作シェル, sush, 寿司シェル, bash-completion
Copyright: (C) 2025 Ryuichi Ueda
---

# bash-completionと自作シェルその後

　[前回](/?post=20250217)、bash-completionが動いたと書いたんですが、当然「動いた」と「使える」は違うわけでいろいろ直していました。で、やっと自分で使ってまあこんなもんかなというところまできたのでまたメモを書いておきます。


## gitやその他コマンドの補完機能の自動ロード

　まずあのあと、`git`の後のサブコマンド（`add`や`branch`とかのアレ）の補完ができないかいろいろ調べていました。どのコマンドがどんなふうに補完されるかは、Bashでは`complete`というコマンドで調査できます。次の例はLinuxのBashの例です。

```bash
### Bashの例 ###
ueda@p1gen3:~$ complete | head -n 3
complete -F _longopt mv
complete -F _root_command gksudo
complete -F _command nice
```

出力の読み方は、たとえば「`mv`は`_longopt`という関数をつかって補完候補を見つける」というふうに読みます。`_longopt`というのはコマンドのロングオプション（とファイル）を探す関数で、Bashがbash-completionを読み込んだときに一緒に読み込まれます。
