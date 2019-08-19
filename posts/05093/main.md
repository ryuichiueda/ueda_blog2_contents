---
Keywords: コマンド,Linux,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答例】第15回ドキッ！grepだらけのシェル芸勉強会
<h1>イントロのスライド</h1>

<iframe src="//www.slideshare.net/slideshow/embed_code/44124362" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/20150201-15grep" title="20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）" target="_blank">20150201 第15回シェル芸勉強会イントロ（ドキッ！grepだらけのシェル芸勉強会）</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h1>諸注意</h1>

解答はUbuntu Linux 14.04で作成しました。コマンドがないときは適宜インストールのほど。

Macな人はbrewでGNU grep（ggrep）をインストールすると良かれ悪しかれ拡張オプションが使えます。インストール方法は例えばこちらが分かりやすいかと。3行で済みます。

<iframe marginwidth="0" marginheight="0" src="http://b.hatena.ne.jp/entry.parts?url=http%3A%2F%2Fqiita.com%2Fquattro_4%2Fitems%2Fe75f2b4156ef45fb6640" scrolling="no" frameborder="0" height="230" width="500"><div class="hatena-bookmark-detail-info"><a href="http://qiita.com/quattro_4/items/e75f2b4156ef45fb6640">高速化したGNU grepをインストールする - Qiita</a><a href="http://b.hatena.ne.jp/entry/qiita.com/quattro_4/items/e75f2b4156ef45fb6640">はてなブックマーク - 高速化したGNU grepをインストールする - Qiita</a></div></iframe>

<!--more-->

<h2>Q1</h2>

次のようにファイルを作ります。

```bash
$ seq 2 5 > a
$ seq 1 9 > b
$ seq 5 11 > c
$ seq 3 6 > d
```

1という文字を含まないファイルを列挙してください（aとdですね）。

<!--more-->

<h1>解答</h1>

```bash
$ grep -L 1 {a..d}
a
d
###-Lを知らなければ###
$ grep -c 1 {a..d} | awk -F: '$2==0'
a:0
d:0
```

<h2>Q2</h2>

作業ディレクトリを作り、その下に次のようにfile.1〜file.10000というファイルを作ります。

```bash
$ seq 1 10000 | xargs -I@ touch file.@
```

以下の数字を持つファイルだけ残して後のファイルを消去してください。

<ul>
 <li>1〜9</li>
 <li>10, 20, 30, ..., 90</li>
 <li>数字の下2桁が0のファイル</li>
</ul>


<!--more-->

<h1>解答</h1>

```bash
$ ls -f | grep -v "file\\..$" | grep -v "file\\..0$" | grep -v "file\\..*00$" | xargs rm
rm: cannot remove ‘.’: Is a directory
rm: cannot remove ‘..’: Is a directory
###こんな書き方も###
$ ls -f | 
grep -v -e "file\\..$" -e "file\\..0$" -e "file\\..*00$" |
xargs rm
rm: cannot remove ‘.’: Is a directory
rm: cannot remove ‘..’: Is a directory
$ ls
file.1 file.2300 file.4 file.5400 file.70 file.8500
file.10 file.2400 file.40 file.5500 file.700 file.8600
file.100 file.2500 file.400 file.5600 file.7000 file.8700
file.1000 file.2600 file.4000 file.5700 file.7100 file.8800
file.10000 file.2700 file.4100 file.5800 file.7200 file.8900
file.1100 file.2800 file.4200 file.5900 file.7300 file.9
file.1200 file.2900 file.4300 file.6 file.7400 file.90
file.1300 file.3 file.4400 file.60 file.7500 file.900
file.1400 file.30 file.4500 file.600 file.7600 file.9000
file.1500 file.300 file.4600 file.6000 file.7700 file.9100
file.1600 file.3000 file.4700 file.6100 file.7800 file.9200
file.1700 file.3100 file.4800 file.6200 file.7900 file.9300
file.1800 file.3200 file.4900 file.6300 file.8 file.9400
file.1900 file.3300 file.5 file.6400 file.80 file.9500
file.2 file.3400 file.50 file.6500 file.800 file.9600
file.20 file.3500 file.500 file.6600 file.8000 file.9700
file.200 file.3600 file.5000 file.6700 file.8100 file.9800
file.2000 file.3700 file.5100 file.6800 file.8200 file.9900
file.2100 file.3800 file.5200 file.6900 file.8300
file.2200 file.3900 file.5300 file.7 file.8400
```

