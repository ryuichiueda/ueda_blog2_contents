---
Keywords: ROS,日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月20日） 

　[オープンキャンパス](https://www.it-chiba.ac.jp/admissions/event/oc/)の準備そっちのけ。（準備はできてるつもりだけど。）多動が出てソワソワしてずっと仕事A->仕事B->Twitter->仕事A->仕事C->Twitter->...みたいな状態だったが全体的にガーッと仕事が進んだ。体もソワソワしてたので抑制してたら脚が疲れた。

## シェルスクリプト高速開発手法入門の表紙 

　ウェブに掲載された。シェル芸をさらに極められるらしい。すげえ。

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51T-SfWPsPL._SL160_.jpg" width="124" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>KADOKAWA 2019-06-28 (Release 2019-06-28)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ギャグなのか本気なのか判断がつかない結構ヤバい本だ…<br><br>フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版 上田　隆一：生活・実用書 | KADOKAWA <a href="https://t.co/wga1uHpPrN">https://t.co/wga1uHpPrN</a> <a href="https://twitter.com/kadokawa_PR?ref_src=twsrc%5Etfw">@kadokawa_pr</a>より</p>&mdash; matsumuratomonori (@GTDOUCJKOI) <a href="https://twitter.com/GTDOUCJKOI/status/1141509556167532544?ref_src=twsrc%5Etfw">June 20, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


マジです！


## ラズパイマウスでCartographer

　昨日見つけた`slam_karto`は色々アレらしいので、[GoogleのCartographer](https://github.com/googlecartographer/cartographer)を試す。結果、ラズパイマウスで動いた。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">オドメトリとオープンキャンパスの準備がグダグダだけど、Cartographerはラズパイマウスで動いた。 <a href="https://t.co/yivWLC6inX">pic.twitter.com/yivWLC6inX</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1141628586056540160?ref_src=twsrc%5Etfw">2019年6月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


なんのドキュメントもないままGitHubに突っ込む。だいたい自分のリポジトリはこんなのばっかりなのでダメ。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ドキュメントないけどラズパイマウスでCartographer動かすやつ（超絶雑状態）<a href="https://t.co/5RfvNFOnFF">https://t.co/5RfvNFOnFF</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1141654834539446272?ref_src=twsrc%5Etfw">June 20, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


なお、[cartographerをcatrographerとミススペルした](https://github.com/ryuichiueda/raspimouse_cartographer/commit/5205c85f7721932ca837113574a1047866de7013)おかげで20分くらい無駄にした。
