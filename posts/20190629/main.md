---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月29日）

　日記、よっぱらいすぎて金曜をすっとばしてしまったが、老衰かアルコールか尿もれか何かの影響で何をやったか全く覚えてない。だから日記を書くのか。なるほど。

　それはさておき本日については大学で学生さんのご家族の方と面談会。その前の空き時間で野球を見ながらラズパイマウスをいじってた。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">特に難しいこともしてないけど。 <a href="https://t.co/09Dglt8bBA">pic.twitter.com/09Dglt8bBA</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1144820357544591361?ref_src=twsrc%5Etfw">2019年6月29日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## ROSのtf2で微妙な何かがあった

　以前はバリバリ動いていた[このパッケージ](https://github.com/ryuichiueda/raspimouse_navigation_3)を動かそうとして、

```
Invalid argument "/odom" passed to canTransform argument target_frame in tf2 frame_ids cannot start with a '/' like: ...
```

というエラーが出てなぜか動かないので修正。パラメータに指定するフレームの頭にスラッシュを入れたらアカンということにいつの間にか（あるいは元から）なってたっぽい。ということで、[こんなふう](https://github.com/ryuichiueda/raspimouse_navigation_3/commit/c1c3dca4ea008e7f488f6d39faaf0aa953568b71#diff-2f5bfa1f6175ba86d4a527709bc0a282)に変えたら動いた。

　こまかい経緯については何も調べてないけど現場からは以上です。

## 研究室でいつのまにかこういうものができてた

　完成度高い。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ARのロボットコントローラ + デバッグツール作りました <a href="https://t.co/ieqwQKevtb">pic.twitter.com/ieqwQKevtb</a></p>&mdash; えーす (@Ushiro_OTF) <a href="https://twitter.com/Ushiro_OTF/status/1144543273467334656?ref_src=twsrc%5Etfw">2019年6月28日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


いわゆる「机の下プロジェクト」だったみたいなんだけど、以前から研究室でやってたテーマ（下のYouTubeのものが先祖）ではあるので、素直に頭をさげて研究室の成果とさせていただいた。あれがないこれがないという理由で学生さんの創作意欲を止めないよう、研究室の設備とかロボットとか環境とかを整えておくの大事やなと。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Kvja3ROYhB4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 本日のエモい発言からの流れるような宣伝

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">なんかいろいろごちゃごちゃごちゃ言ってしまったけど、自分は、読んでなんか気持ちよくなる本より、読んだ後に何か満たされない思いが残って自分で調べたり試したりしてもらえるような本を書かねばならんと思っているのです。</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1144969295148933120?ref_src=twsrc%5Etfw">June 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ということで、「[フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版](/?post=20190616_bashcms2_book)」、絶賛発売中ですのでぜひともよろしくお願いいたします。


寝る。
