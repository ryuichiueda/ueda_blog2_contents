---
Keywords:シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---
# 【解答】年末年始シェル芸問題集
<a href="http://blog.ueda.asia/?p=4852" title="【問題】年末年始シェル芸問題集" target="_blank">年末出したシェル芸の問題</a>の私の解答です。ただ、挑戦した皆さんの解答の方が面白いし鋭いので、「シェル芸」で検索してみてください。あとで下の方に皆さんの解答例を掲載していこうと思います。<br />
<br />
<h1>Q1</h1><br />
<br />
<br />
年末年始はディレクトリの掃除をしましょう。ということで、ご自身のPCから重複しているデータを探してみてください。全てのファイルから探すのは大変なので、手始めに重複しているJPEG画像リストを作ってみてください。<br />
<br />
<!--more--><br />
<br />
<h1>解答</h1><br />
<br />
もし何も出てこなかったら適当なjpegファイルをコピーして検出できるか試してみてください。「sed 's/.*/"&"/'」はファイルに半角空白があるときのためにファイル名をダブルクォートで囲む処理です。sortのLANG=Cと-sオプションはファイル数が膨大なときに処理を速くするためにつけています。<br />
<br />
注意: 時間がかかるかもしれません。とりあえずsortの前に一度ファイルに出した方がよいかもしれません。<br />
<br />
[bash]<br />
###出力で1列目の数が同じものが重複の疑いのあるものです###<br />
uedambp:~ ueda$ find ~/ -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' |<br />
xargs -n 1 gmd5sum | LANG=C sort -s -k1,1 |<br />
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'<br />
###Linuxの場合（さらにルートから検索をかけてみる）###<br />
ueda\@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' | <br />
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | <br />
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'<br />
...<br />
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/var/www/bashcms/pages/whats_bashCMS/chinjyu.jpg<br />
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/chinjyu.jpg<br />
f1c3a09b784cc5a55bb820aaa873c79f /var/tmp/GIT/SD_BOOK/IMAGE/noodle.jpg<br />
f1c3a09b784cc5a55bb820aaa873c79f /home/ueda/GIT/SD_BOOK/IMAGE/noodle.jpg<br />
###Open usp Tukubai使用###<br />
ueda\@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' | <br />
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | yarr num=1 | awk 'NF&gt;2'<br />
[/bash]<br />
<br />
<h1>Q2</h1><br />
<br />
羽田空港の緯度経度を求めてください。<br />
<br />
<h1>解答</h1><br />
<br />
いくつかWebAPIを提供しているサイトがあると思いますが、私はFlightRadar24から持ってきました。<br />
<br />
<a href="http://blog.cykey.ca/post/88174516880/analyzing-flightradar24s-internal-api-structure" target="_blank">こちらを参考にしました。</a><br />
<br />
[bash]<br />
uedambp:~ ueda$ curl http://www.flightradar24.com/_json/airports.php 2&gt; /dev/null | <br />
jq . | grep -C 6 HND<br />
 &quot;lon&quot;: &quot;15.082770&quot;,<br />
 &quot;country&quot;: &quot;Sweden&quot;,<br />
 &quot;alt&quot;: &quot;1503&quot;<br />
 },<br />
 {<br />
 &quot;name&quot;: &quot;Tokyo Haneda International Airport&quot;,<br />
 &quot;iata&quot;: &quot;HND&quot;,<br />
 &quot;icao&quot;: &quot;RJTT&quot;,<br />
 &quot;lat&quot;: &quot;35.552250&quot;,<br />
 &quot;lon&quot;: &quot;139.779602&quot;,<br />
 &quot;country&quot;: &quot;Japan&quot;,<br />
 &quot;alt&quot;: &quot;21&quot;<br />
 },<br />
[/bash]<br />
<br />
<h1>Q3</h1><br />
<br />
<br />
任意の級数からネイピア数（自然対数の底の数）を求めてください。精度が良いほど良いこととします。<br />
<br />
<a href="http://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%A4%E3%83%94%E3%82%A2%E6%95%B0%E3%81%AE%E8%A1%A8%E7%8F%BE" target="_blank">こちらを参考に。</a><br />
<br />
<h1>解答</h1><br />
<br />
もっと簡単な解答がありそうですが。1/(0!)の項が抜けるので最後に1を足さなければいけないのが残念。<br />
<br />
[bash]<br />
uedambp:~ ueda$ seq 1 1000 |<br />
awk '{for(i=1;i&lt;=$1;i++){printf(&quot;%d &quot;,i)}{print &quot;&quot;}}' |<br />
tr ' ' '*' | sed 's/\\*$/)/' | sed 's:^:1/(:' | bc -l | <br />
tr '\\n' '+' | sed 's/$/1/' | bc -l <br />
2.71828182845904523526<br />
[/bash]<br />
<br />
<h1>Q4</h1><br />
<br />
<a href="http://blog.ueda.asia/misc/message2015.txt" target="_blank">http://blog.ueda.asia/misc/message2015.txt</a>は、あるメッセージにbase64を多重にかけたものです。解読してください。ワンライナーでなくても構いません。<br />
<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
uedambp:~ ueda$ a=$(curl http://blog.ueda.asia/misc/message2015.txt) ; <br />
while a=$(echo $a | base64 -D) &amp;&amp; echo $a ; do : ; done <br />
...<br />
T2lncGV6b2dmQ0E2SUNaOU96b0sK<br />
OigpezogfCA6ICZ9OzoK<br />
:(){: | : &amp;};:<br />
Invalid character in input stream.<br />
[/bash]<br />
<br />
<h1>Q5</h1><br />
<br />
円周率をなるべく精度よく求めてみてください。<br />
<br />
<h1>解答</h1><br />
<br />
モンテカルロ法でささっと（なにがささっとだか・・・）。<br />
<br />
[bash]<br />
uedambp:~ ueda$ cat /dev/urandom | gtr -dc '0-9' |<br />
gfold -b10 | sed 's/^/0./' | sed 's/$/5/' |<br />
awk 'NR%2==0{print $1}NR%2!=0{printf($1 &quot; &quot;)}' |<br />
awk '{x=$1-0.5;y=$2-0.5;r=sqrt(x^2 + y^2);if(r &lt; 0.5){n++};print NR, 4*n/NR}'<br />
...<br />
729078 3.14094<br />
729079 3.14094<br />
729080 3.14094<br />
729081 3.14095<br />
729082 3.14095<br />
729083 3.14094<br />
729084 3.14094<br />
...<br />
###だんだん収束していきます###<br />
[/bash]<br />
<br />
<h1>Q6</h1><br />
<br />
集合{a,b,c,d,e}から全ての組み合わせ（部分集合）を列挙してください。<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
uedambp:~ ueda$ echo {,a}{,b}{,c}{,d}{,e}<br />
e d de c ce cd cde b be bd bde bc bce bcd bcde a ae ad ade ac ace acd acde ab abe abd abde abc abce abcd abcde<br />
[/bash]<br />
<br />
<h1>Q7</h1><br />
<br />
8128が完全数であることを確認してください。<br />
<br />
<h1>解答</h1><br />
<br />
[bash]<br />
uedambp:~ ueda$ seq 2 8128 | awk '{print 8128/$1}' | grep -Fv . | numsum<br />
8128<br />
[/bash]
