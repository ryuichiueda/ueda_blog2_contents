---
Keywords: コマンド,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第24回◯◯o◯裏番組シェル芸勉強会
問題のみのページは<a href="/?post=08639">こちら</a>

<h2>イントロ</h2>

<ul>
	<li><a href="/?presenpress=%e7%ac%ac24%e5%9b%9e%e2%97%af%e2%97%afo%e2%97%af%e8%a3%8f%e7%95%aa%e7%b5%84%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">スライドのリンク</a></li>
</ul>


<h2>問題で使うファイル等</h2>

GitHubにあります。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>

今回はUbuntu Linux 16.04で解答例を作りました。

<h2>Q1</h2>

```bash
$ cat Q1
玉子 卵 玉子 玉子 玉子 玉子
玉子 玉子 卵 卵 卵 玉子
卵 玉子 卵 玉子 玉子 玉子
卵 玉子 卵 卵 卵 卵
玉子 卵 玉子
```

上のようなQ1ファイルについて、次のような出力を得てください。


```bash
玉子:5 卵:1 
玉子:3 卵:3 
玉子:4 卵:2 
玉子:1 卵:5 
玉子:2 卵:1 
```

<h3>解答</h3>

AWKの力技になります。力技でない方法を募集。

```bash
$ cat Q1 |
 awk '{for(i=1;i<=NF;i++){a[$i]++};for(k in a){printf("%s:%d ",k,a[k]);a[k]=0}print ""}'
玉子:5 卵:1 
玉子:3 卵:3 
玉子:4 卵:2 
玉子:1 卵:5 
玉子:2 卵:1 
```


<h2>Q2</h2>

次のようなテキストについて、繰り返し出てきた文字の2つ目以降を省いて出力してください。例えばQ2のファイル

```bash
$ cat Q2
へのへのもへじ
```

の場合、「へのもじ」が正解の出力になります。


<h3>解答</h3>

```bash
$ cat Q2 | grep -o . | nl | sort -k2,2 -k1,1n |
 uniq -f 1 | sort | awk '{printf $2}' | xargs
へのもじ
$ cat Q2 | grep -o . | awk '{if(!a[$1]){printf $1};a[$1]=1}END{print ""}'
へのもじ
$ < Q2 grep -o . | awk '{if(!a[$1]){printf $1};a[$1]=1}' | xargs
へのもじ
```


<h2>Q3</h2>

```bash
$ cat Q3
金 日成
キム ワイプ
金 正日
キム タオル
金 正男
```

というデータを、

```bash
%%
キム タオル
キム ワイプ
%%
金 正男
金 正日
金 日成
%%
```

というように第一フィールドをキーにして%%でレコードを区切ってください。awkを使ってできた人は、awkを使わないでやってみてください。

<h3>解答</h3>

```bash
$ sort Q3 | awk '{if($1!=a){print "%%";print;a=$1}else{print}}END{print "%%"}'
%%
キム タオル
キム ワイプ
%%
金 正男
金 正日
金 日成
%%
$ sort Q2 | rev | uniq --group=both -f 1 | rev | sed 's/^$/%%/'
%%
キム タオル
キム ワイプ
%%
金 正男
金 正日
金 日成
%%
```

<h2>Q4</h2>

Q4.xlsxのA1のセルには数字が書いてあります。その数字を出力してください。A4には文字列が書いてあるので余裕がある人はそれも特定してみましょう。

<h3>解答</h3>

A1のセル（数字の読み方）

```bash
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml | sed 's;</c>;&\\n;g' |
 grep -o '<c.*</c>' | grep A1 | sed 's;.*<v>;;' | sed 's;<.*;;'
114514
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml | hxselect -s '\\n' c |
 grep A1 | hxselect -c v
114514
```

A2の文字列の読み方。シートには文字列のIDが書いてあるのでこれで文字列のシートを読んで特定。

