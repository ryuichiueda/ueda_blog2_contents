# 【問題と解答例】第12回本当は怖くないシェル芸勉強会
<a href="http://blog.ueda.asia/?page_id=684" target="_blank">過去問はこちら</a><br />
<br />
<a href="http://blog.ueda.asia/?p=3569">問題のみのページはこちら</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/37591306" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/ryuichiueda/20140802uspstudy" title="2014/08/02 第12回シェル芸勉強会イントロ" target="_blank">2014/08/02 第12回シェル芸勉強会イントロ</a> </strong> from <strong><a href="http://www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<!--more--><br />
<h2>環境</h2><br />
<br />
Linuxで解答を作ったのでMacな方は次のようにコマンドの読み替えを。<br />
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
次のように、画面にバッテンを描いてください。（この出力例の大きさは21x21です。）<br />
<br />
[bash]<br />
x x<br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
 x x <br />
x x<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ yes | head -n 21 |<br />
awk '{for(i=1;i&lt;=21;i++){<br />
if(i==NR || 22-i==NR){printf &quot;x&quot;}else{printf &quot; &quot;}}<br />
print &quot;&quot;}'<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
小問1. 次のechoの出力から回文を完成させてください。<br />
<br />
[bash]<br />
ueda\@remote:~$ echo たけやぶ<br />
###このようにワンライナーで出力を作る###<br />
ueda\@remote:~$ echo たけやぶ | ...<br />
たけやぶやけた<br />
[/bash]<br />
<br />
小問2. 次のファイルの各行について回文を完成させてください。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat kaibun <br />
たけやぶ<br />
わたしまけ<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
###小問1###<br />
ueda\@remote:~$ echo たけやぶ | <br />
while read s ; do echo $s ; rev &lt;&lt;&lt; $s ; done | <br />
xargs | sed 's/ .//'<br />
たけやぶやけた<br />
ueda\@remote:~$ echo たけやぶ | sed 's/./&amp; /g' |<br />
awk '{printf $0;for(i=NF-1;i&gt;=1;i--){printf $i};print &quot;&quot;}' |<br />
tr -d ' '<br />
たけやぶやけた<br />
###鳥海さん解答###<br />
echo たけやぶ | ( read s ; echo $s ; rev &lt;&lt;&lt; $s ) | xargs | sed 's/. //'<br />
###小問2###<br />
ueda\@remote:~/tmp$ rev kaibun | paste kaibun - | sed 's/.\\t//'<br />
たけやぶやけた<br />
わたしまけましたわ<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
ウェブ等からデータを取得して南武線の駅名のリストを作ってください。<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~$ curl http://ja.wikipedia.org/wiki/%E5%8D%97%E6%AD%A6%E7%B7%9A | <br />
sed -n '/南武線新旧 快速停車駅/,$p' | sed -n '/川崎/,$p' | <br />
sed -n '1,/立川/p' | sed 's/&lt;[^&lt;]*&gt;//g'<br />
ueda\@remote:~$ curl 'http://express.heartrails.com/api/json?method=getStations&amp;line=JR南武線' |<br />
 jq . | grep '&quot;name&quot;' | awk '{print $2}' | tr -d '&quot;,'<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
