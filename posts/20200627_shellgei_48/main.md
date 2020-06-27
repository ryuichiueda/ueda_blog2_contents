---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2020 Ryuichi Ueda
---

# 【問題と解答】jus共催 第48回引きこもりもりシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.48)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 20.04で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

次のようなシェルスクリプトを作ります。

```bash
$ cat lineno
echo $LINENO
```

このシェルスクリプトは普通に実行すると、「`lineno`の1行目」という意味で1が出力されます。

```bash
$ ./lineno 
1
$ bash lineno 
1
```

この`lineno`に書いたコマンドを実行して、現在操作しているBashの行番号を出力してみてください。できるひとは外部コマンドなしで実現してみましょう。

```bash
$ echo $LINENO
58
$ こたえ
59
```

### 解答例

```bash
$ echo $LINENO
58
$ eval $(<lineno)
59
```


## Q2

次のように打つと、`BASH`で始まる変数名が列挙できます。

```bash
$ echo ${!BASH*}
BASH BASHOPTS BASHPID BASH_ALIASES BASH_ARGC BASH_ARGV BASH_ARGV0 BASH_CMDS BASH_COMMAND BASH_COMPLETION_VERSINFO BASH_LINENO BASH_REMATCH BASH_SOURCE BASH_SUBSHELL BASH_VERSINFO BASH_VERSION
```

この中で、`BASH_VERSION`の値が見たいと思いました。`echo ${!BASH*}`の前後や間にいろいろ足して、`BASH_VERSION`の値を表示してください。できれば外部コマンドの利用は避けてください。


### 解答例

```
$ eval echo '$'$(a=(${!BASH*});echo ${a[-1]})
5.0.16(1)-release
$ eval echo '$'$(echo ${!BASH*} | sed 's/.* //')
5.0.16(1)-release
$ echo ${!BASH*} | awk '{print "^"$NF}' | grep -f- <(set)
BASH_VERSION='5.0.16(1)-release'
```

## Q3

`sleep`をみっつ、`systemd`（あるいは`init`などプロセス番号1のプロセス）の下にぶら下げてください。できるひとは100個ぶらさげてください。

### 解答例


```bash
$ ( sleep 100 | sleep 100 | sleep 100 & )
$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
・・・
        ├─3*[sleep]
        ├─snapd───11*[{snapd}]
・・・
```

補足: デスクトップ版だと`systemd`の下の`systemd`にぶら下がることがあります。

## Q4

いま触っている端末上で`echo $$`して`1`が出るように細工してください。

### 解答例


```bash
$ sudo unshare --fork --pid --mount-proc bash
# echo $$
1
```

* 出典: 

<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">連載「Linuxのしくみ」はコンテナ機能を実現するためのカーネル機能、namespaceについて扱っています。いつものように具体例も出しつつ説明していますので、ぜひごらんください <a href="https://t.co/RpUuXTM6p6">pic.twitter.com/RpUuXTM6p6</a></p>&mdash; sat🛏 (@satoru_takeuchi) <a href="https://twitter.com/satoru_takeuchi/status/1273569132139606017?ref_src=twsrc%5Etfw">June 18, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## Q5

3秒に一回、プロンプトに勝手に`unko`と入力されて叱られるようにしてください。


```bash
$ unko

コマンド 'unko' が見つかりません。もしかして:

  command 'nuko' from snap nuko (0.2.1)

他のバージョンについては 'snap info <snapname>' を確認してください。

$ unko

コマンド 'unko' が見つかりません。もしかして:

  command 'nuko' from snap nuko (0.2.1)

他のバージョンについては 'snap info <snapname>' を確認してください。

$ unko

コマンド 'unko' が見つかりません。もしかして:

  command 'nuko' from snap nuko (0.2.1)

他のバージョンについては 'snap info <snapname>' を確認してください。
```

### 解答例


```bash
$ exec < <( while echo unko ; do sleep 3 ; done )
```


## Q6

`$SHLVL`の数字で`seq`の役割を果たす一行のシェルスクリプトを書いて、1から順に出力を得てください。シェルレベルが限界を超えるのは気にしなくてもかまいません。

```bash
$ 出力例
1
2
3
4
5
...
999
bash: 警告: シェルレベル (1000) は高すぎます。1に再設定されました
1
2
...
```


### 解答例


```bash
$ cat f
echo $SHLVL && bash f
$ ./f | head
1
2
3
4
5
6
7
8
9
10
```


## Q7

つぎのように、`sleep`を3代ぶらさげてください。シェルスクリプトを使ってもかまいません。手が出ない場合は2代で十分です。

```bash
$ ps u --forest
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ueda       57701  0.0  0.0  12660  5784 pts/5    Ss   10:39   0:00 bash
ueda       57992  0.0  0.0   9112   588 pts/5    S+   10:44   0:00  \_ sleep 100
ueda       57993  0.0  0.0   9112   524 pts/5    S+   10:44   0:00      \_ sleep 100
ueda       57994  0.0  0.0   9112   580 pts/5    S+   10:44   0:00          \_ sleep 100
・・・
```

