---
Keywords: CLI,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第22回ゴールデンウィークの存在疑惑シェル芸勉強会
- <a href="/?post=08073">問題のみのページはこちら</a>

<h2>イントロのプレゼン資料</h2>

- <a href="/?presenpress=%e7%ac%ac22%e5%9b%9e%e3%82%b4%e3%83%bc%e3%83%ab%e3%83%87%e3%83%b3%e3%82%a6%e3%82%a3%e3%83%bc%e3%82%af%e3%81%ae%e5%ad%98%e5%9c%a8%e7%96%91%e6%83%91%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7" target="_blank">ここです。</a>

<h2>問題で使うファイル等</h2>

GitHubにあります。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.22">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.22</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はUbuntu Linuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>

<h2>Q1</h2>

次のファイルの中身について、「cat <ファイル名>」から初めて、同じワンライナーでそれぞれ中央値を求めてください。データの数が偶数の場合は、中央の二つの値の平均を中央値とします。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat a
1
3
4
1
6
6
8
2
ueda@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat b
3.4
13
4242
-4
-5
```

<h3>解答</h3>

データ数が偶数と奇数の時で場合分けが必要で面倒くさいです。（場合分けのない方法絶賛募集中。）

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat a | sort -n |xargs |
awk 'NF%2==0{print 0.5*($(NF/2)+$(NF/2+1))}NF%2==1{print $(NF/2+1)}'
3.5
ueda@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat b | sort -n | xargs |
awk 'NF%2==0{print 0.5*($(NF/2)+$(NF/2+1))}NF%2==1{print $(NF/2+1)}'
3.4
```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a><br>cat a | st --median<br>cat a | sort -n | awk &#39;{v[i++]=$1;}END {x=int((i+1)/2); if(x&lt;(i+1)/2) print (v[x-1]+v[x])/2; else print v[x-1];}&#39;</p>&mdash; Blacknon(エビス) (@blacknon_) <a href="https://twitter.com/blacknon_/status/726283843154501632">2016年4月30日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<h2>Q2</h2>

次のような出力から初めて、

```bash
ueda@remote:~$ echo カレーライス 醤油ラーメン | ...
```

次のような出力を得てください（表示がずれてますが、「ー」のところで文字列をクロスさせています）。最初のパイプより右側はマルチバイト文字を使わないようにしてみましょう。「ー」が何文字目にあるか等の情報は何でも使って結構です。

```bash
 カ
 レ
醤油ラーメン
 ラ
 イ
 ス
```

<h3>解答</h3>

```bash
ueda@remote:~$ echo カレーライス 醤油ラーメン |
 awk '{print $2;gsub(/./," &\\n",$1);print $1}' |
 awk 'NR==1{a=$1}NR!=1{print $1==substr(a,4,1)?a:$0}'
 カ
 レ
醤油ラーメン
 ラ
 イ
 ス

```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">力技（bash版)<br>Q2 % echo カレーライス 醤油ラーメン | (read a b;grep -o . &lt;&lt;&lt;$a|sed &#39;3!s/^/ /;3s/./&#39;$b&#39;/&#39;)<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (@eban) <a href="https://twitter.com/eban/status/726287523870171136">2016年4月30日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<h2>Q3</h2>

次のデータについて、

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q3
aaabbb
bababa
aaabbb
aaabbb
bababa
bbbbba
```

次のような出力を得てください。

```bash
bababa 2 5
aaabbb 1 3 4
bbbbba 6
```

次に、得られた答えから元のデータを復元してください。Q3の答えはQ3.ansにあります。

<h3>解答</h3>

前半はAWKの連想配列のおさらい問題でした。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q3 |
awk '{a[$1]=a[$1]" "NR}END{for(k in a){print k,a[k]}}' 
bababa 2 5
aaabbb 1 3 4
bbbbba 6
```

復元は次の通り。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q3.ans |
 awk '{for(i=2;i<=NF;i++)print $1,$i}' |
 sort -k2,2n | awk '{print $1}'
aaabbb
bababa
aaabbb
aaabbb
bababa
bbbbba
```


<h2>Q4</h2>

次のファイルについて、素数行目に存在するりんごとみかんをそれぞれ数えてください。できる人は素数の行を2,3,5,7と明示的に指定しないでやってみてください。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q4
りんご
りんご
みかん
みかん
りんご
みかん
りんご
りんご
```

<h3>解答</h3>

先にfactorを使ってからpasteでQ4ファイルをくっつけると楽です。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ seq 1 100 | factor |
 paste - Q4 | awk 'NF==3' | grep -oE '[あ-ん]+' | sort | uniq 
