---
Keywords: 日記, ROS, CMake
Copyright: (C) 2022 Ryuichi Ueda
---

# 日記（2022年3月21日）

　午前は共同研究の年度末報告書のとりまとめと査読関係。午後は昼寝したあとコードをいじる。

## ロボット学会誌の論文が正式に公表

　よくルールを知らないんですが、フリーアクセスっぽいです（うれしい）。ぜひ読んでみてください。畳み込みニューラルネットワークを、本物にかなり近いCGで学習させています。学生さん主導の研究です。深層学習なんもわからん。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ロボット学会誌の論文、正式に公表されました。葉っぱボサボサの畑で作物の茎を検出できるようになったよという研究。（なんかフリーで見れるっぽい）<br><br>J-STAGE Articles - 密生した圃場における一部が隠れた果菜類の主茎の検出 <a href="https://t.co/G2ax1jK7Bj">https://t.co/G2ax1jK7Bj</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1505897188877955073?ref_src=twsrc%5Etfw">March 21, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## [ナビゲーション用バカ価値反復パッケージ](https://github.com/ryuichiueda/value_iteration)の改良

　ロボティクスシンポジアで発表したアルゴリズムが、発表直前に無駄の多いことに気づき、本日修正。具体的には、大域計画中に発見した未知障害物を、そのまま大域計画に織り込んでしまうようにしました。これまでは局所計画でしか未知障害物を扱っておらず、この無意味な制約でアルゴリズムが複雑で効率悪くなっていました。この修正で、計算量もコードの量も減りました。詳しくは・・・そのうち学会で発表します。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">価値反復を無理やりリアルタイムで使って経路計画するパッケージ、しつこく障害物を置いてもさっと迂回できるように改良しました。<a href="https://t.co/aYasSFfwXH">https://t.co/aYasSFfwXH</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1505871029360480257?ref_src=twsrc%5Etfw">March 21, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　早く誰かに使ってもらえるようにしなければ意味がないので、試したい方には、GitHubかTwitterでつきっきりで対応いたします。


