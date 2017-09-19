---
Keywords: コマンド,CLI,IE使っている方おつかれさまです,w3m,寝る,シェル芸ではないな・・・
Copyright: (C) 2017 Ryuichi Ueda
---

# 【この記事は何の役にも立ちません！】IEを使わずにFirefoxをダウンロードするヒント（当てずっぽう）
<blockquote class="twitter-tweet" lang="ja"><p>IEを使わずにChromeやFirefoxをインストールする方法をシェル芸でなんとかひとつ</p>&mdash; kentaro yanagida (\@yng13) <a href="https://twitter.com/yng13/statuses/461503780643540992">2014, 4月 30</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

・・・とお題が出ましたが、手元にWindowsがありません。

<!--more-->

しかし、Cygwinにw3mがあればできるはずなので、その手順をば。もしWindowsでできなかったら申し訳ないです。

<span style="color:red">（追記: おおおお！<a href="http://news.mynavi.jp/articles/2013/07/09/w3m/002.html">Windowsでw3mを動かす）</a></span>

<span style="color:red">（追記2: じゃあどうやってCygwinインストールするんだと？）</span>

まず、Cygwinにw3mが存在している場合、こうすればFirefoxのサイトが見られるはずです。

```bash
ueda\@remote:~$ w3m http://www.mozilla.org/ja/firefox/new/
```

こんな画面が出ます。

<a href="スクリーンショット-2014-04-30-23.11.30.png"><img src="スクリーンショット-2014-04-30-23.11.30-687x1024.png" alt="スクリーンショット 2014-04-30 23.11.30" width="625" height="931" class="aligncenter size-large wp-image-3077" /></a>

で、カーソルを
```bash
Firefox のダウンロード — 日本語
 • Windows
```
の所にあわせてEnterを押します。

それで、ダウンロードが始まります。画面下に、
```bash
(Download)Save file to: Firefox%20Setup%20Stub%2029.0.exe
```
と出るはずです。

あとは、このファイルを検索で探し出してインストールすればよろしいかと。念のためもう一度言っておきますが、Windowsでは検証しておりません。


寝る。

<h2>追記: じゃあCygwinどうやってダウンロードするんだよ？（注意: これもダメ）</h2>

```bash
$ wget http://cygwin.com/setup-x86_64.exe
```

でいいんですが・・・。wgetがないという・・・。みんな不便なもの使ってるな・・・
