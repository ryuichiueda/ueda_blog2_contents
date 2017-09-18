---
Keywords:勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---
# 【問題のみ】第24回◯◯o◯裏番組シェル芸勉強会
解答は<a href="https://blog.ueda.asia/?p=8592">こちら</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<ul><br />
	<li><a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac24%e5%9b%9e%e2%97%af%e2%97%afo%e2%97%af%e8%a3%8f%e7%95%aa%e7%b5%84%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">スライドのリンク</a></li><br />
</ul><br />
<br />
<br />
<br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24</a><br />
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
今回はUbuntu Linux 16.04で解答例を作りました。<br />
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
[bash]<br />
玉子:5 卵:1 <br />
玉子:3 卵:3 <br />
玉子:4 卵:2 <br />
玉子:1 卵:5 <br />
玉子:2 卵:1 <br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
次のようなテキストについて、繰り返し出てきた文字の2つ目以降を省いて出力してください。例えばQ2のファイル<br />
<br />
[bash]<br />
$ cat Q2<br />
へのへのもへじ<br />
[/bash]<br />
<br />
の場合、「へのもじ」が正解の出力になります。<br />
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
<h2>Q4</h2><br />
Q4.xlsxのA1のセルには数字が書いてあります。その数字を出力してください。A4には文字列が書いてあるので余裕がある人はそれも特定してみましょう。<br />
<h2>Q5</h2><br />
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
というようにecho &lt;代入したい数&gt;から始めてワンライナーで解いてみてください。<br />
<h2>Q6</h2><br />
「玉子」と「卵」の数を数えて、数が少ない方を数が大きい方で置換してください。<br />
<br />
[bash]<br />
$ cat Q6 <br />
卵卵玉子玉子玉子玉子玉子卵卵卵玉子玉子卵玉子玉子玉子玉子卵卵玉子卵玉子卵卵玉子卵玉子<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
次のseq（あるいはjot等）の出力から、各桁の数字の構成が同じもの（例: 11122と22111等）を重複とみなし、除去してください。<br />
<br />
[bash]<br />
$ seq -w 00000 99999<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
1. まず、1〜7を全て含む7桁の整数を全て列挙して、tmpというファイルに出力してください。<br />
<br />
2. 次に、相異なる７以下の正の整数a,b,c,d,e,f,gを用いて、<br />
<code><br />
abcd + efg<br />
</code><br />
と表せる素数と、その時のa〜gの数字を全て求めましょう。tmpを用いて構いません。<br />
<br />
（参考: 2011年日本数学オリンピック予選第3問から。一部改。<a href="http://www.imojp.org/challenge/old/jmo21yq.html" target="_blank">http://www.imojp.org/challenge/old/jmo21yq.html</a>）
