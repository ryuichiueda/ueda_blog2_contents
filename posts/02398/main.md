---
Keywords: xlsx,寝る,エクセル方眼紙もお任せ！,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Excelファイルをシェル芸でほじくる。ただしエクセル方眼紙は後日ということで。
追記：<a href="http://blog.ueda.asia/?p=2417" title="Excelファイルをシェル芸でほじくる。（hxselect編）" target="_blank">続編書きました</a><br />
<br />
だっこした子供が寝てしまってキーボードを叩くしかやることがない上田ですこんばんわ。<br />
<br />
最近エクセル方眼紙がブームです。シェル芸人としては便乗するしかありません。ちょっとエクセルのファイルに悪戯してみます。皆さんも手を動かしてみてください。<br />
<br />
<br />
<a href="スクリーンショット-2014-03-26-23.05.29.png"><img src="スクリーンショット-2014-03-26-23.05.29-279x300.png" alt="スクリーンショット 2014-03-26 23.05.29" width="279" height="300" class="aligncenter size-medium wp-image-2399" /></a><br />
<br />
まず上に挙げたエクセルファイルを用意して、book.xlsxと名前とつけます。セルにはとりあえず数字だけ書きましょう。文字列がある場合はまた後日。<br />
<br />
こんな風に適当なディレクトリに置いてください。<br />
<br />
[bash]<br />
uedambp:tmp ueda$ pwd<br />
/Users/ueda/tmp<br />
uedambp:tmp ueda$ ls <br />
book.xlsx<br />
[/bash]<br />
<br />
次にやるのは「解凍」です。実は.xlsxはzipファイルです。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
uedambp:tmp ueda$ unzip book.xlsx <br />
Archive: book.xlsx<br />
 inflating: [Content_Types].xml <br />
 inflating: _rels/.rels <br />
 inflating: xl/_rels/workbook.xml.rels <br />
 inflating: xl/workbook.xml <br />
 extracting: docProps/thumbnail.jpeg <br />
 inflating: xl/theme/theme1.xml <br />
 inflating: xl/styles.xml <br />
 inflating: xl/worksheets/sheet1.xml <br />
 inflating: docProps/core.xml <br />
 inflating: docProps/app.xml <br />
[/bash]<br />
<br />
解凍するとこんなディレクトリツリーが出現します。エロいですね。（何が？）<br />
<br />
[bash]<br />
uedambp:tmp ueda$ tree<br />
.<br />
├── [Content_Types].xml<br />
├── _rels<br />
├── book.xlsx<br />
├── docProps<br />
│   ├── app.xml<br />
│   ├── core.xml<br />
│   └── thumbnail.jpeg<br />
└── xl<br />
 ├── _rels<br />
 │   └── workbook.xml.rels<br />
 ├── styles.xml<br />
 ├── theme<br />
 │   └── theme1.xml<br />
 ├── workbook.xml<br />
 └── worksheets<br />
 └── sheet1.xml<br />
