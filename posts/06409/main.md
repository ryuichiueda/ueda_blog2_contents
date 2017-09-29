---
Keywords: コマンド,CLI,Linux,Unix,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第17回ジュンク堂はシェル芸が乗っ取った勉強会
<h2>ルール</h2>

<ul>
	<li>ワンライナーで出されたお題を解きます。</li>
	<li>汎用的な解を考えるのは出された問題をとりあえず解いてから。</li>
	<li>特にどの環境とは指定しないので各自環境に合わせて読み替えを。ただし今回、AWKだけはGNU Awk 4.0.1を使っていると明記しておきます。</li>
	<li>今回のテーマはAWKですが、何で解いても構いません。別にPowerShellだろうがRubyだろうが構いません。ワンライナーじゃないけどエクセル方眼紙でも。</li>
</ul>



<h2>環境</h2>
今回はLinuxで解答例を作りましたので、BSDやMacな方は以下の表をご参考に・・・。

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

次のようなデータを

```bash
$ cat data1
a 1
b 4
a 2
a 3
b 5
```

次のように変換してみましょう。

```bash
a 1 2 3
b 4 5
```

余力のある人は次のようなJSON形式にしてみましょう。

```bash
{a:[1,2,3],b:[4,5]}
```

<h2>解答</h2>

連想配列にデータを追記していって最後に出力するのが楽な方法です。

```bash
$ cat data1 | awk '{d[$1]=d[$1]" "$2}END{for(k in d){print k d[k]}}' 
a 1 2 3
b 4 5
```

JSONにするには力技（しか思い浮かばなかった）。

```bash
$ cat data1 | awk '{d[$1]=d[$1]" "$2}END{for(k in d){print k d[k]}}' |
 awk -v q='"' '{printf q$1q":[";for(i=2;i<=NF;i++){printf $i","};print "]"}' |
 xargs | tr ' ' ',' | awk '{print "{"$0"}"}' | sed 's/,]/]/g'
{a:[1,2,3],b:[4,5]}
```

<h2>Q2</h2>

以下の数字のファイルから同じレコード（行）があるかないかを調べ、ある場合には何行目と何行目にあるのか出力しましょう。

```bash
$ cat data
0.5937836043 0.4644710001
0.3637036697 0.5593602512
0.5655269331 0.6793148112
0.7804610574 0.2905477797
0.3637036697 0.5593602512
```

<h2>解答</h2>

```bash
$ cat data | awk 'a[$0]{print a[$0],NR,$0}{a[$0]=NR}'
```

1千万行でも10秒くらいで答えが出ることを確認済みです。もっと大きなレコード数で行う場合はもう一捻り必要です。


<h2>Q3</h2>

次のJSONのデータについて、aに対応づけられた配列内の数字の合計とbに対応づけられた配列内の数字の合計を求めましょう。

```bash
$ cat data
{"a":[1,2,3],"b":[4,5]}
```

<h2>解答</h2>

きれいな方法が思い浮かばないので力技で。

```bash
$ grep -o '"[ab]":\\[[^\\[]*\\]' data | tr '":[],' ' ' |
 awk '{n=0;for(i=2;i<=NF;i++){n+=$i};print $1,n}'
a 6
b 9
$ cat data | jq . | tr -dc '[:alnum:]\\n' |
 awk '/[ab]/{k=$1}!/[ab]/{n[k]+=$1}END{for(k in n){print k,n[k]}}'
a 6
b 9
###jqを使う例を。もっとうまくできるようですが・・・。###
$ cat data | jq 'reduce .a[] as $n (0; . + $n),reduce .b[] as $n (0; . + $n)'
6
9
```

<h2>Q4</h2>

次のようなIPv6アドレスをechoした後にパイプでコマンドをつなぎ、「::」で省略されているセクションに0を補ってください。

```bash
$ echo 2001:db8::9abc
```

ただし、同じワンライナーが

```bash
::1
```

でも使えるようにしてください。

<h2>解答</h2>

whileを使ってNFが8になるまでフィールドを補ってから処理してやると素直な処理になります。初めてシェル芸勉強会でawkのwhileを使いました・・・。

```bash
$ echo 2001:db8::9abc |
 awk -F: '{while(NF!=8){gsub(/::/,":0::",$0)};for(i=1;i<=8;i++){$i=$i!=""?$i:0};print}' |
 tr ' ' ':'
2001:db8:0:0:0:0:0:9abc
$ echo ::1 |
 awk -F: '{while(NF!=8){gsub(/::/,":0::",$0)};for(i=1;i<=8;i++){$i=$i!=""?$i:0};print}' |
 tr ' ' ':'
0:0:0:0:0:0:0:1
###別解###
$ echo 2001:db8::9abc |
 awk -F: '{while(NF!=8){gsub(/::/,":0::",$0)}print}' |
 tr ':' '\\n' | awk '!NF{print 0}NF{print}' | xargs | tr ' ' ':'
```
