---
Keywords: コマンド,CLI,Linux,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】jus共催 第30回危念シェル芸勉強会
<a href="https://blog.ueda.tech/?p=10188">問題のみのページはこちら</a><br />
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
Keywords:  嫌がらせ<br />
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
<h3>解答</h3><br />
grepの-mオプションを使うと一番最初にマッチした行を取り出せます。<br />
<br />
[bash]<br />
$ grep -m 1 '^Keywords:' posts/*/main.md |<br />
 sed 's;posts/;;' | sed 's;/main.md:; ;'<br />
[/bash]<br />
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
<h3>解答</h3><br />
いちおうこれで大丈夫だとは思うのですが、自分でもなんだかよくわかりません・・・。<br />
<br />
[bash]<br />
$ cat url.html | sed -r 's;(img src=&quot;|a href=&quot;);&amp;/files/;g' |<br />
 sed -r 's;(href=&quot;|src=&quot;)/files//;\\1/;' |<br />
 sed -r 's;(href=&quot;|src=&quot;)/files/(https://|http://);\\1\\2;g' |<br />
 sed 's;/./;/;g'<br />
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
[/bash]<br />
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
<h3>解答</h3><br />
ゴリゴリやってもあまり苦労はしないと思いますが、Pandocの紹介がてら問題を出しました。<br />
<br />
[bash]<br />
$ cat list | sed 's/\\* /&lt;li&gt;/' | sed 's;$;&lt;/li&gt;;' |<br />
 sed '1iContent-Type: text/html\\n\\n&lt;!DOCTYPE html&gt;&lt;html&gt;&lt;head&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;/head&gt;&lt;body&gt;&lt;ul&gt;' |<br />
 sed '$a&lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;' | sed 's/&gt;&lt;/&gt;\\n&lt;/g'<br />
### Pandocを使う方法 ###<br />
$ pandoc list -t html5 -s | sed '5,12d' | sed '1iContent-Type: text/html\\n'<br />
[/bash]<br />
<br />
ブラウザからの応答に反応するには、レスポンス行も追加します。（改行は\\r\\nの方がいいかもしれません。）<br />
<br />
[bash]<br />
$ pandoc list -t html5 -s | sed '5,12d' |<br />
 sed '1iHTTP/1.1 200 OK\\nContent-Type: text/html\\n' | nc -l 8080<br />
### 連続応答 ###<br />
$ while : ; do pandoc list -t html5 -s | sed '5,12d' |<br />
 sed '1iHTTP/1.1 200 OK\\nContent-Type: text/html\\n' | nc -l 8080 ; done<br />
[/bash]<br />
<br />
<h2>Q4</h2><br />
&amp;&amp;や;でコマンドを繋いだワンライナーで、GitHubにリポジトリを作ってそこにテキストファイルを一つ置いてください。<br />
<h3>解答</h3><br />
hubの紹介のための問題でした。<br />
<br />
[bash]<br />
$ mkdir hoge &amp;&amp; cd hoge &amp;&amp; git init &amp;&amp; echo aho &gt; aho.txt <br />
&amp;&amp; git add -A &amp;&amp; git commit -m &quot;aho&quot; <br />
&amp;&amp; hub create ryuichiueda/hoge &amp;&amp; git push origin master<br />
Initialized empty Git repository in /home/ueda/hoge/hoge/hoge/.git/<br />
[master (root-commit) 76206c8] aho<br />
 1 file changed, 1 insertion(+)<br />
 create mode 100644 aho.txt<br />
Updating origin<br />
created repository: ryuichiueda/hoge<br />
Counting objects: 3, done.<br />
Writing objects: 100% (3/3), 215 bytes | 0 bytes/s, done.<br />
Total 3 (delta 0), reused 0 (delta 0)<br />
To git\@github.com:ryuichiueda/hoge.git<br />
 * [new branch] master -&gt; master<br />
[/bash]<br />
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
<h3>解答</h3><br />
Perlを使ってみました。（Perlに慣れていればもっと前処理は簡単になると思います。）<br />
<br />
[bash]<br />
$ cat complex | sed 's/^/(/' | sed 's/$/)/' | sed '2,$i*' |<br />
 xargs | tr -d ' ' |<br />
 xargs -I\@ perl -e '{use Math::Complex;print(\@);print &quot;\\n&quot;}'<br />
11+10i<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
フィボナッチ数列で、6765の4つ前の数を出力してください。<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ echo a | awk 'BEGIN{a=1;b=1}{while(1){print a;c=b;b+=a;a=c}}' |<br />
 grep -m 1 -B4 6765 | head -n 1<br />
987<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
次の数字の列について、00, 01, 02,...,99の数字2つ並びのうち、含まれないものを抽出してください。できる人はループを使わないで抽出してください。<br />
<br />
[bash]<br />
cat nums<br />
1232154916829552629124634124821535923503018381369677458868876877570978993996890718096846698577281037379417474410221480004050608111920262721512985412925301<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ seq -w 0 99 | while read n ; do grep -q $n nums || echo $n ; done <br />
31<br />
33<br />
42<br />
43<br />
56<br />
61<br />
64<br />
65<br />
[/bash]<br />
<br />
whileやforを使わない場合はこんな感じで。<br />
<br />
[bash]<br />
$ cat nums | sed 's/.\\(.*\\)/\\1\\n&amp;/' | fold -b2 | grep .. | sort -u |<br />
 sort -m - &lt;(seq -w 00 99) | sort | uniq -u<br />
31<br />
33<br />
42<br />
43<br />
56<br />
61<br />
64<br />
65<br />
[/bash]<br />
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
<br />
<h3>解答</h3><br />
ブレース展開を使うとこんな感じです。<br />
<br />
[bash]<br />
$ cat alphabet |<br />
 awk '{a=$1;gsub(/-/,&quot;..&quot;,a);print &quot;echo&quot;,$1,&quot;{&quot;a&quot;}&quot;}' |<br />
 bash | awk '{print $1,NF}' | sort -k2,2n |<br />
 tail -n 1 | awk '{print $1}'<br />
e-q<br />
[/bash]<br />
<br />
あとは10進数のasciiコードに変換する方法を示します。<br />
<br />
[bash]<br />
$ cat alphabet | xxd -ps | fold -b2| tr a-f A-F |<br />
 sed '1iobase=10;ibase=16;' | bc | xargs -n 4 |<br />
 awk '{print $1-$3}' | tr -d - | awk '{print NR,$1}' |<br />
 sort -k2,2n | tail -n 1 | awk '{print $1}' |<br />
 xargs -I\@ sed -n \@p alphabet <br />
e-q<br />
$ cat alphabet | tr - ' ' |<br />
 perl -anle '{print abs(ord($F[0])-ord($F[1]))}' |<br />
 awk '{print NR,$1}' | sort -k2,2n | tail -n 1 |<br />
 awk '{print $1}' | xargs -I\@ sed -n \@p alphabet <br />
e-q<br />
[/bash]<br />

