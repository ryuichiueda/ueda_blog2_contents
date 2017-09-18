---
Keywords:コマンド,CLI,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】jus共催 第30回危念シェル芸勉強会
<a href="https://blog.ueda.tech/?p=10134">解答はこちら</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.30" target="_blank" rel="noopener">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.30</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>環境</h2><br />
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。<br />
<h2>イントロ</h2><br />
<br />
<a href="https://blog.ueda.tech/?presenpress=%E7%AC%AC30%E5%9B%9E%E5%8D%B1%E5%BF%B5%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8%E5%8B%89%E5%BC%B7%E4%BC%9A#/">スライド</a><br />
<br />
<h2>Q1</h2><br />
リポジトリの中に、次のようなディレクトリがあります。<br />
<br />
[bash]<br />
$ tree posts<br />
posts<br />
├── 20170806_check_of_webhook<br />
│   └── main.md<br />
├── 20170810_negi<br />
│   ├── green_negi.jpg<br />
│   ├── main.md<br />
│   ├── white_negi.jpg<br />
│   └── ねぎ.pdf<br />
├── 20170810_negistagram<br />
│   └── main.md<br />
├── 20170812_work<br />
├── 20170812_working<br />
│   └── main.md<br />
├── 20170814_layout<br />
│   └── main.md<br />
├── 20170818_bash<br />
│   └── main.md<br />
├── 20170820_bootstrap<br />
│   └── main.md<br />
├── 20170820_injection<br />
│   └── main.md<br />
└── template<br />
 └── main.md<br />
[/bash]<br />
<br />
この中の、各main.mdは次のようなヘッダ付きのマークダウンです。<br />
<br />
[bash]<br />
$ cat posts/20170818_bash/main.md <br />
---<br />
Keywords: 嫌がらせ<br />
Copyright: (C) 2017 Ryuichi Ueda<br />
---<br />
<br />

# 検索機能への嫌がらせ<br />
Keywords: ワッショイ<br />
Keywords: ワッショイ<br />
Keywords: ワッショイ<br />
[/bash]<br />
<br />
これらのファイルから、次のような出力を作ってください。なお、Keywordsの行は各ファイルで最初にある行しか抽出しないこととします。<br />
<br />
[bash]<br />
20170806_check_of_webhook Keywords: Webhook<br />
20170810_negi Keywords: ネギ<br />
20170810_negistagram Keywords: Twitter, Instagram, ネギ<br />
20170812_working Keywords: 働けども働けども, bashcms2<br />
20170814_layout Keywords: table, 雑<br />
20170818_bash Keywords: 嫌がらせ<br />
20170820_bootstrap Keywords: Bootstrap<br />
20170820_injection Keywords: injection<br />
template Keywords: <br />
[/bash]<br />
<br />
<br />
<br />
<h2>Q2</h2><br />
次のHTMLファイルurl.htmlについて、リンクが相対パスになっているものについては頭に/files/をつけて、/から始まっているものとhttpやhttpsから始まっているものはそのままにしてください。できる人は変なところに改行があるものなどに対応できるように、なるべく一般解に近づけましょう。<br />
<br />
[html]<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
&lt;head&gt;<br />
 &lt;meta charset=&quot;utf-8&quot;&gt;<br />
&lt;/head&gt;<br />
&lt;body&gt;<br />
 &lt;ul&gt;<br />
 &lt;li&gt;&lt;a href=&quot;./hoge.html&quot;&gt;ほげ&lt;/a&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;img src=&quot;ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ&lt;/a&gt;&lt;a href=&quot;huge.html&quot;&gt;ふげ&lt;/a&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;/root.jpg&quot;&gt;&lt;/a&gt;これはそのまま&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない&lt;/a&gt;&lt;/li&gt;<br />
 &lt;/ul&gt;<br />
&lt;/body&gt;<br />
&lt;/html&gt;<br />
[/html]<br />
<br />
次が出力例です。<br />
<br />
[html]<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
&lt;head&gt;<br />
 &lt;meta charset=&quot;utf-8&quot;&gt;<br />
&lt;/head&gt;<br />
&lt;body&gt;<br />
 &lt;ul&gt;<br />
 &lt;li&gt;&lt;a href=&quot;/files/hoge.html&quot;&gt;ほげ&lt;/a&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;img src=&quot;/files/ayasii.jpg&quot; alt=&quot;怪しい&quot; /&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;https://blog.ueda.tech/&quot;&gt;クソブログ&lt;/a&gt;&lt;a href=&quot;/files/huge.html&quot;&gt;ふげ&lt;/a&gt;&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;/root.jpg&quot;&gt;&lt;/a&gt;これはそのまま&lt;/li&gt;<br />
 &lt;li&gt;&lt;a href=&quot;http://www.usptomo.com/&quot;&gt;更新してない&lt;/a&gt;&lt;/li&gt;<br />
 &lt;/ul&gt;<br />
&lt;/body&gt;<br />
&lt;/html&gt;<br />
[/html]<br />
<br />
<h2>Q3</h2><br />
次のファイルについて、<br />
<br />
[bash]<br />
$ cat list<br />
* 妬み<br />
* 嫉み<br />
* 僻み<br />
[/bash]<br />
<br />
次のようにHTMLにして、頭にHTTPヘッダをつけてください。インデントは不要ですがタグは1行1個でお願いします。<br />
<br />
[html]<br />
Content-Type: text/html<br />
<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
&lt;head&gt;<br />
 &lt;meta charset=&quot;utf-8&quot;&gt;<br />
&lt;/head&gt;<br />
&lt;body&gt;<br />
&lt;ul&gt;<br />
&lt;li&gt;妬み&lt;/li&gt;<br />
&lt;li&gt;嫉み&lt;/li&gt;<br />
&lt;li&gt;僻み&lt;/li&gt;<br />
&lt;/ul&gt;<br />
&lt;/body&gt;<br />
&lt;/html&gt;<br />
[/html]<br />
<br />
すぐできて退屈な人は、インターネット上のサーバでこのHTMLファイルを送信するサーバをワンライナーで立ててください。<br />
<br />
<h2>Q4</h2><br />
&amp;&amp;や;でコマンドを繋いだワンライナーで、GitHubにリポジトリを作ってそこにテキストファイルを一つ置いてください。<br />
<br />
<br />
<h2>Q5</h2><br />
次のファイルの1行目の複素数と2行目の複素数をかけ算してください。<br />
<br />
[bash]<br />
$ cat complex <br />
1 + 4*i<br />
3 - 2*i<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
フィボナッチ数列で、6765の4つ前の数を出力してください。<br />
<br />
<h2>Q7</h2><br />
次の数字の列について、00, 01, 02,...,99の数字2つ並びのうち、含まれないものを抽出してください。できる人はループを使わないで抽出してください。<br />
<br />
[bash]<br />
cat nums<br />
1232154916829552629124634124821535923503018381369677458868876877570978993996890718096846698577281037379417474410221480004050608111920262721512985412925301<br />
[/bash]<br />
<br />
<br />
<h2>Q8</h2><br />
次のアルファベットの区間のうち、間に含まれるアルファベットが一番多いものはどれでしょうか。<br />
<br />
[bash]<br />
$ cat alphabet <br />
a-g<br />
e-q<br />
z-v<br />
r-y<br />
[/bash]<br />

