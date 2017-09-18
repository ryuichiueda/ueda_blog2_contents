---
Copyright: (C) Ryuichi Ueda
---

# 開眼シェルスクリプト2014年4月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>4. 開眼シェルスクリプト 第4回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>4.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　書いている筆者本人が超地味だと公言する開眼シェルスクリプトも、<br />
今回で第四回です。今回は（この連載にしては）派手です。ブラウザで絵を描きます。</p><br />
<div class="section" id="id3"><br />
<h3>4.1.1. 禁欲的になれとは言ってません<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　端末で古いコマンドを使い、<br />
テキストばかりいじっているのでそう思われてもしょうがないのですが、<br />
別に昔に帰れとか、GUI見るなとか、そういうことをこの連載で言いたいわけではないのです。<br />
むしろ、逆です。ここ数年は、データの保存や表現形式は、テキスト<br />
（というよりも、より人間が読みやすい）データに向かっているようなので、<br />
テキストを操作できるということは、より普遍的なスキルになりつつあるようです。</p><br />
<p>　○○が廃れたなどと具体例を出して言うと角が立ちますので、一つ例を出します。<br />
筆者は職業柄、画面のスクリーンショットを撮ることが多いのですが、<br />
スクリーンショットはバイナリ形式のpng形式で保存しています。<br />
16進数でファイルの先頭を出すと、リスト1のように見えます。<br />
バイナリなので、catすると悲惨なことになります。</p><br />
<p>↓リスト1: png画像をodで見る。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>od -tx 201204_1.png | head -n 2<br />
0000000 474e5089 0a1a0a0d 0d000000 52444849<br />
0000020 df000000 ad000000 00000608 aa133000<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　別にcatできなくても画像なので全く構わないわけですが、<br />
それでも筆者は、10年後20年後には、<br />
ビットマップ画像（脚注：ベクトル画像でなく、あくまでビットマップ画像。）<br />
のフォーマットの最終型が次のようなテキストファイルを圧縮したものになると考えています。</p><br />
<p>↓リスト2: 近未来ビットマップ（予想）</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>y x r g b<br />
0 0 128 128 128<br />
0 1 255 121 121<br />
0 2 32 128 128<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この形式の問題はサイズがバカでかく、見た目もバカっぽいということですが、</p><br />
<ul class="simple"><br />
<li>ハードの進化でサイズの問題が些細なことになったらどうなる？</li><br />
<li>画像の一部だけ切り取るのはpng形式とどっちが楽か？</li><br />
<li>言語付属のライブラリを作ってメンテナンスする手間はどっちが楽か？</li><br />
<li>形式を拡張しなければならないとき、png形式と比べてどっちが自然に拡張できるか？</li><br />
</ul><br />
<p>などといろいろ利点、欠点を考えると、<br />
特に嫌悪や嘲笑の対象になるような形式でもないでしょう。<br />
実際、PDP-7上でUNIXが取った戦略は後者だったのです。</p><br />
<p>　今回は、次の有名な格言を。</p><br />
<ul><br />
<li><dl class="first docutils"><br />
<dt>Keep it simple, stupid.</dt><br />
<dd><p class="first last">（KISSの原則、ケリー・ジョンソン）</p><br />
</dd><br />
</dl><br />
</li><br />
</ul><br />
</div><br />
</div><br />
<div class="section" id="html"><br />
<h2>4.2. 今回のお題：HTMLで表とグラフを描く<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回のお題は、HTMLファイルをブラウザで見ることになりますが、<br />
次の方法のいずれかで見てください。</p><br />
<ul class="simple"><br />
<li>httpサーバを通してHTMLファイルを見る。</li><br />
<li>手元のデスクトップ機のUNIX環境でHTMLファイルを作り、手元のブラウザで見る。</li><br />
</ul><br />
<p>後者の場合は、httpサーバは不要です。<br />
今回は後者の場合を想定して話を進めて行きます。<br />
今回使用する環境も、リモートのサーバではなく、<br />
デスクトップ機です。諸元は以下のようになってます。</p><br />
<ul class="simple"><br />
<li>マシン：ThinkPad SL510</li><br />
<li>CPU, OS等：リスト3参照</li><br />
</ul><br />
<p>↓リスト3: CPU, OS等の情報</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>cat /proc/cpuinfo | grep <span class="s2">&quot;model name&quot;</span><br />
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz<br />
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz<br />
<span class="c">#↑補足: CPUはデュアルコアのもの1個</span><br />
ueda\@uedaubuntu:~<span class="nv">$ </span>uname -a<br />
Linux uedaubuntu 3.0.0-14-generic <span class="c">#23-Ubuntu SMP Mon Nov 21 20:34:47 UTC 2011 i686 i686 i386 GNU/Linux</span><br />
ueda\@uedaubuntu:~<span class="nv">$ </span>cat /etc/lsb-release | grep DESCRIPTION<br />
<span class="nv">DISTRIB_DESCRIPTION</span><span class="o">=</span><span class="s2">&quot;Ubuntu 11.10&quot;</span><br />
ueda\@uedaubuntu:~<span class="nv">$ </span>firefox -v<br />
Mozilla Firefox 9.0.1<br />
ueda\@uedaubuntu:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span><br />
ja_JP.UTF-8<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="section" id="html-html5"><br />
<h3>4.2.1. HTMLのおさらい（あるいは初めてのHTML5）<a class="headerlink" href="#html-html5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず、HTMLのおさらいをします。<br />
HTML は、テキストのどこがタイトルでどこが本文で・・・<br />
と印をつけていく方法の一種で、単なるテキストファイルです。<br />
それ以上のものでもそれ以下のものでもありません。<br />
それを踏まえて、リスト4のHTMLファイルを見てみましょう。HTML5で書いています。<br />
HTML5は、従来のHTMLの余計なものが省かれて簡素化されたので、<br />
以前のHTMLよりは理解しやすいと思います。説明する方も簡単で助かります。</p><br />
<p>↓リスト4: HTMLのおさらい</p><br />
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="cp">&lt;!DOCTYPE html&gt;</span><br />
<span class="nt">&lt;html&gt;</span><br />
 <span class="nt">&lt;head&gt;</span><br />
 <span class="nt">&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;utf-8&quot;</span> <span class="nt">/&gt;</span><br />
 <span class="nt">&lt;title&gt;</span>htmlの書き方<span class="nt">&lt;/title&gt;</span><br />
 <span class="nt">&lt;/head&gt;</span><br />
 <span class="nt">&lt;body&gt;</span><br />
 あいうえお<br />
 <span class="nt">&lt;/body&gt;</span><br />
