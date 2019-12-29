---
Keywords: 日記, Raspberry Pi 4, Satysfi
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年12月29日） 

　シェル芸勉強会の翌日でバテていたけど合間にいろいろやった。これだけやって夜に長女の家庭教師をやって体力なくなって終了。他、ウェブサイトのバックアップシステムのバグfixとか熱帯魚の水槽の水換えとか。

## Raspberry Pi 4にUbuntu 18.04

　ROS用にインストール。以前やったときはいろいろ失敗したけど、
今回は某氏のおかげで一発で64bit版・サーバ版のUbuntu 18.04が動いた。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/GravityPresence?ref_src=twsrc%5Etfw">@GravityPresence</a> に教えてもらったRaspberry Pi 4のUbuntu 18.04のイメージ動いた。あざっす。<a href="https://t.co/3fH4nQLGCy">https://t.co/3fH4nQLGCy</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1211090369821257728?ref_src=twsrc%5Etfw">December 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## UbuntuにSatysfiをインストール

　ある書き物のためにノートPCのUbuntu 18.04にSatysfiをインストール。Macとちがって
`opam`という（`opy`並に日本語的には微妙な名前の）OCamlの
パッケージマネージャを使うのでちょっとむずい。
OCamlのバージョンをSatysfiに合わせなきゃいけないところが
自分的にはハマりポイントだった。

* 参考にしたサイト
  * https://github.com/gfngfn/SATySFi/blob/master/README-ja.md
  * https://opam.ocaml.org/doc/Install.html

　インストールした記念に、ちょっと書き物を進めた。（本末転倒）


## シェル芸勉強会のまとめ

　[このページ](/?post=20191228_shellgei_45_links)です。みなさまありがとうございました。

## シェル芸人からの挑戦状

　メンバーの皆さんの作った問題の確認と解答の追加など。

## ウェブサイト（bashcms2）の機能追加

　[このページ](/?page=analysis)に日次のPV数の表示を追加。システムに[このCGIスクリプト](https://github.com/ryuichiueda/bashcms2/blob/ueda_site/bin/analyzer/daily.cgi)を加えて、ページのMarkdownの中にJavaScriptとHTMLを書いて実装。


以上。明日は早起きして家族を羽田に送る。（車は持ってないので電車で。）寝る。
