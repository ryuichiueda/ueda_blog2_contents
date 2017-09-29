---
Keywords: Excel,PowerPoint,Word,シェル芸,エクシェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第26回シェル芸勉強会及びエクシェル芸勉強会
問題のみのページは<a href="https://blog.ueda.asia/?p=9226">コチラ</a>

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

.xlsxや.docx、.pptxファイルはzipファイルです。リポジトリの中のxlsx,docx,pptxを展開し、中にどんなファイルがあるか見て、再び戻して再び.xlsx,.docx,.pptxファイルとして開いてみてください。

<h3>解答</h3>

解凍すると、一つのディレクトリに収まってなく、その場にいくつかのファイルが展開されるので厄介です。ファイルの置き場所と展開する場所を分けましょう。

```bash
$ mkdir ~/tmp
$ cd ~/tmp
###tmpの下に置かずに解凍###
$ unzip ~/ShellGeiData/vol.26/graph.xlsx 
ueda\@remote:~/tmp$ ls
[Content_Types].xml _rels docProps xl
ueda\@remote:~/tmp$ tree
.
├── [Content_Types].xml
├── _rels
├── docProps
│   ├── app.xml
│   ├── core.xml
│   └── thumbnail.jpeg
└── xl
 ├── _rels
 │   └── workbook.xml.rels
 ├── calcChain.xml
 ├── charts
 │   └── chart1.xml
 ├── drawings
 │   ├── _rels
 │   │   └── drawing1.xml.rels
 │   └── drawing1.xml
 ├── styles.xml
 ├── theme
 │   └── theme1.xml
 ├── workbook.xml
 └── worksheets
 ├── _rels
 │   └── sheet1.xml.rels
 └── sheet1.xml

10 directories, 14 files
###再圧縮したファイルも別のディレクトリに作ると事故が少ない###
ueda\@remote:~/tmp$ zip -r ../hoge.xlsx ./
```


<h2>Q2</h2>

20141019OSC_LT.pptxのスライドに何回「危険」という単語が出てくるか数えてください。画像になっているものは除きます。

<h3>解答</h3>

```bash
$ unzip ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ;
grep -o 危険 ppt/slides/slide* | wc -l
17
```

unzipは-pオプションで必要なファイルだけcatすることができます。ということで次のようにすると完全にワンライナーになります。

```bash
$ unzip -p ~/ShellGeiData/vol.26/20141019OSC_LT.pptx 'ppt/slides/slide*' |
 grep -o 危険 | wc -l
17
```


<h2>Q3</h2>

20141019OSC_LT.pptxのスライドから画像を抽出して、一つのディレクトリにまとめてzipで固めてください。

<h3>解答</h3>

```bash
$ unzip ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ;
 zip -r media.zip ./ppt/media/
```

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


<h3>解答</h3>

```bash
$ unzip -p ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ppt/slides/slide7.xml |
 xmllint --format - | grep '<a:[pt]>' | sed 's;</.*;;' |
 sed 's;<.*>;;' | awk 'NF==0{print "\@\@\@"}{print}' |
 xargs | sed 's/\@\@*/\\n/g' | awk 'NF' | tr -d ' '
戦果（？）
初日だけで見知らぬ方のマシン3台轟沈
その他自爆者多数
Docker上で試したらホストマシン沈黙の報告
自分の本がサイト経由で1冊だけ売れた
フォロワーが1人減った
2014/10/19
OSCTokyo/Fall2014
7
```

```bash

```

<h2>Q5</h2>

graph.xlsxの2列の数字を抜き出して端末にSSV形式のデータ（CSVのカンマがスペースになったもの）、あるいはセルの番号と値のリストとして抜き出してください。


<h3>解答</h3>

```bash
###スペース区切り###
$ unzip ~/ShellGeiData/vol.26/graph.xlsx;
 cat xl/worksheets/sheet1.xml |
 sed 's;</row>;\\n;g' | sed 's;</v>.*<v>; ;' |
 sed 's;.*<v>;;' | sed 's;</v>.*;;' | grep -v "^<"
###スペース区切り・ワンライナーバージョン###
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |
 sed 's;</row>;\\n;g' | sed 's;</v>.*<v>; ;' |
 sed 's;.*<v>;;' | sed 's;</v>.*;;' | grep -v "^<"
```

もっとスマートに行うには、html-xml-utilsとlibxml2-utilsをインストールしてhxselectコマンドやxmllintを使います。

