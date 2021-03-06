---
Keywords: 詳解確率ロボティクス
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクス

<span style="color:red">増版（第4刷）決定！</span>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">【重版速報】<br>おかげさまで、重版が決まりました。ありがとうございます！<br><br>上田隆一・著『詳解　確率ロボティクス』【4刷】<a href="https://t.co/ZlzkrQbWyw">https://t.co/ZlzkrQbWyw</a><br><br>著者による解説動画もあります。<a href="https://t.co/sJI7Jr1pXC">https://t.co/sJI7Jr1pXC</a> <a href="https://t.co/pAFxVdhQrQ">pic.twitter.com/pAFxVdhQrQ</a></p>&mdash; 講談社サイエンティフィク (@kspub_kodansha) <a href="https://twitter.com/kspub_kodansha/status/1267275779097808900?ref_src=twsrc%5Etfw">June 1, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



## 講義用スライド・動画

### スライド

現在、コロナ対策のオンライン講義のために各章を解説した動画を作成中です。それにともない、スライドの内容も新しくしています。

* リポジトリ: https://github.com/ryuichiueda/LNPR_SLIDES
    * [第一章](https://ryuichiueda.github.io/LNPR_SLIDES/chap1.html)

### ビデオ

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLbUh9y6MXvjfOLwmuuBbXKUX45rZsM8iH" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## リポジトリ一覧

* コード（書籍を読む時に使うもの）: https://github.com/ryuichiueda/LNPR_BOOK_CODES
* コード（完成品・改良版）: https://github.com/ryuichiueda/LNPR
* 講義用スライド: https://github.com/ryuichiueda/LNPR_SLIDES

## 訂正

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.20 下から2行目|頻度が大きい \\( \Longrightarrow \\) 頻度が高い  | 上田 | 頻度は「高い」「低い」です。 |
|p.91 1、3行目|角度、角速度\\( \Longrightarrow \\)速度、角速度|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> p.91の1行目、3行目の「角度、角速度」は「速度、角速度」ですかね。<a href="https://twitter.com/hashtag/%E8%A9%B3%E8%A7%A3%E7%A2%BA%E7%8E%87%E3%83%AD%E3%83%9C%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9?src=hash&amp;ref_src=twsrc%5Etfw">#詳解確率ロボティクス</a></p>&mdash; Usk Tamura (@slx01) <a href="https://twitter.com/slx01/status/1300707440611139584?ref_src=twsrc%5Etfw">September 1, 2020</a></blockquote>|1箇所ならともかくコピペで2箇所間違えました。|
|p.96 `noise_simulation7.ipynb [3]` 19行目、p.97 `noise_simulation8.ipynb [3]` 26行目、p.98 `noise_simulation9.ipynb [3]` 31、38行目、p.99 `noise_simulation10.ipynb [3]` 47行目、p.127 `mcl11.ipynb [2]` 19行目| `relative_polar_pos` $$\longrightarrow$$ `observation_function`|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">p.96: noise_simulation7.ipynb [3] 19行目、p.97: noise_simulation8.ipynb [3] 26行目、p.98: noise_simulation9.ipynb [3] 31行目, 38行目、p.99: noise_simulation10.ipynb [3] 47行目、p.100: noise_simulation11.ipynb [3] 55行目。</p>&mdash; Usk Tamura (@slx01) <a href="https://twitter.com/slx01/status/1300956652661665792?ref_src=twsrc%5Etfw">September 2, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|コードの差し替えミスでした。|
|p.173 式(7.33)、式(7.35)|\\( (1-\tilde{N})/N \\) \Longrightarrow  \\( (N-\tilde{N})/N \\)|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解確率ロボティクスのp173のP(Υ=1)とP(Υ=0)の和が1にならないのはなんでや…<br>誰か有能な方教えてください</p>&mdash; M (@p_x9) <a href="https://twitter.com/p_x9/status/1303375562061176833?ref_src=twsrc%5Etfw">September 8, 2020</a></blockquote>|算数は苦手です。|

### 第4刷で訂正済み

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.56 式(2.94)|積分は不要|上田|\\( \boldsymbol{x}\\)で積分したら\\(p_3\\)が\\( \boldsymbol{x} \\)の関数にならないじゃないか・・・|
|p.62|section_sentor \\( \Longrightarrow \\) section_sensor|<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">たびたびすみません。P62の3.2.1に「コーディングは、section_sentorのとなり」と記載されていますが、section_sensorの誤記でしょうか？<br>（粗探しや間違い探しなどしてません！偶然見つかりました😭）</p>&mdash; と雷 (@chmod_x_akasit) <a href="https://twitter.com/chmod_x_akasit/status/1272394146536321024?ref_src=twsrc%5Etfw">June 15, 2020</a></blockquote>|sentorとは。|
|p.80 `ideal_robot10.ipynb [7]` 21行目| `relative_polar_pos` $$\longrightarrow$$ `observation_function`|[@maskot1977](https://twitter.com/maskot1977)さん|コードの差し替えミスでした。|
|p.186 ページ上にある式番号を振っていない3行の式|1行目から2行目のイコールまでが不要。2行目の「右の分布から不要な・・・」という補足も不要。つまり、2行目と3行目をイコールでつないだ式が書いてあれば十分。|上田|式(8.10)と比べると余計な記述をしていると思いました。|
|p.191 式(8.33)の最後の行列|右上の要素の\\( \ell^2\_{\hat{\boldsymbol{m}}\_{t-1}} \\)と左下の要素の\\( \ell\_{\hat{\boldsymbol{m}}\_{t-1}} \\)を入れ替え|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">詳解確率ロボティクスp.191 式(8.33)，2段目から3段目への変形で1行2列目の要素と2行1列目の要素の分母が置き換わるところで次数が変わってるのはなんでなんだろう...<br>1行目の要素の分母の次数は1乗で2行目は2乗になるんじゃないのかな</p>&mdash; Kohta (@fjnkt98) <a href="https://twitter.com/fjnkt98/status/1255825300656582656?ref\_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|コピペミスです・・・。|
|p.196 式(8.54)|\\( \lt N(m) \gt_m \\) \\( \Longrightarrow \\) \\( [[ N(m) ]]_m \\)|上田|凡ミスです。|
|p.233 式(9.65)|\\( \Omega_{j,t} = R_{j,t}Q_{j,t}R_{j,t}^\top \\) \\( \Longrightarrow \\) \\( \Omega_{j,t} = (R_{j,t}Q_{j,t}R_{j,t}^\top)^{-1} \\)|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|気を抜いておりました・・・|
|p.233 式(9.65)の下の行|写像した共分散行列です。\\( \Longrightarrow \\)写像して得られる精度行列です。|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.233 セルの24行目、p.237 セルの16行目|右辺の行列を`np.linalg.inv(` `R.dot(Q1).dot(R.T))`と逆行列に訂正|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.234 図9.12(c)|[この図に差し替え](https://b.ueda.tech/pages/lnpr/9.12c.png)|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.234 最終行|方向に星印が移動\\( \Longrightarrow \\)方向に、わずかに星印が移動|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.364 脚注2|共分散行列 \\( \Longrightarrow \\) 半正定値対称行列|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>  唐突なツイート失礼します詳解確率ロボティクスの内容について質問です。<br>P364の注2に「B.1.5項の結果から共分散行列と解釈できます」と記載されてますが、半正定値対称行列ではないでしょうか？<br>そうなるとΨが対称行列になるので納得します。</p>&mdash; と雷 (@chmod_x_akasit) <a href="https://twitter.com/chmod_x_akasit/status/1272103493101223936?ref_src=twsrc%5Etfw">June 14, 2020</a></blockquote>|もう少し補足すると共分散行列ではなくて精度行列です。|


### 第3刷で訂正済み

|場所|訂正事項|発見者|一言|
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

|場所|訂正事項|発見者|一言  |
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
