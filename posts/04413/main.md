---
Keywords: 勉強会,シェル芸,シェル芸勉強会,難しめ
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第14回東京居残りシェル芸勉強会
<ul>
 <li>
<a href="/?post=04671" title="【問題のみ】第14回東京居残りシェル芸勉強会">問題だけ見たい人はコッチ</a></li>
 <li><a href="http://togetter.com/li/757291" target="_blank">まとめと別解はコッチ</a></li>
</ul>

<h1>始める前に</h1>

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

<h1>イントロ</h1>

<iframe src="//www.slideshare.net/slideshow/embed_code/42680416" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>

<h1>Q1</h1>

100!を計算してください。正確に。

<!--more-->

<h1>解答</h1>

```bash
ueda@remote:~$ seq 100 | xargs | tr ' ' '*' | bc
93326215443944152681699238856266700490715968264381621468592963895217\\
59999322991560894146397615651828625369792082722375825118521091686400\\
0000000000000000000000
ueda@remote:~$ python -c 'import math;print math.factorial(100)'
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
###中央大の飯尾先生から###
ueda@remote:~$ echo `seq 100` "`yes '*' | head -99`" p | dc
933262154439441526816992388562667004907159682643816214685929638952175\\
999932299156089414639761565182862536979208272237582511852109168640000\\
00000000000000000000
```


<h1>Q2</h1>

次のseqからsed（と言ってもgsed）だけでfizzbuzzを完成させてください。

```bash
ueda@remote:~$ seq 100 | sed ...
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
...
```

<h1>解答</h1>

```bash
ueda@remote:~$ seq 100 | sed '5~5s/.*/Buzz/' | sed '3~3s/[0-9]*/Fizz/'
```


<h1>Q3</h1>

このうち素数はどれでしょうか？

```bash
ueda@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58
```

<h1>解答</h1>

```bash
ueda@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58 | xargs printf "%d\\n" |
 factor | awk 'NF==2{print $2}' | xargs printf "0x%02x\\n"
0x13
0x0d
```

<h1>Q4</h1>

次の16進数（UTF-8）で書かれたメッセージを復元してください。

```bash
e89fb9e3818ce9a39fe381b9e3819fe38184
```

<h1>解答</h1>

```bash
ueda@remote:~$ echo e89fb9e3818ce9a39fe381b9e3819fe38184 | xxd -p -r
蟹が食べたいueda@remote:~$
ueda@remote:~$ echo e89fb9e3818ce9a39fe381b9e3819fe38184 | fold -b2 |
 sed 's/^/0x/' | xargs printf '%d\\n' | LANG=C awk '{printf("%c",$1)}'
蟹が食べたいueda@remote:~$ 
```


<h1>Q5</h1>

次のようなファイルを作ってください。
（catするとahoとだけ出て、容量は1GB。）

```bash
ueda@remote:~$ cat hoge
aho
ueda@remote:~$ ls -l hoge
-rw-r--r-- 1 ueda ueda 1000000000 12月 7 14:53 hoge
```

<h1>解答</h1>

```bash
$ cat /dev/zero | head -c 999999996 | cat <(echo "aho") - > hoge
```


<h1>Q6</h1>

日本の山を標高の高い順から並べていってください。順位と標高も一緒に出力してください。<a href="http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29" target="_blank">（こちらからcurlで持ってきて加工してください）</a>

おそらく力技になります。

<h1>解答</h1>

```bash
ueda@remote:~$ curl http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29 | 
sed -n '/<table class="sortable"/,$p' | sed -n '1,/<\\/table>/p' | 
grep '^<td>' | grep -v jpg | sed 's/<\\/*small>//g' | sed 's/<\\/.*$//' |
 sed 's/.*>//' | awk '/^[0-9][0-9]*$/{print ""}{printf("%s ",$0)}' |
 awk 'NF{print $1,$2,$4}'
1 富士山 3,775.6
2 北岳 3,193.2
3 奥穂高岳 3,190
3 間ノ岳 3,190
5 槍ヶ岳 3,180
6 悪沢岳 3,141
7 赤石岳 3,120.53
8 涸沢岳 3,110
9 北穂高岳 3,106
10 大喰岳 3,101
...
```

<h1>Q7</h1>

分数で正確に答えを求めてください。できれば約分してください。

```bash
echo '1/4 + 2/5 + 7/16 - 5/9'
```

<h1>解答</h1>

```bash
ueda@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/[+-]/\\n&/g' |
 tr '/' ' ' | sed 's/^+ //' | sed 's/- /-/' |
 awk 'BEGIN{n=0;d=1}{n=n*$2+d*$1;d=d*$2}END{print n,d}'
1532 2880
###約分（死ぬ）###
ueda@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/[+-]/\\n&/g' |
 tr '/' ' ' | sed 's/^+ //' | sed 's/- /-/' |
 awk 'BEGIN{n=0;d=1}{n=n*$2+d*$1;d=d*$2}END{print n,d}' | factor |
 awk 'NR==1{$1="a";print}NR==2{$1="b";print}' | tarr num=1 |
 count 1 2 | self 2 1 3 | sort | yarr num=1 |
 awk 'NF==5{if($3>$5){print $1,$2,$3-$5}else{print $1,$4,$5-$3}}NF!=5{print}'
 | grep -v ' 0$' | self 2 1 3 | sort |
 awk '{a=1;for(i=0;i<$3;i++){a*=$2};print $1,a}' | yarr num=1 |
 awk '{a=1;for(i=2;i<=NF;i++){a*=$i};print $1,a}'
a 383
b 720
###素直に（？）Python使いましょう###
ueda@remote:~$ echo '1/4 + 2/5 + 7/16 - 5/9' | sed 's/\\([+-]\\) /\\1/g' |
 sed 's;\\([+-]*[0-9]*\\)/\\([0-9]*\\);+ Fraction(\\1,\\2);g' |
 awk '{print "from fractions import Fraction ; a = ",$0,";print a"}' |
 python 
383/720
```

<h1>Q8</h1>

```bash
*****************************************************************
```

をポキポキ折ってください。

```bash
###例###
************************
 *
 *
 *
 **************************
 *
 *
 *
 *
 *
 *
 **
 *
 ***
```

<h1>解答</h1>

```bash
ueda@remote:~$ echo '*****************************************************************' |
 grep -o . | awk '{r=int(rand()*10);if(r<1){print}else{printf($1)}}' |
 sed '1~2n;s/./&\\n/g' | awk 'NF' |
 awk '{for(i=0;i<a;i++){printf(" ")}print}length($1)>1{a+=length($1)-1}'
************************
 *
 *
 *
 **************************
 *
 *
 *
 *
 *
 *
 **
 *
 ***
```
