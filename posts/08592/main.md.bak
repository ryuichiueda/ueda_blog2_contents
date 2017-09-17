# 【問題と解答】第24回◯◯o◯裏番組シェル芸勉強会
問題のみのページは<a href="https://blog.ueda.asia/?p=8639">こちら</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<ul><br />
	<li><a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac24%e5%9b%9e%e2%97%af%e2%97%afo%e2%97%af%e8%a3%8f%e7%95%aa%e7%b5%84%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">スライドのリンク</a></li><br />
</ul><br />
<br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
GitHubにあります。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24</a><br />
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
<br />
今回はUbuntu Linux 16.04で解答例を作りました。<br />
<br />
<h2>Q1</h2><br />
<br />
[bash]<br />
$ cat Q1<br />
玉子 卵 玉子 玉子 玉子 玉子<br />
玉子 玉子 卵 卵 卵 玉子<br />
卵 玉子 卵 玉子 玉子 玉子<br />
卵 玉子 卵 卵 卵 卵<br />
玉子 卵 玉子<br />
[/bash]<br />
<br />
上のようなQ1ファイルについて、次のような出力を得てください。<br />
<br />
<br />
[bash]<br />
玉子:5 卵:1 <br />
玉子:3 卵:3 <br />
玉子:4 卵:2 <br />
玉子:1 卵:5 <br />
玉子:2 卵:1 <br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
AWKの力技になります。力技でない方法を募集。<br />
<br />
[bash]<br />
$ cat Q1 |<br />
 awk '{for(i=1;i&lt;=NF;i++){a[$i]++};for(k in a){printf(&quot;%s:%d &quot;,k,a[k]);a[k]=0}print &quot;&quot;}'<br />
玉子:5 卵:1 <br />
玉子:3 卵:3 <br />
玉子:4 卵:2 <br />
玉子:1 卵:5 <br />
玉子:2 卵:1 <br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
次のようなテキストについて、繰り返し出てきた文字の2つ目以降を省いて出力してください。例えばQ2のファイル<br />
<br />
[bash]<br />
$ cat Q2<br />
へのへのもへじ<br />
[/bash]<br />
<br />
の場合、「へのもじ」が正解の出力になります。<br />
<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat Q2 | grep -o . | nl | sort -k2,2 -k1,1n |<br />
 uniq -f 1 | sort | awk '{printf $2}' | xargs<br />
へのもじ<br />
$ cat Q2 | grep -o . | awk '{if(!a[$1]){printf $1};a[$1]=1}END{print &quot;&quot;}'<br />
へのもじ<br />
$ &lt; Q2 grep -o . | awk '{if(!a[$1]){printf $1};a[$1]=1}' | xargs<br />
へのもじ<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
[bash]<br />
$ cat Q3<br />
金 日成<br />
キム ワイプ<br />
金 正日<br />
キム タオル<br />
金 正男<br />
[/bash]<br />
<br />
というデータを、<br />
<br />
[bash]<br />
%%<br />
キム タオル<br />
キム ワイプ<br />
%%<br />
金 正男<br />
金 正日<br />
金 日成<br />
%%<br />
[/bash]<br />
<br />
というように第一フィールドをキーにして%%でレコードを区切ってください。awkを使ってできた人は、awkを使わないでやってみてください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ sort Q3 | awk '{if($1!=a){print &quot;%%&quot;;print;a=$1}else{print}}END{print &quot;%%&quot;}'<br />
%%<br />
キム タオル<br />
キム ワイプ<br />
%%<br />
金 正男<br />
金 正日<br />
金 日成<br />
%%<br />
$ sort Q2 | rev | uniq --group=both -f 1 | rev | sed 's/^$/%%/'<br />
%%<br />
キム タオル<br />
キム ワイプ<br />
%%<br />
金 正男<br />
金 正日<br />
金 日成<br />
%%<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
Q4.xlsxのA1のセルには数字が書いてあります。その数字を出力してください。A4には文字列が書いてあるので余裕がある人はそれも特定してみましょう。<br />
<br />
<h3>解答</h3><br />
<br />
A1のセル（数字の読み方）<br />
<br />
[bash]<br />
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml | sed 's;&lt;/c&gt;;&amp;\\n;g' |<br />
 grep -o '&lt;c.*&lt;/c&gt;' | grep A1 | sed 's;.*&lt;v&gt;;;' | sed 's;&lt;.*;;'<br />
114514<br />
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml | hxselect -s '\\n' c |<br />
 grep A1 | hxselect -c v<br />
114514<br />
[/bash]<br />
<br />
A2の文字列の読み方。シートには文字列のIDが書いてあるのでこれで文字列のシートを読んで特定。<br />
<br />
[bash]<br />
###これで6番目（0番から始まるので7番目）の文字列とわかる###<br />
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml |<br />
 hxselect -s '\\n' c | grep A4<br />
&lt;c r=&quot;A4&quot; t=&quot;s&quot;&gt;&lt;v&gt;6&lt;/v&gt;&lt;/c&gt;<br />
###抽出###<br />
$ unzip -p Q4.xlsx xl/sharedStrings.xml |<br />
 hxselect -s '\\n' si | awk 'NR==7'<br />
