---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年5月26日）

## pyplotがシェル芸botでエラーを起こす

　シェル芸botでPythonを動かすときに、pyplotをimportするとエラーを起こすという問題に取り組んだが解決せず。

　シェル芸botのDockerイメージで試したところ、こういうエラーが出る。GUI環境でないので描画の際に困るっぽい。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">とりあえず原因特定したっぽい <a href="https://t.co/3y2aWXdzF1">pic.twitter.com/3y2aWXdzF1</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132466360443736064?ref_src=twsrc%5Etfw">2019年5月26日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　これは、[こちらの記事](https://qiita.com/TomokIshii/items/3a26ee4453f535a69e9e)にあるように、

```
import matplotlib as mpl
mpl.use('Agg')
```

と書いておくと、GUIがないサーバでもOKということ。実際に、Dockerの環境だと次のようにエラーは出なくなる。


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これはローカルだとエラー出ないんだけどなあ・・・ <a href="https://t.co/YKW6BFwLSH">pic.twitter.com/YKW6BFwLSH</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132468011707723776?ref_src=twsrc%5Etfw">2019年5月26日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


でも、本番のシェル芸bot環境だとpyplotを読み込むとそこで実行が終わってしまう模様。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="et" dir="ltr">python3 &lt;&lt; EOF<br>import matplotlib<br>matplotlib.use(&#39;Agg&#39;)<br>import matplotlib.pyplot as plt<br>EOF<br>echo あああ <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1132471940373835776?ref_src=twsrc%5Etfw">May 26, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


わからん。
