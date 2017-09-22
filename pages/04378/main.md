---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年6月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典：USP magazine 2014年6月号

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4904807081" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>


<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a>

<h1>3. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1>
<div class="section" id="id1">
<h2>3.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　皆さん、酒飲んだくれてますか？
富山の生んだブラックエンジェル（脚注: 略すと富山ブラック）上田です。</p>
</div>
<div class="section" id="id2">
<h2>3.2. 今回の問題: シェル芸勉強会第1回2問目<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　・・・と、挨拶の後、
別に面白いことも思い浮かばなかったのでさっさと本題に行きます。
今日からは第三回にしてやっと2問目です
（脚注: 遅い。）。</p>
<blockquote>
<div>/etc/passwd から、次を調べてください。
「ログインシェルがbashのユーザとshのユーザ、どっちが多い？」</div></blockquote>
<p>　たぶん私がこんな問題を出されたら、解答はこうです。</p>
<blockquote>
<div>知るかボケ</div></blockquote>
<p>・・・すんません
（大学受験で出題された400字作文でこんな解答をして
浪人の遠因となった過去が。）。
真面目にやります。やりません。いや、やりますやります。</p>
<p>　事前準備として、次のようにcabalというツールで
splitというパッケージをインストールしておきます。
root権限でやりましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sudo cabal install split
</pre></div>
</td></tr></table></div>
<p>cabalがインストールされていない場合は、
第一回でもやりましたが、
次のようにインストールします。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###Ubuntu###</span>
ueda\@ubuntu:~<span class="nv">$ </span>sudo apt-get install haskell-platform
<span class="c">###Mac###</span>
uedamac:~ ueda<span class="nv">$ </span>brew install haskell-platform
</pre></div>
</td></tr></table></div>
<p>　また、入力する <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> はLinuxのものを想定しています。
（脚注: Macでやってもよいのですが、
なーんか <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt>
がぐちゃぐちゃでよく分からないんですよね・・・。）</p>
</div>
<div class="section" id="etc-password">
<h2>3.3. 手始め: <tt class="docutils literal"><span class="pre">/etc/password</span></tt> の最後のフィールドを取得<a class="headerlink" href="#etc-password" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>まず <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> から、
集計に必要な部分だけ取得することにしましょう。
シェル芸なら図1のような感じですね。</p>
<ul class="simple">
<li>図1: シェル芸でシェルのリストを作る</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk -F: <span class="s1">&#39;{print $NF}&#39;</span> /etc/passwd | head
/bin/bash
/bin/sh
/bin/sh
/bin/sh
...
</pre></div>
</td></tr></table></div>
<p>　さて、対応するHaskellのコードは図2のようになります。</p>
<ul class="simple">
<li>図2: q1_2_1.hs</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_1</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">Data.List.Split</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span>

<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>

<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span>
</pre></div>
</td></tr></table></div>
<p>　関数は三つです。
4行目の <tt class="docutils literal"><span class="pre">main</span></tt> 関数は前回の問題でも出てきましたが、
標準入力から字を読み込んで標準出力に加工した字を出す関数です。</p>
<p>　6,7行目の関数の説明はすっ飛ばして先に
9,10行目をやっつけましょう。
この関数は、 <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> の一行を入力に受け付けます。
受け付ける文字列は、例えば</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>ueda:x:1000:1000:Ryuichi Ueda,,,:/home/ueda:/bin/bash
</pre></div>
</td></tr></table></div>
<p>のようなもので、この関数は、
コロン区切りの最後のデータ
<tt class="docutils literal"><span class="pre">/bin/bash</span></tt> を返します。
ちょっと <tt class="docutils literal"><span class="pre">ghci</span></tt> でやってみましょう。
図3のようになります。</p>
<ul class="simple">
<li>図3: 関数が無いと叱られる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghci
GHCi, version 7.4.1: http://www.haskell.org/ghc/ :? <span class="k">for </span><span class="nb">help</span>
（略）
Prelude&gt; <span class="nb">let </span>getShell <span class="nv">ln</span> <span class="o">=</span> last <span class="nv">$ </span>splitOn <span class="s2">&quot;:&quot;</span> ln

