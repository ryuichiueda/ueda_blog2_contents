---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年9月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="cgi3">
<h1>21. 開眼シェルスクリプト 第21回 シェルスクリプトでCGIスクリプト3<a class="headerlink" href="#cgi3" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　ここ二回、シェルスクリプトでCGIやっちまえ！という企画で進めてきましたが、
今回はその最終回です。最終回らしく最もシェルスクリプトと縁遠そうな
Ajaxをやってみます。</p>
<p>　Ajaxというのは Asynchronous JavaScript + XML の略なのですが、
これほどよく分からない言葉もありません。
また、jQueryなどの直接Ajaxとは関係ないものと抱き合わせで覚える人も多いので、
なんとなく敷居の高いもののように感じている人もいると思います。</p>
<p>　今回は、JavaScriptとシェルスクリプトだけでAjaxを実現することで、
Ajaxの正体が案外単純なものであることをお見せします。
今回の内容を理解するには、JavaScriptの知識が少し必要です。
しかし、JSONもXMLもjQueryもprototype.jsも出てきません。
そいつらは本質的に無関係です。</p>
<p>言葉や属性こそ、物事の本質に一致すべきであり、
逆に本質を言葉に従わせるべきではない。
というのは、最初に物事が存在し、言葉はそのあとに従うものだからだ。</p>
<p>&#8212;ガリレオ・ガリレイ</p>
<div class="section" id="id1">
<h2>21.1. 環境<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回、前々回に引き続き、
筆者はMacでapacheを動作させてコードの動作確認をしています。
今回は、CGIスクリプトだけでなく、
静的なHTMLファイルもブラウザで閲覧したいのですが、
筆者のMacでは、デフォルトで <tt class="docutils literal"><span class="pre">/Library/WebServer/Documents/</span></tt>
というディレクトリにHTMLファイルを置くということになっているみたいです。
前々回、 <tt class="docutils literal"><span class="pre">~/cgi-bin/</span></tt> というシンボリックリンクを作って
CGIスクリプト置き場にリンクを張りましたが、
今回も同様にシンボリックリンクを張ります。</p>
<p>　手順をリスト1に示します。
万が一、前々回、前回を読んでいなくても、
リスト1の <tt class="docutils literal"><span class="pre">ls</span></tt> の出力のように設定できれば大丈夫です。</p>
<ul class="simple">
<li>リスト1: HTMLファイルの置き場所にリンクを張って所有権を変更</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ln -s /Library/WebServer/Documents/ html
uedamac:~ ueda<span class="nv">$ </span>sudo chown ueda:staff html
uedamac:~ ueda<span class="nv">$ </span>ls -l ~/cgi-bin ~/html
lrwxr-xr-x 1 ueda staff 35 4 22 23:52 /Users/ueda/cgi-bin -&gt; /Library/WebServer/CGI-Executables/
lrwxr-xr-x 1 ueda staff 29 6 16 11:37 /Users/ueda/html -&gt; /Library/WebServer/Documents/
</pre></div>
</td></tr></table></div>
<p>　準備ができたら、apacheを立ち上げましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>sudo apachectl start
</pre></div>
</div>
<p>　また、今回はMac上で作ったCGIスクリプトがLinuxサーバと通信を行います。
通信先のLinuxサーバには <tt class="docutils literal"><span class="pre">sar</span></tt> コマンド（sysstat）
がインストールされていることを前提としています。</p>
</div>
<div class="section" id="id2">
<h2>21.2. 最初の例<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まず、一番簡単な例から示します。
Ajaxというのは、結局のところ、
ブラウザに表示されたウェブページの裏でJavaScriptがCGIスクリプトを呼び出し、
結果をもらってウェブページの一部を書き換える方法です。
ということは、htmlの中に、その仕掛けを書いてやればよいということになります。</p>
<p>　その仕掛けのミニマムな構成が、リスト2のhtmlファイルです。
HTML5で書いていますが、別にHTML 4.01でもXHTMLでもかまいません。</p>
<ul class="simple">
<li>リスト2: <tt class="docutils literal"><span class="pre">~/html/ajax1.html</span></tt></li>
</ul>
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="nt">&lt;html</span> <span class="na">lang=</span><span class="s">&quot;ja&quot;</span><span class="nt">&gt;</span>
 <span class="nt">&lt;head&gt;</span>
 <span class="nt">&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;UTF-8&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;script&gt;</span>
 <span class="kd">function</span> <span class="nx">callCgi</span><span class="p">(){</span>
 <span class="kd">var</span> <span class="nx">h</span> <span class="o">=</span> <span class="k">new</span> <span class="nx">XMLHttpRequest</span><span class="p">();</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">open</span><span class="p">(</span><span class="s2">&quot;POST&quot;</span><span class="p">,</span><span class="s2">&quot;/cgi-bin/show.cgi&quot;</span><span class="p">,</span><span class="kc">false</span><span class="p">);</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">setRequestHeader</span><span class="p">(</span><span class="s2">&quot;Content-Type&quot;</span><span class="p">,</span>
 <span class="s2">&quot;application/x-www-form-urlencoded&quot;</span><span class="p">);</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">send</span><span class="p">(</span> <span class="s2">&quot;dummy=&quot;</span> <span class="o">+</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">random</span><span class="p">()</span> <span class="p">);</span>
 <span class="nb">document</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">innerHTML</span> <span class="o">=</span> <span class="nx">h</span><span class="p">.</span><span class="nx">responseText</span><span class="p">;</span>
 <span class="p">}</span>
 <span class="nt">&lt;/script&gt;</span>
 <span class="nt">&lt;/head&gt;</span>
 <span class="nt">&lt;body</span> <span class="na">onload=</span><span class="s">&quot;callCgi()&quot;</span><span class="nt">&gt;</span>
 <span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/html&gt;</span>
