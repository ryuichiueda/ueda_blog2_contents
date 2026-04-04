---
Keywords: Linux
Copyright: (C) 2026 Ryuichi Ueda
---

# SCHED_DEADLINEで処理の不履行を起こす

　いま機械系の学生さん向けのLinuxの本を書いてるんですが、本の中でこの興味深い例をなるべくシンプルな形で再現できないか、とふと考えて、本のためのコードを使い回してやってみました。ラズパイ5を使いました。

Katsuhiro Suzuki: [全プロセスが一秒止まる不具合続編: カーネル内部で何が起きたか？](https://zenn.dev/turing_motors/articles/fdfb70b7a9d90b), Tech Blog - Turing


## 使うコード

### その1: SCHED_DEADLINEで正確に時刻を刻むシェルスクリプト

　まず、次のようなシェルスクリプトを用意します。

```bash
#!/bin/bash

while ! read -t 1 _hoge ; do
        echo $EPOCHREALTIME
done
```
名前はなんでもいいのですが、`clock.bash`とでもしておきます。このシェルスクリプトの挙動は

* 3行目: readでキーボードから文字を受け付けるけど1秒でタイムアウト
* 4行目: Unix時刻を表示

というもので、そのまま起動すると、1秒ごとにUnix時刻を出力します。

　これを次のように起動すると、

```bash
ueda@raspi5:~$ sudo chrt -d --sched-runtime 1000000 \
--sched-deadline 10000000 --sched-period 2000000000 0 ./clock.bash
・・・
1775294226.926749
1775294228.926750
1775294230.926757
1775294232.926762
・・・
```

* 2秒ごとにカーネルに叩き起こされて時刻を出力
* 2秒ごとではあるが、SCHED_DEADLINEという優先度最高のタスクとして起動するので他の処理で遅延することは基本ない

ということで、かなり正確に2秒ずつ時刻を出力するようになります。


```bash
1775293866.251041
1775293867.251156
1775293874.251532  #飛んだ！！！
1775293875.251711
1775293876.251803
```


```bash
Tasks: 160 total,   3 running, 154 sleeping,   0 stopped,   3 zombie
%Cpu(s):  0.0 us, 43.6 sy,  0.0 ni, 12.4 id, 44.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3984.1 total,   2137.6 free,   1864.4 used,     30.1 buff/cache
MiB Swap:   2048.0 total,      0.1 free,   2047.9 used.   2119.7 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
     58 root      20   0       0      0      0 S  86.0   0.0   0:43.58 [kswapd0]
   4058 ueda      20   0       0      0      0 R  54.2   0.0   0:09.91 [swap]
・・・
```
