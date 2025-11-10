---
Keywords: 自作シェル,rusty_bash,寿司シェル
Copyright: (C) 2025 Ryuichi Ueda
---

# 近況（2025年11月10日）

　ずっとブログやシェル芸勉強会をさぼって半年間、ニューラルネット〜VLA（画像とか言葉の指示とかでロボットを動かすやつ）の勉強をしていました。特にシェル芸界隈のみなさますみません。

## きっかけ

　5月あたりに急に後期の画像処理の講義を担当することになって、そういえば学科にVLAの講義がないなあと思ってイチから講義を組み直すことにしました。

## 問題

　他にいろいろネタがあったので、いままでニューラルネットワークに全く手を出してこなかった。

## 対応

　とりあえず必読の[ゼロから作るDeep Learning](https://demuc.de/papers/schoenberger2016sfm.pdf)から初めて、学生のときに雑に勉強していたのを真面目に学び直し、あとはTransformerの教科書を何冊か読みました。んで、その後、主要な論文を読み始め、分からんことがあると教科書に戻ったり、引用されている論文を読んでいきました。最終的に[$\pi_0$というVLAの論文](https://arxiv.org/abs/2410.24164)を読んで、だいたいなにやってるか分かるかなあ・・・というところまできました。

　勉強した感想ですが、1995〜2005年ごろのニューラルネットとちがって、確率論が絡んでたり思ったより合理的な世界なんだなあと思いました（こなみかん）。確率論が絡んで洗練されているので、「あーあーあーそうね」という箇所が多くて、なんか首の皮一枚つながった感があります。

　特に、オートエンコーダーのところは、自分がニューラルネットなしで博士論文でやってたこと（方策の圧縮）と関係するので、試したことないけどなんか共感しました。（オートエンコーダーの論文が出たのは自分が博士論文を書いていた頃の2006年です。）


## 錬成された講義資料

　元々素人が作ったものなんですが、学生さんはこれ見て私の説明受けて学ぶのはガチなので、責任をとるという意味で公開します。たぶん学生さんの代わりに論文数十本分の輪講資料を作ったという意味では、おそらく有益なんじゃないかなと。いや、有益に違いありません。

- [第1回: ガイダンス・イントロダクション](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson1.html)
- [第2回: 人工ニューラルネットワークの学習](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson2.html)
- [第3回: 画像の識別と生成の基礎I](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson3.html)
- [第4回: 画像の識別と生成の基礎II](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson4.html)
- [第4.5回: 画像の識別と生成の基礎II（の補足）](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson4-2.html)
- [第5回: 埋め込みと文脈の付加](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson5.html)
- [第6回: Transformerの構造](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson6.html)
- [第7回: Transformerの応用](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson7.html)
- [第8回: 画像処理と言語処理の融合](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson8.html)
- [第9回: 画像と言語、ロボット制御の融合I](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson9.html)
- [第10回: 画像と言語、ロボット制御の融合II](https://ryuichiueda.github.io/slides_marp/advanced_vision/lesson10.html)

あと2回、次のようにテーマが残っていますが、とりあえず↑でVLAまで行きました。

- 第11回: NeRF
- 第12回: 3D Gaussian Splatting

