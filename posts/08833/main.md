# 【問題と解答】第26回シェル芸勉強会及びエクシェル芸勉強会
問題のみのページは<a href="https://blog.ueda.asia/?p=9226">コチラ</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.26" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.26</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>環境</h2><br />
<br />
シェル芸を行うのはUbuntu Linux 16.04です。確認はMacのExcelやWord, PowerPointで行いました。今回は特にワンライナーにこだわる必要はありません。シェルスクリプトにしても構いません。もちろん、一般解にこだわる必要もありません。<br />
<br />
<h2>イントロ</h2><br />
<br />
<a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac26%e5%9b%9e%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a%e5%8f%8a%e3%81%b3%e3%82%a8%e3%82%af%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">第26回シェル芸勉強会及びエクシェル芸勉強会</a><br />
<br />
<h2>Q1</h2><br />
<br />
.xlsxや.docx、.pptxファイルはzipファイルです。リポジトリの中のxlsx,docx,pptxを展開し、中にどんなファイルがあるか見て、再び戻して再び.xlsx,.docx,.pptxファイルとして開いてみてください。<br />
<br />
<h3>解答</h3><br />
<br />
解凍すると、一つのディレクトリに収まってなく、その場にいくつかのファイルが展開されるので厄介です。ファイルの置き場所と展開する場所を分けましょう。<br />
<br />
[bash]<br />
$ mkdir ~/tmp<br />
$ cd ~/tmp<br />
###tmpの下に置かずに解凍###<br />
$ unzip ~/ShellGeiData/vol.26/graph.xlsx <br />
ueda\@remote:~/tmp$ ls<br />
[Content_Types].xml _rels docProps xl<br />
ueda\@remote:~/tmp$ tree<br />
.<br />
├── [Content_Types].xml<br />
├── _rels<br />
├── docProps<br />
│   ├── app.xml<br />
│   ├── core.xml<br />
│   └── thumbnail.jpeg<br />
└── xl<br />
 ├── _rels<br />
 │   └── workbook.xml.rels<br />
 ├── calcChain.xml<br />
 ├── charts<br />
 │   └── chart1.xml<br />
 ├── drawings<br />
 │   ├── _rels<br />
 │   │   └── drawing1.xml.rels<br />
 │   └── drawing1.xml<br />
 ├── styles.xml<br />
 ├── theme<br />
 │   └── theme1.xml<br />
 ├── workbook.xml<br />
 └── worksheets<br />
 ├── _rels<br />
 │   └── sheet1.xml.rels<br />
 └── sheet1.xml<br />
<br />
10 directories, 14 files<br />
###再圧縮したファイルも別のディレクトリに作ると事故が少ない###<br />
ueda\@remote:~/tmp$ zip -r ../hoge.xlsx ./<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
20141019OSC_LT.pptxのスライドに何回「危険」という単語が出てくるか数えてください。画像になっているものは除きます。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ unzip ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ;<br />
grep -o 危険 ppt/slides/slide* | wc -l<br />
17<br />
[/bash]<br />
<br />
unzipは-pオプションで必要なファイルだけcatすることができます。ということで次のようにすると完全にワンライナーになります。<br />
<br />
[bash]<br />
$ unzip -p ~/ShellGeiData/vol.26/20141019OSC_LT.pptx 'ppt/slides/slide*' |<br />
 grep -o 危険 | wc -l<br />
17<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
20141019OSC_LT.pptxのスライドから画像を抽出して、一つのディレクトリにまとめてzipで固めてください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ unzip ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ;<br />
 zip -r media.zip ./ppt/media/<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
20141019OSC_LT.pptxのスライドの7ページ目のテキストをスクレイピングしましょう。以下が出力の例です。<br />
<br />
[bash]<br />
戦果（？）<br />
初日だけで見知らぬ方のマシン3台轟沈<br />
その他自爆者多数<br />
Docker上で試したらホストマシン沈黙の報告<br />
自分の本がサイト経由で1冊だけ売れた<br />
フォロワーが1人減った<br />
（以下、フッタ等の文字列が混ざっても可とします）<br />
[/bash]<br />
<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ unzip -p ~/ShellGeiData/vol.26/20141019OSC_LT.pptx ppt/slides/slide7.xml |<br />
 xmllint --format - | grep '&lt;a:[pt]&gt;' | sed 's;&lt;/.*;;' |<br />
 sed 's;&lt;.*&gt;;;' | awk 'NF==0{print &quot;\@\@\@&quot;}{print}' |<br />
 xargs | sed 's/\@\@*/\\n/g' | awk 'NF' | tr -d ' '<br />
