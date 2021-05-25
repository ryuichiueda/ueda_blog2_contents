---
Keywords: 詳解確率ロボティクス
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクスの関連コンテンツ

## 解説動画

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLbUh9y6MXvjfOLwmuuBbXKUX45rZsM8iH" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## リポジトリ一覧

* コード（書籍を読む時に使うもの）: https://github.com/ryuichiueda/LNPR_BOOK_CODES
* コード（完成品・改良版）: https://github.com/ryuichiueda/LNPR
* 講義用スライド: https://github.com/ryuichiueda/LNPR_SLIDES

## 書籍の内容と関係のあるROSリポジトリ

### [ryuichiueda/amcl](https://github.com/ryuichiueda/emcl)


* amclの代替の自己位置推定パッケージ
    * 5章のパーティクルフィルタ、7章の膨張リセットの実装です。
    * emclの代替パッケージです。
    * ↓デモ動画

<iframe width="560" height="315" src="https://www.youtube.com/embed/X4zXKi0mr0I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### [ryuichiueda/value_iteration](https://github.com/ryuichiueda/value_iteration)

* 価値反復パッケージ
    * 10章の価値反復のパッケージです。書籍ではオフライン手法と紹介しましたが、小さな環境ではオンラインで利用できます。move_baseのグローバルプランナーの代わりに使えますが、nove_baseと互換性はありません。また、2021年5月23日現在、ローカルプランナーを実装していません。
    * 下の動画: 動作している様子。計算した状態価値関数がグレーで表示されています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/AsjQZ3WDI-Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
