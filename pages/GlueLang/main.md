---
Copyright: (C) Ryuichi Ueda
---

# GlueLang

GlueLangは、スクリプティングに特化したシェルです。

* リポジトリ: https://github.com/ryuichiueda/GlueLang
* マニュアル:
    - 日本語: https://ryuichiueda.github.io/GlueLangDoc_ja/
    - English: http://ryuichiueda.github.io/GlueLang/
* ブログ記事: [グルー言語を作る](https://b.ueda.tech/key.cgi?key=%E3%82%B0%E3%83%AB%E3%83%BC%E8%A8%80%E8%AA%9E%E3%82%92%E4%BD%9C%E3%82%8B)

## 主な特徴（バージョン0.2.0）

たぶんピンと来ない人が多いと思われますが・・・

### パイプの記号が>>=なので目立つ 

* bashのコード: `hoge.bash`

```
#!/bin/bash
echo abc | rev | grep -o .
```

* glueのコード

```
#!/usr/local/bin/glue

import PATH
echo 'abc' >>= rev >>= grep '-o' '.'
```

* 実行結果

```
$ ./hoge.bash
c
b
a
$ ./hoge.glue
c
b
a
```
