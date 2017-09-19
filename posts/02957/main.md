---
Keywords: コマンド,シェルスクリプト,わーどうしましょう,CLI,エクシェル芸,ワードシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Word（docx）用sedを改良してしもうた。
<a href="http://blog.ueda.asia/?p=2931" title="Word（docx）用sedを作ってしもうた。">昨日</a>からの続編です。Word版sedを作る話。

やっぱりsedはsedらしくということで、


<ul>
<li>標準入力からファイルを読む</li>
<li>sedのコマンドがそのまま使えるようにする</li>
</ul>

というように改変しました。<a href="https://github.com/ryuichiueda/ShellOfficeTools" target="_blank">https://github.com/ryuichiueda/ShellOfficeTools</a>で公開しております。


<!--more-->

あと、コマンドらしくヘルプを追加したりtrapをしかけたり。

こんな感じです。
[bash]
###標準入力からdocxを受ける###
server:ShellOfficeTools ueda$ cat ~/Desktop/letter.docx |
 ./wordsed 's/\@\@*/ボケ/g' &gt; out.docx
###へるぷを出す###
server:ShellOfficeTools ueda$ ./wordsed -h
WordSed 1.0: a string replacement tool for docx
Wed Apr 23 19:24:28 JST 2014

Copyright (C) 2014 Ryuichi UEDA

usage1: cat original.docx | wordsed &lt;sed command&gt; &gt; newfile.docx
usage2: wordsed &lt;sed command&gt; original.docx &gt; newfile.docx
[/bash]

試してませんが多段でパイプに繋ぐことも可能となりました。

ということで、お役立てください。