戦果（？）<br />
初日だけで見知らぬ方のマシン3台轟沈<br />
その他自爆者多数<br />
Docker上で試したらホストマシン沈黙の報告<br />
自分の本がサイト経由で1冊だけ売れた<br />
フォロワーが1人減った<br />
2014/10/19<br />
OSCTokyo/Fall2014<br />
7<br />
[/bash]<br />
<br />
[bash]<br />
<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
graph.xlsxの2列の数字を抜き出して端末にSSV形式のデータ（CSVのカンマがスペースになったもの）、あるいはセルの番号と値のリストとして抜き出してください。<br />
<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
###スペース区切り###<br />
$ unzip ~/ShellGeiData/vol.26/graph.xlsx;<br />
 cat xl/worksheets/sheet1.xml |<br />
 sed 's;&lt;/row&gt;;\\n;g' | sed 's;&lt;/v&gt;.*&lt;v&gt;; ;' |<br />
 sed 's;.*&lt;v&gt;;;' | sed 's;&lt;/v&gt;.*;;' | grep -v &quot;^&lt;&quot;<br />
###スペース区切り・ワンライナーバージョン###<br />
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |<br />
 sed 's;&lt;/row&gt;;\\n;g' | sed 's;&lt;/v&gt;.*&lt;v&gt;; ;' |<br />
 sed 's;.*&lt;v&gt;;;' | sed 's;&lt;/v&gt;.*;;' | grep -v &quot;^&lt;&quot;<br />
[/bash]<br />
<br />
もっとスマートに行うには、html-xml-utilsとlibxml2-utilsをインストールしてhxselectコマンドやxmllintを使います。<br />
<br />
[bash]<br />
$ sudo apt install html-xml-utils<br />
$ sudo apt install libxml2-utils<br />
###番号と値のリスト###<br />
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |<br />
 hxselect c -s '\\n' | sed 's;[^=]*=&quot;;;' |<br />
 sed 's;&quot;.*&lt;v&gt;; ;' | sed 's;&lt;.*;;'<br />
$ unzip -p ~/ShellGeiData/vol.26/graph.xlsx xl/worksheets/sheet1.xml |<br />
 xmllint --format - | grep -e '&lt;c r=' -e '&lt;v&gt;' | xargs |<br />
 sed 's;&lt;/v&gt;;\\n;g' | sed 's/.*=//' | sed 's/&gt;.*&gt;/ /'<br />
[/bash]<br />
<br />
もっと便利なツールもあるという噂ですが、とりあえず私からこれくらいで・・・<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
hanshin.xlsxのシートについてQ2と同様SSV形式か、セルの番号と値のリストとして端末上に出力してください。日付のセルについては何を出力しても良いことにします。<br />
<br />
<h3>解答</h3><br />
<br />
文字列は展開したファイルのxl/sharedStrings.xmlに順番に入っています。<br />
<br />
[bash]<br />
$ unzip ~/GIT/ShellGeiData/vol.26/hanshin.xlsx <br />
$ xmllint --format xl/sharedStrings.xml | head<br />
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;yes&quot;?&gt;<br />
&lt;sst xmlns=&quot;http://schemas.openxmlformats.org/spreadsheetml/2006/main&quot; count=&quot;18&quot; uniqueCount=&quot;15&quot;&gt;<br />
 &lt;si&gt;<br />
 &lt;t&gt;真弓&lt;/t&gt;<br />
 &lt;rPh sb=&quot;0&quot; eb=&quot;2&quot;&gt;<br />
 &lt;t&gt;マユミ&lt;/t&gt;<br />
 &lt;/rPh&gt;<br />
 &lt;phoneticPr fontId=&quot;1&quot;/&gt;<br />
 &lt;/si&gt;<br />
 &lt;si&gt;<br />
[/bash]<br />
<br />
読みのデータが邪魔なので、消去した上でリストを作っておきます。<br />
<br />
[bash]<br />
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/sharedStrings.xml |<br />
 hxselect si -s '\\n' | awk -F'[&lt;&gt;]' '{print NR-1,$5}' &gt; strings<br />
