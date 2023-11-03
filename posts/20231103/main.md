---
Keywords: 自作シェル, bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# Bashのファイル記述子255について

　連載[「魅惑の自作シェルの世界」](/?page=sd_rusty_bash)のための調べものをしていて、以前から気になってた「BashのFD255」について真面目に調べました。なんのことかというと、これのことです。

```bash
$ ls -l /proc/$$/fd
合計 0
lrwx------ 1 ueda ueda 64 11月  3 13:55 0 -> /dev/pts/1
lrwx------ 1 ueda ueda 64 11月  3 13:55 1 -> /dev/pts/1
lrwx------ 1 ueda ueda 64 11月  3 13:55 2 -> /dev/pts/1
lrwx------ 1 ueda ueda 64 11月  3 13:55 255 -> /dev/pts/1 #これは何？
```

標準入出力のファイル記述子（FD）0, 1, 2番が端末につながっているのは分かりますが、255番がいるのはなんなのかと。

## しらべた結果

　[このページ](https://unix.stackexchange.com/questions/475389/in-bash-what-is-file-descriptor-255-for-can-i-use-it)にたどりつきました。全部書いてありました。読めば書いてあるんですが、「Bashがインタラクティブシェルとして使われているときに、標準エラー出力がリダイレクトされたときのユーザーとの通信用」とのことです。

　実はこのページ、最初から255の謎を調べていたわけではなく、「どのファイル記述子が端末とつながっているかどうかをズボラに調べる方法」を探していてついでに発見したものです。確かに255がそういうものなら、255は端末につながっているとして良さそうです。ユーザーが<span style="text-color:red">変なリダイレクトをしなければ</span>、という話ですが。


## ということで変な操作をしてみる

　シェルで`exec 255>&-`を打つと255を閉じることができるので、実験してみましょう。まず、`exec`の前に、次のように`ps`を打ってみます。

```bash
$ ps au --forest
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
・・・
ueda      210157  0.0  0.0  12828  5440 pts/3    Ss   15:02   0:00 bash
ueda      218236  0.0  0.0  13716  3360 pts/3    R+   18:11   0:00  \_ ps au --forest
・・・
```

`ps`のSTATの項目に`+`がつきますが、これは`ps`がフォアグラウンド（端末とむすびついている）という印です。


　ここで、`exec`して255を閉じてしまいます。

```bash
$ exec 255>&-
$ ls -l /proc/$$/fd
合計 0
lrwx------ 1 ueda ueda 64 11月  3 13:55 0 -> /dev/pts/3
lrwx------ 1 ueda ueda 64 11月  3 13:55 1 -> /dev/pts/3
lrwx------ 1 ueda ueda 64 11月  3 13:55 2 -> /dev/pts/3
```

これで再び`ps`を実行すると・・・

```bash
$ ps au --forest
・・・
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ueda      210157  0.0  0.0  12828  5440 pts/3    Ss+  15:02   0:00 bash
ueda      218270  0.0  0.0  13716  3360 pts/3    R    18:13   0:00  \_ ps au --forest
・・・
```

というように、シェルのほうがフォアグラウンドのままになります。ちゃんとBashのコードを読んでいませんが、Bashが端末につながっているかどうかを255で確認しているのだと思います。

　これは普通のコマンドだとあまり問題になりませんが、画面を占拠するようなコマンドがエラーを出すようになります。

```bash
$ top
bash: [210157: 1 (255)] tcsetattr: 不正なファイル記述子です

[1]+  停止                  top
$ vi
bash: [210157: 1 (255)] tcsetattr: 不正なファイル記述子です

[2]+  停止                  vi
$ jobs
[1]-  停止                  top
[2]+  停止                  vi
$ exit #たぶんexitすると消えてくれます。（ゾンビになってたらごめんなさい）
```

　また、こういう遊びもできます（どうしてこうなるかは解析していません）。

```bash
$ stty tostop
$ exec 255&>-
（固まる）
```


## 試した環境

　次のとおりです。

```bash
$ echo $BASH_VERSION
5.1.16(1)-release
$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.3 LTS"
```

現場からは以上です。シェルを壊すのはたのしいです。