### 解答例

次のようなシェルスクリプトが考えられます。

```bash
$ cat hoge2
bash -c '
sleep 100 &
exec sleep 100
' &
exec sleep 100
```


## Q8

次のように2分木状にプロセスをぶらさげてください。forkbombには気をつけてくださいね。

```bash
$ ps --forest
    PID TTY          TIME CMD
 163971 pts/7    00:00:00 bash
 165295 pts/7    00:00:00  \_ bash
 165296 pts/7    00:00:00  |   \_ bash
 165297 pts/7    00:00:00  |       \_ bash
 165299 pts/7    00:00:00  |       |   \_ bash
 165327 pts/7    00:00:00  |       |   |   \_ bash
 165349 pts/7    00:00:00  |       |   |   |   \_ bash
 165355 pts/7    00:00:00  |       |   |   |   |   \_ bash
 165359 pts/7    00:00:00  |       |   |   |   |   |   \_ sleep
 165356 pts/7    00:00:00  |       |   |   |   |   \_ bash
 165350 pts/7    00:00:00  |       |   |   |   \_ bash
 165357 pts/7    00:00:00  |       |   |   |       \_ bash
 165358 pts/7    00:00:00  |       |   |   |       \_ bash
 165328 pts/7    00:00:00  |       |   |   \_ bash
 165329 pts/7    00:00:00  |       |   |       \_ bash
 165333 pts/7    00:00:00  |       |   |       |   \_ bash
 165334 pts/7    00:00:00  |       |   |       |   \_ bash
 165330 pts/7    00:00:00  |       |   |       \_ bash
 165347 pts/7    00:00:00  |       |   |           \_ bash
 165348 pts/7    00:00:00  |       |   |           \_ bash
 165300 pts/7    00:00:00  |       |   \_ bash
 165302 pts/7    00:00:00  |       |       \_ bash
 165310 pts/7    00:00:00  |       |       |   \_ bash
 165316 pts/7    00:00:00  |       |       |   |   \_ bash
 165320 pts/7    00:00:00  |       |       |   |   \_ bash
 165312 pts/7    00:00:00  |       |       |   \_ bash
 165315 pts/7    00:00:00  |       |       |       \_ bash
 165319 pts/7    00:00:00  |       |       |       \_ bash
 165304 pts/7    00:00:00  |       |       \_ bash
 165306 pts/7    00:00:00  |       |           \_ bash
 165331 pts/7    00:00:00  |       |           |   \_ bash
 165332 pts/7    00:00:00  |       |           |   \_ bash
 165308 pts/7    00:00:00  |       |           \_ bash
 165311 pts/7    00:00:00  |       |               \_ bash
 165314 pts/7    00:00:00  |       |               \_ bash
 165298 pts/7    00:00:00  |       \_ bash
 165301 pts/7    00:00:00  |           \_ bash
 165305 pts/7    00:00:00  |           |   \_ bash
 165321 pts/7    00:00:00  |           |   |   \_ bash
 165337 pts/7    00:00:00  |           |   |   |   \_ bash
 165338 pts/7    00:00:00  |           |   |   |   \_ bash
 165323 pts/7    00:00:00  |           |   |   \_ bash
 165335 pts/7    00:00:00  |           |   |       \_ bash
 165336 pts/7    00:00:00  |           |   |       \_ bash
 165307 pts/7    00:00:00  |           |   \_ bash
 165309 pts/7    00:00:00  |           |       \_ bash
 165322 pts/7    00:00:00  |           |       |   \_ bash
 165324 pts/7    00:00:00  |           |       |   \_ bash
 165313 pts/7    00:00:00  |           |       \_ bash
 165317 pts/7    00:00:00  |           |           \_ bash
 165318 pts/7    00:00:00  |           |           \_ bash
 165303 pts/7    00:00:00  |           \_ bash
 165325 pts/7    00:00:00  |               \_ bash
 165339 pts/7    00:00:00  |               |   \_ bash
 165351 pts/7    00:00:00  |               |   |   \_ bash
 165352 pts/7    00:00:00  |               |   |   \_ bash
 165340 pts/7    00:00:00  |               |   \_ bash
 165353 pts/7    00:00:00  |               |       \_ bash
 165354 pts/7    00:00:00  |               |       \_ bash
 165326 pts/7    00:00:00  |               \_ bash
 165341 pts/7    00:00:00  |                   \_ bash
 165345 pts/7    00:00:00  |                   |   \_ bash
 165346 pts/7    00:00:00  |                   |   \_ bash
 165342 pts/7    00:00:00  |                   \_ bash
 165343 pts/7    00:00:00  |                       \_ bash
 165344 pts/7    00:00:00  |                       \_ bash
 165386 pts/7    00:00:00  \_ ps
```

### 解答例

```bash
$ a=bash ; for i in {1..5} ; do a=$(sed 's/bash/(&|&)/g' <<< $a) ; done ; sed 'asleep 100;' <<< $a | bash &
```
