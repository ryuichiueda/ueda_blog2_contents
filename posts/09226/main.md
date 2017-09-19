---
Keywords: コマンド,CLI,Excel,PowerPoint,Word,勉強会,シェル芸,エクシェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第26回シェル芸勉強会及びエクシェル芸勉強会
解答は<a href="https://blog.ueda.asia/?p=8833">コチラ</a>

<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.26" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.26</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>

シェル芸を行うのはUbuntu Linux 16.04です。確認はMacのExcelやWord, PowerPointで行いました。今回は特にワンライナーにこだわる必要はありません。シェルスクリプトにしても構いません。もちろん、一般解にこだわる必要もありません。

<h2>イントロ</h2>

<a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac26%e5%9b%9e%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a%e5%8f%8a%e3%81%b3%e3%82%a8%e3%82%af%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">第26回シェル芸勉強会及びエクシェル芸勉強会</a>


<h2>Q1</h2>

.xlsxや.docx、.pptxファイルはzipファイルです。リポジトリの中のxlsx,docx,pptxを展開し、中にどんなファイルがあるか見て、再び戻して再び.xlsxファイルとして開いてみてください。

<h2>Q2</h2>

20141019OSC_LT.pptxのスライドに何回「危険」という単語が出てくるか数えてください。画像になっているものは除きます。

<h2>Q3</h2>

20141019OSC_LT.pptxのスライドから画像を抽出して、一つのディレクトリにまとめてzipで固めてください。

<h2>Q4</h2>

20141019OSC_LT.pptxのスライドの7ページ目のテキストをスクレイピングしましょう。以下が出力の例です。

```bash
戦果（？）
初日だけで見知らぬ方のマシン3台轟沈
その他自爆者多数
Docker上で試したらホストマシン沈黙の報告
自分の本がサイト経由で1冊だけ売れた
フォロワーが1人減った
（以下、フッタ等の文字列が混ざっても可とします）
```


<h2>Q5</h2>

graph.xlsxの2列の数字を抜き出して端末にSSV形式のデータ（CSVのカンマがスペースになったもの）、あるいはセルの番号と値のリストとして抜き出してください。


<h2>Q6</h2>

hanshin.xlsxのシートについてQ2と同様SSV形式か、セルの番号と値のリストとして端末上に出力してください。日付のセルについては何を出力しても良いことにします。

<h2>Q7</h2>

certificate.docxファイルを開いて確認し、人の名前が入るところに好きな名前を入れてみましょう。


<h2>Q8</h2>

Q7を応用し、次のリストlist.txtで、複数の表彰状を作ってみましょう。

```bash
$ cat list.txt 
シェル芸おじさん
シェル芸野郎
変態シェル芸豚野郎
```





