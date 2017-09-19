---
Keywords: コマンド,Haskell,open
Copyright: (C) 2017 Ryuichi Ueda
---

# Haskell版のcgi-nameとketa
Haskell版のOpen usp Tukubaiのコマンド：<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/cgi-name.hs" target="_blank">cgi-namea.hs</a>と<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/keta.hs" target="_blank">keta.hs</a>をリリースしましたー。他にやることが山積みですが。

正月は実家に帰りますが基本、ずっと仕事の模様。

南無阿弥陀仏。

<h2>使い方</h2>

まずGHCでコンピャイル。
[bash]
uedamac:COMMANDS.HS ueda$ ghc keta.hs 
[1 of 1] Compiling Main ( keta.hs, keta.o )
Linking keta ...
uedamac:COMMANDS.HS ueda$ ghc cgi-name.hs 
[1 of 1] Compiling Main ( cgi-name.hs, cgi-name.o )
Linking cgi-name ...
[/bash]

<!--more-->

cgi-nameは、GETやPOSTで投げられた文字列をキーバリューの形式に整形するコマンドです。

[bash]
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | sed 's/.*?//' | ./cgi-name 
q ナリタタイシン
oq ナリタタイシン
aqs chrome..69i57j0l5.1951j0j4
sourceid chrome
espv 210
es_sm 91
ie UTF-8
[/bash]

ketaは桁揃えするコマンドで、端末で手作業でデータいじりするときにはかなり便利です。さっきの例（なぜ<a href="http://ja.wikipedia.org/wiki/%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3" target="_blank">ナリタタイシン</a>なのか自分でもよく分からんが。）

[bash]
###右揃え###
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | 
sed 's/.*?//' | ./cgi-name | ./keta
 q ナリタタイシン
 oq ナリタタイシン
 aqs chrome..69i57j0l5.1951j0j4
sourceid chrome
 espv 210
 es_sm 91
 ie UTF-8
###左揃え###
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | 
sed 's/.*?//' | ./cgi-name | ./keta --
q ナリタタイシン 
oq ナリタタイシン 
aqs chrome..69i57j0l5.1951j0j4
sourceid chrome 
espv 210 
es_sm 91 
ie UTF-8 
###桁揃えに必要な桁数を求める###
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | 
sed 's/.*?//' | ./cgi-name | ./keta -v
8 26
###1列目を8文字で右揃え、2列目を26文字で左揃え###
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | 
sed 's/.*?//' | ./cgi-name | ./keta 8 -26
 q ナリタタイシン 
 oq ナリタタイシン 
 aqs chrome..69i57j0l5.1951j0j4
sourceid chrome 
 espv 210 
 es_sm 91 
 ie UTF-8 
[/bash]


ぜひお使いください。
