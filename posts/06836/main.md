---
Keywords: CLI,UNIX/Linuxサーバ,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第18回ニンニク入れますかシェル芸勉強会
問題だけのページはこちら: <a href="https://blog.ueda.asia/?p=6877">https://blog.ueda.asia/?p=6877</a>
過去問はこちら: <a href="https://blog.ueda.asia/?page_id=684">https://blog.ueda.asia/?page_id=684</a>

<h2>オープニングスライド（悪い冗談）</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/w5x7GU5sc8yQyA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/18-52211721" title="第18回シェル芸勉強会スライド" target="_blank">第18回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h2>問題で使うファイル等</h2>

今回からGitHubに置くようにしました。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18</a>

にあります。

クローンは以下のようにお願いします。

[bash]
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
[/bash]

<h2>環境</h2>
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>

<h2>Q1</h2>

次のファイルは1列目がキー、2列目が値ですが、「オトン」と「オカン」の両方の値があるキーを探してください。

[bash]
$ cat text 
001 オトン
001 オトン
001 アカン
002 オカン
003 オトン
003 ヤカン
003 オカン
004 オカン
005 オトン
005 ミカン
005 アカン
[/bash]

<h2>解答</h2>

値がオトンとオカンのレコードを抽出してuniqで1列目が重複しているレコードを探します（解答例の出力の2列目は無視で）。

[bash]
$ grep -e オトン -e オカン text | sort -u | uniq -w 3 -d
003 オカン
[/bash]

<h2>Q2</h2>

次の２つのファイルについて、aだけにあるレコード、bだけにあるレコード、両方にあるレコードを分類して、

[bash]
$ cat a 
谷保
鹿島田
分倍河原
川崎
$ cat b
分倍河原
谷保
登戸
南多摩
[/bash]

次のような出力を作ってください。

[bash]
a 鹿島田
a 川崎
b 登戸
b 南多摩
c 谷保
c 分倍河原
[/bash]

<h2>解答</h2>

commを使ってみたかっただけです。

[bash]
$ comm &lt;(sort a) &lt;(sort b) | sed 's/^/\\t/' |
sed 's/\\t\\t\\t/c /' | sed 's/\\t\\t/b /' | sed 's/\\t/a /' | sort
a 鹿島田
a 川崎
b 登戸
b 南多摩
c 谷保
c 分倍河原
###別解###
$ grep '' a b | awk -F: '{print $2,$1}' |
awk '{a[$1]=a[$1]$2}END{for(k in a){print a[k],k}}' |
sed 's/ab/c/' | sort
a 鹿島田
a 川崎
b 登戸
b 南多摩
c 谷保
c 分倍河原

[/bash]

<h2>Q3</h2>

次の３つのファイルについて、それぞれ書いてある数字の合計値を求めましょう。

[bash]
$ cat a
1 2
3 4 5
$ cat b
1 2 3

$ cat c
7
8
9
[/bash]

<h2>解答</h2>

どうやってファイル名と値の2列のデータにするかが鍵。

[bash]
$ grep -o &quot;[0-9]*&quot; * |
awk -F: '{x[$1]+=$2}END{for(k in x){print k,x[k]}}'
a 15
b 6
c 24
###Tukubaiを使うと楽。###
$ grep -o &quot;[0-9]*&quot; * | tr : ' ' | sm2 1 1 2 2
a 15
b 6
c 24
[/bash]

<h2>Q4</h2>

次のデータについて、

[bash]
$ cat cross
_abcdef
a_x____
b______
c______
d______
e______
f___x__
[/bash]

次のような出力を作ってください。

[bash]
a-b
f-d
[/bash]

つまり、xのついている場所の縦軸と横軸の記号を出力するワンライナーを考えてください。

<h2>解答</h2>

ベタにAWKを使うか、Tukubaiを使うか。

[bash]
$ sed 's/./&amp; /g' cross |
awk 'NR==1{split($0,a,&quot; &quot;)}
/x/{for(i=1;i&lt;=7;i++){if($i==&quot;x&quot;){print $1 &quot;-&quot; a[i]}}}'
###Tukubai使用###
$ sed 's/./&amp; /g' cross | unmap num=1 |
awk '/x/{print $1 &quot;-&quot; $2}'

[/bash]

<h2>Q5</h2>

次のテキストから空白行の重複だけ除去してください。つまり、2行以上の空白行を1行にまとめてください。

[bash]
あ
あ




い
い

う

え



お お
お
お
[/bash]

<h2>解答</h2>

文字のある行にだけ番号をつけてuniqすればよいですね。

[bash]
$ grep -n '' text | sed 's/.*:$//' | uniq | sed 's/.*://'
あ
あ

い
い

う

え

お お
お
お
###別解###
$ awk '$1{print NR,$0}!$1' text | uniq | sed 's/^[0-9]* //'
###ebanさんを始めオプションを知っている人の答え（恐れ入りました）###
$ cat -s text
[/bash]

