---
Keywords: コマンド,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第25回もう4年もやってんのかシェル芸勉強会
<h2>イントロ</h2>

<a href="/?presenpress=%e7%ac%ac25%e5%9b%9e%e3%82%82%e3%81%864%e5%b9%b4%e3%82%82%e3%82%84%e3%81%a3%e3%81%a6%e3%82%93%e3%81%ae%e3%81%8b%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">こちら</a>
<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.24" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.25</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はUbuntu Linux 16.04で解答例を作りました。
<h2>Q1</h2>
www.usptomo.comのIPアドレスだけを出力するワンライナーを考えてみてください。
<h3>解答</h3>

```bash
$ dig www.usptomo.com | grep -A1 ANSWER 
| tail -n 1 | awk '{print $NF}'
157.7.203.188
$ ping -c1 www.usptomo.com | head -n 1 
| awk '{print $3}' | tr -d '()'
157.7.203.188
```

<h2>Q2</h2>
次のような出力を作ってください。（<a href="http://togetter.com/li/1041621" target="_blank">出典</a>）

```bash
ひらけ！ポンキッキ
らけ！ポンキッキひ
け！ポンキッキひら
！ポンキッキひらけ
ポンキッキひらけ！
ンキッキひらけ！ポ
キッキひらけ！ポン
ッキひらけ！ポンキ
キひらけ！ポンキッ
```

<h3>解答</h3>
ベタなものを載せておきます。変態的解答はウェブで。

```bash
$ a="ひらけ！ポンキッキ" ; for i in $(seq 2 $(wc -m <<< $a)) ; 
do echo $a ; a=$(sed 's/\\(.\\)\\(.*\\)/\\2\\1/g' <<< $a) ; done
```

<h2>Q3</h2>
rbashと打つとリダイレクトが使えなくなります。

この状況で、/etc/passwdからbashをログインシェルにしているユーザのレコードを抽出し、hoge等のファイルに出力してみましょう。様々な方法を考えてみましょう。bashと打ったりexitでもとのbashに戻るのは反則とします。
<h3>解答</h3>

```bash
$ grep bash$ /etc/passwd | tee hoge
$ grep bash$ /etc/passwd | awk '{print $0 > "huge"}'
$ grep bash$ /etc/passwd | dd of=hohe
```

<h2>Q4</h2>
以下のひらがなからワンライナーを始めて、濁点がつく字だけに濁点をつけてみてください。

```bash
$ echo すけふぇにんけん
```

<h3>解答</h3>

```bash
$ echo すけふぇにんけん | sed 's/./&゛/g' 
| nkf --katakana | nkf -Z4 
| nkf --hiragana | sed 's/゛//g'
ずげぶぇにんげん
```

<h2>Q5</h2>
1秒に一つ*が伸びていくアニメーションを作ってください。

[playlist type="video" ids="8740"]
<h3>解答</h3>

```bash
$ yes | awk 'BEGIN{a="*"}{print a;a=a"*";system("sleep 1")}' 
| xargs -I\@ echo -ne \@"\\r" 
```

<h2>Q6</h2>
日本語のメッセージから作った次の文字列を復元してください。

```bash
$ cat crypt 
b730a730eb30b8820a00
```

<h3>解答</h3>
0a00あたりがカギになります。

```bash
$ cat crypt | xxd -ps -r | iconv -f=ucs-2le -t=utf8
シェル芸
$ echo -ne $(sed 's/\\(..\\)\\(..\\)/\\\\U\\2\\1/g' < crypt)
シェル芸
```

<h2>Q7</h2>
本日（2016年10月29日）の範囲の毎秒のUNIX時刻で素数となるものを全て列挙してください。出力はUNIX時刻でなく、何時何分何秒か分かるようにしましょう。世界標準時で考えてください。
<h3>解答</h3>

```bash
$ ( date -ud '20161029' +%s ; date -ud '20161030' +%s ) | xargs seq 
| factor | awk 'NF==2{print "\@"$2}' | date -uf - 
```

<h2>Q8</h2>
次のようにサイン波を描いてください。

<a href="b466fc6a3025fb4e2d7d3b98eea47814.png"><img class="aligncenter size-large wp-image-8754" src="b466fc6a3025fb4e2d7d3b98eea47814-1024x871.png" alt="%e3%82%b9%e3%82%af%e3%83%aa%e3%83%bc%e3%83%b3%e3%82%b7%e3%83%a7%e3%83%83%e3%83%88-2016-10-27-21-04-17" width="660" height="561" /></a>
<h3>解答</h3>

```bash
$ seq 1 20 | awk '{a=sin($1/3) * 10 + 10;for(i=0;i<a;i++)printf "\@ ";
printf "* ";for(i=a;i<20;i++)printf "\@ ";print ""}' 
| rs -t 23 | tr \@ ' ' 
```