北から順（正確には都道府県番号順）に並べてください。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat pref <br />
鹿児島県<br />
青森県<br />
大阪府<br />
群馬県<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
Webを利用します。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ curl http://elze.tanosii.net/d/kenmei.htm |<br />
nkf -wLux | grep &quot;[都道府県]&quot; |<br />
grep -f ./pref | sed 's/[^&gt;]*&gt;//' | sed 's/(.*//'<br />
青森県<br />
群馬県<br />
大阪府<br />
鹿児島県<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
各行の数字を大きい順にソートしてください。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat input <br />
A 31 1234 -42 4<br />
B 10 31.1 -34 94<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat input | <br />
awk '{for(i=2;i&lt;=NF;i++){print $1,$i}}' | <br />
sort -k1,1 -k2,2nr | <br />
awk '{if(a==$1){printf &quot; &quot;$2}else{print &quot;&quot;;printf $0;a=$1}}' | <br />
awk 'NF!=0'<br />
A 1234 31 4 -42<br />
B 94 31.1 10 -34<br />
###tukubai使用###<br />
ueda\@remote:~/tmp$ cat input | tarr num=1 | <br />
sort -k1,1 -k2,2nr | yarr num=1<br />
A 1234 31 4 -42<br />
B 94 31.1 10 -34<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
次のファイルについてグラフを作ってください。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat num <br />
5<br />
3<br />
4<br />
10<br />
2<br />
[/bash]<br />
<br />
このような出力を作ります。<br />
<br />
[bash]<br />
 5 *****<br />
 3 ***<br />
 4 ****<br />
10 **********<br />
 2 **<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat num | <br />
awk '{printf(&quot;%2d &quot;,$1);for(i=0;i&lt;$1;i++){printf &quot;*&quot;}print &quot;&quot;}'<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
Q6のグラフを次のように縦にしてください。<br />
（多少ズレてもよしとします。）<br />
<br />
[bash]<br />
 * <br />
 * <br />
 * <br />
 * <br />
 * <br />
* * <br />
* * * <br />
* * * * <br />
* * * * *<br />
* * * * *<br />
5 3 4 10 2<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat num | <br />
awk '{printf $1&quot; &quot;;for(i=0;i&lt;$1;i++){printf &quot;* &quot;}<br />
for(i=$1;i&lt;=15;i++){printf &quot;_ &quot;};print &quot;&quot;}' |<br />
 awk '{for(i=1;i&lt;=NF;i++){a[NR,i]=$i}}<br />
END{for(i=1;i&lt;=15;i++)<br />
{for(j=1;j&lt;=NR;j++){printf a[j,i]&quot; &quot;}print &quot;&quot;}}' | <br />
tac | sed -n '/\\*/,$p' | tr _ ' '<br />
###tukubai使用###<br />
ueda\@remote:~/tmp$ cat num | <br />
awk '{printf $1&quot; &quot;;<br />
for(i=0;i&lt;$1;i++){printf &quot;* &quot;}<br />
for(i=$1;i&lt;=15;i++){printf &quot;_ &quot;};print &quot;&quot;}' |<br />
 tateyoko | tac | keta | sed -n '/\\*/,$p' | tr _ ' '<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
次のデータは、何かの試合の結果ですが、各チームが何勝何敗だったかを集計してください。引き分けは無いと仮定して構いません。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat result <br />
A-B 1-2<br />
B-A 3-1<br />
C-A 1-0<br />
B-C 5-4<br />
C-B 2-1<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ cat result | tr '-' ' ' | <br />
awk '{print $1,$2,($3&gt;$4)?&quot;W L&quot;:&quot;L W&quot;}' | <br />
awk '{print $1,$3;print $2,$4}' | <br />
awk '$2==&quot;L&quot;{L[$1]++}$2==&quot;W&quot;{W[$1]++}<br />
END{for(w in W){print w,W[w]&quot;勝&quot;};for(l in L){print l,L[l]&quot;負&quot;}}' |<br />
 sort<br />
A 3負<br />
B 1負<br />
B 3勝<br />
C 1負<br />
C 2勝<br />
###tukubai###<br />
ueda\@remote:~/tmp$ cat result | tr '-' ' ' | <br />
awk '{if($3&gt;$4){print $1,&quot;W&quot;;print $2,&quot;L&quot;}<br />
else{print $2,&quot;W&quot;;print $1,&quot;L&quot;}}' | <br />
sort | count 1 2 | map num=1<br />
* L W<br />
A 3 0<br />
B 1 3<br />
C 1 2<br />
[/bash]<br />
<br />
<br />

