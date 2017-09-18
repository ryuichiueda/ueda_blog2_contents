---
Keywords:コマンド,シェルスクリプト,わーどうしましょう,CLI,エクシェル芸,ワードシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---
# Word（docx）用sedを改良してしもうた。
<a href="http://blog.ueda.asia/?p=2931" title="Word（docx）用sedを作ってしもうた。">昨日</a>からの続編です。Word版sedを作る話。<br />
<br />
やっぱりsedはsedらしくということで、<br />
<br />
<br />
<ul><br />
<li>標準入力からファイルを読む</li><br />
<li>sedのコマンドがそのまま使えるようにする</li><br />
</ul><br />
<br />
というように改変しました。<a href="https://github.com/ryuichiueda/ShellOfficeTools" target="_blank">https://github.com/ryuichiueda/ShellOfficeTools</a>で公開しております。<br />
<br />
<br />
<!--more--><br />
<br />
あと、コマンドらしくヘルプを追加したりtrapをしかけたり。<br />
<br />
こんな感じです。<br />
[bash]<br />
###標準入力からdocxを受ける###<br />
server:ShellOfficeTools ueda$ cat ~/Desktop/letter.docx |<br />
 ./wordsed 's/\@\@*/ボケ/g' &gt; out.docx<br />
###へるぷを出す###<br />
server:ShellOfficeTools ueda$ ./wordsed -h<br />
WordSed 1.0: a string replacement tool for docx<br />
Wed Apr 23 19:24:28 JST 2014<br />
<br />
Copyright (C) 2014 Ryuichi UEDA<br />
<br />
usage1: cat original.docx | wordsed &lt;sed command&gt; &gt; newfile.docx<br />
usage2: wordsed &lt;sed command&gt; original.docx &gt; newfile.docx<br />
[/bash]<br />
<br />
試してませんが多段でパイプに繋ぐことも可能となりました。<br />
<br />
ということで、お役立てください。
