---
Keywords: 執筆,ご報告
Copyright: (C) 2019 Ryuichi Ueda
---

# 「フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門」を書き直しました

　「フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門」の改定2版が出ます。この本はbashでブログのサイトを作るという、かなり攻めた内容の本で、[ITエンジニアに読んでほしい！技術書・ビジネス書対象2015の技術書部門ベスト10](https://www.shoeisha.co.jp/campaign/award/2015/result)に入ったり、出版2ヶ月後に[bashの超やばいバグ](https://ja.wikipedia.org/wiki/2014%E5%B9%B4%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF%E8%84%86%E5%BC%B1%E6%80%A7)が見つかって「この本大丈夫か？」と心配されたりと、いろいろ話題になった本でした。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">全面的に書きかえました。| フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版 上田　隆一：生活・実用書 | KADOKAWA <a href="https://t.co/h0S0ipSKpA">https://t.co/h0S0ipSKpA</a> <a href="https://twitter.com/kadokawa_PR?ref_src=twsrc%5Etfw">@kadokawa_pr</a>さんから <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a> <a href="https://twitter.com/hashtag/%E3%81%AA%E3%81%AE%E3%81%AB?src=hash&amp;ref_src=twsrc%5Etfw">#なのに</a> <a href="https://twitter.com/hashtag/%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%AE%E6%9C%AC?src=hash&amp;ref_src=twsrc%5Etfw">#ウェブシステムの本</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1140189505548238848?ref_src=twsrc%5Etfw">June 16, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　今回の内容は、5年たって周囲の状況がいろいろ変わってきたことにあわせて、<span style="color:red">ほぼ全面にわたって書き直しています</span>。改訂2版ということですが、ほぼ別の本になっています。

　内容は、ブログ用のウェブサイトをワンライナー満載のシェルスクリプトでゴリゴリ作っていくというもので、これは初版と変わっていません。変わったのが、<span style="color:red">書籍中で作っていくウェブサイトがご覧のこのサイト</span>だということです。つまり、このサイト https://b.ueda.tech はbashで作られており、そして改訂2版はこのサイトの作り方を書いた本になっています。



<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/41tcU9fYKbL._SL160_.jpg" width="112" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>KADOKAWA 2019-06-28 (Release 2019-06-28)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
       <p style="font-size:80%">（ちなみにこのアフィリエイトも上記amazon-itemをラッパーしたシェルスクリプトで作って貼っています。）</p>
      </div>
    </div>
  </div>
</div>


　ということで、今ご覧になっているサイトがどういう風にbashで動いているか、もしご興味があれば読んでいただけると幸いです。[目薬みたいなマークのフレームワーク](https://jp.vuejs.org/v2/guide/index.html)がとても便利な昨今、いったいなんでbashでウェブサイト作んなきゃいけないんだという感じですが、もしかしたら目から鱗が落ちるか、あるいは目が飛び出るかもしれません。そういえば、5年前は全然違うフレームワークが大流行りしてましたね・・・。あれ、どうなっちゃいましたっけ？


　・・・と、喧嘩を売るつもりは全くない<a href="#fn1">[^1]</a>のですが、役に立つかどうかは別として、自分で書いてある通りに手を動かしてみると楽しい本ではあると思います。何卒よろしくお願いいたします。

<hr />
<ol>
<li id="fn1"><p>売ってるじゃねーかという感じですが、フレームワークを使うかどうかや出来合いのCMSを使うかどうかは一長一短なので、あくまで冗談です。あと、「5年前に流行ったフレームワーク」に何か特定の心当たりがあるわけでもありません。<a href="#fnref1" class="footnote-back">↩</a></p></li>
</ol>