<h2>Q6</h2>

チェスボードの画像ファイルを作ってください。ウェブサイトから画像をパクるのは最近いろいろ問題となっているのでやめましょう。以下は例です。解像度は任意で構いません。

<a href="chess.png"><img src="chess.png" alt="chess" width="400" height="400" class="aligncenter size-full wp-image-6843" /></a>

<h2>解答</h2>

PGM形式で画像を作るのが一番簡単です。

[bash]
$ yes '0 1 0 1 0 1 0 1' |
head -n 8 | sed '1~2s/0 1/1 0/g' | cat &lt;(echo &quot;P2 8 8 1&quot;) - &gt; a.pgm
###AWKを使う場合###
$ seq 1 64 | awk '{print ($1 + int((NR-1)/8))%2}' |
xargs -n 8 | awk 'BEGIN{print &quot;P2&quot;,8,8,1}{print}' &gt; a.pgm
[/bash]

pgmが見れない。あるいは8x8ピクセルだとヤダという場合はImageMagickで変換を。

[bash]
$ convert -scale 400 a.pgm a.png
[/bash]

<h2>Q7</h2>

次のファイルには1組だけ同じ文字が含まれていますが、何行目と何行目にあるでしょうか？

[bash]
$ cat chinese_characters 
㔀㔁㔂㔃㔄㔅㔆㔇㔈㔉㔊㔋㔌㔍㔎㔏
㔐㔑㔒㔓㔔㔕㔖㔗㔘㔙㔚㔛㔜㔝㔞㔟
㔠㔡㔢㔣㔤㔥㔦㔧㔨㔩㔪㔫㔬㔭㔮㔯
㔰㔱㔲㔳㔴㔵㔶㔷㔸㔹㔺㔻㔼㔽㔾㔿
㕀㕁㕂㕃㕄㕅㕆㕇㕈㕉㕊㕋㕌㕍㕎㕏
㕐㕑㕒㕓㕔㕕㕖㕗㕘㕙㕚㕛㕜㕝㕞㕟
㕠㕡㕢㕣㕤㕥㕦㕧㕨㕩㕪㕫㕬㕭㕮㕯
㕰㕱㕲㕳㕴㕵㕶㕷㕸㕹㕺㕻㕼㕽㕾㕿
㖀㖁㖂㖃㖄㖅㖆㖇㖈㖉㖊㖋㖌㖍㖎㖏
㖐㖑㖒㖓㖔㖕㖖㖗㖘㖙㖚㖛㖜㖝㖞㖟
㖠㖡㖢㖣㖤㖥㖦㖧㖨㖩㖪㖫㖬㖭㖮㖯
㖰㖱㖲㖳㖴㖵㖶㖷㖸㖹㖺㖻㖼㖽㖾㖿
㗀㗁㗂㗃㗄㗅㗆㗇㗈㗉㕐㗊㗋㗌㗍㗎
㗐㗑㗒㗓㗔㗕㗖㗗㗘㗙㗚㗛㗜㗝㗞㗟
㗠㗡㗢㗣㗤㗥㗦㗧㗨㗩㗪㗫㗬㗭㗮㗯
㗰㗱㗲㗳㗴㗵㗶㗷㗸㗹㗺㗻㗼㗽㗾㗿
[/bash]


<h2>解答</h2>

同じファイルをワンライナーで二回読み込みます。

[bash]
$ grep -o . chinese_characters | LANG=C sort | 
LANG=C uniq -d | grep -f - -n chinese_characters 
6:㕐㕑㕒㕓㕔㕕㕖㕗㕘㕙㕚㕛㕜㕝㕞㕟
13:㗀㗁㗂㗃㗄㗅㗆㗇㗈㗉㕐㗊㗋㗌㗍㗎
[/bash]

LANG=Cをちゃんと付けないとダメなようです。

[bash]
###間違い###
$ grep -o . chinese_characters | sort |
uniq -d | grep -f - -n chinese_characters 
1:㔀㔁㔂㔃㔄㔅㔆㔇㔈㔉㔊㔋㔌㔍㔎㔏
[/bash]



<h2>Q8</h2>

次のファイルの中に、複数回登場する数字の並びがいくつかありますが、その中で最長のものはどれでしょうか？例えば「23」という数字の並びは4つありますが、それより長い数字の列で、2回以上登場するものが存在します。

[bash]
$ cat number 
8264611130023148519839960536022802096895154738213681101003238003191122723922378922942503388843815799
[/bash]


<h2>解答</h2>

どうやって数字の並びを全通り出力するかがミソです。以下の出力のように003と922が正解です。

[bash]
$ cat number |
awk '{for(j=1;j&lt;length($1);j++)for(i=1;i&lt;=length($1)-j+1;i++){print substr($1,i,j)}}' |
sort | uniq -d | awk '{print length($1),$1}' | sort -k1,1n
...
2 99
3 003
3 922
[/bash]
