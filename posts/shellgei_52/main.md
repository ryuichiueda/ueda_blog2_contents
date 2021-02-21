---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2021 Ryuichi Ueda
---

# 【問題と解答】jus共催 第52回見目麗しく端正で上品なシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.52)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu 20.04で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

ファイル`big_dipper`の星の部分に`chiki`に書かれた「チキチキボーン」という文字を埋め込んでください．

```
$ cat big_dipper 
*

      *
 
      *

       *

   *


             *
       *
$ cat chiki
チキチキボーン
```

参考: 

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">チキチキボーン丼を作ろうと思ってる</p>&mdash; kanata (@kanata201612) <a href="https://twitter.com/kanata201612/status/1357844890629992449?ref_src=twsrc%5Etfw">February 6, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### 解答例

```
$ cat chiki | grep -o . | awk '{print "s_\\*_"$1"_"}' | sed -z -f - big_dipper
$ awk -v s=$(<chiki) '/\*/{gsub(/\*/,substr(s,++a,1));print}!NF' big_dipper
チ

      キ

      チ

       キ

   ボ


             ー
       ン
```


## Q2

　次の`updown`と`chiki`ファイル: 

```
$ cat updown 
^v^^^^v^^^^^vvvvv^vv
$ cat chiki 
チキチキボーン
```

から，次の出力を得てください．

```
チ　チキボー　チキチキボ　　　　　キ　　
^ v ^ ^ ^ ^ v ^ ^ ^ ^ ^ v v v v v ^ v v
　キ　　　　ン　　　　　ーンチキチ　ボー
```

### 解答例

```
$ cat updown | grep -o . | paste -d "" - <(yes $(<chiki) |
grep -o .) | head -n 20 |
sed -E 's/\^(.)/\1 ^ 　/;s/v(.)/　 v \1/' | rs -T | sed 's/  //g'
チ　チキボー　チキチキボ　　　　　キ　　
^ v ^ ^ ^ ^ v ^ ^ ^ ^ ^ v v v v v ^ v v
　キ　　　　ン　　　　　ーンチキチ　ボー
```


## Q3

`dekiru`の「出来」のうち、
ひらがなにすることが適切なものをひらがなに修正して、
別のファイルに保存してください。
文脈に依存するので、一般解を求める必要はありません。
その後、修正前後の原稿の各行を見やすく横に並べて、変更した箇所、
変更していない箇所がひと目で分かるように出力してください。

```
$ cat dekiru
学生の論文を添削していると「できる」を
「出来る」と書いてしまう人がいて、
たまにそれとなく注意を促したり、
だまって直してgitのdiffで気づいてと
思ったりしています。
基本的に、「出来る、出来ない」
はひらがなでかきます。
「出来事」、「出来高」など、
名詞の場合は漢字にします。
細かい話かもしれませんが、
このようなほんの些細なことの積み重ねで、
読みやすい文章になるわけです。
書き手になったときに、それを忘れて
細かいことはどうでもいいという
態度でよいのでしょうか。
プログラムでインデントや変数の名前に厳しい人が、
作文になると甘くなるのは、
単に自分が好きなことだけにこだわっているだけです。
確かにこのような表記のルールは膨大で
完璧には出来ませんし、
学会によっても少し違うこともあります。
しかし、コードの規約と同様、
常によりよい記述が出来ることを
目指す必要があります。
```

### 解答例

