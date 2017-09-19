---
Keywords: コマンド,UNIX/Linuxサーバ,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第29回激しいシェル芸勉強会
<a href="https://blog.ueda.tech/?p=9870">解答のページはこちら</a>

<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.29" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.29</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


<h2>環境</h2>
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールしてつかいましょう。BSD系の人は玄人なので各自対応のこと。

<h2>イントロ</h2>
<ul>

	<li><a href="https://blog.ueda.tech/?presenpress=%E7%AC%AC29%E5%9B%9E%E6%BF%80%E3%81%97%E3%81%84%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8%E5%8B%89%E5%BC%B7%E4%BC%9A#/">こちら</a></li></ul>


<h2>Q1</h2>

次の2つのファイルは、講義で出した課題1,2それぞれの点数です。

```bash
$ cat kadai1
001 山田 20
002 出川 30
005 鳥海 44
$ cat kadai2 
001 山田 20
003 上田 15
004 今泉 22
005 鳥海 44
```

両方に名前のある人については点数を合計して、次のように全員の得点リストを作ってください。

```bash
001 山田 40
002 出川 30
003 上田 15
004 今泉 22
005 鳥海 88
```

<h2>Q2</h2>

次の2つのファイルは、5回の講義の出欠と6回目の講義で出席した人の番号のデータです。attendに6回目の講義の出欠を反映したデータを標準出力に出力してください。

```bash
$ cat attend
001 山田 出出欠出出
002 出川 出出欠欠欠
003 上田 出出出出出
004 今泉 出出出出出
005 鳥海 欠出欠出欠
$ cat attend6
001,005,003
```


<h2>Q3</h2>

次の2つのファイルは5回の講義の出欠とテストの成績を記録したファイルです。

```bash
###$1: 番号, $2: 名前, $3: 出欠 ###
$ cat attend 
001 山田 出出欠出出 
002 出川 出出欠欠欠
003 上田 出出出出出
004 今泉 出出出出出
005 鳥海 欠出欠出欠
###$1: 番号, $2: テストの点数（受けてない人のデータは無い）###
$ cat test 
001 90
002 78
004 80
005 93
```

こういうルールで、最終的な点数を出して、番号、名前、点数を記録したファイル作ってください。

<ul>
	<li>出席が過半数に満たない人、テストを受けていない人は0点</li>
	<li>出席が過半数の人はテストの点数を採用</li>
</ul>


<h2>Q4</h2>

<h3>Q4.1</h3>

次の出力をパイプで受けて

```bash
$ echo -1 4 5 2 42 421 44 311 -9 -11
```

次のように同じ桁のものを横並びに出力を得てください。横に並べる時の順番は任意とします。また、この出力のように正の数と負の数を分けます。

```bash
-11 
-9 -1 
2 4 5 
42 44 
311 421 
```

<h3>Q4.2</h3>

次の出力をパイプで受けて

```bash
$ echo -1 +4 5 2 42 421 44 311 -9 -11
```

次のように同じ桁のものを横並びに出力を得てください。Q1.1と同じく横に並べる時の順番は任意とします。

```bash
-11 
-9 -1 
2 +4 5 
42 44 
311 421 
```

<h2>Q5</h2>

次のファイルの中身について、

```bash
$ cat triangle 
 1
 3 9
 7 a 6
8 4 2 5
```

次のように右に転がしてください。できる人はawkを使わないでやってみましょう。

```bash
 8 
 4 7 
 2 a 3 
5 6 9 1
```

<h2>Q6</h2>

次の1から100までの素数を書いたファイル（いくつか欠番が存在）について、

```bash
$ cat prime 
2 3 5 7 11 13 17 19 31 37 41 43 47 53 59 67 71 73 79 83 89 97
```

次のように欠番のところで折り返してください。（ワンライナーの中に欠番を直接書かないでくださいね。）

```bash
2 3 5 7 11 13 17 19 
31 37 41 43 47 53 59 
67 71 73 79 83 89 97
```


<h2>Q7</h2>

リポジトリ内のnyaan.htmlは、ブラウザで見ると次のように見えます。<a href="81487cda9a61853c1fd356329c35e86d.png"><img src="81487cda9a61853c1fd356329c35e86d-1024x462.png" alt="" width="660" height="298" class="aligncenter size-large wp-image-9897" /></a>

次のようにcatから始めて、この文字を（大きなまま）端末上に表示してみてください。
```bash
$ cat ./nyaan.html | ...
```

できる人は小さい通常の文字で「にゃーん」と出してみてください（これは解答例を考えていません）。


<h2>Q8</h2>

次のshellgeiファイルについて、

```bash
$ cat shellgei 
 m 
 &quot;&quot;m m &quot;m # # # # 
 mm # # #mmm&quot;&quot;&quot; m&quot; 
 &quot; m&quot; mmm&quot;&quot; # # # m&quot; # mm&quot;&quot;m 
 m&quot; #mm m&quot; # m&quot; &quot; # # 
 &quot;mm&quot;&quot; &quot;&quot;&quot;&quot; &quot; m&quot; #&quot; m&quot; # 
 
 
```

次のように、文字の無い列を詰めてください。

```bash
 m 
 &quot;&quot;m m &quot;m # # # #
mm # # #mmm&quot;&quot;&quot; m&quot; 
 &quot; m&quot; mmm&quot;&quot; # # # m&quot; # mm&quot;&quot;m 
 m&quot; #mm m&quot; # m&quot; &quot; # # 
&quot;mm&quot;&quot; &quot;&quot;&quot;&quot; &quot;m&quot; #&quot; m&quot; # 
```

