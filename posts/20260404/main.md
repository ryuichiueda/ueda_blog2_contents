---
Keywords: Linux, SCHED_DEADLINE
Copyright: (C) 2026 Ryuichi Ueda
---

# SCHED_DEADLINEで処理の不履行を起こす

　いま機械系の学生さん向けのLinuxの本を書いてるんですが、本の中でこの興味深い例をなるべくシンプルな形で再現できないか、とふと考えて、本のためのコードを使い回してやってみました。

Katsuhiro Suzuki: [全プロセスが一秒止まる不具合続編: カーネル内部で何が起きたか？](https://zenn.dev/turing_motors/articles/fdfb70b7a9d90b), Tech Blog - Turing

　事前知識がいろいろ必要な記事で、ちゃんと説明できていませんが、とりあえずふーんという感じで読んでいただければと。

## 使う環境

　RAMが4GBのラズパイ5を使いました。リアルタイムLinux（`PREEMPT_RT`）で試す前に、今回は`PREEMPT_DYNAMIC`で試しました。2GBのスワップファイルが使えるように設定されています。

```bash
ueda@raspi5:~$ uname -a
Linux raspi5 6.8.0-1051-raspi #55-Ubuntu SMP PREEMPT_DYNAMIC
Thu Mar 19 11:43:53 UTC 2026 aarch64 aarch64 aarch64 GNU/Linux
ueda@raspi5:~$ swapon -s
Filename    Type       Size    Used    Priority
/swap       file    2097148   52360    -2
ueda@raspi5:~/swap$ free
               total        used        free      shared  buff/cache   available
Mem:         4079708      229448     3775804          28      144664     3850260
Swap:        2097148       52320     2044828
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
（端末1）ueda@raspi5:~$ sudo chrt -d --sched-runtime 1000000 \
--sched-deadline 10000000 --sched-period 2000000000 0 ./clock.bash
```

* 2秒ごとにカーネルに叩き起こされて時刻を出力
* 2秒ごとではあるが、SCHED_DEADLINEという優先度最高のタスクとして起動するので他の処理で遅延することは基本ない

ということで、かなり正確に2秒ずつ時刻を出力するようになります。負荷をかけると端末の表示が遅れることがありますが、出力される時刻自体は正確です。だいたい10マイクロ秒くらいの誤差というかドリフトで時刻が出てきます。


```bash
### さっきのコマンドのあとの出力 ###
・・・（端末1）・・・
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

名前は`swap.c`にしましょう。次のように実行すると、6000MiBメモリを食ってくれます。実験に使ったラズパイでは、メモリもスワップも使い尽くします。`top`の表示を見ていくと、Swapのfreeの値が減っていきます（何分かかかります）。

```bash
（端末2）ueda@raspi5:~$ gcc -O0 swap.c -o swap
（端末2）ueda@raspi5:~$ ./swap 6000 &
（端末2）ueda@raspi5:~$ top -c             #監視用
・・・
top - 18:40:13 up  7:32,  3 users,  load average: 1.69, 0.50, 3.03
Tasks: 154 total,   2 running, 152 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.1 us,  1.3 sy,  0.0 ni, 46.2 id, 52.4 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3984.1 total,     45.1 free,   3945.5 used,     53.1 buff/cache
MiB Swap:   2048.0 total,   1616.9 free,    431.0 used.     38.6 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   4181 ueda      20   0 4186212   3.6g    848 R   3.7  92.7   0:04.02 ./swap 6000
・・・
### topを出るとスワップがなくなって「強制終了」と表示されています。###
[1]+  強制終了            ./swap 6000
```

　上で示したブログの記事では、メモリが食い潰されたときにカーネルスレッドのkswapd0の処理が長時間ロックをかけてしまうということです。このときにSCHED_DEADLINEのプロセスに何か起こると実験成功ということになります。

## 実験

　`clock.bash`を先に立ち上げて、あとから`swap`を立ちあげてしばらく待ちます。上に書いたように、前者、後者を立ち上げた端末をそれぞれ「端末1」、「端末2」とします。

　端末2でSwapのfreeが`0`になったあとすぐ2GBに戻るので、そのときに端末1を見てみましょう。2秒か4秒、処理が飛ぶのが観測できます。

```bash
1775294574.927951
1775294576.927986
1775294578.927969
1775294584.931808  #飛んだ！！！
1775294586.927980
```
10回くらい実験しましたが、全部飛びました。やったぜ（？）

　スワップがなくなる瞬間の`top`の出力をうまく採取できたので示します。`kswapd0`と`swap`というカーネルスレッドが結構激しく動いているのが確認できました。

```bash
### 端末2のtop ###
Tasks: 160 total,   3 running, 154 sleeping,   0 stopped,   3 zombie
%Cpu(s):  0.0 us, 43.6 sy,  0.0 ni, 12.4 id, 44.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3984.1 total,   2137.6 free,   1864.4 used,     30.1 buff/cache
MiB Swap:   2048.0 total,      0.1 free,   2047.9 used.   2119.7 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
     58 root      20   0       0      0      0 S  86.0   0.0   0:43.58 [kswapd0]
   4058 ueda      20   0       0      0      0 R  54.2   0.0   0:09.91 [swap]
・・・
```

　明日あたり`PREEMPT_RT`でも試してみようと思います。ロックの問題なので、たぶん`PREEMPT_RT`でも起こりそうだと予想してますが、どうでしょう？

　面白い。以上です。
