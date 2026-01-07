---
Keywords: Linux, SCHED_DEADLINE
Copyright: (C) 2026 Ryuichi Ueda
---

# sleepコマンドなしでbashを眠らせる

　[前回の記事](/?post=20260104)で
「`SCHED_DEADLINE`をシェルスクリプトで試すにはフォークしたらアカン」
ということを書きました。
なので、3秒ごとに1ミリ秒間リアルタイムで動かすシェルスクリプトでは`sleep`コマンドを使わず、CPUを100%使わせてました。

　ただ、`sleep`なしでもBashを眠らせられないかと疑問に思ったので調べたところ、[stack overflowに、readにタイムアウトを設定して使う方法](https://stackoverflow.com/questions/32425457/bash-unix-how-can-i-pause-a-process-without-using-sleep-command)がありました。
ということでやってみました。`read`はビルトインコマンドなので、フォークしません。

## 実験

　前回のシェルスクリプトに、1行`read`の行を加えました。これで、「`SECONDS`の値が変わって`echo`したら次のループに行くまで1秒待つ」というコードになります。

```bash
ueda@raspi5:~$ cat some_task_read.bash
#!/bin/bash

n=1
while true ; do
	if [[ "$SECONDS" != "$PREV" ]] ; then
		echo $SECONDS $n  #これが仕事
		PREV=$SECONDS
		read -t 1 _hoge   #加筆: 入力を1秒待ってタイムアウト
	fi

	((n++))
done
```

　これを前回のリアルタイム処理と組み合わせると、

1. 前回から3秒後、`SECONDS`の値が変わっているので`echo`が実行される
2. `echo`のあとすぐに`read`が実行され、システムコールが発行されてカーネルがシェルスクリプトをランキューから外す
3. 1秒ではなく次の周期までシェルスクリプトが寝たままになり、3秒後に1に移行

という挙動になると思われます。

## 動かしてみる

　とりあえず単体で動かしてみます。

```bash
ueda@raspi5:~$ ./some_task_read.bash
0 1
1 2
2 3
3 4
4 5
・・・
```

　他の端末で見たところ、CPUはほとんど使ってませんでした。

ueda@raspi5:~$ ps u -C some_task_read.bash
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ueda        9431  0.0  0.0   5216  3200 pts/0    S+   18:51   0:00 /bin/bash ./some_task_read.bash

　ちなみに`read`の行がないと、CPUの使用率は100%になります。

## `SCHED_DEADLINE`と組み合わせる

　前回と同じ挙動になりました（端末の様子は割愛）。CPUはより使わないようになり、おそらく他のプロセスに迷惑をかける度合いは大幅に減少しているはずです。


　なるほど。

