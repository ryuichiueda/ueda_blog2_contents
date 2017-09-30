---
Keywords: GlueLang,研究,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangに中間ファイルを変数のように使える機能を実装
<a href="/?post=04719" title="煽られるように開発中の言語（Glue）について説明・・・">GlueLangの開発</a>は休日に行うことにした上田です。おこんばんは。

GlueLangというのは、「次世代シェルスクリプティング言語」と勝手に銘打って勝手に作っている素敵なサムシングです。<a target="_blank" href="https://github.com/ryuichiueda/GlueLang">リポジトリはこちら。</a>

<!--more-->

現在、一行にー個コマンドを書いていくと順に実行できるようになっています。パイプはまだ使えません。FizzBuzzのコードを例として示しておきます。あ、コードは<a target="_blank" href="https://github.com/ryuichiueda/GlueLang">ココ</a>にあります。

```bash
uedambp:GlueLang ueda$ cat TEST/fizzbuzz.glue 

# for Mac

file nums = /usr/bin/seq '1' '100'

#gsed can be installed by "brew install coreutils"
file buzz = /usr/local/bin/gsed '5~5s/.*/Buzz/' nums

#output
/usr/local/bin/gsed '3~3s/[0-9]*/Fizz/' buzz
```

ちゃんと動きます。

```bash
uedambp:GlueLang ueda$ ./main TEST/fizzbuzz.glue | head -n 5
1
2
Fizz
4
Buzz
```

Glueのコードを見てのとおり、パスを通してなく見づらくてすいません。その代わり、「file nums」というように、変数のように中間ファイルが使えるところまで実装できました。Glueではベタにファイル変数と呼ぶことにします。

今のところ、Ctrl+Cだと消えませんが、プログラムが終わるときにファイル変数に結び付けられたファイルを削除するところまで実装しました。

その他、現在の仕様では文字列はシングルクォート、変数はクォートなしにして識別することにしました。仕様を頭の中でいろいろ考えているうちに、$マークは無くす方針になってきました。あまり好きではありませんので。

<h2>メモ</h2>

<h3>to do</h3>
次はパイプとimportの実装。それが終わったらエラーの際のメッセージを詳細にするのと、仕様についてドキュメントを書くのが先。

<h3>雑感</h3>

stl便利。

<h3>その他</h3>

Mac環境のテストは自分のマシン、Linux環境のテストは<a href="https://travis-ci.org/ryuichiueda/GlueLang" target="_blank">Travis CI</a>でやっている。
