---
Keywords: コマンド,勉強会,寝る,日記,研究,シェル芸,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記（難しすぎるシェル芸の問題等）
<h1>論文読み</h1>

本日は

<a href="http://www.nature.com/nrn/journal/v7/n8/abs/nrn1932.html" target="_blank">Path integration and the neural basis of the 'cognitive map'</a>

を読んだ。この分野の論文を読むスピードがようやく上がってきた。

<h1>SLを止める</h1>

<span style="color:red">追記: USP友の会のFacebookページで聞いたらあっという間に解決しました。ただ、自分のアイデアではないのでここでは書かないw。</span>

・・・というシェル芸の問題を考えついた。<a href="http://usptomo.doorkeeper.jp/events/19679" target="_blank">週末のシェル芸勉強会</a>のために。

SLというのはslコマンドの出力のことである。が、難しすぎる。

```bash
$ sl | LANG=C sed 's/\\x1B\\[.*[A-G|]*//g' | LANG=C sed 's/[\\x08\\x0d]//g' 
```

などと余計な制御コードを取り払ってみたが、制御コードの中に重要な情報がありそうであり、それが抜けてしまうのでダメそうである。どなたか・・・。

あ、今回の勉強会はこういうトリッキーなのは出しません。非常に実用的です。ぜひご参加を。


今日はもうちょっと飲んでから寝る。
