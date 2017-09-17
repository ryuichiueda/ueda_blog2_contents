# すっかりスルー気味でしたが、クロス集計用のコマンドがあります。
こんにちは。風邪ひき大王です。執筆は最後の生業とどなたかが言っていましたが、私も体が弱っていてここに何か書くくらいしか気力が起きません。<br />
<br />
以前ウェブで、\@iktakahiroさんの「コマンドでクロス集計する」というのが反響を呼んでいました。<br />
<br />
<ul><br />
<li><a href="http://www.slideshare.net/iktakahiro/bashawk" target="_blank">http://www.slideshare.net/iktakahiro/bashawk</a></li><br />
</ul><br />
<br />
AWK User会（たぶんさいとうさん）もやってます。<br />
<br />
<ul><br />
<li><a href="http://gauc.no-ip.org/awk-users-jp/blis.cgi/DoukakuAWK_317" target="_blank">http://gauc.no-ip.org/awk-users-jp/blis.cgi/DoukakuAWK_317</a></li><br />
</ul><br />
<br />
シェル芸勉強会にいつも参加してくださるくんすとさんも、インスパイアされているご様子。<br />
<br />
<ul><br />
<li><a href="http://kunst1080.hatenablog.com/entry/2013/06/01/160617" target="_blank">http://kunst1080.hatenablog.com/entry/2013/06/01/160617</a></li><br />
<li><a href="http://kunst1080.hatenablog.com/entry/2013/06/02/234025" target="_blank">http://kunst1080.hatenablog.com/entry/2013/06/02/234025</a></li><br />
</ul><br />
<br />
<h2>Tukubaiのmapコマンドがそれ</h2><br />
<br />
そんでもって、Tukubaiの総本山である某社のエンジニアは、シェル（シェルスクリプト）でクロス集計などは一日に何度もやっているので、それ専用のコマンドを使っています。<br />
<br />
例えば、くんすとさんのところのデータ：<br />
<br />
[bash]<br />
A Ice 130<br />
A Ice 180<br />
B Juice 120<br />
B Ice 130<br />
I OREO 210<br />
I OREO 210<br />
I OREO 210<br />
[/bash]<br />
（空白はタブではなくスペースです。）<br />
<br />
をクロス集計したければ、次のようにコマンドを使います。<br />
<br />
まずsm2という集計のコマンドで、同じキーを持つレコードを足し算します。<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat data | sort | sm2 1 2 3 3 <br />
A Ice 310<br />
B Ice 130<br />
B Juice 120<br />
I OREO 630<br />
[/bash]<br />
<br />
さて、これで1列目を縦軸、2列目を横軸に持って行きたいわけですが、mapというコマンドで一発です。<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat data | sort | sm2 1 2 3 3 | map num=1<br />
* Ice Juice OREO<br />
A 310 0 0<br />
B 130 120 0<br />
I 0 0 630<br />
[/bash]<br />
<br />
<h2>おわりに</h2><br />
<br />
わたしからも、bash（シェル）最強、と申し上げておきます。Tukubaiのオープン版は<a href="https://uec.usp-lab.com/TUKUBAI/CGI/TUKUBAI.CGI?POMPA=DOWNLOAD" target="_blank">こちら</a>と<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai" target="_blank">こちら</a>にありますのでステマしておきますね。join系のコマンドもあります。<br />
<br />
<br />
しゃっくりが止まらないので寝るます。
