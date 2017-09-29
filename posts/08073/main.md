---
Keywords: CLI,UNIX/Linuxサーバ,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第22回ゴールデンウィークの存在疑惑シェル芸勉強会
- <a href="https://blog.ueda.asia/?p=8028">解答はこちら</a>

<h2>イントロのプレゼン資料</h2>

- <a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac22%e5%9b%9e%e3%82%b4%e3%83%bc%e3%83%ab%e3%83%87%e3%83%b3%e3%82%a6%e3%82%a3%e3%83%bc%e3%82%af%e3%81%ae%e5%ad%98%e5%9c%a8%e7%96%91%e6%83%91%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7" target="_blank">ここです。</a>

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
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat a
1
3
4
1
6
6
8
2
ueda\@remote:~/GIT/ShellGeiData/vol.22/Q1$ cat b
3.4
13
4242
-4
-5
```


<h2>Q2</h2>

次のような出力から初めて、

```bash
ueda\@remote:~$ echo カレーライス 醤油ラーメン | ...
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

<h2>Q3</h2>

次のデータについて、

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q3
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



<h2>Q4</h2>

次のファイルについて、素数行目に存在するりんごとみかんをそれぞれ数えてください。できる人は素数の行を2,3,5,7と明示的に指定しないでやってみてください。

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q4
りんご
りんご
みかん
みかん
りんご
みかん
りんご
りんご
```


<h2>Q5</h2>

足して10になる並びを全て見つけてみましょう。

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q5
1 3 4 4 2 3 5 6 7 9 1 4
```


<h2>Q6</h2>

次のファイルQ6_1のX,Y,Zに、

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_1 
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
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q6_2
X 駄馬の首
Y 人間
Z 死相
```


<h2>Q7</h2>

明示的に端末を閉じたりシェルを終わらせるためのコマンド（shutdown, reboot, exit, logout等）以外で端末を閉じてみてください。


<h2>Q8</h2>

次のC++のコードに関数プロトタイプをくっつけてください。

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.cc 
#include <iostream&gt;
#include <string&gt;
using namespace std;

void aho(void)
{
	cout << nazo() << endl;
}

string nazo(void)
{
	return &quot;謎&quot;;
}

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}
```

つまりこういう出力を作ります。

```bash
ueda\@remote:~/GIT/ShellGeiData/vol.22$ cat Q8.ans.cc 
#include <iostream&gt;
#include <string&gt;
using namespace std;
void aho(void);
string nazo(void);

void aho(void)
{
	cout << nazo() << endl;
}

string nazo(void)
{
	return &quot;謎&quot;;
}

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}
```


