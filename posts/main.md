---
Keywords: arXiv, 研究
Copyright: (C) 2019 Ryuichi Ueda
---

# arXivにpdf投げた

　昨年のICRAのアルゴリズムについて大幅に実験増やして投稿論文にしたけど、比較がなくて通らん+クソ忙しい+これ比較いらんだろ（学生の反面教師感が甚だしい）ということでarXivにのせて放置することにしました。

* https://arxiv.org/abs/1904.08761

色々古い人間なので投稿は初めてというのは先日書いたとおりでしたがその後スムーズに公開されました。

　内容は移動ロボットの教示。下のビデオでは「teaching」と表示されているときに私がゲームパッドで動きを教えていて、「replay」でロボットが行動を再現しています。パーティクルフィルタで実装されたベイスフィルタで動いていますが自己位置推定はしていません。

<iframe width="560" height="315" src="https://www.youtube.com/embed/nLhoIT9r_ls" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

　まだできることがほんの些細なのですが、超絶簡単なアルゴリズムでここまでできており、個人的には面白いです。もちろん世間の判断は違いますが、移動ロボットを触ったことある人にとっては、この些細な実験が見かけほど簡単ではないことは理解できると思います。

　コードはここに置いてあります。ラズパイマウスでしか動きませんが読むのは簡単かと。

* https://github.com/ryuichiueda/raspimouse_gamepad_teach_and_replay

　寝るます。