<span class="nt">&lt;/html&gt;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト4の1行目は、このファイルがhtmlであるということを言っています。<br />
シバン（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> ）に似ています。<br />
それ以降は、 <tt class="docutils literal"><span class="pre">&lt;html&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/html&gt;</span></tt> の間に「要素」を詰め込んでいきます。<br />
要素というのは、</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">&lt;hoge&gt;</span></tt> から <tt class="docutils literal"><span class="pre">&lt;/hoge&gt;</span></tt> までの塊</li><br />
<li>あるいは <tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">...</span> <span class="pre">/&gt;</span></tt></li><br />
</ul><br />
<p>のことで、HTMLは、要素の下に要素がぶら下がって、<br />
その下に・・・と木構造になります。<br />
リスト1の場合は、一番外側のhtmlの下にheadとbodyがぶら下がって、<br />
headの下にはさらにmetaとtitleがぶら下がっています。<br />
<tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">...</span> <span class="pre">/&gt;</span></tt> の形式をとるときには <tt class="docutils literal"><span class="pre">/</span></tt> は不要なのですが、<br />
筆者は <tt class="docutils literal"><span class="pre">/</span></tt> がないと閉じた感じがしないので、<br />
かならず入れるようにしています。</p><br />
<p>　要素には、「内容」と「属性」というものがあります。<br />
「内容」は <tt class="docutils literal"><span class="pre">&lt;hoge&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/hoge&gt;</span></tt> に挟まれた部分、<br />
「属性」は、 <tt class="docutils literal"><span class="pre">&lt;hoge</span> <span class="pre">a=&quot;b&quot;</span> <span class="pre">c=&quot;d&quot;</span> <span class="pre">...</span> <span class="pre">&gt;</span></tt> のように <tt class="docutils literal"><span class="pre">名前=&quot;値&quot;</span></tt><br />
を並べて書いたものです。<br />
「内容」はその名の通り、要素が持っている情報本体で、<br />
属性は、要素に対する味付けと考えてください。</p><br />
<p>　HTML5なので、HTML5に対応しているブラウザで見てみましょう。<br />
上のHTMLをhoge.htmlと名前をつけてどこかに保存します。<br />
ウェブサーバを立ち上げなくてもファイルをダブルクリックすれば見られるはずです。<br />
環境によっては、次のように端末からfirefoxを立ち上げることもできます。<br />
（くれぐれもリモートのマシンにssh接続している場合はやらないでください。）</p><br />
<div class="highlight-bash"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>firefox hoge.html<br />
</pre></div><br />
</div><br />
<div class="figure"><br />
<img alt="_images/201204_1.png" src="201204_1.png" /><br />
<p class="caption">図1：リスト1のHTMLをfirefoxで見る</p><br />
</div><br />
<p>見ることができましたでしょうか。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>4.2.2. HTMLを出力するシェルスクリプト<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、HTMLを出力するシェルスクリプトを作ってみましょう。<br />
CGIスクリプトにすることもできるのですが、それは後日ということで、<br />
とにかくHTMLファイルを作るシェルスクリプトを作ります。</p><br />
<p>　まずは、リスト5のようなシェルスクリプトから始めます。</p><br />
<p>↓リスト5: HTMLのおさらい</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12<br />
13<br />
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/GIHYO<span class="nv">$ </span>cat html.sh<br />
<span class="c">#!/bin/bash</span><br />
<br />
cat <span class="s">&lt;&lt; EOF &gt; ./hoge.html</span><br />
<span class="s">&lt;!DOCTYPE html&gt;</span><br />
<span class="s">&lt;html&gt;</span><br />
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;UTF-8&quot; /&gt;&lt;/head&gt;</span><br />
<span class="s"> &lt;body&gt;</span><br />
<span class="s"> $(date)</span><br />
<span class="s"> &lt;/body&gt;</span><br />
<span class="s">&lt;/html&gt;</span><br />
<span class="s">EOF</span><br />
<br />
firefox ./hoge.html<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト5で大事なのは、4～12行目の部分です。<br />
この部分は「ヒアドキュメント」と呼ばれ、<br />
<tt class="docutils literal"><span class="pre">command</span> <span class="pre">&lt;&lt;</span> <span class="pre">EOF</span></tt> と <tt class="docutils literal"><span class="pre">EOF</span></tt> に挟まれたテキストがそのまま<br />
<tt class="docutils literal"><span class="pre">command</span></tt> の標準入力に入力されます。<br />
EOFは、別の文字列でも構いません。<br />
もしヒアドキュメントの途中でEOFと出てくる可能性があれば、<br />
別の文字列にした方がよいでしょう。<br />
この例では、./hoge.htmlに5～11行目の中身が溜まります。<br />
catで見てみてください。</p><br />
<p>　もう一つ大事なのは9行目で、 <tt class="docutils literal"><span class="pre">$(</span> <span class="pre">)</span></tt> でコマンドを挟むと、<br />
コマンドの出力がヒアドキュメント中に埋め込まれます。<br />
この例では、dateコマンドの結果がbody要素の内容になります。<br />
<tt class="docutils literal"><span class="pre">$(</span> <span class="pre">)</span></tt> の中にパイプでコマンドをずらずら連ねるとヒアドキュメント内に<br />
HTMLとコードが混ざって汚くなるので、<br />
以下ではヒアドキュメント内ではcatだけを使います。</p><br />
<p>　このスクリプトを実行すると、firefoxが立ち上がり、<br />
図2のようにスクリプトを実行した時刻がブラウザの画面に表示されます。</p><br />
<div class="figure"><br />
<img alt="_images/201204_2.png" src="201204_2.png" /><br />
<p class="caption">図2: リスト5の実行結果</p><br />
</div><br />
</div><br />
<div class="section" id="id5"><br />
<h3>4.2.3. 表を表示<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、何か統計情報を表にしてみましょう。<br />
表ならば端末で見れば十分なのですが、いくつも表を並べて一度に見たり、<br />
比較したりするにはブラウザはうってつけの道具です。<br />
表にするのは趣味丸出しのリスト6のデータです。</p><br />
<p>↓リスト6: 通算本塁打数</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/WEB/GIHYO<span class="nv">$ </span>head -n 5 HOMER<br />
順位 選手 本塁打 FROM TO 試合 打数<br />
1 王　貞治 868 1959 1980 2831 9250<br />
2 野村　克也 657 1954 1980 3017 10472<br />
3 門田　博光 567 1970 1992 2571 8868<br />
4 山本　浩二 536 1969 1986 2284 8052<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　まず、このデータをそのまま表にしてみましょう。<br />
HTMLでは表（テーブル）はリスト7のように書きます。<br />
<tt class="docutils literal"><span class="pre">&lt;tr&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/tr&gt;</span></tt> で挟まれた部分が1行に相当、<br />
<tt class="docutils literal"><span class="pre">&lt;td&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/td&gt;</span></tt> で挟まれた部分がテーブルの一区画（セル）に相当します。</p><br />
<p>↓リスト7: HTMLのテーブル</p><br />
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nt">&lt;table&gt;</span><br />
 <span class="nt">&lt;tr&gt;</span><br />
 <span class="nt">&lt;td&gt;</span>1行1列<span class="nt">&lt;/td&gt;</span><br />
 <span class="nt">&lt;td&gt;</span>1行2列<span class="nt">&lt;/td&gt;</span><br />
 <span class="nt">&lt;/tr&gt;</span><br />
 <span class="nt">&lt;tr&gt;</span><br />
 <span class="nt">&lt;td&gt;</span>2行1列<span class="nt">&lt;/td&gt;</span><br />
 <span class="nt">&lt;td&gt;</span>2行2列<span class="nt">&lt;/td&gt;</span><br />
 <span class="nt">&lt;/tr&gt;</span><br />
