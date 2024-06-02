---
Keywords: 自作シェル, 寿司シェル, sush
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルの進捗とBashの細かい話（2024年6月2日）

　[自作シェル](/?page=rusty_bash)の開発が暴走気味なのでドキュメントを残すための記事です。普段使いするようになって、自分を楽させるために大量の時間をつぎ込んでます。怠惰はプログラマーのなんとかですね・・・。


## 補完機能の強化その1

　こんなふうにタブ2回で出した補完の候補を、そのままタブや矢印キーで選択できるようにしました。

<blockquote class="twitter-tweet" data-media-max-width="560"><p lang="ja" dir="ltr">そういえば補完候補の選択には矢印キーも使えるようにしました <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/16o5AX3tpD">pic.twitter.com/16o5AX3tpD</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1797202651131871529?ref_src=twsrc%5Etfw">June 2, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 補完機能の強化その2


　`git`のサブコマンドで補完候補を変える機能を少し実装しました。
といってもシェル側の対応は少しで、
`.bashrc`に相当する`.sushrc`に補完用のスクリプトを書きました。

```bash

🍣 cat ~/.sushrc
case $- in
    *i*) ;;
      *) return ;;
esac

PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\b\[\033[00m\]\[\033[01;35m\]\w\[\033[00m\]🍣 '
PS2='> '
alias ls='ls --color=auto'

alias git-writing='git add -A ; git commit -m Writing; git push'

_git_comp () {
	if [ "$COMP_CWORD" = 1 ] ; then
		CANDS=( $( git |& grep '^  *[a-z]' | awk '{print $1}') )
		COMPREPLY=( $(compgen -W "${CANDS[@]}" -- "${cur}") )
	elif [ "$COMP_CWORD" = 2 -a "$prev" = switch ] ; then
		COMPREPLY=( $(compgen -W "$( git branch | tr -d '*' )" -- "${cur}" ) )
	elif [ "$COMP_CWORD" = 2 -a "$prev" = merge ] ; then
		COMPREPLY=( $(compgen -W "$( git branch | tr -d '*' )" -- "${cur}" ) )
	elif [ "$COMP_CWORD" = 2 -a "$prev" = diff ] ; then
		COMPREPLY=( $(compgen -W "$( git branch | tr -d '*' ) $(compgen -f)" -- "${cur}" ) )
	fi
} && complete -F _git_comp git
```
