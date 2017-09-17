# AWKでビール区切りデータ（beer separated values, BSV）を作ってみる
こんなのを見てしまったばっかりに・・・<br />
<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><a href="https://twitter.com/ngsw/status/586900807179579393">April 11, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
Macでこんなワンライナーを書いて実行してしまい・・・<br />
<br />
<!--more--><br />
<br />
[bash]<br />
$ echo ソーセージ 餃子 シメのラーメン |<br />
 awk -v OFS=&quot;\\xF0\\x9f\\x8d\\xba&quot; '{print $1,$2,$3}'<br />
[/bash]<br />
<br />
<br />
こんな出力を得ました。<br />
<br />
<a href="スクリーンショット-2015-04-12-22.55.56.png"><img src="スクリーンショット-2015-04-12-22.55.56-300x23.png" alt="スクリーンショット 2015-04-12 22.55.56" width="300" height="23" class="aligncenter size-medium wp-image-5770" /></a><br />
<br />
なんの役にもたたない・・・<br />
<br />
さらに・・・<br />
<br />
[bash]<br />
$ echo ソーセージ 餃子 シメのラーメン | sed p | sed p | sed p |<br />
 awk -v OFS=&quot;\\xF0\\x9f\\x8d\\xba&quot; '{print $1,$2,$3}'<br />
[/bash]<br />
<br />
<a href="スクリーンショット-2015-04-12-23.04.52.png"><img src="スクリーンショット-2015-04-12-23.04.52-300x181.png" alt="スクリーンショット 2015-04-12 23.04.52" width="300" height="181" class="aligncenter size-medium wp-image-5777" /></a><br />
<br />
ほんとうにくだらない。ほんとうにくだらない。<br />
<br />
あ、AWKのOFSっていうのは「output field separator」のことで、出力の区切り文字をこのようにオプションで指定できます。<br />
<br />
最後にちょっと人の役に立ったかも。自分には何の役にもたってないけど。<br />
<br />
<br />
日曜日おわり。寝る。