<span class="nt">&lt;/table&gt;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これをawkで作ってみましょう。リスト8のようになります。<br />
各フィールドを td で囲んで外側を tr で包めばよいということになります。<br />
ただまあ、数字も名前も全部左揃えになっており、<br />
表現力に限界があります。<br />
なんとかしようとすると、とたんにawkの部分が膨れてしまうでしょう。<br />
これについては、グラフのところで解決します。</p><br />
<p>　ちなみに、9行目のteeコマンドは標準入力をファイルと標準出力に二股分岐するコマンドです。<br />
パイプの間に挟んでデバッグによく使います。</p><br />
<p>↓リスト8: 表の出力</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12<br />
13<br />
14<br />
15<br />
16<br />
17<br />
18<br />
19<br />
20<br />
21<br />
22<br />
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
awk <span class="s1">&#39;{ print &quot;&lt;tr&gt;&quot;;</span><br />
<span class="s1"> for(i=1;i&lt;=NF;i++){print &quot;&lt;td&gt;&quot;$i&quot;&lt;/td&gt;&quot;};</span><br />
<span class="s1"> print &quot;&lt;/tr&gt;&quot; }&#39;</span> ./HOMER &gt; <span class="nv">$tmp</span>-table<br />
<br />
tee <span class="nv">$tmp</span>-html <span class="s">&lt;&lt; EOF</span><br />
<span class="s">&lt;!DOCTYPE html&gt;</span><br />
<span class="s">&lt;html&gt;</span><br />
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;/head&gt;</span><br />
<span class="s"> &lt;body&gt;</span><br />
<span class="s"> &lt;h1 style=&quot;font-size:18px&quot;&gt;通算本塁打&lt;/h1&gt;</span><br />
<span class="s"> &lt;table border=&quot;1&quot; cellspacing=&quot;0&quot;&gt;</span><br />
<span class="s">$(cat $tmp-table)</span><br />
<span class="s"> &lt;/table&gt;</span><br />
<span class="s"> &lt;/body&gt;</span><br />
<span class="s">&lt;/html&gt;</span><br />
<span class="s">EOF</span><br />
<br />
firefox <span class="nv">$tmp</span>-html<br />
rm -f <span class="nv">$tmp</span>-*<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="figure"><br />
<img alt="_images/201204_3.png" src="201204_3.png" /><br />
<p class="caption">図3：表の出力</p><br />
</div><br />
<p>　次のグラフ描画の際に使うので、cssについて簡単に説明します。<br />
リスト8のh1の属性： style=&#8221;font-size:18px&#8221; は、<br />
h1の内容がブラウザに描かれるときのフォントの大きさを指定しています。<br />
<tt class="docutils literal"><span class="pre">font-size:18px</span></tt> の部分はcssと呼ばれるもので、<br />
<tt class="docutils literal"><span class="pre">属性1:値1;属性2:値2;...</span></tt> というように並べていくと、<br />
ブラウザへの出力方法を細かく指定できます。<br />
どんな属性があるかは、ウェブ上に様々な情報があるのでそちらに譲ります。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>4.2.4. グラフを描く<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、次にリスト8の本塁打数をグラフにしてみましょう。<br />
絵を描くわけですが、ここではSVG（scalable vector graphics）<br />
というものをHTMLに埋め込んで使います。<br />
まずは理屈抜きで、HTMLの例をリスト9に、ブラウザで見たものを図4に示します。</p><br />
<p>↓リスト9: svgで描画するHTML</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12<br />
13<br />
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/GIHYO<span class="nv">$ </span>cat svg.html<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
&lt;head&gt;&lt;meta <span class="nv">charset</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span> /&gt;&lt;/head&gt;<br />
&lt;!--注意：インデントは正しく！--&gt;<br />
&lt;body&gt;<br />
&lt;svg&gt;<br />
 &lt;text <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;10&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;36&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;font-size:16px&quot;</span>&gt;USP&lt;/text&gt;<br />
 &lt;rect <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;50&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;20&quot;</span> <span class="nv">width</span><span class="o">=</span><span class="s2">&quot;60&quot;</span> <span class="nv">height</span><span class="o">=</span><span class="s2">&quot;20&quot;</span><br />
 <span class="nv">fill</span><span class="o">=</span><span class="s2">&quot;white&quot;</span> <span class="nv">stroke</span><span class="o">=</span><span class="s2">&quot;black&quot;</span> /&gt;<br />
 &lt;text <span class="nv">x</span><span class="o">=</span><span class="s2">&quot;110&quot;</span> <span class="nv">y</span><span class="o">=</span><span class="s2">&quot;36&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;text-anchor:end&quot;</span>&gt;00&lt;/text&gt;<br />