c- 1 みかん
 3 りんご
```

<h2>Q5</h2>

足して10になる並びを全て見つけてみましょう。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q5
1 3 4 4 2 3 5 6 7 9 1 4
```

<h3>解答</h3>

計算量的には損ですが、先に組み合わせを全部列挙すると楽です。ただ、列挙は面倒くさいです。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q5 |
 awk '{for(len=1;len<=NF;len++)for(shift=1;shift<=NF-len+1;shift++)
{for(i=shift;i<shift+len;i++){printf $i" "};print ""}}' |
 awk '{a=0;for(i=1;i<=NF;i++)a+=$i;print $0,a}' | awk '$NF==10'
9 1 10
4 4 2 10
2 3 5 10
```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> Q5 Egison芸<br>$ cat Q5|xargs -n 1|egison -Ts &#39;1#(match-all %1 (list integer)[&lt;join <a href="https://twitter.com/search?q=%24a&amp;src=ctag">$a</a>&lt;join <a href="https://twitter.com/search?q=%24b&amp;src=ctag">$b</a> <a href="https://twitter.com/search?q=%24c&amp;src=ctag">$c</a>&gt;&gt;[b (foldl + 0 b)]])&#39; | grep &#39;10$&#39;</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/726302635733585920">2016年4月30日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<h2>Q6</h2>

次のファイルQ6_1のX,Y,Zに、

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_1 
所謂いわゆる「Z」というものにだって、
もっと何か表情なり印象なりがあるものだろうに、
YのからだにXでもくっつけたなら、
こんな感じのものになるであろうか、
とにかく、どこという事なく、見る者をして、
ぞっとさせ、いやな気持にさせるのだ。
私はこれまで、こんな不思議な男の顔を見た事が、
やはり、いちども無かった。
```

Q6_2に書いてある文字列を当てはめてください。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_2
X 駄馬の首
Y 人間
Z 死相
```

<h3>解答</h3>

sedでsedのコマンドを作ってsedに食わせます。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_2 | sed 's;^;s/;' |
 tr ' ' '/' | sed 's;$;/;' | sed -f - Q6_1
所謂いわゆる「死相」というものにだって、
もっと何か表情なり印象なりがあるものだろうに、
人間のからだに駄馬の首でもくっつけたなら、
こんな感じのものになるであろうか、
とにかく、どこという事なく、見る者をして、
ぞっとさせ、いやな気持にさせるのだ。
私はこれまで、こんな不思議な男の顔を見た事が、
やはり、いちども無かった。
```


<h2>Q7</h2>

明示的に端末を閉じたりシェルを終わらせるためのコマンド（shutdown, reboot, exit, logout等）以外で端末を閉じてみてください。

<h3>解答例</h3>

execで何かコマンドを指定すると、シェルのプロセスが終わって端末が閉じます。（他の方法があれば是非。）

```bash
ueda@remote:~$ exec echo アホ
アホ
Connection to test.usptomo.com closed.
uedamb:~ ueda$ 
```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Q7<br>$ alias eval=&#39;eval eval&#39;<br>$ eval hoge<br>[1] 23695 segmentation fault (core dumped) mksh -l<br>午前の勉強成果です♥ <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="https://twitter.com/hashtag/%E5%8D%B1%E9%99%BA%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#危険シェル芸</a></p>&mdash; ginjiro (@gin_135) <a href="https://twitter.com/gin_135/status/726307646714695680">2016年4月30日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<h2>Q8</h2>

次のC++のコードに関数プロトタイプをくっつけてください。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.cc 
#include <iostream>
#include <string>
using namespace std;

void aho(void)
{
	cout << nazo() << endl;
}

string nazo(void)
{
	return "謎";
}

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}
```

つまりこういう出力を作ります。

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.ans.cc 
#include <iostream>
#include <string>
using namespace std;
void aho(void);
string nazo(void);

void aho(void)
{
	cout << nazo() << endl;
}

string nazo(void)
{
	return "謎";
}

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}
```

<h3>解答例</h3>

```bash
ueda@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.cc | grep ')$' |
 grep -v '^int main' | sed 's/$/;/' |
 awk 'BEGIN{a=0}FILENAME=="-"{a=1}{print a,$0}/using/{a+=2}' Q8.cc - |
 sort -s -k1,1 | sed 's/^..//'
```

<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Q8 % cat Q8.cc | sed &#39;/void/!d;s/$/;/&#39; | sed &#39;/name/r/dev/stdin&#39; Q8.cc <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>&mdash; eban (@eban) <a href="https://twitter.com/eban/status/726313222022647808">2016年4月30日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
