---
Keywords: 未分類
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangに標準入力を読みながら実行するループを実装
昨日の続きです。今日は大学で卒業に関するイベント等々があって酔っ払って帰ってきましたが、勢いで開発を進めました。

今日は、bashの次のような処理を<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>に実装しました。

```bash
###こんなスクリプト###
$ cat hoge.bash 
#!/bin/bash

seq 1 3 |
while read a ; do
	echo &quot;\@&quot; $a
done
###こんな出力###
$ ./hoge.bash
\@ 1
\@ 2
\@ 3
```

GlueLangだと次のようになります。標準入力から1行ごとに配列argvに文字列が読み込まれ、foreachの下に書いた処理が繰り返されます。

```bash
###こんなスクリプト###
$ cat hoge.glue 
import PATH

seq 1 3 &gt;&gt;= foreach
 echo '\@' argv[1]
###こんな出力###
$ glue ./hoge.glue 
\@ 1
\@ 2
\@ 3
```


こんな感じです。寝る。
