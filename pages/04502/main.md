---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2014年4月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>4. 開眼シェルスクリプト 第4回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>4.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　書いている筆者本人が超地味だと公言する開眼シェルスクリプトも、
今回で第四回です。今回は（この連載にしては）派手です。ブラウザで絵を描きます。</p>
<div class="section" id="id3">
<h3>4.1.1. 禁欲的になれとは言ってません<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　端末で古いコマンドを使い、
テキストばかりいじっているのでそう思われてもしょうがないのですが、
別に昔に帰れとか、GUI見るなとか、そういうことをこの連載で言いたいわけではないのです。
むしろ、逆です。ここ数年は、データの保存や表現形式は、テキスト
（というよりも、より人間が読みやすい）データに向かっているようなので、
テキストを操作できるということは、より普遍的なスキルになりつつあるようです。</p>
<p>　○○が廃れたなどと具体例を出して言うと角が立ちますので、一つ例を出します。
筆者は職業柄、画面のスクリーンショットを撮ることが多いのですが、
スクリーンショットはバイナリ形式のpng形式で保存しています。
16進数でファイルの先頭を出すと、リスト1のように見えます。
バイナリなので、catすると悲惨なことになります。</p>
<p>↓リスト1: png画像をodで見る。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>od -tx 201204_1.png | head -n 2
0000000 474e5089 0a1a0a0d 0d000000 52444849
0000020 df000000 ad000000 00000608 aa133000
</pre></div>
</td></tr></table></div>
<p>　別にcatできなくても画像なので全く構わないわけですが、
それでも筆者は、10年後20年後には、
ビットマップ画像（脚注：ベクトル画像でなく、あくまでビットマップ画像。）
のフォーマットの最終型が次のようなテキストファイルを圧縮したものになると考えています。</p>
<p>↓リスト2: 近未来ビットマップ（予想）</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>y x r g b
0 0 128 128 128
0 1 255 121 121
0 2 32 128 128
...
</pre></div>
</td></tr></table></div>
<p>この形式の問題はサイズがバカでかく、見た目もバカっぽいということですが、</p>
<ul class="simple">
<li>ハードの進化でサイズの問題が些細なことになったらどうなる？</li>
<li>画像の一部だけ切り取るのはpng形式とどっちが楽か？</li>
<li>言語付属のライブラリを作ってメンテナンスする手間はどっちが楽か？</li>
<li>形式を拡張しなければならないとき、png形式と比べてどっちが自然に拡張できるか？</li>
</ul>
<p>などといろいろ利点、欠点を考えると、
特に嫌悪や嘲笑の対象になるような形式でもないでしょう。
実際、PDP-7上でUNIXが取った戦略は後者だったのです。</p>
<p>　今回は、次の有名な格言を。</p>
<ul>
<li><dl class="first docutils">
<dt>Keep it simple, stupid.</dt>
<dd><p class="first last">（KISSの原則、ケリー・ジョンソン）</p>
</dd>
</dl>
</li>
</ul>
</div>
</div>
<div class="section" id="html">
<h2>4.2. 今回のお題：HTMLで表とグラフを描く<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回のお題は、HTMLファイルをブラウザで見ることになりますが、
次の方法のいずれかで見てください。</p>
<ul class="simple">
<li>httpサーバを通してHTMLファイルを見る。</li>
<li>手元のデスクトップ機のUNIX環境でHTMLファイルを作り、手元のブラウザで見る。</li>
</ul>
<p>後者の場合は、httpサーバは不要です。
今回は後者の場合を想定して話を進めて行きます。
今回使用する環境も、リモートのサーバではなく、
デスクトップ機です。諸元は以下のようになってます。</p>
<ul class="simple">
<li>マシン：ThinkPad SL510</li>
<li>CPU, OS等：リスト3参照</li>
</ul>
<p>↓リスト3: CPU, OS等の情報</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>cat /proc/cpuinfo | grep <span class="s2">&quot;model name&quot;</span>
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz
<span class="c">#↑補足: CPUはデュアルコアのもの1個</span>
ueda\@uedaubuntu:~<span class="nv">$ </span>uname -a
Linux uedaubuntu 3.0.0-14-generic <span class="c">#23-Ubuntu SMP Mon Nov 21 20:34:47 UTC 2011 i686 i686 i386 GNU/Linux</span>
ueda\@uedaubuntu:~<span class="nv">$ </span>cat /etc/lsb-release | grep DESCRIPTION
<span class="nv">DISTRIB_DESCRIPTION</span><span class="o">=</span><span class="s2">&quot;Ubuntu 11.10&quot;</span>
ueda\@uedaubuntu:~<span class="nv">$ </span>firefox -v
Mozilla Firefox 9.0.1
ueda\@uedaubuntu:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span>
ja_JP.UTF-8
</pre></div>
</td></tr></table></div>
<div class="section" id="html-html5">
<h3>4.2.1. HTMLのおさらい（あるいは初めてのHTML5）<a class="headerlink" href="#html-html5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず、HTMLのおさらいをします。
HTML は、テキストのどこがタイトルでどこが本文で・・・
と印をつけていく方法の一種で、単なるテキストファイルです。
それ以上のものでもそれ以下のものでもありません。
それを踏まえて、リスト4のHTMLファイルを見てみましょう。HTML5で書いています。
HTML5は、従来のHTMLの余計なものが省かれて簡素化されたので、
以前のHTMLよりは理解しやすいと思います。説明する方も簡単で助かります。</p>
<p>↓リスト4: HTMLのおさらい</p>
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="nt">&lt;html&gt;</span>
 <span class="nt">&lt;head&gt;</span>
 <span class="nt">&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;utf-8&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;title&gt;</span>htmlの書き方<span class="nt">&lt;/title&gt;</span>
 <span class="nt">&lt;/head&gt;</span>
 <span class="nt">&lt;body&gt;</span>
 あいうえお
 <span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/html&gt;</span>
