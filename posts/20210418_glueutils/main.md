---
Keywords: glueutils, GlueLang
Copyright: (C) 2021 Ryuichi Ueda
---

# glueutilsについて

この前から[glueutils](https://github.com/ryuichiueda/glueutils)という怪しげなコマンドパッケージを作っているのですが、解説を書いておこうと思います。

## なにをするパッケージか

標準入出力のリダイレクトなど、シェルでやるような処理をコマンドだけで可能にするためのパッケージ群です。

## なにが嬉しいか

* リダイレクト処理が貧弱なシェル（私の作ってる[GlueLang](/?page=GlueLang)など）でもリダイレクトが可能（もともとこの用途で作成してます。）
* シェルで`2>&1`とか`> /dev/null`とかリダイレクトを書くとゴチャゴチャするので、ゴチャゴチャしない方法を提供
