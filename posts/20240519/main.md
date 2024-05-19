---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルの進捗（2024年5月19日）

　[連載](/?page=sd_rusty_bash)で扱っている内容を大きく超えて暴走開発しており、周囲を置いてきぼりにしているので、ここでの記述を増やしていく所存です。（そろそろロボット学会に向けて研究のコードも書かねばならんのだが。）

　当面の目標は、この前から書いているとおり[bash-completionの巨大スクリプト](https://github.com/scop/bash-completion/blob/main/bash_completion)を読み込めること、その前にホーム下の`.bashrc`を読み込めるようにせんといかんだろうということで、そうしてます。

## .bashrcの冒頭のcase文への対策

　`~/.bashrc`（Ubuntuのデフォルトのものなど）の冒頭にはこういう記述があります。これに対応しました。

```bash

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```

特殊パラメータ`$-`の値は、Bashに設定されている複数のオプションを文字列にしたものです。上のcase文は、`$-`のなかに`i`オプションがあれば何もせず、なければ`return`で`~/.bashrc`の読み込みを終了します。`i`オプションは端末とやりとりしているインタラクティブシェルということを表すので、インタラクティブでなければ`~/.bashrc`のあとの内容は読み込まないぞという処理になっています。

　で、ここ数日はこれが解釈できるように実装を追加していました。

* `case`コマンドの実装
* `*i*`などのグロブの処理
* `return`の実装

実装の詳細を細かく書こうかな・・・と思ったんですが、すんごい長くなるので、とりあえずmainブランチのコードを動かした例だけ乗っけときます。

### case文の例

```bash

### インタラクティブな場合 ###
ueda@uedax1:~/GIT/rusty_bash$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/sush`
ueda@uedax1:main🌵~/GIT/rusty_bash(debug)🍣 case $- in *i*) echo iあるよ ;; *) echo iないよ ;; esac
iあるよ
### インタラクティブじゃない場合 ###
ueda@uedax1:~/GIT/rusty_bash$ echo 'case $- in *i*) echo iあるよ ;; *) echo iないよ ;; esac' | ./target/debug/sush
iないよ
```

### sourceに書かれたcase文内でのreturnの例

```bash

### こういうファイルを用意 ###
ueda@uedax1:~/GIT/rusty_bash$ cat /tmp/dummy_bashrc
case AAA in
    AAA) echo returnしますよ ; return ; echo ここには来ないよ ;;
esac
ueda@uedax1:~/GIT/rusty_bash$ cargo run
ueda@uedax1:main🌵~/GIT/rusty_bash(debug)🍣 source /tmp/dummy_bashrc 
returnしますよ
### ちなみにreturnはsourceのファイルの中か関数の中でしか使えません。 ####
ueda@uedax1:main🌵~/GIT/rusty_bash(debug)🍣 cat /tmp/dummy_bashrc | ./target/debug/sush
returnしますよ   #↓エラーが出る
sush: return: can only `return' from a function or sourced script
ここには来ないよ
```

## breakの実装

　returnの実装のついでにbreakの実装をしました。breakは、次のBashの例のとおり、for, while, untilでしか使えません。


```bash

$ break
bash: break: `for'、`while' または `until' ループでのみ意味があります
```

　もうひとつBashのbreakに関するネタとして、`break 数字`とやると何重にもなったループを一気に抜けることができます。Bashの例を示します。

```bash

### 2重のwhileを一発で抜ける例（ちゃんと止まる） ###
$ while true ; do while true; do break 2 ; done ; echo 止まらねえ ; done ; echo とまった
とまった
### breakの2を取ると止まらない ###
$ while true ; do while true; do break ; done ; echo 止まらねえ ; done ; echo とまった
止まらねえ
止まらねえ
止まらねえ
・・・
```

これも今のmainブランチには実装されています。


　現場からは以上です。使ってみてください。連載と関係なく要望はissueに書いて大丈夫です！
