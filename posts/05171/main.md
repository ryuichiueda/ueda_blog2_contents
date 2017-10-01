---
Keywords: コマンド,CLI,grep,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】第15回ドキッ！grepだらけのシェル芸勉強会
<h1>イントロのスライド</h1>

<iframe src="//www.slideshare.net/slideshow/embed_code/44124362" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150201-15grep" title="20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）" target="_blank">20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h1>諸注意</h1>

解答はUbuntu Linux 14.04で作成しました。コマンドがないときは適宜インストールのほど。

Macな人はbrewでGNU grep（ggrep）をインストールすると良かれ悪しかれ拡張オプションが使えます。インストール方法は例えばこちらが分かりやすいかと。3行で済みます。

<iframe marginwidth="0" marginheight="0" src="http://b.hatena.ne.jp/entry.parts?url=http%3A%2F%2Fqiita.com%2Fquattro_4%2Fitems%2Fe75f2b4156ef45fb6640" scrolling="no" frameborder="0" height="230" width="500"><div class="hatena-bookmark-detail-info"><a href="http://qiita.com/quattro_4/items/e75f2b4156ef45fb6640">高速化したGNU grepをインストールする - Qiita</a><a href="http://b.hatena.ne.jp/entry/qiita.com/quattro_4/items/e75f2b4156ef45fb6640">はてなブックマーク - 高速化したGNU grepをインストールする - Qiita</a></div></iframe>

<!--more-->

<h1>Q1</h1>

次のようにファイルを作ります。

```bash
$ seq 2 5 > a
$ seq 1 9 > b
$ seq 5 11 > c
$ seq 3 6 > d
```

1という文字を含まないファイルを列挙してください（aとdですね）。

<h1>Q2</h1>

作業ディレクトリを作り、その下に次のようにfile.1〜file.10000というファイルを作ります。

```bash
$ seq 1 10000 | xargs -I@ touch file.@
```

以下の数字を持つファイルだけ残して後のファイルを消去してください。

<ul>
 <li>1〜9</li>
 <li>10, 20, 30, ..., 90</li>
 <li>数字の下2桁が0のファイル</li>
</ul>


<h1>Q3</h1>

次のテキストから、「-v」、「-f」、「awk」の数をカウントしてください。gawk、nawkは避けてください（awkの数としてカウントしない）。できる人はgrepは1個で。さらにできる人は拡張正規表現を使わないでやってみましょう。


```bash
$ cat text1 
awk -v v="hoge" 'BEGIN{print v}'
echo 'BEGIN{print 1}' | gawk -f -
nawk 'BEGIN{print " BEGIN{print x}"}' | awk -v x=3 -f -
```


<h1>Q4</h1>

/etc/の下（子、孫、・・・）のファイルのうち、シバンが「#!/bin/sh」のシェルスクリプトについて、中に「set -e」と記述のあるファイルとないファイルの数をそれぞれ数えてください。（コメント中のset -eも数えてOKです。）


<h1>Q5</h1>

日本語やギリシャ文字のある行を除去してください。

```bash
$ cat text2 
A pen is a pen?
日本語でおk
ΩΩπ<Ω< na nandatte!!
Randy W. Bass
env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
#危険シェル芸
```


<h1>Q6</h1>

次のようにファイルa, b, cを作ります。

```bash
$ echo 1 2 3 4 > a
$ echo 2 3 4 5 > b
$ echo 1 4 5 > c
```

ファイルの中の数字を足して10になるファイルを挙げてください。

<h1>Q7</h1>

psコマンドを打って（オプションは任意）、そのpsコマンドの行、親プロセスの行、親の親のプロセスの行を表示してみてください。

<h1>Q8</h1>

seqとfactorの出力の後ろにgrepだけをいくつかつなげて、「素数の一つ前の数で、かつ10以上の数」を列挙してください。

```bash
$ seq 10 1000 | factor | ...(grepだけ)
```

