---
Keywords: 報告
Copyright: (C) 2021 Ryuichi Ueda
---

# 久しぶりに投稿論文（うっそうとした畑で作物の茎を認識するための深層学習に関するもの）が出ます

　ITエンジニア本大賞同様、ここに書くのが遅れました（もしかしたら書いて忘れてるかもしれません）が、
久々に投稿論文が採択されて、掲載待ちです。
**「お前の本業はなんだ？」と聞かれて思わず「ライター」と答えてしまう** ような状況が続いてましたので嬉しいです。
筆頭の三上さん、共著者の皆様おめでとうございます＆ありがとうございました。
なお、まだ正式なものは掲載されていませんが、早期公開という制度があって、校正の入る前の原稿が下記リンクからPDFが入手できます。ぜひ読んでみてください。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ヤンマーさんと行っている深層学習の研究の論文がロボット学会誌で公開されましたー。<br><br>葉っぱに隠れた作物の茎がどこにあるかを推定して補間するという研究です。<br><br>（いま思うと、その前段階である「見えている茎の認識」のほうが超絶難易度高いんですが。）<a href="https://t.co/mUKzljEGMD">https://t.co/mUKzljEGMD</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1481187873835524098?ref_src=twsrc%5Etfw">January 12, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 内容

　論文の内容については、共同研究なので論文以上の情報をここには書けないのですが、[ここ](https://github.com/ryuichiueda/jrsj_color_figs/tree/main/vol_40_no_2)から画像を持ってきて説明します。

　まず、次ようなリアルなCG画像（背景は実写）を準備します。このCGと、どこが葉でどこが茎なのかを指示したデータで、ニューラルネットワークをトレーニングします。なぜCGを使うかというと、「どこが葉でどこが茎なのかを指示したデータ」を実物から作るのには、大変な手間がかかるからです。

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_2.png)

CG画像は、上田研のCG職人石川さん（すでに卒業）が作りました。

　トレーニングするニューラルネットは2つあります。
一方は、（ちょっとノイズがあるけど）手前の葉っぱや茎を検出するものです。調教済みのニューラルネットワークの入出力を下図に示します。左のような写真を入力すると、右のような塗り絵を出力します。

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_11.png)

　もう一方のニューラルネットワークは、上のニューラルネットワークの出力から、写真手前に写った茎を（葉っぱに隠れたものも含めて）検出するものです。下図では、上の写真が元の写真で、下の白黒画像が出力です。

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_12.png)

多少間違いもありますが、葉っぱに隠れたところも白くつながっているのが分かるでしょうか。

　元の写真を見ると分かるように、畑で水平方向にカメラを向けて写真を撮ると、半分以上が緑に覆われた写真になりがちです。この写真からは、人間でもどこに何があるのか判別するのに時間がかかります。深層学習の研究としても、従来よりかなり難しい問題を解いているのですが、作成したニューラルネットワークは1秒もかからず、どこが葉でどこが茎かを出力できました。


　あとは、冒頭のツイート内の[リンク](https://www.rsj.or.jp/pub/jrsj/advpub/400201.html)から、PDFをご一読ください。


以上です。
