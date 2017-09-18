---
Keywords:寝る,日記,シェル芸,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---
# 雑記（2017年9月9日）
<h3>にゃーんを短く</h3><br />
<br />
<br />
こういうことがあって<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">ネットワークエンジニア「ping打つと"にゃーん"返すサービス作ったよ」<br />
<br />
他界隈のエンジニア「なんだこれ癒やされる（けどCiscoルータ限定かあ…）」<br />
<br />
シェル芸人「 $ sudo ping -i 0 -c 1400 | grep …」<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="https://t.co/KnZe5vW0xw">pic.twitter.com/KnZe5vW0xw</a></p><br />
— ぐれさん (\@grethlen) <a href="https://twitter.com/grethlen/status/906154326975905793">2017年9月8日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
当然こういう話になって、<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">にゃーん表示するやつ、140文字に収まらなかったけど某E氏が絶対140文字以内におさめてくるパターンでしょこれ。絶対そうでしょ。おれしってる。</p>&mdash; ぐれさん (\@grethlen) <a href="https://twitter.com/grethlen/status/906167669518327808">2017年9月8日</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
割って入って<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">U氏だけど。<br><br>sudo ping -i0 -c1400 <a href="https://t.co/uyDjdhRmYR">https://t.co/uyDjdhRmYR</a>|awk &#39;/^6/{print NR}&#39;|sort -n - &lt;(seq 1400)|uniq -c|awk &#39;{printf $1}&#39;|fold -w70|tr 12 U!</p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/906286383580381184">2017年9月8日</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<br />
こうなって、<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">sudo ping -i0 -c1400 <a href="https://t.co/uyDjdhRmYR">https://t.co/uyDjdhRmYR</a>|grep -o ^.|tr -d &#39;\\n&#39;|fold -w70| sed &#39;s/[^F]/ /g&#39;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="https://twitter.com/hashtag/ping?src=hash">#ping</a> <a href="https://twitter.com/hashtag/%E3%81%AB%E3%82%83%E3%83%BC%E3%82%93?src=hash">#にゃーん</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/906291672153075712">2017年9月8日</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
当然こうなった。<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">sudo ping -i0 -c1400 <a href="https://t.co/1SFrjlHAot">https://t.co/1SFrjlHAot</a> | tr -dc yU | fold -w70 | tr y &#39; &#39;<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/906305537075056640">2017年9月8日</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<br />
<h3>ロボット学会のスライド</h3><br />
<br />
最低バージョン完成<br />
<br />
<h3>ICRA</h3><br />
<br />
明日にかける。<br />
<br />
<h3>某案件</h3><br />
<br />
作り物の大改修のあと、書いたところの修正も一気にした。ICRAそっちのけだけど、やりたいことを他のスケジュールで抑制するとかえって気疲れするので。<br />
<br />
<br />
集中しすぎて体が興奮しているが、寝る。
