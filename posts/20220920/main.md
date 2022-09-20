---
Keywords: 日記
Copyright: (C) 2022 Ryuichi Ueda
---

# 日記（2022年9月20日）

　ICRAの学生の原稿は無事提出されたけど明日ビデオの締め切り。SIの締め切りが来週。
たのむからみんな作文に関心持って、学生同士で文章を添削できるようになってほしい。
本の執筆は89/250[pages]。


## PCREの.（ドット）

シェル・ワンライナー160本ノックへの https://github.com/shellgei/shellgei160/issues/52 の指摘について、ebanさんから「`grep -zP`」としたときに、改行は「`.`」でマッチしないと教えてもらいました。これがミニマムな例でしょうか。


```bash
$ seq 5 | grep -zoP 1.   #マッチしない
$ seq 5 | grep -zo. 1.   #.が1のうしろの改行にマッチ
1
$ seq 5 | grep -zoE 1.   #.が1のうしろの改行にマッチ
1
```

## 本の事後分布の説明

こんなことを思った。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">なんで事後確率求めるのにヒストグラムフィルタ使わずに「周辺尤度が計算できないから・・・」みたいな難しい話から入ってく説明ばっかりなんだろ？</p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1571973834311634944?ref_src=twsrc%5Etfw">September 19, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


ということで、最初はヒストグラムフィルタ使って説明することにした。
グラフを折れ線グラフにしているので分かりにくいけど、
横軸を0.01刻みで離散型確率変数にしてます。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ヒストグラムフィルタでベルヌーイ試行の事後分布求めたら、ベータ分布っぽくなった。（そりゃそうか。ん？そうなの？） <a href="https://t.co/1iCJWbzdXu">https://t.co/1iCJWbzdXu</a> <a href="https://t.co/1ND3fe8yLC">pic.twitter.com/1ND3fe8yLC</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1572184616509014016?ref_src=twsrc%5Etfw">September 20, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## YouTubeの視聴回数20万回超え

ご視聴いただきありがとうございます。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">YouTubeの視聴回数20万回突破しました。 <a href="https://t.co/LITgfij9Hw">pic.twitter.com/LITgfij9Hw</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1569635897783746560?ref_src=twsrc%5Etfw">September 13, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