<br />
6 directories, 10 files<br />
[/bash]<br />
<br />
sheet1.xmlを見てみましょう。<br />
<br />
[bash]<br />
uedambp:tmp ueda$ cat xl/worksheets/sheet1.xml <br />
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;yes&quot;?&gt;<br />
&lt;worksheet <br />
xmlns=&quot;http://schemas.openxmlformats.org/spreadsheetml/2006/main&quot; <br />
xmlns:r=&quot;http://schemas.openxmlformats.org/officeDocument/2006/relations<br />
hips&quot; xmlns:mc=&quot;http://schemas.openxmlformats.org/markup-<br />
compatibility/2006&quot; mc:Ignorable=&quot;x14ac&quot; <br />
xmlns:x14ac=&quot;http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac&quot;<br />
&gt;&lt;dimension ref=&quot;A1:A4&quot;/&gt;&lt;sheetViews&gt;&lt;sheetView tabSelected=&quot;1&quot; <br />
workbookViewId=&quot;0&quot;&gt;&lt;selection activeCell=&quot;A5&quot; sqref=&quot;A5&quot;/&gt;&lt;/sheetView&gt;<br />
&lt;/sheetViews&gt;&lt;sheetFormatPr baseColWidth=&quot;12&quot; defaultRowHeight=&quot;18&quot; <br />
x14ac:dyDescent=&quot;0&quot;/&gt;&lt;sheetData&gt;&lt;row r=&quot;1&quot; spans=&quot;1:1&quot;&gt;&lt;c r=&quot;A1&quot;&gt;<br />
&lt;v&gt;1&lt;/v&gt;&lt;/c&gt;&lt;/row&gt;&lt;row r=&quot;2&quot; spans=&quot;1:1&quot;&gt;&lt;c r=&quot;A2&quot;&gt;&lt;v&gt;2&lt;/v&gt;&lt;/c&gt;&lt;/row&gt;<br />
&lt;row r=&quot;3&quot; spans=&quot;1:1&quot;&gt;&lt;c r=&quot;A3&quot;&gt;&lt;v&gt;3&lt;/v&gt;&lt;/c&gt;&lt;/row&gt;&lt;row r=&quot;4&quot; <br />
spans=&quot;1:1&quot;&gt;&lt;c r=&quot;A4&quot;&gt;&lt;v&gt;-4.2300000000000004&lt;/v&gt;&lt;/c&gt;&lt;/row&gt;&lt;/sheetData&gt;<br />
&lt;phoneticPr fontId=&quot;1&quot;/&gt;&lt;pageMargins left=&quot;0.7&quot; right=&quot;0.7&quot; top=&quot;0.75&quot; <br />
bottom=&quot;0.75&quot; header=&quot;0.3&quot; footer=&quot;0.3&quot;/&gt;&lt;extLst&gt;&lt;ext uri=&quot;{64002731-A6B0-<br />
56B0-2670-7721B7C09600}&quot; <br />
xmlns:mx=&quot;http://schemas.microsoft.com/office/mac/excel/2008/main&quot;&gt;<br />
&lt;mx:PLV Mode=&quot;0&quot; OnePage=&quot;0&quot; WScale=&quot;0&quot;/&gt;&lt;/ext&gt;&lt;/extLst&gt;<br />
&lt;/worksheet&gt;uedambp:tmp ueda$ <br />
[/bash]<br />
<br />
<del>嫌がらせ</del>容量の抑制のために改行ナッシングです。<br />
<br />
[ad#articleheader]<br />
<br />
数字はcという名前の要素に入っています。抽出してみましょう。POSIXにうるさい方々には叱られそうですが・・・。<br />
<br />
[bash]<br />
uedambp:tmp ueda$ cat xl/worksheets/sheet1.xml |<br />
 grep -o '&lt;c [^&lt;]*&gt;&lt;v&gt;[^&lt;]*&lt;/v&gt;&lt;/c&gt;'<br />
&lt;c r=&quot;A1&quot;&gt;&lt;v&gt;1&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A2&quot;&gt;&lt;v&gt;2&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A3&quot;&gt;&lt;v&gt;3&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A4&quot;&gt;&lt;v&gt;-4.2300000000000004&lt;/v&gt;&lt;/c&gt;<br />
[/bash]<br />
<br />
あとは余計な記号を除去してセルの番号と数字を取り出します。<br />
<br />
[bash]<br />
uedambp:tmp ueda$ cat xl/worksheets/sheet1.xml |<br />
 grep -o '&lt;c [^&lt;]*&gt;&lt;v&gt;[^&lt;]*&lt;/v&gt;&lt;/c&gt;' | tr '&gt;&lt;&quot;' ' ' | awk '{print $3,$5}'<br />
A1 1<br />
A2 2<br />
A3 3<br />
A4 -4.2300000000000004<br />
[/bash]<br />
<br />
ぜひやってみてください。案外使える技かもしれません。<br />
<br />
文字列や数式が入っている場合についてはまた後日。<br />
<br />
<br />
寝る。
