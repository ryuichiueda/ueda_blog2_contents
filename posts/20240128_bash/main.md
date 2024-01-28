---
Keywords: bash
Copyright: (C) 2024 Ryuichi Ueda
---

# Bashのブレース展開のルールの謎

　Bashのコードが長すぎて事実上ブラックボックスなので、はっきり言ってルールがさっぱりわかりません。構文解析（最近、LL法と思われる方法しか使ってないのでLR法）をたぶんイチからおさらいしないと理解できない模様ですが、ヒントください（泣）

* Bashのbison/yacc用と思われるコード: https://github.com/bminor/bash/blob/f3b6bd19457e260b65d11f2712ec3da56cef463f/parse.y

　明日あたり構文木を紙に書いてみますか・・・

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">うーんうーん<br><br>```<br>$ echo {b{c},c}<br>b{c} c<br>$ echo {}b{c},c}<br>{}bc} {}bc<br>$ echo a{}b{c},c}<br>a}b{c} ac<br>$ echo {a}{b{c},e}<br>{a}b{c} {a}e<br>$ echo {a}b{c},e}<br>a}b{c} e<br>$ echo {a}b{c,d},e}<br>a}bc a}bd e<br>```</p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1751594409676906939?ref_src=twsrc%5Etfw">January 28, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

特に2番目と3番目、あたまにaがついただけで解釈変わるのなんで？私は何を見落としているんでしょうか？？？たぶん情報科出てる人ならさっと教えてくれるはず・・・くれるはず・・・


とりあえず仕事に支障が出るので寝る。
