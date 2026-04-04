---
Keywords: Linux
Copyright: (C) 2026 Ryuichi Ueda
---

# SCHED_DEADLINEで処理の不履行を起こす

　いま機械系の学生さん向けのLinuxの本を書いてるんですが、本の中でこの興味深い例をなるべくシンプルな形で再現できないか、とふと考えて、本のためのコードを使い回してやってみました。

Katsuhiro Suzuki: [全プロセスが一秒止まる不具合続編: カーネル内部で何が起きたか？](https://zenn.dev/turing_motors/articles/fdfb70b7a9d90b), Tech Blog - Turing

## 使う環境

　ラズパイ5を使いました。リアルタイムLinux（`PREEMPT_RT`）で試す前に、今回は`PREEMPT_DYNAMIC`で試しました。

```bash
ueda@raspi5:~$ uname -a
Linux raspi5 6.8.0-1051-raspi #55-Ubuntu SMP PREEMPT_DYNAMIC
Thu Mar 19 11:43:53 UTC 2026 aarch64 aarch64 aarch64 GNU/Linux
```

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

というもので、そのまま起動すると、1秒ごとにUnix時刻を出力します。実験ではシェルスクリプトからフォークが起こるといけないので、`sleep 1`じゃなくて`read -t 1`を使っています。

　これを次のように起動すると、

```bash
ueda@raspi5:~$ sudo chrt -d --sched-runtime 1000000 \
--sched-deadline 10000000 --sched-period 2000000000 0 ./clock.bash
```

* 2秒ごとにカーネルに叩き起こされて時刻を出力
* 2秒ごとではあるが、SCHED_DEADLINEという優先度最高のタスクとして起動するので他の処理で遅延することは基本ない

ということで、かなり正確に2秒ずつ時刻を出力するようになります。負荷をかけると端末の表示が遅れることがありますが、出力される時刻自体は正確です。だいたい10マイクロ秒くらいの誤差というかドリフトで時刻が出てきます。

```bash
### さっきのコマンドのあとの出力 ###
・・・
1775294226.926749
1775294228.926750
1775294230.926757
1775294232.926762
・・・
```

### その2: メモリとスワップファイルを食い潰すC言語のコード

　今度は、引数の分だけ実メモリやスワップファイルを消費していくコードを書きます。他の実験に使ったコードなので、目的に比べて回りくどいかもしれません。

```c
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
        int n = atoi(argv[1]);
        for(int i=0;i<n;i++) {
                char *p = malloc(1024*1024); //1MiBメモリ確保
                for(int i=0;i<1024*1024;i+=4096)
                        p[i] = 111; //各ページの先頭に値を入れて実メモリを食う
        }
        exit(0); //メモリの後始末はカーネルに任せます
}
```

名前は`swap.c`にしましょう。次のように実行すると、6000MiBメモリを食ってくれます。

```bash
1775294574.927951
1775294576.927986
1775294578.927969
1775294584.931808  #飛んだ！！！
1775294586.927980
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
