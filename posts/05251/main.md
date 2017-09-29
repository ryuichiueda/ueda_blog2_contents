---
Keywords: どうでもいい,大技,実践シェル芸,日記,シェル芸,エクシェル芸,パワポシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記（シェル芸フル動員のデータ集計）
日記です。集計仕事でシェル芸を駆使しまくりました。手でやると次の日再起不能になるくらい疲れたと思う。ていうか1日じゃ絶対に終わらん。シェル芸に救われました。

実践、しかも汚いデータ相手になると大技の連続です。繰り出した技を並べておきます。掲載できないデータなので哭きの竜並に雰囲気だけをお楽しみください・・・。

<!--more-->

<ul>
 <li>zipとsedとimagemagickでパワポの画像を別のものに差し替える（パワポシェル芸）</li>
 <li>sedでHTMLスクレイピング</li>
 <li>nkfとsed、awk等々でExcelに貼るcsvをいくつも作る</li>
 <li>Tukubaiのloopx, join1,2,3でinner join, outer join, cross joinとにかくjoin</li>
</ul>

一個だけ、スクレイピングに使ったシェルスクリプトが差し障りなさそうなので、掲載しておきます。<span style="color:red">読まないでください。</span>

```bash
#!/bin/bash -xv

dir=$(echo $1 | sed 's;/[^/]*$;;')

cat $1 |
nkf -wLux |
gsed 's/&gt;/&gt;\\n/g' |
gsed -n '/<table/,/<\\/table&gt;/p' |
tr -d '\\n' |
gsed 's;</li&gt;;&amp;\\n;g' |
gsed 's/<a[^<]*&gt;//g' |
gsed 's/.*<td&gt;/%%\\n/' |
gsed 's/<ul&gt;/\\n/g' |
gsed 's/<br&gt;/\\n/g' |
gsed 's/\\[.*\\]//g' |
gsed 's/<img src=&quot;//g' |
gsed 's/&quot;&gt;//' |
sed 's/→.*//' |
sed 's/[《》]/ /g' |
sed 's/ */ /g' |
sed 's/<[^<]*&gt;//g' |
awk -v d=&quot;$1&quot; '{
 if(/%%/){k=&quot;&quot;;rank++;}
 else if(k==&quot;&quot;){k=$1}
 else{print d,k,&quot;RANK&quot;rank,$0}
}' |
sed 's;^[^ ]*/;;' |
sed 's/\\.html//' |
sed 's/_/ /' |
tee $dir/TYPE_ALL
```

gsedとsedが入り混じってますが、単に私がいい加減にやってるだけです。深い意味はありません。あと、シェルスクリプトはシェル芸ではありませんが、これはワンライナーの延長ということで。しかし、<a href="http://blog.ueda.asia/?cat=457">glue</a>でやればよかった・・・。


人生にも深い意味なんてないですよね。（確認）

あ、これも掲載しても良さそうです。パワポに画像をグレースケールにして貼って、一部文言を差し替えるシェルスクリプトです。テンプレートになるパワポファイルは予めunzipしてあって、そいつのxml等を書き換えてzipしてパワポのファイルに戻すということをやってます。

```bash
#!/bin/bash -e

#$1: filename $2: IMAGE $3: COURSE

cp &quot;$2&quot; &quot;$2.png&quot;

grayimg=gray.$(basename &quot;$2.png&quot;)

convert -type GrayScale &quot;$2.png&quot; $grayimg
cp $grayimg ./$3/ppt/media/image1.png

cp ./$3/ppt/slides/slide1.xml slide1.xml
sed &quot;s/\@/$1/&quot; ./$3/ppt/slides/slide1.xml &gt; new.xml
mv new.xml ./$3/ppt/slides/slide1.xml

( cd ./$3/ &amp;&amp; zip -r ../../$1.$3.pptx ./)

mv slide1.xml ./$3/ppt/slides/slide1.xml
rm $grayimg
```

<del>ね、簡単でしょ。</del>

寝る。
