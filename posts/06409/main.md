---
Keywords:コマンド,CLI,Linux,Unix,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---
# 【問題と解答】第17回ジュンク堂はシェル芸が乗っ取った勉強会
<h2>ルール</h2><br />
<br />
<ul><br />
	<li>ワンライナーで出されたお題を解きます。</li><br />
	<li>汎用的な解を考えるのは出された問題をとりあえず解いてから。</li><br />
	<li>特にどの環境とは指定しないので各自環境に合わせて読み替えを。ただし今回、AWKだけはGNU Awk 4.0.1を使っていると明記しておきます。</li><br />
	<li>今回のテーマはAWKですが、何で解いても構いません。別にPowerShellだろうがRubyだろうが構いません。ワンライナーじゃないけどエクセル方眼紙でも。</li><br />
</ul><br />
<br />
<br />
<br />
<h2>環境</h2><br />
今回はLinuxで解答例を作りましたので、BSDやMacな方は以下の表をご参考に・・・。<br />
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
次のようなデータを<br />
<br />
[bash]<br />
$ cat data1<br />
a 1<br />
b 4<br />
a 2<br />
a 3<br />
b 5<br />
[/bash]<br />
<br />
次のように変換してみましょう。<br />
<br />
[bash]<br />
a 1 2 3<br />
b 4 5<br />
[/bash]<br />
<br />
余力のある人は次のようなJSON形式にしてみましょう。<br />
<br />
[bash]<br />
{a:[1,2,3],b:[4,5]}<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
連想配列にデータを追記していって最後に出力するのが楽な方法です。<br />
<br />
[bash]<br />
$ cat data1 | awk '{d[$1]=d[$1]&quot; &quot;$2}END{for(k in d){print k d[k]}}' <br />
a 1 2 3<br />
b 4 5<br />
[/bash]<br />
<br />
JSONにするには力技（しか思い浮かばなかった）。<br />
<br />
[bash]<br />
$ cat data1 | awk '{d[$1]=d[$1]&quot; &quot;$2}END{for(k in d){print k d[k]}}' |<br />
 awk -v q='&quot;' '{printf q$1q&quot;:[&quot;;for(i=2;i&lt;=NF;i++){printf $i&quot;,&quot;};print &quot;]&quot;}' |<br />
 xargs | tr ' ' ',' | awk '{print &quot;{&quot;$0&quot;}&quot;}' | sed 's/,]/]/g'<br />
{a:[1,2,3],b:[4,5]}<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
以下の数字のファイルから同じレコード（行）があるかないかを調べ、ある場合には何行目と何行目にあるのか出力しましょう。<br />
<br />
[bash]<br />
$ cat data<br />
0.5937836043 0.4644710001<br />
0.3637036697 0.5593602512<br />
0.5655269331 0.6793148112<br />
0.7804610574 0.2905477797<br />
0.3637036697 0.5593602512<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
[bash]<br />
$ cat data | awk 'a[$0]{print a[$0],NR,$0}{a[$0]=NR}'<br />
[/bash]<br />
<br />
1千万行でも10秒くらいで答えが出ることを確認済みです。もっと大きなレコード数で行う場合はもう一捻り必要です。<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
次のJSONのデータについて、aに対応づけられた配列内の数字の合計とbに対応づけられた配列内の数字の合計を求めましょう。<br />
<br />
[bash]<br />
$ cat data<br />
{&quot;a&quot;:[1,2,3],&quot;b&quot;:[4,5]}<br />
[/bash]<br />
<br />
<h2>解答</h2><br />
<br />
きれいな方法が思い浮かばないので力技で。<br />
<br />
[bash]<br />
$ grep -o '&quot;[ab]&quot;:\\[[^\\[]*\\]' data | tr '&quot;:[],' ' ' |<br />
 awk '{n=0;for(i=2;i&lt;=NF;i++){n+=$i};print $1,n}'<br />
a 6<br />
b 9<br />
$ cat data | jq . | tr -dc '[:alnum:]\\n' |<br />
 awk '/[ab]/{k=$1}!/[ab]/{n[k]+=$1}END{for(k in n){print k,n[k]}}'<br />
a 6<br />
b 9<br />
###jqを使う例を。もっとうまくできるようですが・・・。###<br />
$ cat data | jq 'reduce .a[] as $n (0; . + $n),reduce .b[] as $n (0; . + $n)'<br />
6<br />
9<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
<br />
次のようなIPv6アドレスをechoした後にパイプでコマンドをつなぎ、「::」で省略されているセクションに0を補ってください。<br />
<br />
[bash]<br />
$ echo 2001:db8::9abc<br />
[/bash]<br />
<br />
ただし、同じワンライナーが<br />
<br />
[bash]<br />
::1<br />
[/bash]<br />
<br />
でも使えるようにしてください。<br />
<br />
<h2>解答</h2><br />
<br />
whileを使ってNFが8になるまでフィールドを補ってから処理してやると素直な処理になります。初めてシェル芸勉強会でawkのwhileを使いました・・・。<br />
<br />
[bash]<br />
$ echo 2001:db8::9abc |<br />
 awk -F: '{while(NF!=8){gsub(/::/,&quot;:0::&quot;,$0)};for(i=1;i&lt;=8;i++){$i=$i!=&quot;&quot;?$i:0};print}' |<br />
 tr ' ' ':'<br />
2001:db8:0:0:0:0:0:9abc<br />
$ echo ::1 |<br />
 awk -F: '{while(NF!=8){gsub(/::/,&quot;:0::&quot;,$0)};for(i=1;i&lt;=8;i++){$i=$i!=&quot;&quot;?$i:0};print}' |<br />
 tr ' ' ':'<br />
0:0:0:0:0:0:0:1<br />
###別解###<br />
$ echo 2001:db8::9abc |<br />
 awk -F: '{while(NF!=8){gsub(/::/,&quot;:0::&quot;,$0)}print}' |<br />
 tr ':' '\\n' | awk '!NF{print 0}NF{print}' | xargs | tr ' ' ':'<br />
[/bash]
