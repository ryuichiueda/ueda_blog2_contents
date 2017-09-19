---
Keywords: CLI,UNIX/Linuxサーバ,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第20回記念、年末年始の浮ついた気分大粉砕シェル芸勉強会
<a href="https://blog.ueda.asia/?p=7332">問題だけページはコチラ</a>

<h2>イントロ</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/eosHmifvAQbFmL" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20-56450263" title="第20回シェル芸勉強会イントロ" target="_blank">第20回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div>

<h2>問題で使うファイル等</h2>

前回からGitHubに置くようにしました。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20</a>

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

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20/Q1" target="_blank">リポジトリ内のvol.20/Q1ディレクトリ</a>には次のように数字が書いてあるファイルが4つ入っています。

[bash]
$ ls 
file_A-1 file_A-2 file_B-1 file_B-2
$ head -n 2 *
==&gt; file_A-1 &lt;==
1
31351

==&gt; file_A-2 &lt;==
11
35

==&gt; file_B-1 &lt;==
-32
12

==&gt; file_B-2 &lt;==
912
3
[/bash]

file_A-*のグループ、file_B-*のグループからそれぞれ最大の数を探してください。他にfile_C-*、file_D-*、・・・とグループがたくさんあると想定して、1回のワンライナーで両方探すこととします。

<h3>解答</h3>

[bash]
$ grep ^ * | sed 's/-[0-9]*:/ /' | sort -k1,1 -k2,2nr |
awk '{print $2,$1}' | uniq -f 1
233333 file_A
9912 file_B
[/bash]


<h2>Q2</h2>

<a href="http://ja.uncyclopedia.info/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8" target="_blank">アンサイクロぺディアのシェル芸のページ</a>から、「カースト最上位者が日常的に書く、素数を出力するワンライナー」のコードを取得して実行してください。

<h3>解答</h3>

[bash]
$ curl -s http://ja.uncyclopedia.info/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8 |
grep eval | sed 's/^..//' | bash
[/bash]

<h2>Q3</h2>

次のファイルについて、奇数を1列目、偶数を2列目に振り分けて、奇数の列を昇順、偶数の列を降順にソートしてください。

[bash]
$ cat Q3
1
4
2
9
5
8
[/bash]

つまりこうしてください。

[bash]
1 8
5 4
9 2
[/bash]

<h3>解答</h3>

[bash]
$ paste &lt;(awk '$1%2' Q3 | sort) &lt;(awk '$1%2==0' Q3 | sort -r) | tr '\\t' ' '
1 8
5 4
9 2
$ cat Q3 | sed 's/.*[02468]$/-&amp;/' | sort | xargs |
awk '{for(i=NF/2;i&gt;=1;i--){print $(NF-i+1),-$i}}'
1 8
5 4
9 2
[/bash]

<h2>Q4</h2>

今、ログインしているサーバについて、自分の今使っているリモート端末以外の端末を抹殺してください。rootになっても構いません。

<h2>解答</h2>

もっと楽な方法がありそうですが・・・。ttyコマンドはオプションに$()で埋め込んでもうまく働きません。（ttyが端末と関係ないプロセスで立ち上がるので）。

[bash]
ueda\@remote:~$ a=$(tty | sed 's;/dev/;;') ; ps aux |
awk '$7~/pts\\/[0-9]*/' | awk -v &quot;t=$a&quot; '$7!=t' |
awk '{print $2}' | xargs sudo kill 
[/bash]


<h2>Q5</h2>

任意の二つの自然数をechoして最大公約数を求めましょう。

<h3>解答</h3>

[bash]
ueda\@remote:~$ echo 45 126 |
awk '{while($1*$2!=0){if($1&gt;$2){$1=$1-$2}else{$2=$2-$1}print}}' |
awk 'END{print $1}'
9
###Tukubai使用（こっちの方が長いが・・・）###
ueda\@remote:~$ echo 60 9 | factor | tarr num=1 | tr -d : | 
self 2 1 | sort | count 1 2 | self 1 3 | yarr num=1 |
awk 'NF&gt;2' | awk '{print $1,$2&lt;$3?$2:$3}' |
awk 'BEGIN{a=1}{a*=$1**$2}END{print a}'
[/bash]


<h2>Q6</h2>

ファイルQ6の中の人の名前について、誰が1列目と2列目の何番めに記述されているかを求めましょう。

[bash]
###スペースは全角###
$ cat Q6
山田　上田　吉田　武田
吉田　武田　上田　山田
[/bash]

解答例は次のようなものです。

[bash]
吉田 3 1
山田 1 4
上田 2 3
武田 4 2
[/bash]

<h3>解答</h3>

[bash]
$ cat Q6 | sed 's/　/ /g' | awk '{for(i=1;i&lt;=NF;i++){print $i,NR,i}}' |
sort -k1,2 | awk '{print $1,$3}' | xargs -n 4 | awk '{print $1,$2,$4}'
吉田 3 1
山田 1 4
上田 2 3
武田 4 2
[/bash]

<h2>Q7</h2>

一部分に「魚」を持つ漢字をなるべくたくさん列挙してみてください。方法はお任せします。

<h3>解答</h3>

あくまで一例で一部分ですが・・・

[bash]
$ seq 39770 40058 | xargs printf &quot;&amp;#x%x;&quot; | nkf --numchar-input 
[/bash]

<h2>Q8</h2>

次の漢数字をアラビア数字に変換しましょう。


[bash]
$ cat Q8 
五千七百三十五
四千三
四十五
九万六千二百三十三
十一
百十二
[/bash]


<h3>解答</h3>

[bash]
$ cat Q8 | sed 'y/一二三四五六七八九/１２３４５６７８９/' |
nkf -Z1 | sed 's/十/1*10+/' | sed 's/百/1*100+/' |
sed 's/千/1*1000+/' | sed 's/万/1*10000+/' |
sed 's/\\([0-9]\\)1/\\1/g' | bc
5735
4003
45
96233
11
112
[/bash]

<h2>宣伝</h2>

[amazonjs asin="4774173444" locale="JP" title="シェルプログラミング実用テクニック (Software Design plus)"]
