---
Keywords: ROS 2
Copyright: (C) 2024 Ryuichi Ueda
---

# C++で作ったROS 1のパッケージをROS 2に移植するときのつまづきポイント ―その3

　https://github.com/ryuichiueda/value_iteration
を
https://github.com/ryuichiueda/value_iteration2
に移植中です（おわらねー）。今日は「RVizがゴールをtopicに吐いてくれない」という謎現象を解決しました。


## Nav2用のRVizのプラグインがあるらしい（ので葬らんした）

RVizの画面の「ゴールを矢印を引いて指定するやつ」
の出力を取得する方法を探していたところ、
「nav2_utilで
