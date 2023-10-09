---
Keywords: シェル, bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# シェルのジョブまわりのメモ 

　[連載](/?page=sd_rusty_bash)のためのおさらいと予習です。
環境はこんな感じ。

```bash
ueda@x1:~$ echo $BASH_VERSION
5.1.16(1)-release
ueda@x1:~$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.3 LTS"
```

## ジョブの単位

### バックグラウンドジョブの場合

　バックグラウンドジョブの場合、パイプラインを`&&`や`||`で結んだものがひとつの単位。

```bash
$ sleep 10 | sleep 20 && sleep 30 && sleep 40 &
[1] 13298
$ jobs
[1]+  実行中               sleep 10 | sleep 20 && sleep 30 && sleep 40 &
```

### フォアグラウンドジョブを後ろに下げた場合

　フォアグラウンドで`&&`や`||`でつないだコマンド入力を実行して`Ctrl+Z`した場合、最初のパイプラインのところでジョブが切り離されて管理されるようになる。シェルには`false`が返って、以降のパイプラインを実行するかしないかの判定に使われる。（`killall SIGSTOP sleep`で実験しても同じでした。）

```bash
$ ls | sleep 20 && echo a || echo b
^Z
[1]+  停止                  ls --color=auto | sleep 20
b                    # &&につながったecho aじゃなくて||につながったecho bのほうが実行される
$ fg
ls --color=auto | sleep 20
$ echo $?            #実行後はふつうに最後のコマンドの終了ステータスが入る
0
```

`Ctrl+Z`された直後の終了ステータスは128。

```bash
$ ls | sleep 20
^Z
[4]+  停止                  ls --color=auto | sleep 20
$ echo $?
128
```

　つぎのような場合は、ふたつのジョブに分解される。

```bash
$ ls | sleep 20 || ls | sleep 30
^Z
[1]+  停止                  ls --color=auto | sleep 20
^Z
[2]+  停止                  ls --color=auto | sleep 30
$ jobs
[1]-  停止                  ls --color=auto | sleep 20
[2]+  停止                  ls --color=auto | sleep 30
```

## `&&`、`||`でつながれたバックグラウンドジョブはフォークする

　次のように、基本的にバックグラウンドジョブは表のシェルで直接実行される。

```bash
$ ls | sleep 10 &
[1] 16205
$ ps --forest
    PID TTY          TIME CMD
   9001 pts/1    00:00:00 bash
  16205 pts/1    00:00:00  \_ sleep #表のbashのプロセスでsleepを実行
  16206 pts/1    00:00:00  \_ ps
```

　ところが、パイプラインが複数あるとフォークが起こり、サブシェルで実行される。

```bash
$ ls | sleep 10 || ls | sleep 20 &
[1] 16231
$ ps --forest
    PID TTY          TIME CMD
   9001 pts/1    00:00:00 bash
  16231 pts/1    00:00:00  \_ bash      #ひとつbashが挟まる
  16233 pts/1    00:00:00  |   \_ sleep
  16234 pts/1    00:00:00  \_ ps
```


## `jobs`の表示

　`+`のついているものはカレントジョブ（定義は後述）。`-`はその一つ前。（上のコードの例を参照のこと）。`fg`でカレントジョブを表に持ってくると、`-`だったものが`+`に昇格する。

```bash
$ jobs
[1]   停止                  ls --color=auto | sleep 20
[2]-  停止                  ls --color=auto | sleep 30
[3]+  停止                  ls --color=auto | sleep 40
### カレントジョブをfgしてCtrl+Cする ###
$ fg
ls --color=auto | sleep 40
^C
### sleep 30のジョブがカレントジョブに昇格 ###
$ jobs
[1]-  停止                  ls --color=auto | sleep 20
[2]+  停止                  ls --color=auto | sleep 30
```

## カレントジョブ

基本は直前に止まったジョブのこと。バックグラウンドジョブを`&`をつかって実行状態にすると、カレントジョブにならずに停止中のもののうしろに順番がさがる。

