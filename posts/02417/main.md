---
Keywords:コマンド,CLI,html-xml-utils,hxselect,jq,元ショッカー,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---
# Excelファイルをシェル芸でほじくる。（hxselect編）
昨日<a href="http://blog.ueda.asia/?p=2398" title="Excelファイルをシェル芸でほじくる。ただしエクセル方眼紙は後日ということで。" target="_blank">これ</a>を書いた後思い出したのですが、実はxmlを捌くのにもっと便利なコマンドがあるので、これを使ってもう一回やってみます。<br />
<br />
<br />
<br />
まず、こんなふうにhtml-xml-utilsをインストールします。<br />
[bash]<br />
###Mac###<br />
uedambp:~ ueda$ brew install html-xml-utils<br />
###Ubuntu###<br />
root\@remote:~# apt-get install html-xml-utils<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
んで、昨日の記事では「c」という要素を無理矢理grepで引っ張りだしてましたが、hxselectというコマンドを使うと脳みその負荷が大幅に減ります。<br />
[bash]<br />
ueda\@remote:~/tmp$ cat xl/worksheets/sheet1.xml | hxselect c<br />
&lt;c r=&quot;A1&quot;&gt;&lt;v&gt;1&lt;/v&gt;&lt;/c&gt;&lt;c r=&quot;A2&quot;&gt;&lt;v&gt;2&lt;/v&gt;&lt;/c&gt;&lt;c r=&quot;A3&quot;&gt;&lt;v&gt;3&lt;/v&gt;&lt;/c&gt;&lt;c <br />
r=&quot;A4&quot;&gt;&lt;v&gt;-4.2300000000000004&lt;/v&gt;&lt;/c&gt;ueda\@remote:~/tmp$<br />
ueda\@remote:~/tmp$ cat xl/worksheets/sheet1.xml | hxselect c |<br />
 sed 's;&lt;/c&gt;;&amp;\\n;g'<br />
&lt;c r=&quot;A1&quot;&gt;&lt;v&gt;1&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A2&quot;&gt;&lt;v&gt;2&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A3&quot;&gt;&lt;v&gt;3&lt;/v&gt;&lt;/c&gt;<br />
&lt;c r=&quot;A4&quot;&gt;&lt;v&gt;-4.2300000000000004&lt;/v&gt;&lt;/c&gt;<br />
[/bash]<br />
もう、どれだけビールを飲んでも仕事できそうなくらい簡単です（本当か？）。<br />
<br />
あとは<a href="http://blog.ueda.asia/?p=2398" title="Excelファイルをシェル芸でほじくる。ただしエクセル方眼紙は後日ということで。" target="_blank">昨日の記事</a>をご参考に。<br />
<br />
似たようなものに、JSON形式を捌く<a href="http://stedolan.github.io/jq/" target="_blank">jqというコマンド</a>もありますので、ウェブな方もぜひシェル芸を極めていただきたく。<br />
<br />
<br />
しかし、エクセルネタは書きたいことが山ほどある・・・。<span style="color:red">元SIer戦闘員（歩兵すなわちショッカー）としてエクセルと戦って毎回死んだ経験がフルに生かされている・・・。</span><br />
<br />
ところで、SIerのプログラマーのことをハッカーと対比してショッカーとか言ってしまっているが無用な恨みを買いそうである。いや、身内意識が強いので・・・。<br />
<br />
<br />
さて、家事の続きを・・・。
