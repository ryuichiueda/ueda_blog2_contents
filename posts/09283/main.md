---
Keywords: コマンド,sed,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第27回sedこわいシェル芸勉強会
<a href="https://blog.ueda.asia/?p=9309">問題のみのページ</a>はこちら。<br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.27" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.27</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>イントロ</h2><br />
<br />
<ul><br />
 <li><a target="_blank" href="https://blog.ueda.asia/?post_type=presenpress&p=9312">スライド</a></li><br />
</ul><br />
<br />
<h2>環境</h2><br />
対象とするsedはGNU sedだけに絞っています。解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。BSD系の人は玄人なので各自対応のこと。<br />
<br />
<h2>Q1</h2><br />
次のechoの出力について、偶数番目の文字だけ大文字にしてください。できたら、奇数番目の文字だけ大文字にしてください。<br />
<br />
[bash]<br />
$ echo abcdefghijklmn<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
###偶数番目を大文字に###<br />
$ echo abcdefghijklmn | sed 's/\\(.\\)\\(.\\)/\\1\\U\\2/g'<br />
aBcDeFgHiJkLmN<br />
###奇数番目を大文字に###<br />
$ echo abcdefghijklmn | sed 's/\\(.\\)\\(.\\)/\\U\\1\\L\\2/g'<br />
AbCdEfGhIjKlMn<br />
###-rを使うと多少スッキリする###<br />
$ echo abcdefghijklmn | sed -r 's/(.)(.)/\\U\\1\\L\\2/g'<br />
AbCdEfGhIjKlMn<br />
[/bash]<br />
<br />
<h2>Q2</h2><br />
seq 1 100から始めてsedだけでFizzBuzzをやってみましょう。<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ seq 1 100 | sed '0~3s/.*/Fizz/;0~5s/$/Buzz/' |<br />
 sed 's/[0-9]*B/B/' | xargs<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
次の出力について、3行目を7行目の下に移動してください。<br />
<br />
[bash]<br />
$ seq 1 10<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
hで3行目をホールドスペースに突っ込み、Gでパターンスペースに戻します。<br />
<br />
[bash]<br />
$ seq 1 10 | sed '3h;3d;7G'<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
次のコードのmainとahoの位置を入れ替えてください。<br />
<br />
[bash]<br />
$ cat aho.cc <br />
#include &lt;iostream&gt;<br />
using namespace std;<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	aho();<br />
	return 0;<br />
}<br />
<br />
void aho(void)<br />
{<br />
	cout &lt;&lt; &quot;aho&quot; &lt;&lt; endl;<br />
}<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
mainの部分をホールドスペースに入れる→消す→ファイルの一番後ろでホールドスペースを吐き出すという流れになります。<br />
<br />
[bash]<br />
$ cat aho.cc | sed '/int/,/}/H;/int/,/}/d;$G'<br />
#include &lt;iostream&gt;<br />
using namespace std;<br />
<br />
<br />
void aho(void)<br />
{<br />
	cout &lt;&lt; &quot;aho&quot; &lt;&lt; endl;<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	aho();<br />
	return 0;<br />
}<br />
###{}でまとめる###<br />
$ cat aho.cc | sed '/int/,/}/{H;d};$G'<br />
###もうちょっと厳密なやつ###<br />
$ cat aho.cc | sed '/ main(/,/^}/{H;d};$G'<br />
###そのままコンパイルして実行###<br />
$ cat aho.cc | sed '/int/,/}/H;/int/,/}/d;$G' |<br />
 g++ -x c++ - &amp;&amp; ./a.out<br />
aho<br />
[/bash]<br />
<br />
<h2>Q5</h2><br />
seq 1 10 | から始めて次のような出力を作ってください。<br />
<br />
[bash]<br />
2<br />
1<br />
4<br />
3<br />
6<br />
5<br />
8<br />
7<br />
10<br />
9<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ seq 1 10 | sed '1~2h;1~2d;0~2G'<br />
2<br />
1<br />
4<br />
3<br />
6<br />
5<br />
8<br />
7<br />
10<br />
9<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
echo 1から始めて次のような出力を作ってください。<br />
<br />
[bash]<br />
1<br />
11<br />
111<br />
1111<br />
11111<br />
111111<br />
1111111<br />
11111111<br />
111111111<br />
1111111111<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
ラベルを使います。<br />
<br />
[bash]<br />
$ echo 1 | sed ':LOOP p;s/./&amp;&amp;/;b LOOP' | head<br />
1<br />
11<br />
111<br />
1111<br />
11111<br />
111111<br />
1111111<br />
11111111<br />
111111111<br />
1111111111<br />
###分岐を使う###<br />
$ echo 1 | sed ':LOOP p;s/./&amp;&amp;/;/1\\{10\\}/!b LOOP'<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
aというファイルをtouch等で作り、次の縛りでa1, a2, a3, ..., a10というファイルをaからコピーして作ってください。縛り1と縛り2を独立した別々の問題として解き、その後縛り1,2を両方満たす解を考えてみましょう。<br />
<ul><br />
 	<li>縛り1: 使うコマンドはseq、cp、sedだけ</li><br />
 	<li>縛り2: ワンライナー中で数字を使わない</li><br />
</ul><br />
<h3>解答</h3><br />
<br />
[bash]<br />
###縛り1###<br />
$ touch a<br />
$ seq 1 10 | sed 's/./cp a a&amp;/e'<br />
$ ls a a? a10<br />
a a1 a10 a2 a3 a4 a5 a6 a7 a8 a9<br />
###縛り2###<br />
$ yes | sed -n '=' | head | sed 's/./cp a a&amp;/e'<br />
###両方###<br />
$ sed ':a ;p;s/./&amp;&amp;/;/........../!b a' &lt;&lt;&lt; y |<br />
 sed -n = | sed 's/^/cp a a/e'<br />
###（おまけ）ファイルaをsedで作る###<br />
$ sed 'w a' &lt;&lt;&lt; &quot;abc&quot;<br />
abc<br />
$ cat a<br />
abc<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
echo 1 | から始めて、あとはsedだけで次のような出力を得てください。<br />
<br />
[bash]<br />
1<br />
11<br />
111<br />
1111<br />
11111<br />
11111<br />
1111<br />
111<br />
11<br />
1<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ echo 1 | sed ':LOOP p;s/./&amp;&amp;/;/1\\{5\\}/!b LOOP' | sed 'p;1!G;h;$!d'<br />
1<br />
11<br />
111<br />
1111<br />
11111<br />
11111<br />
1111<br />
111<br />
11<br />
1<br />
[/bash]<br />