</pre></div>
</td></tr></table></div>
<p>　シェルスクリプトの話でないのであまり細かく話したくありませんが、
最低限知っておくべきことを書きます。
16行目の <tt class="docutils literal"><span class="pre">onload=&quot;callCgi()&quot;</span></tt> を書く事によって、
ブラウザにこのHTMLの内容が表示されたときに6行目の
<tt class="docutils literal"><span class="pre">function〜</span></tt> で定義した関数が起動します。
8〜11行目でCGIスクリプトを呼び出して、
12行目でCGIスクリプトが送ってきた文字列を受け取っています。
それで、受け取った文字列は12行目の前半で <tt class="docutils literal"><span class="pre">document.body.innerHTML=</span></tt>
とあるように、bodyの内側に相当する部分に代入しています。
ブラウザにはこの代入がすぐに反映されるので、
画面には代入したものが表示されます。</p>
<p>　もうちょっとCGIスクリプトを呼び出す部分を説明しなければなりません。
まず、8行目はPOSTメソッドを使い、 <tt class="docutils literal"><span class="pre">/cgi-bin/show.cgi</span></tt>
にデータを送るぞと宣言しています。
先月号でGETメソッドを使ってCGIスクリプトに文字列を投げましたが、
POSTもCGIスクリプトにデータを送るもう一つの方法です。
もう一個の引数 <tt class="docutils literal"><span class="pre">false</span></tt> は、今は無視で。
9, 10行目は、 <tt class="docutils literal"><span class="pre">show.cgi</span></tt> を呼び出すときに使うHTTPヘッダを作っています。
実際に <tt class="docutils literal"><span class="pre">show.cgi</span></tt> を呼び出しているのは11行目で、
<tt class="docutils literal"><span class="pre">show.cgi</span></tt> に向かって <tt class="docutils literal"><span class="pre">dummy=&lt;乱数&gt;</span></tt> という文字列を送っています。
毎回同じ文字列をPOSTしようとすると、
怠けてCGIスクリプトを呼ばないブラウザがあるので、それを防いでいます。
ところで、この部分のJavaScriptの書き方は、
元来単純なHTTPを複雑にラッパーしていて、
正直ぎこちない感じがします。皆さんはどう感じるでしょうか？</p>
<p>　では、このHTMLから呼ばれる <tt class="docutils literal"><span class="pre">show.cgi</span></tt> を作りましょう。
とにかく何か文字列を送ればブラウザに表示されるのですが、
ここはリスト3のように書いて
<tt class="docutils literal"><span class="pre">date</span></tt> コマンドの出力でも送ってみましょう。</p>
<ul class="simple">
<li>リスト3: <tt class="docutils literal"><span class="pre">~/cgi-bin/show.cgi</span></tt></li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="s1">&#39;Content-type: text/html&#39;</span>
<span class="nb">echo</span>
<span class="nb">echo</span> <span class="s1">&#39;&lt;strong style=&quot;font-size:24px&quot;&gt;&#39;</span>
date
<span class="nb">echo</span> <span class="s1">&#39;&lt;/strong&gt;&#39;</span>
</pre></div>
</td></tr></table></div>
<p>このようにHTTPヘッダを出力した後に
<tt class="docutils literal"><span class="pre">date</span></tt> を実行します。
ただ時刻を送っても面白くないので、
<tt class="docutils literal"><span class="pre">strong</span></tt> で囲ってCSSでスタイルも指定しています。
<tt class="docutils literal"><span class="pre">show.cgi</span></tt> のパーミッションをいじって実行可能にしたら、
<tt class="docutils literal"><span class="pre">ajax1.html</span></tt> をブラウザで見てみましょう。
図1のように大きな太字で時刻が表示されたら成功です。</p>
<p>　 <tt class="docutils literal"><span class="pre">show.cgi</span></tt> の方は、普通のCGIスクリプトのようにHTTPヘッダを出力した後、
HTMLの破片を出力します。
<tt class="docutils literal"><span class="pre">ajax1.html</span></tt> に比べて単純極まりないですが、
そういうものです。
これもまた、JSONで送った方がきれいとかいろいろ議論はありますが、
ここではスルーしておきましょう。
簡単にできることを無理に複雑にすることはないでしょう。</p>
<ul class="simple">
<li>図1: <tt class="docutils literal"><span class="pre">ajax1.html</span></tt> から <tt class="docutils literal"><span class="pre">show.cgi</span></tt> を呼び出した後</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="AJAX1.png"><img alt="" src="AJAX1.png" style="width: 30%;" /></a>
</div>
</div>
<div class="section" id="id3">
<h2>21.3. 非同期通信<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今の例を応用すると、
動的にブラウザに写るものを書き換え放題になるわけですが、
頻繁にCGIスクリプトを呼び出す場合には一つ問題があります。
上の書き方では、CGIスクリプトが返事をよこさないと、
ブラウザは待っている間、固まってしまいます。</p>
<p>　実はAjaxにはブラウザを固めないもう一つの書き方があります。
リスト4のように書きます。
ブラウザから閲覧すると、 <tt class="docutils literal"><span class="pre">ajax1.html</span></tt>
と同じように時刻が表示されると思います。</p>
<ul class="simple">
<li>リスト4: <tt class="docutils literal"><span class="pre">ajax1.html</span></tt> を非同期処理に書き換えた <tt class="docutils literal"><span class="pre">ajax2.html</span></tt></li>
</ul>
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="nt">&lt;html</span> <span class="na">lang=</span><span class="s">&quot;ja&quot;</span><span class="nt">&gt;</span>
 <span class="nt">&lt;head&gt;</span>
 <span class="nt">&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;UTF-8&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;script&gt;</span>
 <span class="kd">function</span> <span class="nx">callCgi</span><span class="p">(){</span>
 <span class="kd">var</span> <span class="nx">h</span> <span class="o">=</span> <span class="k">new</span> <span class="nx">XMLHttpRequest</span><span class="p">();</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">onreadystatechange</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(){</span>
 <span class="k">if</span><span class="p">(</span><span class="nx">h</span><span class="p">.</span><span class="nx">readyState</span> <span class="o">!=</span> <span class="mi">4</span> <span class="o">||</span> <span class="nx">h</span><span class="p">.</span><span class="nx">status</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">)</span>
 <span class="k">return</span><span class="p">;</span>

 <span class="nb">document</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">innerHTML</span> <span class="o">=</span> <span class="nx">h</span><span class="p">.</span><span class="nx">responseText</span><span class="p">;</span>
 <span class="p">}</span>

 <span class="nx">h</span><span class="p">.</span><span class="nx">open</span><span class="p">(</span><span class="s2">&quot;POST&quot;</span><span class="p">,</span><span class="s2">&quot;/cgi-bin/show.cgi&quot;</span><span class="p">,</span><span class="kc">true</span><span class="p">);</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">setRequestHeader</span><span class="p">(</span><span class="s2">&quot;Content-Type&quot;</span><span class="p">,</span>
 <span class="s2">&quot;application/x-www-form-urlencoded&quot;</span><span class="p">);</span>
 <span class="nx">h</span><span class="p">.</span><span class="nx">send</span><span class="p">(</span> <span class="s2">&quot;dummy=&quot;</span> <span class="o">+</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">random</span><span class="p">()</span> <span class="p">);</span>
 <span class="p">}</span>
 <span class="nt">&lt;/script&gt;</span>
 <span class="nt">&lt;/head&gt;</span>
 <span class="nt">&lt;body</span> <span class="na">onload=</span><span class="s">&quot;callCgi()&quot;</span><span class="nt">&gt;</span>
 <span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/html&gt;</span>
