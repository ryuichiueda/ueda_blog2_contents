---
Keywords: 勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第25回もう4年もやってんのかシェル芸勉強会
<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.25</a>

にあります。ただ、今回は1つしかファイルがありません。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はUbuntu Linux 16.04で解答例を作りました。
<h2>Q1</h2>
www.usptomo.comのIPアドレスだけを出力するワンライナーを考えてみてください。
<h2>Q2</h2>
次のような出力を作ってください。（<a href="http://togetter.com/li/1041621" target="_blank">出典</a>）

```bash
ひらけ！ポンキッキ
らけ！ポンキッキひ
け！ポンキッキひら
！ポンキッキひらけ
ポンキッキひらけ！
ンキッキひらけ！ポ
キッキひらけ！ポン
ッキひらけ！ポンキ
キひらけ！ポンキッ
```

<h2>Q3</h2>
rbashと打つとリダイレクトが使えなくなります。

この状況で、/etc/passwdからbashをログインシェルにしているユーザのレコードを抽出し、hoge等のファイルに出力してみましょう。様々な方法を考えてみましょう。bashと打ったりexitでもとのbashに戻るのは反則とします。
<h2>Q4</h2>
以下のひらがなからワンライナーを始めて、濁点がつく字だけに濁点をつけてみてください。

```bash
$ echo すけふぇにんけん
```

<h2>Q5</h2>
1秒に一つ*が伸びていくアニメーションを作ってください。

[playlist type="video" ids="8740"]
<h2>Q6</h2>
日本語のメッセージから作った次の文字列を復元してください。

```bash
$ cat crypt 
b730a730eb30b8820a00
```

<h2>Q7</h2>
本日（2016年10月29日）の範囲の毎秒のUNIX時刻で素数となるものを全て列挙してください。出力はUNIX時刻でなく、何時何分何秒か分かるようにしましょう。世界標準時で考えてください。
<h2>Q8</h2>
次のようにサイン波を描いてください。

<a href="b466fc6a3025fb4e2d7d3b98eea47814.png"><img class="aligncenter size-large wp-image-8754" src="b466fc6a3025fb4e2d7d3b98eea47814-1024x871.png" alt="%e3%82%b9%e3%82%af%e3%83%aa%e3%83%bc%e3%83%b3%e3%82%b7%e3%83%a7%e3%83%83%e3%83%88-2016-10-27-21-04-17" width="660" height="561" /></a>
