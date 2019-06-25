---
Keywords: 日記,ロボット,cartographer
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月25日）

　本日は午前が[講義資料書き](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap6_60min.html?#/)。午後は原稿の校正、つくばチャレンジチームのミーティング、そして下記のようにcartographerを実験のためにラズパイマウス用にカスタマイズ。

## [cartographer](http://wiki.ros.org/cartographer)をラズパイマウスで動かせた

　先日に引き続き、実験に使うcartographerのセッティング。なんとかなった。


　これが先日までの状況。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">オドメトリとオープンキャンパスの準備がグダグダだけど、Cartographerはラズパイマウスで動いた。 <a href="https://t.co/yivWLC6inX">pic.twitter.com/yivWLC6inX</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1141628586056540160?ref_src=twsrc%5Etfw">2019年6月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　今日の状況。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">できたー <a href="https://t.co/q4Pjddt2qC">pic.twitter.com/q4Pjddt2qC</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1143452290830852096?ref_src=twsrc%5Etfw">2019年6月25日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　いろいろガチャガチャ設定をいじったが、決定的だったのは、「`trajectory_builder_2d.lua`の`use_online_correlative_scan_matching`を`true`にする」だった。とりあえず雑ながら動いた設定を[ryuichiueda/raspimouse_cartographer](https://github.com/ryuichiueda/raspimouse_cartographer)にアップした。




