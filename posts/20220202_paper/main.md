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

　論文の内容については、共同研究なので論文以上の情報をここには書けないのですが、[ここ](https://github.com/ryuichiueda/jrsj_color_figs)から画像を持ってきて説明すると、上田研のCG職人石川さん（すでに卒業）の作った、

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_2.png)

のようなリアルなCG画像（背景は実写）でニューラルネットワークを学習すると、

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_11.png)

というように、ちょっとノイズがあるけど、手前の葉っぱや茎を検出するニューラルネットワークや、

![](https://raw.githubusercontent.com/ryuichiueda/jrsj_color_figs/main/vol_40_no_2/fig_12.png)

というように、手前の茎を（葉っぱに隠れたものも含めて）検出できるニューラルネットワークができるよ、というものです。

