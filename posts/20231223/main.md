---
Keywords: bash, 日記
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年12月23日）

　シェル芸勉強会のまとめはもうちょいお待ちください。

## 論文見ろと煽ったら見られすぎた

　[この論文](https://www.fujipress.jp/jrm/rb/robot003500061489/)についてこういうツイートをしたら、[論文のページのview数のランキング（60日通算）](https://www.fujipress.jp/most-viewed/)に1日で6位になってしまいました。2日目は5位でした。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">変態論文が出ました。CPUぶん回して単純計算で経路計画と障害物回避をやる頭の悪いやつで、他の賢い方法を軒並み葬り去る可能性アリ<br><br>「スケーラビリティーみせろや！」と査読で言われて（速くならんけど）ノートPCで120スレッドまわしたり、とにかくアホで個人的に大満足<a href="https://t.co/fIz6lNaow0">https://t.co/fIz6lNaow0</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1737241838321553868?ref_src=twsrc%5Etfw">December 19, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　研究者はこういうことせずに真面目に良い研究をしたほうがいいのですが、宣伝も大事なのでよかったとします。論文を紹介する動画でも作ろうかな・・・。なんか巷では、「40万くれたら動画作ってやる」と寄ってくる人もいるらしい。ちなみに、この論文の掲載には（カラーページが多い関係で）38万円かかりました。貴様の研究室、もうお金が1万5千円しかないぞと事務から連絡がきました。やべえ。


## Bashのブレース展開とコマンド置換に関する実験

　`man`には「ブレース展開のほうが先」と書いてあるので、ほんとうにそうなってるか実験しました。
```bash
$ time echo $(sleep 2 ; echo a){b,c}
ab ac

real	0m4.008s
user	0m0.005s
sys	0m0.002s
```
実行時間が4秒になっているので、先に
```bash
$ echo $(sleep 2 ; echo a){b,c}
```
が
```bash
echo $(sleep 2 ; echo a)b $(sleep 2 ; echo a)c
```
に展開されて、`sleep 2 ; echo a`が2回実行されていることが分かりました。


以上です。
