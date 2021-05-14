---
Keywords: 日記,ROS
Copyright: (C) 2021 Ryuichi Ueda
---

# 日記（2021年5月14日）

プログラミングを始めると日記書いている場合じゃなくなる。

## ROS用価値反復モジュール

この前から作っている[emcl](https://github.com/ryuichiueda/emcl)に加え、[価値反復で大域的な経路計画をするモジュール](https://github.com/ryuichiueda/value_iteration)を作成中です。これも私が学生のときに使っていた大昔の技術なんですが、新しい研究に使うために実装しています。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解確率ロボティクスで詳解した価値反復で大域経路計画するROSのモジュール作ってます。<br><br>本ではオフラインの方法として紹介したけど計算から浮動小数点数を排除して高速化したので、これくらいの環境ならリアルタイムで使えてます。<a href="https://t.co/MkWeJHmB52">https://t.co/MkWeJHmB52</a> <a href="https://t.co/f3uLZSBSpj">pic.twitter.com/f3uLZSBSpj</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1393217064249139201?ref_src=twsrc%5Etfw">May 14, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

リアルタイムで使えるなら、どんな探索手法よりも強力なので、こちらも標準的な2次元のナビゲーションのモジュールの置き換えを狙いたいところです。ただ、ほんとに置き換えるなら`move_base`に組み込んで使えるようにしたほうがいいけど、`move_base`ガン無視で作っているので今後どうしようかとちょっと悩んでます。

