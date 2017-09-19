---
Keywords: コマンド,寝る,エクセル方眼紙もお任せ！,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# エクセルのワークシートを読み込むコマンド
<a href="https://github.com/ryuichiueda/ShellOfficeTools" target="_blank">https://github.com/ryuichiueda/ShellOfficeTools</a>
にエクセルのワークシートを読むコマンド「exread-sheet」を加えました。まだバグがあると思いますが。

<!--more-->

思いっきりsed芸になってしまいました・・・

```bash
#!/bin/bash

usage () {
	cat &lt;&lt;- FIN &gt;&amp;2
	ExRead Sheet 1.0: read of an excel sheet
	Wed Apr 23 23:34:39 JST 2014

	Copyright (C) 2014 Ryuichi UEDA

	usage: exread &lt;sheet&gt; original.xlsx
	FIN

	exit 1
}

[ &quot;$1&quot; = &quot;-h&quot; ] &amp;&amp; usage
[ &quot;$1&quot; = &quot;--help&quot; ] &amp;&amp; usage

unzip -p &quot;$2&quot; &quot;xl/worksheets/$1.xml&quot;		|
grep -o '&lt;c [^&lt;]*&gt;[^v]*&lt;v&gt;[^&lt;]*&lt;/v&gt;&lt;/c&gt;'	|
sed 's;&gt;&lt;f&gt;[^&lt;]*&lt;/f&gt;; t=&quot;n&quot;&gt;;'			|
sed 's;&lt;c \\(r=&quot;[A-Z]*[0-9]*&quot;\\)&gt;;&lt;c \\1 t=&quot;n&quot;&gt;;'	|
sed 's;^&lt;c ;;'					|
sed 's;&lt;/v&gt;&lt;/c&gt;;;'				|
sed 's;[frt]=;;g'				|
sed 's;&gt;&lt;v&gt;; ;'					|
tr -d '&quot;'					|
sed 's/^[A-Z]*/&amp; /'

exit 0
#The MIT License
#
#Copyright (C) Ryuichi UEDA
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the &quot;Software&quot;), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
```


使ってみます。

```bash
###昔の実験データ###
uedambp:ShellOfficeTools ueda$ ./exread-sheet sheet1 ./results.xlsx | head
A 1 s 0
B 1 s 1
C 1 s 0
D 1 s 1
E 1 s 0
F 1 s 1
A 2 n 175
B 2 n 0
C 2 n 172.352
D 2 n 0
###データの個数は8006個###
uedambp:ShellOfficeTools ueda$ ./exread-sheet sheet1 ./results.xlsx | wc -l
 8006
###そこそこ速いです###
uedambp:ShellOfficeTools ueda$ time ./exread-sheet sheet1 ./results.xlsx &gt; /dev/null 

real	0m0.099s
user	0m0.230s
sys	0m0.017s
```

セルと何のセルか「数値 or 文字列」、そして値（文字列の場合は文字列シートの参照番号）が入ってます。

次は文字列の入ったxmlファイルを読み込むコマンドを作ります。


寝る。ビールが空になったら。
