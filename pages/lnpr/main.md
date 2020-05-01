---
Keywords: 詳解確率ロボティクス
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクス

<span style="color:red">増版（第3刷）決定！</span>


## 講義用スライド・動画

### スライド

現在、コロナ対策のオンライン講義のために各章を解説した動画を作成中です。それにともない、スライドの内容も新しくしています。

* リポジトリ: https://github.com/ryuichiueda/LNPR_SLIDES
    * [第一章](https://ryuichiueda.github.io/LNPR_SLIDES/chap1.html)

### ビデオ

* 1章

<iframe width="560" height="315" src="https://www.youtube.com/embed/tlbeAu8yHEc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* 2章前半

<iframe width="560" height="315" src="https://www.youtube.com/embed/5VRwvnrGJ60" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* 2章後半その1

<iframe width="560" height="315" src="https://www.youtube.com/embed/BCNuZk4-jxM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* 4章

<iframe width="560" height="315" src="https://www.youtube.com/embed/YiyttOnTuBQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## リポジトリ一覧

* コード（書籍を読む時に使うもの）: https://github.com/ryuichiueda/LNPR_BOOK_CODES
* コード（完成品・改良版）: https://github.com/ryuichiueda/LNPR
* 講義用スライド: https://github.com/ryuichiueda/LNPR_SLIDES

## 訂正


|場所|訂正前/後|発見者|一言|
|:---|:-----|------|:-----|
|p.80 `ideal_robot10.ipynb [7]` 21行目| `z = self.relative_polar_pos(...` $$\longrightarrow$$ `z = self.observation_function(...`|[@maskot1977](https://twitter.com/maskot1977)さん|コードの差し替えミスでした。|
|p.191 式(8.33)の最後の行列|右上の要素の$$\ell^2$$と右下の要素の$$\ell$$を入れ替え（添字は省略）|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">詳解確率ロボティクスp.191 式(8.33)，2段目から3段目への変形で1行2列目の要素と2行1列目の要素の分母が置き換わるところで次数が変わってるのはなんでなんだろう...<br>1行目の要素の分母の次数は1乗で2行目は2乗になるんじゃないのかな</p>&mdash; Kohta (@fjnkt98) <a href="https://twitter.com/fjnkt98/status/1255825300656582656?ref_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|コピペミスです・・・。|


### 第3刷で訂正済み

|場所|訂正前/後|発見者|一言|
|:---|:-----|------|:-----|
|p.16 本文下から2行目|とうてい受け入れにくい$$\longrightarrow$$とうてい受け入れがたい|上田|「難い」をひらがなに直すときに手違いがありました。|
|p.8 「冷戦期」の下の文|Roudolf$$\longrightarrow$$Rudolf||大変失礼いたしました。|
|p.8 下から10行目|ネリ・ゴードン（Neli ...$$\longrightarrow$$ニール・ゴードン（Neil ...||ずーっと間違えて覚えてました。名前間違えるのは最悪です。すんません・・・|
|p.19 本文9行目|こと分かります。$$\longrightarrow$$ことが分かります。|||
|p.56 数式も含めて10行目|足し合わせもの$$\longrightarrow$$足し合わせたもの|||
|p.121 5.3.4の表題の下の行|$$\delta_{\omega\omega} = 0.2\ \delta_{\nu\omega} = 0$$$$\longrightarrow$$$$\delta_{\omega\omega} = 0.2, \delta_{\nu\omega} = 0$$|||
|p.125 式も含めて下から10行目|は，はそれぞれ$$\longrightarrow$$はそれぞれ|||
|p.147 式(6.26)| $$\hat{\mu}_x - m_y$$ $$\longrightarrow$$ $$\hat{\mu}_y - m_y$$|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> <br>突然のリプライで申し訳ありません。確率ロボティクスの本のP147式6.26ですがy側の信念分布の中心点の係数がxになっている理由を教えていただけないでしょうか。<br>距離計測なのでy成分だと思っていました。</p>&mdash; Acky_F (@AckyF1) <a href="https://twitter.com/AckyF1/status/1216181205361520640?ref_src=twsrc%5Etfw">January 12, 2020</a></blockquote>|校正から漏れました|
|p.156 式も含めて6行目|N個ぶ$$\longrightarrow$$N個選ぶ|||
|p.239 6行目|graphbased_slam..._sensor2$$\longrightarrow$$graphbased_slam...sensor2.ipynb|||
|p.259 本文6行目|区関数$$\longrightarrow$$区間数|||
|p.285 下から3行目|ようにをつけて$$\longrightarrow$$ように値をつけて|||
|p.313 12.4.1の表題の2行上|この方法には$$\longrightarrow$$この方法は|||
|p.315 1行目|越えることに$$\longrightarrow$$越えるごとに|||
|p.327 下から4行目|作ること相当し$$\longrightarrow$$作ることに相当し|||
|p.345 中央|負担率（responsibilty）$$\longrightarrow$$負担率（responsibility）||愛が足りない。|
|p.375 本文下から2行目|リポリトリ$$\longrightarrow$$リポジトリ|||
|p.379 [Gordon 1993]|Neli$$\longrightarrow$$Neil||上に同じ。大変すみません。|
|p.380 [Igl 2018]|Leanring$$\longrightarrow$$Learning||勢いでタイプしてそのままになってました。|
|p.380 [Kalman 1960]|Roudolf$$\longrightarrow$$Rudolf||すみません！|
|p.382 [Sutton 1996]|Advannces$$\longrightarrow$$Advances||Macのキーボードが・・・|

### 第2刷で訂正済み

|場所|訂正前/後|発見者|一言  |
|:---|:-----|------|:-----|
|p.75 ideal_robot7.ipynb [6]の6行目 | landmark_id = len(self.landmarks) + 1 $$\longrightarrow$$ landmark_id = len(self.landmarks) | <blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>「確率ロボティクス」p. 76の図3.9との整合性を取るのであれば，p.75のIn[6]の6行目の最後の部分，”+1&quot;が不要のようです．ご確認ください．</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1188724503632736256?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |リポジトリのコードも直しておきました。|
|p.94 4.3節の5行目|次の4種類 $$\longrightarrow$$  次の5種類|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」$$\longrightarrow$$ 「次の5種類」<br>p. 99, 100：occulusion $$\longrightarrow$$ occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|修正漏れです|
|p.99 下から2,3行目、p.100のコードと1行目|occulusion $$\longrightarrow$$ occlusion |<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」→「次の5種類」<br>p. 99, 100：occulusion → occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|よくやるタイプミス&修正漏れですすみません・・・|
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |
|p.364 式(B.20)の右辺 | $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G - \Sigma_1^{-1})\boldsymbol{x}$$ $$\longrightarrow$$ $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G + \Sigma_1^{-1})\boldsymbol{x}$$|<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">唐突なリプすいません。自分も読んでいて、ひとつ気づいたので。。。<br>詳細確率ロボティクス p364 (B.20) Ψ^(-1)に相当する( )中の真ん中の符号、－ではなくて+ではないでしょうか？</p>&mdash; ma2 (@m_ma2) <a href="https://twitter.com/m_ma2/status/1189531321397202944?ref_src=twsrc%5Etfw">October 30, 2019</a></blockquote> |すみません・・・| 



## 電子書籍

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4065170060/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51YzQqKHi8L._SL160_.jpg" width="114" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4065170060/ryuichiueda-22">詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装 (KS理工学専門書)</a></dt>
          <dd>[上田 隆一]</dd>
          <dd>講談社 2019-10-27</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装 KS理工学専門書 (上田隆一) の、紀伊國屋電子書籍版が予約開始されました。金曜配信。<a href="https://t.co/oXnAXP9VzV">https://t.co/oXnAXP9VzV</a></p>&mdash; 紀伊國屋電子書籍Kinoppy新刊情報 (@kinokuniyanew) <a href="https://twitter.com/kinokuniyanew/status/1206814690237546496?ref_src=twsrc%5Etfw">December 17, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
