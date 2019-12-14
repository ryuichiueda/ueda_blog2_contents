---
Keywords: CLI,Linux,UNIX/Linuxサーバ,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】第18回ニンニク入れますかシェル芸勉強会
解答はこちら: <a href="/?post=06836">/?p=6836</a>
過去問はこちら: <a href="/?page=00684">/?page_id=684</a>


<h2>オープニングスライド（悪い冗談）</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/w5x7GU5sc8yQyA" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/18-52211721" title="第18回シェル芸勉強会スライド" target="_blank">第18回シェル芸勉強会スライド</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>


<h2>問題で使うファイル等</h2>

今回からGitHubに置くようにしました。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.18</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

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

```bash
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
```

<h2>Q2</h2>

次の２つのファイルについて、aだけにあるレコード、bだけにあるレコード、両方にあるレコードを分類して、

```bash
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
```

次のような出力を作ってください。

```bash
a 鹿島田
a 川崎
b 登戸
b 南多摩
c 谷保
c 分倍河原
```

<h2>Q3</h2>

次の３つのファイルについて、それぞれ書いてある数字の合計値を求めましょう。

```bash
$ cat a
1 2
3 4 5
$ cat b
1 2 3

$ cat c
7
8
9
```

<h2>Q4</h2>

次のデータについて、

```bash
$ cat cross
_abcdef
a_x____
b______
c______
d______
e______
f___x__
```

次のような出力を作ってください。

```bash
a-b
f-d
```

つまり、xのついている場所の縦軸と横軸の記号を出力するワンライナーを考えてください。

<h2>Q5</h2>

次のテキストから空白行の重複だけ除去してください。つまり、2行以上の空白行を1行にまとめてください。

```bash
あ
あ




い
い

う

え



お お
お
お
```


<h2>Q6</h2>

チェスボードの画像ファイルを作ってください。ウェブサイトから画像をパクるのは最近いろいろ問題となっているのでやめましょう。以下は例です。解像度は任意で構いません。

<a href="/posts/06836/chess.png"><img src="/posts/06836/chess.png" alt="chess" width="400" height="400" class="aligncenter size-full wp-image-6843" /></a>


<h2>Q7</h2>

次のファイルには1組だけ同じ文字が含まれていますが、何行目と何行目にあるでしょうか？

```bash
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
```


<h2>Q8</h2>

次のファイルの中に、複数回登場する数字の並びがいくつかありますが、その中で最長のものはどれでしょうか？例えば「23」という数字の並びは4つありますが、それより長い数字の列で、2回以上登場するものが存在します。

```bash
$ cat number 
8264611130023148519839960536022802096895154738213681101003238003191122723922378922942503388843815799
```


