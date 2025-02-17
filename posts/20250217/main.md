---
Keywords: 自作シェル, sush, 寿司シェル, bash-completion
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルでbash-completionが動き始めた

　ほんとは今年の正月に決着をつけるつもりだったのですが、やっと自作シェルで[bash-completion](https://github.com/scop/bash-completion)が動くようになりました。

## なにそれ

　bash-completionというのはメジャーなほうのLinux環境のBashならデフォルトで動いている、シェルの補完機能です。たとえばBashで`ls --`と打ってタブを押すと、
```bash

ueda@x1gen13:~$ ls --
--all                                      --ignore=
--almost-all                               --indicator-style=
--author                                   --inode
--block-size=                              --kibibytes
```
というようにロングオプションの候補が出てきますが、[自作シェル（dev-completionブランチ）](https://github.com/shellgei/rusty_bash/tree/dev-completion)でも、

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">オプションの補完できた〜〜〜（ｾﾞｴｾﾞｴ） <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/0rTmCENxya">pic.twitter.com/0rTmCENxya</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1891084779228991683?ref_src=twsrc%5Etfw">February 16, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

というように動きました。あとは、ファイル名の補完も自分で書いたものから変更して、bash-completionのものを使うようにしました。

## 結構大変でした

　「やっと」といってもbash-completionが動く自作シェルはたぶん存在しないと思います・・・。巨大でトリッキーなシェルスクリプトで、動かすの大変なので。2024年の5月に


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">自作シェル、いい感じで使えてるんだけどbash-completionほしいなあ・・・（遠い道のり） <a href="https://t.co/YyvNQiBULL">pic.twitter.com/YyvNQiBULL</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1785985897458180437?ref_src=twsrc%5Etfw">May 2, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

と言って対応を開始しだしたので、