</pre></div>
</td></tr></table></div>
<p>　これもJavaScriptの話なのであまり詳しく説明したくないのですが、
何をやっているかというと、 <tt class="docutils literal"><span class="pre">h.onreadystatechange</span></tt>
というのが、CGIスクリプトから返事が来たら実行される関数の名前で、
そこに <tt class="docutils literal"><span class="pre">=</span> <span class="pre">function(){...</span></tt> で関数の中身を結びつけています。
8行目から13行目は、単に関数を名前に代入しているだけなので、
実際に実行されるのはCGIスクリプトから返事が来たときです。</p>
<p>　ということは、8〜13行目はすっ飛ばされて、
<tt class="docutils literal"><span class="pre">open</span></tt> 以下の、CGIスクリプトにちょっかいを出す処理が行われた後に、
この関数は終わります。
<tt class="docutils literal"><span class="pre">open</span></tt> の第三引数が <tt class="docutils literal"><span class="pre">false</span></tt> から <tt class="docutils literal"><span class="pre">true</span></tt> に変わっていますが、
これは「非同期にするよ」という意味です。</p>
<p>　関数が終わった後（いや、反応がものすごい早い場合は終わる前かもしれませんが）
CGIスクリプトから返事が来ます。
そこで、8~13行目で設定した関数の中身が走ります。
まず、9行目で</p>
<ul class="simple">
<li>CGIスクリプトから受信完了（ <tt class="docutils literal"><span class="pre">h.readyState</span></tt> が4 ）</li>
<li>CGIスクリプトからのステータスコードがOK（ <tt class="docutils literal"><span class="pre">h.status</span></tt> が200 ）（脚注： 404 not found とか 403 forbidden とかのアレです。）</li>
</ul>
<p>であることを確認し、その下に書いてある処理を実行します。</p>
<p>　この書き方だと、CGIスクリプトからの受信を受け取る処理が後ろに回るので、
ブラウザ側で待ちが発生しているように見えることはありません。
Ajaxの際は、普通はこのように非同期を使い、
画面の内容に齟齬が出ないようにしたいときは同期を使います。</p>
</div>
<div class="section" id="id4">
<h2>21.4. 複数のサーバの監視画面を作る<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　このままだとまるでJavaScript講座になってしまうので、
シェルスクリプトを組み合わせて作り物をしてみましょう。
管理している複数のLinuxサーバの負荷をモニタするツールを作ってみます。</p>
<p>　まず、Ajaxで呼び出されるシェルスクリプトを書きます。
リスト6に示すのは、IPアドレスとsshのポート番号をPOSTされたら、
そのIPの持ち主のロードアベレージを取得し、
SVG（Scalable Vector Graphics）でグラフを描くシェルスクリプトです。</p>
<ul class="simple">
<li>リスト6: Ajaxで呼び出される <tt class="docutils literal"><span class="pre">ldavg.cgi</span></tt></li>
</ul>
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
37
38
39
40</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -xv</span>
<span class="nb">exec </span>2&gt; /tmp/log

<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:<span class="nv">$PATH</span>
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

dd <span class="nv">bs</span><span class="o">=</span><span class="k">${</span><span class="nv">CONTENT_LENGTH</span><span class="k">}</span> |
cgi-name -i_ -d_ &gt; <span class="nv">$tmp</span>-name

<span class="nv">host</span><span class="o">=</span><span class="k">$(</span>nameread host <span class="nv">$tmp</span>-name<span class="k">)</span>
<span class="nv">port</span><span class="o">=</span><span class="k">$(</span>nameread port <span class="nv">$tmp</span>-name<span class="k">)</span>

ssh <span class="s2">&quot;$host&quot;</span> -p <span class="s2">&quot;$port&quot;</span> <span class="s1">&#39;LANG=C sar -q&#39;</span> |
grep <span class="s2">&quot;^..:..:..&quot;</span> |
sed <span class="s1">&#39;s/^\\(..\\):\\(..\\):../\\1時\\2分/&#39;</span> |
grep -v ldavg |
tail -r |
awk <span class="s1">&#39;{print NR*20+20,$1,int($4*100),$4,\\</span>
<span class="s1"> NR*20+7,NR*20+19}&#39;</span> &gt; <span class="nv">$tmp</span>-sar
<span class="c">#1:文字y位置 2:時刻 3:棒グラフ幅 4:ldavg</span>
<span class="c">#5:棒グラフy位置 6:ldavg文字y位置</span>