&lt;interactive&gt;:2:26:
 Not in scope: <span class="sb">`</span>splitOn<span class="s1">&#39;</span>
<span class="s1"> Perhaps you meant `splitAt&#39;</span> <span class="o">(</span>imported from Prelude<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>・・・なんか怒られてしまいました。
ちゃんと読むと（脚注: ちゃんと読みましょう。）
「 <tt class="docutils literal"><span class="pre">splitOn</span></tt> なんて関数ねえぞ！」
と言っています。</p>
<p>　これを解消する鍵は <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> のコードの1行目にあります。</p>
<div class="highlight-hs"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">Data.List.Split</span>
</pre></div>
</div>
<p>とありますが、これは <tt class="docutils literal"><span class="pre">Data.List.Split</span></tt>
という「モジュール」をインポート、つまり使うという意味になります。
先ほど <tt class="docutils literal"><span class="pre">cabal</span></tt> でインストールしたのがこのモジュールに対応する
パッケージです。中身は関数だらけです。</p>
<p>さて、これを知った上でもう一度 <tt class="docutils literal"><span class="pre">ghci</span></tt>
で図4のように試してみましょう。</p>
<ul class="simple">
<li>図4: 適切なモジュールをimportすると起こられない</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="nn">Data.List.Split</span>
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="kr">let</span> <span class="n">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span>
<span class="kt">Loading</span> <span class="n">package</span> <span class="n">split</span><span class="o">-</span><span class="mf">0.2</span><span class="o">.</span><span class="mi">2</span> <span class="o">...</span> <span class="n">linking</span> <span class="o">...</span> <span class="n">done</span><span class="o">.</span>
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">getShell</span> <span class="s">&quot;aaa:bbb:ccc&quot;</span>
<span class="s">&quot;ccc&quot;</span>
</pre></div>
</td></tr></table></div>
<p>うまくいきました。</p>
<p>　 <tt class="docutils literal"><span class="pre">getShell</span></tt> の中身について説明すると、
<tt class="docutils literal"><span class="pre">splitOn</span></tt> が、指定した文字列で文字列を切ってリスト化する関数です。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">splitOn</span> <span class="s">&quot;aho&quot;</span> <span class="s">&quot;thisahothataho&quot;</span>
<span class="p">[</span><span class="s">&quot;this&quot;</span><span class="p">,</span><span class="s">&quot;that&quot;</span><span class="p">,</span><span class="s">&quot;&quot;</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">last</span></tt> は、リストの最後の要素を返します。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">last</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span>
<span class="mi">3</span>
</pre></div>
</td></tr></table></div>
<p>　では、6,7行目の説明を。
6,7行目は、標準入力から読み込まれた字を
行ごとに分割してリストにして
（ <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> の部分）、
<tt class="docutils literal"><span class="pre">map</span></tt> で各行に <tt class="docutils literal"><span class="pre">getShell</span></tt> を適用して、
<tt class="docutils literal"><span class="pre">map</span></tt> の返した文字列のリストを <tt class="docutils literal"><span class="pre">unlines</span></tt>
で改行を入れてリストをくっつけて返しています。</p>
<p>　これも <tt class="docutils literal"><span class="pre">ghci</span></tt> で試せばよいですね。
図5のようにやってみましょう。
便利ですね〜。
<tt class="docutils literal"><span class="pre">ghci</span></tt> で改行を指定するときは、
<tt class="docutils literal"><span class="pre">\\n</span></tt> と書いておけば大丈夫です。</p>
<ul class="simple">
<li>図5: ghciで <tt class="docutils literal"><span class="pre">main'</span></tt> を試す</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="kr">let</span> <span class="n">cs</span> <span class="ow">=</span> <span class="s">&quot;aa:bb</span><span class="se">\\n</span><span class="s">cc:dd&quot;</span>
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">lines</span> <span class="n">cs</span>
<span class="p">[</span><span class="s">&quot;aa:bb&quot;</span><span class="p">,</span><span class="s">&quot;cc:dd&quot;</span><span class="p">]</span>
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>
<span class="p">[</span><span class="s">&quot;bb&quot;</span><span class="p">,</span><span class="s">&quot;dd&quot;</span><span class="p">]</span>
<span class="kt">Prelude</span> <span class="kt">Data</span><span class="o">.</span><span class="kt">List</span><span class="o">.</span><span class="kt">Split</span><span class="o">&gt;</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>
<span class="s">&quot;bb</span><span class="se">\\n</span><span class="s">dd</span><span class="se">\\n</span><span class="s">&quot;</span>
</pre></div>
</td></tr></table></div>
<p>このような、関数を組み合わせるプロセスは
シェル芸にも通じるところがあります。
入出力だけ考えるという点で、
関数型言語とシェル芸は通じるところがあります。</p>
<p>　 <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> をコンパイルして
図6のように出力を見ておきましょう。</p>
<ul class="simple">
<li>図6: <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> の使用</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_1</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sync</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span>
<span class="o">...</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id3">
<h2>3.4. さて、数えましょう<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="undefined">
<h3>3.4.1. 関数を新設して <tt class="docutils literal"><span class="pre">undefined</span></tt> で型チェック<a class="headerlink" href="#undefined" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>では、今度は数える部分を書きましょう。
先ほどの <tt class="docutils literal"><span class="pre">q1_2_1.hs</span></tt> は <tt class="docutils literal"><span class="pre">map</span> <span class="pre">getShell</span> <span class="pre">(lines</span> <span class="pre">cs)</span></tt>
の出力を <tt class="docutils literal"><span class="pre">unlines</span></tt> してそのまま出力していましたが、
この <tt class="docutils literal"><span class="pre">unlines</span></tt> に入力する前に
シェルの種類を数える関数を挟めばよいことになります。
まず、この考えをそのままコードにします。
図7のように書きました。</p>
<ul class="simple">
<li>図7: <tt class="docutils literal"><span class="pre">q1_2_2.hs</span></tt></li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
13</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_2</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">Data.List.Split</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span>

<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>

<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span>

<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span>
<span class="nf">shellCount</span> <span class="ow">=</span> <span class="n">undefined</span>
</pre></div>
</td></tr></table></div>
<p>7行目の <tt class="docutils literal"><span class="pre">unlines</span></tt> の後ろ（脚注: 処理的には手前）
に <tt class="docutils literal"><span class="pre">shellCount</span></tt> という関数をはさんで、
<tt class="docutils literal"><span class="pre">shellCount</span></tt> という関数を12,13行目で定義しています。
・・・といっても、13行目に <tt class="docutils literal"><span class="pre">undefined</span></tt>
とあるように、まだ定義していません。</p>
<p>　何でこんなことをするかというと、
コンパイラにかけるためで、
<tt class="docutils literal"><span class="pre">undefined</span></tt> と書いておくと</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_2_2.hs
<span class="o">[</span>1 of 1<span class="o">]</span> Compiling Main <span class="o">(</span> q1_2_2.hs, q1_2_2.o <span class="o">)</span>
Linking q1_2_2 ...
</pre></div>
</td></tr></table></div>
<p>というように通ります。
当然実行時にエラーが出ますが。
ただ、こうやってコンパイラに通すと
型をチェックすることができます。
そのため、わざわざ <tt class="docutils literal"><span class="pre">undefined</span></tt>
と書いてコンパイルしてみたのでした。</p>
</div>
<div class="section" id="shellcount">
<h3>3.4.2. <tt class="docutils literal"><span class="pre">shellCount</span></tt> を実装（前半）<a class="headerlink" href="#shellcount" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、 <tt class="docutils literal"><span class="pre">shellCount</span></tt> を書いたものを示します。
・・・と言いたいところなのですが、
思ってたよりややこしかったのでまた途中までのコードを
図8に示します。</p>
<ul class="simple">
<li>図8: <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt></li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">Data.List</span>
<span class="kr">import</span> <span class="nn">Data.List.Split</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span>

<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>

<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span>

<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span>
<span class="nf">shellCount</span> <span class="n">shs</span> <span class="ow">=</span> <span class="n">map</span> <span class="n">f</span> <span class="o">$</span> <span class="n">shellCount&#39;</span> <span class="p">[</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">s</span><span class="p">)</span> <span class="o">|</span> <span class="n">s</span> <span class="ow">&lt;-</span> <span class="p">(</span><span class="n">sort</span> <span class="n">shs</span><span class="p">)</span> <span class="p">]</span>
 <span class="kr">where</span> <span class="n">f</span> <span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="n">str</span><span class="p">)</span> <span class="ow">=</span> <span class="n">unwords</span> <span class="p">[</span><span class="n">show</span> <span class="n">n</span><span class="p">,</span><span class="n">str</span><span class="p">]</span>

