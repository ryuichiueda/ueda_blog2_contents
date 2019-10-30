---
Keywords: 報告,詳解確率ロボティクス
Copyright: (C) 2019 Ryuichi Ueda
---

# 詳解確率ロボティクスのファーストインプレッション集

　昨日はネタに走ってしまいましたが、今日は詳解確率ロボティクスを早速入手された方のツイートを貼り付けさせていただきます。宣伝に使ってしまってすみません。


## コードについて

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">自分用と会社用に買いました。ソースコードがついて、とてもわかりやすくなったProbabilistic Robotics。自己位置推定と行動決定はこの本でカバーできそうです。<br>あとは、perceptionの領域で同じレベルの本があればいいのに。Tracking とか Fusionとか。<br>詳解確率ロボティクス<a href="https://t.co/gz2orSjUr6">https://t.co/gz2orSjUr6</a></p>&mdash; tekeom (@tekeom) <a href="https://twitter.com/tekeom/status/1188633011840937984?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解 確率ロボティクス届いた〜<br>パラパラ中身見たけど、これはだいぶ実装フレンドリーな感じ、良いぞ〜 <a href="https://t.co/RwfoUzoECC">pic.twitter.com/RwfoUzoECC</a></p>&mdash; あき (@cumulo_autumn) <a href="https://twitter.com/cumulo_autumn/status/1188718930002448384?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">こんだけコードも乗ってて、解説もわかりやすそう。これで４０００円代は神。<br>今日から読む！！<br>&gt; 詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装 (KS理工学専門書)  <a href="https://t.co/NLnhJrPpVm">https://t.co/NLnhJrPpVm</a></p>&mdash; Masa (@asas_mimi) <a href="https://twitter.com/asas_mimi/status/1188385909755899904?ref_src=twsrc%5Etfw">October 27, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解確率ロボティクス届いた。こういう系でよくある数式と理論だけじゃなくて、jupyterNotebookでガリガリコードも載ってる。SLAM、マルコフ、強化学習、ベイズでセンサーデータまであって至れり尽くせりやんけ🥰</p>&mdash; kevin28gou (@kevin28gou) <a href="https://twitter.com/kevin28gou/status/1188331092606013441?ref_src=twsrc%5Etfw">October 27, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">理論メインのSLAM本が多い中、実装をきちんと見せてくれて、しかもpythonで気軽に試せる。SLAM初心者はこの本から入るのが良さそう。 <a href="https://t.co/EU4ekp5dU3">pic.twitter.com/EU4ekp5dU3</a></p>&mdash; Miyatti (@y4tk38) <a href="https://twitter.com/y4tk38/status/1188451272359211009?ref_src=twsrc%5Etfw">October 27, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">自律移動技術の聖書『Probabilistic Robotics』の翻訳で有名な<a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 先生の『詳解確率ロボティクス』を献本して頂きました😃。じっくり読んで書評させて頂きます♪ 全体を眺めただけですが、全編カラーでコードや数式も多く、長く楽しめそうです。何より後書きに自分の名前があって感動でした😭 <a href="https://t.co/lXMGWKSNhI">pic.twitter.com/lXMGWKSNhI</a></p>&mdash; Atsushi Sakai (@Atsushi_twi) <a href="https://twitter.com/Atsushi_twi/status/1187333365986250752?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　やっぱりコードがついているのが好評のようです。コードはここにあります。

* 書籍のリファレンス用のコード: https://github.com/ryuichiueda/LNPR_BOOK_CODES
* 完成したコード: https://github.com/ryuichiueda/LNPR

## 1章について


　それからインサイダーからこのようなお言葉をいただきました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">私がM1のときの確率ロボティクスの1回目の講義で上田先生が移動ロボットのナビゲーションの話をするにあたって、大航海時代の航海術の話をされてたのが個人的にかなりツボだったんですが、「詳解確率ロボティクス」でも第一章でそこが丁寧に語られてるのがかなりツボですね。</p>&mdash; なすぷる (@Nasupl_r) <a href="https://twitter.com/Nasupl_r/status/1188811080924950528?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　また、1章にはこんなことも書いてしまいました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">第1章からヤバいｗ<br><br>===============<br>筆者は学生のとき、確率に対する実感を養うために（実際は家賃込みの月6万円の仕送りを増やすために）、学生寮、後楽園、高田馬場あたりの「現場」でかなりの訓練をして仕送りを減らしていましたが、そちらをおすすめするわけにはいきません。 <a href="https://t.co/KbY7ZGXMZu">https://t.co/KbY7ZGXMZu</a></p>&mdash; Miyatti (@y4tk38) <a href="https://twitter.com/y4tk38/status/1188682410537340928?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ワロタ<br><br>&gt; 確率に対する実感を養うために（実際は家賃込みの月6万円の仕送りを増やすために）、学生寮、後楽園、高田馬場あたりの「現場」でかなりの訓練をして仕送りを減らしていましたが<a href="https://t.co/7cWF9HSgZx">https://t.co/7cWF9HSgZx</a></p>&mdash; ふぁむたろう (@fam_taro) <a href="https://twitter.com/fam_taro/status/1188679140871815168?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解 確率ロボティクスの一章の抜粋がすでに面白い <a href="https://t.co/cWH2HSACq2">pic.twitter.com/cWH2HSACq2</a></p>&mdash; いーもり (@Oswaldmori1977) <a href="https://twitter.com/Oswaldmori1977/status/1187760290068217856?ref_src=twsrc%5Etfw">October 25, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


これ（駒場時代の荒れた生活）については何か機会があったら書き残しておきたいです。

## 魂

入ってます。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ご恵贈有難うございます。<br>パラパラ見たけど、この本は魂入ってるぞ！ <a href="https://t.co/8pn8EkJbQv">pic.twitter.com/8pn8EkJbQv</a></p>&mdash; Shuuji Kajita (@s_kajita) <a href="https://twitter.com/s_kajita/status/1187580441764564992?ref_src=twsrc%5Etfw">October 25, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## その他

　他、「点群とかICPとかNDTとか扱ってないんだよなー」というツイートもありましたが、その通りです。（ちょーっとネガティブな方とお見受けしたのでツイートは貼りません。）本の中にもその旨書きました。ぜひ経験の深い方に本書のスタイルで書いていただけたらと・・・。


感想を寄せていただいたみなさま、ありがとうございました。