</pre></div>
</td></tr></table></div>
<p>　リスト4の1行目は、このファイルがhtmlであるということを言っています。
シバン（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> ）に似ています。
それ以降は、 <tt class="docutils literal"><span class="pre">&lt;html&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/html&gt;</span></tt> の間に「要素」を詰め込んでいきます。
要素というのは、</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">&lt;hoge&gt;</span></tt> から <tt class="docutils literal"><span class="pre">&lt;/hoge&gt;</span></tt> までの塊</li>
<li>あるいは <tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">...</span> <span class="pre">/&gt;</span></tt></li>
</ul>
<p>のことで、HTMLは、要素の下に要素がぶら下がって、
その下に・・・と木構造になります。
リスト1の場合は、一番外側のhtmlの下にheadとbodyがぶら下がって、
headの下にはさらにmetaとtitleがぶら下がっています。
<tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">...</span> <span class="pre">/&gt;</span></tt> の形式をとるときには <tt class="docutils literal"><span class="pre">/</span></tt> は不要なのですが、
筆者は <tt class="docutils literal"><span class="pre">/</span></tt> がないと閉じた感じがしないので、
かならず入れるようにしています。</p>
<p>　要素には、「内容」と「属性」というものがあります。
「内容」は <tt class="docutils literal"><span class="pre">&lt;hoge&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/hoge&gt;</span></tt> に挟まれた部分、
「属性」は、 <tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">a=&quot;b&quot;</span> <span class="pre">c=&quot;d&quot;</span> <span class="pre">...</span> <span class="pre">&gt;</span></tt> のように <tt class="docutils literal"><span class="pre">名前=&quot;値&quot;</span></tt>
を並べて書いたものです。
「内容」はその名の通り、要素が持っている情報本体で、
属性は、要素に対する味付けと考えてください。</p>
<p>　HTML5なので、HTML5に対応しているブラウザで見てみましょう。
上のHTMLをhoge.htmlと名前をつけてどこかに保存します。
ウェブサーバを立ち上げなくてもファイルをダブルクリックすれば見られるはずです。
環境によっては、次のように端末からfirefoxを立ち上げることもできます。
（くれぐれもリモートのマシンにssh接続している場合はやらないでください。）</p>
<div class="highlight-bash"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>firefox hoge.html
</pre></div>
</div>
<div class="figure">
<img alt="_images/201204_1.png" src="201204_1.png" />
<p class="caption">図1：リスト1のHTMLをfirefoxで見る</p>
</div>
<p>見ることができましたでしょうか。</p>
</div>
<div class="section" id="id4">
<h3>4.2.2. HTMLを出力するシェルスクリプト<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、HTMLを出力するシェルスクリプトを作ってみましょう。
CGIスクリプトにすることもできるのですが、それは後日ということで、
とにかくHTMLファイルを作るシェルスクリプトを作ります。</p>
<p>　まずは、リスト5のようなシェルスクリプトから始めます。</p>
<p>↓リスト5: HTMLのおさらい</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/GIHYO<span class="nv">$ </span>cat html.sh
<span class="c">#!/bin/bash</span>

