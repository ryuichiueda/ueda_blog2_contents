# 日記（難しすぎるシェル芸の問題等）
<h1>論文読み</h1><br />
<br />
本日は<br />
<br />
<a href="http://www.nature.com/nrn/journal/v7/n8/abs/nrn1932.html" target="_blank">Path integration and the neural basis of the 'cognitive map'</a><br />
<br />
を読んだ。この分野の論文を読むスピードがようやく上がってきた。<br />
<br />
<h1>SLを止める</h1><br />
<br />
<span style="color:red">追記: USP友の会のFacebookページで聞いたらあっという間に解決しました。ただ、自分のアイデアではないのでここでは書かないw。</span><br />
<br />
・・・というシェル芸の問題を考えついた。<a href="http://usptomo.doorkeeper.jp/events/19679" target="_blank">週末のシェル芸勉強会</a>のために。<br />
<br />
SLというのはslコマンドの出力のことである。が、難しすぎる。<br />
<br />
[bash]<br />
$ sl | LANG=C sed 's/\\x1B\\[.*[A-G|]*//g' | LANG=C sed 's/[\\x08\\x0d]//g' <br />
[/bash]<br />
<br />
などと余計な制御コードを取り払ってみたが、制御コードの中に重要な情報がありそうであり、それが抜けてしまうのでダメそうである。どなたか・・・。<br />
<br />
あ、今回の勉強会はこういうトリッキーなのは出しません。非常に実用的です。ぜひご参加を。<br />
<br />
<br />
今日はもうちょっと飲んでから寝る。
