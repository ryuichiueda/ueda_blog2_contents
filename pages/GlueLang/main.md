---
Copyright: (C) Ryuichi Ueda
---

# GlueLang

[GlueLang](https://github.com/ryuichiueda/GlueLang)は、スクリプティングに特化したシェルです。

## 主な特徴（バージョン0.2.0）

たぶんピンと来ない人が多いと思われますが・・・

### 中間ファイルを変数のように扱える

```
#!/usr/local/bin/glue

import PATH            # PATHの下にあるコマンドを有効に

file nums = seq '1' '100'
file buzz = sed '5~5s/.*/Buzz/' nums

sed '3~3s/[0-9]*/Fizz/' buzz

# numsもbuzzも自動で消去される
```

### エラーを起こした場所が分かりやすい

次のようにわざとエラーを起こすコードを実行すると・・・

```
#!/usr/local/bin/glue

import PATH

file nums = seq '1' '100'
file buzz = se '5~5s/.*/Buzz/' nums   # sedをseに変更

sed '3~3s/[0-9]*/Fizz/' buzz

# numsもbuzzも自動で消去される
```

次のようにエラーの起きた位置を示してくれます。

```
$ ./fizzbuzz.glue
Parse error at line 6, char 13
	line6: file buzz = se '5~5s/.*/Buzz/' nums
	                   ^

	Command se not exist
	process_level 0
	exit_status 2
	pid 25881
ERROR: 2
```

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

### リンク

* リポジトリ: https://github.com/ryuichiueda/GlueLang
* マニュアル:
    - 日本語: https://ryuichiueda.github.io/GlueLangDoc_ja/
    - English: http://ryuichiueda.github.io/GlueLang/
* ブログ記事: [グルー言語を作る](https://b.ueda.tech/key.cgi?key=%E3%82%B0%E3%83%AB%E3%83%BC%E8%A8%80%E8%AA%9E%E3%82%92%E4%BD%9C%E3%82%8B)
