---
Keywords: CLI,USP友の会,勉強会,シェル芸,シェル芸勉強会,難しめ
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第14回東京居残りシェル芸勉強会
<a href="/?post=04413" title="【問題と解答例】第14回東京居残りシェル芸勉強会">解答はコッチ</a>

<h2>始める前に</h2>

今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

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

<h2>イントロ</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/42680416" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>


<h2>Q1</h2>

100!を計算してください。正確に。

<!--more-->

<h2>Q2</h2>

次のseqからsed（と言ってもgsed）だけでfizzbuzzを完成させてください。

```bash
ueda@remote:~$ seq 100 | sed ...
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
...
```

<h2>Q3</h2>

このうち素数はどれでしょうか？

```bash
ueda@remote:~$ echo 0xaf 0x13 0x0d 0x24 0x58
```

<h2>Q4</h2>

次の16進数（UTF-8）で書かれたメッセージを復元してください。

```bash
e89fb9e3818ce9a39fe381b9e3819fe38184
```

<h2>Q5</h2>

次のようなファイルを作ってください。
（catするとahoとだけ出て、容量は1GB。）

```bash
ueda@remote:~$ cat hoge
aho
ueda@remote:~$ ls -l hoge
-rw-r--r-- 1 ueda ueda 1000000000 12月 7 14:53 hoge
```

<h2>Q6</h2>

日本の山を標高の高い順から並べていってください。順位と標高も一緒に出力してください。<a href="http://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%B1%B1%E4%B8%80%E8%A6%A7_%28%E9%AB%98%E3%81%95%E9%A0%86%29" target="_blank">（こちらからcurlで持ってきて加工してください）</a>

おそらく力技になります。


## Q7

分数で正確に答えを求めてください。できれば約分してください。

```bash
echo '1/4 + 2/5 + 7/16 - 5/9'
```

## Q8

```bash
*****************************************************************
```

をポキポキ折ってください。

