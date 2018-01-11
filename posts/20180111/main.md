---
Keywords: 頭の中だだ漏らし,日記
Copyright: (C) 2017 Ryuichi Ueda
---

# 雑記（2018年1月11日）

近頃の学生さんは子供にお年玉をやるらしい。

### 仕事

某合宿の引き継ぎ。本の執筆と本のためのコード書き。ゼミ。査読の割り振り。

### どうしてもMacでDVIビュワーが欲しい件

数ページの論文ならともかく、ここ数年、300ページ級の原稿と格闘している身としては、LaTeXの原稿をpdfにするのをいちいち待っているのが相当時間の無駄なので、Windowsのdvioutみたいなものがどうしても欲しくなる。ということで、ちょっと時間を割いて調査した。

まず、これを試した。しかし、日本語がダメそう。あと、どういう風にtexファイルをコンパイルしているのかよくわからんかった。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">本日試したDVIビュワー1（というか統合環境）<a href="https://t.co/ZVNVGrEFFw">https://t.co/ZVNVGrEFFw</a><br><br>結果: 日本語が表示できず。</p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/951467349894348802?ref_src=twsrc%5Etfw">January 11, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

次に最高に便利そうなこちらを試させていただく。GitHubからzipでダウンロードして、原稿のあるディレクトリに展開し、dviファイルを表示するためのhtmlファイルを書き、原稿のディレクトリでPythonの簡易HTTPサーバを立ち上げることで、ブラウザに原稿が表示された。すんごい。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">本日試したDVIビュワー2<a href="https://t.co/dbZBHvo002">https://t.co/dbZBHvo002</a><br><br>大変魅力的で素晴らしかったのですが、英語が出ず。あと、数式が・・・（もう自分が設定を頑張ればちょっとうまくできるかもしれない）</p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/951468022148902913?ref_src=twsrc%5Etfw">January 11, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


しかし、大方のDVIビュワーとは逆で日本語は綺麗に出力され、英語が出ないという結果に。私の設定が悪いのかも。あと、数式の出力は如何ともしがたい感じがあったので、数式多用の私にはちょっと手に負えない感じ。しかし、すごいコード書く人もいるもんだとただただ感心。

んーしかし、なんとかならないですかね。やっぱりpxdviか何かが一番いいんでしょうか。あるいは原稿を書くときだけWindowsを使うとか・・・。

Windowsか・・・


寝る。
