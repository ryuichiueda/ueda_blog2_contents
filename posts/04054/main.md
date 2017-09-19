---
Keywords: テスト,コマンド,シェルスクリプト,Travis,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# Open usp TukubaiのテストをTravis CIでやってみた
bash騒ぎが収まってない中ではありますが、とある役得で<a href="https://travis-ci.org/" target="_blank">Travis CI</a>の使い方を覚えたので<a href="https://github.com/ryuichiueda/Open-usp-Tukubai" target="_blank">Open usp Tukubaiを自分のGitHubにフォークして</a>使ってみました。

シェルスクリプトでテストスクリプトを書いている人って少ないかもしれませんが、シェルスクリプトでテストスクリプトを書いている人には簡単に使えます。というわけでテストはシェルスクリプトで書きましょう。bashを使うかどうかは・・・ご自身でご判断をorz。

<h2>前提</h2>

こんな状況です。

<ul>
 <li>Pythonで作ったOpen usp Tukubaiコマンドのテストをしたい。（なぜPythonなのかは聞かないでほしい）</li>
 <li>テストはシェルスクリプトで書いてある（<a href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/master/TEST" target="_blank">テストスクリプトのディレクトリ</a>）。各コマンドに対してテストのスクリプトがあり、このテストスクリプトの終了ステータスが0であることを以てテストにパスしたとする。（例: <a href="https://github.com/ryuichiueda/Open-usp-Tukubai/blob/master/TEST/self.test" target="_blank">self.test</a>）</li>
 <li>いつもは開発マシン（FreeBSD）で、<a href="https://github.com/ryuichiueda/Open-usp-Tukubai/blob/master/TEST/regress.all" target="_blank">regress.all</a>を叩いてテストしている。（Haskell版は今回はテストしない。）</li>
 <li>Travis CIのアカウントを持っている。</li>
</ul>

<h2>サインインからリポジトリの連携までの設定</h2>

私が書くよりこちらがご参考なるかと・・・。<a href="http://sue445.hatenablog.com/entry/2013/06/01/170607" target="_blank">http://sue445.hatenablog.com/entry/2013/06/01/170607</a>

<h2>テスト方法の設定</h2>

リポジトリの下に.travis.ymlを作って、何をどうテストするか書きます。こんな感じです。使いたいPythonのバージョンを指定して、テストスクリプトをshで呼び出すだけです。

[ruby]
language: python
python:
 - &quot;2.7&quot;
 - &quot;2.6&quot;
script: 
 - sh -e ./TEST/test.at.travis
[/ruby]

Travis CIのために書いたテストはこちら。regress.allでは各Pythonのバージョンでの調査手続きが入っていましたが、それが不要なので新たに書き直しました。ただただ、各コマンドのテストスクリプトを順に並べただけです。for文使えとか言われるかもしれませんが、for使うくらいならベタに並べた方がよいというUSP流に従います。今の今だと、for文使ってないことよりもbashが並んでいることの方が刺激的かもしれませんが。

[bash]
uedambp:Open-usp-Tukubai ueda$ head TEST/test.at.travis 
PATH=$PATH:./COMMANDS

bash ./TEST/calclock.test COMMANDS &quot;&quot;
bash ./TEST/cjoin0.test COMMANDS &quot;&quot;
bash ./TEST/cjoin1.test COMMANDS &quot;&quot;
bash ./TEST/cjoin2.test COMMANDS &quot;&quot;
bash ./TEST/ctail.test COMMANDS &quot;&quot;
bash ./TEST/count.test COMMANDS &quot;&quot;
bash ./TEST/getlast.test COMMANDS &quot;&quot;
bash ./TEST/getfirst.test COMMANDS &quot;&quot;
###以後ひたすらベタにコマンドが並ぶ###
[/bash]

.travis.ymlでshに-eを指定しているので、並べたスクリプトのどれかがコケたら終了してテスト失敗と相成ります。1行目はテスト内でOpen usp Tukubaiを使うので、それのパス通しです。ディレクトリは、とりあえずリポジトリのディレクトリがカレントディレクトリとなるようです。

んでまあ最後に、READMEに

<img src="https://travis-ci.org/ryuichiueda/Open-usp-Tukubai.svg?branch=master" />

ボタンを貼り付けるために、READMEに拡張子.mdを加えて、Travisの画面の右上にある上のボタンをクリックしてコードをコピーし、貼付けました。

テスト結果は、<a href="https://travis-ci.org/ryuichiueda/Open-usp-Tukubai" target="_blank">https://travis-ci.org/ryuichiueda/Open-usp-Tukubai</a>の通りです。ログにエラーと出ていますが、これはエラーが出る事を確認するためのテストを行った結果のログなので問題ありません。各コマンドのテストスクリプトは（1個バグがあって直したものの）修正なしで使えました。しかも最初からsh（bash？）とbashが使えるので、.travis.ymlでshでシェルスクリプトを起動する設定を書いておけば他の設定は不要です。

これでMacでもLinux上でもバージョン違いのPythonでテストできるようになったので、私としては便利だなと。このままデプロイまでやればおもしろんですが、これはコマンドなのでデプロイはありません。これで地味に終了です。

<h2>まとめ</h2>

私のようにテストをシェルスクリプトで書く人間には有り難いサービスです。各コマンドのテストスクリプトは手直し無しで使えました。

もうちょっと調べなければいかんのはシバンの使い方で、/usr/local/bin/bashが通らなかったので、今回は使いませんでした。たぶん/bin/bashですかね。


bashのテストもこれ使えばいいのになんて考えましたが、アレのテストを気づくのに人類は20年かかってますので、便利なサービスを使えばよいというものではないでしょう。

寝る。

