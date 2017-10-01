---
Keywords: CLI,USP友の会,問題,シェル芸,シェル芸勉強会,解答
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第12回本当は怖くないシェル芸勉強会
<a href="/?page=00684" target="_blank">過去問はこちら</a>

<a href="/?post=03569">問題のみのページはこちら</a>

<h2>イントロ</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/37591306" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/ryuichiueda/20140802uspstudy" title="2014/08/02 第12回シェル芸勉強会イントロ" target="_blank">2014/08/02 第12回シェル芸勉強会イントロ</a> </strong> from <strong><a href="http://www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>
<!--more-->
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

<h2>Q1</h2>

次のように、画面にバッテンを描いてください。（この出力例の大きさは21x21です。）

```bash
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
```

<h2>解答</h2>

```bash
ueda@remote:~$ yes | head -n 21 |
awk '{for(i=1;i<=21;i++){
if(i==NR || 22-i==NR){printf "x"}else{printf " "}}
print ""}'
```


<h2>Q2</h2>

小問1. 次のechoの出力から回文を完成させてください。

```bash
ueda@remote:~$ echo たけやぶ
###このようにワンライナーで出力を作る###
ueda@remote:~$ echo たけやぶ | ...
たけやぶやけた
```

小問2. 次のファイルの各行について回文を完成させてください。

```bash
ueda@remote:~/tmp$ cat kaibun 
たけやぶ
わたしまけ
```

<h2>解答</h2>

```bash
###小問1###
ueda@remote:~$ echo たけやぶ | 
while read s ; do echo $s ; rev <<< $s ; done | 
xargs | sed 's/ .//'
たけやぶやけた
ueda@remote:~$ echo たけやぶ | sed 's/./& /g' |
awk '{printf $0;for(i=NF-1;i>=1;i--){printf $i};print ""}' |
tr -d ' '
たけやぶやけた
###鳥海さん解答###
echo たけやぶ | ( read s ; echo $s ; rev <<< $s ) | xargs | sed 's/. //'
###小問2###
ueda@remote:~/tmp$ rev kaibun | paste kaibun - | sed 's/.\\t//'
たけやぶやけた
わたしまけましたわ
```

<h2>Q3</h2>

ウェブ等からデータを取得して南武線の駅名のリストを作ってください。

<h2>解答</h2>

```bash
ueda@remote:~$ curl http://ja.wikipedia.org/wiki/%E5%8D%97%E6%AD%A6%E7%B7%9A | 
sed -n '/南武線新旧 快速停車駅/,$p' | sed -n '/川崎/,$p' | 
sed -n '1,/立川/p' | sed 's/<[^<]*>//g'
ueda@remote:~$ curl 'http://express.heartrails.com/api/json?method=getStations&line=JR南武線' |
 jq . | grep '"name"' | awk '{print $2}' | tr -d '",'
```

<h2>Q4</h2>

北から順（正確には都道府県番号順）に並べてください。

```bash
ueda@remote:~/tmp$ cat pref 
鹿児島県
青森県
大阪府
群馬県
```

<h2>解答</h2>

Webを利用します。

```bash
ueda@remote:~/tmp$ curl http://elze.tanosii.net/d/kenmei.htm |
nkf -wLux | grep "[都道府県]" |
grep -f ./pref | sed 's/[^>]*>//' | sed 's/(.*//'
青森県
群馬県
大阪府
鹿児島県
```

<h2>Q5</h2>

各行の数字を大きい順にソートしてください。

```bash
ueda@remote:~/tmp$ cat input 
A 31 1234 -42 4
B 10 31.1 -34 94
```

<h2>解答</h2>

```bash
ueda@remote:~/tmp$ cat input | 
awk '{for(i=2;i<=NF;i++){print $1,$i}}' | 
sort -k1,1 -k2,2nr | 
awk '{if(a==$1){printf " "$2}else{print "";printf $0;a=$1}}' | 
awk 'NF!=0'
A 1234 31 4 -42
B 94 31.1 10 -34
###tukubai使用###
ueda@remote:~/tmp$ cat input | tarr num=1 | 
sort -k1,1 -k2,2nr | yarr num=1
A 1234 31 4 -42
B 94 31.1 10 -34
```

<h2>Q6</h2>

次のファイルについてグラフを作ってください。

```bash
ueda@remote:~/tmp$ cat num 
5
3
4
10
2
```

このような出力を作ります。

```bash
 5 *****
 3 ***
 4 ****
10 **********
 2 **
```

<h2>解答</h2>

```bash
ueda@remote:~/tmp$ cat num | 
awk '{printf("%2d ",$1);for(i=0;i<$1;i++){printf "*"}print ""}'
```

<h2>Q7</h2>

Q6のグラフを次のように縦にしてください。
（多少ズレてもよしとします。）

```bash
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
```

<h2>解答</h2>

```bash
ueda@remote:~/tmp$ cat num | 
awk '{printf $1" ";for(i=0;i<$1;i++){printf "* "}
for(i=$1;i<=15;i++){printf "_ "};print ""}' |
 awk '{for(i=1;i<=NF;i++){a[NR,i]=$i}}
END{for(i=1;i<=15;i++)
{for(j=1;j<=NR;j++){printf a[j,i]" "}print ""}}' | 
tac | sed -n '/\\*/,$p' | tr _ ' '
###tukubai使用###
ueda@remote:~/tmp$ cat num | 
awk '{printf $1" ";
for(i=0;i<$1;i++){printf "* "}
for(i=$1;i<=15;i++){printf "_ "};print ""}' |
 tateyoko | tac | keta | sed -n '/\\*/,$p' | tr _ ' '
```

<h2>Q8</h2>

次のデータは、何かの試合の結果ですが、各チームが何勝何敗だったかを集計してください。引き分けは無いと仮定して構いません。

```bash
ueda@remote:~/tmp$ cat result 
A-B 1-2
B-A 3-1
C-A 1-0
B-C 5-4
C-B 2-1
```

<h2>解答</h2>

```bash
ueda@remote:~/tmp$ cat result | tr '-' ' ' | 
awk '{print $1,$2,($3>$4)?"W L":"L W"}' | 
awk '{print $1,$3;print $2,$4}' | 
awk '$2=="L"{L[$1]++}$2=="W"{W[$1]++}
END{for(w in W){print w,W[w]"勝"};for(l in L){print l,L[l]"負"}}' |
 sort
A 3負
B 1負
B 3勝
C 1負
C 2勝
###tukubai###
ueda@remote:~/tmp$ cat result | tr '-' ' ' | 
awk '{if($3>$4){print $1,"W";print $2,"L"}
else{print $2,"W";print $1,"L"}}' | 
sort | count 1 2 | map num=1
* L W
A 3 0
B 1 3
C 1 2
```



