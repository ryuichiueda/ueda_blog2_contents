# Haskell版のcgi-nameとketa
Haskell版のOpen usp Tukubaiのコマンド：<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/cgi-name.hs" target="_blank">cgi-namea.hs</a>と<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/keta.hs" target="_blank">keta.hs</a>をリリースしましたー。他にやることが山積みですが。<br />
<br />
正月は実家に帰りますが基本、ずっと仕事の模様。<br />
<br />
南無阿弥陀仏。<br />
<br />
<h2>使い方</h2><br />
<br />
まずGHCでコンピャイル。<br />
[bash]<br />
uedamac:COMMANDS.HS ueda$ ghc keta.hs <br />
[1 of 1] Compiling Main ( keta.hs, keta.o )<br />
Linking keta ...<br />
uedamac:COMMANDS.HS ueda$ ghc cgi-name.hs <br />
[1 of 1] Compiling Main ( cgi-name.hs, cgi-name.o )<br />
Linking cgi-name ...<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
cgi-nameは、GETやPOSTで投げられた文字列をキーバリューの形式に整形するコマンドです。<br />
<br />
[bash]<br />
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | sed 's/.*?//' | ./cgi-name <br />
q ナリタタイシン<br />
oq ナリタタイシン<br />
aqs chrome..69i57j0l5.1951j0j4<br />
sourceid chrome<br />
espv 210<br />
es_sm 91<br />
ie UTF-8<br />
[/bash]<br />
<br />
ketaは桁揃えするコマンドで、端末で手作業でデータいじりするときにはかなり便利です。さっきの例（なぜ<a href="http://ja.wikipedia.org/wiki/%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3" target="_blank">ナリタタイシン</a>なのか自分でもよく分からんが。）<br />
<br />
[bash]<br />
###右揃え###<br />
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | <br />
sed 's/.*?//' | ./cgi-name | ./keta<br />
 q ナリタタイシン<br />
 oq ナリタタイシン<br />
 aqs chrome..69i57j0l5.1951j0j4<br />
sourceid chrome<br />
 espv 210<br />
 es_sm 91<br />
 ie UTF-8<br />
###左揃え###<br />
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | <br />
sed 's/.*?//' | ./cgi-name | ./keta --<br />
q ナリタタイシン <br />
oq ナリタタイシン <br />
aqs chrome..69i57j0l5.1951j0j4<br />
sourceid chrome <br />
espv 210 <br />
es_sm 91 <br />
ie UTF-8 <br />
###桁揃えに必要な桁数を求める###<br />
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | <br />
sed 's/.*?//' | ./cgi-name | ./keta -v<br />
8 26<br />
###1列目を8文字で右揃え、2列目を26文字で左揃え###<br />
uedamac:COMMANDS.HS ueda$ echo &quot;https://www.google.co.jp/search?q=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;oq=%E3%83%8A%E3%83%AA%E3%82%BF%E3%82%BF%E3%82%A4%E3%82%B7%E3%83%B3&amp;aqs=chrome..69i57j0l5.1951j0j4&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8&quot; | <br />
sed 's/.*?//' | ./cgi-name | ./keta 8 -26<br />
 q ナリタタイシン <br />
 oq ナリタタイシン <br />
 aqs chrome..69i57j0l5.1951j0j4<br />
sourceid chrome <br />
 espv 210 <br />
 es_sm 91 <br />
 ie UTF-8 <br />
[/bash]<br />
<br />
<br />
ぜひお使いください。
