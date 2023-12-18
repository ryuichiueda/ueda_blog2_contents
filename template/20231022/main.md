---
Keywords: シェル, bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# シェルのジョブまわりのメモ2

　[このメモ](/?post=20231008)に引き続き、[連載](/?page=sd_rusty_bash)のためのおさらいと予習です。
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

## プロセスグループ

　パイプラインに相当する部分（コマンドひとつだけの命令を含む）は互いに独立なプロセスグループID（PGID）を持つ。

```bash
$ ps -fj --forest
UID          PID    PPID    PGID     SID  C STIME TTY          TIME CMD
ueda       22711    5222   22711   22711  0 10月21 pts/2  00:00:00 bash
ueda       34862   22711   34862   22711  0 07:37 pts/2    00:00:00  \_ ps -fj --forest #bashと違うPGID
$ sleep 10 | ps -fj --forest
UID          PID    PPID    PGID     SID  C STIME TTY          TIME CMD
ueda       22711    5222   22711   22711  0 10月21 pts/2  00:00:00 bash
ueda       34867   22711   34867   22711  0 07:38 pts/2    00:00:00  \_ sleep 10 #bashと違うPGID
ueda       34868   22711   34867   22711  0 07:38 pts/2    00:00:00  \_ ps -fj --forest  #sleepとおなじPGID
```

