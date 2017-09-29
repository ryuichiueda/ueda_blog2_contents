---
Keywords: コマンド,CLI,Linux,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】jus共催 第30回危念シェル芸勉強会
<a href="https://blog.ueda.tech/?p=10188">問題のみのページはこちら</a>

<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.30" target="_blank" rel="noopener">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.30</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。
<h2>イントロ</h2>

<a href="https://blog.ueda.tech/?presenpress=%E7%AC%AC30%E5%9B%9E%E5%8D%B1%E5%BF%B5%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8%E5%8B%89%E5%BC%B7%E4%BC%9A#/">スライド</a>

<h2>Q1</h2>
リポジトリの中に、次のようなディレクトリがあります。

```bash
$ tree posts
posts
├── 20170806_check_of_webhook
│   └── main.md
├── 20170810_negi
│   ├── green_negi.jpg
│   ├── main.md
│   ├── white_negi.jpg
│   └── ねぎ.pdf
├── 20170810_negistagram
│   └── main.md
├── 20170812_work
├── 20170812_working
│   └── main.md
├── 20170814_layout
│   └── main.md
├── 20170818_bash
│   └── main.md
├── 20170820_bootstrap
│   └── main.md
├── 20170820_injection
│   └── main.md
└── template
 └── main.md
```

この中の、各main.mdは次のようなヘッダ付きのマークダウンです。

```bash
$ cat posts/20170818_bash/main.md 
---
Keywords:  嫌がらせ
Copyright: (C) 2017 Ryuichi Ueda
---


# 検索機能への嫌がらせ
Keywords: ワッショイ
Keywords: ワッショイ
Keywords: ワッショイ
```

これらのファイルから、次のような出力を作ってください。なお、Keywordsの行は各ファイルで最初にある行しか抽出しないこととします。

```bash
20170806_check_of_webhook Keywords: Webhook
20170810_negi Keywords: ネギ
20170810_negistagram Keywords: Twitter, Instagram, ネギ
20170812_working Keywords: 働けども働けども, bashcms2
20170814_layout Keywords: table, 雑
20170818_bash Keywords: 嫌がらせ
20170820_bootstrap Keywords: Bootstrap
20170820_injection Keywords: injection
template Keywords: 
```

<h3>解答</h3>
grepの-mオプションを使うと一番最初にマッチした行を取り出せます。

```bash
$ grep -m 1 '^Keywords:' posts/*/main.md |
 sed 's;posts/;;' | sed 's;/main.md:; ;'
```

<h2>Q2</h2>
次のHTMLファイルurl.htmlについて、リンクが相対パスになっているものについては頭に/files/をつけて、/から始まっているものとhttpやhttpsから始まっているものはそのままにしてください。できる人は変なところに改行があるものなどに対応できるように、なるべく一般解に近づけましょう。

```html
<!DOCTYPE html&gt;
<html&gt;
<head&gt;
 <meta charset=&quot;utf-8&quot;&gt;
</head&gt;
<body&gt;
 <ul&gt;
 <li&gt;<a href=&quot;./hoge.html&quot;&gt;ほげ</a&gt;</li&gt;
 <li&gt;<img src=&quot;ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;</li&gt;
 <li&gt;<a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ</a&gt;<a href=&quot;huge.html&quot;&gt;ふげ</a&gt;</li&gt;
 <li&gt;<a href=&quot;/root.jpg&quot;&gt;</a&gt;これはそのまま</li&gt;
 <li&gt;<a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない</a&gt;</li&gt;
 </ul&gt;
</body&gt;
</html&gt;
```

次が出力例です。