cat <span class="s">&lt;&lt; FIN &gt; $tmp-svg</span>
<span class="s">&lt;svg style=&quot;width:300px;height:600px&quot;&gt;</span>
<span class="s"> &lt;text x=&quot;0&quot; y=&quot;20&quot; font-size=&quot;20&quot;&gt;$host&lt;/text&gt;</span>
<span class="s">&lt;!-- RECORDS --&gt;</span>
<span class="s"> &lt;text x=&quot;0&quot; y=&quot;%1&quot; font-size=&quot;14&quot;&gt;%2&lt;/text&gt;</span>
<span class="s"> &lt;rect x=&quot;68&quot; y=&quot;%5&quot; width=&quot;%3&quot; height=&quot;15&quot;</span>
<span class="s"> fill=&quot;navy&quot; stroke=&quot;black&quot; /&gt;</span>
<span class="s"> &lt;text x=&quot;70&quot; y=&quot;%6&quot; font-size=&quot;10&quot; fill=&quot;white&quot;&gt;%4&lt;/text&gt;</span>
<span class="s">&lt;!-- RECORDS --&gt;</span>
<span class="s">&lt;/svg&gt;</span>
<span class="s">FIN</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/html&quot;</span>
<span class="nb">echo</span>
mojihame -lRECORDS <span class="nv">$tmp</span>-svg <span class="nv">$tmp</span>-sar

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　このスクリプトは説明すべき点がいくつもあります。
まず、4行目の <tt class="docutils literal"><span class="pre">PATH</span></tt> の設定は、
標準的でないコマンド
（脚注：この場合はOpen usp Tukubai。<a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a> を参考のこと）
の場所を明示的に指定するためのものです。
端末から手でシェルスクリプトと実行する場合は、
立ち上がりの際に設定ファイルからコマンドのパスが読み込まれた状態になりますが、
CGIスクリプトやcronで呼ばれるスクリプトの場合は、
明示的に指定する必要があります。</p>
<p>　そして、7,8行目は、POSTされたデータを読み込む処理です。
POSTは、前回行ったGETメソッドと同じくクライアント
（ブラウザ）側からCGIスクリプトにデータを送り込む処理です。
GETの場合は <tt class="docutils literal"><span class="pre">QUERY_STRING</span></tt> という変数にデータがセットされますが、
POSTではapacheがCGIスクリプトの標準入力にデータを突っ込んでくるので、
それを <tt class="docutils literal"><span class="pre">dd</span></tt> コマンドで吸い出します。
<tt class="docutils literal"><span class="pre">dd</span></tt> は、HDDのイメージを吸い出したりするあの <tt class="docutils literal"><span class="pre">dd</span></tt> です。
標準入力なのでもっと簡単な方法もありそうですが、
筆者がUSP研究所に入社したときはすでにこの方法が確立されていたので、
他を試していません。</p>
<p>　 <tt class="docutils literal"><span class="pre">dd</span></tt> から出たデータは、これも弊社ではお約束ですが、Open usp Tukubaiの
<tt class="docutils literal"><span class="pre">cgi-name</span></tt> というコマンドに通してそのままファイルに出力します。
<tt class="docutils literal"><span class="pre">cgi-name</span></tt> の動きをリスト7に示します。
HTMLのフォームからPOSTされたデータは、
このリストの <tt class="docutils literal"><span class="pre">echo</span></tt> のオプションのような文字列でやって来るのですが、
それをコマンドなどでさばきやすいようにキーバリュー式のテキストに変換します。
エンコードされた日本語等も変換してくれます。</p>
<ul class="simple">
<li>リスト7: <tt class="docutils literal"><span class="pre">cgi-name</span></tt> の動作</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;host=ueda@www.usptomo.com&amp;port=12345&#39;</span> | cgi-name
host ueda@www.usptomo.com
port 12345
</pre></div>
</td></tr></table></div>
<p>　10,11行目は、変数 <tt class="docutils literal"><span class="pre">host,</span> <span class="pre">port</span></tt> にそれぞれホスト、
ポート番号を代入する処理です。 <tt class="docutils literal"><span class="pre">nameread</span></tt> も Open usp Tukubai
のコマンドで、ファイルから、指定したキーの値を取るものです。
このとき、 <tt class="docutils literal"><span class="pre">host,post</span></tt> に変な（攻撃用の）データが代入されるかもしれません。
後ろの <tt class="docutils literal"><span class="pre">ssh</span></tt> のオプションに指定するときは、
必ずクオートしておきましょう。</p>
<p>　13〜19行目は、監視対象のLinuxホストからロードアベレージ
を取得して、SVGに埋め込む文字列を作っています。
<tt class="docutils literal"><span class="pre">sar</span> <span class="pre">-q</span></tt> の出力は、リスト8のようなものです。
この出力から余計なヘッダを除去し、
<tt class="docutils literal"><span class="pre">ldavg-1</span></tt> というフィールドを取得して、リスト9のように、
グラフを描くために必要な縦軸、横軸、その他座標を出力します。
<tt class="docutils literal"><span class="pre">tail</span> <span class="pre">-r</span></tt> はファイルの上下を逆さにするコマンドで、
Linuxの <tt class="docutils literal"><span class="pre">tac</span></tt> と等価です。</p>
<ul class="simple">
<li>リスト8: <tt class="docutils literal"><span class="pre">sar</span></tt> の出力</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ssh www.usptomo.com -p 12345 <span class="s1">&#39;LANG=C sar -q&#39;</span> | head -n 7
Linux 2.6.32-279.19.1.el6.x86_64 <span class="o">(</span>略<span class="o">)</span>

