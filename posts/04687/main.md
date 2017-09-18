---
Keywords: CLI,UNIX/Linuxサーバ,USP友の会,勉強になりました,勉強会,寝る,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 第14回シェル芸勉強会で個人的に面白かった解答
個人的に印象に残った解法をペタペタ貼り付けします。シェル芸勉強会関連のウェブ工作活動が続いておりますが、これが最後です。<br />
<br />
<a href="https://www.usptomo.com/PAGE=20141214USPSTUDY" target="_blank">公式の勉強会報告はこちらです。</a><br />
<br />
<a href="http://blog.ueda.asia/?p=4671" title="【問題のみ】第14回東京居残りシェル芸勉強会">問題はこちら</a><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>シェル芸初参加だがみんな変態すぎて&#10;まるで追いつけない。&#10;&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; YOUG (\@YOUG_XX) <a href="https://twitter.com/YOUG_XX/status/543652746105065472">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
・・・追いつかなくて・・・大丈夫だと思います・・・。<br />
<br />
<br />
では、いってみましょう。<br />
<br />
<!--more--><br />
<br />
<h1>Q1での副会長の解答</h1><br />
<br />
腕が上がってるような気が。なぜかRedHat系でしか動かないのですが、いい感じです。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>echo $(seq 1 100) | sed -e &#39;s/[[:space:]]/\\ \\\\*\\ /g&#39; | xargs expr <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; (っ´∀｀)っ ゃー (\@nullpopopo) <a href="https://twitter.com/nullpopopo/status/543637613769261056">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>Q2をGNU sedでなくオリジナルのsedで解く</h1><br />
<br />
n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;・・・<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>seq 100 | sed &#39;n;n;s/.*/Fizz/&#39; | sed &#39;n;n;n;n;s/[0-9]*$/Buzz/&#39; <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; No Wasabeef No Life (\@Hexomino) <a href="https://twitter.com/Hexomino/status/543642331627282432">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>seq 100 | sed -e &#39;n;n;s/.*/Fizz/&#39; | sed &#39;n;n;n;n;/F/s/$/Buzz/;/F/!s/.*/Buzz/&#39;&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; fujita masaru (\@t5tmy) <a href="https://twitter.com/t5tmy/status/543641047494959104">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>Q2&#10;seq 100 | sed -e &#39;n;n;s/^.*$/Fz/&#39; | sed -e &#39;n;n;n;n;s/^.*$/Bz/&#39; | sed -e &#39;n;n;n;n;n;n;n;n;n;n;n;n;n;n;s/^.*$/FzBz/&#39;&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; hidezzz (\@hidezzz) <a href="https://twitter.com/hidezzz/status/543643262402064385">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>Q2をjqで解く</h1><br />
<br />
jqで解くって、何を言っているのか意味がわかりません・・・<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>sedじゃなくてjqで&#10;% seq 100|jq -r &#39;. as$i|[[&quot;Fizz&quot;][.%3],[&quot;Buzz&quot;][.%5]]|add//$i&#39; <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/543641395953561600">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>フェルマーですか？</h1><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> 問題3、解けたけど長すぎるので提出できない!! (答えは0x13と0x0D)</p>&mdash; 日柳 光久 (\@mikkun_jp) <a href="https://twitter.com/mikkun_jp/status/543646625814425601">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>opensslで素数の問題を解く</h1><br />
<br />
みなさんいったいなんなんですか？opensslは計算コマンドじゃありませんよ。しかも二人。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>% echo 0xaf 0x13 0x0d 0x24 0x58 | fmt -1 | sed s/..//|xargs -n1 openssl prime -hex | grep -v not <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/543646133843525632">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>echo 0xaf 0x13 0x0d 0x24 0x58 | xargs printf &#39;%d\\n&#39; | xargs -n 1 openssl prime | grep -v &#39;not&#39;&#10;微妙。。&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; fujita masaru (\@t5tmy) <a href="https://twitter.com/t5tmy/status/543646172322074625">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>Q3をRubyで解く</h1><br />
<br />
コマンド並みにメソッドとオプションを知っていないとできない芸だと思う・・・。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>% echo 0xaf 0x13 0x0d 0x24 0x58 | ruby -rmathn -ane &#39;puts <a href="https://twitter.com/search?q=%24F&amp;src=ctag">$F</a>.select{|x|Prime.prime?(x.hex)} <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/543644235266682880">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>今回も炸裂したphp_cli芸</h1><br />
<br />
ありがとうございます。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>echo 0xaf 0x13 0x0d 0x24 0x58 | php -r &#39;$a=explode(&quot; &quot;, fgets(STDIN));foreach($a as <a href="https://twitter.com/search?q=%24b&amp;src=ctag">$b</a>){if(gmp_prob_prime($b)){echo <a href="https://twitter.com/search?q=%24b&amp;src=ctag">$b</a>,&quot;\\n&quot;;}}&#39; <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; kuwa1 (\@kuwashima) <a href="https://twitter.com/kuwashima/status/543647868569911298">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>Pythonつこうた</h1><br />
<br />
Pythonメタプログラマーと呼んでくらっさい。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>Q7前半 echo &#39;1/4 + 2/5 + 7/16 - 5/9&#39; | sed &#39;s/\\([+-]\\) /\\1/g&#39; |&#10; sed &#39;s;\\([+-]*[0-9]*\\)/\\([0-9]*\\);+ Fraction(\\1,\\2);g&#39; |&#10;&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; Ryuichi UEDA (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/544129655570042880">2014, 12月 14</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>Q7後半&#10; awk &#39;{print &quot;from fractions import Fraction ; a = &quot;,$0,&quot;;print a&quot;}&#39; |&#10; python&#10;&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; Ryuichi UEDA (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/544129758062080001">2014, 12月 14</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
（自分の解答例をコピペしたツイートを貼り付けてます。）<br />
<br />
あ。もう一人・・・<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>echo &#39;print &#39;$(seq 100 | tr &#39;\\n&#39; &#39;*&#39;)1 | python&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; fujita masaru (\@t5tmy) <a href="https://twitter.com/t5tmy/status/543636102850940928">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>巻島？パリグランプリ？</h1><br />
<br />
mathematicaみたいなことができるらしいです。今度使ってみます。mecabもそうですが、CLIと親和性の強い大型コマンドは本当に有難いです。感謝感謝。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>echo &#39;1/4 + 2/5 + 7/16 - 5/9&#39; | paste - &lt;(echo &#39;;&#39;) | maxima | tail -4 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; fukuda (\@fukuda0000) <a href="https://twitter.com/fukuda0000/status/543671903395655680">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>PARI/GPを使うと計算できてしまう(インストールすると200MBほど食うが)。&#10;% sudo apt install pari-gp&#10;% echo &#39;1/4 + 2/5 + 7/16 - 5/9&#39; | gp -f -q&#10;383/720&#10;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/543816990394032129">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<h1>地獄のQ8</h1><br />
<br />
自分のです。汚い。ここまで来ると左から右へ一筆書きというより、頭の中でインデントを想像しながらプログラミングする感覚になります。もちろん、遊びです。<br />
<br />
<blockquote class="twitter-tweet" lang="ja"><p>Q8 会場で作った答え。死ぬ。 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="http://t.co/NUbQQQw19i">pic.twitter.com/NUbQQQw19i</a></p>&mdash; Ryuichi UEDA (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/543675929466126337">2014, 12月 13</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<br />
<br />
スタッフの方、会場に来られた方、リモート参戦の方、皆様ありがとうございました。<br />
<br />
<br />
寝る。