```html
<!DOCTYPE html&gt;
<html&gt;
<head&gt;
 <meta charset=&quot;utf-8&quot;&gt;
</head&gt;
<body&gt;
 <ul&gt;
 <li&gt;<a href=&quot;/files/hoge.html&quot;&gt;ほげ</a&gt;</li&gt;
 <li&gt;<img src=&quot;/files/ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;</li&gt;
 <li&gt;<a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ</a&gt;<a href=&quot;/files/huge.html&quot;&gt;ふげ</a&gt;</li&gt;
 <li&gt;<a href=&quot;/root.jpg&quot;&gt;</a&gt;これはそのまま</li&gt;
 <li&gt;<a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない</a&gt;</li&gt;
 </ul&gt;
</body&gt;
</html&gt;
```

<h3>解答</h3>
いちおうこれで大丈夫だとは思うのですが、自分でもなんだかよくわかりません・・・。

```bash
$ cat url.html | sed -r 's;(img src=&quot;|a href=&quot;);&amp;/files/;g' |
 sed -r 's;(href=&quot;|src=&quot;)/files//;\\1/;' |
 sed -r 's;(href=&quot;|src=&quot;)/files/(https://|http://);\\1\\2;g' |
 sed 's;/./;/;g'
<!DOCTYPE html&gt;
<html&gt;
<head&gt;
 <meta charset=&quot;utf-8&quot;&gt;
</head&gt;
<body&gt;
 <ul&gt;
 <li&gt;<a href=&quot;/files/hoge.html&quot;&gt;ほげ</a&gt;</li&gt;
 <li&gt;<img src=&quot;/files/ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;</li&gt;
 <li&gt;<a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ</a&gt;<a href=&quot;/files/huge.html&quot;&gt;ふげ</a&gt;</li&gt;
 <li&gt;<a href=&quot;/root.jpg&quot;&gt;</a&gt;これはそのまま</li&gt;
 <li&gt;<a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない</a&gt;</li&gt;
 </ul&gt;
</body&gt;
</html&gt;
```

<h2>Q3</h2>
次のファイルについて、

```bash
$ cat list
* 妬み
* 嫉み
* 僻み
```

次のようにHTMLにして、頭にHTTPヘッダをつけてください。インデントは不要ですがタグは1行1個でお願いします。

```html
Content-Type: text/html

<!DOCTYPE html&gt;
<html&gt;
<head&gt;
 <meta charset=&quot;utf-8&quot;&gt;
</head&gt;
<body&gt;
<ul&gt;
<li&gt;妬み</li&gt;
<li&gt;嫉み</li&gt;
<li&gt;僻み</li&gt;
</ul&gt;
</body&gt;
</html&gt;
```

すぐできて退屈な人は、インターネット上のサーバでこのHTMLファイルを送信するサーバをワンライナーで立ててください。
<h3>解答</h3>
ゴリゴリやってもあまり苦労はしないと思いますが、Pandocの紹介がてら問題を出しました。

```bash
$ cat list | sed 's/\\* /<li&gt;/' | sed 's;$;</li&gt;;' |
 sed '1iContent-Type: text/html\\n\\n<!DOCTYPE html&gt;<html&gt;<head&gt;<meta charset=&quot;utf-8&quot;&gt;</head&gt;<body&gt;<ul&gt;' |
 sed '$a</ul&gt;</body&gt;</html&gt;' | sed 's/&gt;</&gt;\\n</g'
### Pandocを使う方法 ###
$ pandoc list -t html5 -s | sed '5,12d' | sed '1iContent-Type: text/html\\n'
```

ブラウザからの応答に反応するには、レスポンス行も追加します。（改行は\\r\\nの方がいいかもしれません。）

```bash
$ pandoc list -t html5 -s | sed '5,12d' |
 sed '1iHTTP/1.1 200 OK\\nContent-Type: text/html\\n' | nc -l 8080
### 連続応答 ###
$ while : ; do pandoc list -t html5 -s | sed '5,12d' |
 sed '1iHTTP/1.1 200 OK\\nContent-Type: text/html\\n' | nc -l 8080 ; done
```

<h2>Q4</h2>
&amp;&amp;や;でコマンドを繋いだワンライナーで、GitHubにリポジトリを作ってそこにテキストファイルを一つ置いてください。
<h3>解答</h3>
hubの紹介のための問題でした。

