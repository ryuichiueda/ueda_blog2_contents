---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記（2025年1月18日）

　1月は期末の発表＆卒論シーズンなので各学年のポスターやスライド、卒論、修論の添削の毎日です。で、これはとても疲れる（<span style="color:red">まだ一人前とは言えない文章を精読して、様々な感情を抑えて、本人にとってためになるアドバイスをする~~という地獄のような~~</span>）作業なので、合間に現実逃避するようにコードを組んでます。んで、コード書くだけなのでリリースしたり作業記録をつけたりする作業がすべて後回しになってるのでメモしときます。

## 学会で発表したアルゴリズムのROS 2移植

　このときに発表したアルゴリズムをROS 2で使えるようにしています。ロボットから見えてるものが数秒後にどこにいくか予測するアルゴリズムです。[モザイクかかってるポスターはこちら](https://www.docswell.com/s/ryuichiueda/ZEX11D-si2024)。


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">えーとですね、初心者すぎてポスター貼るところを間違えてて、本当の持ち主の方が貼り直してくださいました。<br><br>大変申し訳ございませんでした・・・ <a href="https://t.co/eelpATwUM6">https://t.co/eelpATwUM6</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1869205420386193502?ref_src=twsrc%5Etfw">December 18, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

C++で画像ファイルを読み込んで画像ファイルを出力するコマンドとして作っていたのを、[RustでROS 2のパッケージとして](https://github.com/ryuichiueda/ogm_flow_estimator_static)実装しなおしています。

READMEを作っていますが、まだちょっと直すのでついった上ではできたといってません。また、ロボットが静止していることを前提にして作っていて、ロボットが動けるものは別のパッケージにしようと思います。いまのところ出力はこんな感じです。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">仮想マシンの機嫌で計算時間が1msになったり10msになったりするけどたぶん1msで計算できとる <a href="https://t.co/1zogabgCtc">https://t.co/1zogabgCtc</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1879829299538297237?ref_src=twsrc%5Etfw">January 16, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
