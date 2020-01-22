---
Keywords: 日記, Linux, dviout
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（2020年1月22日） 

## wineでのdvioutの設定（続き）

　この前、Linuxでdviout使えたバンザイという日記を書いたけど、Ghostscriptの設定がまだでした。で、設定してepsを貼り込めるようにできました。

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


## 叱られ

　職員証の写真をパーカー姿で撮影したら事務からお叱りの電話がかかってきました。お手数かけました。すんません。


