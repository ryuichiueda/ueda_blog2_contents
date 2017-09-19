---
Keywords: 寝る,シェル芸,クロス集計
Copyright: (C) 2017 Ryuichi Ueda
---

# すっかりスルー気味でしたが、クロス集計用のコマンドがあります。
こんにちは。風邪ひき大王です。執筆は最後の生業とどなたかが言っていましたが、私も体が弱っていてここに何か書くくらいしか気力が起きません。

以前ウェブで、\@iktakahiroさんの「コマンドでクロス集計する」というのが反響を呼んでいました。

<ul>
<li><a href="http://www.slideshare.net/iktakahiro/bashawk" target="_blank">http://www.slideshare.net/iktakahiro/bashawk</a></li>
</ul>

AWK User会（たぶんさいとうさん）もやってます。

<ul>
<li><a href="http://gauc.no-ip.org/awk-users-jp/blis.cgi/DoukakuAWK_317" target="_blank">http://gauc.no-ip.org/awk-users-jp/blis.cgi/DoukakuAWK_317</a></li>
</ul>

シェル芸勉強会にいつも参加してくださるくんすとさんも、インスパイアされているご様子。

<ul>
<li><a href="http://kunst1080.hatenablog.com/entry/2013/06/01/160617" target="_blank">http://kunst1080.hatenablog.com/entry/2013/06/01/160617</a></li>
<li><a href="http://kunst1080.hatenablog.com/entry/2013/06/02/234025" target="_blank">http://kunst1080.hatenablog.com/entry/2013/06/02/234025</a></li>
</ul>

<h2>Tukubaiのmapコマンドがそれ</h2>

そんでもって、Tukubaiの総本山である某社のエンジニアは、シェル（シェルスクリプト）でクロス集計などは一日に何度もやっているので、それ専用のコマンドを使っています。

例えば、くんすとさんのところのデータ：

[bash]
A Ice 130
A Ice 180
B Juice 120
B Ice 130
I OREO 210
I OREO 210
I OREO 210
[/bash]
（空白はタブではなくスペースです。）

をクロス集計したければ、次のようにコマンドを使います。

まずsm2という集計のコマンドで、同じキーを持つレコードを足し算します。

[bash]
uedamac:~ ueda$ cat data | sort | sm2 1 2 3 3 
A Ice 310
B Ice 130
B Juice 120
I OREO 630
[/bash]

さて、これで1列目を縦軸、2列目を横軸に持って行きたいわけですが、mapというコマンドで一発です。

[bash]
uedamac:~ ueda$ cat data | sort | sm2 1 2 3 3 | map num=1
* Ice Juice OREO
A 310 0 0
B 130 120 0
I 0 0 630
[/bash]

<h2>おわりに</h2>

わたしからも、bash（シェル）最強、と申し上げておきます。Tukubaiのオープン版は<a href="https://uec.usp-lab.com/TUKUBAI/CGI/TUKUBAI.CGI?POMPA=DOWNLOAD" target="_blank">こちら</a>と<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai" target="_blank">こちら</a>にありますのでステマしておきますね。join系のコマンドもあります。


しゃっくりが止まらないので寝るます。
