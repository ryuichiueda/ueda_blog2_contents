---
Keywords:未分類
Copyright: (C) 2017 Ryuichi Ueda
---
# GlueLangに標準入力を読みながら実行するループを実装
昨日の続きです。今日は大学で卒業に関するイベント等々があって酔っ払って帰ってきましたが、勢いで開発を進めました。<br />
<br />
今日は、bashの次のような処理を<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>に実装しました。<br />
<br />
[bash]<br />
###こんなスクリプト###<br />
$ cat hoge.bash <br />
#!/bin/bash<br />
<br />
seq 1 3 |<br />
while read a ; do<br />
	echo &quot;\@&quot; $a<br />
done<br />
###こんな出力###<br />
$ ./hoge.bash<br />
\@ 1<br />
\@ 2<br />
\@ 3<br />
[/bash]<br />
<br />
GlueLangだと次のようになります。標準入力から1行ごとに配列argvに文字列が読み込まれ、foreachの下に書いた処理が繰り返されます。<br />
<br />
[bash]<br />
###こんなスクリプト###<br />
$ cat hoge.glue <br />
import PATH<br />
<br />
seq 1 3 &gt;&gt;= foreach<br />
 echo '\@' argv[1]<br />
###こんな出力###<br />
$ glue ./hoge.glue <br />
\@ 1<br />
\@ 2<br />
\@ 3<br />
[/bash]<br />
<br />
<br />
こんな感じです。寝る。
