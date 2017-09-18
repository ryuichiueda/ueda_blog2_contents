---
Keywords: コマンド,CLI,ファイル入出力,素数ネタ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# ゴールデンウイークシェル芸問題のまとめ
<h2>問題はこんなものでした</h2><br />
以下のように1から100まで数字が書いてあるansというファイルを作り、ansの中から素数でない数をワンライナーだけで消し去ってください。（ansの中身を書き換えるということです。forもwhileもなしで、コマンドはパイプでつないで。）<br />
<br />
[bash]<br />
ueda\@ubuntu:~/tmp$ seq 1 100 &gt; ans<br />
[/bash]<br />
<br />
<h2>問題の意図</h2><br />
<br />
意図は隠しつつ伝える必要があるので毎回苦労しますが、この問題は素数がポイントなのではなく、「入力ファイルを出力で上書きできますか？」ということがポイントです。<br />
<br />
こういうことを言うと「シェルによって違う」という話になりがちですが、まずは理詰めで考えることの方が大事なんじゃないかなと、個人的には思います。コード読めという話も出てきますが、これも同様、理詰めで考えればわざわざ読む必要もありません。<br />
<br />
<h2>攻略法</h2><br />
<br />
理屈で考えると、パイプラインの中身がすべて同時に動いている状況で、入力ファイルを出力ファイルに書き戻すには、<br />
<br />
<ul><br />
 <li>入力と出力を時間的に完全に分離</li><br />
 <li>iノード（= ファイルの実体）を分離</li><br />
 <li>パイプに通さずにコマンドに上書きさせる</li><br />
