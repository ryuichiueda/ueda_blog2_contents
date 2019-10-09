---
Copyright: (C) Ryuichi Ueda
---

# the opy book

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

## 2. 検索

　opyは、AWKのように`grep`の拡張版として利用することができます。たとえば、次の例は`seq 5`の結果から偶数の行を検索するものです。

```
$ seq 5
1
2
3
4
5
$ seq 5 | opy 'F1%2==0'
2
4
```

ここで、`F1`は「（各行の）1列目」を表します。`opy`は標準入力から行を読み込むと、空白を見つけて自動で分割し、`F1, F2, ...`という変数に割り当てます。詳細は後述します。


