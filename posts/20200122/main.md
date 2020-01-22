---
Keywords: 日記, Linux, dviout
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（2020年1月22日） 

## wineでのdvioutの設定（続き）

　この前、[Linuxでdviout使えたバンザイという日記](/?post=20191107)を書いたけど、Ghostscriptの設定がまだでした。で、設定してepsを貼り込めるようにできました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">そういえばwineでUbuntuに入れたdvioutでepsを貼ることができるようになった。これでpdf作らずに原稿書ける。pngがまだだけど。 <a href="https://t.co/4QtfIim6w7">pic.twitter.com/4QtfIim6w7</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1219935823354679296?ref_src=twsrc%5Etfw">January 22, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


手順はだいたいこんな感じです。

* `~/.wine/drive_c/gs`に、WindowsでインストールしたGhostscriptをコピー
* `$ ln -s ~/.wine/drive_c/gs ~/gs`（ホームにGhostscriptのディレクトリのリンクを作る）
* dvioutを立ち上げ、Option -> Setup Parameters -> Graphics
* Ghostscriptをverboseにして、「gsx」を次のように設定

```
z:\home\ueda\gs\gs9.50\bin\gswin32c -dNOSAFER -I z:\home\ueda\gs\gs9.50\Resource\Init -I z:\home\ueda\gs\gs9.50\Kanji
```

　これで画像（eps）が表示できました。`gswin32c`のオプションですが、`-I`がライブラリのパスで、`-dNOSAFER`が、どこかに中間ファイルを自由に置けるという意味のようです。`-dNOSAFER`を当てるのに時間がかかりました・・・。

## シェル芸botが国際化？

　英語圏の人が「こんなbot見つけた！」とシェル芸bot発見の悦びを爆発させたことがきっかけで、シェル芸botで[`#shellgei`](https://twitter.com/search?q=%23shellgei&f=live)タグが使えるようになったみたいです。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">echo This cool bot executes the terminal commands you tweet! <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a> <a href="https://t.co/IxSvrIVbjL">https://t.co/IxSvrIVbjL</a></p>&mdash; Gleb Sabirzyanov (@zyumbik) <a href="https://twitter.com/zyumbik/status/1219605329274720256?ref_src=twsrc%5Etfw">January 21, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　で、さっそくシェル芸人総出で英語圏勢を出迎えています。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="und" dir="ltr"><a href="https://t.co/BXFCJPzdY3">https://t.co/BXFCJPzdY3</a> <a href="https://t.co/FaPXGBFZz4">pic.twitter.com/FaPXGBFZz4</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1219769270025932800?ref_src=twsrc%5Etfw">January 21, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="und" dir="ltr"><a href="https://t.co/vYbq8RbcmT">https://t.co/vYbq8RbcmT</a> <a href="https://t.co/Mbp1RS2xQA">pic.twitter.com/Mbp1RS2xQA</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1219780323602358272?ref_src=twsrc%5Etfw">January 22, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="und" dir="ltr"><a href="https://t.co/6gUgiIOVyC">https://t.co/6gUgiIOVyC</a> <a href="https://t.co/7Ntto2kVPz">pic.twitter.com/7Ntto2kVPz</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1219769718459912192?ref_src=twsrc%5Etfw">January 21, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



## 叱られた

　職員証の写真をパーカー姿で撮影したら事務からお叱りの電話がかかってきました。お手数かけました。すんません。


