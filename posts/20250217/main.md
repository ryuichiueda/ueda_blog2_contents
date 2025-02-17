---
Keywords: 自作シェル, sush, 寿司シェル, bash-completion
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルでbash-completionが動き始めた

　ほんとは今年の正月に決着をつけるつもりだったのですが、[連載](/?page=sd_rusty_bash)で作っているRust製の自作シェル（Rusty Bash、和名は寿司シェル）で、やっと[bash-completion](https://github.com/scop/bash-completion)が動くようになりました。


## bash-completionってなに

　bash-completionというのはメジャーどころのLinux環境のBashならデフォルトで動いている、シェルの補完機能です。たとえばBashで`ls --`と打ってタブを押すと、
```bash

ueda@x1gen13:~$ ls --
--all                                      --ignore=
--almost-all                               --indicator-style=
--author                                   --inode
--block-size=                              --kibibytes
```
というようにロングオプションの候補が出てきますが、これは、[この変態シェルスクリプト](https://github.com/scop/bash-completion/blob/main/bash_completion)で動いています。この補完候補は、bash-completionが`ls --help`を起動して、出力からロングオプションをBashの正規表現機能でスクレイピングして出力しています。変態です。


## 寿司シェルの状況

　上の例については[自作シェル（dev-completionブランチ）](https://github.com/shellgei/rusty_bash/tree/dev-completion)でも、

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">オプションの補完できた〜〜〜（ｾﾞｴｾﾞｴ） <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/0rTmCENxya">pic.twitter.com/0rTmCENxya</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1891084779228991683?ref_src=twsrc%5Etfw">February 16, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

というように動きました。あとは、ファイル名の補完も自分で書いたものから変更して、bash-completionのものを使うようにしました。ただ、まだbash-completionがつかっているBashの全機能を信頼性高く実装しているわけではないので、たまにエラーやワーニングが出ます。

　次は`git`の補完機能を動かそうとしています。ただ、他のコマンドと違って少々特殊なので、まだどうやってやるか、現状の寿司シェルでなんで動かないかは把握できてません。

## 結構大変なんだけどひっそりと開発

　bash-completionへの対応は、2024年の5月に

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">自作シェル、いい感じで使えてるんだけどbash-completionほしいなあ・・・（遠い道のり） <a href="https://t.co/YyvNQiBULL">pic.twitter.com/YyvNQiBULL</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1785985897458180437?ref_src=twsrc%5Etfw">May 2, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

と言ってから開始しだしたので、ほぼ10ヶ月かかりました。かなりの工数がかかるので、bash-completionが動く自作シェルはBashと、あといくつかしか存在しないと思われます。

　ただ結構大変な割に、自分自身の営業不足であんまりネットがざわざわしておりません。変態geek行為をしていれば勝手に盛り上がった昔とは違うんです・・・違うんです・・・。ということで、ちょっとでも寿司シェルに興味を持ってもらうため、なんで作っているのか書いておくと、

* 自分でコードをいじれるシェルがあると嬉しいな
* シェルもいつか（数十年後？）脱C言語しなければならなくなると思うので、そのときに選ばれると嬉しいな

くらいに考えてのことです。このふたつになにか心がひかれるなら、乗っかっていただければ幸いです。特にOSかなにかにバンドルされるようになると嬉しいので、もしなんかそういう活動がしたい人はご協力お願いいたします。それから、あとはコードの質問はなるべく返事しますので、Rustの勉強にもご活用ください。また、敷居の低い参加のとっかかりとしては、未実装の部分でもなんでもいいから、[issue](https://github.com/shellgei/rusty_bash/issues)に「Bashはこう動くけど寿司シェルは違う」と書くのがよろしいかと（当面は日本語でおkで）。

　現場からは以上です。なにとぞなにとぞよろしくお願いいたします。
