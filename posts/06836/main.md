---
Keywords:CLI,UNIX/Linuxサーバ,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第18回ニンニク入れますかシェル芸勉強会
問題だけのページはこちら: <a href="https://blog.ueda.asia/?p=6877">https://blog.ueda.asia/?p=6877</a><br />
過去問はこちら: <a href="https://blog.ueda.asia/?page_id=684">https://blog.ueda.asia/?page_id=684</a><br />
<br />
<h2>オープニングスライド（悪い冗談）</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/w5x7GU5sc8yQyA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/18-52211721" title="第18回シェル芸勉強会スライド" target="_blank">第18回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
今回からGitHubに置くようにしました。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18</a><br />
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
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
<br />
<table><br />
 <tr><br />
 <th>Mac,BSD系</th><br />
 <th>Linux</th><br />
 </tr><br />
 <tr><br />
 <td>gdate</td><br />
 <td>date</td><br />
 </tr><br />
 <tr><br />
 <td>gsed</td><br />
 <td>sed</td><br />
 </tr><br />
 <tr><br />
 <td>tail -r</td><br />
 <td>tac</td><br />
 </tr><br />
 <tr><br />
 <td>gtr</td><br />
 <td>tr</td><br />
 </tr><br />
 <tr><br />
 <td>gfold</td><br />
 <td>fold</td><br />
 </tr><br />
