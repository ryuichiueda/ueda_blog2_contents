---
Keywords: 自作シェル,rusty_bash,寿司シェル
Copyright: (C) 2025 Ryuichi Ueda
---

# 自作シェルの進捗（2025年3月29日）

　なんか春休みで研究そっちのけで自作シェル（[rusty_bash、sush、寿司シェルといろんな呼び名で呼ばれているやつ](https://github.com/shellgei/rusty_bash/)）を開発してます。（研究以外の仕事はちゃんとやってますねんのため。）

　最近はポツポツと海外からのissueが来てます。Bashみたいなデカいシェルをほぼスクラッチ状態から作るのは手分けしたとしても時間がかかるので、たぶんそんなアホなことやってる人は地球上でそんなにおらんだろうと思います。

## Bashの公式リポジトリのテスト

　海外から「ちゃんと公式のテストを使え。グラフも描け」と言われで、対応しました。

* これ: https://github.com/shellgei/rusty_bash/issues/124#issue-2888738573

Bashの公式リポジトリは[ココ](https://savannah.gnu.org/git/?group=bash)にありますが、そのリポジトリの中に`tests`というディレクトリがあり、そのなかにテストスクリプトが入ってます。使い方はこんな感じ。（手練れ向けで、細かいトラップまで考慮してないのでご容赦ください。）

1. リポジトリのなかで`./configure`して`make`
2. 最新のUbuntuだと一箇所「ヘッダファイルが明示的に指定されていない」とエラーが出るので修正
3. `make test`あるいは`tests`のなかで、`THIS_SH=<テストしたいシェル> ./hogehoge.test`を実行

みなさんも手持ちの自作シェルで試してみてください（？）

　で、このリポジトリをフォークして、[自作シェルのテスト用のリポジトリ](https://github.com/ryuichiueda/bash_for_sush_test)を作りました。このなかの`sush_test`というディレクトリのなかに、Bashと自作シェルを比較するためのシェルスクリプトと、gnuplotでグラフを描くシェルスクリプトを置きました。本日時点でのグラフはこんな感じです。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">本日の進捗 <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://t.co/lkv4e6JcZd">pic.twitter.com/lkv4e6JcZd</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1905883207775744183?ref_src=twsrc%5Etfw">March 29, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

各折れ線グラフは

* `PASSED`: 全84のテストスクリプト中でBashと違いが出なかったものの数
* `NOT PASSED`: `bash`と`sush`で違いが出たスクリプトの数
* `DNF`: 途中で止まったスクリプトの数（面倒なので`NOT PASSED`には入れてません）
* `TOTAL LINES of DIFF`: 全スクリプトに対して`bash`の出力と`sush`の出力を`diff`で比較したときの`diff`の出力の行数

を表してます。`TOTAL...`の行数が減っていたり、`PASSED`の数が増えていたりすれば、「上田研究さぼってるなあ」ということになります。グラフは[自作シェルのリポジトリのトップページ](https://github.com/shellgei/rusty_bash/)に掲載していますので、毎日気にしていただけると幸いです。


　`sush_test`の中身は、最初`rusty_bash`のリポジトリの中に置いていました。しかしこれだと、これだとあるブランチでテストをした結果を`main`ブランチのREADMEに反映するのがめちゃくちゃ面倒なので、分けました。

## グラフを描いた結果・・・

　更新するのが楽しいのでつい開発してしまい、冒頭のように研究そっちのけになってます。いかん。

　最後に宣伝ですが、[Software Design](https://www.amazon.co.jp/shop/ryuichiueda/list/7MLC9JANITU0?ref_=aipsflist)で3年にわたって連載している「魅惑の自作シェルの世界」もよろしくおねがいしまーす。


　余力があれば今日中に技術面での話も書きます。