<span class="nf">shellCount&#39;</span> <span class="ow">::</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">String</span><span class="p">)]</span> <span class="ow">-&gt;</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">String</span><span class="p">)]</span>
<span class="nf">shellCount&#39;</span> <span class="n">shs</span> <span class="ow">=</span> <span class="n">shs</span>
</pre></div>
</td></tr></table></div>
<p>　このコードをコンパイルして実行すると
図9のようになります。</p>
<ul class="simple">
<li>図9: <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコンパイル</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">ghc</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span>
<span class="p">[</span><span class="mi">1</span> <span class="kr">of</span> <span class="mi">1</span><span class="p">]</span> <span class="kt">Compiling</span> <span class="kt">Main</span> <span class="p">(</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">hs</span><span class="p">,</span> <span class="n">q1_2_3</span><span class="o">.</span><span class="n">o</span> <span class="p">)</span>
<span class="kt">Linking</span> <span class="n">q1_2_3</span> <span class="o">...</span>
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_3</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span>
<span class="mi">1</span> <span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span>
<span class="o">...</span>
</pre></div>
</td></tr></table></div>
<p>つまり、シェルのパスに個数をくっつけたデータになりました。
シェルの名前はソート済みですので、あとは例えば
Open usp Tukubaiを使って
図10のようにやれば答えが出てきてしまうのですが
（脚注: ああ・・・答えを書いてしまった・・・。）、
もうちょっとHaskellで辛抱しましょう・・・。</p>
<ul class="simple">
<li>図10: <tt class="docutils literal"><span class="pre">q1_2_3</span></tt> からTukubaiを使って答えを出す</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">passwd</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_2_3</span> <span class="o">|</span>
 <span class="n">self</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">|</span> <span class="n">sm2</span> <span class="mi">1</span> <span class="mi">1</span> <span class="mi">2</span> <span class="mi">2</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">bash</span> <span class="mi">2</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">false</span> <span class="mi">4</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sh</span> <span class="mi">17</span>
<span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">sync</span> <span class="mi">1</span>
<span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">sbin</span><span class="o">/</span><span class="n">nologin</span> <span class="mi">1</span>
</pre></div>
</td></tr></table></div>
<p>　さて、 <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコードを読んでいきます。
まず、17,18行目の <tt class="docutils literal"><span class="pre">shellCount'</span></tt> は、
今のところ入力をそのまま出力しています。
この関数の実装は後回しにします。
同じ型のものを返す関数を仮に書くときは <tt class="docutils literal"><span class="pre">undefined</span></tt>
よりもこのように同じものを返しておいた方が
デバッグに便利です。
17行目にあるように、この関数の型は</p>
<div class="highlight-bash"><div class="highlight"><pre>shellCount&#39; :: [(Int,String)] -&gt; [(Int,String)]
</pre></div>
</div>
<p>です。 <tt class="docutils literal"><span class="pre">(a,b)</span></tt> （ここではa,bはそれぞれIntとString）
というものがありますが、
これは「タプル」というもので、
二つの型の値を組み合わせるときに使います。
ですのでこの関数の型は
「IntとStringのタプルのリストを入出力する」
ということになります。</p>
<p>　んで、今回作ったメインのものは13〜15行目の
<tt class="docutils literal"><span class="pre">shellCount</span></tt> です。ここには新しい書き方が二つも！</p>
<p>　まず、15行目の <tt class="docutils literal"><span class="pre">where</span></tt> ですが、
<tt class="docutils literal"><span class="pre">where</span></tt> と書くと、関数の中で関数を定義できます。
ここで定義しているのは関数 <tt class="docutils literal"><span class="pre">f</span></tt> で、
こいつは何をやっているかというと、
数字（Int）と文字列（String）のタプルを入力にもらって、
数字を文字列化し、文字列とくっつけて出力しています。
<tt class="docutils literal"><span class="pre">ghci</span></tt> で等価なコードを試してみましょう。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; [show 5,&quot;abcde&quot;] &lt;- 5がfの引数のn, &quot;abcde&quot;がstrに相当
[&quot;5&quot;,&quot;abcde&quot;]
Prelude&gt; unwords [show 5,&quot;abcde&quot;]
&quot;5 abcde&quot;
</pre></div>
</td></tr></table></div>
<p>　次に <tt class="docutils literal"><span class="pre">[</span></tt> と <tt class="docutils literal"><span class="pre">]</span></tt> で囲まれた部分ですが、
これはリスト内包というものです。
これもクドクド説明するより例で示した方がいいですね。
例えば下の例だと、リスト <tt class="docutils literal"><span class="pre">[1,2,3]</span></tt>
から一つずつ要素を <tt class="docutils literal"><span class="pre">x</span></tt> に結びつけて、
それに一つずつ2を足してリストにします。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="p">[</span> <span class="n">x</span><span class="o">+</span><span class="mi">2</span> <span class="o">|</span> <span class="n">x</span> <span class="ow">&lt;-</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span> <span class="p">]</span>
<span class="p">[</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>実は、次の <tt class="docutils literal"><span class="pre">map</span></tt> を使った例と等価です。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">map</span> <span class="p">(</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span>
<span class="p">[</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>んで、 <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> のコードでは、
タプルを作るためにリスト内包を使っています。
具体例を下に示します。
例の中で <tt class="docutils literal"><span class="pre">sort</span></tt> も使ってみます。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import Data.List &lt;- sortを使うためにimport
Prelude Data.List&gt; [ (1,s) | s &lt;- (sort [&quot;bbb&quot;,&quot;aaa&quot;,&quot;ccc&quot;] ) ]
[(1,&quot;aaa&quot;),(1,&quot;bbb&quot;),(1,&quot;ccc&quot;)]
</pre></div>
</td></tr></table></div>
<p>　さあ、最後に <tt class="docutils literal"><span class="pre">shellCount'</span></tt> を実装します。
今のところタプルの数字、つまり個数はすべて「1」
で出力していますが、これを同じシェルでまとめていきます。</p>
<p>　さて次を・・・というところですが、
紙面がもうございません。
今月はこれでお開きにしたいと思います。</p>
</div>
</div>
<div class="section" id="id4">
<h2>3.5. おわりに<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はシェル芸勉強会第1回の2問目を扱いました。
本編ではあまり言及しませんでしたが、
今回は問題を関数に分けていくプロセスが随所で見られました。
Haskellのコードを書くときは、このように
頭を整理してどこで関数を分けることができるのか、
探りながら書いていくことになります。
実はこれ、どんな言語でも通用する発想方法ですので、
何の言語を使うにせよよいトレーニングになるかと。
つまりはHaskellやれということで、
今回を締めさせていただきます。</p>
<p>　次回は続きからということで、
まーた途中になっちまいましたが、
来月まで辛抱強くお待ちいただければ・・・と。</p>
</div>
