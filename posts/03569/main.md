---
Keywords: USP友の会,勉強会,問題,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題だけ】第12回本当は怖くないシェル芸勉強会
<h2>環境</h2>

Linuxで解答を作ったのでMacな方は次のようにコマンドの読み替えを。

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
<!--more-->
<h2>Q1</h2>

次のように、画面にバッテンを描いてください。（この出力例の大きさは21x21です。）

[bash]
x x
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
 x x 
x x
[/bash]


<h2>Q2</h2>

小問1. 次のechoの出力から回文を完成させてください。

[bash]
ueda\@remote:~$ echo たけやぶ
###このようにワンライナーで出力を作る###
ueda\@remote:~$ echo たけやぶ | ...
たけやぶやけた
[/bash]

小問2. 次のファイルの各行について回文を完成させてください。

[bash]
ueda\@remote:~/tmp$ cat kaibun 
たけやぶ
わたしまけ
[/bash]

<h2>Q3</h2>

ウェブ等からデータを取得して南武線の駅名のリストを作ってください。

<h2>Q4</h2>

北から順（正確には都道府県番号順）に並べてください。

[bash]
ueda\@remote:~/tmp$ cat pref 
鹿児島県
青森県
大阪府
群馬県
[/bash]

<h2>Q5</h2>

各行の数字を大きい順にソートしてください。

[bash]
ueda\@remote:~/tmp$ cat input 
A 31 1234 -42 4
B 10 31.1 -34 94
[/bash]


<h2>Q6</h2>

次のファイルについてグラフを作ってください。

[bash]
ueda\@remote:~/tmp$ cat num 
5
3
4
10
2
[/bash]

このような出力を作ります。

[bash]
 5 *****
 3 ***
 4 ****
10 **********
 2 **
[/bash]

<h2>Q7</h2>

Q6のグラフを次のように縦にしてください。
（多少ズレてもよしとします。）

[bash]
 * 
 * 
 * 
 * 
 * 
* * 
* * * 
* * * * 
* * * * *
* * * * *
5 3 4 10 2
[/bash]


<h2>Q8</h2>

次のデータは、何かの試合の結果ですが、各チームが何勝何敗だったかを集計してください。引き分けは無いと仮定して構いません。

[bash]
ueda\@remote:~/tmp$ cat result 
A-B 1-2
B-A 3-1
C-A 1-0
B-C 5-4
C-B 2-1
[/bash]



