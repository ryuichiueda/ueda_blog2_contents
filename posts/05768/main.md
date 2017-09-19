---
Keywords: コマンド,どうでもいい,awk,CLI,OFS,寝る,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# AWKでビール区切りデータ（beer separated values, BSV）を作ってみる
こんなのを見てしまったばっかりに・・・


<blockquote class="twitter-tweet" data-partner="tweetdeck"><a href="https://twitter.com/ngsw/status/586900807179579393">April 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Macでこんなワンライナーを書いて実行してしまい・・・

<!--more-->

```bash
$ echo ソーセージ 餃子 シメのラーメン |
 awk -v OFS=&quot;\\xF0\\x9f\\x8d\\xba&quot; '{print $1,$2,$3}'
```


こんな出力を得ました。

<a href="スクリーンショット-2015-04-12-22.55.56.png"><img src="スクリーンショット-2015-04-12-22.55.56-300x23.png" alt="スクリーンショット 2015-04-12 22.55.56" width="300" height="23" class="aligncenter size-medium wp-image-5770" /></a>

なんの役にもたたない・・・

さらに・・・

```bash
$ echo ソーセージ 餃子 シメのラーメン | sed p | sed p | sed p |
 awk -v OFS=&quot;\\xF0\\x9f\\x8d\\xba&quot; '{print $1,$2,$3}'
```

<a href="スクリーンショット-2015-04-12-23.04.52.png"><img src="スクリーンショット-2015-04-12-23.04.52-300x181.png" alt="スクリーンショット 2015-04-12 23.04.52" width="300" height="181" class="aligncenter size-medium wp-image-5777" /></a>

ほんとうにくだらない。ほんとうにくだらない。

あ、AWKのOFSっていうのは「output field separator」のことで、出力の区切り文字をこのようにオプションで指定できます。

最後にちょっと人の役に立ったかも。自分には何の役にもたってないけど。


日曜日おわり。寝る。
