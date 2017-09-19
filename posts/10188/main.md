---
Keywords: コマンド,CLI,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】jus共催 第30回危念シェル芸勉強会
<a href="https://blog.ueda.tech/?p=10134">解答はこちら</a>

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



<h2>Q2</h2>
次のHTMLファイルurl.htmlについて、リンクが相対パスになっているものについては頭に/files/をつけて、/から始まっているものとhttpやhttpsから始まっているものはそのままにしてください。できる人は変なところに改行があるものなどに対応できるように、なるべく一般解に近づけましょう。

```html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
 &lt;meta charset=&quot;utf-8&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
 &lt;ul&gt;
 &lt;li&gt;&lt;a href=&quot;./hoge.html&quot;&gt;ほげ&lt;/a&gt;&lt;/li&gt;
 &lt;li&gt;&lt;img src=&quot;ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ&lt;/a&gt;&lt;a href=&quot;huge.html&quot;&gt;ふげ&lt;/a&gt;&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;/root.jpg&quot;&gt;&lt;/a&gt;これはそのまま&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない&lt;/a&gt;&lt;/li&gt;
 &lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;
```

次が出力例です。

```html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
 &lt;meta charset=&quot;utf-8&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
 &lt;ul&gt;
 &lt;li&gt;&lt;a href=&quot;/files/hoge.html&quot;&gt;ほげ&lt;/a&gt;&lt;/li&gt;
 &lt;li&gt;&lt;img src=&quot;/files/ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ&lt;/a&gt;&lt;a href=&quot;/files/huge.html&quot;&gt;ふげ&lt;/a&gt;&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;/root.jpg&quot;&gt;&lt;/a&gt;これはそのまま&lt;/li&gt;
 &lt;li&gt;&lt;a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない&lt;/a&gt;&lt;/li&gt;
 &lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;
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

&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
 &lt;meta charset=&quot;utf-8&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;ul&gt;
&lt;li&gt;妬み&lt;/li&gt;
&lt;li&gt;嫉み&lt;/li&gt;
&lt;li&gt;僻み&lt;/li&gt;
&lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;
```

すぐできて退屈な人は、インターネット上のサーバでこのHTMLファイルを送信するサーバをワンライナーで立ててください。

<h2>Q4</h2>
&amp;&amp;や;でコマンドを繋いだワンライナーで、GitHubにリポジトリを作ってそこにテキストファイルを一つ置いてください。


<h2>Q5</h2>
次のファイルの1行目の複素数と2行目の複素数をかけ算してください。

```bash
$ cat complex 
1 + 4*i
3 - 2*i
```

<h2>Q6</h2>
フィボナッチ数列で、6765の4つ前の数を出力してください。

<h2>Q7</h2>
次の数字の列について、00, 01, 02,...,99の数字2つ並びのうち、含まれないものを抽出してください。できる人はループを使わないで抽出してください。

```bash
cat nums
1232154916829552629124634124821535923503018381369677458868876877570978993996890718096846698577281037379417474410221480004050608111920262721512985412925301
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

