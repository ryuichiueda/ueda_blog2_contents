---
Keywords: opy,シェル芸
Copyright: (C) 2021 Ryuichi Ueda
---

# opyのCSV操作のベンチマーク

Pythonでワンライナーを書くためのラッパーコマンド[opy](/?page=opy)について、CSVの読み書き機能のベンチマークをしてみました。1億行、4.2GBのCSVファイルを使いました。`grep`や`awk`を駆使する場合にくらべて時間はかかりますが、そこそこ妥当な速度で処理ができました。

## 使ったマシン

Intel Core i9-10885H（物理コア8個）ThinkPad P1です。DRAMの量は64GB。


## 準備

　ベンチマーク用のデータを`https://file.ueda.tech/DATA_COLLECTION/TESTDATA.gz`から落とします。

```bash
$ wget https://file.ueda.tech/DATA_COLLECTION/TESTDATA.gz
$ ls -l
合計 1277320
-rw-rw-r-- 1 ueda ueda 1307970445  2月 14  2016 TESTDATA.gz
$ ls -lh
合計 1.3G
-rw-rw-r-- 1 ueda ueda 1.3G  2月 14  2016 TESTDATA.gz
```

内容を確認してから、CSV形式にします。

```bash
### zcatで内容確認 ###
$ zcat TESTDATA.gz | head -n 3
2377 高知県 -9,987,759 2001年1月5日
2910 鹿児島県 5,689,492 1992年5月6日
8458 大分県 1,099,824 2010年2月22日
### 3列目をダブルクォートで囲んで、全体をカンマ区切りに直す ###
$ zcat TESTDATA.gz | awk '{print $1","$2",\""$3"\","$4}' | head -n 3
2377,高知県,"-9,987,759",2001年1月5日
2910,鹿児島県,"5,689,492",1992年5月6日
8458,大分県,"1,099,824",2010年2月22日
### 全データを処理 ###
$ time zcat TESTDATA.gz | awk '{print $1","$2",\""$3"\","$4}' > TESTDATA.csv

real	0m37.401s
user	0m56.342s
sys	0m4.499s
### 行数の確認（1億行）###
$ wc -l TESTDATA.csv
100000000 TESTDATA.csv
### サイズは4.2GB ###
$ ls -lh TESTDATA.csv
-rw-rw-r-- 1 ueda ueda 4.2G  7月  4 13:41 TESTDATA.csv
```


