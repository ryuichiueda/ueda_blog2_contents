---
Keywords:CLI,UNIX/Linuxサーバ,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第22回ゴールデンウィークの存在疑惑シェル芸勉強会
- <a href="https://blog.ueda.asia/?p=8028">解答はこちら</a><br />
<br />
<h2>イントロのプレゼン資料</h2><br />
<br />
- <a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac22%e5%9b%9e%e3%82%b4%e3%83%bc%e3%83%ab%e3%83%87%e3%83%b3%e3%82%a6%e3%82%a3%e3%83%bc%e3%82%af%e3%81%ae%e5%ad%98%e5%9c%a8%e7%96%91%e6%83%91%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7" target="_blank">ここです。</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
GitHubにあります。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.22">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.22</a><br />
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
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
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
次のファイルの中身について、「cat <ファイル名>」から初めて、同じワンライナーでそれぞれ中央値を求めてください。データの数が偶数の場合は、中央の二つの値の平均を中央値とします。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat a<br />
1<br />
3<br />
4<br />
1<br />
6<br />
6<br />
8<br />
2<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat b<br />
3.4<br />
13<br />
4242<br />
-4<br />
-5<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
次のような出力から初めて、<br />
<br />
[bash]<br />
ueda\@remote:~$ echo カレーライス 醤油ラーメン | ...<br />
[/bash]<br />
<br />
次のような出力を得てください（表示がずれてますが、「ー」のところで文字列をクロスさせています）。最初のパイプより右側はマルチバイト文字を使わないようにしてみましょう。「ー」が何文字目にあるか等の情報は何でも使って結構です。<br />
<br />
[bash]<br />
 カ<br />
 レ<br />
醤油ラーメン<br />
 ラ<br />
 イ<br />
 ス<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
次のデータについて、<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q3<br />
aaabbb<br />
bababa<br />
aaabbb<br />
aaabbb<br />
bababa<br />
bbbbba<br />
[/bash]<br />
<br />
次のような出力を得てください。<br />
<br />
[bash]<br />
bababa 2 5<br />
aaabbb 1 3 4<br />
bbbbba 6<br />
[/bash]<br />
<br />
次に、得られた答えから元のデータを復元してください。Q3の答えはQ3.ansにあります。<br />
<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
次のファイルについて、素数行目に存在するりんごとみかんをそれぞれ数えてください。できる人は素数の行を2,3,5,7と明示的に指定しないでやってみてください。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q4<br />
りんご<br />
りんご<br />
みかん<br />
みかん<br />
りんご<br />
みかん<br />
りんご<br />
りんご<br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
足して10になる並びを全て見つけてみましょう。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q5<br />
1 3 4 4 2 3 5 6 7 9 1 4<br />
[/bash]<br />
<br />
<br />
<h2>Q6</h2><br />
<br />
次のファイルQ6_1のX,Y,Zに、<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_1 <br />
所謂いわゆる「Z」というものにだって、<br />
もっと何か表情なり印象なりがあるものだろうに、<br />
YのからだにXでもくっつけたなら、<br />
こんな感じのものになるであろうか、<br />
とにかく、どこという事なく、見る者をして、<br />
ぞっとさせ、いやな気持にさせるのだ。<br />
私はこれまで、こんな不思議な男の顔を見た事が、<br />
やはり、いちども無かった。<br />
[/bash]<br />
<br />
Q6_2に書いてある文字列を当てはめてください。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_2<br />
X 駄馬の首<br />
Y 人間<br />
Z 死相<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
明示的に端末を閉じたりシェルを終わらせるためのコマンド（shutdown, reboot, exit, logout等）以外で端末を閉じてみてください。<br />
<br />
<br />
<h2>Q8</h2><br />
<br />
次のC++のコードに関数プロトタイプをくっつけてください。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.cc <br />
#include &lt;iostream&gt;<br />
#include &lt;string&gt;<br />
using namespace std;<br />
<br />
void aho(void)<br />
{<br />
	cout &lt;&lt; nazo() &lt;&lt; endl;<br />
}<br />
<br />
string nazo(void)<br />
{<br />
	return &quot;謎&quot;;<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	aho();<br />
	return 0;<br />
}<br />
[/bash]<br />
<br />
つまりこういう出力を作ります。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.ans.cc <br />
#include &lt;iostream&gt;<br />
#include &lt;string&gt;<br />
using namespace std;<br />
void aho(void);<br />
string nazo(void);<br />
<br />
void aho(void)<br />
{<br />
	cout &lt;&lt; nazo() &lt;&lt; endl;<br />
}<br />
<br />
string nazo(void)<br />
{<br />
	return &quot;謎&quot;;<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	aho();<br />
	return 0;<br />
}<br />
[/bash]<br />
<br />

