---
Keywords:CLI,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第23回梅雨でモワッとしたシェル芸勉強会
問題だけのページは<a href="https://blog.ueda.asia/?p=8465">こちら</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
GitHubにあります。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.23">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.23</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>環境</h2><br />
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
<br />
<table><br />
 <tr><br />
 <th>Mac,BSD系</th><br />
 <th>Linux</th><br />
 </tr><br />
 <tr><br />
 <td>gdate</td><br />
 <td>date</td><br />
 </tr><br />
 <tr><br />
 <td>gsed</td><br />
 <td>sed</td><br />
 </tr><br />
 <tr><br />
 <td>tail -r</td><br />
 <td>tac</td><br />
 </tr><br />
 <tr><br />
 <td>gtr</td><br />
 <td>tr</td><br />
 </tr><br />
 <tr><br />
 <td>gfold</td><br />
 <td>fold</td><br />
 </tr><br />
</table><br />
<br />
<br />
<h2>イントロ</h2><br />
<br />
<a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac23%e5%9b%9e%e6%a2%85%e9%9b%a8%e3%81%a7%e3%83%a2%e3%83%af%e3%83%83%e3%81%a8%e3%81%97%e3%81%9f%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">スライド</a><br />
<br />
<br />
<h2>Q1</h2><br />
<br />
まず、次のように、気象庁の毎月の台風の上陸数に関するデータをダウンロードし、landing.csvというファイルに保存してください。<span style="color:red">UTF-8に見えてもExcelから作ったCSVはBOM付きだったりするので、ネットから入手したデータは最初にnkfに通す癖を。</span><br />
<br />
[bash]<br />
$ curl http://www.data.jma.go.jp/fcd/yoho/typhoon/statistics/landing/landing.csv |<br />
 nkf -wLux &gt; landing.csv<br />
[/bash]<br />
<br />
次にこのデータを、以下のようなデータ（ファイル名: monthly_typhoon）に変換してください。第1フィールドが年月、第2フィールドが台風の上陸頻度です。<br />
<br />
[bash]<br />
$ head monthly_typhoon <br />
195101 0<br />
195102 0<br />
195103 0<br />
195104 0<br />
195105 0<br />
195106 0<br />
195107 1<br />
195108 0<br />
195109 0<br />
195110 1<br />
$ tail monthly_typhoon <br />
201503 0<br />
201504 0<br />
201505 0<br />
201506 0<br />
201507 2<br />
201508 1<br />
201509 1<br />
201510 0<br />
201511 0<br />
201512 0<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat landing.csv | awk -F, '{for(i=2;i&lt;=13;i++){print $1,$i}}' |<br />
 grep -v 年 | awk '{print $1 sprintf(&quot;%02d&quot;,(NR-1)%12+1),$2}' |<br />
 awk 'NF==1{print $1,0}NF!=1' &gt; monthly_typhoon<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
monthly_typhoonから年ごとの台風の上陸頻度を集計し、元のlanding.csvの最後のフィールドに描いてある上陸頻度と比較してデータに間違いがなさそうなことを確認してください。<br />
<br />
<h3>解答</h3><br />
<br />
次のように書いて出力がなければ整合性が取れています。<br />
<br />
[bash]<br />
$ cat monthly_typhoon |<br />
 awk '{a[substr($1,1,4)]+=$2}END{for(k in a)print k,a[k]}' |<br />
 sort | paste - &lt;(tail -n +2 landing.csv | sed 's/,$/,0/') |<br />
 tr , ' ' | awk '$1!=$3 || $2!=$NF'<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
これまでの統計について、各月に台風が上陸した率を求めましょう。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat monthly_typhoon | sed 's/^....//' |<br />
 awk '$2==0{a[$1]++}$2!=0{b[$1]++}END{for(k in a){print k,b[k]/(a[k]+b[k])}}' |<br />
 sort<br />
01 0<br />
02 0<br />
03 0<br />
04 0.0153846<br />
05 0.0307692<br />
06 0.138462<br />
07 0.4<br />
08 0.630769<br />
09 0.630769<br />
10 0.2<br />
11 0.0153846<br />
12 0<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
各年で最初に台風が上陸した月を抽出し、何月が何回だったか集計してください。<br />
<br />
<h3>解答</h3><br />
<br />
まずこうすると各年で何月だったか分かります。<br />
<br />
[bash]<br />
$ sed 's/^..../&amp; /' monthly_typhoon | grep -v ' 0$' | uniq -w4<br />
[/bash]<br />
<br />
何月が何回だったかは次の通り。<br />
<br />
[bash]<br />
$ sed 's/^..../&amp; /' monthly_typhoon | grep -v ' 0$' | uniq -w4 |<br />
 awk '{print $2}' | sort | uniq <br />
