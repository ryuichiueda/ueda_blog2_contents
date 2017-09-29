---
Keywords: コマンド,CLI,html-xml-utils,hxselect,jq,元ショッカー,シェル芸,エクシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Excelファイルをシェル芸でほじくる。（hxselect編）
昨日<a href="http://blog.ueda.asia/?p=2398" title="Excelファイルをシェル芸でほじくる。ただしエクセル方眼紙は後日ということで。" target="_blank">これ</a>を書いた後思い出したのですが、実はxmlを捌くのにもっと便利なコマンドがあるので、これを使ってもう一回やってみます。



まず、こんなふうにhtml-xml-utilsをインストールします。
```bash
###Mac###
uedambp:~ ueda$ brew install html-xml-utils
###Ubuntu###
root\@remote:~# apt-get install html-xml-utils
```

<!--more-->

んで、昨日の記事では「c」という要素を無理矢理grepで引っ張りだしてましたが、hxselectというコマンドを使うと脳みその負荷が大幅に減ります。
```bash
ueda\@remote:~/tmp$ cat xl/worksheets/sheet1.xml | hxselect c
<c r=&quot;A1&quot;&gt;<v&gt;1</v&gt;</c&gt;<c r=&quot;A2&quot;&gt;<v&gt;2</v&gt;</c&gt;<c r=&quot;A3&quot;&gt;<v&gt;3</v&gt;</c&gt;<c 
r=&quot;A4&quot;&gt;<v&gt;-4.2300000000000004</v&gt;</c&gt;ueda\@remote:~/tmp$
ueda\@remote:~/tmp$ cat xl/worksheets/sheet1.xml | hxselect c |
 sed 's;</c&gt;;&amp;\\n;g'
<c r=&quot;A1&quot;&gt;<v&gt;1</v&gt;</c&gt;
<c r=&quot;A2&quot;&gt;<v&gt;2</v&gt;</c&gt;
<c r=&quot;A3&quot;&gt;<v&gt;3</v&gt;</c&gt;
<c r=&quot;A4&quot;&gt;<v&gt;-4.2300000000000004</v&gt;</c&gt;
```
もう、どれだけビールを飲んでも仕事できそうなくらい簡単です（本当か？）。

あとは<a href="http://blog.ueda.asia/?p=2398" title="Excelファイルをシェル芸でほじくる。ただしエクセル方眼紙は後日ということで。" target="_blank">昨日の記事</a>をご参考に。

似たようなものに、JSON形式を捌く<a href="http://stedolan.github.io/jq/" target="_blank">jqというコマンド</a>もありますので、ウェブな方もぜひシェル芸を極めていただきたく。


しかし、エクセルネタは書きたいことが山ほどある・・・。<span style="color:red">元SIer戦闘員（歩兵すなわちショッカー）としてエクセルと戦って毎回死んだ経験がフルに生かされている・・・。</span>

ところで、SIerのプログラマーのことをハッカーと対比してショッカーとか言ってしまっているが無用な恨みを買いそうである。いや、身内意識が強いので・・・。


さて、家事の続きを・・・。