&lt;/svg&gt;<br />
&lt;/body&gt;<br />
&lt;/html&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="figure"><br />
<img alt="_images/201204_4.png" src="201204_4.png" /><br />
<p class="caption">図4：表の出力</p><br />
</div><br />
<p>　 <tt class="docutils literal"><span class="pre">&lt;svg&gt;</span></tt> と <tt class="docutils literal"><span class="pre">&lt;/svg&gt;</span></tt> の間に、rectやらtextやらがいますが、<br />
要は図形一つ一つを指定していくとブラウザに<br />
直接図形を描き出してくれるということです。<br />
こんな便利な機能を使わない手はありません。<br />
ただ、図形の部分のHTMLをawkで出力しようとすると<br />
ややこしいコードになってしまうという問題があります。</p><br />
<p>　ここでは、mojihameという便利コマンドを使うことにします。<br />
おそらく聞いたことが無いコマンドだと思いますが、<br />
USP研究所のコマンドの一部がスクリプト言語で公開されているので、<br />
ネットからダウンロードできます。</p><br />
<ul class="simple"><br />
<li><a class="reference external" href="http://uec.usp-lab.com">http://uec.usp-lab.com</a></li><br />
</ul><br />
<p>からたどっていくとOpen usp tukubai<br />
という名前のコマンドセットがダウンロードできるので、<br />
その中のmojihameというコマンドを使います。<br />
設定方法はサイトで確認できますが、<br />
単なるpythonのスクリプトなので、スクリプトをダウンロードして<br />
<tt class="docutils literal"><span class="pre">python</span> <span class="pre">mojihame</span></tt> と打てば実行できます。</p><br />
<p>　mojihameはリスト10のように使います。<br />
<tt class="docutils literal"><span class="pre">temp</span></tt> ファイルの%1、%2、・・・というのは、<br />
ここをデータファイルの第1、第2フィールドで置き換えるという意味で、<br />
3行目、5行目の「AAA」はこの間を<br />
データファイルのレコードの数だけ繰り返し出力しろという意味のマークです。<br />
mojihameで <tt class="docutils literal"><span class="pre">-lAAA</span></tt> とマークをオプションで指定して、<br />
tempとdataを入力すると、レコードがテンプレートに嵌って出力されます。</p><br />
<p>↓リスト10: mojihameの使い方</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12<br />
13<br />
14<br />
15<br />
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>cat temp<br />
長者番付（秘）<br />
AAA<br />
%1位 %2さん 納税額%3円<br />
AAA<br />
ueda\@uedaubuntu:~<span class="nv">$ </span>cat data<br />
1 松浦 12<br />
2 濱田 8<br />
3 上田 -5<br />
4 法林 -110<br />
ueda\@uedaubuntu:~<span class="nv">$ </span>mojihame -lAAA temp data<br />
長者番付（秘）<br />
1位 松浦さん 納税額12円<br />
2位 濱田さん 納税額8円<br />
3位 上田さん 納税額-5円<br />
4位 法林さん 納税額-110円<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　では、mojihame+svgで本塁打数を横向きの棒グラフで書いてみます。<br />
図4のUSPのところに選手名、00のところに本塁打数を書きます。<br />
また、本塁打数に比例させて四角の幅を変えます。</p><br />
<p>　やることは、HTMLでmojihame用のテンプレートを書くことと、<br />
mojihameに食わせるデータを準備することです。<br />
リスト11に、最終的なスクリプトを示します。<br />
図5はブラウザに表示される絵です。<br />
描画なので座標の指定がややこしいですが、<br />
テンプレートをいじりながら必要なフィールドを泥縄式に足していっただけなので、<br />
頭はそんなに使ってません。</p><br />
<p>↓リスト11: グラフを描くスクリプト</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10<br />
11<br />
12<br />
13<br />
14<br />
15<br />
16<br />
17<br />
18<br />
19<br />
20<br />
21<br />
22<br />
23<br />
24<br />
25<br />
26<br />
27<br />
28<br />
29<br />
30<br />
31<br />
32<br />
33<br />
34<br />
35<br />
36<br />
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
<span class="c">#1:順位 2:選手 3:本塁打 4:FROM 5:TO 6:試合 7:打数</span><br />
<span class="c">#ヘッダを削る</span><br />
tail -n +2 ./HOMER |<br />
<span class="c">#上位10傑</span><br />
head |<br />
awk <span class="s1">&#39;{wid=$3/2;print $2,$3,NR*24,NR*24+16,wid+95,wid}&#39;</span> &gt; <span class="nv">$tmp</span>-data<br />
<span class="c">#1:選手名 2:本塁打数 3:グラフ左上y座標 4:字左下y座標</span><br />
<span class="c">#5:本塁打数文字右端位置 6:グラフ幅</span><br />
<br />
<span class="c">#テンプレートを準備</span><br />
cat <span class="s">&lt;&lt; EOF &gt; $tmp-template</span><br />
<span class="s">&lt;!DOCTYPE html&gt;</span><br />
<span class="s">&lt;html&gt;</span><br />
<span class="s"> &lt;head&gt;&lt;meta charset=&quot;UTF-8&quot; /&gt;&lt;/head&gt;</span><br />
<span class="s"> &lt;body&gt;</span><br />
<span class="s"> &lt;svg style=&quot;height:500px;width:800px;font-size:16px&quot;&gt;</span><br />
<span class="s">&lt;!-- RECORDS --&gt;</span><br />
<span class="s"> &lt;text x=&quot;10&quot; y=&quot;%4&quot;&gt;%1&lt;/text&gt;</span><br />
<span class="s"> &lt;rect x=&quot;100&quot; y=&quot;%3&quot; width=&quot;%6&quot; height=&quot;20&quot;</span><br />
<span class="s"> fill=&quot;white&quot; stroke=&quot;black&quot; /&gt;</span><br />
<span class="s"> &lt;text x=&quot;%5&quot; y=&quot;%4&quot; style=&quot;text-anchor:end&quot;&gt;%2&lt;/text&gt;</span><br />
<span class="s">&lt;!-- RECORDS --&gt;</span><br />
<span class="s">&lt;/svg&gt;</span><br />
<span class="s">&lt;/body&gt;</span><br />
<span class="s">&lt;/html&gt;</span><br />
<span class="s">EOF</span><br />
<br />
<span class="c">#レコードをテンプレートに流し込む</span><br />
mojihame -lRECORDS <span class="nv">$tmp</span>-template <span class="nv">$tmp</span>-data &gt; <span class="nv">$tmp</span>-html<br />
<span class="c">#表示</span><br />
firefox <span class="nv">$tmp</span>-html<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="figure"><br />
<img alt="_images/201204_5.png" src="201204_5.png" /><br />
<p class="caption">図5：リスト10の結果</p><br />
</div><br />
<p>　さらに派手にしたものを図6に示します。<br />
これはコードが長い（それでも72行しかない）ので紙面には載せられませんが、<br />
<a class="reference external" href="https://github.com/ryuichiueda/SoftwareDesign">https://github.com/ryuichiueda/SoftwareDesign</a> にアップロードします。</p><br />
<div class="figure"><br />
<img alt="_images/201204_6.png" src="201204_6.png" /><br />
<p class="caption">図6：さらにお絵描きを凝ったもの</p><br />
</div><br />
</div><br />
</div><br />
<div class="section" id="id7"><br />
<h2>4.3. 終わりに<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、bashを使ってHTMLファイルを作成しました。<br />
意外にも親和性が高いということが示せたと思います。<br />
HTML5やUTF-8などの普及で、<br />
昔ほど難しいことをやらなくてもできることが増えています。<br />
今後も「技術的に難しくても本質的に難しく無いもの」<br />
はどんどん簡単になっていくでしょう。<br />
シェルスクリプトの出番も増えるかもしれません。</p><br />
<p>　もう一つ新しい話題として、今回はmojihameというコマンドを使いました。<br />
ほとんど反則技ですが（脚注：弊社で初めて見たときは本当に反則だと思いました。）、<br />
便利になるコマンドはどんな言語でもよいから作って使えばよいという、<br />
これもシェルスクリプトらしい特長になっていると思います。</p><br />
</div><br />
</div>