</ul><br />
<br />
のいずれかの方法がとられている必要があります。もちろん、こうでなくてもOSがよしなに計ってくれればよいのですが、そんな冗長な処理をOSに搭載するのは問題です。<br />
<br />
シェルの話をすると、問題のansファイルは、シェルの「あるプロセス」がansファイルに書き込みを始めるときにファイルの中身が空になります。空にしないとファイルの頭からデータを保存できないので、これもコードを読まずに理屈で考えると分かるかと。<br />
<br />
で、私が想定していた解は、こちらです。<br />
<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">factor &lt;ans |sed -n &#39;s/^\\([0-9]*\\): *[0-9]*$/\\1/p&#39; |sponge ans&#10;moreutils好き。 <a href="https://t.co/ZdC6JeAfih">https://t.co/ZdC6JeAfih</a></p>&mdash; ふみやす%シェルまおう的なにか\@通販生活 (\@satoh_fumiyasu) <a href="https://twitter.com/satoh_fumiyasu/status/594365570075598848">May 2, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">% factor &lt; ans | awk &#39;$0*=NF==2&#39; | sponge ans&#10;moreutilsのspongeコマンド <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/594168850821697536">May 1, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
平たく書くとこんな感じ。<br />
<br />
[bash]<br />
###spongeコマンドをインストールする###<br />
ueda\@ubuntu:~/tmp$ sudo apt-get install moreutils<br />
###使う###<br />
ueda\@ubuntu:~/tmp$ cat ans | factor | awk 'NF==2{print $2}' | sponge ans<br />
[/bash]<br />
<br />
sponge(1)というコマンドを使います。名前の通り、入力された字を吸い取っていき、吸い取ってから引数に指定したファイルに書き込みます。ということで、上に挙げた「入力と出力を時間的に完全に分離する」が守られています。<br />
<br />
<br />
「ファイルの実体を分離する」の解もありました。すごい。これは思いつきません。<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">% ( rm ans &amp;&amp; factor | awk &#39;$0*=NF==2&#39; &gt; ans ) &lt; ans <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/594165658046214148">May 1, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
ebanさんはどんな方法でも解いてくるので本当にすごいなあと・・・。<br />
<br />
解説をしておくと、まずansをオープンした後にansを消してから処理してansに書き出すという処理になっています。「rm ans」の時点では、ansが開いているので実体（iノード）はまだ消去されません。ansという名前だけ消えます。んで、その後に「factor ... > ans」となっているので、ansという名前の別のiノードができます。確認しておきましょう。<br />
<br />
[bash]<br />
ueda\@web:~/tmp$ seq 1 10 &gt; ans<br />
ueda\@web:~/tmp$ ls -i ans<br />
2363953 ans<br />
ueda\@web:~/tmp$ (rm ans; factor | awk 'NF==2{print $2}' &gt; ans) &lt; ans<br />
ueda\@web:~/tmp$ ls -i ans<br />
2364013 ans<br />
[/bash]<br />
<br />
実はこの挙動、<a href="http://www.amazon.co.jp/gp/product/4048660683/ref=as_li_ss_tl?ie=UTF8&camp=247&creative=7399&creativeASIN=4048660683&linkCode=as2&tag=ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門</a><img src="http://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=4048660683" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />で少し説明しています。ただ、「具体的な使い道が分からん」という言葉と共に書いたので、今、使い道が分かりました。しかし、こんなコードは普通書かないので「使い道」なのかどうかは定かではありません。<br />
<br />
<br />
最後のコマンドに上書きさせる方法は、（私がspongeを教えてもらったのは斉藤さんからなので）解答を禁止したはずの斉藤さんから強烈なものをいただきました。<br />
<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">最新の gawk の解を gawk だけで。&#10;$ gawk -i inplace &#39;{&quot;factor &quot;$0|getline}NF==2&amp;&amp;$0=$2&#39; ans&#10;<a href="http://t.co/3ALgyyYuUp">http://t.co/3ALgyyYuUp</a>&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; Hirofumi Saito (\@hi_saito) <a href="https://twitter.com/hi_saito/status/594450805765210113">May 2, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
説明は斉藤さんにお任せします。っていうかなんだこれ？？？<br />
<br />
<h2>ブログで取り上げていただきましたのでリンク</h2><br />
<br />
おれの無いぞという方はぜひご連絡くだしあ。<br />
<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">はてなブログに投稿しました <a href="https://twitter.com/hashtag/%E3%81%AF%E3%81%A6%E3%81%AA%E3%83%96%E3%83%AD%E3%82%B0?src=hash">#はてなブログ</a> <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a>&#10;【FreeBSD】入力ファイルに直接リダイレクトして書き込みができるかどうか実験してみた - くんすとの備忘録&#10;<a href="http://t.co/B45Aoo8piL">http://t.co/B45Aoo8piL</a></p>&mdash; くんすとのプレアデス (\@kunst1080) <a href="https://twitter.com/kunst1080/status/594450979728199682">May 2, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">日記書いた! 入力ファイルへのリダイレクト問題 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a>&#10;<a href="http://t.co/LsLYN0H76l">http://t.co/LsLYN0H76l</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/594547960282746882">May 2, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">はてなブログに投稿しました <a href="https://twitter.com/hashtag/%E3%81%AF%E3%81%A6%E3%81%AA%E3%83%96%E3%83%AD%E3%82%B0?src=hash">#はてなブログ</a>&#10;ゴールデンウイークシェル芸問題を解きました - くんすとの備忘録&#10;<a href="http://t.co/yO2UVK1aWm">http://t.co/yO2UVK1aWm</a></p>&mdash; くんすとのプレアデス (\@kunst1080) <a href="https://twitter.com/kunst1080/status/595222172357922817">May 4, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
ブログでないけど有難うございます。<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">GWシェル芸問題、なんか面白いことしたいと思ったらえらいことになりました <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a>&#10;<a href="https://t.co/69qhyMxvms">https://t.co/69qhyMxvms</a></p>&mdash; ひまじん (\@__Himajin) <a href="https://twitter.com/__Himajin/status/594153933716652032">May 1, 2015</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<br />
<h2>せんでん</h2><br />
<br />
最後に宣伝・・・。今回の問題は扱ってませんが、基本、ワンライナーの、シェル芸人による、ワンライナーの本です。<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4774173444" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>