```
### 修正 ###
$ cat dekiru | sed -E 's/出来([ぁ-ん])/でき\1/g' |
sed '2s/できる/出来る/g'  > ans
### 確認（grepは色つけのため） ###
$ cat dekiru | awk '{printf("%-40s\n",$0)}' | paste - ans | awk '{print $1==$2?" ":"*",$0}' | grep -e 出来 -e でき -e '^'
  学生の論文を添削していると「できる」を                     	学生の論文を添削していると「できる」を
  「出来る」と書いてしまう人がいて、                       	「出来る」と書いてしまう人がいて、
  たまにそれとなく注意を促したり、                        	たまにそれとなく注意を促したり、
  だまって直してgitのdiffで気づいてと                   	だまって直してgitのdiffで気づいてと
  思ったりしています。                              	思ったりしています。
* 基本的に、「出来る、出来ない」                         	基本的に、「できる、できない」
  はひらがなでかきます。                             	はひらがなでかきます。
  「出来事」、「出来高」など、                          	「出来事」、「出来高」など、
  名詞の場合は漢字にします。                           	名詞の場合は漢字にします。
  細かい話かもしれませんが、                           	細かい話かもしれませんが、
  このようなほんの些細なことの積み重ねで、                    	このようなほんの些細なことの積み重ねで、
  読みやすい文章になるわけです。                         	読みやすい文章になるわけです。
  書き手になったときに、それを忘れて                       	書き手になったときに、それを忘れて
  細かいことはどうでもいいという                         	細かいことはどうでもいいという
  態度でよいのでしょうか。                            	態度でよいのでしょうか。
  プログラムでインデントや変数の名前に厳しい人が、                	プログラムでインデントや変数の名前に厳しい人が、
  作文になると甘くなるのは、                           	作文になると甘くなるのは、
  単に自分が好きなことだけにこだわっているだけです。               	単に自分が好きなことだけにこだわっているだけです。
  確かにこのような表記のルールは膨大で                      	確かにこのような表記のルールは膨大で
* 完璧には出来ませんし、                             	完璧にはできませんし、
  学会によっても少し違うこともあります。                     	学会によっても少し違うこともあります。
  しかし、コードの規約と同様、                          	しかし、コードの規約と同様、
* 常によりよい記述が出来ることを                         	常によりよい記述ができることを
  目指す必要があります。                             	目指す必要があります。
```

## Q4

`aho.html`は、一箇所、タグの名前が間違っているところがあります。間違いは何行目にあるでしょうか。何行目にあればよいか分かれば、全部ワンライナーで解く必要はなく、目視をつかっても構いません。


### 解答例

こたえは293行目でした。

```
$ grep -Eo -e '<[a-z]+' -e '[a-z]+>' aho.html  | tr -d '<>' | sort -u
a
aside
body
br
button
code
div
footer
form
h
head
hr
html
i
img
input
ins
li
link
meta
nav
p
pre
script
span
spin
strong
title
ul
$ grep -n spin aho.html
293:<a class="sourceLine" id="cb10-2" title="2"><span class="fu">awk</spin> <span class="st">&#39;{t=2*3.14*$2/1000000000;c=cos(t)*5+5;s=sin(t)*10+13;</span></a>
```


## Q5

次の`annotation.md`は、ソフトウェアデザイン2018年3月号のシェル芸人からの挑戦状で用いたものです。
このマークダウンについて、文中の`[^about_a]`などの注釈の記号の部分に、ファイル下の注釈を埋め込んでください。
埋め込む際は、TeXの記号`\footnote{...}`を使ってください。

```
$ cat annotation.md
# Aについて

A[^about_a]は素晴らしい。
Aのに似たものとしてB[^about_b]が存在するが、やはりAには及ばない。
他方でAに匹敵すると言われるC[^about_c]が近年注目を集めているが、これについても触れたい。
CとはもともとはDを発展させたものであり、F[^abort_f]という別名もある。

[^about_a]: Aの起源は室町時代に遡る。
[^about_c]: Cの起源は江戸時代に遡る。
[^about_d]: Dの起源はわからない。
[^about_f]: Fはおいしい。
```

出力例を示します。

```
# Aについて

A\footnote{Aの起源は室町時代に遡る。}は素晴らしい。
Aのに似たものとしてB[^about_b]が存在するが、やはりAには及ばない。
他方でAに匹敵すると言われるC\footnote{Cの起源は江戸時代に遡る。}が近年注目を集めているが、これについても触れたい。
CとはもともとはDを発展させたものであり、F[^abort_f]という別名もある。
```


### 解答例

```
$ cat annotation.md | awk '{print $1,"\\\\footnote{"$2"}"}' |
grep '\[\^.*\]:' | sed 's;^;s/;' | sed 's;: ;/;' | sed 's;$;/;' |
sed -E 's/(\[|\^|\])/\\&/g' | sed -f - annotation.md | grep -v '^\\footnote{.*}:'
```

## Q6

TeXは、章のタイトルや式のうしろに`\label{ラベル}`と書くと、
章や式の番号を`\ref{ラベル}`で埋め込むことができます。
これを踏まえて、

1. ラベルがあるのに参照されていない
2. 存在しないラベルを参照している

箇所の行番号と行を出力してください。1と2を区別する必要はありません。

### 解答例

