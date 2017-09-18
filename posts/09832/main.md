---
Keywords:ラズパイマウス,Linux,Raspberry,ROS
Copyright: (C) 2017 Ryuichi Ueda
---

# 最近のラズパイマウスまわりの情報
最近、ラズパイマウス本の宣伝をしてませんが、ラズパイマウスの開発やラズパイマウス上で動くソフトウェアはどんどん増えてますので、情報を並べておきます。<br />
<ul><br />
 	<li><a href="#gamepad">ゲームパッドとラズパイマウスをつなぐROSパッケージ</a></li><br />
 	<li><a href="#hector">Hector SLAM + ナビゲーションのパッケージ</a></li><br />
 	<li><a href="#event">イベント等</a></li><br />
 	<li><a href="#hardware">オプション（ハードウェア）</a></li><br />
 	<li><a href="#maze">迷路走行用ROSパッケージ</a></li><br />
 	<li><a href="#learning">学習モジュール</a></li><br />
 	<li><a href="#simulator">シミュレータ</a></li><br />
</ul><br />
[amazonjs asin="4822239292" locale="JP" title="Raspberry Piで学ぶ ROSロボット入門"]<br />
<br />
本の情報はGitHubに掲載しています。<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">最近質問の書き込みが少ないです・・・<a href="https://t.co/T8u8Wjsi9v">https://t.co/T8u8Wjsi9v</a></p><br />
— Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/878950427932237826">2017年6月25日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
質問お待ちしております！！<br />
<h2 id="gamepad">ゲームパッドとラズパイマウスをつなぐROSパッケージ</h2><br />
弊研究室の岡崎氏が管理しています。<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">先週公開されたRaspberry Pi Mouse + ROS用ゲームコントローラ接続パッケージですが、研究室内でソーシャルドキュメンテーション中です。増える英語、飛び交うプルリク。<a href="https://t.co/RAjx1mvvkI">https://t.co/RAjx1mvvkI</a></p><br />
— CIT未ロボ上田研 (\@uedalaboratory) <a href="https://twitter.com/uedalaboratory/status/871707077856567296">2017年6月5日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<h2 id="hector">Hector SLAM + ナビゲーションのパッケージ</h2><br />
同じく岡崎氏作のHector SLAMしながらナビゲーションするパッケージ。千葉工大のOBの前川氏のパッケージからあまりいじっていないそうです。<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">仕事が早いっすね。| ROSを使ったRaspberry Pi Mouseのナビゲーション <a href="https://t.co/616wWmWkOy">https://t.co/616wWmWkOy</a> <a href="https://twitter.com/hashtag/citarlab?src=hash">#citarlab</a> <a href="https://twitter.com/uedalaboratory">\@uedalaboratory</a>さんから</p><br />
— CIT未ロボ上田研 (\@uedalaboratory) <a href="https://twitter.com/uedalaboratory/status/874259302168412160">2017年6月12日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
岡崎さんは現在、移動ロボットでは標準的な構成となるgmappingとナビゲーションメタパッケージをラズパイマウスに移植中です。<br />
<h2 id="event">イベント等</h2><br />
終わったものや募集が定員に達したものばかり挙げますが・・・。これからもあるかもしれません。ありがとうございます。<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">ROS Japan UG #12 Raspberry Pi Mouseハッカソン を公開しました！ <a href="https://t.co/9h126BZLiD">https://t.co/9h126BZLiD</a> <a href="https://twitter.com/hashtag/rosjp?src=hash">#rosjp</a></p><br />
— Yutaka Kondo (\@youtalk) <a href="https://twitter.com/youtalk/status/874109784168857600">2017年6月12日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><br />
<p dir="ltr" lang="ja">本日はお疲れ様でした。明日5/23(火)はRaspberry Piで学ぶROSロボット入門勉強会です。初回ためもくもく会の形式となります。興味のある方は是非ご参加ください！ <a href="https://t.co/kY2tpVZHuF">https://t.co/kY2tpVZHuF</a></p><br />
— コワーキングスペース秋葉原Weeyble (\@weeyble) <a href="https://twitter.com/weeyble/status/866661840008261634">May 22, 2017</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<h2 id="hardware">オプション（ハードウェア）</h2><br />
色々開発中のようです。どれがもう売っててどれがまだなのかよくわからんので<a href="http://www.rt-shop.jp/index.php?main_page=product_info&amp;cPath=1295&amp;products_id=3418">アールティさんのページ</a>でご確認を。<br />
<br />
<iframe style="border: none; overflow: hidden;" src="https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2FRaspberryPiMouse%2Fvideos%2F1537782756245807%2F&amp;show_text=1&amp;width=560" width="560" height="420" frameborder="0" scrolling="no"></iframe><br />
<br />
<iframe style="border: none; overflow: hidden;" src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FRaspberryPiMouse%2Fposts%2F1529923667031716%3A0&amp;width=500" width="500" height="485" frameborder="0" scrolling="no"></iframe><br />
<br />
↓こちらはモータの実際の回転量を計測できる基盤（コネクタ）です。<br />
<br />
<iframe style="border: none; overflow: hidden;" src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FRaspberryPiMouse%2Fposts%2F1510372068986876&amp;width=500" width="500" height="664" frameborder="0" scrolling="no"></iframe><br />
<h2 id="maze">迷路走行用ROSパッケージ</h2><br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">ラズパイマウス本で作るパッケージ「pimouse_ros」の上で動作する迷路走行用パッケージです。<a href="https://t.co/csXDgmRm9s">https://t.co/csXDgmRm9s</a><a href="https://twitter.com/hashtag/%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4%E3%83%9E%E3%82%A6%E3%82%B9%E6%9C%AC?src=hash">#ラズパイマウス本</a></p><br />
— Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/878869543367491584">2017年6月25日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
こんな感じで走ります。分岐点でどこを曲がるかは、その時のセンサの値次第です。<br />
<br />
<iframe src="https://www.youtube.com/embed/Zcfcbe8Le3I" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe><br />
<h2 id="learning">学習モジュール</h2><br />
ロボット学会のネタなのでまだ詳細を発表できませんが、今こんなものを作っています。<br />
<br />
こういう制御のプログラムでロボットを動かして・・・<br />
<br />
<iframe src="https://www.youtube.com/embed/q_kBCbnZUEw" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe><br />
<br />
ロボットが別の学習プログラムで動きを真似をします。真似してる動作は簡単ですが、学習プログラムもアホみたいに簡単です。<br />
<br />
<iframe src="https://www.youtube.com/embed/wOGkQbXE2T0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe><br />
<h2 id="simulator">シミュレータ</h2><br />
忘れてました。こちらも色々開発が進んでいるようです。実機と同じようにデバイスファイル（に見せかけたダミーファイル）でセンサ、アクチュエータを通信できるように改造してほしいという依頼を出しています。<br />
<ul><br />
 	<li><a href="https://github.com/rt-net/raspimouse_sim/">シミュレータのリポジトリ</a></li><br />
</ul>
