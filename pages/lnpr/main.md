---
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクス

<span style="color:red">増刷決定</span>

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

<h2 id="typo">訂正</h2>

* 第2刷以前

|場所|訂正前/後|発見者|一言|
|:---|:-----|------|:-----|
|p.8 「冷戦期」の下の文|Roudolf$$\longrightarrow$$Rudolf||大変失礼いたしました。|
|p.8 下から10行目|ネリ・ゴードン（Neli ...$$\longrightarrow$$ニール・ゴードン（Neil ...||ずーっと間違えて覚えてました。名前間違えるのは最悪です。すんません・・・|
|p.19 本文9行目|こと分かります。$$\longrightarrow$$ことが分かります。|||
|p.56 数式も含めて10行目|足し合わせもの$$\longrightarrow$$足し合わせたもの|||
|p.121 5.3.4の表題の下の行|$$\delta_{\omega\omega} = 0.2\ \delta_{\nu\omega} = 0$$$$\longrightarrow$$$$\delta_{\omega\omega} = 0.2, \delta_{\nu\omega} = 0$$|||
|p.125 式も含めて下から10行目|は，はそれぞれ$$\longrightarrow$$はそれぞれ|||
|p.156 式も含めて6行目|N個ぶ$$\longrightarrow$$N個選ぶ|||
|p.239 6行目|graphbased_slam..._sensor2$$\longrightarrow$$graphbased_slam...sensor2.ipynb|||
|p.259 本文6行目|区関数$$\longrightarrow$$区間数|||
|p.285 下から3行目|ようにをつけて$$\longrightarrow$$ように値をつけて|||
|p.313 12.4.1の表題の2行上|この方法には$$\longrightarrow$$この方法は|||
|p.315 1行目|越えることに$$\longrightarrow$$越えるごとに|||
|p.327 下から4行目|作ること相当し$$\longrightarrow$$作ることに相当し|||
|p.345 中央|負担率（responsibilty）$$\longrightarrow$$負担率（responsibility）||iが足りないです。|
|p.375 本文下から2行目|リポリトリ$$\longrightarrow$$リポジトリ|||
|p.379 [Gordon 1993]|Neli$$\longrightarrow$$Neil||上に同じ。大変すみません。|
|p.380 [Igl 2018]|Leanring$$\longrightarrow$$Learning||勢いでタイプしてそのままになってました。|
|p.380 [Kalman 1960]|Roudolf$$\longrightarrow$$Rudolf||すみません！|
|p.382 [Sutton 1996]|Advannces$$\longrightarrow$$Advances||Macのキーボードが・・・|

* 第1刷以前

|場所|訂正前/後|発見者|一言  |
|:---|:-----|------|:-----|
|p.75 ideal_robot7.ipynb [6]の6行目 | landmark_id = len(self.landmarks) + 1 $$\longrightarrow$$ landmark_id = len(self.landmarks) | <blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>「確率ロボティクス」p. 76の図3.9との整合性を取るのであれば，p.75のIn[6]の6行目の最後の部分，”+1&quot;が不要のようです．ご確認ください．</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1188724503632736256?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |リポジトリのコードも直しておきました。|
|p.94 4.3節の5行目|次の4種類 $$\longrightarrow$$  次の5種類|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」$$\longrightarrow$$ 「次の5種類」<br>p. 99, 100：occulusion $$\longrightarrow$$ occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|修正漏れです|
|p.99 下から2,3行目、p.100のコードと1行目|occulusion $$\longrightarrow$$ occlusion |<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」→「次の5種類」<br>p. 99, 100：occulusion → occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|よくやるタイプミス&修正漏れですすみません・・・|
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
