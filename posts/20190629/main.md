---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月29日）

　日記、よっぱらいすぎて金曜をすっとばしてしまったが、老衰かなにかの影響で何をやったか全く覚えてない。だから日記を書くのか。なるほど。本日は大学で学生さんのご家族の方と面談。その前の空き時間で野球を見ながらラズパイマウスをいじってた。

## ROSのtf2で微妙な何かがあった

　以前はバリバリ動いていた[このパッケージ](https://github.com/ryuichiueda/raspimouse_navigation_3)を動かそうとして、

```
Invalid argument "/odom" passed to canTransform argument target_frame in tf2 frame_ids cannot start with a '/' like: ...
```

というエラーが出てなぜか動かないので修正。パラメータに指定するフレームの頭にスラッシュを入れたらアカンということにいつの間にか（あるいは元から）なってたっぽい。ということで、[こんなふう](https://github.com/ryuichiueda/raspimouse_navigation_3/commit/c1c3dca4ea008e7f488f6d39faaf0aa953568b71#diff-2f5bfa1f6175ba86d4a527709bc0a282)に変えたら動いた。

　こまかい経緯については何も調べてないのですが現場からは以上です。（テスト書かないとアカン・・・）

## 研究室でいつのまにかこういうものができてた

　完成度高い。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ARのロボットコントローラ + デバッグツール作りました <a href="https://t.co/ieqwQKevtb">pic.twitter.com/ieqwQKevtb</a></p>&mdash; えーす (@Ushiro_OTF) <a href="https://twitter.com/Ushiro_OTF/status/1144543273467334656?ref_src=twsrc%5Etfw">2019年6月28日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


いわゆる「机の下プロジェクト」だったみたいなんだけど、以前から研究室でやってたテーマではあるので、素直に頭をさげて研究室の成果とさせていただいた。あれがないこれがないという理由で学生さんの創作意欲を止めないよう、研究室の設備とかロボットとか環境とかを整えておくの大事やなと。


寝る。
