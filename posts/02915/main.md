---
Keywords: エクセル,CLI,Excel,エクセル方眼紙はこうやって処理する,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# unzip -p で真のエクシェル芸が完成したような気がする。
なんでこんなに眠いのか。

地味に好評な<a href="http://blog.ueda.asia/?p=2415" target="_blank">エクシェル芸</a>ですが、肝心なことを忘れていました。

これまでのブログの記事では、エクセルを一旦解凍していましたが、unzipの-pを使うとその必要はありません。こんな感じにxlsxから標準出力にダイレクトにxmlを流すことができます。unzip -pの後にzipファイル（この場合はエクセルファイル）、その次にzipの中の見たいファイルを指定します。最初のシートなら大抵xl/worksheets/sheet1.xmlを指定すればよいことになります。

<!--more-->

```bash
ueda\@remote:~$ unzip -p book1.xlsx xl/worksheets/sheet1.xml 
<?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;yes&quot;?&gt;
<worksheet xmlns=&quot;http://schemas.openxmlformats.org/spreadsheetml/2006/main&quot; 
xmlns:r=&quot;http://schemas.openxmlformats.org/officeDocument/2006/relationshi
ps&quot; xmlns:mc=&quot;http://schemas.openxmlformats.org/markup-compatibility/2006&quot;
 mc:Ignorable=&quot;x14ac&quot; 
xmlns:x14ac=&quot;http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac&quot;&gt;
<dimension ref=&quot;A1:A4&quot;/&gt;<sheetViews&gt;<sheetView tabSelected=&quot;1&quot; 
workbookViewId=&quot;0&quot;&gt;<selection activeCell=&quot;A5&quot; sqref=&quot;A5&quot;/&gt;</sheetView&gt;
</sheetViews&gt;<sheetFormatPr baseColWidth=&quot;12&quot; defaultRowHeight=&quot;18&quot; 
x14ac:dyDescent=&quot;0&quot;/&gt;<sheetData&gt;<row r=&quot;1&quot; spans=&quot;1:1&quot;&gt;<c r=&quot;A1&quot;&gt;<v&gt;1</v&gt;
</c&gt;</row&gt;<row r=&quot;2&quot; spans=&quot;1:1&quot;&gt;<c r=&quot;A2&quot;&gt;<v&gt;2</v&gt;</c&gt;</row&gt;<row r=&quot;3&quot; 
spans=&quot;1:1&quot;&gt;<c r=&quot;A3&quot;&gt;<v&gt;3</v&gt;</c&gt;</row&gt;<row r=&quot;4&quot; spans=&quot;1:1&quot;&gt;<c r=&quot;A4&quot;&gt;
<v&gt;-4.2300000000000004</v&gt;</c&gt;</row&gt;</sheetData&gt;<phoneticPr fontId=&quot;1&quot;/&gt;
<pageMargins left=&quot;0.7&quot; right=&quot;0.7&quot; top=&quot;0.75&quot; bottom=&quot;0.75&quot; header=&quot;0.3&quot; 
footer=&quot;0.3&quot;/&gt;<extLst&gt;<ext uri=&quot;{64002731-A6B0-56B0-2670-7721B7C09600}&quot; 
xmlns:mx=&quot;http://schemas.microsoft.com/office/mac/excel/2008/main&quot;&gt;<mx:PLV 
Mode=&quot;0&quot; OnePage=&quot;0&quot; WScale=&quot;0&quot;/&gt;</ext&gt;</extLst&gt;</worksheet&gt;ueda\@remote:~$ 

```

ということで、xlsxからワンライナーでデータをすっぱ抜くワンライナーが完成です。
```bash
ueda\@remote:~$ unzip -p book1.xlsx xl/worksheets/sheet1.xml |
 hxselect c | sed 's;</c&gt;;&amp;\\n;g'
<c r=&quot;A1&quot;&gt;<v&gt;1</v&gt;</c&gt;
<c r=&quot;A2&quot;&gt;<v&gt;2</v&gt;</c&gt;
<c r=&quot;A3&quot;&gt;<v&gt;3</v&gt;</c&gt;
<c r=&quot;A4&quot;&gt;<v&gt;-4.2300000000000004</v&gt;</c&gt;
```



これぞ真のエクシェル芸。なんじゃそりゃ？

うまくやればワンライナーだけでエクセル方眼紙からデータを抜いて、方眼紙にばらまかれた数字や文字列を結合することも夢ではない。<span style="color:red">やりたくないけど</span>。

ところで、zipしたままファイル名が見たければ、unzip -lすれば見れます。これもご活用を。

```bash
ueda\@remote:~$ unzip -l book1.xlsx
Archive: book1.xlsx
 Length Date Time Name
--------- ---------- ----- ----
 1084 1980-01-01 00:00 [Content_Types].xml
 733 1980-01-01 00:00 _rels/.rels
 557 1980-01-01 00:00 xl/_rels/workbook.xml.rels
 745 1980-01-01 00:00 xl/workbook.xml
 16544 1980-01-01 00:00 docProps/thumbnail.jpeg
 7646 1980-01-01 00:00 xl/theme/theme1.xml
 1210 1980-01-01 00:00 xl/styles.xml
 1150 1980-01-01 00:00 xl/worksheets/sheet1.xml
 617 1980-01-01 00:00 docProps/core.xml
 803 1980-01-01 00:00 docProps/app.xml
--------- -------
 31089 10 files
```

昼寝する。
