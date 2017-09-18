---
Keywords: CLI,USP友の会,勉強会,シェル芸,シェル芸勉強会,難しめ
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第14回東京居残りシェル芸勉強会
<a href="http://blog.ueda.asia/?p=4413" title="【問題と解答例】第14回東京居残りシェル芸勉強会">解答はコッチ</a><br />
<br />
<h1>始める前に</h1><br />
<br />
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
<h1>イントロ</h1><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/42680416" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br />
<br />
<br />
<h1>Q1</h1><br />
<br />
100!を計算してください。正確に。<br />
<br />
<!--more--><br />
<br />
<h1>Q2</h1><br />
<br />
次のseqからsed（と言ってもgsed）だけでfizzbuzzを完成させてください。<br />
<br />
[bash]<br />
ueda\@remote:~$ seq 100 | sed ...<br />
1<br />
2<br />
Fizz<br />
4<br />
Buzz<br />
Fizz<br />
7<br />
8<br />
Fizz<br />
Buzz<br />
11<br />
Fizz<br />
13<br />
14<br />
FizzBuzz<br />
16<br />
17<br />
Fizz<br />
19<br />
Buzz<br />
...<br />
[/bash]<br />
<br />
<h1>Q3</h1><br />
<br />
このうち素数はどれでしょうか？<br />
<br />
[bash]<br />
ueda\@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58<br />
[/bash]<br />
<br />
<h1>Q4</h1><br />
<br />
次の16進数（UTF-8）で書かれたメッセージを復元してください。<br />
<br />
[bash]<br />
e89fb9e3818ce9a39fe381b9e3819fe38184<br />
[/bash]<br />
<br />
<h1>Q5</h1><br />
<br />
次のようなファイルを作ってください。<br />
（catするとahoとだけ出て、容量は1GB。）<br />
<br />
[bash]<br />
ueda\@remote:~$ cat hoge<br />
aho<br />
ueda\@remote:~$ ls -l hoge<br />
-rw-r--r-- 1 ueda ueda 1000000000 12月 7 14:53 hoge<br />
[/bash]<br />
<br />
<h1>Q6</h1><br />
<br />
日本の山を標高の高い順から並べていってください。順位と標高も一緒に出力してください。<a href="http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29" target="_blank">（こちらからcurlで持ってきて加工してください）</a><br />
<br />
おそらく力技になります。<br />
<br />
<br />
<h1>Q7</h1><br />
<br />
分数で正確に答えを求めてください。できれば約分してください。<br />
<br />
[bash]<br />
echo '1/4 + 2/5 + 7/16 - 5/9'<br />
[/bash]<br />
<br />
<br />
<h1>Q8</h1><br />
<br />
[bash]<br />
*****************************************************************<br />
[/bash]<br />
<br />
をポキポキ折ってください。<br />

