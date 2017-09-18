---
Keywords:CLI,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第22回ゴールデンウィークの存在疑惑シェル芸勉強会
- <a href="https://blog.ueda.asia/?p=8073">問題のみのページはこちら</a><br />
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
<h3>解答</h3><br />
<br />
データ数が偶数と奇数の時で場合分けが必要で面倒くさいです。（場合分けのない方法絶賛募集中。）<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat a | sort -n |xargs |<br />
awk 'NF%2==0{print 0.5*($(NF/2)+$(NF/2+1))}NF%2==1{print $(NF/2+1)}'<br />
3.5<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat b | sort -n | xargs |<br />
awk 'NF%2==0{print 0.5*($(NF/2)+$(NF/2+1))}NF%2==1{print $(NF/2+1)}'<br />
3.4<br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a><br>cat a | st --median<br>cat a | sort -n | awk &#39;{v[i++]=$1;}END {x=int((i+1)/2); if(x&lt;(i+1)/2) print (v[x-1]+v[x])/2; else print v[x-1];}&#39;</p>&mdash; Blacknon(エビス) (\@blacknon_) <a href="https://twitter.com/blacknon_/status/726283843154501632">2016年4月30日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
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
<h3>解答</h3><br />
<br />
[bash]<br />
ueda\@remote:~$ echo カレーライス 醤油ラーメン |<br />
 awk '{print $2;gsub(/./,&quot; &amp;\\n&quot;,$1);print $1}' |<br />
 awk 'NR==1{a=$1}NR!=1{print $1==substr(a,4,1)?a:$0}'<br />
 カ<br />
 レ<br />
醤油ラーメン<br />
 ラ<br />
 イ<br />
 ス<br />
<br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">力技（bash版)<br>Q2 % echo カレーライス 醤油ラーメン | (read a b;grep -o . &lt;&lt;&lt;$a|sed &#39;3!s/^/ /;3s/./&#39;$b&#39;/&#39;)<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/726287523870171136">2016年4月30日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
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
<h3>解答</h3><br />
<br />
前半はAWKの連想配列のおさらい問題でした。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q3 |<br />
awk '{a[$1]=a[$1]&quot; &quot;NR}END{for(k in a){print k,a[k]}}' <br />
bababa 2 5<br />
aaabbb 1 3 4<br />
bbbbba 6<br />
[/bash]<br />
<br />
復元は次の通り。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q3.ans |<br />
 awk '{for(i=2;i&lt;=NF;i++)print $1,$i}' |<br />
 sort -k2,2n | awk '{print $1}'<br />
aaabbb<br />
bababa<br />
aaabbb<br />
aaabbb<br />
bababa<br />
bbbbba<br />
[/bash]<br />
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
<h3>解答</h3><br />
<br />
先にfactorを使ってからpasteでQ4ファイルをくっつけると楽です。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ seq 1 100 | factor |<br />
 paste - Q4 | awk 'NF==3' | grep -oE '[あ-ん]+' | sort | uniq <br />
c- 1 みかん<br />
 3 りんご<br />
[/bash]<br />
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
<h3>解答</h3><br />
<br />
計算量的には損ですが、先に組み合わせを全部列挙すると楽です。ただ、列挙は面倒くさいです。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q5 |<br />
 awk '{for(len=1;len&lt;=NF;len++)for(shift=1;shift&lt;=NF-len+1;shift++)<br />
{for(i=shift;i&lt;shift+len;i++){printf $i&quot; &quot;};print &quot;&quot;}}' |<br />
 awk '{a=0;for(i=1;i&lt;=NF;i++)a+=$i;print $0,a}' | awk '$NF==10'<br />
9 1 10<br />
4 4 2 10<br />
2 3 5 10<br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> Q5 Egison芸<br>$ cat Q5|xargs -n 1|egison -Ts &#39;1#(match-all %1 (list integer)[&lt;join <a href="https://twitter.com/search?q=%24a&amp;src=ctag">$a</a>&lt;join <a href="https://twitter.com/search?q=%24b&amp;src=ctag">$b</a> <a href="https://twitter.com/search?q=%24c&amp;src=ctag">$c</a>&gt;&gt;[b (foldl + 0 b)]])&#39; | grep &#39;10$&#39;</p>&mdash; ぐれさん (\@grethlen) <a href="https://twitter.com/grethlen/status/726302635733585920">2016年4月30日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
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
<h3>解答</h3><br />
<br />
sedでsedのコマンドを作ってsedに食わせます。<br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_2 | sed 's;^;s/;' |<br />
 tr ' ' '/' | sed 's;$;/;' | sed -f - Q6_1<br />
所謂いわゆる「死相」というものにだって、<br />
もっと何か表情なり印象なりがあるものだろうに、<br />
人間のからだに駄馬の首でもくっつけたなら、<br />
こんな感じのものになるであろうか、<br />
とにかく、どこという事なく、見る者をして、<br />
ぞっとさせ、いやな気持にさせるのだ。<br />
私はこれまで、こんな不思議な男の顔を見た事が、<br />
やはり、いちども無かった。<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
明示的に端末を閉じたりシェルを終わらせるためのコマンド（shutdown, reboot, exit, logout等）以外で端末を閉じてみてください。<br />
<br />
<h3>解答例</h3><br />
<br />
execで何かコマンドを指定すると、シェルのプロセスが終わって端末が閉じます。（他の方法があれば是非。）<br />
<br />
[bash]<br />
ueda\@remote:~$ exec echo アホ<br />
アホ<br />
Connection to test.usptomo.com closed.<br />
uedamb:~ ueda$ <br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Q7<br>$ alias eval=&#39;eval eval&#39;<br>$ eval hoge<br>[1] 23695 segmentation fault (core dumped) mksh -l<br>午前の勉強成果です♥ <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="https://twitter.com/hashtag/%E5%8D%B1%E9%99%BA%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#危険シェル芸</a></p>&mdash; ginjiro (\@gin_135) <a href="https://twitter.com/gin_135/status/726307646714695680">2016年4月30日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
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
<h3>解答例</h3><br />
<br />
[bash]<br />
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.cc | grep ')$' |<br />
 grep -v '^int main' | sed 's/$/;/' |<br />
 awk 'BEGIN{a=0}FILENAME==&quot;-&quot;{a=1}{print a,$0}/using/{a+=2}' Q8.cc - |<br />
 sort -s -k1,1 | sed 's/^..//'<br />
[/bash]<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q8 % cat Q8.cc | sed &#39;/void/!d;s/$/;/&#39; | sed &#39;/name/r/dev/stdin&#39; Q8.cc <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (\@eban) <a href="https://twitter.com/eban/status/726313222022647808">2016年4月30日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
