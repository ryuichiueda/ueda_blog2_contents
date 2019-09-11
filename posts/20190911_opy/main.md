---
Keywords: opy, Python, ワンライナー, シェル芸
Copyright: (C) 2019 Ryuichi Ueda
---

# 自作コマンド（opy）をbrewとsnapに対応した 

## 要旨

　[この記事](/?post=20190908_opy)がそこそこ反響を呼んで調子に乗った上田は、`opy`（おーぴーわい or おーぱい。促音禁止）の普及を図るためにbrewとsnapに手を出した。

## homebrew

　ということで、まずはMacで簡単にインストールできるようにbrewに対応しました。こちらを参考にしました。

* https://qiita.com/masawada/items/484bbf83ef39cad7af74

結果、これでインストールできるようになりました。

```
$ brew tap ryuichiueda/oneliner-python
$ brew install oneliner-python
```

書いた設定はこんな感じです。

* https://github.com/ryuichiueda/homebrew-oneliner-python/blob/master/oneliner-python.rb

```
require "formula"

class OnelinerPython < Formula
  homepage "https://github.com/ryuichiueda/opy"
  url "https://github.com/ryuichiueda/opy/archive/v1.4.4.tar.gz"
  sha256 "f3ab839ff0e919bcf5764fb0a8eb69904d3eba2fa3eb4f19ebf60c464a782a73"
  head "https://github.com/ryuichiueda/opy.git"
  version "1.4.4"

  def install
    bin.install "opy"
    man1.install "opy.1" 
  end
end
```


　ついでに`chikubeam`(1)させていただきました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ちょwwwwwwwwwwwww<a href="https://t.co/tefTMSxY8U">https://t.co/tefTMSxY8U</a> <a href="https://t.co/4W6RdonQBm">pic.twitter.com/4W6RdonQBm</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1171012412448788480?ref_src=twsrc%5Etfw">September 9, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

とてもたのしい（とてもたのしい）。


## Snappy (snap)

　で、次にsnapに対応しました。deb作るの大変そうだし、こっちの方が新しいし・・・って手を出しましたがかなりつらかったです。

　snapのパッケージを作るときは、snapcraftというツールをインストールして、[次のようなyaml](https://github.com/ryuichiueda/opy-snap/blob/master/snap/snapcraft.yaml)を書いて、そこで`snapcraft`と打って作ります。`snapcraft`のやってることを見ていると、何かVMみたいなものを作ってそのなかに必要なツールをダウンロードしてビルドして、そのあと固めて`snap`という拡張子のファイルにするみたいです。

```
name: opy
version: 'latest'
summary: Onelinerers' Python, which works like AWK
description: |
  This command works like AWK in one liners. It enables you to use Python
  modules on CLI.
grade: stable
confinement: strict

apps:
  opy:
    command: opy

parts:
  opy:
    source: https://github.com/ryuichiueda/opy.git
    plugin: dump
    source-tag: master
    source-depth: 1
```

　ビルドがうまくいったら、Ubuntu Oneのアカウントで https://snapcraft.io にログインし、https://snapcraft.io/register-snap でパッケージの名前を予約して、

```
$ snap push --release=stable opy_latest_amd64.snap
```

とアップロードしました。これで、[こんなふうに](https://snapcraft.io/opy)パッケージがインターネッツ上にさらされました。あとは、任意のsnapが使える環境で、誰でも

```
$ sudo snap install opy
```

するとインストールできる状況になりました。



### ハマったところ

　細かい手順は書く時間がないので、ハマりポイントを書いておきます。最初はopyという図々しい名前でなく、oneliner-pythonという名前でパッケージを作っていました。ただ、これだとどんなに頑張ってもコマンド名が`oneliner-python.opy`とか`oneliner-python`にしかなりませんでした。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">snapのパッケージの作り方、だいたいわかったんだけど、コマンドをインストールしたら「&lt;パッケージ名&gt;.&lt;コマンド名&gt;」みたいになっちゃって、パッケージ名をどう除去するのかわからんという状況。</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1171438396733980674?ref_src=twsrc%5Etfw">September 10, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

どうやら名前がバッティングするのを避けるために、パッケージ名をくっつけるしかなさそう。

　一応、これはユーザの方で

```
$ sudo snap alias oneliner-python.opy opy
```

とすればよいようなのですが、これはこれで面倒なので、結局パッケージ名をopyにしました。

　また、オプションがいろいろ煩雑で、手元で試しにsnapファイルをインストールするときは、

```
$ sudo snap install opy_latest_amd64.snap --dangerous
```

というふうに`--dangerous`とオプションを加えなければいけませんが、よく忘れて時間を食いました。また、pushするときも`--release=stable`をつけないと、snap installできない状態になり、また同じsnapファイルをアップロードできなくなるので、これも時間を食いました。



　ちなみに、`https://snapcraft.io/opy`ではダウンロード数とかも閲覧できるみたいなので楽しみです。これでダウンロードが少ないと、先日のバズりが、「`opy`面白い！使ってみたい！」ではなく、「opyがお○ぱいだ！」という点でのものだったことになり、大変悲しいのでぜひsnapでインストールしてみてください。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">お、おっぱ……<br><br>Pythonをコマンドラインで使いたいのでopyというコマンドを作った | 上田ブログ <a href="https://t.co/eThANDMEV2">https://t.co/eThANDMEV2</a></p>&mdash; うむー (@umux_24) <a href="https://twitter.com/umux_24/status/1171235408497131521?ref_src=twsrc%5Etfw">September 10, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


違う！寝る。