```bash
$ sudo apt install html-xml-utils
$ sudo apt install libxml2-utils
###番号と値のリスト###
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |
 hxselect c -s '\\n' | sed 's;[^=]*=";;' |
 sed 's;".*<v>; ;' | sed 's;<.*;;'
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |
 xmllint --format - | grep -e '<c r=' -e '<v>' | xargs |
 sed 's;</v>;\\n;g' | sed 's/.*=//' | sed 's/>.*>/ /'
```

もっと便利なツールもあるという噂ですが、とりあえず私からこれくらいで・・・


<h2>Q6</h2>

hanshin.xlsxのシートについてQ2と同様SSV形式か、セルの番号と値のリストとして端末上に出力してください。日付のセルについては何を出力しても良いことにします。

<h3>解答</h3>

文字列は展開したファイルのxl/sharedStrings.xmlに順番に入っています。

```bash
$ unzip ~/GIT/ShellGeiData/vol.26/hanshin.xlsx 
$ xmllint --format xl/sharedStrings.xml | head
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="18" uniqueCount="15">
 <si>
 <t>真弓</t>
 <rPh sb="0" eb="2">
 <t>マユミ</t>
 </rPh>
 <phoneticPr fontId="1"/>
 </si>
 <si>
```

読みのデータが邪魔なので、消去した上でリストを作っておきます。

```bash
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/sharedStrings.xml |
 hxselect si -s '\\n' | awk -F'[<>]' '{print NR-1,$5}' > strings
$ head -n 3 strings 
0 真弓
1 弘田
2 バース
```

次に、シートのデータを加工していきます。文字列のセルには「t="s"」という属性があるので、これで文字列のセルと数字のセルを分けます。文字列のセルのv要素にある数字は、sharedStrings.xmlの何番目の文字列がこのセルに入るかを意味します。（sharedStrings.xmlはXMLファイルなのにデータの並び順で文字列を管理しているという・・・）

```bash
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/worksheets/sheet1.xml |
 hxselect c -s '\\n' | grep '<v>' |
 awk -F'[<> "]' '/t="s"/{print $4,"s",$(NF-4)}!/t="s"/{print $4,"n",$(NF-4)}'
B1 n 42522
C1 n 42561
A2 n 1
B2 s 0
C2 s 0
A3 n 2
B3 s 1
C3 s 9
A4 n 3
B4 s 2
...
```

ここまでできたら、awkで無理やり文字列のファイルとデータのファイルを混ぜて答えを出します。この例ではFILENAMEという変数を使っています。

```bash
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/worksheets/sheet1.xml |
 hxselect c -s '\\n' | grep '<v>' |
 awk -F'[<> "]' '/t="s"/{print $4,"s",$(NF-4)}!/t="s"/{print $4,"n",$(NF-4)}' |
 awk 'FILENAME=="strings"{s[$1]=$2}FILENAME=="-"&&
$2=="s"{print $1,s[$3]}$2=="n"{print $1,$3}' strings -
B1 42522
C1 42561
A2 1
B2 真弓
C2 真弓
A3 2
B3 弘田
C3 北村
A4 3
B4 バース
C4 バース
A5 4
B5 掛布
C5 掛布
A6 5
B6 岡田
C6 佐野
A7 6
B7 佐野
C7 木戸
A8 7
B8 平田
C8 平田
A9 8
B9 木戸
C9 永尾
A10 9
B10 ゲイル
C10 池田
```

<h2>Q7</h2>

certificate.docxファイルを開いて確認し、人の名前が入るところに好きな名前を入れてみましょう。

<h3>解答</h3>

ホームの下にtmp等の一時ディレクトリを作ってそこで試しましょう。-iオプションは、BSD系のsedの場合-i.bakと言うように拡張子をつけてバックアップファイルを作らなければなりませんが、その場合はバックアップファイルを消してから再圧縮します。

```bash
###~/tmp/で作業すると仮定します###
$ unzip ~/ShellGeiData/vol.26/certificate.docx ; 
sed -i 's/WINNER/しぇる芸のオッサン/' word/document.xml ; 
zip -r ../hoge.docx ./
###ワーニングが出ますが開けます###
```

<h2>Q8</h2>

Q7を応用し、次のリストlist.txtで、複数の表彰状を作ってみましょう。

```bash
$ cat list.txt 
シェル芸おじさん
シェル芸野郎
変態シェル芸豚野郎
```

<h3>解答</h3>

unzipに-o（overwrite）オプションをつけると便利です。

```bash
$ cat ~/ShellGeiData/vol.26/list.txt | 
while read name ; do unzip -o ~/ShellGeiData/vol.26/certificate.docx ;
 sed -i "s/WINNER/$name/" word/document.xml ;
 zip -r ../$name.docx ./ ; done
```





