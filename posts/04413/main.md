---
Keywords:勉強会,シェル芸,シェル芸勉強会,難しめ
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第14回東京居残りシェル芸勉強会
<ul><br />
 <li><br />
<a href="http://blog.ueda.asia/?p=4671" title="【問題のみ】第14回東京居残りシェル芸勉強会">問題だけ見たい人はコッチ</a></li><br />
 <li><a href="http://togetter.com/li/757291" target="_blank">まとめと別解はコッチ</a></li><br />
</ul><br />
<br />
<h1>始める前に</h1><br />
<br />
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
<h1>イントロ</h1><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/42680416" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br />
<br />
<h1>Q1</h1><br />
<br />
100!を計算してください。正確に。<br />
<br />
<!--more--><br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ seq 100 | xargs | tr ' ' '*' | bc<br />
93326215443944152681699238856266700490715968264381621468592963895217\\<br />
59999322991560894146397615651828625369792082722375825118521091686400\\<br />
0000000000000000000000<br />
ueda\@remote:~$ python -c 'import math;print math.factorial(100)'<br />
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000<br />
###中央大の飯尾先生から###<br />
ueda\@remote:~$ echo `seq 100` &quot;`yes '*' | head -99`&quot; p | dc<br />
933262154439441526816992388562667004907159682643816214685929638952175\\<br />
999932299156089414639761565182862536979208272237582511852109168640000\\<br />
00000000000000000000<br />
[/bash]<br />
<br />
<br />
<h1>Q2</h1><br />
<br />
次のseqからsed（と言ってもgsed）だけでfizzbuzzを完成させてください。<br />
<br />
[bash]<br />
ueda\@remote:~$ seq 100 | sed ...<br />
1<br />
2<br />
Fizz<br />
4<br />
Buzz<br />
Fizz<br />
7<br />
8<br />
Fizz<br />
Buzz<br />
11<br />
Fizz<br />
13<br />
14<br />
FizzBuzz<br />
16<br />
17<br />
Fizz<br />
19<br />
Buzz<br />
...<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ seq 100 | sed '5~5s/.*/Buzz/' | sed '3~3s/[0-9]*/Fizz/'<br />
[/bash]<br />
<br />
<br />
<h1>Q3</h1><br />
<br />
このうち素数はどれでしょうか？<br />
<br />
[bash]<br />
ueda\@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58 | xargs printf &quot;%d\\n&quot; |<br />
 factor | awk 'NF==2{print $2}' | xargs printf &quot;0x%02x\\n&quot;<br />
0x13<br />
0x0d<br />
[/bash]<br />
<br />
<h1>Q4</h1><br />
<br />
次の16進数（UTF-8）で書かれたメッセージを復元してください。<br />
<br />
[bash]<br />
e89fb9e3818ce9a39fe381b9e3819fe38184<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ echo e89fb9e3818ce9a39fe381b9e3819fe38184 | xxd -p -r<br />
蟹が食べたいueda\@remote:~$<br />
ueda\@remote:~$ echo e89fb9e3818ce9a39fe381b9e3819fe38184 | fold -b2 |<br />
 sed 's/^/0x/' | xargs printf '%d\\n' | LANG=C awk '{printf(&quot;%c&quot;,$1)}'<br />
蟹が食べたいueda\@remote:~$ <br />
[/bash]<br />
<br />
<br />
<h1>Q5</h1><br />
<br />
次のようなファイルを作ってください。<br />
（catするとahoとだけ出て、容量は1GB。）<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge<br />
aho<br />
ueda\@remote:~$ ls -l hoge<br />
-rw-r--r-- 1 ueda ueda 1000000000 12月 7 14:53 hoge<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
$ cat /dev/zero | head -c 999999996 | cat &lt;(echo &quot;aho&quot;) - &gt; hoge<br />
[/bash]<br />
<br />
<br />
<h1>Q6</h1><br />
<br />
日本の山を標高の高い順から並べていってください。順位と標高も一緒に出力してください。<a href="http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29" target="_blank">（こちらからcurlで持ってきて加工してください）</a><br />
<br />
おそらく力技になります。<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ curl http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29 | <br />
sed -n '/&lt;table class=&quot;sortable&quot;/,$p' | sed -n '1,/&lt;\\/table&gt;/p' | <br />
grep '^&lt;td&gt;' | grep -v jpg | sed 's/&lt;\\/*small&gt;//g' | sed 's/&lt;\\/.*$//' |<br />
 sed 's/.*&gt;//' | awk '/^[0-9][0-9]*$/{print &quot;&quot;}{printf(&quot;%s &quot;,$0)}' |<br />
 awk 'NF{print $1,$2,$4}'<br />