cat <span class="s">&lt;&lt; EOF &gt; ./hoge.html</span>
<span class="s">&lt;!DOCTYPE html&gt;</span>
<span class="s">&lt;html&gt;</span>
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;UTF-8&quot; /&gt;&lt;/head&gt;</span>
<span class="s"> &lt;body&gt;</span>
<span class="s"> $(date)</span>
<span class="s"> &lt;/body&gt;</span>
<span class="s">&lt;/html&gt;</span>
<span class="s">EOF</span>

firefox ./hoge.html
</pre></div>
</td></tr></table></div>
<p>リスト5で大事なのは、4～12行目の部分です。
この部分は「ヒアドキュメント」と呼ばれ、
<tt class="docutils literal"><span class="pre">command</span> <span class="pre">&lt;&lt;</span> <span class="pre">EOF</span></tt> と <tt class="docutils literal"><span class="pre">EOF</span></tt> に挟まれたテキストがそのまま
<tt class="docutils literal"><span class="pre">command</span></tt> の標準入力に入力されます。
EOFは、別の文字列でも構いません。
もしヒアドキュメントの途中でEOFと出てくる可能性があれば、
別の文字列にした方がよいでしょう。
この例では、./hoge.htmlに5～11行目の中身が溜まります。
catで見てみてください。</p>
<p>　もう一つ大事なのは9行目で、 <tt class="docutils literal"><span class="pre">$(</span> <span class="pre">)</span></tt> でコマンドを挟むと、
コマンドの出力がヒアドキュメント中に埋め込まれます。
この例では、dateコマンドの結果がbody要素の内容になります。
<tt class="docutils literal"><span class="pre">$(</span> <span class="pre">)</span></tt> の中にパイプでコマンドをずらずら連ねるとヒアドキュメント内に
HTMLとコードが混ざって汚くなるので、
以下ではヒアドキュメント内ではcatだけを使います。</p>
<p>　このスクリプトを実行すると、firefoxが立ち上がり、
図2のようにスクリプトを実行した時刻がブラウザの画面に表示されます。</p>
<div class="figure">
<img alt="_images/201204_2.png" src="201204_2.png" />
<p class="caption">図2: リスト5の実行結果</p>
</div>
</div>
<div class="section" id="id5">
<h3>4.2.3. 表を表示<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、何か統計情報を表にしてみましょう。
表ならば端末で見れば十分なのですが、いくつも表を並べて一度に見たり、
比較したりするにはブラウザはうってつけの道具です。
表にするのは趣味丸出しのリスト6のデータです。</p>
<p>↓リスト6: 通算本塁打数</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/WEB/GIHYO<span class="nv">$ </span>head -n 5 HOMER
順位 選手 本塁打 FROM TO 試合 打数
1 王　貞治 868 1959 1980 2831 9250
2 野村　克也 657 1954 1980 3017 10472
3 門田　博光 567 1970 1992 2571 8868
4 山本　浩二 536 1969 1986 2284 8052
</pre></div>
</td></tr></table></div>
<p>　まず、このデータをそのまま表にしてみましょう。
HTMLでは表（テーブル）はリスト7のように書きます。
<tt class="docutils literal"><span class="pre">&lt;tr&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/tr&gt;</span></tt> で挟まれた部分が1行に相当、
<tt class="docutils literal"><span class="pre">&lt;td&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/td&gt;</span></tt> で挟まれた部分がテーブルの一区画（セル）に相当します。</p>
<p>↓リスト7: HTMLのテーブル</p>
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nt">&lt;table&gt;</span>
 <span class="nt">&lt;tr&gt;</span>
 <span class="nt">&lt;td&gt;</span>1行1列<span class="nt">&lt;/td&gt;</span>
 <span class="nt">&lt;td&gt;</span>1行2列<span class="nt">&lt;/td&gt;</span>
 <span class="nt">&lt;/tr&gt;</span>
 <span class="nt">&lt;tr&gt;</span>
 <span class="nt">&lt;td&gt;</span>2行1列<span class="nt">&lt;/td&gt;</span>
 <span class="nt">&lt;td&gt;</span>2行2列<span class="nt">&lt;/td&gt;</span>
 <span class="nt">&lt;/tr&gt;</span>
