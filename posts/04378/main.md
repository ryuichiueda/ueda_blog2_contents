# USP Magazine 2014年6月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典：USP magazine 2014年6月号<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4904807081" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
<br />
<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a><br />
<br />
<h1>3. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1><br />
<div class="section" id="id1"><br />
<h2>3.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　皆さん、酒飲んだくれてますか？<br />
富山の生んだブラックエンジェル（脚注: 略すと富山ブラック）上田です。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>3.2. 今回の問題: シェル芸勉強会第1回2問目<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　・・・と、挨拶の後、<br />
別に面白いことも思い浮かばなかったのでさっさと本題に行きます。<br />
今日からは第三回にしてやっと2問目です<br />
（脚注: 遅い。）。</p><br />
<blockquote><br />
<div>/etc/passwd から、次を調べてください。<br />
「ログインシェルがbashのユーザとshのユーザ、どっちが多い？」</div></blockquote><br />
<p>　たぶん私がこんな問題を出されたら、解答はこうです。</p><br />
<blockquote><br />
<div>知るかボケ</div></blockquote><br />
<p>・・・すんません<br />
（大学受験で出題された400字作文でこんな解答をして<br />
浪人の遠因となった過去が。）。<br />
真面目にやります。やりません。いや、やりますやります。</p><br />
<p>　事前準備として、次のようにcabalというツールで<br />
splitというパッケージをインストールしておきます。<br />
root権限でやりましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sudo cabal install split<br />
</pre></div><br />
</td></tr></table></div><br />
<p>cabalがインストールされていない場合は、<br />
第一回でもやりましたが、<br />
次のようにインストールします。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###Ubuntu###</span><br />
ueda\@ubuntu:~<span class="nv">$ </span>sudo apt-get install haskell-platform<br />
<span class="c">###Mac###</span><br />
uedamac:~ ueda<span class="nv">$ </span>brew install haskell-platform<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　また、入力する <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> はLinuxのものを想定しています。<br />
（脚注: Macでやってもよいのですが、<br />
なーんか <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt><br />
がぐちゃぐちゃでよく分からないんですよね・・・。）</p><br />
</div><br />
<div class="section" id="etc-password"><br />
<h2>3.3. 手始め: <tt class="docutils literal"><span class="pre">/etc/password</span></tt> の最後のフィールドを取得<a class="headerlink" href="#etc-password" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>まず <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> から、<br />
集計に必要な部分だけ取得することにしましょう。<br />
シェル芸なら図1のような感じですね。</p><br />
<ul class="simple"><br />
<li>図1: シェル芸でシェルのリストを作る</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk -F: <span class="s1">&#39;{print $NF}&#39;</span> /etc/passwd | head<br />
/bin/bash<br />
/bin/sh<br />
/bin/sh<br />
/bin/sh<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、対応するHaskellのコードは図2のようになります。</p><br />
<ul class="simple"><br />
<li>図2: q1_2_1.hs</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_1</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span><br />
<br />
<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<br />
<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　関数は三つです。<br />
4行目の <tt class="docutils literal"><span class="pre">main</span></tt> 関数は前回の問題でも出てきましたが、<br />
標準入力から字を読み込んで標準出力に加工した字を出す関数です。</p><br />
<p>　6,7行目の関数の説明はすっ飛ばして先に<br />
9,10行目をやっつけましょう。<br />
この関数は、 <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> の一行を入力に受け付けます。<br />
受け付ける文字列は、例えば</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>ueda:x:1000:1000:Ryuichi Ueda,,,:/home/ueda:/bin/bash<br />
</pre></div><br />
</td></tr></table></div><br />
<p>のようなもので、この関数は、<br />
コロン区切りの最後のデータ<br />
<tt class="docutils literal"><span class="pre">/bin/bash</span></tt> を返します。<br />
ちょっと <tt class="docutils literal"><span class="pre">ghci</span></tt> でやってみましょう。<br />
図3のようになります。</p><br />
<ul class="simple"><br />
<li>図3: 関数が無いと叱られる</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghci<br />
GHCi, version 7.4.1: http://www.haskell.org/ghc/ :? <span class="k">for </span><span class="nb">help</span><br />
（略）<br />
Prelude&gt; <span class="nb">let </span>getShell <span class="nv">ln</span> <span class="o">=</span> last <span class="nv">$ </span>splitOn <span class="s2">&quot;:&quot;</span> ln<br />
<br />
&lt;interactive&gt;:2:26:<br />
 Not in scope: <span class="sb">`</span>splitOn<span class="s1">&#39;</span><br />
<span class="s1"> Perhaps you meant `splitAt&#39;</span> <span class="o">(</span>imported from Prelude<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>・・・なんか怒られてしまいました。<br />
ちゃんと読むと（脚注: ちゃんと読みましょう。）<br />
「 <tt class="docutils literal"><span class="pre">splitOn</span></tt> なんて関数ねえぞ！」<br />
と言っています。</p><br />
<p>　これを解消する鍵は <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> のコードの1行目にあります。</p><br />
<div class="highlight-hs"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
</pre></div><br />
</div><br />
<p>とありますが、これは <tt class="docutils literal"><span class="pre">Data.List.Split</span></tt><br />
という「モジュール」をインポート、つまり使うという意味になります。<br />
先ほど <tt class="docutils literal"><span class="pre">cabal</span></tt> でインストールしたのがこのモジュールに対応する<br />
パッケージです。中身は関数だらけです。</p><br />
<p>さて、これを知った上でもう一度 <tt class="docutils literal"><span class="pre">ghci</span></tt><br />
で図4のように試してみましょう。</p><br />
<ul class="simple"><br />
<li>図4: 適切なモジュールをimportすると起こられない</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="kr">let</span> <span class="n">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span><br />
<span class="kt">Loading</span> <span class="n">package</span> <span class="n">split</span><span class="o">-</span><span class="mf">0.2</span><span class="o">.</span><span class="mi">2</span> <span class="o">...</span> <span class="n">linking</span> <span class="o">...</span> <span class="n">done</span><span class="o">.</span><br />
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">getShell</span> <span class="s">&quot;aaa:bbb:ccc&quot;</span><br />
<span class="s">&quot;ccc&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>うまくいきました。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">getShell</span></tt> の中身について説明すると、<br />
<tt class="docutils literal"><span class="pre">splitOn</span></tt> が、指定した文字列で文字列を切ってリスト化する関数です。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">splitOn</span> <span class="s">&quot;aho&quot;</span> <span class="s">&quot;thisahothataho&quot;</span><br />
<span class="p">[</span><span class="s">&quot;this&quot;</span><span class="p">,</span><span class="s">&quot;that&quot;</span><span class="p">,</span><span class="s">&quot;&quot;</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">last</span></tt> は、リストの最後の要素を返します。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">last</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span><br />
<span class="mi">3</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　では、6,7行目の説明を。<br />
6,7行目は、標準入力から読み込まれた字を<br />
行ごとに分割してリストにして<br />
（ <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> の部分）、<br />
<tt class="docutils literal"><span class="pre">map</span></tt> で各行に <tt class="docutils literal"><span class="pre">getShell</span></tt> を適用して、<br />
<tt class="docutils literal"><span class="pre">map</span></tt> の返した文字列のリストを <tt class="docutils literal"><span class="pre">unlines</span></tt><br />
で改行を入れてリストをくっつけて返しています。</p><br />
<p>　これも <tt class="docutils literal"><span class="pre">ghci</span></tt> で試せばよいですね。<br />
図5のようにやってみましょう。<br />
便利ですね〜。<br />
<tt class="docutils literal"><span class="pre">ghci</span></tt> で改行を指定するときは、<br />
<tt class="docutils literal"><span class="pre">\\n</span></tt> と書いておけば大丈夫です。</p><br />
<ul class="simple"><br />
<li>図5: ghciで <tt class="docutils literal"><span class="pre">main'</span></tt> を試す</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="kr">let</span> <span class="n">cs</span> <span class="ow">=</span> <span class="s">&quot;aa:bb</span><span class="se">\\n</span><span class="s">cc:dd&quot;</span><br />
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">lines</span> <span class="n">cs</span><br />
<span class="p">[</span><span class="s">&quot;aa:bb&quot;</span><span class="p">,</span><span class="s">&quot;cc:dd&quot;</span><span class="p">]</span><br />
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<span class="p">[</span><span class="s">&quot;bb&quot;</span><span class="p">,</span><span class="s">&quot;dd&quot;</span><span class="p">]</span><br />
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<span class="s">&quot;bb</span><span class="se">\\n</span><span class="s">dd</span><span class="se">\\n</span><span class="s">&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>このような、関数を組み合わせるプロセスは<br />
シェル芸にも通じるところがあります。<br />
入出力だけ考えるという点で、<br />
関数型言語とシェル芸は通じるところがあります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> をコンパイルして<br />
図6のように出力を見ておきましょう。</p><br />
<ul class="simple"><br />
<li>図6: <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> の使用</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_1</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sync</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span><br />
<span class="o">...</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id3"><br />
<h2>3.4. さて、数えましょう<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="undefined"><br />
<h3>3.4.1. 関数を新設して <tt class="docutils literal"><span class="pre">undefined</span></tt> で型チェック<a class="headerlink" href="#undefined" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>では、今度は数える部分を書きましょう。<br />
先ほどの <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> は <tt class="docutils literal"><span class="pre">map</span> <span class="pre">getShell</span> <span class="pre">(lines</span> <span class="pre">cs)</span></tt><br />
の出力を <tt class="docutils literal"><span class="pre">unlines</span></tt> してそのまま出力していましたが、<br />
この <tt class="docutils literal"><span class="pre">unlines</span></tt> に入力する前に<br />
シェルの種類を数える関数を挟めばよいことになります。<br />
まず、この考えをそのままコードにします。<br />
図7のように書きました。</p><br />
<ul class="simple"><br />
<li>図7: <tt class="docutils literal"><span class="pre">q1_2_2.hs</span></tt></li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
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
13</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_2</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span><br />
<br />
<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<br />
<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span><br />
<br />
<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span><br />
<span class="nf">shellCount</span> <span class="ow">=</span> <span class="n">undefined</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>7行目の <tt class="docutils literal"><span class="pre">unlines</span></tt> の後ろ（脚注: 処理的には手前）<br />
に <tt class="docutils literal"><span class="pre">shellCount</span></tt> という関数をはさんで、<br />
<tt class="docutils literal"><span class="pre">shellCount</span></tt> という関数を12,13行目で定義しています。<br />
・・・といっても、13行目に <tt class="docutils literal"><span class="pre">undefined</span></tt><br />
とあるように、まだ定義していません。</p><br />
<p>　何でこんなことをするかというと、<br />
コンパイラにかけるためで、<br />
<tt class="docutils literal"><span class="pre">undefined</span></tt> と書いておくと</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_2_2.hs<br />
<span class="o">[</span>1 of 1<span class="o">]</span> Compiling Main <span class="o">(</span> q1_2_2.hs, q1_2_2.o <span class="o">)</span><br />
Linking q1_2_2 ...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>というように通ります。<br />
当然実行時にエラーが出ますが。<br />
ただ、こうやってコンパイラに通すと<br />
型をチェックすることができます。<br />
そのため、わざわざ <tt class="docutils literal"><span class="pre">undefined</span></tt><br />
と書いてコンパイルしてみたのでした。</p><br />
</div><br />
<div class="section" id="shellcount"><br />
<h3>3.4.2. <tt class="docutils literal"><span class="pre">shellCount</span></tt> を実装（前半）<a class="headerlink" href="#shellcount" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、 <tt class="docutils literal"><span class="pre">shellCount</span></tt> を書いたものを示します。<br />
・・・と言いたいところなのですが、<br />
思ってたよりややこしかったのでまた途中までのコードを<br />
図8に示します。</p><br />
<ul class="simple"><br />
<li>図8: <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt></li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">Data.List</span><br />
<span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span><br />
<br />
<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<br />
<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span><br />
<br />
<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span><br />
<span class="nf">shellCount</span> <span class="n">shs</span> <span class="ow">=</span> <span class="n">map</span> <span class="n">f</span> <span class="o">$</span> <span class="n">shellCount&#39;</span> <span class="p">[</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">s</span><span class="p">)</span> <span class="o">|</span> <span class="n">s</span> <span class="ow">&lt;-</span> <span class="p">(</span><span class="n">sort</span> <span class="n">shs</span><span class="p">)</span> <span class="p">]</span><br />
 <span class="kr">where</span> <span class="n">f</span> <span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="n">str</span><span class="p">)</span> <span class="ow">=</span> <span class="n">unwords</span> <span class="p">[</span><span class="n">show</span> <span class="n">n</span><span class="p">,</span><span class="n">str</span><span class="p">]</span><br />
