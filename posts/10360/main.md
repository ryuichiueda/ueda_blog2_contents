---
Keywords: 寝る,日記,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 雑記（2017年9月11日）
昨夜の話だけど、昨日雑記を投稿した後、某ページの運用開始の設定をしていて遅くまで起きていたorz。で、そのときに<a href="/?post=10351">Gitの事故</a>に引き続き、次に書くようにLet's encryptの事故を起こした。寝たのは12:30。ただ今日は調子が良かった。

<h3>Let's encryptを使っていて一時サイトがおかしくなる</h3>

新しいサイトをウェブサーバに作ってLet's encryptでhttps化したら、同じサーバで動いている他のSSLのページのいくつかがブラウザに危険指定されてしまう。色々試行錯誤していたが、ブラウザで危険なサイトを見ようとすると新しいサイトに飛ばされたので、Apacheの設定を疑う。で、confファイルで、

<pre>
&lt;VirtualHost *:443&gt;
</pre>

とホスト名が明示されていないものが全滅していることが判明。慌てて*の部分を正しく設定。なんとか破綻させずに復旧。

しかし、自分はいったいいくつウェブサイトを持っているのか。作業が終わった後、お前の本職はなんなんだと自身を詰問。

<h3>研究室のサイトにhttpの読み込みが混入</h3>

ついでに研究室のサイトのhttps化が不十分とブラウザに叱られたので原因を調査。一つは、<a href="http://xn--lcki7of.jp/848/">こういう話</a>でナンジャコリャという感想。もう一つは、サイトに表示する矢印アイコンのURLがhttp://lab.ueda.techのままだったことで、ちゃんと新しい設定が反映されておらずお手上げ状態・・・だったけどテーマをアップデートしたら勝手に直る。ナンジャコリャ。

<h3>思い出した</h3>

2年前のロボット学会で発表順を間違えたことを今日学生に話した。確か3番目の発表順なのに2番目におもむろに登壇。PCをつないで話し始めようとしたところで本来の2番目の人が困った顔をしていて、座長の梶田先生からご指摘。「ダッバッハ！しっつれいしました！」と降段。新橋のサラリーマン気分がまだ抜けてなくて（？）、全く恥ずかしくはなかったが、恥ずかしかった。

そのときのツイートを探したが見つからず。いいネタなのに（←反省の色無し）つぶやかないのは千葉工大に移ったばかりだったからなのか、単に検索が下手だからか。

明日からロボット学会。どんな爆笑が待っているのか。（←反省しろ）


<h3>第30回シェル芸勉強会の大阪サテライトのレポート</h3>

大阪のLTの一ファンとしてお待ちしておりました。お忙しそうですので、なるべく楽な感じでお願いいたします。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">はてなブログに投稿しました <a href="https://twitter.com/hashtag/%E3%81%AF%E3%81%A6%E3%81%AA%E3%83%96%E3%83%AD%E3%82%B0?src=hash">#はてなブログ</a> <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a><br>「第30回シェル芸勉強会　大阪サテライト」レポート - くんすとの備忘録<a href="https://t.co/UtoG8SdYxx">https://t.co/UtoG8SdYxx</a></p>&mdash; くんすと@埼玉両日 (@kunst1080) <a href="https://twitter.com/kunst1080/status/907240151222444032">2017年9月11日</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

東京もシェル芸勉強会特有の伝統的なグダグダ感を大切にしていきたいところです。

<h3>仕事</h3>

ICRA最低バージョンできあがる。ロボット学会のパワポも最低バージョン一歩手前。某案件の執筆進む。ICRAのビデオはロボット学会の会場で作る予定。実験ビデオ、ズボンから赤いパンツ（ラルフローレン）がはみ出ているがそのままノーカットで作る予定。

なにこのひどい日記？

寝る。

