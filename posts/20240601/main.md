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
`.bashrc`に相当する`.sushrc`に補完用の関数を書きました。
いま使っている`.sushrc`を示します。このなかの`_git_comp`が補完用の関数です。
関数のあんまりきれいでないif文については、読み方を
https://blog.cybozu.io/entry/2016/09/26/080000 に丸投げします。

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

_git_comp () {   #これ以下がgitに対する補完の仕掛け
	if [ "$COMP_CWORD" = 1 ] ; then #git と打った後にサブコマンドを打つ前か打っている途中
		CANDS=( $( git |& grep '^  *[a-z]' | awk '{print $1}') ) #ヘルプからサブコマンドのリストを作る
		COMPREPLY=( $(compgen -W "${CANDS[@]}" -- "${cur}") )    # ${cur}（打っている途中の文字列）と一致するものを補完候補に
	elif [ "$COMP_CWORD" = 2 -a "$prev" = switch ] ; then #git switchのとき
		COMPREPLY=( $(compgen -W "$( git branch | tr -d '*' )" -- "${cur}" ) ) #ブランチの一覧を${cur}でフィルタをかけて補完候補に
	elif [ "$COMP_CWORD" = 2 -a "$prev" = merge ] ; then  #git mergeのとき
		COMPREPLY=( $(compgen -W "$( git branch | tr -d '*' )" -- "${cur}" ) ) #同上
        elif [ "$COMP_CWORD" = 2 -a "$prev" = diff ] ; then  #git diffのとき
                COMPREPLY=( $(compgen -W "$(compgen -f) $( git branch | tr -d '*' )"  -- "${cur}" ) )  #ファイルとブランチの両方を補完候補に
	fi #ほんとはもっと分岐する 
} && complete -F _git_comp git  #関数の定義がうまくいったらgitの補完関数として_git_compを登録
```

　これで、次のように状況に応じて補完候補が切り替わります（候補が1つしかないときは補完されます）。

```bash

### git <tab><tab>と打ったとき ###
ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 git
clone   add     restore bisect  grep    show    branch  merge   reset   tag     pull
init    mv      rm      diff    log     status  commit  rebase  switch  fetch   push
### git r<tab><tab>と打ったとき ###
ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 git r 
restore rm      rebase  reset
### git switch <tab><tab>と打ったとき ###
ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 git switch
dev-completion sd/202407_5    sd/202411_1    sd/202502_1    sd/202504_5    terminal_13
main           sd/202408_0    sd/202411_2    sd/202502_2    sd/202504_ref  terminal_14
prepare_1      sd/202408_1    sd/202411_3    sd/202502_3    sd/202505_0    terminal_15
（以下略）
### git switch <tab><tab>と打ったとき（ブランチの他、ファイルも補完候補に） ###
ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 git diff 
.git              sd/202405_2       sd/202409_3       sd/202501_1       sd/202504_1       terminal_11       
.github           sd/202405_3       sd/202409_4       sd/202501_2       sd/202504_2       terminal_12       
.gitignore        sd/202406_0       sd/202410_0       sd/202501_3       sd/202504_3       terminal_13 
（以下略）
```

仕事しながらもうちょっと`~/.sushrc`を充実させてみようと思います。


## SIGPIPEとPIPESTATUSへの対応

　しました。パイプが詰まるとコマンドが終了ステータス141を出します。いままでの実装だと`SIGPIPE`をシェルが受け取ってコマンドに行かないという現象が見られたので、寿司シェル側では`SIGPIPE`を無視するようにしました。サブシェルでは無視しないように設定を戻します。

```bash

ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 seq 10 | true
Pid: Pid(296910), Signal: SIGPIPE
ueda@uedaP1g6:main🌵~/GIT/rusty_bash🍣 echo ${PIPESTATUS[@]}
141 0
```

まだまだBashに比べると機能が少ないのですが、普段使う分にはいい感じになってきました。

　現場からは以上です。
