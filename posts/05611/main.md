---
Keywords:CLI,シェル芸,集合
Copyright: (C) 2017 Ryuichi Ueda
---
# シェル芸で部分集合を全通り求める方法（別解求む）
ちょっと質問というかお題なのですが、ある集合の部分集合を全通り求める（意味がわからなかったらブログの一番下の出力を見てみてください）必要があって、シェル芸でできないかと考えてみました。<br />
<br />
私の解はこんな感じです。{a,b,c,d}の部分集合を全て求めてみます。a,b,c,dにはアルファベット一文字でなくて数文字入ることもあるとします。<br />
<br />
<br />
まず、とりあえず要素をechoしてみます。<br />
<br />
[bash]<br />
uedambp:~ ueda$ echo a b c d<br />
a b c d<br />
[/bash]<br />
<br />
次にこうやって・・・<br />
<br />
<!--more--><br />
<br />
[bash]<br />
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&amp;\\},;g' | tr -d ' ' |<br />
 awk '{print &quot;echo&quot;,$0}'<br />
echo {,a},{,b},{,c},{,d},<br />
[/bash]<br />
<br />
bashに突っ込みます。<br />
<br />
[bash]<br />
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&amp;\\},;g' | tr -d ' ' |<br />
 awk '{print &quot;echo&quot;,$0}' | bash<br />
,,,, ,,,d, ,,c,, ,,c,d, ,b,,, ,b,,d, ,b,c,, ,b,c,d, a,,,, a,,,d, a,,c,, a,,c,d, a,b,,, a,b,,d, a,b,c,, a,b,c,d,<br />
[/bash]<br />
<br />
あとは適当に整形して終わり。<br />
<br />
[bash]<br />
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&amp;\\},;g' | tr -d ' ' | awk '{print &quot;echo&quot;,$0}' | bash | sed 's/,,*/,/g' | tr ' ' '\\n' | sed 's/,$/}/' | sed 's/^/{/'<br />
{}<br />
{,d}<br />
{,c}<br />
{,c,d}<br />
{,b}<br />
{,b,d}<br />
{,b,c}<br />
{,b,c,d}<br />
{a}<br />
{a,d}<br />
{a,c}<br />
{a,c,d}<br />
{a,b}<br />
{a,b,d}<br />
{a,b,c}<br />
{a,b,c,d}<br />
[/bash]<br />
<br />
なーんかもっと簡単な方法があるように思うのですが、思いつきません。シェル芸的にはできたからいいんですけど、もし別解があれば教えていただきたく。<br />
<br />
<br />
寝る。<br />