00:00:01 runq-sz plist-sz ldavg-1 ldavg-5 ldavg-15
00:10:01 1 136 1.26 1.10 0.58
00:20:01 0 132 0.02 0.32 0.45
00:30:01 0 133 0.08 0.06 0.23
00:40:01 0 131 0.00 0.00 0.10
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>リスト9: <tt class="docutils literal"><span class="pre">$tmp-sar</span></tt> に溜まるデータ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>40 14時00分 12 0.12 27 39
60 13時50分 0 0.00 47 59
80 13時40分 3 0.03 67 79
...
</pre></div>
</td></tr></table></div>
<p>　あとはSVGを作ってHTTPヘッダをつけて標準出力に出すだけです。
Open usp Tukubaiの <tt class="docutils literal"><span class="pre">mojihame</span></tt> コマンドで、
<tt class="docutils literal"><span class="pre">$tmp-svg</span></tt> にリスト6のデータを繰り返しはめ込んでいき、
グラフのSVGを作ります。これはずいぶん昔、
第4回で扱ったテーマなので繰り返し説明することはやめておきますが、
とにかく絵を描くためのHTML片を出力しているんだと納得し、
先にお進み下さい。</p>
<p>　次はHTML側・・・と行きたいのですが、
<tt class="docutils literal"><span class="pre">ssh</span></tt> で鍵認証を使うのでその設定をしなければなりません。
<tt class="docutils literal"><span class="pre">_www</span></tt> ユーザで <tt class="docutils literal"><span class="pre">ueda&#64;www.usptomo.com</span></tt>
に接続したいのですが、
Macの場合は <tt class="docutils literal"><span class="pre">/Library/WebServer/.ssh/</span></tt>
下に鍵一式を置けばよいようです。
私は自分の鍵を流用するためにリスト10のような横着をしましたが、
まともにやるならrootになって鍵を作って接続先のサーバにセットしましょう。
所有者とパーミッションに注意。</p>
<ul class="simple">
<li>リスト10: ueda アカウントの鍵を _www アカウントに移す</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>bash-3.2# <span class="nb">cd</span> /Library/WebServer/
bash-3.2# rsync -a /Users/ueda/.ssh/ .ssh/
bash-3.2# chown _www:_www .ssh/
bash-3.2# chown _www:_www .ssh/*
</pre></div>
</td></tr></table></div>
<p>　これでHTML側の話に移れます。
HTML側では、複数のホストに対して <tt class="docutils literal"><span class="pre">ldavg.cgi</span></tt>
を実行し、グラフを描くようにコーディングします。
リスト11にコードを示します。
これで複数のサーバの状態を一目で監視するウェブ画面の出来上がりです。
Ajaxは面倒臭いですけど非同期で使います。</p>
<ul class="simple">
<li>リスト11: <tt class="docutils literal"><span class="pre">ldavg.html</span></tt></li>
</ul>
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
35</pre></div></td><td class="code"><div class="highlight"><pre>&lt;!DOCTYPE html&gt;
&lt;html <span class="nv">lang</span><span class="o">=</span><span class="s2">&quot;ja&quot;</span>&gt;
 &lt;head&gt;
 &lt;meta <span class="nv">charset</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span> /&gt;
 &lt;script&gt;
 var <span class="nv">hosts</span> <span class="o">=</span> <span class="o">[</span><span class="s2">&quot;host=ueda@www.usptomo.com&amp;port=12345&quot;</span>,
 <span class="s2">&quot;host=ueda@araibo.is-a-geek.com&amp;port=12345&quot;</span><span class="o">]</span>;

 <span class="k">function </span>check<span class="o">(){</span>
 ldavg<span class="o">(</span>0,<span class="s2">&quot;graph0&quot;</span><span class="o">)</span>;
 ldavg<span class="o">(</span>1,<span class="s2">&quot;graph1&quot;</span><span class="o">)</span>;
 <span class="o">}</span>

 <span class="k">function </span>ldavg<span class="o">(</span>hostno,target<span class="o">){</span>
 var <span class="nv">h</span> <span class="o">=</span> new XMLHttpRequest<span class="o">()</span>;
 h.onreadystatechange <span class="o">=</span> <span class="k">function</span><span class="o">(){</span>
 <span class="k">if</span><span class="o">(</span>h.readyState !<span class="o">=</span> 4 <span class="o">||</span> h.status !<span class="o">=</span> 200<span class="o">)</span>
 <span class="k">return</span>;

 document.getElementById<span class="o">(</span>target<span class="o">)</span>.innerHTML <span class="o">=</span> h.responseText;
 <span class="o">}</span>

 h.open<span class="o">(</span><span class="s2">&quot;POST&quot;</span>,<span class="s2">&quot;/cgi-bin/ldavg.cgi&quot;</span>,true<span class="o">)</span>;
 h.setRequestHeader<span class="o">(</span><span class="s2">&quot;Content-Type&quot;</span>,
 <span class="s2">&quot;application/x-www-form-urlencoded&quot;</span><span class="o">)</span>;
 h.send<span class="o">(</span> <span class="s2">&quot;d=&quot;</span> + Math.random<span class="o">()</span> + <span class="s2">&quot;&amp;&quot;</span> + hosts<span class="o">[</span>hostno<span class="o">])</span>;
 <span class="o">}</span>

 &lt;/script&gt;
 &lt;/head&gt;
 &lt;body <span class="nv">onload</span><span class="o">=</span><span class="s2">&quot;check();setInterval(&#39;check()&#39;,60000)&quot;</span>&gt;
 &lt;div <span class="nv">id</span><span class="o">=</span><span class="s2">&quot;graph0&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;height:600px;width:350px;float:left&quot;</span>&gt;&lt;/div&gt;
 &lt;div <span class="nv">id</span><span class="o">=</span><span class="s2">&quot;graph1&quot;</span> <span class="nv">style</span><span class="o">=</span><span class="s2">&quot;height:600px;width:350px;float:left&quot;</span>&gt;&lt;/div&gt;
 &lt;/body&gt;
&lt;/html&gt;
</pre></div>
</td></tr></table></div>
<p>　このコードは、リスト3をもとにして作ったものです。
31行目の <tt class="docutils literal"><span class="pre">&lt;body</span> <span class="pre">onload=...</span></tt> で、
ページが読み込まれたときに <tt class="docutils literal"><span class="pre">check</span></tt>
という関数を呼び出し、あとは60秒ごとに <tt class="docutils literal"><span class="pre">check</span></tt>
を繰り返し呼びます。
<tt class="docutils literal"><span class="pre">check</span></tt> 関数では、監視対象のホストを指定して
<tt class="docutils literal"><span class="pre">ldavg</span></tt> 関数を呼び出しています。</p>
<p>　これで <tt class="docutils literal"><span class="pre">ldavg.html</span></tt> をブラウザに表示すると図2
のようにグラフが表示され、
1分毎（ <tt class="docutils literal"><span class="pre">sar</span></tt> のデータ自体は10分毎）に再描画されます。</p>
<ul class="simple">
<li>図2: 完成した画面</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="LDAVG.png"><img alt="" src="LDAVG.png" style="width: 80%;" /></a>
</div>
</div>
<div class="section" id="id5">
<h2>21.5. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はCGIの最終回ということで、
シェルスクリプトでAjaxというお題に挑戦しました。
今回紹介した方法でできないことというのはそんなにないので、
きれいにウェブページをデザインすれば、
まさか後ろがシェルスクリプトだとは
思わないようなサイトが作れることでしょう。</p>
<p>・・・案外、そういうサイトは多いのかもしれませんよ。</p>
<p>　次回は、原稿やメモ書きなどの、
文章を扱うというお題を扱います。</p>
</div>
</div>