<span class="nt">&lt;/table&gt;</span>
</pre></div>
</td></tr></table></div>
<p>これをawkで作ってみましょう。リスト8のようになります。
各フィールドを td で囲んで外側を tr で包めばよいということになります。
ただまあ、数字も名前も全部左揃えになっており、
表現力に限界があります。
なんとかしようとすると、とたんにawkの部分が膨れてしまうでしょう。
これについては、グラフのところで解決します。</p>
<p>　ちなみに、9行目のteeコマンドは標準入力をファイルと標準出力に二股分岐するコマンドです。
パイプの間に挟んでデバッグによく使います。</p>
<p>↓リスト8: 表の出力</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

awk <span class="s1">&#39;{ print &quot;&lt;tr&gt;&quot;;</span>
<span class="s1"> for(i=1;i&lt;=NF;i++){print &quot;&lt;td&gt;&quot;$i&quot;&lt;/td&gt;&quot;};</span>
<span class="s1"> print &quot;&lt;/tr&gt;&quot; }&#39;</span> ./HOMER &gt; <span class="nv">$tmp</span>-table

tee <span class="nv">$tmp</span>-html <span class="s">&lt;&lt; EOF</span>
<span class="s">&lt;!DOCTYPE html&gt;</span>
<span class="s">&lt;html&gt;</span>
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;/head&gt;</span>
<span class="s"> &lt;body&gt;</span>
<span class="s"> &lt;h1 style=&quot;font-size:18px&quot;&gt;通算本塁打&lt;/h1&gt;</span>
<span class="s"> &lt;table border=&quot;1&quot; cellspacing=&quot;0&quot;&gt;</span>
<span class="s">$(cat $tmp-table)</span>
<span class="s"> &lt;/table&gt;</span>
<span class="s"> &lt;/body&gt;</span>
<span class="s">&lt;/html&gt;</span>
<span class="s">EOF</span>

firefox <span class="nv">$tmp</span>-html
rm -f <span class="nv">$tmp</span>-*
</pre></div>
</td></tr></table></div>
<div class="figure">
<img alt="_images/201204_3.png" src="201204_3.png" />
<p class="caption">図3：表の出力</p>
</div>
<p>　次のグラフ描画の際に使うので、cssについて簡単に説明します。
リスト8のh1の属性： style=&#8221;font-size:18px&#8221; は、
h1の内容がブラウザに描かれるときのフォントの大きさを指定しています。
<tt class="docutils literal"><span class="pre">font-size:18px</span></tt> の部分はcssと呼ばれるもので、
<tt class="docutils literal"><span class="pre">属性1:値1;属性2:値2;...</span></tt> というように並べていくと、
ブラウザへの出力方法を細かく指定できます。
どんな属性があるかは、ウェブ上に様々な情報があるのでそちらに譲ります。</p>
</div>
<div class="section" id="id6">
<h3>4.2.4. グラフを描く<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、次にリスト8の本塁打数をグラフにしてみましょう。
絵を描くわけですが、ここではSVG（scalable vector graphics）
というものをHTMLに埋め込んで使います。
まずは理屈抜きで、HTMLの例をリスト9に、ブラウザで見たものを図4に示します。</p>
<p>↓リスト9: svgで描画するHTML</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/GIHYO<span class="nv">$ </span>cat svg.html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;meta <span class="nv">charset</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span> /&gt;&lt;/head&gt;
&lt;!--注意：インデントは正しく！--&gt;
&lt;body&gt;
&lt;svg&gt;
 &lt;text <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;10&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;36&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;font-size:16px&quot;</span>&gt;USP&lt;/text&gt;
 &lt;rect <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;50&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;20&quot;</span> <span class="nv">width</span><span class="o">=</span><span class="s2">&quot;60&quot;</span> <span class="nv">height</span><span class="o">=</span><span class="s2">&quot;20&quot;</span>
 <span class="nv">fill</span><span class="o">=</span><span class="s2">&quot;white&quot;</span> <span class="nv">stroke</span><span class="o">=</span><span class="s2">&quot;black&quot;</span> /&gt;
 &lt;text <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;110&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;36&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;text-anchor:end&quot;</span>&gt;00&lt;/text&gt;
