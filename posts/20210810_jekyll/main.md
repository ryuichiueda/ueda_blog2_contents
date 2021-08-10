---
Keywords: GitHub,Jekyll
Copyright: (C) 2021 Ryuichi Ueda
---

# GitHub上のJekyll製サイトでFont Awesomeを使う

英語の情報見ても「プラグインないよー」みたいな話になってたけど、普通にテンプレートのHTMLにlinkを埋め込んだら使えた。チミ達は生のHTMLを書かんのか？[このサイト](https://shellgei.github.io/info/)のための作業でした。

## テンプレートのHTMLを作る

* 参考サイト: http://yoshikyoto.github.io/githubpages/jekyll.html

上記サイトを参考に、`_layouts`の下に`default.html`を作ると良いと思います。HTMLのデザイン等を流用したい場合は、今表示しているGitHub上のページからソースをコピーしてきて、そこに埋め込み用のタグを仕込みます。

## Font Awesomeのリンクを仕込む

このサイトのHTMLからコピペしました。いろいろルールが変わっているかもしれませんので、このままコピペはおやめください。

```html
<!DOCTYPE html>
・・・
    <!-- head要素の下に起きましょう -->
    <!-- Font Awesome CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
・・・
```

## マークダウンのファイルでアイコン呼び出し

こんな感じで埋め込みます。

```md
    * [WSL1のインストール実演動画 <i class="fa fa-external-link"></i>](https://youtu.be/JAszcQ8IEwg)
```

こんな感じで表示されます。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">やっと付いた・・・テンプレートからfontawesome読み込んだ。 <a href="https://t.co/EyKRxzQhPO">pic.twitter.com/EyKRxzQhPO</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1424901325255438336?ref_src=twsrc%5Etfw">August 10, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


現場からは以上です。