```
$ cat contents.tex | grep -Po '\\(ref|label){[^{]*}' |
tr '\{}' '   ' | sort -u | sort -k2,2 | uniq -f 1 -u |
awk '{print $1"{"$2"}"}' | grep -n -f - contents.tex
19:\subsection{ロボットの姿勢と座標系}\label{sub:pose}
116:	\varphi_{c,t} \sim \mathcal{N}\left(\varphi_{c,t}^*,(3\pi/180)^2\right) \label{eq:phidist}\\
157:\ref{sub:noise}項でモデル化した雑音から計算する。
170:	\V{e}_{c,t,t'} = \V{x}_t' - \V{x}_t - \V{\mu}_{c,t,t'}\label{eq:e}
220:また、式(\ref{eq:unko})から、
242:	\end{bmatrix} \label{eq:e2}
319:また、\ref{sub:noise}項の定義では、遠いところでランドマークを
```

## Q7

TeXの原稿`contents.tex`から，3x3行列を抜き出してください．
3x3行列は，次のように記述されています．

* `\begin{bmatrix}`から`\end{bmatrix}`の間に3行で記述されている．
* 各行に`&`で区切られた3個の式が記述されている．
* 各行の行末は`\\`で終わっている．

一般解を考えるのは大変なので、とりあえずbmatrixの部分を抽出して、3x3行列だけ残せばよいです。

### 解答例

```
$ cat contents.tex |
awk '/\\begin{bmatrix}/,/\\end{bmatrix}/{printf $0"@@@"}/\\end{bmatrix}/{print ""}' |
awk '{a=$0;print gsub(/&/,"",a),$0}' | grep ^6 | sed 's/@@@/\n/g' | sed 's/^6//'
 	\begin{bmatrix}
	(d_{c,t}/10)^2 & 0 & 0 \\
	0 & [(d_{c,t}/10)\sin(3\pi/180)]^2 & 0 \\
	0 & 0 & (3\pi/180)^2\cdot 2
	\end{bmatrix}

 	\begin{bmatrix}
	c & s  & 0 \\
	-s & c & 0 \\
	0 & 0 & 1
	\end{bmatrix}

 	\begin{bmatrix}
		-1 &  0 & d_{c,t} \sin(\theta_t + \varphi_{c,t}) \\
		 0 & -1 & -d_{c,t} \cos(\theta_t + \varphi_{c,t}) \\
		 0 &  0 & -1
	\end{bmatrix} \\

 	\begin{bmatrix}
		 1 & 0 & -d_{c,t'} \sin(\theta_{t'} + \varphi_{c,t'})\\
		 0 & 1 & d_{c,t'} \cos(\theta_{t'} + \varphi_{c,t'})\\
		 0 & 0 & 1
	\end{bmatrix}

```

## Q8

TeXの原稿`contents.tex`には、別の場所に全く同じテキストが複数行にわたって重複して書いてある部分がいくつかあります。
「複数行にわたって重複」というのは、たとえば「1〜3行目と100〜102行目が全く同じ」というような意味です。
このような部分の行番号を求めてください。
出力から目視できればよく、特に出力を整形する必要はありません。
`\begin{align}`や空行など、コンテンツに関係ないものが複数行にわたって重複している部分は出力しなくても大丈夫です。


### 解答例


つぎのようにすると、208〜210行目と224〜226行目、214〜216行目と230〜232行目が複数行にわたって重複していることが分かります。

```
cat contents.tex | tr ' \t' __ | awk '!/^$/{print NR,$0}' |
sort -k2,2 | uniq -f 1 -D | sort -k1,1n | grep -v begin | grep -v end
208 _d_{c,t}_\cos(\theta_t_+_\varphi_{c,t})_\\
209 _d_{c,t}_\sin(\theta_t_+_\varphi_{c,t})_\\
210 _\psi_{c,t}
214 _d_{c,t'}_\cos(\theta_{t'}_+_\varphi_{c,t'})_\\
215 _d_{c,t'}_\sin(\theta_{t'}_+_\varphi_{c,t'})_\\
216 _\psi_{c,t'}
224 _d_{c,t}_\cos(\theta_t_+_\varphi_{c,t})_\\
225 _d_{c,t}_\sin(\theta_t_+_\varphi_{c,t})_\\
226 _\psi_{c,t}
230 _d_{c,t'}_\cos(\theta_{t'}_+_\varphi_{c,t'})_\\
231 _d_{c,t'}_\sin(\theta_{t'}_+_\varphi_{c,t'})_\\
232 _\psi_{c,t'}
```
