# 【問題のみ】第29回激しいシェル芸勉強会
<a href="https://blog.ueda.tech/?p=9870">解答のページはこちら</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.29" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.29</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<br />
<h2>環境</h2><br />
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールしてつかいましょう。BSD系の人は玄人なので各自対応のこと。<br />
<br />
<h2>イントロ</h2><br />
<ul><br />
<br />
	<li><a href="https://blog.ueda.tech/?presenpress=%E7%AC%AC29%E5%9B%9E%E6%BF%80%E3%81%97%E3%81%84%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8%E5%8B%89%E5%BC%B7%E4%BC%9A#/">こちら</a></li></ul><br />
<br />
<br />
<h2>Q1</h2><br />
<br />
次の2つのファイルは、講義で出した課題1,2それぞれの点数です。<br />
<br />
[bash]<br />
$ cat kadai1<br />
001 山田 20<br />
002 出川 30<br />
005 鳥海 44<br />
$ cat kadai2 <br />
001 山田 20<br />
003 上田 15<br />
004 今泉 22<br />
005 鳥海 44<br />
[/bash]<br />
<br />
両方に名前のある人については点数を合計して、次のように全員の得点リストを作ってください。<br />
<br />
[bash]<br />
001 山田 40<br />
002 出川 30<br />
003 上田 15<br />
004 今泉 22<br />
005 鳥海 88<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
<br />
次の2つのファイルは、5回の講義の出欠と6回目の講義で出席した人の番号のデータです。attendに6回目の講義の出欠を反映したデータを標準出力に出力してください。<br />
<br />
[bash]<br />
$ cat attend<br />
001 山田 出出欠出出<br />
002 出川 出出欠欠欠<br />
003 上田 出出出出出<br />
004 今泉 出出出出出<br />
005 鳥海 欠出欠出欠<br />
$ cat attend6<br />
001,005,003<br />
[/bash]<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
次の2つのファイルは5回の講義の出欠とテストの成績を記録したファイルです。<br />
<br />
[bash]<br />
###$1: 番号, $2: 名前, $3: 出欠 ###<br />
$ cat attend <br />
001 山田 出出欠出出 <br />
002 出川 出出欠欠欠<br />
003 上田 出出出出出<br />
004 今泉 出出出出出<br />
005 鳥海 欠出欠出欠<br />
###$1: 番号, $2: テストの点数（受けてない人のデータは無い）###<br />
$ cat test <br />
001 90<br />
002 78<br />
004 80<br />
005 93<br />
[/bash]<br />
<br />
こういうルールで、最終的な点数を出して、番号、名前、点数を記録したファイル作ってください。<br />
<br />
<ul><br />
	<li>出席が過半数に満たない人、テストを受けていない人は0点</li><br />
	<li>出席が過半数の人はテストの点数を採用</li><br />
</ul><br />
<br />
<br />
<h2>Q4</h2><br />
<br />
<h3>Q4.1</h3><br />
<br />
次の出力をパイプで受けて<br />
<br />
[bash]<br />
$ echo -1 4 5 2 42 421 44 311 -9 -11<br />
[/bash]<br />
<br />
次のように同じ桁のものを横並びに出力を得てください。横に並べる時の順番は任意とします。また、この出力のように正の数と負の数を分けます。<br />
<br />
[bash]<br />
-11 <br />
-9 -1 <br />
2 4 5 <br />
42 44 <br />
311 421 <br />
[/bash]<br />
<br />
<h3>Q4.2</h3><br />
<br />
次の出力をパイプで受けて<br />
<br />
[bash]<br />
$ echo -1 +4 5 2 42 421 44 311 -9 -11<br />
[/bash]<br />
<br />
次のように同じ桁のものを横並びに出力を得てください。Q1.1と同じく横に並べる時の順番は任意とします。<br />
<br />
[bash]<br />
-11 <br />
-9 -1 <br />
2 +4 5 <br />
42 44 <br />
311 421 <br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
<br />
次のファイルの中身について、<br />
<br />
[bash]<br />
$ cat triangle <br />
 1<br />
 3 9<br />
 7 a 6<br />
8 4 2 5<br />
[/bash]<br />
<br />
次のように右に転がしてください。できる人はawkを使わないでやってみましょう。<br />
<br />
[bash]<br />
 8 <br />
 4 7 <br />
 2 a 3 <br />
5 6 9 1<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
次の1から100までの素数を書いたファイル（いくつか欠番が存在）について、<br />
<br />
[bash]<br />
$ cat prime <br />
2 3 5 7 11 13 17 19 31 37 41 43 47 53 59 67 71 73 79 83 89 97<br />
[/bash]<br />
<br />
次のように欠番のところで折り返してください。（ワンライナーの中に欠番を直接書かないでくださいね。）<br />
<br />
[bash]<br />
2 3 5 7 11 13 17 19 <br />
31 37 41 43 47 53 59 <br />
67 71 73 79 83 89 97<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
リポジトリ内のnyaan.htmlは、ブラウザで見ると次のように見えます。<a href="81487cda9a61853c1fd356329c35e86d.png"><img src="81487cda9a61853c1fd356329c35e86d-1024x462.png" alt="" width="660" height="298" class="aligncenter size-large wp-image-9897" /></a><br />
<br />
次のようにcatから始めて、この文字を（大きなまま）端末上に表示してみてください。<br />
[bash]<br />
$ cat ./nyaan.html | ...<br />
[/bash]<br />
<br />
できる人は小さい通常の文字で「にゃーん」と出してみてください（これは解答例を考えていません）。<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
次のshellgeiファイルについて、<br />
<br />
[bash]<br />
$ cat shellgei <br />
 m <br />
 &quot;&quot;m m &quot;m # # # # <br />
 mm # # #mmm&quot;&quot;&quot; m&quot; <br />
 &quot; m&quot; mmm&quot;&quot; # # # m&quot; # mm&quot;&quot;m <br />
 m&quot; #mm m&quot; # m&quot; &quot; # # <br />
 &quot;mm&quot;&quot; &quot;&quot;&quot;&quot; &quot; m&quot; #&quot; m&quot; # <br />
 <br />
 <br />
[/bash]<br />
<br />
次のように、文字の無い列を詰めてください。<br />
<br />
[bash]<br />
 m <br />
 &quot;&quot;m m &quot;m # # # #<br />
mm # # #mmm&quot;&quot;&quot; m&quot; <br />
 &quot; m&quot; mmm&quot;&quot; # # # m&quot; # mm&quot;&quot;m <br />
 m&quot; #mm m&quot; # m&quot; &quot; # # <br />
&quot;mm&quot;&quot; &quot;&quot;&quot;&quot; &quot;m&quot; #&quot; m&quot; # <br />
[/bash]<br />

