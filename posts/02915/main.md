---
Keywords: エクセル,CLI,Excel,エクセル方眼紙はこうやって処理する,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# unzip -p で真のエクシェル芸が完成したような気がする。
なんでこんなに眠いのか。

地味に好評な<a href="/?post=02415" target="_blank">エクシェル芸</a>ですが、肝心なことを忘れていました。

これまでのブログの記事では、エクセルを一旦解凍していましたが、unzipの-pを使うとその必要はありません。こんな感じにxlsxから標準出力にダイレクトにxmlを流すことができます。unzip -pの後にzipファイル（この場合はエクセルファイル）、その次にzipの中の見たいファイルを指定します。最初のシートなら大抵xl/worksheets/sheet1.xmlを指定すればよいことになります。

<!--more-->

```bash
ueda\@remote:~$ unzip -p book1.xlsx xl/worksheets/sheet1.xml 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" 
xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationshi
ps" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
 mc:Ignorable="x14ac" 
xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac">
<dimension ref="A1:A4"/><sheetViews><sheetView tabSelected="1" 
workbookViewId="0"><selection activeCell="A5" sqref="A5"/></sheetView>
</sheetViews><sheetFormatPr baseColWidth="12" defaultRowHeight="18" 
x14ac:dyDescent="0"/><sheetData><row r="1" spans="1:1"><c r="A1"><v>1</v>
</c></row><row r="2" spans="1:1"><c r="A2"><v>2</v></c></row><row r="3" 
spans="1:1"><c r="A3"><v>3</v></c></row><row r="4" spans="1:1"><c r="A4">
<v>-4.2300000000000004</v></c></row></sheetData><phoneticPr fontId="1"/>
<pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" 
footer="0.3"/><extLst><ext uri="{64002731-A6B0-56B0-2670-7721B7C09600}" 
xmlns:mx="http://schemas.microsoft.com/office/mac/excel/2008/main"><mx:PLV 
Mode="0" OnePage="0" WScale="0"/></ext></extLst></worksheet>ueda\@remote:~$ 

```

ということで、xlsxからワンライナーでデータをすっぱ抜くワンライナーが完成です。
```bash
ueda\@remote:~$ unzip -p book1.xlsx xl/worksheets/sheet1.xml |
 hxselect c | sed 's;</c>;&\\n;g'
<c r="A1"><v>1</v></c>
<c r="A2"><v>2</v></c>
<c r="A3"><v>3</v></c>
<c r="A4"><v>-4.2300000000000004</v></c>
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
