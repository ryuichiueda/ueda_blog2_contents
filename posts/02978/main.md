---
Keywords:コマンド,寝る,エクセル方眼紙もお任せ！,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# エクセルのワークシートを読み込むコマンド
<a href="https://github.com/ryuichiueda/ShellOfficeTools" target="_blank">https://github.com/ryuichiueda/ShellOfficeTools</a><br />
にエクセルのワークシートを読むコマンド「exread-sheet」を加えました。まだバグがあると思いますが。<br />
<br />
<!--more--><br />
<br />
思いっきりsed芸になってしまいました・・・<br />
<br />
[bash]<br />
#!/bin/bash<br />
<br />
usage () {<br />
	cat &lt;&lt;- FIN &gt;&amp;2<br />
	ExRead Sheet 1.0: read of an excel sheet<br />
	Wed Apr 23 23:34:39 JST 2014<br />
<br />
	Copyright (C) 2014 Ryuichi UEDA<br />
<br />
	usage: exread &lt;sheet&gt; original.xlsx<br />
	FIN<br />
<br />
	exit 1<br />
}<br />
<br />
[ &quot;$1&quot; = &quot;-h&quot; ] &amp;&amp; usage<br />
[ &quot;$1&quot; = &quot;--help&quot; ] &amp;&amp; usage<br />
<br />
unzip -p &quot;$2&quot; &quot;xl/worksheets/$1.xml&quot;		|<br />
grep -o '&lt;c [^&lt;]*&gt;[^v]*&lt;v&gt;[^&lt;]*&lt;/v&gt;&lt;/c&gt;'	|<br />
sed 's;&gt;&lt;f&gt;[^&lt;]*&lt;/f&gt;; t=&quot;n&quot;&gt;;'			|<br />
sed 's;&lt;c \\(r=&quot;[A-Z]*[0-9]*&quot;\\)&gt;;&lt;c \\1 t=&quot;n&quot;&gt;;'	|<br />
sed 's;^&lt;c ;;'					|<br />
sed 's;&lt;/v&gt;&lt;/c&gt;;;'				|<br />
sed 's;[frt]=;;g'				|<br />
sed 's;&gt;&lt;v&gt;; ;'					|<br />
tr -d '&quot;'					|<br />
sed 's/^[A-Z]*/&amp; /'<br />
<br />
exit 0<br />
#The MIT License<br />
#<br />
#Copyright (C) Ryuichi UEDA<br />
#<br />
#Permission is hereby granted, free of charge, to any person obtaining a copy<br />
#of this software and associated documentation files (the &quot;Software&quot;), to deal<br />
#in the Software without restriction, including without limitation the rights<br />
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell<br />
#copies of the Software, and to permit persons to whom the Software is<br />
#furnished to do so, subject to the following conditions:<br />
#<br />
#The above copyright notice and this permission notice shall be included in<br />
#all copies or substantial portions of the Software.<br />
#<br />
#THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR<br />
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,<br />
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE<br />
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER<br />
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,<br />
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN<br />
#THE SOFTWARE.<br />
[/bash]<br />
<br />
<br />
使ってみます。<br />
<br />
[bash]<br />
###昔の実験データ###<br />
uedambp:ShellOfficeTools ueda$ ./exread-sheet sheet1 ./results.xlsx | head<br />
A 1 s 0<br />
B 1 s 1<br />
C 1 s 0<br />
D 1 s 1<br />
E 1 s 0<br />
F 1 s 1<br />
A 2 n 175<br />
B 2 n 0<br />
C 2 n 172.352<br />
D 2 n 0<br />
###データの個数は8006個###<br />
uedambp:ShellOfficeTools ueda$ ./exread-sheet sheet1 ./results.xlsx | wc -l<br />
 8006<br />
###そこそこ速いです###<br />
uedambp:ShellOfficeTools ueda$ time ./exread-sheet sheet1 ./results.xlsx &gt; /dev/null <br />
<br />
real	0m0.099s<br />
user	0m0.230s<br />
sys	0m0.017s<br />
[/bash]<br />
<br />
セルと何のセルか「数値 or 文字列」、そして値（文字列の場合は文字列シートの参照番号）が入ってます。<br />
<br />
次は文字列の入ったxmlファイルを読み込むコマンドを作ります。<br />
<br />
<br />
寝る。ビールが空になったら。