&lt;/svg&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre></div>
</td></tr></table></div>
<div class="figure">
<img alt="_images/201204_4.png" src="201204_4.png" />
<p class="caption">図4：表の出力</p>
</div>
<p>　 <tt class="docutils literal"><span class="pre">&lt;svg&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/svg&gt;</span></tt> の間に、rectやらtextやらがいますが、
要は図形一つ一つを指定していくとブラウザに
直接図形を描き出してくれるということです。
こんな便利な機能を使わない手はありません。
ただ、図形の部分のHTMLをawkで出力しようとすると
ややこしいコードになってしまうという問題があります。</p>
<p>　ここでは、mojihameという便利コマンドを使うことにします。
おそらく聞いたことが無いコマンドだと思いますが、
USP研究所のコマンドの一部がスクリプト言語で公開されているので、
ネットからダウンロードできます。</p>
<ul class="simple">
<li><a class="reference external" href="http://uec.usp-lab.com">http://uec.usp-lab.com</a></li>
</ul>
<p>からたどっていくとOpen usp tukubai
という名前のコマンドセットがダウンロードできるので、
その中のmojihameというコマンドを使います。
設定方法はサイトで確認できますが、
単なるpythonのスクリプトなので、スクリプトをダウンロードして
<tt class="docutils literal"><span class="pre">python</span> <span class="pre">mojihame</span></tt> と打てば実行できます。</p>
<p>　mojihameはリスト10のように使います。
<tt class="docutils literal"><span class="pre">temp</span></tt> ファイルの%1、%2、・・・というのは、
ここをデータファイルの第1、第2フィールドで置き換えるという意味で、
3行目、5行目の「AAA」はこの間を
データファイルのレコードの数だけ繰り返し出力しろという意味のマークです。
mojihameで <tt class="docutils literal"><span class="pre">-lAAA</span></tt> とマークをオプションで指定して、
tempとdataを入力すると、レコードがテンプレートに嵌って出力されます。</p>
<p>↓リスト10: mojihameの使い方</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>cat temp
長者番付（秘）
AAA
%1位 %2さん 納税額%3円
AAA
ueda\@uedaubuntu:~<span class="nv">$ </span>cat data
1 松浦 12
2 濱田 8
3 上田 -5
4 法林 -110
ueda\@uedaubuntu:~<span class="nv">$ </span>mojihame -lAAA temp data
長者番付（秘）
1位 松浦さん 納税額12円
2位 濱田さん 納税額8円
3位 上田さん 納税額-5円
4位 法林さん 納税額-110円
</pre></div>
</td></tr></table></div>
<p>　では、mojihame+svgで本塁打数を横向きの棒グラフで書いてみます。
図4のUSPのところに選手名、00のところに本塁打数を書きます。
また、本塁打数に比例させて四角の幅を変えます。</p>
<p>　やることは、HTMLでmojihame用のテンプレートを書くことと、
mojihameに食わせるデータを準備することです。
リスト11に、最終的なスクリプトを示します。
図5はブラウザに表示される絵です。
描画なので座標の指定がややこしいですが、
テンプレートをいじりながら必要なフィールドを泥縄式に足していっただけなので、
頭はそんなに使ってません。</p>
<p>↓リスト11: グラフを描くスクリプト</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

