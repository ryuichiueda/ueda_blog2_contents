---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年5月26日）

## pyplotがシェル芸botでエラーを起こす→解決してもらう

　シェル芸botでPythonを動かすときに、pyplotをimportするとエラーを起こすという問題に取り組んだが解決せず。

　シェル芸botのDockerイメージで試したところ、こういうエラーが出る。GUI環境でないので描画の際に困るっぽい。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">とりあえず原因特定したっぽい <a href="https://t.co/3y2aWXdzF1">pic.twitter.com/3y2aWXdzF1</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132466360443736064?ref_src=twsrc%5Etfw">2019年5月26日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　これは、[こちらの記事](https://qiita.com/TomokIshii/items/3a26ee4453f535a69e9e)にあるように、

```
import matplotlib as mpl
mpl.use('Agg')
```

と書いておくと、GUIがないサーバでもOKということ。実際に、Dockerの環境だと次のようにエラーは出なくなる。


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これはローカルだとエラー出ないんだけどなあ・・・ <a href="https://t.co/YKW6BFwLSH">pic.twitter.com/YKW6BFwLSH</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132468011707723776?ref_src=twsrc%5Etfw">2019年5月26日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


でも、本番のシェル芸bot環境だとpyplotを読み込むとそこで実行が終わってしまう模様。この↓ツイートには反応なし。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="et" dir="ltr">python3 &lt;&lt; EOF<br>import matplotlib<br>matplotlib.use(&#39;Agg&#39;)<br>import matplotlib.pyplot as plt<br>EOF<br>echo あああ <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132471940373835776?ref_src=twsrc%5Etfw">May 26, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


わからん。

### その後

　解決していただきました。こういうことだったのね・・・。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">再開しました。メモリ上限を100Mにしてみたよ <a href="https://t.co/23LzClFlDy">https://t.co/23LzClFlDy</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1132501418936479744?ref_src=twsrc%5Etfw">2019年5月26日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## bashcms2のDockerイメージ作成

　bashcms2本（下の宣伝参照）のシステムをインストールしたDockerのイメージを作った。

* リポジトリ: https://github.com/ryuichiueda/bashcms2-image

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/41tcU9fYKbL._SL160_.jpg" width="112" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>KADOKAWA 2019-06-28 (Release 2019-06-28)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>

bashcms2本、なんかこう、イマイチ盛り上がりに欠けるのでもう少し宣伝しないといけないけど、日記でダラダラ紹介してしまったからテンション高めの宣伝が書けない。しくじった。


どんまい。寝る。
