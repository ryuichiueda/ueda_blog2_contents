---
Keywords: emcl,詳解確率ロボティクス
Copyright: (C) 2021 Ryuichi Ueda
---

# 真面目にamclの代替ROSパッケージを作った

連休中はずっとこれを作ってました。とりあえず学内での反応がよさそうなので普及を目指します。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">mclに膨張リセットを実装してemclというパッケージを作りました。パーティクルの場所をずらしても少しなら収束します。こっちは実用を目指します。<br><br>（たぶんamclより使い勝手は良いはず。）<a href="https://t.co/u6MQhjRRuN">https://t.co/u6MQhjRRuN</a> <a href="https://t.co/sxPFCd0IzF">pic.twitter.com/sxPFCd0IzF</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1389450563503280128?ref_src=twsrc%5Etfw">May 4, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## なぜわざわざこんなことをしているのか

amclで済む場合はamclを使えばよいのですが、次の点で書き直してもいいんじゃないかと思いました。

1. amclはROSのインターフェイス部分がC++、推定ルーチンがCで書かれていて、手を入れようとするとややこしい
2. amclはロボットが止まっていると推定もほぼ停止

特に2については、同じリポジトリに同居している割には、navigationメタパッケージのナビゲーション方法と相性が悪いのが気になってました。というのは、navigationパッケージを使うと、自己位置推定に何かトラブルがあったときにロボットが静止することが多く、この場合にamclも止まってしまうと何も解決しないからです。もちろん、ロボットが静止していてもセンサデータを無理やり取り込むことはできるのですが、それなら最初から全部のセンサデータを使うようにしておいたほうが自然です。

## どういう実装にしたか

とりあえず、

* ロボットが動いていようが止まっていようが、一定周期でTFからオドメトリデータを取得
* センサデータは非同期に取り込んでおいて、オドメトリでパーティクルの姿勢を更新したあとに新しいセンサデータが届いていたら、そのデータを使ってパーティクルの重みを更新してリサンプリング
* パーティクルの重みの更新のあと、更新した重みの総和がしきい値を下回ったら膨張リセット
