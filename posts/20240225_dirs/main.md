---
Keywords: Bash, メモ
Copyright: (C) 2024 Ryuichi Ueda
---

# ディレクトリ関係のチルダ展開の使い方

　Bashの場合のメモです。自分は使ったことがないのですが、Bashではチルダ展開で`PWD, OLDPWD`にあるディレクトリや`pushd`で記録したディレクトリを参照できます。

## やってみた

```bash
$ echo $BASH_VERSION
5.1.16(1)-release
### pushdで履歴を残しながらディレクトリ移動 ###
ueda@hoge:~$ pushd /etc
/etc ~
ueda@hoge:/etc$ pushd /var
/var /etc ~
ueda@hoge:/var$ pushd /
/ /var /etc ~
ueda@hoge:/$ dirs
/ /var /etc ~
### ~+と~- ###
ueda@hoge:/$ echo ~+ #いまのディレクトリ
/
$ echo ~- #前にいたディレクトリ
/var
### ~-N（スタックの底から参照） ###
ueda@hoge:/$ echo ~-0 #スタックの底
/home/ueda
ueda@hoge:/$ echo ~-1 #次
/etc
ueda@hoge:/$ echo ~-2 #その次・・・
/var
ueda@hoge:/$ echo ~-3
/
ueda@hoge:/$ echo ~-4 #スタックにない場合は展開しない
~-4
### ~-N（スタックの上から参照） ###
ueda@hoge:/$ echo ~+0
/
ueda@hoge:/$ echo ~+1
/var
ueda@hoge:/$ echo ~+2
/etc
ueda@hoge:/$ echo ~+3
/home/ueda
ueda@hoge:/$ echo ~+4
~+4
```

以上。
