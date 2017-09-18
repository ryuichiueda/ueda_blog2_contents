---
Keywords:コマンド,Linux,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第15回ドキッ！grepだらけのシェル芸勉強会
<h1>イントロのスライド</h1><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/44124362" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150201-15grep" title="20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）" target="_blank">20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h1>諸注意</h1><br />
<br />
解答はUbuntu Linux 14.04で作成しました。コマンドがないときは適宜インストールのほど。<br />
<br />
Macな人はbrewでGNU grep（ggrep）をインストールすると良かれ悪しかれ拡張オプションが使えます。インストール方法は例えばこちらが分かりやすいかと。3行で済みます。<br />
<br />
<iframe marginwidth="0" marginheight="0" src="http://b.hatena.ne.jp/entry.parts?url=http%3A%2F%2Fqiita.com%2Fquattro_4%2Fitems%2Fe75f2b4156ef45fb6640" scrolling="no" frameborder="0" height="230" width="500"><div class="hatena-bookmark-detail-info"><a href="http://qiita.com/quattro_4/items/e75f2b4156ef45fb6640">高速化したGNU grepをインストールする - Qiita</a><a href="http://b.hatena.ne.jp/entry/qiita.com/quattro_4/items/e75f2b4156ef45fb6640">はてなブックマーク - 高速化したGNU grepをインストールする - Qiita</a></div></iframe><br />
<br />
<!--more--><br />
<br />
<h1>Q1</h1><br />
<br />
次のようにファイルを作ります。<br />
<br />
[bash]<br />
$ seq 2 5 &gt; a<br />
$ seq 1 9 &gt; b<br />
$ seq 5 11 &gt; c<br />
$ seq 3 6 &gt; d<br />
[/bash]<br />
<br />
1という文字を含まないファイルを列挙してください（aとdですね）。<br />
<br />
<!--more--><br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
$ grep -L 1 {a..d}<br />
a<br />
d<br />
###-Lを知らなければ###<br />
$ grep -c 1 {a..d} | awk -F: '$2==0'<br />
a:0<br />
d:0<br />
[/bash]<br />
<br />
<h1>Q2</h1><br />
<br />
作業ディレクトリを作り、その下に次のようにfile.1〜file.10000というファイルを作ります。<br />
<br />
[bash]<br />
$ seq 1 10000 | xargs -I\@ touch file.\@<br />
[/bash]<br />
<br />
以下の数字を持つファイルだけ残して後のファイルを消去してください。<br />
<br />
<ul><br />
 <li>1〜9</li><br />
 <li>10, 20, 30, ..., 90</li><br />
 <li>数字の下2桁が0のファイル</li><br />
</ul><br />
<br />
<br />
<!--more--><br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
$ ls -f | grep -v &quot;file\\..$&quot; | grep -v &quot;file\\..0$&quot; | grep -v &quot;file\\..*00$&quot; | xargs rm<br />
rm: cannot remove ‘.’: Is a directory<br />
rm: cannot remove ‘..’: Is a directory<br />
###こんな書き方も###<br />
$ ls -f | <br />
grep -v -e &quot;file\\..$&quot; -e &quot;file\\..0$&quot; -e &quot;file\\..*00$&quot; |<br />
xargs rm<br />
rm: cannot remove ‘.’: Is a directory<br />
rm: cannot remove ‘..’: Is a directory<br />
$ ls<br />
file.1 file.2300 file.4 file.5400 file.70 file.8500<br />
file.10 file.2400 file.40 file.5500 file.700 file.8600<br />
file.100 file.2500 file.400 file.5600 file.7000 file.8700<br />
file.1000 file.2600 file.4000 file.5700 file.7100 file.8800<br />
file.10000 file.2700 file.4100 file.5800 file.7200 file.8900<br />
file.1100 file.2800 file.4200 file.5900 file.7300 file.9<br />
file.1200 file.2900 file.4300 file.6 file.7400 file.90<br />
file.1300 file.3 file.4400 file.60 file.7500 file.900<br />
file.1400 file.30 file.4500 file.600 file.7600 file.9000<br />
file.1500 file.300 file.4600 file.6000 file.7700 file.9100<br />
file.1600 file.3000 file.4700 file.6100 file.7800 file.9200<br />
file.1700 file.3100 file.4800 file.6200 file.7900 file.9300<br />
file.1800 file.3200 file.4900 file.6300 file.8 file.9400<br />
file.1900 file.3300 file.5 file.6400 file.80 file.9500<br />
file.2 file.3400 file.50 file.6500 file.800 file.9600<br />
file.20 file.3500 file.500 file.6600 file.8000 file.9700<br />
file.200 file.3600 file.5000 file.6700 file.8100 file.9800<br />
file.2000 file.3700 file.5100 file.6800 file.8200 file.9900<br />
file.2100 file.3800 file.5200 file.6900 file.8300<br />
file.2200 file.3900 file.5300 file.7 file.8400<br />
[/bash]<br />
<br />
<h1>Q3</h1><br />
<br />
次のテキストから、「-v」、「-f」、「awk」の数をそれぞれカウントしてください。gawk、nawkは避けてください（awkの数としてカウントしない）。できる人はgrepは1個で。さらにできる人は拡張正規表現を使わないでやってみましょう。<br />
<br />
<br />
[bash]<br />
$ cat text1 <br />
awk -v v=&quot;hoge&quot; 'BEGIN{print v}'<br />
echo 'BEGIN{print 1}' | gawk -f -<br />
nawk 'BEGIN{print &quot; BEGIN{print x}&quot;}' | awk -v x=3 -f -<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
###ベタな感じ（これでも全然問題ありません）###<br />
$ grep -oE '(-[a-z]|[a-z]?awk)' text1 | grep -v '[ng]awk' | sort | uniq <br />
c- 2 -f<br />
 2 -v<br />
 2 awk<br />