</table><br />
<br />
<h2>Q1</h2><br />
<br />
次のファイルは1列目がキー、2列目が値ですが、「オトン」と「オカン」の両方の値があるキーを探してください。<br />
<br />
[bash]<br />
$ cat text <br />
001 オトン<br />
001 オトン<br />
001 アカン<br />
002 オカン<br />
003 オトン<br />
003 ヤカン<br />
003 オカン<br />
004 オカン<br />
005 オトン<br />
005 ミカン<br />
005 アカン<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
値がオトンとオカンのレコードを抽出してuniqで1列目が重複しているレコードを探します（解答例の出力の2列目は無視で）。<br />
<br />
[bash]<br />
$ grep -e オトン -e オカン text | sort -u | uniq -w 3 -d<br />
003 オカン<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
次の２つのファイルについて、aだけにあるレコード、bだけにあるレコード、両方にあるレコードを分類して、<br />
<br />
[bash]<br />
$ cat a <br />
谷保<br />
鹿島田<br />
分倍河原<br />
川崎<br />
$ cat b<br />
分倍河原<br />
谷保<br />
登戸<br />
南多摩<br />
[/bash]<br />
<br />
次のような出力を作ってください。<br />
<br />
[bash]<br />
a 鹿島田<br />
a 川崎<br />
b 登戸<br />
b 南多摩<br />
c 谷保<br />
c 分倍河原<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
commを使ってみたかっただけです。<br />
<br />
[bash]<br />
$ comm &lt;(sort a) &lt;(sort b) | sed 's/^/\\t/' |<br />
sed 's/\\t\\t\\t/c /' | sed 's/\\t\\t/b /' | sed 's/\\t/a /' | sort<br />
a 鹿島田<br />
a 川崎<br />
b 登戸<br />
b 南多摩<br />
c 谷保<br />
c 分倍河原<br />
###別解###<br />
$ grep '' a b | awk -F: '{print $2,$1}' |<br />
awk '{a[$1]=a[$1]$2}END{for(k in a){print a[k],k}}' |<br />
sed 's/ab/c/' | sort<br />
a 鹿島田<br />
a 川崎<br />
b 登戸<br />
b 南多摩<br />
c 谷保<br />
c 分倍河原<br />
<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
次の３つのファイルについて、それぞれ書いてある数字の合計値を求めましょう。<br />
<br />
[bash]<br />
$ cat a<br />
1 2<br />
3 4 5<br />
$ cat b<br />
1 2 3<br />
<br />
$ cat c<br />
7<br />
8<br />
9<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
どうやってファイル名と値の2列のデータにするかが鍵。<br />
<br />
[bash]<br />
$ grep -o &quot;[0-9]*&quot; * |<br />
awk -F: '{x[$1]+=$2}END{for(k in x){print k,x[k]}}'<br />
a 15<br />
b 6<br />
c 24<br />
###Tukubaiを使うと楽。###<br />
$ grep -o &quot;[0-9]*&quot; * | tr : ' ' | sm2 1 1 2 2<br />
a 15<br />
b 6<br />
c 24<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
次のデータについて、<br />
<br />
[bash]<br />
$ cat cross<br />
_abcdef<br />
a_x____<br />
b______<br />
c______<br />
d______<br />
e______<br />
f___x__<br />
[/bash]<br />
<br />
次のような出力を作ってください。<br />
<br />
[bash]<br />
a-b<br />
f-d<br />
[/bash]<br />
<br />
つまり、xのついている場所の縦軸と横軸の記号を出力するワンライナーを考えてください。<br />
<br />
<h2>解答</h2><br />
<br />
ベタにAWKを使うか、Tukubaiを使うか。<br />
<br />
[bash]<br />
$ sed 's/./&amp; /g' cross |<br />
awk 'NR==1{split($0,a,&quot; &quot;)}<br />
/x/{for(i=1;i&lt;=7;i++){if($i==&quot;x&quot;){print $1 &quot;-&quot; a[i]}}}'<br />
###Tukubai使用###<br />
$ sed 's/./&amp; /g' cross | unmap num=1 |<br />
awk '/x/{print $1 &quot;-&quot; $2}'<br />
<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
次のテキストから空白行の重複だけ除去してください。つまり、2行以上の空白行を1行にまとめてください。<br />
<br />
[bash]<br />
あ<br />
あ<br />
<br />
<br />
<br />
<br />
い<br />
い<br />
<br />
う<br />
<br />
え<br />
<br />
<br />
<br />
お お<br />
お<br />
お<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
文字のある行にだけ番号をつけてuniqすればよいですね。<br />
<br />
[bash]<br />
$ grep -n '' text | sed 's/.*:$//' | uniq | sed 's/.*://'<br />
あ<br />
あ<br />
<br />
い<br />
い<br />
<br />
う<br />
<br />
え<br />
<br />
お お<br />
お<br />
お<br />
###別解###<br />
$ awk '$1{print NR,$0}!$1' text | uniq | sed 's/^[0-9]* //'<br />
###ebanさんを始めオプションを知っている人の答え（恐れ入りました）###<br />
$ cat -s text<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
チェスボードの画像ファイルを作ってください。ウェブサイトから画像をパクるのは最近いろいろ問題となっているのでやめましょう。以下は例です。解像度は任意で構いません。<br />
<br />
<a href="chess.png"><img src="chess.png" alt="chess" width="400" height="400" class="aligncenter size-full wp-image-6843" /></a><br />
<br />
<h2>解答</h2><br />
<br />
PGM形式で画像を作るのが一番簡単です。<br />
<br />
[bash]<br />
$ yes '0 1 0 1 0 1 0 1' |<br />
head -n 8 | sed '1~2s/0 1/1 0/g' | cat &lt;(echo &quot;P2 8 8 1&quot;) - &gt; a.pgm<br />
###AWKを使う場合###<br />
$ seq 1 64 | awk '{print ($1 + int((NR-1)/8))%2}' |<br />
xargs -n 8 | awk 'BEGIN{print &quot;P2&quot;,8,8,1}{print}' &gt; a.pgm<br />
[/bash]<br />
<br />
pgmが見れない。あるいは8x8ピクセルだとヤダという場合はImageMagickで変換を。<br />
<br />
[bash]<br />
$ convert -scale 400 a.pgm a.png<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
次のファイルには1組だけ同じ文字が含まれていますが、何行目と何行目にあるでしょうか？<br />
<br />
[bash]<br />
$ cat chinese_characters <br />
㔀㔁㔂㔃㔄㔅㔆㔇㔈㔉㔊㔋㔌㔍㔎㔏<br />
㔐㔑㔒㔓㔔㔕㔖㔗㔘㔙㔚㔛㔜㔝㔞㔟<br />
㔠㔡㔢㔣㔤㔥㔦㔧㔨㔩㔪㔫㔬㔭㔮㔯<br />
㔰㔱㔲㔳㔴㔵㔶㔷㔸㔹㔺㔻㔼㔽㔾㔿<br />
㕀㕁㕂㕃㕄㕅㕆㕇㕈㕉㕊㕋㕌㕍㕎㕏<br />
㕐㕑㕒㕓㕔㕕㕖㕗㕘㕙㕚㕛㕜㕝㕞㕟<br />
㕠㕡㕢㕣㕤㕥㕦㕧㕨㕩㕪㕫㕬㕭㕮㕯<br />
㕰㕱㕲㕳㕴㕵㕶㕷㕸㕹㕺㕻㕼㕽㕾㕿<br />
㖀㖁㖂㖃㖄㖅㖆㖇㖈㖉㖊㖋㖌㖍㖎㖏<br />
㖐㖑㖒㖓㖔㖕㖖㖗㖘㖙㖚㖛㖜㖝㖞㖟<br />
㖠㖡㖢㖣㖤㖥㖦㖧㖨㖩㖪㖫㖬㖭㖮㖯<br />
㖰㖱㖲㖳㖴㖵㖶㖷㖸㖹㖺㖻㖼㖽㖾㖿<br />
㗀㗁㗂㗃㗄㗅㗆㗇㗈㗉㕐㗊㗋㗌㗍㗎<br />
㗐㗑㗒㗓㗔㗕㗖㗗㗘㗙㗚㗛㗜㗝㗞㗟<br />
㗠㗡㗢㗣㗤㗥㗦㗧㗨㗩㗪㗫㗬㗭㗮㗯<br />
㗰㗱㗲㗳㗴㗵㗶㗷㗸㗹㗺㗻㗼㗽㗾㗿<br />
[/bash]<br />
<br />
<br />
<h2>解答</h2><br />
<br />
同じファイルをワンライナーで二回読み込みます。<br />
<br />
[bash]<br />
$ grep -o . chinese_characters | LANG=C sort | <br />
LANG=C uniq -d | grep -f - -n chinese_characters <br />
6:㕐㕑㕒㕓㕔㕕㕖㕗㕘㕙㕚㕛㕜㕝㕞㕟<br />
13:㗀㗁㗂㗃㗄㗅㗆㗇㗈㗉㕐㗊㗋㗌㗍㗎<br />
[/bash]<br />
<br />
LANG=Cをちゃんと付けないとダメなようです。<br />
<br />
[bash]<br />
###間違い###<br />
$ grep -o . chinese_characters | sort |<br />
uniq -d | grep -f - -n chinese_characters <br />
1:㔀㔁㔂㔃㔄㔅㔆㔇㔈㔉㔊㔋㔌㔍㔎㔏<br />
[/bash]<br />
<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
次のファイルの中に、複数回登場する数字の並びがいくつかありますが、その中で最長のものはどれでしょうか？例えば「23」という数字の並びは4つありますが、それより長い数字の列で、2回以上登場するものが存在します。<br />
<br />
[bash]<br />
$ cat number <br />
8264611130023148519839960536022802096895154738213681101003238003191122723922378922942503388843815799<br />
[/bash]<br />
<br />
<br />
<h2>解答</h2><br />
<br />
どうやって数字の並びを全通り出力するかがミソです。以下の出力のように003と922が正解です。<br />
<br />
[bash]<br />
$ cat number |<br />
awk '{for(j=1;j&lt;length($1);j++)for(i=1;i&lt;=length($1)-j+1;i++){print substr($1,i,j)}}' |<br />
sort | uniq -d | awk '{print length($1),$1}' | sort -k1,1n<br />
...<br />
2 99<br />
3 003<br />
3 922<br />
[/bash]
