---
Keywords: CLI,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第23回梅雨でモワッとしたシェル芸勉強会
問題だけのページは<a href="https://blog.ueda.asia/?p=8465">こちら</a>

<h2>問題で使うファイル等</h2>

GitHubにあります。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.23">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.23</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>


<h2>イントロ</h2>

<a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac23%e5%9b%9e%e6%a2%85%e9%9b%a8%e3%81%a7%e3%83%a2%e3%83%af%e3%83%83%e3%81%a8%e3%81%97%e3%81%9f%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">スライド</a>


<h2>Q1</h2>

まず、次のように、気象庁の毎月の台風の上陸数に関するデータをダウンロードし、landing.csvというファイルに保存してください。<span style="color:red">UTF-8に見えてもExcelから作ったCSVはBOM付きだったりするので、ネットから入手したデータは最初にnkfに通す癖を。</span>

```bash
$ curl http://www.data.jma.go.jp/fcd/yoho/typhoon/statistics/landing/landing.csv |
 nkf -wLux > landing.csv
```

次にこのデータを、以下のようなデータ（ファイル名: monthly_typhoon）に変換してください。第1フィールドが年月、第2フィールドが台風の上陸頻度です。

```bash
$ head monthly_typhoon 
195101 0
195102 0
195103 0
195104 0
195105 0
195106 0
195107 1
195108 0
195109 0
195110 1
$ tail monthly_typhoon 
201503 0
201504 0
201505 0
201506 0
201507 2
201508 1
201509 1
201510 0
201511 0
201512 0
```

<h3>解答</h3>

```bash
$ cat landing.csv | awk -F, '{for(i=2;i<=13;i++){print $1,$i}}' |
 grep -v 年 | awk '{print $1 sprintf("%02d",(NR-1)%12+1),$2}' |
 awk 'NF==1{print $1,0}NF!=1' > monthly_typhoon
```

<h2>Q2</h2>

monthly_typhoonから年ごとの台風の上陸頻度を集計し、元のlanding.csvの最後のフィールドに描いてある上陸頻度と比較してデータに間違いがなさそうなことを確認してください。

<h3>解答</h3>

次のように書いて出力がなければ整合性が取れています。

```bash
$ cat monthly_typhoon |
 awk '{a[substr($1,1,4)]+=$2}END{for(k in a)print k,a[k]}' |
 sort | paste - <(tail -n +2 landing.csv | sed 's/,$/,0/') |
 tr , ' ' | awk '$1!=$3 || $2!=$NF'
```

<h2>Q3</h2>

これまでの統計について、各月に台風が上陸した率を求めましょう。

<h3>解答</h3>

```bash
$ cat monthly_typhoon | sed 's/^....//' |
 awk '$2==0{a[$1]++}$2!=0{b[$1]++}END{for(k in a){print k,b[k]/(a[k]+b[k])}}' |
 sort
01 0
02 0
03 0
04 0.0153846
05 0.0307692
06 0.138462
07 0.4
08 0.630769
09 0.630769
10 0.2
11 0.0153846
12 0
```

<h2>Q4</h2>

各年で最初に台風が上陸した月を抽出し、何月が何回だったか集計してください。

<h3>解答</h3>

まずこうすると各年で何月だったか分かります。

```bash
$ sed 's/^..../& /' monthly_typhoon | grep -v ' 0$' | uniq -w4
```

何月が何回だったかは次の通り。

```bash
$ sed 's/^..../& /' monthly_typhoon | grep -v ' 0$' | uniq -w4 |
 awk '{print $2}' | sort | uniq 
c- 1 04
 2 05
 9 06
 21 07
 19 08
 7 09
 2 10
```

<h2>Q5</h2>

台風が上陸しなかった年を抽出してください。

<h3>解答</h3>

```bash
$ cat monthly_typhoon | sed 's/.. / /' | grep ' 0$' |
 uniq -c | awk '$1==12{print $2}'
1984
1986
2000
2008
```

<h2>Q6</h2>

まず、<a href="http://www.city.osaka.lg.jp/shimin/page/0000298810.html" target="_blank">大阪市のページ</a>から、「平成27年 大阪市の犯罪発生情報 ひったくり」のデータを次のようにダウンロードして整形してください。<span style="color:red">なお、大阪を選んだ理由は2016年6月現在、ちゃんとテキストでこのようなデータを提供している大都市が他に見つからないからであり、他の意図があるわけではありません。</span>また、なぜか女性の被害者のデータしかないのですが、気にしないことにします。

```bash
$ curl http://www.city.osaka.lg.jp/shimin/cmsfiles/contents/0000298/298810/006hittakuri2015.csv |
 nkf -wLux | tr , ' ' | tail -n +2 > hittakuri
$ head -n 5 hittakuri 
大阪市北区 曾根崎 １丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 1月 24日 2時頃 女性 20代
大阪市北区 兎我野町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 2月 11日 20時頃 女性 20代
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 3時頃 女性 20代
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 2時頃 女性 40代
大阪市北区 角田町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 7日 3時頃 女性 20代
```

データは、大阪市からクリエイティブコモンズライセンスCC-BYで提供されているものです。

このデータについて、各区で何件ずつレコードがあるか確認してください。

<h3>解答</h3>

データの確認のため、あえて簡単にしてみました。

```bash
$ awk '{print $1}' hittakuri | sort | uniq 
c- 19 大阪市阿倍野区
 8 大阪市旭区
 6 大阪市港区
 1 大阪市此花区
 29 大阪市住吉区
 9 大阪市住之江区
 23 大阪市城東区
 31 大阪市生野区
 28 大阪市西区
 37 大阪市西成区
 8 大阪市西淀川区
 7 大阪市大正区
 56 大阪市中央区
 6 大阪市鶴見区
 20 大阪市天王寺区
 15 大阪市都島区
 22 大阪市東住吉区
 18 大阪市東成区
 17 大阪市東淀川区
 9 大阪市福島区
 33 大阪市平野区
 53 大阪市北区
 31 大阪市淀川区
 22 大阪市浪速区
```

<h2>Q7</h2>

リポジトリのvol.23/OSAKAディレクトリに、各区の人口データ「population_h27sep」が入っています。このデータを使い、各区の人口当たりのひったくり件数のランキングを作ってください。

<h3>解答</h3>

指数表記になるとちゃんとソート順が変わる等面倒なので気をつけましょう。

```bash
$ awk '{print $1}' hittakuri | sort | uniq -c |
 awk '{print $2,$1}' | LANG=C sort | join - <(LANG=C sort population_h27sep) |
 awk '{printf("%s %7f\\n",$1,$2/$3)}' | sort -k2,2nr
```

<h2>Q8</h2>

同一住所で同日に2件以上ひったくりが起こった場合について、その住所と日付を出力してください。

<h3>解答</h3>

```bash
$ cat hittakuri | awk '{print $1$2$3,$8,$9,$10}' | sort | uniq -d
大阪市北区角田町付近 2015年 11月 4日
大阪市北区曾根崎２丁目付近 2015年 4月 13日
大阪市淀川区十三本町１丁目付近 2015年 4月 16日
```

<h2>Q9</h2>

ひったくりの手段とその成功率を求めてください。ただし、通報が行われなかった事件はなかったと仮定します。

<h3>解答</h3>

```bash
$ awk '{print $5,$7}' hittakuri | awk '$1=="既遂"{a[$2]++}{b[$2]++}END{for(k in a){print k,a[k]/b[k]}}'
徒歩 0.942308
自動車 0.904762
自転車 0.92053
自動二輪 0.954225
```