c- 1 04<br />
 2 05<br />
 9 06<br />
 21 07<br />
 19 08<br />
 7 09<br />
 2 10<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
台風が上陸しなかった年を抽出してください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat monthly_typhoon | sed 's/.. / /' | grep ' 0$' |<br />
 uniq -c | awk '$1==12{print $2}'<br />
1984<br />
1986<br />
2000<br />
2008<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
まず、<a href="http://www.city.osaka.lg.jp/shimin/page/0000298810.html" target="_blank">大阪市のページ</a>から、「平成27年 大阪市の犯罪発生情報 ひったくり」のデータを次のようにダウンロードして整形してください。<span style="color:red">なお、大阪を選んだ理由は2016年6月現在、ちゃんとテキストでこのようなデータを提供している大都市が他に見つからないからであり、他の意図があるわけではありません。</span>また、なぜか女性の被害者のデータしかないのですが、気にしないことにします。<br />
<br />
[bash]<br />
$ curl http://www.city.osaka.lg.jp/shimin/cmsfiles/contents/0000298/298810/006hittakuri2015.csv |<br />
 nkf -wLux | tr , ' ' | tail -n +2 &gt; hittakuri<br />
$ head -n 5 hittakuri <br />
大阪市北区 曾根崎 １丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 1月 24日 2時頃 女性 20代<br />
大阪市北区 兎我野町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 2月 11日 20時頃 女性 20代<br />
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 3時頃 女性 20代<br />
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 2時頃 女性 40代<br />
大阪市北区 角田町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 7日 3時頃 女性 20代<br />
[/bash]<br />
<br />
データは、大阪市からクリエイティブコモンズライセンスCC-BYで提供されているものです。<br />
<br />
このデータについて、各区で何件ずつレコードがあるか確認してください。<br />
<br />
<h3>解答</h3><br />
<br />
データの確認のため、あえて簡単にしてみました。<br />
<br />
[bash]<br />
$ awk '{print $1}' hittakuri | sort | uniq <br />
c- 19 大阪市阿倍野区<br />
 8 大阪市旭区<br />
 6 大阪市港区<br />
 1 大阪市此花区<br />
 29 大阪市住吉区<br />
 9 大阪市住之江区<br />
 23 大阪市城東区<br />
 31 大阪市生野区<br />
 28 大阪市西区<br />
 37 大阪市西成区<br />
 8 大阪市西淀川区<br />
 7 大阪市大正区<br />
 56 大阪市中央区<br />
 6 大阪市鶴見区<br />
 20 大阪市天王寺区<br />
 15 大阪市都島区<br />
 22 大阪市東住吉区<br />
 18 大阪市東成区<br />
 17 大阪市東淀川区<br />
 9 大阪市福島区<br />
 33 大阪市平野区<br />
 53 大阪市北区<br />
 31 大阪市淀川区<br />
 22 大阪市浪速区<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
リポジトリのvol.23/OSAKAディレクトリに、各区の人口データ「population_h27sep」が入っています。このデータを使い、各区の人口当たりのひったくり件数のランキングを作ってください。<br />
<br />
<h3>解答</h3><br />
<br />
指数表記になるとちゃんとソート順が変わる等面倒なので気をつけましょう。<br />
<br />
[bash]<br />
$ awk '{print $1}' hittakuri | sort | uniq -c |<br />
 awk '{print $2,$1}' | LANG=C sort | join - &lt;(LANG=C sort population_h27sep) |<br />
 awk '{printf(&quot;%s %7f\\n&quot;,$1,$2/$3)}' | sort -k2,2nr<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
同一住所で同日に2件以上ひったくりが起こった場合について、その住所と日付を出力してください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat hittakuri | awk '{print $1$2$3,$8,$9,$10}' | sort | uniq -d<br />
大阪市北区角田町付近 2015年 11月 4日<br />
大阪市北区曾根崎２丁目付近 2015年 4月 13日<br />
大阪市淀川区十三本町１丁目付近 2015年 4月 16日<br />
[/bash]<br />
<br />
<h2>Q9</h2><br />
<br />
ひったくりの手段とその成功率を求めてください。ただし、通報が行われなかった事件はなかったと仮定します。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ awk '{print $5,$7}' hittakuri | awk '$1==&quot;既遂&quot;{a[$2]++}{b[$2]++}END{for(k in a){print k,a[k]/b[k]}}'<br />
徒歩 0.942308<br />
自動車 0.904762<br />
自転車 0.92053<br />
自動二輪 0.954225<br />
[/bash]<br />