<h2>Q3</h2>

次のテキストから、「-v」、「-f」、「awk」の数をそれぞれカウントしてください。gawk、nawkは避けてください（awkの数としてカウントしない）。できる人はgrepは1個で。さらにできる人は拡張正規表現を使わないでやってみましょう。


```bash
$ cat text1 
awk -v v="hoge" 'BEGIN{print v}'
echo 'BEGIN{print 1}' | gawk -f -
nawk 'BEGIN{print " BEGIN{print x}"}' | awk -v x=3 -f -
```

<h1>解答</h1>

```bash
###ベタな感じ（これでも全然問題ありません）###
$ grep -oE '(-[a-z]|[a-z]?awk)' text1 | grep -v '[ng]awk' | sort | uniq 
c- 2 -f
 2 -v
 2 awk
###最小手順（と思われる方法）###
$ grep -wEo "(-[a-z]|awk)" text1 | sort | uniq 
c- 2 -f
 2 -v
 2 awk
###拡張正規表現を使わない###
$ grep -wo -e "-[a-z]" -e "awk" text1 | sort | uniq 
c- 2 -f
 2 -v
 2 awk
```

<h2>Q4</h2>

/etc/の下（子、孫、・・・）のファイルのうち、シバンが「#!/bin/sh」のシェルスクリプトについて、中に「set -e」と記述のあるファイルとないファイルの数をそれぞれ数えてください。（コメント中のset -eも数えてOKです。）

<h1>解答</h1>

一例です。set -eと記述があるものが33、無いものが75となります。

```bash
$ sudo grep -l '#!/bin/sh' /etc/ -R | sudo xargs grep -c 'set -e' |
 sed 's/.*://' | awk '{if($1==0){print 0}else{print 1}}' | sort | uniq 
c-grep: /etc/alternatives/ghostscript-current/Resource/CIDFSubst/DroidSansFallback.ttf: No such file or directory
grep: /etc/blkid.tab: No such file or directory
 75 0
 33 1
```

<h2>Q5</h2>

日本語やギリシャ文字のある行を除去してください。

```bash
$ cat text2 
A pen is a pen?
日本語でおk
ΩΩπ<Ω< na nandatte!!
Randy W. Bass
env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
#危険シェル芸
```

<h1>解答</h1>

別解求む。

```bash
$ LANG=C grep "^[[:print:]]*$" text2
```


<h2>Q6</h2>

次のようにファイルa, b, cを作ります。

```bash
$ echo 1 2 3 4 > a
$ echo 2 3 4 5 > b
$ echo 1 4 5 > c
```

ファイルの中の数字を足して10になるファイルを挙げてください。

<h1>解答</h1>

```bash
###grepを使わなくてもいけますが・・・###
$ for i in a b c ; do [ 10 -eq $(numsum -r $i) ] && echo $i ; done
###grepでリストを作る###
$ grep "" * | tr ':' ' ' | 
awk '{for(i=2;i<=NF;i++){a+=$i};print $1,a;a=0}' | grep " 10$"
###Tukubaiを利用###
$ grep "" * | tr ':' ' ' | ysum num=1 | grep " 10$"
```

<h2>Q7</h2>

psコマンドを打って（オプションは任意）、そのpsコマンドの行、親プロセスの行、親の親のプロセスの行を表示してみてください。

<h1>解答</h1>

すごくいい加減な気がしないでもありませんが・・・

```bash
$ ps -eo ppid,pid,command > f ; grep "ps -eo" f | grep -v grep |
 awk '{print " "$1" ";print " "$2" "}' | grep -f - f |
 awk '{print " "$1" ";print " "$2" "}' | grep -f - f
 5696 5767 sshd: ueda@pts/6 
 5767 5768 -bash
 5768 8806 ps -eo ppid,pid,command
```

<h2>Q8</h2>

seqとfactorの出力の後ろにgrepだけをいくつかつなげて、「素数の一つ前の数で、かつ10以上の数」を列挙してください。

```bash
$ seq 10 1000 | factor | ...(grepだけ)
```

<h1>解答</h1>

```bash
$ seq 10 1000 | factor | grep -EB 1 '^[^ ]+ [^ ]+$' |
 grep -Eo '^[0-9]+[02468]:' | grep -Eo '^[0-9]+'
```


