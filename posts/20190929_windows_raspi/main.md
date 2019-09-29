---
Keywords: ブチギレ,ICS,Raspberry,Windows,インターネット接続の共有
Copyright: (C) 2019 Ryuichi Ueda
---

# Raspberry Piを有線LANでWindows 10に直結してWindows 10経由でインターネットに接続する手順


　[この記事](https://b.ueda.tech/?post=08694)の改訂版です。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">次に、頑張ってこの画面に行きます。<a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a><a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a> <a href="https://t.co/Z79oyLvOy5">pic.twitter.com/Z79oyLvOy5</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178126465822380033?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">Wi-Fiのところで右クリックしてプロパティーを選択します。<a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a><a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a> <a href="https://t.co/rJSvZMV1Rb">pic.twitter.com/rJSvZMV1Rb</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178127104770101249?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">で、子画面が開くので、「共有」のタブを開いてチェックボックスにチェックを入れます。 <a href="https://t.co/OPBtwfvvRB">pic.twitter.com/OPBtwfvvRB</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178127430659129344?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">そのまま右下の「設定」を押しましょう。<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a><a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a> <a href="https://t.co/Q7kRdvNlx1">pic.twitter.com/Q7kRdvNlx1</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178127845618438146?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">で、画面の数字がイミフなので、全部チェックを入れちまいます。<br><br>（以前のWindows 8の頃はhttpとかsshとか説明が出ていたのですが、なぜか謎の数字しか出てこないクソみたいなことになってます。さきほどのうんこも泣いてます。）<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a><a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a> <a href="https://t.co/mQ3Gvwhksl">pic.twitter.com/mQ3Gvwhksl</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178128779736014848?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">これであとはOKを押していって準備完了です。<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a><a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178128987362512896?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">今度は左下の枠（名前は知らん）にcmdと打つと上にコマンドプロンプトが出てくるので、立ち上げます。<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a><a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a> <a href="https://t.co/NXbQT1Jywd">pic.twitter.com/NXbQT1Jywd</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178129586321707008?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">立ち上げたら「arp -a」と打ちます。いろいろ情報が出てきます。<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a><a href="https://twitter.com/hashtag/robosys2019?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2019</a> <a href="https://t.co/AhGtLZ9AWD">pic.twitter.com/AhGtLZ9AWD</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1178129859165356032?ref_src=twsrc%5Etfw">September 29, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

