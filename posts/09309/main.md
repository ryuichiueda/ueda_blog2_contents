---
Keywords: コマンド,Linux,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第27回sedこわいシェル芸勉強会
解答例は<a href="https://blog.ueda.asia/?p=9283">こちら</a>。

<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.27" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.27</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>イントロ</h2>

<ul>
 <li><a target="_blank" href="https://blog.ueda.asia/?post_type=presenpress&p=9312">スライド</a></li>
</ul>

<h2>環境</h2>

対象とするsedはGNU sedだけに絞っています。解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。GSD系の人は玄人なので各自対応のこと。

<h2>Q1</h2>

次のechoの出力について、偶数番目の文字だけ大文字にしてください。できたら、奇数番目の文字だけ大文字にしてください。

```bash
$ echo abcdefghijklmn
```


<h2>Q2</h2>

seq 1 100から始めてsedだけでFizzBuzzをやってみましょう。


<h2>Q3</h2>

次の出力について、3行目を7行目の下に移動してください。

```bash
$ seq 1 10
```


<h2>Q4</h2>

次のコードのmainとahoの位置を入れ替えてください。

```bash
$ cat aho.cc 
#include <iostream&gt;
using namespace std;

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}

void aho(void)
{
	cout << &quot;aho&quot; << endl;
}
```


<h2>Q5</h2>

seq 1 10 | から始めて次のような出力を作ってください。

```bash
2
1
4
3
6
5
8
7
10
9
```


<h2>Q6</h2>

echo 1から始めて次のような出力を作ってください。

```bash
1
11
111
1111
11111
111111
1111111
11111111
111111111
1111111111
```


<h2>Q7</h2>
aというファイルをtouch等で作り、次の縛りでa1, a2, a3, ..., a10というファイルをaからコピーして作ってください。縛り1と縛り2を独立した別々の問題として解き、その後縛り1,2を両方満たす解を考えてみましょう。
<ul>
 	<li>縛り1: 使うコマンドはseq、cp、sedだけ</li>
 	<li>縛り2: ワンライナー中で数字を使わない</li>
</ul>

<h2>Q8</h2>

echo 1 | から始めて、あとはsedだけで次のような出力を得てください。

```bash
1
11
111
1111
11111
11111
1111
111
11
1
```


