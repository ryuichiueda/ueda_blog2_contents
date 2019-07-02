---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月2日）

　本日は午前に研究の準備、午後につくばチャレンジのミーティング。たぶん腰が凝ってて股関節から股間にかけて痛く、集中力皆無。

## ROSいじり

　昨日からやってたことができてロボットが動くようになった。詳細はいずれ真面目に書く。


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">某アルゴリズム一応動いた。 <a href="https://t.co/nq0hcEuvpT">pic.twitter.com/nq0hcEuvpT</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1145881389511745536?ref_src=twsrc%5Etfw">2019年7月2日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

本当はロボットに四角を描かせたいのだがamclのチューニングが甘い（というより実質機能していない）のでずれる。明日チューニングする。

## フロアの地図作成

　[Cartographer](https://google-cartographer-ros.readthedocs.io/en/latest/)で研究室の階の地図を作成。gmappingのように途中で変な地図が選ばれて台無しということが原理的になさそうなので楽。

<iframe width="560" height="315" src="https://www.youtube.com/embed/jS5_a9BW2zI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">さっき作った地図とロボットの軌跡 <a href="https://t.co/fBEyG3sRJL">pic.twitter.com/fBEyG3sRJL</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1145989955052642305?ref_src=twsrc%5Etfw">July 2, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## このサイトが落ちてた

　[bashcms本](https://amzn.to/2RUgY3y)に書いてあるシステムに移行して初めて落ちたと記憶。bashcms本を読んで誰かがうまく落としたんじゃないかと「おー！すげー！」となったが、こういうことだった。自爆だった。つまらん。

1. 自宅のラズパイから毎日一回、ウェブサーバのバックアップをとっている。
1. このときにウェブサーバ上で大きなtarファイルを作る。
1. 普段はラズパイにつながっているHDDにtarファイルをダウンロードしてからウェブサーバ側のtarファイルを削除している。
1. ところがHDDに何かあって書き込めなくなった。
1. ウェブサーバがtarファイルでパンク。

とりあえずラズパイを再起動したら直った。

　逆をいえば、ラズパイもウェブサーバもbashcmsも2年近く、何も問題もなく動いていたと。しかし、タイミング悪い。そろそろHDDを買い替えなければ。

## 今日のシェル芸

　キングウンコじゃなくてウンコクイーンじゃないのだろか？？？

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">アイマスってやつか…<br> <a href="https://t.co/Zg8BTQRkOU">https://t.co/Zg8BTQRkOU</a> <a href="https://t.co/bUOLoLGsWd">pic.twitter.com/bUOLoLGsWd</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1145697862740631557?ref_src=twsrc%5Etfw">2019年7月1日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　寝る。
