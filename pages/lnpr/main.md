---
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクス

<span style="color:red">発売中です。</span>

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4065170060/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51VhYaeelWL._SL160_.jpg" width="113" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4065170060/ryuichiueda-22">詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装 (KS理工学専門書)</a></dt>
          <dd>[上田 隆一]</dd>
          <dd>講談社 2019-10-28</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>

## リポジトリ一覧

* コード（書籍を読む時に使うもの）: https://github.com/ryuichiueda/LNPR_BOOK_CODES
* コード（完成品・改良版）: https://github.com/ryuichiueda/LNPR
* 講義用スライド: https://github.com/ryuichiueda/LNPR_SLIDES

## 訂正

* 第2刷以前

|場所|訂正前/後|発見者|一言  |
|:---|:-----|------|:-----|
|p.94 4.3節の5行目|次の4種類 $$\longrightarrow$$  次の5種類|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」$$\longrightarrow$$ 「次の5種類」<br>p. 99, 100：occulusion $$\longrightarrow$$ occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|修正漏れです|
|p.99 下から2,3行目、p.100のコードと1行目|occulusion $$\longrightarrow$$ occlusion |<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」→「次の5種類」<br>p. 99, 100：occulusion → occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|よくやるタイプミス&修正漏れですすみません・・・|


* 第1刷以前

|場所|訂正前/後|発見者|一言  |
|:---|:-----|------|:-----|
|p.75 ideal_robot7.ipynb [6]の6行目 | landmark_id = len(self.landmarks) + 1 → landmark_id = len(self.landmarks) | <blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>「確率ロボティクス」p. 76の図3.9との整合性を取るのであれば，p.75のIn[6]の6行目の最後の部分，”+1&quot;が不要のようです．ご確認ください．</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1188724503632736256?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |リポジトリのコードも直しておきました。|
|p.364 式(B.20)の右辺 | $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G - \Sigma_1^{-1})\boldsymbol{x}$$ $$\longrightarrow$$ $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G + \Sigma_1^{-1})\boldsymbol{x}$$|<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">唐突なリプすいません。自分も読んでいて、ひとつ気づいたので。。。<br>詳細確率ロボティクス p364 (B.20) Ψ^(-1)に相当する( )中の真ん中の符号、－ではなくて+ではないでしょうか？</p>&mdash; ma2 (@m_ma2) <a href="https://twitter.com/m_ma2/status/1189531321397202944?ref_src=twsrc%5Etfw">October 30, 2019</a></blockquote> |すみません・・・|



## 講義用スライド

* リポジトリ: https://github.com/ryuichiueda/LNPR_SLIDES


* [2. 確率統計の基礎](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap2_60min.html)
* [5. パーティクルフィルタを用いた自己位置推定](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap5_60min.html)
* [6. カルマンフィルタによる自己位置推定](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap6_60min.html)
* [7. 自己位置推定の諸問題](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap7_60min.html)
* [8. パーティクルフィルタを用いたSLAM](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap8_60min.html)
* [9. グラフ表現を用いたSLAM](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap9_60min.html)
* [10. マルコフ決定過程と動的計画法](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap10_60min.html)
* [11. 強化学習](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap11_60min.html)
* [12. 部分観測マルコフ決定過程](https://ryuichiueda.github.io/LNPR_SLIDES/slides/chap12_60min.html)