###最小手順（と思われる方法）###<br />
$ grep -wEo &quot;(-[a-z]|awk)&quot; text1 | sort | uniq <br />
c- 2 -f<br />
 2 -v<br />
 2 awk<br />
###拡張正規表現を使わない###<br />
$ grep -wo -e &quot;-[a-z]&quot; -e &quot;awk&quot; text1 | sort | uniq <br />
c- 2 -f<br />
 2 -v<br />
 2 awk<br />
[/bash]<br />
<br />
<h1>Q4</h1><br />
<br />
/etc/の下（子、孫、・・・）のファイルのうち、シバンが「#!/bin/sh」のシェルスクリプトについて、中に「set -e」と記述のあるファイルとないファイルの数をそれぞれ数えてください。（コメント中のset -eも数えてOKです。）<br />
<br />
<h1>解答</h1><br />
<br />
一例です。set -eと記述があるものが33、無いものが75となります。<br />
<br />
[bash]<br />
$ sudo grep -l '#!/bin/sh' /etc/ -R | sudo xargs grep -c 'set -e' |<br />
 sed 's/.*://' | awk '{if($1==0){print 0}else{print 1}}' | sort | uniq <br />
c-grep: /etc/alternatives/ghostscript-current/Resource/CIDFSubst/DroidSansFallback.ttf: No such file or directory<br />
grep: /etc/blkid.tab: No such file or directory<br />
 75 0<br />
 33 1<br />
[/bash]<br />
<br />
<h1>Q5</h1><br />
<br />
日本語やギリシャ文字のある行を除去してください。<br />
<br />
[bash]<br />
$ cat text2 <br />
A pen is a pen?<br />
日本語でおk<br />
ΩΩπ&lt;Ω&lt; na nandatte!!<br />
Randy W. Bass<br />
env x='() { :;}; echo vulnerable' bash -c &quot;echo this is a test&quot;<br />
#危険シェル芸<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
別解求む。<br />
<br />
[bash]<br />
$ LANG=C grep &quot;^[[:print:]]*$&quot; text2<br />
[/bash]<br />
<br />
<br />
<h1>Q6</h1><br />
<br />
次のようにファイルa, b, cを作ります。<br />
<br />
[bash]<br />
$ echo 1 2 3 4 &gt; a<br />
$ echo 2 3 4 5 &gt; b<br />
$ echo 1 4 5 &gt; c<br />
[/bash]<br />
<br />
ファイルの中の数字を足して10になるファイルを挙げてください。<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
###grepを使わなくてもいけますが・・・###<br />
$ for i in a b c ; do [ 10 -eq $(numsum -r $i) ] &amp;&amp; echo $i ; done<br />
###grepでリストを作る###<br />
$ grep &quot;&quot; * | tr ':' ' ' | <br />
awk '{for(i=2;i&lt;=NF;i++){a+=$i};print $1,a;a=0}' | grep &quot; 10$&quot;<br />
###Tukubaiを利用###<br />
$ grep &quot;&quot; * | tr ':' ' ' | ysum num=1 | grep &quot; 10$&quot;<br />
[/bash]<br />
<br />
<h1>Q7</h1><br />
<br />
psコマンドを打って（オプションは任意）、そのpsコマンドの行、親プロセスの行、親の親のプロセスの行を表示してみてください。<br />
<br />
<h1>解答</h1><br />
<br />
すごくいい加減な気がしないでもありませんが・・・<br />
<br />
[bash]<br />
$ ps -eo ppid,pid,command &gt; f ; grep &quot;ps -eo&quot; f | grep -v grep |<br />
 awk '{print &quot; &quot;$1&quot; &quot;;print &quot; &quot;$2&quot; &quot;}' | grep -f - f |<br />
 awk '{print &quot; &quot;$1&quot; &quot;;print &quot; &quot;$2&quot; &quot;}' | grep -f - f<br />
 5696 5767 sshd: ueda\@pts/6 <br />
 5767 5768 -bash<br />
 5768 8806 ps -eo ppid,pid,command<br />
[/bash]<br />
<br />
<h1>Q8</h1><br />
<br />
seqとfactorの出力の後ろにgrepだけをいくつかつなげて、「素数の一つ前の数で、かつ10以上の数」を列挙してください。<br />
<br />
[bash]<br />
$ seq 10 1000 | factor | ...(grepだけ)<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
$ seq 10 1000 | factor | grep -EB 1 '^[^ ]+ [^ ]+$' |<br />
 grep -Eo '^[0-9]+[02468]:' | grep -Eo '^[0-9]+'<br />
[/bash]<br />
<br />