1 富士山 3,775.6<br />
2 北岳 3,193.2<br />
3 奥穂高岳 3,190<br />
3 間ノ岳 3,190<br />
5 槍ヶ岳 3,180<br />
6 悪沢岳 3,141<br />
7 赤石岳 3,120.53<br />
8 涸沢岳 3,110<br />
9 北穂高岳 3,106<br />
10 大喰岳 3,101<br />
...<br />
[/bash]<br />
<br />
<h1>Q7</h1><br />
<br />
分数で正確に答えを求めてください。できれば約分してください。<br />
<br />
[bash]<br />
echo '1/4 + 2/5 + 7/16 - 5/9'<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/[+-]/\\n&amp;/g' |<br />
 tr '/' ' ' | sed 's/^+ //' | sed 's/- /-/' |<br />
 awk 'BEGIN{n=0;d=1}{n=n*$2+d*$1;d=d*$2}END{print n,d}'<br />
1532 2880<br />
###約分（死ぬ）###<br />
ueda\@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/[+-]/\\n&amp;/g' |<br />
 tr '/' ' ' | sed 's/^+ //' | sed 's/- /-/' |<br />
 awk 'BEGIN{n=0;d=1}{n=n*$2+d*$1;d=d*$2}END{print n,d}' | factor |<br />
 awk 'NR==1{$1=&quot;a&quot;;print}NR==2{$1=&quot;b&quot;;print}' | tarr num=1 |<br />
 count 1 2 | self 2 1 3 | sort | yarr num=1 |<br />
 awk 'NF==5{if($3&gt;$5){print $1,$2,$3-$5}else{print $1,$4,$5-$3}}NF!=5{print}'<br />
 | grep -v ' 0$' | self 2 1 3 | sort |<br />
 awk '{a=1;for(i=0;i&lt;$3;i++){a*=$2};print $1,a}' | yarr num=1 |<br />
 awk '{a=1;for(i=2;i&lt;=NF;i++){a*=$i};print $1,a}'<br />
a 383<br />
b 720<br />
###素直に（？）Python使いましょう###<br />
ueda\@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/\\([+-]\\) /\\1/g' |<br />
 sed 's;\\([+-]*[0-9]*\\)/\\([0-9]*\\);+ Fraction(\\1,\\2);g' |<br />
 awk '{print &quot;from fractions import Fraction ; a = &quot;,$0,&quot;;print a&quot;}' |<br />
 python <br />
383/720<br />
[/bash]<br />
<br />
<h1>Q8</h1><br />
<br />
[bash]<br />
*****************************************************************<br />
[/bash]<br />
<br />
をポキポキ折ってください。<br />
<br />
[bash]<br />
###例###<br />
************************<br />
 *<br />
 *<br />
 *<br />
 **************************<br />
 *<br />
 *<br />
 *<br />
 *<br />
 *<br />
 *<br />
 **<br />
 *<br />
 ***<br />
[/bash]<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
ueda\@remote:~$ echo '*****************************************************************' |<br />
 grep -o . | awk '{r=int(rand()*10);if(r&lt;1){print}else{printf($1)}}' |<br />
 sed '1~2n;s/./&amp;\\n/g' | awk 'NF' |<br />
 awk '{for(i=0;i&lt;a;i++){printf(&quot; &quot;)}print}length($1)&gt;1{a+=length($1)-1}'<br />
************************<br />
 *<br />
 *<br />
 *<br />
 **************************<br />
 *<br />
 *<br />
 *<br />
 *<br />
 *<br />
 *<br />
 **<br />
 *<br />
 ***<br />
[/bash]
