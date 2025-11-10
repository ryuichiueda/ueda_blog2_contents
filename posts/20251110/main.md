---
Keywords: 研究, LLM, VLM, VLA, Transformer
Copyright: (C) 2025 Ryuichi Ueda
---

# 近況（2025年11月10日）

　半年ぶりの更新です。ずっとブログやシェル芸勉強会、連載の部分以外の自作シェルの開発をさぼって半年間、ニューラルネット〜VLA（画像とか言葉の指示とかでロボットを動かすやつ）の勉強をしていました。特にシェル芸界隈のみなさますみません。

## きっかけ

　5月頭に急に後期の大学院の画像処理の講義を担当することになって、[Transformer](https://ja.wikipedia.org/wiki/Transformer_(%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%83%A2%E3%83%87%E3%83%AB))の使用を前提に講義を組み直すことにしました。
「**言葉を駆使する人間はめんどくさくて邪悪**」という考えを拗らせているため言語関係は全然興味がなかったのですが、
学生さんが[Segment Anything Model（SAM）](https://segment-anything.com/)を使って研究するのを見ていて、「言語を絡めたほうが画像処理は柔軟になる」という今思うと当たり前なことに気づいて、ちょっと興味が出てきたころでした。単なる道具じゃなくて、中身も知っておこうと。


　4月末でブログの更新が止まっているのは、そこから勉強を最優先にしたからです。5月以降、実家に1回行った以外は関東から出ずに引きこもっていました。

## 問題

　他にいろいろ研究・執筆ネタがあったので、個人的にはニューラルネットワークに全く手を出してこなかったというクリティカルな問題がありました。研究室からはそれ関係の論文が出てて賞ももらってたりしますが、学生さんの主体的な努力と、そこそこ年季の入った教員として、知らない分野を扱うときの指導のコツを駆使しただけで、私個人は素人です。

## 対応

　とりあえず研究室に配属された4年生に戻り、忙しいというオッサン（自分）の声は全て遮断して文献を読み漁りました。必読の[ゼロから作るDeep Learning](https://demuc.de/papers/schoenberger2016sfm.pdf)から初めて、学生のときに雑に勉強していたのを真面目に学び直し、あとはTransformerの解説書を何冊か読みました。んで、その後、主要な論文を読み始め、分からんことがあると教科書に戻ったり、引用されている論文を読んでいきました。最終的に[π0というVLAの論文](https://arxiv.org/abs/2410.24164)を読んで、だいたいなにやってるか分かるかなあ・・・というところまできました。

　改めて近年の人工ニューラルネットワークを勉強した感想ですが、確率論や、従来の機械学習の手法が取り入れたれていたり、モデルが古典的な画像処理方法を獲得していたり、思ったより合理的な世界なんだなあと思いました。論文中に確率の式が出てきて「あーあーあーそうね」という箇所が多くて、なんか首の皮一枚つながった感があります。

　特に、オートエンコーダーのところは、自分がニューラルネットなしで博士論文でやってたこと（方策の圧縮）と関係するので、試したことないけどなんか共感しました。オートエンコーダーの論文が出たのは自分が博士論文を書いていた頃の2006年なので、食わず嫌いではないです念のため。

## 錬成された講義資料

　元々素人が作ったものなんですが、学生さんはこれ見て私の説明受けて学ぶのはガチなので、責任をとるという意味で公開します。たぶん学生さんの代わりに論文数十本分の輪講資料を作ったという意味では、おそらく有益なんじゃないかなと。いや、有益に違いありません。もちろん間違いがある可能性もあるので、学生さんのために優しくご指摘ください。講義動画はYouTubeにアップしません絶対に。

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

## 感想


　研究室配属された新人に戻ったのは、千葉工大赴任直後にROSの威力を見せつけられた2015年に続き2度目でした。特に自分のいる分野は進みが早いので、今後も何回か繰り返すんでしょうか。ていうか日頃から論文をちゃんと読んでればそんな必要はないはずなので、普段から勉強されてる先生たちには頭があがりません。


現場からは以上です。
