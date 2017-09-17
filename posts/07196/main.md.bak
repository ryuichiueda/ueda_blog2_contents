# 【問題と解答】第20回記念、年末年始の浮ついた気分大粉砕シェル芸勉強会
<a href="https://blog.ueda.asia/?p=7332">問題だけページはコチラ</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/eosHmifvAQbFmL" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20-56450263" title="第20回シェル芸勉強会イントロ" target="_blank">第20回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
前回からGitHubに置くようにしました。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20</a><br />
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
<br />
<br />
<h2>Q1</h2><br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20/Q1" target="_blank">リポジトリ内のvol.20/Q1ディレクトリ</a>には次のように数字が書いてあるファイルが4つ入っています。<br />
<br />
[bash]<br />
$ ls <br />
file_A-1 file_A-2 file_B-1 file_B-2<br />
$ head -n 2 *<br />
==&gt; file_A-1 &lt;==<br />
1<br />
31351<br />
<br />
==&gt; file_A-2 &lt;==<br />
11<br />
35<br />
<br />
==&gt; file_B-1 &lt;==<br />
-32<br />
12<br />
<br />
==&gt; file_B-2 &lt;==<br />
912<br />
3<br />
[/bash]<br />
<br />
file_A-*のグループ、file_B-*のグループからそれぞれ最大の数を探してください。他にfile_C-*、file_D-*、・・・とグループがたくさんあると想定して、1回のワンライナーで両方探すこととします。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ grep ^ * | sed 's/-[0-9]*:/ /' | sort -k1,1 -k2,2nr |<br />
awk '{print $2,$1}' | uniq -f 1<br />
233333 file_A<br />
9912 file_B<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
<a href="http://ja.uncyclopedia.info/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8" target="_blank">アンサイクロぺディアのシェル芸のページ</a>から、「カースト最上位者が日常的に書く、素数を出力するワンライナー」のコードを取得して実行してください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ curl -s http://ja.uncyclopedia.info/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8 |<br />
grep eval | sed 's/^..//' | bash<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
次のファイルについて、奇数を1列目、偶数を2列目に振り分けて、奇数の列を昇順、偶数の列を降順にソートしてください。<br />
<br />
[bash]<br />
$ cat Q3<br />
1<br />
4<br />
2<br />
9<br />
5<br />
8<br />
[/bash]<br />
<br />
つまりこうしてください。<br />
<br />
[bash]<br />
1 8<br />
5 4<br />
9 2<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ paste &lt;(awk '$1%2' Q3 | sort) &lt;(awk '$1%2==0' Q3 | sort -r) | tr '\\t' ' '<br />
1 8<br />
5 4<br />
9 2<br />
$ cat Q3 | sed 's/.*[02468]$/-&amp;/' | sort | xargs |<br />
awk '{for(i=NF/2;i&gt;=1;i--){print $(NF-i+1),-$i}}'<br />
1 8<br />
5 4<br />
9 2<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
今、ログインしているサーバについて、自分の今使っているリモート端末以外の端末を抹殺してください。rootになっても構いません。<br />
<br />
<h2>解答</h2><br />
<br />
もっと楽な方法がありそうですが・・・。ttyコマンドはオプションに$()で埋め込んでもうまく働きません。（ttyが端末と関係ないプロセスで立ち上がるので）。<br />
<br />
[bash]<br />
ueda\@remote:~$ a=$(tty | sed 's;/dev/;;') ; ps aux |<br />
awk '$7~/pts\\/[0-9]*/' | awk -v &quot;t=$a&quot; '$7!=t' |<br />
awk '{print $2}' | xargs sudo kill <br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
任意の二つの自然数をechoして最大公約数を求めましょう。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
ueda\@remote:~$ echo 45 126 |<br />
awk '{while($1*$2!=0){if($1&gt;$2){$1=$1-$2}else{$2=$2-$1}print}}' |<br />
awk 'END{print $1}'<br />
9<br />
###Tukubai使用（こっちの方が長いが・・・）###<br />
ueda\@remote:~$ echo 60 9 | factor | tarr num=1 | tr -d : | <br />
self 2 1 | sort | count 1 2 | self 1 3 | yarr num=1 |<br />
awk 'NF&gt;2' | awk '{print $1,$2&lt;$3?$2:$3}' |<br />
awk 'BEGIN{a=1}{a*=$1**$2}END{print a}'<br />
[/bash]<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
ファイルQ6の中の人の名前について、誰が1列目と2列目の何番めに記述されているかを求めましょう。<br />
<br />
[bash]<br />
###スペースは全角###<br />
$ cat Q6<br />
山田　上田　吉田　武田<br />
吉田　武田　上田　山田<br />
[/bash]<br />
<br />
解答例は次のようなものです。<br />
<br />
[bash]<br />
吉田 3 1<br />
山田 1 4<br />
上田 2 3<br />
武田 4 2<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat Q6 | sed 's/　/ /g' | awk '{for(i=1;i&lt;=NF;i++){print $i,NR,i}}' |<br />
sort -k1,2 | awk '{print $1,$3}' | xargs -n 4 | awk '{print $1,$2,$4}'<br />
吉田 3 1<br />
山田 1 4<br />
上田 2 3<br />
武田 4 2<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
一部分に「魚」を持つ漢字をなるべくたくさん列挙してみてください。方法はお任せします。<br />
<br />
<h3>解答</h3><br />
<br />
あくまで一例で一部分ですが・・・<br />
<br />
[bash]<br />
$ seq 39770 40058 | xargs printf &quot;&amp;#x%x;&quot; | nkf --numchar-input <br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
次の漢数字をアラビア数字に変換しましょう。<br />
<br />
<br />
[bash]<br />
$ cat Q8 <br />
五千七百三十五<br />
四千三<br />
四十五<br />
九万六千二百三十三<br />
十一<br />
百十二<br />
[/bash]<br />
<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat Q8 | sed 'y/一二三四五六七八九/１２３４５６７８９/' |<br />
nkf -Z1 | sed 's/十/1*10+/' | sed 's/百/1*100+/' |<br />
sed 's/千/1*1000+/' | sed 's/万/1*10000+/' |<br />
sed 's/\\([0-9]\\)1/\\1/g' | bc<br />
5735<br />
4003<br />
45<br />
96233<br />
11<br />
112<br />
[/bash]<br />
<br />
<h2>宣伝</h2><br />
<br />
[amazonjs asin="4774173444" locale="JP" title="シェルプログラミング実用テクニック (Software Design plus)"]
