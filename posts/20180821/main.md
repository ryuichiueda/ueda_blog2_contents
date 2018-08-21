---
Keywords: 頭の中だだ漏らし,日記,ffmpeg,ImageMagick
Copyright: (C) 2018 Ryuichi Ueda
---

# 雑記（2018年8月21日）

　頭が疲れて執筆も某氏のICRAの英語添削もやる気が起きない。

## 合成写真を作って遊ぶ（遊んでいるわけではない）

　論文用に昨日作成。論文の図というのはこちらの意図を早く掴んでもらうためには大変重要なので、いつも多くの時間を割く。一つ作るのに2日かけたことも過去にはあった。一方、書籍の場合は分量も多く、速く執筆しないといけないので、図は簡素に済ませて文章で補うようにしている。


　作り方は以下の通り:

```
mkdir tmp
ffmpeg -i hoge.MP4 -r 1 "tmp/%06d.png"  # hoge.MP4を1Hzでpng画像にバラす
cd tmp
convert *.png -evaluate-sequence min ../a.png # あるいはmax
```

`convert`のminは画像を合成するときに画素の暗いところを残し、maxは明るいところを残す。


　で、できたのが以下の画像。迷惑なツイートであり。


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">自分がいっぱい <a href="https://t.co/qiWMfu2K84">pic.twitter.com/qiWMfu2K84</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1031428001815126016?ref_src=twsrc%5Etfw">2018年8月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">幽霊バージョン <a href="https://t.co/zmp9bHpA1z">pic.twitter.com/zmp9bHpA1z</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1031429438892728320?ref_src=twsrc%5Etfw">2018年8月20日</a></blockquote>

　こちらは4コマだけ自分が入り込んだ画像。1Hzの連続写真で1歩飛ばしで写っているので、自分の歩行周期が0.5Hzだという知見を得た。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">またなんか別テイストなのができた。 <a href="https://t.co/2vcqrRru3d">pic.twitter.com/2vcqrRru3d</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1031448724101259264?ref_src=twsrc%5Etfw">2018年8月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



　`convert`ではラチが開かない場合はフォトショの出番。


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これも研究活動（辛い） <a href="https://t.co/TVso61Eh30">pic.twitter.com/TVso61Eh30</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1031431202580787200?ref_src=twsrc%5Etfw">2018年8月20日</a></blockquote>

　これは`convert`で合成した写真に、ロボットの写真を一つ一つフォトショップで重ねている作業の様子。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ホワイトバランス変わりすぎぃ！！！ <a href="https://t.co/LUSIrCsU9u">pic.twitter.com/LUSIrCsU9u</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1031434922433474561?ref_src=twsrc%5Etfw">2018年8月20日</a></blockquote>


## Hキー

 家で仕事中、MacBookのコードを長女が足にひっかけてしまい、ゴンッとなってHキーが効きづらくなった。一か八かで[こちら](https://tomokazu-kozuma.com/how-to-remove-keycaps-macbook-2016/)を参考に、精密ドライバーをHキーの上に差し込んだら、パキっと音がして直った。直ったのは反応だけでキーの下側の高さが少し低くなってしまったがとりあえずこれで使うことにする。真似は絶対にオススメしない。


それにしても疲れた。