$ head -n 3 strings <br />
0 真弓<br />
1 弘田<br />
2 バース<br />
[/bash]<br />
<br />
次に、シートのデータを加工していきます。文字列のセルには「t="s"」という属性があるので、これで文字列のセルと数字のセルを分けます。文字列のセルのv要素にある数字は、sharedStrings.xmlの何番目の文字列がこのセルに入るかを意味します。（sharedStrings.xmlはXMLファイルなのにデータの並び順で文字列を管理しているという・・・）<br />
<br />
[bash]<br />
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/worksheets/sheet1.xml |<br />
 hxselect c -s '\\n' | grep '&lt;v&gt;' |<br />
 awk -F'[&lt;&gt; &quot;]' '/t=&quot;s&quot;/{print $4,&quot;s&quot;,$(NF-4)}!/t=&quot;s&quot;/{print $4,&quot;n&quot;,$(NF-4)}'<br />
B1 n 42522<br />
C1 n 42561<br />
A2 n 1<br />
B2 s 0<br />
C2 s 0<br />
A3 n 2<br />
B3 s 1<br />
C3 s 9<br />
A4 n 3<br />
B4 s 2<br />
...<br />
[/bash]<br />
<br />
ここまでできたら、awkで無理やり文字列のファイルとデータのファイルを混ぜて答えを出します。この例ではFILENAMEという変数を使っています。<br />
<br />
[bash]<br />
$ unzip -p ~/GIT/ShellGeiData/vol.26/hanshin.xlsx xl/worksheets/sheet1.xml |<br />
 hxselect c -s '\\n' | grep '&lt;v&gt;' |<br />
 awk -F'[&lt;&gt; &quot;]' '/t=&quot;s&quot;/{print $4,&quot;s&quot;,$(NF-4)}!/t=&quot;s&quot;/{print $4,&quot;n&quot;,$(NF-4)}' |<br />
 awk 'FILENAME==&quot;strings&quot;{s[$1]=$2}FILENAME==&quot;-&quot;&amp;&amp;<br />
$2==&quot;s&quot;{print $1,s[$3]}$2==&quot;n&quot;{print $1,$3}' strings -<br />
B1 42522<br />
C1 42561<br />
A2 1<br />
B2 真弓<br />
C2 真弓<br />
A3 2<br />
B3 弘田<br />
C3 北村<br />
A4 3<br />
B4 バース<br />
C4 バース<br />
A5 4<br />
B5 掛布<br />
C5 掛布<br />
A6 5<br />
B6 岡田<br />
C6 佐野<br />
A7 6<br />
B7 佐野<br />
C7 木戸<br />
A8 7<br />
B8 平田<br />
C8 平田<br />
A9 8<br />
B9 木戸<br />
C9 永尾<br />
A10 9<br />
B10 ゲイル<br />
C10 池田<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
certificate.docxファイルを開いて確認し、人の名前が入るところに好きな名前を入れてみましょう。<br />
<br />
<h3>解答</h3><br />
<br />
ホームの下にtmp等の一時ディレクトリを作ってそこで試しましょう。-iオプションは、BSD系のsedの場合-i.bakと言うように拡張子をつけてバックアップファイルを作らなければなりませんが、その場合はバックアップファイルを消してから再圧縮します。<br />
<br />
[bash]<br />
###~/tmp/で作業すると仮定します###<br />
$ unzip ~/ShellGeiData/vol.26/certificate.docx ; <br />
sed -i 's/WINNER/しぇる芸のオッサン/' word/document.xml ; <br />
zip -r ../hoge.docx ./<br />
###ワーニングが出ますが開けます###<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
Q7を応用し、次のリストlist.txtで、複数の表彰状を作ってみましょう。<br />
<br />
[bash]<br />
$ cat list.txt <br />
シェル芸おじさん<br />
シェル芸野郎<br />
変態シェル芸豚野郎<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
unzipに-o（overwrite）オプションをつけると便利です。<br />
<br />
[bash]<br />
$ cat ~/ShellGeiData/vol.26/list.txt | <br />
while read name ; do unzip -o ~/ShellGeiData/vol.26/certificate.docx ;<br />
 sed -i &quot;s/WINNER/$name/&quot; word/document.xml ;<br />
 zip -r ../$name.docx ./ ; done<br />
[/bash]<br />
<br />
<br />
<br />
<br />

