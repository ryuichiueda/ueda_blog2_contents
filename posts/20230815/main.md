---
Keywords: 日記, Misskey
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年8月15日）

　科研費の申請書を書いて、本の校正をして、読書をして、疲れて自分のサイトのテコ入れをしました。

## 読書

　自分の統計の本で人間のことを書いている関係で、「計算論的精神医学」と「自由エネルギー原理入門」を繰り返し読んでいます。自分はそこまで詳しく書くわけではないので、「やっぱり脳みそは変分推論してるのか」くらいでまだ理解は浅いままです。自分が学生のときにパーティクルフィルタ程度しか理解できていない状態で「これからは確率だ」と訴えていたときに、脳みそまでベイズでモデル化しようとしていた人たちがいたのはほんとに情けない限りです。

　上に挙げた本は、[例](https://b.ueda.tech/?post=20230811#amazon%E3%81%AE%E8%87%AA%E5%88%86%E3%81%AE%E3%83%9A%E3%83%BC%E3%82%B8)の[Amazonの自分のショップ](https://www.amazon.co.jp/shop/ryuichiueda/list/1DLTMFGRF0G14?ref_=aip_sf_list_spv_ofs_mixed_d)に置きました。

## 論文で自分のコードを利用してもらった

　自己位置推定のROSパッケージ[emcl2](https://github.com/ryuichiueda/emcl2)を研究に使っていただきました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">自分のコードを使っていただいているレターが発表されていました。感謝です。 <a href="https://twitter.com/hashtag/emcl2?src=hash&amp;ref_src=twsrc%5Etfw">#emcl2</a> <a href="https://t.co/xIpGtRAVLc">https://t.co/xIpGtRAVLc</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1691425851576033280?ref_src=twsrc%5Etfw">August 15, 2023</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

他の人にもちらほら使っていただいているので、論文が出たらこっそりおしえていただければ幸いです。

## サイトのテコ入れ

　数年前までこのサイトには広告（AdSense）がついていたのですが、最近は`ads.txt`問題があって掲載をやめていました。`ads.txt`というのは、広告を載せるサイトが公正なものか確認するためのテキストファイルで、Googleにサイトの **トップレベルドメイン** （この場合はjpとかcomとかのことではなく、b.ueda.techの場合はueda.techなどホスト名のつかないドメイン） に置けと言われていて、どうやってやるのかよく分からず放置していました。

　が、単にAレコードにホスト名抜きでIPアドレスを指定すれば良いだけの話と今更気づいて、DNSサーバーの設定をして、[このように](https://ueda.tech/ads.txt)置きました。ということで、なるべく控えめにしますが、広告が復活します。日記じゃなくて真面目な記事を書かないと・・・


以上です。寝る。
