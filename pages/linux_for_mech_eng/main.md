---
Keywords: 書籍
Copyright: (C) Ryuichi Ueda
---

# 某本のためのサイト


## Linux環境の整備

- ラズパイのセットアップ
    - [Ubuntu Server 24.04 LTS](/?page=raspi_ubuntu_server_setup)

## 参考にしたサイト

- https://rheb.hatenablog.com/entry/2023/03/13/135419
- https://eng-blog.iij.ad.jp/archives/27285
- https://medium.com/@joseagustin.barra/understanding-priority-levels-in-linux-cd8c82eb4dd
- https://qiita.com/nhiroki/items/2fa7bb048118145b00cd
- https://bootlin.com/doc/training/preempt-rt/preempt-rt-slides.pdf
- https://www.valinux.co.jp/blog/entry/20250303
- https://www.global.toshiba/jp/company/digitalsolution/articles/tsoul/tech/t0902.html
- https://gihyo.jp/article/2024/10/daily-linux-241016
- https://qiita.com/rarul/items/7ac832563d935dd7ab88
    - fsfreeze
- https://leavatail.hatenablog.com/entry/2022/01/01/000000#writeback-kthread%E3%81%AE%E6%A6%82%E8%A6%81
    - writebackについて
- https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news171.html
    - システムコール
- https://pingcap.co.jp/blog/linux-kernel-vs-memory-fragmentation-1/
    - メモリのフラグメンテーションについて

### スケジューラ

- スケジューリングクラス
    - https://qiita.com/ueba/items/749e8da79b49fc0bc932
    - https://qiita.com/ueba/items/0e8fe57a4b421eb5622d
    - https://qiita.com/ueba/items/d3e69e047f71a2b52207
- SCHED_BATCHについて
    - https://zenn.dev/tmsn/articles/af8116d7ba13da

### TASK_IDLEについて

- https://hiboma.hatenadiary.jp/entry/2017/11/02/102713
- https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=80ed87c8a9ca0cad7ca66cf3bbdfb17559a66dcf

### スワップに関する話題

- [全プロセスが一秒止まる不具合、原因はLinuxカーネルにあり？](https://zenn.dev/turing_motors/articles/a460fe08b54253)

### ゾンビに関する話題

- https://stackoverflow.com/questions/26996201/zombie-process-even-though-threads-are-still-running
- https://www.sourceware.org/bugzilla/show_bug.cgi?id=9804
