---
Keywords: 日記
Copyright: (C) 2022 Ryuichi Ueda
---

# 日記（2022年9月20日）

　ICRAの学生の原稿は無事提出されたけど明日ビデオの締め切り。SIの締め切りが来週。本の執筆は89/250[pages]。


## PCREの「.」

シェル・ワンライナー160本ノックへの https://github.com/shellgei/shellgei160/issues/52 の指摘について、ebanさんから「`grep -zP`」としたときに改行は「`.`」でマッチしないと教えてもらいました。これがミニマムな例でしょうか。


```bash
$ seq 5 | grep -zoP 1.   #マッチしない
$ seq 5 | grep -zo. 1.   #.が1のうしろの改行にマッチ
1
$ seq 5 | grep -zoE 1.   #.が1のうしろの改行にマッチ
1
```