<br />
<span class="nf">shellCount&#39;</span> <span class="ow">::</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">String</span><span class="p">)]</span> <span class="ow">-&gt;</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">String</span><span class="p">)]</span><br />
<span class="nf">shellCount&#39;</span> <span class="n">shs</span> <span class="ow">=</span> <span class="n">shs</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このコードをコンパイルして実行すると<br />
図9のようになります。</p><br />
<ul class="simple"><br />
<li>図9: <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコンパイル</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">ghc</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span><br />
<span class="p">[</span><span class="mi">1</span> <span class="kr">of</span> <span class="mi">1</span><span class="p">]</span> <span class="kt">Compiling</span> <span class="kt">Main</span> <span class="p">(</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span><span class="p">,</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">o</span> <span class="p">)</span><br />
<span class="kt">Linking</span> <span class="n">q1_2_3</span> <span class="o">...</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_3</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span><br />
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span><br />
<span class="o">...</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>つまり、シェルのパスに個数をくっつけたデータになりました。<br />
シェルの名前はソート済みですので、あとは例えば<br />
Open usp Tukubaiを使って<br />
図10のようにやれば答えが出てきてしまうのですが<br />
（脚注: ああ・・・答えを書いてしまった・・・。）、<br />
もうちょっとHaskellで辛抱しましょう・・・。</p><br />
<ul class="simple"><br />
<li>図10: <tt class="docutils literal"><span class="pre">q1_2_3</span></tt> からTukubaiを使って答えを出す</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_3</span> <span class="o">|</span><br />
 <span class="n">self</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">|</span> <span class="n">sm2</span> <span class="mi">1</span> <span class="mi">1</span> <span class="mi">2</span> <span class="mi">2</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span> <span class="mi">2</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span> <span class="mi">4</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span> <span class="mi">17</span><br />
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sync</span> <span class="mi">1</span><br />
<span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">sbin</span><span class="o">/</span><span class="n">nologin</span> <span class="mi">1</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、 <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコードを読んでいきます。<br />
まず、17,18行目の <tt class="docutils literal"><span class="pre">shellCount'</span></tt> は、<br />
今のところ入力をそのまま出力しています。<br />
この関数の実装は後回しにします。<br />
同じ型のものを返す関数を仮に書くときは <tt class="docutils literal"><span class="pre">undefined</span></tt><br />
よりもこのように同じものを返しておいた方が<br />
デバッグに便利です。<br />
17行目にあるように、この関数の型は</p><br />
<div class="highlight-bash"><div class="highlight"><pre>shellCount&#39; :: [(Int,String)] -&gt; [(Int,String)]<br />
</pre></div><br />
</div><br />
<p>です。 <tt class="docutils literal"><span class="pre">(a,b)</span></tt> （ここではa,bはそれぞれIntとString）<br />
というものがありますが、<br />
これは「タプル」というもので、<br />
二つの型の値を組み合わせるときに使います。<br />
ですのでこの関数の型は<br />
「IntとStringのタプルのリストを入出力する」<br />
ということになります。</p><br />
<p>　んで、今回作ったメインのものは13〜15行目の<br />
<tt class="docutils literal"><span class="pre">shellCount</span></tt> です。ここには新しい書き方が二つも！</p><br />
<p>　まず、15行目の <tt class="docutils literal"><span class="pre">where</span></tt> ですが、<br />
<tt class="docutils literal"><span class="pre">where</span></tt> と書くと、関数の中で関数を定義できます。<br />
ここで定義しているのは関数 <tt class="docutils literal"><span class="pre">f</span></tt> で、<br />
こいつは何をやっているかというと、<br />
数字（Int）と文字列（String）のタプルを入力にもらって、<br />
数字を文字列化し、文字列とくっつけて出力しています。<br />
<tt class="docutils literal"><span class="pre">ghci</span></tt> で等価なコードを試してみましょう。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; [show 5,&quot;abcde&quot;] &lt;- 5がfの引数のn, &quot;abcde&quot;がstrに相当<br />
[&quot;5&quot;,&quot;abcde&quot;]<br />
Prelude&gt; unwords [show 5,&quot;abcde&quot;]<br />
&quot;5 abcde&quot;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次に <tt class="docutils literal"><span class="pre">[</span></tt> と <tt class="docutils literal"><span class="pre">]</span></tt> で囲まれた部分ですが、<br />
これはリスト内包というものです。<br />
これもクドクド説明するより例で示した方がいいですね。<br />
例えば下の例だと、リスト <tt class="docutils literal"><span class="pre">[1,2,3]</span></tt><br />
から一つずつ要素を <tt class="docutils literal"><span class="pre">x</span></tt> に結びつけて、<br />
それに一つずつ2を足してリストにします。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="p">[</span> <span class="n">x</span><span class="o">+</span><span class="mi">2</span> <span class="o">|</span> <span class="n">x</span> <span class="ow">&lt;-</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span> <span class="p">]</span><br />
<span class="p">[</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>実は、次の <tt class="docutils literal"><span class="pre">map</span></tt> を使った例と等価です。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">map</span> <span class="p">(</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span><br />
<span class="p">[</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>んで、 <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコードでは、<br />
タプルを作るためにリスト内包を使っています。<br />
具体例を下に示します。<br />
例の中で <tt class="docutils literal"><span class="pre">sort</span></tt> も使ってみます。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import Data.List &lt;- sortを使うためにimport<br />
Prelude Data.List&gt; [ (1,s) | s &lt;- (sort [&quot;bbb&quot;,&quot;aaa&quot;,&quot;ccc&quot;] ) ]<br />
[(1,&quot;aaa&quot;),(1,&quot;bbb&quot;),(1,&quot;ccc&quot;)]<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さあ、最後に <tt class="docutils literal"><span class="pre">shellCount'</span></tt> を実装します。<br />
今のところタプルの数字、つまり個数はすべて「1」<br />
で出力していますが、これを同じシェルでまとめていきます。</p><br />
<p>　さて次を・・・というところですが、<br />
紙面がもうございません。<br />
今月はこれでお開きにしたいと思います。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>3.5. おわりに<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はシェル芸勉強会第1回の2問目を扱いました。<br />
本編ではあまり言及しませんでしたが、<br />
今回は問題を関数に分けていくプロセスが随所で見られました。<br />
Haskellのコードを書くときは、このように<br />
頭を整理してどこで関数を分けることができるのか、<br />
探りながら書いていくことになります。<br />
実はこれ、どんな言語でも通用する発想方法ですので、<br />
何の言語を使うにせよよいトレーニングになるかと。<br />
つまりはHaskellやれということで、<br />
今回を締めさせていただきます。</p><br />
<p>　次回は続きからということで、<br />
まーた途中になっちまいましたが、<br />
来月まで辛抱強くお待ちいただければ・・・と。</p><br />
</div>
