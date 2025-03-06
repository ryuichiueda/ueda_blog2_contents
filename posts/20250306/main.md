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

これは「補完対象に対応する補完機能が見当たらない場合、`_comp_complete_load`で補完しろ」ということを意味します。で、`_comp_complete_load`がなにかやってるなということになります。実際、コマンドに対応する機能をロードしているのはこの関数から呼ばれている`_comp_load`です。`_comp_load`のコードは[ここ](https://github.com/scop/bash-completion/blob/2f87ac492c375fd2a3a76a087fcaf92e363f911a/bash_completion#L3238)で読めます。めっちゃ長いですが。わたしは読みましたよ。読んだというか自分の作っているシェルに文法全部理解させましたよ。ええ。死ぬ。


## ということで

　自作シェルでも`complete -D`の関数が呼ばれるようにして、このたびめでたく`git`の補完ができるようになりました褒めて褒めて。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">これでgitのサブコマンドの補完と、そのあとの補完がエラーなく動くようになりました <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/pNkgzxTt6U">pic.twitter.com/pNkgzxTt6U</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1894594926652125561?ref_src=twsrc%5Etfw">February 26, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ブランチの補完もうごきましたー🎉 <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/7vzBG6zWT8">pic.twitter.com/7vzBG6zWT8</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1894595123935416708?ref_src=twsrc%5Etfw">February 26, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　`_comp_complete_load`が呼ばれている様子です。

```bash
### 自作シェルの例 ###
$ sush
Rusty Bash (a.k.a. Sushi shell), version 1.0.4 - release
🍣 complete | grep git
🍣 git a                          #なんか補完してみる
add      am       archive  apply
                      ^C
🍣 complete | grep git
complete -F __git_wrap__gitk_main gitk
complete -F __git_wrap__git_main git    #セットされている
#今後の課題: ほんとはもうひとつ読み込まれるはずだけど読み込まれていない#
```

