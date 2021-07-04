---
Keywords: opy,シェル芸
Copyright: (C) 2021 Ryuichi Ueda
---

# opyを使ったCSV操作のベンチマーク

　Pythonでワンライナーを書くためのラッパーコマンド[opy](/?page=opy)について、CSVの読み書き機能のベンチマークをしてみました。1億行、4.2GBのCSVファイルを使いました。


　先に結論を書いておくと、`grep`や`awk`を駆使する場合にくらべて時間はかかりますが、そこそこ妥当な速度で処理ができました。データの中に改行があるCSVデータを処理するときには有効です。

## 使ったマシン

Intel Core i9-10885H（物理コア8個）を搭載したThinkPad P1です。DRAMの量は64GB。


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

## テスト1: 特定のデータだけ抽出

　3列目が富山県のデータだけを抽出してみましょう。


### grep、awkの場合

　`grep`だと4秒弱で抽出できます。ただし、列の構成を無視できるのなら、これで十分です。`awk`の場合は`-F,`で2列目を指定すると、30秒ちょいかかりました。

```
$ time grep 富山県 TESTDATA.csv > ans

real	0m3.841s
user	0m3.181s
sys	0m0.573s
$ head -n 3 ans
7163,富山県,"1,371,974",1994年5月26日
2528,富山県,"6,407,486",1992年10月1日
1320,富山県,"5,784,634",2009年3月7日
$ time awk -F, '$2=="富山県"' TESTDATA.csv > ans

real	0m30.454s
user	0m29.714s
sys	0m0.676s
```

### opyでCSVファイルを一度に読み込む場合

　3分30秒なので、`awk`の7倍くらいと、なかなか検討しています。

```bash
$ time cat TESTDATA.csv | opy -t csv '[T[k] for k in T.keys() if T[k][1] == "富山県"]' > ans

real	3m27.988s
user	3m15.827s
sys	0m20.873s
$ head -n 3 ans
['7163', '富山県', '1,371,974', '1994年5月26日']
['2528', '富山県', '6,407,486', '1992年10月1日']
['1320', '富山県', '5,784,634', '2009年3月7日']
### 空白区切りに戻す場合 ###
$ time cat TESTDATA.csv | opy -t csv '[" ".join(T[k]) for k in T.keys() if T[k][1] == "富山県"]' > ans

real	3m30.300s
user	3m14.338s
sys	0m18.589s
$ head -n 3 ans
7163 富山県 1,371,974 1994年5月26日
2528 富山県 6,407,486 1992年10月1日
1320 富山県 5,784,634 2009年3月7日
```

**ただし、全部CSVをDRAMに読み込むので、めちゃくちゃメモリ使います。**（この例だと46.1GBですね・・・）

```bash
$ while sleep 1 ; do top -b -n 1 -p 246057 ; done
・・・
top - 13:58:37 up 3 days,  5:15,  1 user,  load average: 1.78, 1.57, 1.23
（略）

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
 246057 ueda      20   0   46.1g  46.1g   6180 R 100.0  73.8   3:20.37 python3
・・・
```

### opyでCSVファイルを一行ずつ読み込む場合


　次のように、`-c`を使うと1行ずつCSVとしてレコードを読んでくれる（さらに`-C`でCSVで出力してくれる）ので、DRAMもほぼ使わずワンライナーも短く書けるのですが、時間がかかります。


```bash
### 100万行で17秒なので、1億行なら1700秒（28分強）。 ###
$ time cat TESTDATA.csv | head -n 1000000 | opy -cC 'F2=="富山県"' > ans

real	0m17.129s
user	0m17.126s
sys	0m0.426s
$ head -n 3 ans
"7163","富山県","1,371,974","1994年5月26日"
"2528","富山県","6,407,486","1992年10月1日"
"1320","富山県","5,784,634","2009年3月7日"
```

## テスト2: 数字の前処理+大小比較

　3列目の数字からカンマを取って、絶対値が100万未満のレコードを抽出してみます。`awk`でも2分近くかかります。


```bash
### カンマを消す作業は、他の列のデータがクォートされていないことを利用しており、若干ズルです。 ###
$ time cat TESTDATA.csv | awk -F'"' '{gsub(/,/,"",$2);print}'  | awk -F, '$3<1000000 && $3 > -1000000' > ans

real	1m51.880s
user	2m43.002s
sys	0m8.259s
```

　`opy`だと2倍強時間がかかりますが、データ構造をちゃんと見た上での作業時間なので、なかなか優秀です。ただし、DRAMはバカ食いしてます。

```bash
$ time cat TESTDATA.csv | opy -t csv '[T[k] for k in T.keys() if -1000000 < int(T[k][2].replace(",","")) < 1000000 ]' > ans

real	3m58.216s
user	3m41.913s
sys	0m18.827s
ueda@uedap1:~/tmp2$ head -n3 ans 
['1518', '和歌山県', '-988,312', '2008年12月7日']
['3669', '島根県', '-397,852', '2006年11月3日']
['8931', '山梨県', '-583,286', '2007年6月21日']
```

## テスト3: ソート


　4列目の年月日でデータをソートしてみます。`sort`はファイルからデータを読むとコア数だけ並列処理してくれるので、一度中間ファイルに入れてからソートします。

```bash
$ time  ( cat TESTDATA.csv | awk -F, '{a=$NF;gsub(/[年月日]/," ",a);print a,$0}' > tmp ; sort -k1,3n tmp | awk '{print $NF}' > ans )

real	7m36.403s
user	20m21.787s
sys	0m22.701s
$ head -n3 ans
0000,石川県,"6,774,912",1990年1月1日
0000,兵庫県,"-6,384,895",1990年1月1日
0001,東京都,"340,556",1990年1月1日
```

　`opy`でやってみましょう・・・と挑戦したんですが、「そんなでかいデータ扱えるか💢」と叱られました。


```bash
$ time cat TESTDATA.csv | opy -t csv -m datetime '{a=[ [datetime.datetime.strptime(e[3], "%Y年%m月%d日"),e] for e in T.values()]};{a.sort(key=lambda x:x[0])};[*[e[1] for e in a]]' > ans
強制終了

real	9m14.406s
user	8m49.024s
sys	0m23.651s
```


妥協して1000万行のソートの結果を示しておきます。1千万件でコア1個だけ使って1分半なら、まあまあ妥当でしょう。


```bash
$ time cat TESTDATA.csv | head -n 10000000 | opy -t csv -m datetime '[*sorted(T.values(), key=lambda x:datetime.datetime.strptime(x[3], "%Y年%m月%d日"))]' > ans

real	1m32.006s
user	1m29.025s
sys	0m3.676s
$ head -n 3 ans
['5390', '群馬県', '7,216,266', '1990年1月1日']
['9017', '山口県', '7,573,861', '1990年1月1日']
['0894', '栃木県', '6,389,064', '1990年1月1日']
```


とりあえず以上です。