<span class="c">#1:順位 2:選手 3:本塁打 4:FROM 5:TO 6:試合 7:打数</span>
<span class="c">#ヘッダを削る</span>
tail -n +2 ./HOMER |
<span class="c">#上位10傑</span>
head |
awk <span class="s1">&#39;{wid=$3/2;print $2,$3,NR*24,NR*24+16,wid+95,wid}&#39;</span> &gt; <span class="nv">$tmp</span>-data
<span class="c">#1:選手名 2:本塁打数 3:グラフ左上y座標 4:字左下y座標</span>
<span class="c">#5:本塁打数文字右端位置 6:グラフ幅</span>

<span class="c">#テンプレートを準備</span>
cat <span class="s">&lt;&lt; EOF &gt; $tmp-template</span>
<span class="s">&lt;!DOCTYPE html&gt;</span>
<span class="s">&lt;html&gt;</span>
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;UTF-8&quot; /&gt;&lt;/head&gt;</span>
<span class="s"> &lt;body&gt;</span>
<span class="s"> &lt;svg style=&quot;height:500px;width:800px;font-size:16px&quot;&gt;</span>
<span class="s">&lt;!-- RECORDS --&gt;</span>
<span class="s"> &lt;text x=&quot;10&quot; y=&quot;%4&quot;&gt;%1&lt;/text&gt;</span>
<span class="s"> &lt;rect x=&quot;100&quot; y=&quot;%3&quot; width=&quot;%6&quot; height=&quot;20&quot;</span>
<span class="s"> fill=&quot;white&quot; stroke=&quot;black&quot; /&gt;</span>
<span class="s"> &lt;text x=&quot;%5&quot; y=&quot;%4&quot; style=&quot;text-anchor:end&quot;&gt;%2&lt;/text&gt;</span>
<span class="s">&lt;!-- RECORDS --&gt;</span>
<span class="s">&lt;/svg&gt;</span>
<span class="s">&lt;/body&gt;</span>
<span class="s">&lt;/html&gt;</span>
<span class="s">EOF</span>

<span class="c">#レコードをテンプレートに流し込む</span>
mojihame -lRECORDS <span class="nv">$tmp</span>-template <span class="nv">$tmp</span>-data &gt; <span class="nv">$tmp</span>-html
<span class="c">#表示</span>
firefox <span class="nv">$tmp</span>-html

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<div class="figure">
<img alt="_images/201204_5.png" src="201204_5.png" />
<p class="caption">図5：リスト10の結果</p>
</div>
<p>　さらに派手にしたものを図6に示します。
これはコードが長い（それでも72行しかない）ので紙面には載せられませんが、
<a class="reference external" href="https://github.com/ryuichiueda/SoftwareDesign">https://github.com/ryuichiueda/SoftwareDesign</a> にアップロードします。</p>
<div class="figure">
<img alt="_images/201204_6.png" src="201204_6.png" />
<p class="caption">図6：さらにお絵描きを凝ったもの</p>
</div>
</div>
</div>
<div class="section" id="id7">
<h2>4.3. 終わりに<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、bashを使ってHTMLファイルを作成しました。
意外にも親和性が高いということが示せたと思います。
HTML5やUTF-8などの普及で、
昔ほど難しいことをやらなくてもできることが増えています。
今後も「技術的に難しくても本質的に難しく無いもの」
はどんどん簡単になっていくでしょう。
シェルスクリプトの出番も増えるかもしれません。</p>
<p>　もう一つ新しい話題として、今回はmojihameというコマンドを使いました。
ほとんど反則技ですが（脚注：弊社で初めて見たときは本当に反則だと思いました。）、
便利になるコマンドはどんな言語でもよいから作って使えばよいという、
これもシェルスクリプトらしい特長になっていると思います。</p>
</div>
</div>
