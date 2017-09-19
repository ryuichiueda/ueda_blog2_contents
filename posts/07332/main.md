---
Keywords: コマンド,CLI,USP友の会,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第20回記念、年末年始の浮ついた気分大粉砕シェル芸勉強会
<a href="https://blog.ueda.asia/?p=7196">解答例はコチラ</a>

<h2>イントロ</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/eosHmifvAQbFmL" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20-56450263" title="第20回シェル芸勉強会イントロ" target="_blank">第20回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div>

<h2>問題で使うファイル等</h2>

前回からGitHubに置くようにしました。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
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



<h2>Q1</h2>

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.20/Q1" target="_blank">リポジトリ内のvol.20/Q1ディレクトリ</a>には次のように数字が書いてあるファイルが4つ入っています。

```bash
$ ls 
file_A-1 file_A-2 file_B-1 file_B-2
$ head -n 2 *
==&gt; file_A-1 &lt;==
1
31351

==&gt; file_A-2 &lt;==
11
35

==&gt; file_B-1 &lt;==
-32
12

==&gt; file_B-2 &lt;==
912
3
```

file_A-*のグループ、file_B-*のグループからそれぞれ最大の数を探してください。他にfile_C-*、file_D-*、・・・とグループがたくさんあると想定して、1回のワンライナーで両方探すこととします。


<h2>Q2</h2>

<a href="http://ja.uncyclopedia.info/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8" target="_blank">アンサイクロぺディアのシェル芸のページ</a>から、「カースト最上位者が日常的に書く、素数を出力するワンライナー」のコードを取得して実行してください。


<h2>Q3</h2>

次のファイルについて、奇数を1列目、偶数を2列目に振り分けて、奇数の列を昇順、偶数の列を降順にソートしてください。

```bash
$ cat Q3
1
4
2
9
5
8
```

つまりこうしてください。

```bash
1 8
5 4
9 2
```

<h2>Q4</h2>

今、ログインしているサーバについて、自分の今使っているリモート端末以外の端末を抹殺してください。rootになっても構いません。

<h2>Q5</h2>

任意の二つの自然数をechoして最大公約数を求めましょう。


<h2>Q6</h2>

ファイルQ6の中の人の名前について、誰が1列目と2列目の何番めに記述されているかを提示してください。

```bash
###スペースは全角###
$ cat Q6
山田　上田　吉田　武田
吉田　武田　上田　山田
```

解答例は次のようなものです。

```bash
吉田 3 1
山田 1 4
上田 2 3
武田 4 2
```

<h2>Q7</h2>

一部分に「魚」を持つ漢字をなるべくたくさん列挙してみてください。方法はお任せします。

<h2>Q8</h2>

次の漢数字をアラビア数字に変換しましょう。


```bash
$ cat Q8 
五千七百三十五
四千三
四十五
九万六千二百三十三
十一
百十二
```

<h2>宣伝</h2>

[amazonjs asin="4774173444" locale="JP" title="シェルプログラミング実用テクニック (Software Design plus)"]