```bash
###これで6番目（0番から始まるので7番目）の文字列とわかる###
$ unzip -p Q4.xlsx xl/worksheets/sheet1.xml |
 hxselect -s '\\n' c | grep A4
<c r="A4" t="s"><v>6</v></c>
###抽出###
$ unzip -p Q4.xlsx xl/sharedStrings.xml |
 hxselect -s '\\n' si | awk 'NR==7'
<si><t>エクシェル芸</t><rPh sb="5" eb="6"><t>ゲ</t></rPh><phoneticPr fontId="1"/></si>
```

<h2>Q5</h2>

ファイルQ5について、xに好きな数を代入して各行の式を計算してください。

```bash
$ cat Q5
x + x^2
x + 1/x
x*x*x
```

余裕のある人は、例えばxに2を代入したければ、

```bash
$ echo 2 | ...
```

というようにecho <代入したい数>から始めてワンライナーで解いてみてください。

<h3>解答</h3>

例えばこれで解けます。(-2)のカッコはQ5ファイルでは不要なようです。

```bash
$ sed 's/x/(-2)/g' Q5 | bc -l
2
-2.50000000000000000000
-8
```

echo <数字>からスタートすると、ややこしくなります。

```bash
$ echo -2 | xargs -I@ awk -v a=@ '{gsub(/x/,a,$0);print}' Q5 | bc -l
2
-2.50000000000000000000
-8
```


<h2>Q6</h2>

「玉子」と「卵」の数を数えて、数が少ない方を数が大きい方で置換してください。

```bash
$ cat Q6 
卵卵玉子玉子玉子玉子玉子卵卵卵玉子玉子卵玉子玉子玉子玉子卵卵玉子卵玉子卵卵玉子卵玉子
```

<h3>解答</h3>

力技です。

```bash
$ cat Q6 | grep -oE '(玉子|卵)' | sort | uniq -c |
 sort -n -k1,1n | awk '{print $2}' | xargs |
 awk '{print "s/"$1"/"$2"/g"}' | xargs -I@ sed @ Q6
玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子玉子
```

<h2>Q7</h2>

次のseq（あるいはjot等）の出力から、各桁の数字の構成が同じもの（例: 11122と22111等）を重複とみなし、除去してください。

```bash
$ seq -w 00000 99999
```

<h3>解答</h3>

```bash
###asortを使う場合###
$ seq -w 00000 99999 | sed 's/./& /g' |
 awk '{for(i=1;i<=NF;i++)a[i]=$i;asort(a);for(k in a){printf a[k]}print ""}' |
 sort -u
###ちょっと気の利いた方法（数字が小さい順に並んでいるものだけ残す）###
$ seq -w 00000 99999 | sed 's/./& /g' |
 awk '$1<=$2&&$2<=$3&&$3<=$4&&$4<=$5' | tr -d ' ' 
```


<h2>Q8</h2>

1. まず、1〜7を全て含む7桁の整数を全て列挙して、tmpというファイルに出力してください。

2. 次に、相異なる７以下の正の整数a,b,c,d,e,f,gを用いて、
<code>
abcd + efg
</code>
と表せる素数と、その時のa〜gの数字を全て求めましょう。tmpを用いて構いません。

（参考: 2011年日本数学オリンピック予選第3問から。一部改。<a href="http://www.imojp.org/challenge/old/jmo21yq.html" target="_blank">http://www.imojp.org/challenge/old/jmo21yq.html</a>）

<h3>解答</h3>

1は力技になります。

```bash
$ seq -w 0000000 9999999 | grep -v [089] |
 grep 1 | grep 2 | grep 3 | grep 4 | grep 5 | grep 6 | grep 7 > tmp
```

2は、うまくwhileとfactorを使って求めます。

```bash
$ cat tmp | sed 's/./& /g' | awk '{print $1$2$3$4$5$6$7,$1*$2*$3*$4+$5*$6*$7}' | while read a b ; do echo $b | factor | awk -v n=$a 'NF==2{gsub(/./,"& ",n);print n,$2}' ; done 
2 3 4 6 1 5 7 179
2 3 4 6 1 7 5 179
2 3 4 6 5 1 7 179
2 3 4 6 5 7 1 179
2 3 4 6 7 1 5 179
2 3 4 6 7 5 1 179
2 3 6 4 1 5 7 179
2 3 6 4 1 7 5 179
2 3 6 4 5 1 7 179
...
```
