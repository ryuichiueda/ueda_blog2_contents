---
Keywords: シェル, bash
Copyright: (C) 2023 Ryuichi Ueda
---

# シェルのジョブまわりのメモ 

　[連載](/?page=sd_rusty_bash)のためのおさらいと予習です。

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


## `jobs`の表示

　`+`のついているものはカレントジョブ（最後にバックグラウンドに行ったジョブ）。`-`はその一つ前。（上のコードの例を参照のこと）。`fg`でカレントジョブを表に持ってくると、`-`だったものが`+`に昇格する。

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
