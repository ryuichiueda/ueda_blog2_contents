---
Keywords: Linux, SCHED_DEADLINE
Copyright: (C) 2026 Ryuichi Ueda
---

# LinuxのSCHED_DEADLINEの動作確認

　書籍のための備忘録なのでなぐり書きです。SCHED_DEADLINEというのは、現行のLinuxのタスクスケジューラ
（Earliest Eligible Virtual Deadline First、EEVDF）で定義されているプロセスの動かし方で、「一定周期内に必ずこのタスクやる（やれなかったら切腹）」というものです。


## 対象のタスク

　こんなシェルスクリプト（`./some_task.bash`）を書いてみました。無限ループで、`SECONDS`の値（シェルスクリプトが立ち上がってからの秒数）が変わったら、これまで変数`n`でカウントした数を秒数と一緒に出力します。

```bash
ueda@raspi5:~$ cat some_task.bash
#!/bin/bash

n=1
while true ; do
        if [[ "$SECONDS" != "$PREV" ]] ; then
                echo $SECONDS $n
                PREV=$SECONDS
        fi
        ((n++))
done
```

　とりあえずそのまま実行してみます。ラズパイ5で、1秒にだいたい15万くらいカウントできるみたいです。

```bash
ueda@raspi5:~$ chmod +x ./some_task.bash
ueda@raspi5:~$ ./some_task.bash
0 1
1 143742
2 351871
3 559945
Ctrl+C
```

　なお、本稿の実験の際はフォークのないシェルスクリプトを書かないといけません。別にプロセスができると、そいつがスケジューリングの対象から漏れてしまいます。あとで使う`chrt`コマンドでエラーが出ます。

## SCHED_DEADLINEを指定しての実行

　やってみます。`chrt -d`というコマンドを使います。引数には1回につき1ミリ秒だけ動かし、それを何があっても（？）10ミリ秒以内に終わらせろと指定し、さらに3秒周期ですることを指定します。スクリプトの名前の前の`0`は優先度です（適当です）。

```bash
ueda@raspi5:~$ sudo chrt -d --sched-runtime 1000000 \
--sched-deadline 10000000 --sched-period 3000000000 0 ./some_task.bash
0 1
3 27
6 126
9 373
12 636
Ctrl+C
```

出力のように、3秒につき1ミリ秒しか動いてないので、`n`の数がぐっと減ってます。秒数のカウントも3秒ごとになってます。ちゃんと指示通り動いてるみたいです。

## psで見てみる

　上記のスクリプトが動いている間、`ps`で観察してみました。優先度（`PRI`）が`-101`となっていますが、これは最強の優先度です。3秒に1回だけど絶対に動かせという強い意志を感じます。nice値で優先度が調整できる通常のプロセスでは`CLS`（スケジューリングクラス）が`TS`（タイムシェアリング）になりますが、`some_task.bash`は`DLN`（DEADLINE）となっています。nice値も適用外なので`-`が表示されています。

```bash
ueda@raspi5:~$ ps -eo pid,command,priority,nice,cls,rtprio | grep -e some -e PID
    PID COMMAND                     PRI  NI CLS RTPRIO
   1523 /bin/bash ./some_task.bash  -101  - DLN      0
   1528 grep --color=auto -e some -  20   0  TS      -
```

　ということでうごきました。
~~いかがでしたでしょうか。~~
最初、`--sched-runtime`をもっと小さい値にしていてうまくいかなかったのですが、案外ループが遅いんだなって思いました。


　現場からは以上です。みなさんあけまちんこ、のどちんこ。
