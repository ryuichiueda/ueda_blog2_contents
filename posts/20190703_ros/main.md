---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月3日）

　本日は午前に研究関係でロボットのコード書き。午後は講義資料書き。

## ROSいじり1


　昨日立てた予定どおり、amclをいじってロボットにあるアルゴリズムで行動をとらせる。雑だがだいたい動くようになったので次のフェーズに行く。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">まーとりあえずこんなもんか。 <a href="https://t.co/kQIyBdjJUN">pic.twitter.com/kQIyBdjJUN</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1146240676687781888?ref_src=twsrc%5Etfw">July 3, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



## ROSいじり2


　ロボットとPC側でlaunchファイルが別れているので両方を叩くシェルスクリプトを作った。が、たぶんlaunchファイルに書けるんじゃないかなーと思って調べてないのは怠慢だと思って調べるとちゃんとあった。明日やる。こういうものは本書くときに漏れがないように一通り勉強しなきゃいけないので完全に怠慢。アカン。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">あーなるほど。こうすればよいのか。<a href="https://t.co/tQVlJVseE0">https://t.co/tQVlJVseE0</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1146347445921579008?ref_src=twsrc%5Etfw">July 3, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ありがとうございます。

## DFA、NFA

　昨日、某企業で正規表現が暴走したそうで、シェル芸bot上でも時間のかかる正規表現について実験が行われていました。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">real0m2.365s<br>user0m2.360s<br>sys0m0.000s <a href="https://t.co/Ic6mHXthaD">https://t.co/Ic6mHXthaD</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1146212800567504896?ref_src=twsrc%5Etfw">2019年7月3日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">real0m0.002s<br>user0m0.000s<br>sys0m0.000s <a href="https://t.co/qYps07Blw1">https://t.co/qYps07Blw1</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1146213698639261697?ref_src=twsrc%5Etfw">2019年7月3日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">real0m11.440s<br>user0m9.472s<br>sys0m0.044s <a href="https://t.co/SgigkIjSTZ">https://t.co/SgigkIjSTZ</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1146216507514294272?ref_src=twsrc%5Etfw">2019年7月3日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/search?q=%24x&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$x</a>=&quot;a*a*a*a*a*a*a*a*a*a*a*a*[bc]&quot;;$s = &quot;aaaaaaaaaaaaaaaaaaaaa&quot;; [regex]::Replace($s,$x,{$args})<br><br>real0m0.767s<br>user0m0.844s<br>sys0m0.088s <a href="https://t.co/ot1FTKmcQR">https://t.co/ot1FTKmcQR</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1146223963862732806?ref_src=twsrc%5Etfw">2019年7月3日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　この話、実は2017年12月にシェル芸勉強会で鳥海さんがとりあげていました。DFAを使った正規表現のマッチングは1文字1文字状態遷移させるだけなので受理か不受理が決められた時間で出てきますが、NFAだと探索みたいなこと（バックトラック）が発生して場合によっては異常に時間がかかるという現象があるとのこと。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">あった。DFAとNFA扱った時の鳥海さんのスライド <a href="https://t.co/pu8tiaMfMI">https://t.co/pu8tiaMfMI</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1146404568072245248?ref_src=twsrc%5Etfw">July 3, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　もしかしたらこのサイトの検索機能（`grep`を使用）にも問題があるかもしれませんので、いろいろ挑戦してみていただければと。（なるべくテストすると宣言してからお願いします。）

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">grepは-P使わなければDFA型（決定性有限オートマトン）なので正規表現のマッチは早いすね。Cloudflareは裏でNFA型の何かを使ってたのかな。</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1146214378926157824?ref_src=twsrc%5Etfw">July 3, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　DFA（決定性有限オートマトン）とNFA（非決定性有限オートマトン）については、次の教科書が詳しいです。

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4320122070/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51rjfNYrhjL._SL160_.jpg" width="112" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4320122070/ryuichiueda-22">計算理論の基礎 [原著第2版] 1.オートマトンと言語</a></dt>
          <dd>[Michael Sipser]</dd>
          <dd>共立出版 2008-05-21</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>

## 著作権とライセンスについて

　これもいろいろ昨日から話題になってますが、私も講義で[毎年90分話をしている](https://github.com/ryuichiueda/robosys2018/blob/master/09_license.md)のでおさらいをしました。

　こちら、度々参考にさせていただいております。

<iframe src="//www.slideshare.net/slideshow/embed_code/key/118TR8AdWAm0oL" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/YutakaKachi/ss-118947772" title="オープンソースライセンスの基礎と実務" target="_blank">オープンソースライセンスの基礎と実務</a> </strong> from <strong><a href="https://www.slideshare.net/YutakaKachi" target="_blank">Yutaka Kachi</a></strong> </div>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">知る、読む、使う！ オープンソースライセンス - 達人出版会 <a href="https://t.co/TsciUjAGLH">https://t.co/TsciUjAGLH</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1146409633688330240?ref_src=twsrc%5Etfw">July 3, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


寝る。
