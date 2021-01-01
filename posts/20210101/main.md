---
Keywords: 日記
Copyright: (C) 2021 Ryuichi Ueda
---

# 日記（2020年12月31日〜2021年1月1日）

　年末年始は仕事とは別のことをするということで、
[駅データ.jp](https://ekidata.jp/)で公開停止になっているAPI
（が提供するデータ）をウェブ上に公開する作業をしてました。
もともとは新たに出る書籍のための作業なので仕事といえば仕事ですが・・・

　忘れそうなのでやったことをメモしておきます。

## DockerでAPI環境を構築

　nginx+php+MySQLの環境を構築。Docker Composeを初めて本格的に使用しました。
これをウェブ上で展開しようと思っていたのですが、
ローカルで操作しているうちに、
https://ekidata.jp/api/ で提供されているプログラムは、
APIというよりデータ生成プログラムであることに気づきました。
ということでローカルでプログラムを操作してXMLとJSONのデータを作成しました。

## GitHubにデータを置く

　https://github.com/ryuichiueda/eki に配置。


## 自分のウェブサーバで公開

　http://file.ueda.tech/eki/l/27002.xml というようなURLで公開しました。
https://ekidata.jp/api/api_station.php にあるように、
駅データ.jpさんのURLは 「https://ekidata.jp/api/記号/ファイル 」
というものでしたが、この「 https://ekidata.jp/api/ 」を
「 http://file.ueda.tech/eki/ 」に変えるとデータが得られます。

## uedashbotで利用可能に

　そのうち本家にもプルリク出します。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">泉岳寺 品川 北品川 新馬場 青物横丁 鮫洲 立会川 大森海岸 平和島 大森町 梅屋敷 京急蒲田 雑色 六郷土手 京急川崎 八丁畷 鶴見市場 京急鶴見 花月総持寺 生麦 京急新子安 子安 神奈川新町 京急東神奈川 神奈川 横浜 戸部 日ノ出町 黄金町 南太田 井土ヶ谷 弘明寺 上大岡 屏風浦 杉田 京急富岡 能見台 <a href="https://t.co/7CflCrrawI">https://t.co/7CflCrrawI</a></p>&mdash; uedashbot (@uedashbot) <a href="https://twitter.com/uedashbot/status/1344829045112856577?ref_src=twsrc%5Etfw">January 1, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 謝辞

　[駅データ.jp](https://ekidata.jp/)さん、データの公開と
第三者提供OKの太っ腹、誠にありがとうございます。
