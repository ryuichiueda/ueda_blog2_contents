---
Keywords: 日記
Copyright: (C) 2021 Ryuichi Ueda
---

# 日記（2021年4月19日）

午前中は新学期の事務などの合間にいろいろやりましたが、午後は眠気でミーティング一件やったくらいで終わりました。昨日、ゴリゴリプログラムしてたのが響いた模様。

## glueutils

juzという凶悪なコマンドを作成。引数に書いたコマンドを指定した回数だけ数珠つなぎにします。

```
$ echo 1 | juz 10 awk '{print $1*2}'
1024
```


シェル芸botに放ったところ、結構便利なようです。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="und" dir="ltr"><a href="https://t.co/viud6zJzY7">https://t.co/viud6zJzY7</a> <a href="https://t.co/eEeYzFAPjT">pic.twitter.com/eEeYzFAPjT</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1384007826771570690?ref_src=twsrc%5Etfw">April 19, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">&lt;&lt;&lt;&lt;&lt;うんこ&gt;&gt;&gt;&gt;&gt; <a href="https://t.co/HgiiCyZjhW">https://t.co/HgiiCyZjhW</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1384003888517287936?ref_src=twsrc%5Etfw">April 19, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


これ、`juz 10000000`とかやると大変なことになりそうですけど、まだ試してません。


## 移動ロボットのシミュレーション環境の準備

学生さんにおまかせしてたけど、ナビゲーションスタックの改良の研究をするときに自前でシミュレーション環境を持っておきたかったので。こちらのサイトを参考にとりあえずセットアップしました。

* https://qiita.com/protocol1964/items/1e63aebddd7d5bfd0d1b


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">なんか他にやらなきゃいけないことあるような気がするけど研究する。 <a href="https://t.co/9VYs6Iv9Pu">pic.twitter.com/9VYs6Iv9Pu</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1383951454684123139?ref_src=twsrc%5Etfw">April 19, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

