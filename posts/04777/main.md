---
Keywords:GlueLang,研究,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---
# GlueLangに中間ファイルを変数のように使える機能を実装
<a href="http://blog.ueda.asia/?p=4719" title="煽られるように開発中の言語（Glue）について説明・・・">GlueLangの開発</a>は休日に行うことにした上田です。おこんばんは。<br />
<br />
GlueLangというのは、「次世代シェルスクリプティング言語」と勝手に銘打って勝手に作っている素敵なサムシングです。<a target="_blank" href="https://github.com/ryuichiueda/GlueLang">リポジトリはこちら。</a><br />
<br />
<!--more--><br />
<br />
現在、一行にー個コマンドを書いていくと順に実行できるようになっています。パイプはまだ使えません。FizzBuzzのコードを例として示しておきます。あ、コードは<a target="_blank" href="https://github.com/ryuichiueda/GlueLang">ココ</a>にあります。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ cat TEST/fizzbuzz.glue <br />
# for Mac<br />
<br />
file nums = /usr/bin/seq '1' '100'<br />
<br />
#gsed can be installed by &quot;brew install coreutils&quot;<br />
file buzz = /usr/local/bin/gsed '5~5s/.*/Buzz/' nums<br />
<br />
#output<br />
/usr/local/bin/gsed '3~3s/[0-9]*/Fizz/' buzz<br />
[/bash]<br />
<br />
ちゃんと動きます。<br />
<br />
[bash]<br />
uedambp:GlueLang ueda$ ./main TEST/fizzbuzz.glue | head -n 5<br />
1<br />
2<br />
Fizz<br />
4<br />
Buzz<br />
[/bash]<br />
<br />
Glueのコードを見てのとおり、パスを通してなく見づらくてすいません。その代わり、「file nums」というように、変数のように中間ファイルが使えるところまで実装できました。Glueではベタにファイル変数と呼ぶことにします。<br />
<br />
今のところ、Ctrl+Cだと消えませんが、プログラムが終わるときにファイル変数に結び付けられたファイルを削除するところまで実装しました。<br />
<br />
その他、現在の仕様では文字列はシングルクォート、変数はクォートなしにして識別することにしました。仕様を頭の中でいろいろ考えているうちに、$マークは無くす方針になってきました。あまり好きではありませんので。<br />
<br />
<h2>メモ</h2><br />
<br />
<h3>to do</h3><br />
次はパイプとimportの実装。それが終わったらエラーの際のメッセージを詳細にするのと、仕様についてドキュメントを書くのが先。<br />
<br />
<h3>雑感</h3><br />
<br />
stl便利。<br />
<br />
<h3>その他</h3><br />
<br />
Mac環境のテストは自分のマシン、Linux環境のテストは<a href="https://travis-ci.org/ryuichiueda/GlueLang" target="_blank">Travis CI</a>でやっている。
