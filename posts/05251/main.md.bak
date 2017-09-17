# 日記（シェル芸フル動員のデータ集計）
日記です。集計仕事でシェル芸を駆使しまくりました。手でやると次の日再起不能になるくらい疲れたと思う。ていうか1日じゃ絶対に終わらん。シェル芸に救われました。<br />
<br />
実践、しかも汚いデータ相手になると大技の連続です。繰り出した技を並べておきます。掲載できないデータなので哭きの竜並に雰囲気だけをお楽しみください・・・。<br />
<br />
<!--more--><br />
<br />
<ul><br />
 <li>zipとsedとimagemagickでパワポの画像を別のものに差し替える（パワポシェル芸）</li><br />
 <li>sedでHTMLスクレイピング</li><br />
 <li>nkfとsed、awk等々でExcelに貼るcsvをいくつも作る</li><br />
 <li>Tukubaiのloopx, join1,2,3でinner join, outer join, cross joinとにかくjoin</li><br />
</ul><br />
<br />
一個だけ、スクレイピングに使ったシェルスクリプトが差し障りなさそうなので、掲載しておきます。<span style="color:red">読まないでください。</span><br />
<br />
[bash]<br />
#!/bin/bash -xv<br />
<br />
dir=$(echo $1 | sed 's;/[^/]*$;;')<br />
<br />
cat $1 |<br />
nkf -wLux |<br />
gsed 's/&gt;/&gt;\\n/g' |<br />
gsed -n '/&lt;table/,/&lt;\\/table&gt;/p' |<br />
tr -d '\\n' |<br />
gsed 's;&lt;/li&gt;;&amp;\\n;g' |<br />
gsed 's/&lt;a[^&lt;]*&gt;//g' |<br />
gsed 's/.*&lt;td&gt;/%%\\n/' |<br />
gsed 's/&lt;ul&gt;/\\n/g' |<br />
gsed 's/&lt;br&gt;/\\n/g' |<br />
gsed 's/\\[.*\\]//g' |<br />
gsed 's/&lt;img src=&quot;//g' |<br />
gsed 's/&quot;&gt;//' |<br />
sed 's/→.*//' |<br />
sed 's/[《》]/ /g' |<br />
sed 's/ */ /g' |<br />
sed 's/&lt;[^&lt;]*&gt;//g' |<br />
awk -v d=&quot;$1&quot; '{<br />
 if(/%%/){k=&quot;&quot;;rank++;}<br />
 else if(k==&quot;&quot;){k=$1}<br />
 else{print d,k,&quot;RANK&quot;rank,$0}<br />
}' |<br />
sed 's;^[^ ]*/;;' |<br />
sed 's/\\.html//' |<br />
sed 's/_/ /' |<br />
tee $dir/TYPE_ALL<br />
[/bash]<br />
<br />
gsedとsedが入り混じってますが、単に私がいい加減にやってるだけです。深い意味はありません。あと、シェルスクリプトはシェル芸ではありませんが、これはワンライナーの延長ということで。しかし、<a href="http://blog.ueda.asia/?cat=457">glue</a>でやればよかった・・・。<br />
<br />
<br />
人生にも深い意味なんてないですよね。（確認）<br />
<br />
あ、これも掲載しても良さそうです。パワポに画像をグレースケールにして貼って、一部文言を差し替えるシェルスクリプトです。テンプレートになるパワポファイルは予めunzipしてあって、そいつのxml等を書き換えてzipしてパワポのファイルに戻すということをやってます。<br />
<br />
[bash]<br />
#!/bin/bash -e<br />
<br />
#$1: filename $2: IMAGE $3: COURSE<br />
<br />
cp &quot;$2&quot; &quot;$2.png&quot;<br />
<br />
grayimg=gray.$(basename &quot;$2.png&quot;)<br />
<br />
convert -type GrayScale &quot;$2.png&quot; $grayimg<br />
cp $grayimg ./$3/ppt/media/image1.png<br />
<br />
cp ./$3/ppt/slides/slide1.xml slide1.xml<br />
sed &quot;s/\@/$1/&quot; ./$3/ppt/slides/slide1.xml &gt; new.xml<br />
mv new.xml ./$3/ppt/slides/slide1.xml<br />
<br />
( cd ./$3/ &amp;&amp; zip -r ../../$1.$3.pptx ./)<br />
<br />
mv slide1.xml ./$3/ppt/slides/slide1.xml<br />
rm $grayimg<br />
[/bash]<br />
<br />
<del>ね、簡単でしょ。</del><br />
<br />
寝る。
