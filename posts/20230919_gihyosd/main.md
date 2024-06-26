---
Keywords: 自作シェル, bash, 連載, Software Design
Copyright: (C) 2023 Ryuichi Ueda
---

# Software Design10月号自作シェルの世界

　Software Design 10月号が発売されています。私の連載「[魅惑の自作シェルの世界](/?page=sd_rusty_bash)」について、[先月号](/?post=20230819_gihyosd)に引き続き説明します。今回は10月号の内容自体の説明です。[購入はこちらから](https://www.amazon.co.jp/shop/ryuichiueda/list/7MLC9JANITU0?ref_=aip_sf_list_spv_ons_mixed_d)どうぞー

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Software Design連載の「魅惑の自作シェルの世界」はリダイレクトの実装に突入しました<br><br>連絡先、今月号からMisskeyのアカウントになってます<a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/EeLaxMzd93">pic.twitter.com/EeLaxMzd93</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1703182935300706784?ref_src=twsrc%5Etfw">September 16, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 10月号の内容や裏話

　「リダイレクトに突入」と上でツイートしていますが、実際には、

* 前回までのコードの至らない点についてリファクタリング
* Bashの「`|&`」の実装
* コマンドライン中のリダイレクトのパース（の準備）

くらいになっています。

### リファクタリング（といえばカッコいいが・・・）

　できれば連載中にはお見せしたくないものですが、前回までのコードで変なところを白状し、どう書き直したか説明しました。小説や漫画ではありえん行為です。申し訳ねえです。あ、でも死んだはずのキャラクターが生き返るとかありますね。よかったよかった（？）

　ちなみに連載のコードは、一度自分が書いたBashのクローンのコード（https://github.com/shellgei/rusty_bash のmainブランチにあるもの）の反省を踏まえて、もう一度まっさらな状態から書き直しているものです。そのためある程度は、場当たり的なものではなくて構造化されたものをお見せしてます。ただ、原稿が出たあとでもっとこうすればよかったと思うことが結構あるので、今後もあまり隠さず手直しをしていこうと思います。

### Bashの「`|&`」の実装

　リダイレクトの実装に入る前に、「`|&`」を実装しました。`|&`がなんであるか知りたければ、（ネットで調べるとすぐ出てきますが）ぜひ記事を読んでくださいっ！ここでは「シェル（bashやzsh）を使っていると便利なパイプ」くらいにとどめておきます。

### リダイレクトのパース

　4ページ目からようやく始まってます。リダイレクトに見立てた「`>file`」や「`<file`」という文字列を、入力された文字列から見つけて取り込む処理までを実装しています。内容は読んでというところですが、コマンドのどこにリダイレクトが置けるのかという説明で、Bashの変態性に触れています。なんであんな仕様なんだろ・・・。そういえば以前、「シェル芸〜wwwww」とかやり始めたくらいのときに、Twitter上の大先輩に教えてもらってなんじゃこりゃと思った思い出が。

## 今後

　12月の原稿を書いていますが、まだリダイレクトで次回もリダイレクトなので、4ヶ月はリダイレクト地獄です。特にファイル周りはエラー処理が重要で、ページを割くことになりそうです。自身は現場にはいたもの所詮は「世の中にないものを動かしたらオッケーあとは知らん」というノリの研究者で、そこまでしつこいエラー処理の実装は経験がございません。ということで、勉強しなおしてます。記事は嘘のないように、自分の限界を示しつつ謙虚に書いていきます。


以上です。もういっぺん言うと、Amazonでいい人は[購入はこちらから](https://www.amazon.co.jp/shop/ryuichiueda/list/7MLC9JANITU0?ref_=aip_sf_list_spv_ons_mixed_d)。[技術評論社の公式ページ](https://gihyo.jp/magazine/SD/archive/2023/202310)からも購入できます。
