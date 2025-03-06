---
Keywords: 自作シェル, sush, 寿司シェル, bash-completion
Copyright: (C) 2025 Ryuichi Ueda
---

# bash-completionと自作シェルその後

　[前回](/?post=20250217)、bash-completionが動いたと書いたんですが、当然「動いた」と「使える」は違うわけでいろいろ直していました。で、やっと自分で使ってまあこんなもんかなというところまできたのでまたメモを書いておきます。


## gitの補完の謎

　まずあのあと、`git`の後のサブコマンド（`add`や`branch`とかのアレ）の補完ができないかいろいろ調べていました。どのコマンドがどんなふうに補完されるかは、Bashでは`complete`というコマンドで調査できます。次の例はLinuxのBashの例です。

```bash
### Bashの例 ###
$ complete | head -n 3
complete -F _longopt mv
complete -F _root_command gksudo
complete -F _command nice
```

出力の読み方は、たとえば「`mv`は`_longopt`という関数をつかって補完候補を見つける」というふうに読みます。`_longopt`というのはコマンドのロングオプション（とファイル）を探す関数で、Bashがbash-completionを読み込んだときに一緒に読み込まれます。

　ということは、`git`の補完方法については`complete | grep git`とすれば探せるはずですが、立ち上げたばかりのBashの場合、

```bash
### Bashの例 ###
$ complete | grep git
$      #何も出てこない
```

というように空振ります。

　じゃあどうやって補完しているんだという話になりますが、1回`git`で補完をして`complete`の出力を調べると、

```bash
### Bashの例 ###
$ git <tab> #←なにか補完を試みる（なんでもよい）
$ complete | grep git
complete -o bashdefault -o default -o nospace -F __git_wrap__gitk_main gitk
complete -o bashdefault -o default -o nospace -F __git_wrap__git_main /usr/bin/git
complete -o bashdefault -o default -o nospace -F __git_wrap__git_main git
```

というように、しれっと`git`の項目ができているのがわかります。

## 補完機能の自動ロード

　ということは<span style="color:red">自動で補完機能がロードされている</span>ということになります。で、どうやってということになるんですが、「デフォルトの補完機能」というものがあり、これを調べると手がかりになります。

```bash
### Bashの例 ###
$ complete | grep 'complete .* -D'
complete -F _comp_complete_load -D
```

これは「補完対象に対応する補完機能が見当たらない場合、`_comp_complete_load`で補完しろ」ということを意味します。で、`_comp_complete_load`がなにかやってるなということになります。実際、コマンドに対応する機能をロードしているのはこの関数から呼ばれている`_comp_load`です。`_comp_load`のコードは[ここ](https://github.com/scop/bash-completion/blob/2f87ac492c375fd2a3a76a087fcaf92e363f911a/bash_completion#L3238)で読めます。めっちゃ長いですが。わたしは読みましたよ。読んだというか自分の作っているシェルでエラーなく動かせるようにしましたよ。ええ。死ぬ。


##
