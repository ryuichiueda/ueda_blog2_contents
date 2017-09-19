---
Keywords: CLI,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】第23回梅雨でモワッとしたシェル芸勉強会
解答は<a href="https://blog.ueda.asia/?p=8381">こちら</a>

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
$ $ curl http://www.data.jma.go.jp/fcd/yoho/typhoon/statistics/landing/landing.csv |
 nkf -wLux &gt; landing.csv
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

<h2>Q2</h2>

monthly_typhoonから年ごとの台風の上陸頻度を集計し、元のlanding.csvの最後のフィールドに描いてある上陸頻度と比較してデータに間違いがなさそうなことを確認してください。

<h2>Q3</h2>

これまでの統計について、各月に台風が上陸した率を求めましょう。

<h2>Q4</h2>

各年で最初に台風が上陸した月を抽出し、何月が何回だったか集計してください。


<h2>Q5</h2>

台風が上陸しなかった年を抽出してください。

<h2>Q6</h2>

まず、<a href="http://www.city.osaka.lg.jp/shimin/page/0000298810.html" target="_blank">大阪市のページ</a>から、「平成27年 大阪市の犯罪発生情報 ひったくり」のデータを次のようにダウンロードして整形してください。<span style="color:red">なお、大阪を選んだ理由は2016年6月現在、ちゃんとテキストでこのようなデータを提供している大都市が他に見つからないからであり、他の意図があるわけではありません。</span>また、なぜか女性の被害者のデータしかないのですが、気にしないことにします。

```bash
$ curl http://www.city.osaka.lg.jp/shimin/cmsfiles/contents/0000298/298810/006hittakuri2015.csv |
 nkf -wLux | tr , ' ' | tail -n +2 &gt; hittakuri
$ head -n 5 hittakuri 
大阪市北区 曾根崎 １丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 1月 24日 2時頃 女性 20代
大阪市北区 兎我野町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 2月 11日 20時頃 女性 20代
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 3時頃 女性 20代
大阪市北区 曾根崎 ２丁目付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 13日 2時頃 女性 40代
大阪市北区 角田町 付近 窃盗 既遂 ひったくり 自動二輪 2015年 4月 7日 3時頃 女性 20代
```

データは、大阪市からクリエイティブコモンズライセンスCC-BYで提供されているものです。

このデータについて、各区で何件ずつレコードがあるか確認してください。

<h2>Q7</h2>

リポジトリのvol.23/OSAKAディレクトリに、各区の人口データ「population_h27sep」が入っています。このデータを使い、各区の人口当たりのひったくり件数のランキングを作ってください。

<h2>Q8</h2>

同一住所で同日に2件以上ひったくりが起こった場合について、その住所と日付を出力してください。

<h2>Q9</h2>

ひったくりの手段とその成功率を求めてください。ただし、通報が行われなかった事件はなかったと仮定します。