&lt;si&gt;&lt;t&gt;エクシェル芸&lt;/t&gt;&lt;rPh sb=&quot;5&quot; eb=&quot;6&quot;&gt;&lt;t&gt;ゲ&lt;/t&gt;&lt;/rPh&gt;&lt;phoneticPr fontId=&quot;1&quot;/&gt;&lt;/si&gt;<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
ファイルQ5について、xに好きな数を代入して各行の式を計算してください。<br />
<br />
[bash]<br />
$ cat Q5<br />
x + x^2<br />
x + 1/x<br />
x*x*x<br />
[/bash]<br />
<br />
余裕のある人は、例えばxに2を代入したければ、<br />
<br />
[bash]<br />
$ echo 2 | ...<br />
[/bash]<br />
<br />
というようにecho <代入したい数>から始めてワンライナーで解いてみてください。<br />
<br />
<h3>解答</h3><br />
<br />
例えばこれで解けます。(-2)のカッコはQ5ファイルでは不要なようです。<br />
<br />
[bash]<br />
$ sed 's/x/(-2)/g' Q5 | bc -l<br />
2<br />
-2.50000000000000000000<br />
-8<br />
[/bash]<br />
<br />
echo <数字>からスタートすると、ややこしくなります。<br />
<br />
[bash]<br />
$ echo -2 | xargs -I\@ awk -v a=\@ '{gsub(/x/,a,$0);print}' Q5 | bc -l<br />
2<br />
-2.50000000000000000000<br />
-8<br />
[/bash]<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
「玉子」と「卵」の数を数えて、数が少ない方を数が大きい方で置換してください。<br />
<br />
[bash]<br />
$ cat Q6 <br />
卵卵玉子玉子玉子玉子玉子卵卵卵玉子玉子卵玉子玉子玉子玉子卵卵玉子卵玉子卵卵玉子卵玉子<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
力技です。<br />
<br />
[bash]<br />
$ cat Q6 | grep -oE '(玉子|卵)' | sort | uniq -c |<br />
 sort -n -k1,1n | awk '{print $2}' | xargs |<br />
 awk '{print &quot;s/&quot;$1&quot;/&quot;$2&quot;/g&quot;}' | xargs -I\@ sed \@ Q6<br />
玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
次のseq（あるいはjot等）の出力から、各桁の数字の構成が同じもの（例: 11122と22111等）を重複とみなし、除去してください。<br />
<br />
[bash]<br />
$ seq -w 00000 99999<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
###asortを使う場合###<br />
$ seq -w 00000 99999 | sed 's/./&amp; /g' |<br />
 awk '{for(i=1;i&lt;=NF;i++)a[i]=$i;asort(a);for(k in a){printf a[k]}print &quot;&quot;}' |<br />
 sort -u<br />
###ちょっと気の利いた方法（数字が小さい順に並んでいるものだけ残す）###<br />
$ seq -w 00000 99999 | sed 's/./&amp; /g' |<br />
 awk '$1&lt;=$2&amp;&amp;$2&lt;=$3&amp;&amp;$3&lt;=$4&amp;&amp;$4&lt;=$5' | tr -d ' ' <br />
[/bash]<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
1. まず、1〜7を全て含む7桁の整数を全て列挙して、tmpというファイルに出力してください。<br />
<br />
2. 次に、相異なる７以下の正の整数a,b,c,d,e,f,gを用いて、<br />
<code><br />
abcd + efg<br />
</code><br />
と表せる素数と、その時のa〜gの数字を全て求めましょう。tmpを用いて構いません。<br />
<br />
（参考: 2011年日本数学オリンピック予選第3問から。一部改。<a href="http://www.imojp.org/challenge/old/jmo21yq.html" target="_blank">http://www.imojp.org/challenge/old/jmo21yq.html</a>）<br />
<br />
<h3>解答</h3><br />
<br />
1は力技になります。<br />
<br />
[bash]<br />
$ seq -w 0000000 9999999 | grep -v [089] |<br />
 grep 1 | grep 2 | grep 3 | grep 4 | grep 5 | grep 6 | grep 7 &gt; tmp<br />
[/bash]<br />
<br />
2は、うまくwhileとfactorを使って求めます。<br />
<br />
[bash]<br />
$ cat tmp | sed 's/./&amp; /g' | awk '{print $1$2$3$4$5$6$7,$1*$2*$3*$4+$5*$6*$7}' | while read a b ; do echo $b | factor | awk -v n=$a 'NF==2{gsub(/./,&quot;&amp; &quot;,n);print n,$2}' ; done <br />
2 3 4 6 1 5 7 179<br />
2 3 4 6 1 7 5 179<br />
2 3 4 6 5 1 7 179<br />
2 3 4 6 5 7 1 179<br />
2 3 4 6 7 1 5 179<br />
2 3 4 6 7 5 1 179<br />
2 3 6 4 1 5 7 179<br />
2 3 6 4 1 7 5 179<br />
2 3 6 4 5 1 7 179<br />
...<br />
[/bash]
