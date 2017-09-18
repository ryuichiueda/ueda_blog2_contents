---
Keywords:コマンド,CLI,Linux,Unix,USP友の会,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---
# 【問題のみ】第17回ジュンク堂はシェル芸が乗っ取った勉強会
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
<br />
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

