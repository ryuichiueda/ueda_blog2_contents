---
Copyright: (C) Ryuichi Ueda
---

# the opy book

* [目次に戻る](/?page=opy_book)

* [1. はじめに](/?page=opy_intro)

## 1. はじめに

　opy（オーピーワイ、あるいはオーパイ）は、ワンライナーでPythonを使うためのラッパーコマンドです。Pythonワンライナーで面倒となるテキストの読み込み処理などを暗黙理に行うほか、代表的な行指向言語であるAWKの「パターン/アクション」を取り入れることで、Pythonの文法やライブラリを使った簡潔なワンライナーを書くことを可能にしました。

　このドキュメントは、opyについて網羅的に書いた入門書になることを目指しているものです。まだ書きかけですが、現時点では唯一の入門書です。

### 1.1 opyを立ち上げる

　opyは、リポジトリ https://github.com/ryuichiueda/opy に置いてあります。インストール方法はこのリポジトリの`README.md`に書いてあります。

　opyをインストールしたら、`opy`と打ってみましょう。


```
opy 1.9.3

Copyright 2019 Ryuichi Ueda
Released under MIT license
https://github.com/ryuichiueda/opy

You are using Python 3.7.4 with this command.
```

このようにopyのバージョンやコピーライト、ライセンスの情報が出力されます。また、opyはPythonのラッパーなので、出力の最下行のように、Pythonのバージョンも出力されます。これにより、どのバージョンのPythonの文法や機能が利用できるかを把握できます。


　次に、お約束のHello worldを出力してみましょう。次のように様々な方法がありますが、詳細の説明は次章以降にします。

```
$ echo Hello world | opy '[F0]'
Hello world
$ echo Hello world | opy '[F1,F2]'
Hello world
$ echo Hello world | opy '{print(F0)}'
Hello world
$ opy 'B:["Hello world"]'
Hello world
```

