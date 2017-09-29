---
Keywords: コマンド,sed,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第27回sedこわいシェル芸勉強会
<a href="https://blog.ueda.asia/?p=9309">問題のみのページ</a>はこちら。

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
対象とするsedはGNU sedだけに絞っています。解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。BSD系の人は玄人なので各自対応のこと。

<h2>Q1</h2>
次のechoの出力について、偶数番目の文字だけ大文字にしてください。できたら、奇数番目の文字だけ大文字にしてください。

```bash
$ echo abcdefghijklmn
```

<h3>解答</h3>

```bash
###偶数番目を大文字に###
$ echo abcdefghijklmn | sed 's/\\(.\\)\\(.\\)/\\1\\U\\2/g'
aBcDeFgHiJkLmN
###奇数番目を大文字に###
$ echo abcdefghijklmn | sed 's/\\(.\\)\\(.\\)/\\U\\1\\L\\2/g'
AbCdEfGhIjKlMn
###-rを使うと多少スッキリする###
$ echo abcdefghijklmn | sed -r 's/(.)(.)/\\U\\1\\L\\2/g'
AbCdEfGhIjKlMn
```

<h2>Q2</h2>
seq 1 100から始めてsedだけでFizzBuzzをやってみましょう。
<h3>解答</h3>

```bash
$ seq 1 100 | sed '0~3s/.*/Fizz/;0~5s/$/Buzz/' |
 sed 's/[0-9]*B/B/' | xargs
```

<h2>Q3</h2>
次の出力について、3行目を7行目の下に移動してください。

```bash
$ seq 1 10
```

<h3>解答</h3>
hで3行目をホールドスペースに突っ込み、Gでパターンスペースに戻します。

```bash
$ seq 1 10 | sed '3h;3d;7G'
```

<h2>Q4</h2>
次のコードのmainとahoの位置を入れ替えてください。

```bash
$ cat aho.cc 
#include <iostream>
using namespace std;

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}

void aho(void)
{
	cout << "aho" << endl;
}
```

<h3>解答</h3>
mainの部分をホールドスペースに入れる→消す→ファイルの一番後ろでホールドスペースを吐き出すという流れになります。

```bash
$ cat aho.cc | sed '/int/,/}/H;/int/,/}/d;$G'
#include <iostream>
using namespace std;


void aho(void)
{
	cout << "aho" << endl;
}

int main(int argc, char const* argv[])
{
	aho();
	return 0;
}
###{}でまとめる###
$ cat aho.cc | sed '/int/,/}/{H;d};$G'
###もうちょっと厳密なやつ###
$ cat aho.cc | sed '/ main(/,/^}/{H;d};$G'
###そのままコンパイルして実行###
$ cat aho.cc | sed '/int/,/}/H;/int/,/}/d;$G' |
 g++ -x c++ - && ./a.out
aho
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

<h3>解答</h3>

```bash
$ seq 1 10 | sed '1~2h;1~2d;0~2G'
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

<h3>解答</h3>
ラベルを使います。

```bash
$ echo 1 | sed ':LOOP p;s/./&&/;b LOOP' | head
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
###分岐を使う###
$ echo 1 | sed ':LOOP p;s/./&&/;/1\\{10\\}/!b LOOP'
```

<h2>Q7</h2>
aというファイルをtouch等で作り、次の縛りでa1, a2, a3, ..., a10というファイルをaからコピーして作ってください。縛り1と縛り2を独立した別々の問題として解き、その後縛り1,2を両方満たす解を考えてみましょう。
<ul>
 	<li>縛り1: 使うコマンドはseq、cp、sedだけ</li>
 	<li>縛り2: ワンライナー中で数字を使わない</li>
</ul>
<h3>解答</h3>

```bash
###縛り1###
$ touch a
$ seq 1 10 | sed 's/./cp a a&/e'
$ ls a a? a10
a a1 a10 a2 a3 a4 a5 a6 a7 a8 a9
###縛り2###
$ yes | sed -n '=' | head | sed 's/./cp a a&/e'
###両方###
$ sed ':a ;p;s/./&&/;/........../!b a' <<< y |
 sed -n = | sed 's/^/cp a a/e'
###（おまけ）ファイルaをsedで作る###
$ sed 'w a' <<< "abc"
abc
$ cat a
abc
```

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

<h3>解答</h3>

```bash
$ echo 1 | sed ':LOOP p;s/./&&/;/1\\{5\\}/!b LOOP' | sed 'p;1!G;h;$!d'
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