```bash
$ mkdir hoge &amp;&amp; cd hoge &amp;&amp; git init &amp;&amp; echo aho &gt; aho.txt 
&amp;&amp; git add -A &amp;&amp; git commit -m &quot;aho&quot; 
&amp;&amp; hub create ryuichiueda/hoge &amp;&amp; git push origin master
Initialized empty Git repository in /home/ueda/hoge/hoge/hoge/.git/
[master (root-commit) 76206c8] aho
 1 file changed, 1 insertion(+)
 create mode 100644 aho.txt
Updating origin
created repository: ryuichiueda/hoge
Counting objects: 3, done.
Writing objects: 100% (3/3), 215 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git\@github.com:ryuichiueda/hoge.git
 * [new branch] master -&gt; master
```

<h2>Q5</h2>
次のファイルの1行目の複素数と2行目の複素数をかけ算してください。

```bash
$ cat complex 
1 + 4*i
3 - 2*i
```

<h3>解答</h3>
Perlを使ってみました。（Perlに慣れていればもっと前処理は簡単になると思います。）

```bash
$ cat complex | sed 's/^/(/' | sed 's/$/)/' | sed '2,$i*' |
 xargs | tr -d ' ' |
 xargs -I\@ perl -e '{use Math::Complex;print(\@);print &quot;\\n&quot;}'
11+10i
```

<h2>Q6</h2>
フィボナッチ数列で、6765の4つ前の数を出力してください。
<h3>解答</h3>

```bash
$ echo a | awk 'BEGIN{a=1;b=1}{while(1){print a;c=b;b+=a;a=c}}' |
 grep -m 1 -B4 6765 | head -n 1
987
```

<h2>Q7</h2>
次の数字の列について、00, 01, 02,...,99の数字2つ並びのうち、含まれないものを抽出してください。できる人はループを使わないで抽出してください。

```bash
cat nums
1232154916829552629124634124821535923503018381369677458868876877570978993996890718096846698577281037379417474410221480004050608111920262721512985412925301
```

<h3>解答</h3>

```bash
$ seq -w 0 99 | while read n ; do grep -q $n nums || echo $n ; done 
31
33
42
43
56
61
64
65
```

whileやforを使わない場合はこんな感じで。

```bash
$ cat nums | sed 's/.\\(.*\\)/\\1\\n&amp;/' | fold -b2 | grep .. | sort -u |
 sort -m - <(seq -w 00 99) | sort | uniq -u
31
33
42
43
56
61
64
65
```

<h2>Q8</h2>
次のアルファベットの区間のうち、間に含まれるアルファベットが一番多いものはどれでしょうか。

```bash
$ cat alphabet 
a-g
e-q
z-v
r-y
```

<h3>解答</h3>
ブレース展開を使うとこんな感じです。

```bash
$ cat alphabet |
 awk '{a=$1;gsub(/-/,&quot;..&quot;,a);print &quot;echo&quot;,$1,&quot;{&quot;a&quot;}&quot;}' |
 bash | awk '{print $1,NF}' | sort -k2,2n |
 tail -n 1 | awk '{print $1}'
e-q
```

あとは10進数のasciiコードに変換する方法を示します。

```bash
$ cat alphabet | xxd -ps | fold -b2| tr a-f A-F |
 sed '1iobase=10;ibase=16;' | bc | xargs -n 4 |
 awk '{print $1-$3}' | tr -d - | awk '{print NR,$1}' |
 sort -k2,2n | tail -n 1 | awk '{print $1}' |
 xargs -I\@ sed -n \@p alphabet 
e-q
$ cat alphabet | tr - ' ' |
 perl -anle '{print abs(ord($F[0])-ord($F[1]))}' |
 awk '{print NR,$1}' | sort -k2,2n | tail -n 1 |
 awk '{print $1}' | xargs -I\@ sed -n \@p alphabet 
e-q
```

