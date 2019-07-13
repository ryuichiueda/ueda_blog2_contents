---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月13日）

## bashcms本に書評をいただく

* https://www.artonx.org/diary/20190713.html#p01

ほんと、読んで文章を書くというのは時間のかかることですので、大変有難いです。書いていただいた通り、おすすめです。

　売らねばならないので宣伝貼り付けます。

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/B07TSZZPWN/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51H%2B4kUhbFL._SL160_.jpg" width="121" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/B07TSZZPWN/ryuichiueda-22">フルスクラッチから1日でCMSを作る_シェルスクリプト高速開発手法入門 改訂2版 (アスキードワンゴ)</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>ドワンゴ 2019-07-05 (Release 2019-07-05)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>


## シェル芸bot強化週間

　なんかシェル芸botに乱暴に難癖をつけてきた人がいたので、割とどうでもいいその人そっちのけでシェル芸botの点検（というかゆさぶりというか危険シェル芸大会というか）が始まった。で、↓がクリーンヒットしてシェル芸botが死んだ。さすが。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">seq 100 | xargs -I@ -P0 dd if=/dev/zero of=/images/@ <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1149876657672597505?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

その時寿司屋（と言ってもまわるやつ）にいたので、その場でPCを広げてフッキュー。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">まさか寿司屋でやるとは・・・ <a href="https://t.co/5GB8Bsp7iW">pic.twitter.com/5GB8Bsp7iW</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1149878405199826950?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">あかん <a href="https://t.co/LKzJsIr273">pic.twitter.com/LKzJsIr273</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1149879162762489856?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">サーバ、再起動しました。コンテナたちあげおながいします！ &gt; <a href="https://twitter.com/theoldmoon0602?ref_src=twsrc%5Etfw">@theoldmoon0602</a> <br><br>はやくすしくいたい！！</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1149879519358025728?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">とりあえず容量的にはだいじょうぶなので、ディレクトリをいじらないで寿司食べます。慌てると事故る。 &gt; <a href="https://twitter.com/theoldmoon0602?ref_src=twsrc%5Etfw">@theoldmoon0602</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1149879778247188480?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


で、解決！クリックすると解説が読めます。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">えー、それではめでたくもシェル芸botが復活しましたので、今回の問題について解説していきます</p>&mdash; gǔ yuè (@theoldmoon0602) <a href="https://twitter.com/theoldmoon0602/status/1149916541942554624?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


で、安心してたら本日2発目がクリーンヒット。やった！（やったじゃない。いや大事。）

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/theoldmoon0602?ref_src=twsrc%5Etfw">@theoldmoon0602</a> <br>突然失礼します。現在シェル芸botが反応しません。<br>そうでないことを願いますが、私のツイートが原因でしょうか？<br>もしそうだとしたら大変申し訳ありません。 <a href="https://t.co/Wl1vK78dhB">https://t.co/Wl1vK78dhB</a></p>&mdash; くおん (@qwertanus) <a href="https://twitter.com/qwertanus/status/1149946761772879872?ref_src=twsrc%5Etfw">2019年7月13日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


解説を入れたらもうちょい有用な記事になるんですが、これはまた別のときにまとめるか、他の方に託したいと思います。


　そして~~攻撃~~検証はまだまだ続いている模様。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">画像ファイルをvimで開いて、末尾に怪しいコードを付けてシェル芸botにPOSTしようと思ったのだが、まずTwitterに怒られた(笑)</p>&mdash; Y.Toriyama (@YToriyama) <a href="https://twitter.com/YToriyama/status/1150053308419043328?ref_src=twsrc%5Etfw">July 13, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

最初に難癖をつけてきた人が蚊帳の外であることは言うまでもなし。

## 確率ロボティクス本の初校が始まった

　少し物怖じしてから意を決して開始。本日は上の件があったので数ページだけだったけど、開始することが大切。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">確率ロボティクス本の校正が始まります。見たこともない巨大なバインダクリップにはさまれてます。バインダクリップ、巨大ですがもっと問題なのは、これが1/4の量ということ・・・ <a href="https://twitter.com/hashtag/%E6%AD%BB?src=hash&amp;ref_src=twsrc%5Etfw">#死</a> <a href="https://t.co/C0SgokQKBQ">pic.twitter.com/C0SgokQKBQ</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1149923720867139585?ref_src=twsrc%5Etfw">July 13, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


寝ます。お疲れ様でした。