```bash
### ふたつ停止しているジョブを作る ###
$ jobs
[1]-  停止                  ls --color=auto | sleep 200
[2]+  停止                  ls --color=auto | sleep 300
$ bg %1 #ひとつをバックグラウンドで実行
[1]- ls --color=auto | sleep 200 &
$ sleep 50 & #ひとつバックグラウンドジョブを作成
[3] 15082
$ jobs
[1]   実行中               ls --color=auto | sleep 200 &
[2]+  停止                  ls --color=auto | sleep 300
[3]-  実行中               sleep 50 &  #停止中のジョブの次の優先度になる
$ kill -SIGSTOP 15082  # sleep 50 &を止める
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]-  停止                  ls --color=auto | sleep 300
[3]+  停止                  sleep 50  #止めるとカレントジョブになる
```

## ジョブ番号

ジョブが増えると、現状の最大番号のジョブ番号の次の番号が、そのジョブに与えられる。停止中に終了させられたジョブのジョブ番号は、`jobs`で見たときに回収される。

```bash
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]   停止                  ls --color=auto | sleep 300
[3]-  停止                  sleep 100
[4]+  停止                  sleep 200
$ kill -SIGTERM %3 #3番目のジョブを止める

[3]-  停止                  sleep 100
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]   停止                  ls --color=auto | sleep 300
[3]-  Terminated              sleep 100 #この時点ではまだジョブ番号が残留
[4]+  停止                  sleep 200
$ jobs #もう一度jobsを実行すると3番は消滅
[1]   停止                  ls --color=auto | sleep 200
[2]-  停止                  ls --color=auto | sleep 300
[4]+  停止                  sleep 200 
$ sleep 300 & #もう一個ジョブ投入
[5] 15576
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]-  停止                  ls --color=auto | sleep 300
[4]+  停止                  sleep 200
[5]   実行中               sleep 300 & #3番ではなく5番に
```


実行中に終了させられると、その時点で回収される。

```bash
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]   停止                  ls --color=auto | sleep 300
[3]-  停止                  sleep 100
[4]+  停止                  sleep 200
$ bg %2
[2] ls --color=auto | sleep 300 & #2番のjobを再開
$ jobs
[1]   停止                  ls --color=auto | sleep 200
[2]   実行中               ls --color=auto | sleep 300 &
[3]-  停止                  sleep 100
[4]+  停止                  sleep 200
$ killall sleep #killallで2番のjobを狙い撃ち
[2]   Terminated              ls --color=auto | sleep 300
$ jobs         #jobsするとすでに表示されない
[1]   停止                  ls --color=auto | sleep 200
[3]-  停止                  sleep 100
[4]+  停止                  sleep 200
```


## シグナルへの反応

　`kill -KILL`以外のコマンドを止めるシグナルで素直にプロセスがなくなるのは、実行中のプロセスだけ。停止中のコマンドの場合、実行が再開された瞬間に、送られたシグナルの効果が顕在化。

```bash
### 4つジョブを作る ###
$ ls | sleep 20000 || ls | sleep 30000 || sleep 10000 || sleep 20000
^Z
[1]+  停止                  ls --color=auto | sleep 20000
^Z
[2]+  停止                  ls --color=auto | sleep 30000
^Z
[3]+  停止                  sleep 10000
^Z
[4]+  停止                  sleep 20000
### sleepにSIGTERM一斉送信 ###
$ killall -SIGTERM sleep
### jobsをしてもSIGTERMの効果は分からない ###
$ jobs
[1]   停止                  ls --color=auto | sleep 20000
[2]   停止                  ls --color=auto | sleep 30000
[3]-  停止                  sleep 10000
[4]+  停止                  sleep 20000
### 3番を再開してみる ###
$ kill -SIGCONT %3
### 3番すぐ止まる ###
$ jobs
[1]   停止                  ls --color=auto | sleep 20000
[2]   停止                  ls --color=auto | sleep 30000
[3]-  Terminated              sleep 10000
[4]+  停止                  sleep 20000
$ jobs
[1]   停止                  ls --color=auto | sleep 20000
[2]-  停止                  ls --color=auto | sleep 30000
[4]+  停止                  sleep 20000
### 他もfgしていくと止まっているのが分かる（割愛） ###
```

