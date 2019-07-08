---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月8日）

　今日は朝にシェル芸人からの挑戦状の原稿を提出後、一日中コードを書いていた。ただ、下のデモムービーを撮影するときにうまくSLAMができなくて何時間か中断してしまった。原因はUbuntuのネットワーク設定をnetplanで管理するようになってから、WiFiのpower managementを切るのを忘れていた（切らないとブチブチ通信が途切れる）ためで、これはこれで某本の読者に告知しなければならない・・・。

## ROSのdockerイメージ作った

　テストに使うかなーと思って作った。まだ使ってない。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">そういえば朝にUbuntu 18.04 server + ROSのdockerイメージ作ったんだけど、使う前に別のことやりだしたので作って放置になってた。<a href="https://t.co/9Vy4UOxqTX">https://t.co/9Vy4UOxqTX</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1148237287135670272?ref_src=twsrc%5Etfw">2019年7月8日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">Dockerfileはこれ。<a href="https://t.co/qsaBm78Kfu">https://t.co/qsaBm78Kfu</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1148237518418006017?ref_src=twsrc%5Etfw">July 8, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

作ったけどライセンスとかREADMEとか全然作ってない。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">作ったまま感がひどい。</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1148237581110280192?ref_src=twsrc%5Etfw">July 8, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

反省。


## Cartographerを使ったteach-and-replay

　SLAMの文脈だとSLAM and waypoint navigationという感じのデモ。[このリポジトリ](https://github.com/ryuichiueda/raspimouse_map_based_teach_and_replay)を使用。人がロボットを操縦して、そのあと、ロボットが人の操縦した経路と同じ経路で移動するというもの。

　デモムービーは速度を変えて次のもの2つをYouTubeにアップ。上のが1倍速、下のが5倍速。

<iframe width="560" height="315" src="https://www.youtube.com/embed/fk8Y7kWahSQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/SirW2nRSL8U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

　しかし、このリポジトリもREADMEが古い。アカン。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">作ったまま感がひどい。</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1148237581110280192?ref_src=twsrc%5Etfw">July 8, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　アカン。

## 確率ロボティクス本近況

　ゲラがそろそろ送られてくるっぽい。

## 宣伝

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ガチでやべー本出版されてた<br><br>フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版 <a href="https://t.co/R3wgOMEV5n">https://t.co/R3wgOMEV5n</a></p>&mdash; 有に見せかけた無の代名詞 (@AtPOP) <a href="https://twitter.com/AtPOP/status/1148096401038950401?ref_src=twsrc%5Etfw">July 8, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

やばいです。やばさには自信があります。


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


GitHubのあらゆるものが中途半端な件、大反省の末寝る。
