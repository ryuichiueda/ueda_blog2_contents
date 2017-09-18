---
Keywords:コマンド,Linux,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第27回sedこわいシェル芸勉強会
解答例は<a href="https://blog.ueda.asia/?p=9283">こちら</a>。<br />
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
<br />
対象とするsedはGNU sedだけに絞っています。解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。GSD系の人は玄人なので各自対応のこと。<br />
<br />
<h2>Q1</h2><br />
<br />
次のechoの出力について、偶数番目の文字だけ大文字にしてください。できたら、奇数番目の文字だけ大文字にしてください。<br />
<br />
[bash]<br />
$ echo abcdefghijklmn<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
seq 1 100から始めてsedだけでFizzBuzzをやってみましょう。<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
次の出力について、3行目を7行目の下に移動してください。<br />
<br />
[bash]<br />
$ seq 1 10<br />
[/bash]<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
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
<br />
<h2>Q5</h2><br />
<br />
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
<br />
<h2>Q6</h2><br />
<br />
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
<br />
<h2>Q7</h2><br />
aというファイルをtouch等で作り、次の縛りでa1, a2, a3, ..., a10というファイルをaからコピーして作ってください。縛り1と縛り2を独立した別々の問題として解き、その後縛り1,2を両方満たす解を考えてみましょう。<br />
<ul><br />
 	<li>縛り1: 使うコマンドはseq、cp、sedだけ</li><br />
 	<li>縛り2: ワンライナー中で数字を使わない</li><br />
</ul><br />
<br />
<h2>Q8</h2><br />
<br />
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

