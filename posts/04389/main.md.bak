# USP Magazine 2014年7月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典: USP magazine 7月号<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=490480709X" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
<br />
<br />
<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a><br />
<br />
<h1>4. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1><br />
<div class="section" id="id2"><br />
<h2>4.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　皆さん、しらばっくれてますか？<br />
締め切り後からおもむろに書き始める、<br />
ダメな感じ満載の上田です<br />
<a class="footnote-reference" href="#aaa" id="id3">[2]</a><br />
。<br />
いやあね、もう歳で、とにかく物忘れが酷い酷い。<br />
この前なんか、<br />
自首しようと思ったのに忘れていて、<br />
家までFBIが来て大変でした<br />
<a class="footnote-reference" href="#ccc" id="id4">[3]</a><br />
。</p><br />
<p>　反省はほどほどに、はじめましょう<br />
<a class="footnote-reference" href="#bbb" id="id5">[5]</a><br />
。<br />
まず一つご報告ですが、<br />
Haskellのインストール等の情報を私のサイトにまとめました。</p><br />
<p><tt class="docutils literal"><span class="pre">http://blog.ueda.asia/?page_id=2944</span></tt></p><br />
<p>にあります。続きはWebで。面会は刑務所で。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h2>4.2. おさらい<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回からシェル芸勉強会の第1回2問目をやっちょります。<br />
環境はLinuxを想定しています。</p><br />
<blockquote><br />
<div>/etc/passwd から、次を調べてください。<br />
「ログインシェルがbashのユーザとshのユーザ、どっちが多い？」</div></blockquote><br />
<p>ほんと、しらねーよという感じですが<br />
<a class="footnote-reference" href="#ddd" id="id7">[6]</a><br />
、前回から真面目に取り組んできました。<br />
前回までで完成したコードを図1に示します。</p><br />
<ul class="simple"><br />
<li>図1: 前回の最後のコードq1_2_3.hs</li><br />
</ul><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_3.hs<br />
import Data.List<br />
import Data.List.Split<br />
<br />
<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . main<span class="s1">&#39;</span><br />
<br />
<span class="s1">main&#39;</span> :: String -&gt; String<br />
main<span class="s1">&#39; cs = unlines $ shellCount $ map getShell (lines cs)</span><br />
<br />
<span class="s1">getShell :: String -&gt; String</span><br />
<span class="s1">getShell ln = last $ splitOn &quot;:&quot; ln</span><br />
<br />
<span class="s1">shellCount :: [String] -&gt; [String]</span><br />
<span class="s1">shellCount shs = map f $ shellCount&#39;</span> <span class="o">[</span> <span class="o">(</span>1,s<span class="o">)</span> | s &lt;- <span class="o">(</span>sort shs<span class="o">)</span> <span class="o">]</span><br />
 where f <span class="o">(</span>n,str<span class="o">)</span> <span class="o">=</span> unwords <span class="o">[</span>show n,str<span class="o">]</span><br />
<br />
shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span><br />
<span class="s1">shellCount&#39;</span> <span class="nv">shs</span> <span class="o">=</span> shs<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　関数 <tt class="docutils literal"><span class="pre">shellCount'</span></tt> が今のところダミーになっています。<br />
実行すると図2のような出力が出ます。</p><br />
<ul class="simple"><br />
<li>図2: q1_2_3をexecution <a class="footnote-reference" href="#zzz" id="id8">[9]</a></li><br />
</ul><br />
<p>　おさらいついでにもう一つ補足すると、<br />
図1の <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> の15行目の<br />
<tt class="docutils literal"><span class="pre">show</span></tt> 関数は、数値等を文字列に変換する関数です。<br />
ghciで調べると、図3のような型です。</p><br />
<ul class="simple"><br />
<li>図3: showの型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t show<br />
show :: Show <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; String<br />
</pre></div><br />
</td></tr></table></div><br />
<p>ここで、 <tt class="docutils literal"><span class="pre">Show</span> <span class="pre">a</span></tt> というのは、<br />
「 <tt class="docutils literal"><span class="pre">show</span></tt> が使える任意の型」という意味です。<br />
そのような型がどのように定義されるのかは、<br />
死人が出そうなので説明をやめておきます<br />
<a class="footnote-reference" href="#ggg" id="id9">[4]</a><br />
。代わりに <tt class="docutils literal"><span class="pre">show</span></tt> の動作を図4にお見せします。</p><br />
<ul class="simple"><br />
<li>図4: showの動作</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mf">0.1</span><br />
<span class="s">&quot;0.1&quot;</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mi">1</span><br />
<span class="s">&quot;1&quot;</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mf">1e+100</span><br />
<span class="s">&quot;1.0e100&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>4.3. 開始！<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　Haskellの内部では各レコードは次のような二つの値の対になっています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span><br />
</pre></div><br />
</div><br />
<p>このような対をHaskellでは「タプル」と呼びます。<br />
この例のタプルの型は図5のような感じ。</p><br />
<ul class="simple"><br />
<li>図5: タプルの型</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="s">&quot;/bin/bash&quot;</span><span class="p">)</span><br />
<span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="s">&quot;/bin/bash&quot;</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Num</span> <span class="n">t</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="p">[</span><span class="kt">Char</span><span class="p">])</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>また、 <tt class="docutils literal"><span class="pre">show</span></tt> の型のように <tt class="docutils literal"><span class="pre">Num</span> <span class="pre">t</span> <span class="pre">=&gt;</span></tt> というのが<br />
出てきましたが、これも数字に属する任意の型 <tt class="docutils literal"><span class="pre">t</span></tt><br />
という意味になります。<br />
「1」の型が不定<br />
<a class="footnote-reference" href="#eee" id="id11">[7]</a><br />
なのでややこしい出力になってしまいましたが、<br />
要は数字と文字列のタプルです。<br />
これがリストになったものが、18行目の入力 <tt class="docutils literal"><span class="pre">shs</span></tt><br />
です。<br />
18行目の右辺で、例えば</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/sh&quot;</span><span class="o">)]</span><br />
</pre></div><br />
</div><br />
<p>とあったら</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[(</span>2,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/sh&quot;</span><span class="o">)]</span><br />
</pre></div><br />
</div><br />
<p>とまとめるコードを右辺に書きます。</p><br />
</div><br />
<div class="section" id="id12"><br />
<h2>4.4. パターンマッチで場合分け<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まとめる戦略を次のように考えます。<br />
リスト <tt class="docutils literal"><span class="pre">[a,b,c,...]</span></tt> （a,b,cがそれぞれタプル）に対して、</p><br />
<ol class="arabic simple"><br />
<li>リストの先頭二つの要素aとbを比較</li><br />
<li>aとbに入っているシェルの名前が一致: タプル中の数字を足し合わせて一つの要素にまとめる</li><br />
<li>一致しない: aをそのままにして、bとcを比較</li><br />
</ol><br />
<p>という手続きを書いていこうと思います。</p><br />
<p>　しかしその前に、<br />
じゃあリストに1個しか要素が無かったとき、<br />
あるいは0個だったときのことも考えておかないといけません。<br />
Haskellでは図6のようなコードを書きます。</p><br />
<ul class="simple"><br />
<li>図6: パターンマッチを書いたq1_2_4.hs</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC$ cat q1_2_4.hs<br />
（中略）<br />
shellCount&#39; :: [(Int,String)] -&gt; [(Int,String)]<br />
shellCount&#39; [] = []<br />
shellCount&#39; [a] = [a]<br />
shellCount&#39; shs = shs<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これは4行目がリストが空だったときの対応、<br />
5行目がリストの要素が1個だったときの対応を示しています。<br />
このように、Haskellでは関数を複数定義することができ、<br />
引数の条件によって適用される関数を変えることができます。<br />
この機能は「パターンマッチ」と呼ばれます。<br />
引数の条件（パターン）は、上から順に照合され、<br />
マッチしたらその行の関数が適用されます。<br />
従って、要素数が二つ以上の場合は、6行目の関数が適用されます。</p><br />
</div><br />
<div class="section" id="id13"><br />
<h2>4.5. パターンの書き方<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、図6の6行目の <tt class="docutils literal"><span class="pre">shellCount'</span></tt> に、<br />
リストをまとめる処理を書きましょう。<br />
まだ完成ではありませんが、<br />
まず次のように6行目の関数を書き換えます。</p><br />
<p>　まず、6行目の引数が <tt class="docutils literal"><span class="pre">((n1,s1):(n2,s2):ss)</span></tt><br />
と書き変わっています。<br />
まず、「 <tt class="docutils literal"><span class="pre">:</span></tt> 」ですが、これは図7のような型の演算子です。<br />
演算子の型を調べるときは括弧で囲みます。</p><br />
<ul class="simple"><br />
<li>図7: 「:」の型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span>:<span class="o">)</span><br />
<span class="o">(</span>:<span class="o">)</span> :: a -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これだけでは分かりませんが、 <tt class="docutils literal"><span class="pre">:</span></tt> は<br />
「要素一つをリストの先頭にくっつける」<br />
という演算子です。</p><br />
<p>　ですので <tt class="docutils literal"><span class="pre">((n1,s1):(n2,s2):ss)</span></tt> は、<br />
「 <tt class="docutils literal"><span class="pre">ss</span></tt> という名前のリストに <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt><br />
と <tt class="docutils literal"><span class="pre">(n2,s2)</span></tt> をくっつけたもの」<br />
という意味になります。<br />
<tt class="docutils literal"><span class="pre">ss</span></tt> は空リストでもよいので、<br />
パターンとして見ると、<br />
要素数が2個以上のリストを意味することになります。</p><br />
<p>　そして、ここで使った <tt class="docutils literal"><span class="pre">n1,s1,n2...</span></tt><br />
は、右辺で自由に使えます。</p><br />
</div><br />
<div class="section" id="id14"><br />
<h2>4.6. ガードでも場合分け<a class="headerlink" href="#id14" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次に、図8のところまで書き進めてみました。<br />
7,8行目にまた珍妙な書き方が登場しましたが、<br />
これは「ガード」と呼ばれるものです。<br />
これも関数の定義を場合分けしている書き方で、<br />
7行目が <tt class="docutils literal"><span class="pre">s1</span></tt> と <tt class="docutils literal"><span class="pre">s2</span></tt> が一致している場合に<br />
7行目の右側を評価する、<br />
その他の場合には8行目の右辺を評価するという意味になります。</p><br />
<ul class="simple"><br />
<li>図8: ガードを使ったq1_2_5.hs</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_5.hs<br />
（中略）<br />
shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span><br />
<span class="s1">shellCount&#39;</span> <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span><br />
shellCount<span class="s1">&#39; [a] = [a]</span><br />
<span class="s1">shellCount&#39;</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span><br />
 | <span class="nv">s1</span> <span class="o">==</span> <span class="nv">s2</span> <span class="o">=</span> <span class="o">(</span>n1+n2,s1<span class="o">)</span>:ss<br />
 | <span class="nv">otherwise</span> <span class="o">=</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　パターンマッチと違って、ガードでは値の比較ができます。<br />
パターンマッチは型の比較しかできません。</p><br />
<p>　さて、肝心の7, 8行目の右辺の処理ですが、<br />
7行目は二つの要素をまとめて、残りのリストとくっつけています。<br />
8行目はそのままリストを返しています。</p><br />
</div><br />
<div class="section" id="id15"><br />
<h2>4.7. 再帰処理を行う<a class="headerlink" href="#id15" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　このままこのコードをコンパイルして実行してみると、<br />
図9のように先頭の2行だけ集計されて出力されます。<br />
処理が連鎖するように、もうちょっとだけ加筆が必要です。</p><br />
<ul class="simple"><br />
<li>図9: q1_2_5の実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat /etc/passwd |<br />
 ./q1_2_5 | head -n 3<br />
2 /bin/bash<br />
1 /bin/bash<br />
1 /bin/false<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　完成したコード全体を図10に示します。</p><br />
<ul class="simple"><br />
<li>図10: 完成！（q1_2_6.hs）</li><br />
</ul><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_6.hs<br />
import Data.List<br />
import Data.List.Split<br />
<br />
<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . main<span class="s1">&#39;</span><br />
<br />
<span class="s1">main&#39;</span> :: String -&gt; String<br />
main<span class="s1">&#39; cs = unlines $ shellCount $ map getShell (lines cs)</span><br />
<br />
<span class="s1">getShell :: String -&gt; String</span><br />
<span class="s1">getShell ln = last $ splitOn &quot;:&quot; ln</span><br />
<br />
<span class="s1">shellCount :: [String] -&gt; [String]</span><br />
<span class="s1">shellCount shs = map f $ shellCount&#39;</span> <span class="o">[</span> <span class="o">(</span>1,s<span class="o">)</span> | s &lt;- <span class="o">(</span>sort shs<span class="o">)</span> <span class="o">]</span><br />
 where f <span class="o">(</span>n,str<span class="o">)</span> <span class="o">=</span> unwords <span class="o">[</span>show n,str<span class="o">]</span><br />
<br />
shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span><br />
<span class="s1">shellCount&#39;</span> <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span><br />
shellCount<span class="s1">&#39; [a] = [a]</span><br />
<span class="s1">shellCount&#39;</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span><br />
 | <span class="nv">s1</span> <span class="o">==</span> <span class="nv">s2</span> <span class="o">=</span> shellCount<span class="s1">&#39; $ (n1+n2,s1):ss</span><br />
<span class="s1"> | otherwise = (n1,s1):(shellCount&#39;</span> <span class="nv">$ </span><span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、コードの解説をば。 <tt class="docutils literal"><span class="pre">q1_2_5.hs</span></tt><br />
と <tt class="docutils literal"><span class="pre">q1_2_6.hs</span></tt> の違いですが、まず、<br />
<tt class="docutils literal"><span class="pre">q1_2_6.hs</span></tt> の21行目で、作ったリストに再度、<br />
自分自身 <tt class="docutils literal"><span class="pre">shellCount`</span></tt> を適用しています。<br />
22行目では、最初の要素 <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt> をどけて、<br />
二番目以降のリスト <tt class="docutils literal"><span class="pre">(n2,s2):ss</span></tt><br />
に <tt class="docutils literal"><span class="pre">shellCount'</span></tt> を適用し、<br />
その出力と <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt> をくっつけています。</p><br />
<p>　これで、リストに同じシェルのタプルが続けば<br />
どんどんタプル中の数字が加算されていき、<br />
そうでなければ次のシェルの個数の集計が始まるという<br />
処理になりました。このような再帰処理は、<br />
for文の代わりとなるため、<br />
Haskellではよく使います。</p><br />
<p>　実行してみましょう。図11のように答えが出ます。</p><br />
<ul class="simple"><br />
<li>図11: q1_2_6の実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat /etc/passwd | ./q1_2_6<br />
3 /bin/bash<br />
4 /bin/false<br />
17 /bin/sh<br />
1 /bin/sync<br />
1 /usr/sbin/nologin<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id16"><br />
<h2>4.8. もっと良い別解<a class="headerlink" href="#id16" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　・・・でめでだしめでたしだったのですが、<br />
一通り説明を終えて、<br />
「もっと単純化できるんじゃね？」<br />
と気づいたので、そちらのコードも図12に晒しておきます<br />
<a class="footnote-reference" href="#fff" id="id17">[8]</a><br />
。<br />
回答は無限にあるので、もっといい方法があったら教えてください。<br />
それにしても、ちょっと回りくどかったかもしれません・・・。</p><br />
<ul class="simple"><br />
<li>図12: 回りくどくないq1_2_7.hs</li><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_7</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">Data.List</span><br />
<span class="kr">import</span> <span class="nn">Data.List.Split</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span><br />
<br />
<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">sort</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span><br />
<br />
<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span><br />
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span><br />
<br />
<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span><br />
<span class="nf">shellCount</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="kt">[]</span><br />
<span class="nf">shellCount</span> <span class="p">(</span><span class="n">s</span><span class="kt">:</span><span class="n">ss</span><span class="p">)</span> <span class="ow">=</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">length</span> <span class="n">t</span><span class="p">)</span> <span class="o">++</span> <span class="p">(</span><span class="sc">&#39; &#39;</span><span class="kt">:</span><span class="n">s</span><span class="p">))</span> <span class="kt">:</span> <span class="n">shellCount</span> <span class="n">d</span><br />
 <span class="kr">where</span> <span class="n">t</span> <span class="ow">=</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">s</span><span class="p">)</span> <span class="n">ss</span><br />
 <span class="n">d</span> <span class="ow">=</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">s</span><span class="p">)</span> <span class="n">ss</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このコードでは <tt class="docutils literal"><span class="pre">main'</span></tt> で <tt class="docutils literal"><span class="pre">getShell</span></tt> からシェルの名前を受け取ったら<br />
すぐに <tt class="docutils literal"><span class="pre">sort</span></tt> して <tt class="docutils literal"><span class="pre">shellCount</span></tt><br />
に渡しています。<br />
<tt class="docutils literal"><span class="pre">shellCount</span></tt> はシェルの名前が入った文字列のリスト<br />
<tt class="docutils literal"><span class="pre">[String]</span></tt> を受け取りますが、<br />
それを <tt class="docutils literal"><span class="pre">where</span></tt> 以下で「先頭と同じシェルのリスト」<br />
と、「それ以外のリスト」に分けています。<br />
それぞれ「 <tt class="docutils literal"><span class="pre">t</span></tt> 、 <tt class="docutils literal"><span class="pre">d</span></tt> 」と名付けています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">takeWhile</span></tt> と <tt class="docutils literal"><span class="pre">dropWhile</span></tt> の動作を図13に示しておきます。</p><br />
<ul class="simple"><br />
<li>図13: takeWhile, dropWhile</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span><span class="mi">1</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span><br />
<span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span><span class="mi">1</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span><br />
<span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これで、 <tt class="docutils literal"><span class="pre">t</span></tt> の長さに1を足したものが該当するシェルの個数となります。<br />
また、 <tt class="docutils literal"><span class="pre">d</span></tt> を再度 <tt class="docutils literal"><span class="pre">shellCount</span></tt> に入力すれば、<br />
再帰的に各シェルの個数を集計できます。</p><br />
<p>　さらにこのコードを図14のように縮めてみます。<br />
だんだんシェル芸に見えてきませんでしたか？<br />
だんだんシェル芸に見えてきませんでしたか？</p><br />
<ul class="simple"><br />
<li>図14: mainがシェル芸っぽいq1_2_8.hs</li><br />
</ul><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_8.hs<br />
import Data.List<br />
import Data.List.Split<br />
<br />
<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . unlines . shellCount .<br />
 sort . map <span class="o">(</span>last . splitOn <span class="s2">&quot;:&quot;</span><span class="o">)</span> . lines<br />
<br />
shellCount :: <span class="o">[</span>String<span class="o">]</span> -&gt; <span class="o">[</span>String<span class="o">]</span><br />
shellCount <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span><br />
shellCount <span class="o">(</span>s:ss<span class="o">)</span> <span class="o">=</span> <span class="o">(</span>show <span class="o">(</span>1 + length t<span class="o">)</span> ++ <span class="o">(</span><span class="s1">&#39; &#39;</span>:s<span class="o">))</span> : shellCount d<br />
 where <span class="nv">t</span> <span class="o">=</span> takeWhile <span class="o">(==</span> s<span class="o">)</span> ss<br />
 <span class="nv">d</span> <span class="o">=</span> dropWhile <span class="o">(==</span> s<span class="o">)</span> ss<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id18"><br />
<h2>4.9. 終わりに<a class="headerlink" href="#id18" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は第1回シェル芸勉強会の2問目の答えまで行き着きました。<br />
パターンマッチ、ガード、再帰処理と、<br />
Haskellっぽいものがたくさんでてきましたが、<br />
粘り強く文法を確認していただければと。</p><br />
<p>　次回は3問目から！キリがよい！</p><br />
</div><br />
<div class="section" id="id19"><br />
<h2>4.10. お知らせ：コード募集<a class="headerlink" href="#id19" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>本稿で出た問題のHaskellのコードを、<br />
名前あるいはハンドルネームと共に送ってください。<br />
短いもの、あるいは変態的なものをお願いいたします。</p><br />
<p>email: 編集部のメールアドレス</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id20" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>順に助教、アドバイザリーフェロー、会長。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aaa" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>ごめんなさいごめんなさい。ウルトラスーパーごめんなさい。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="ccc" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>この物語はノンフィクションです。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="ggg" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id9">[4]</a></td><td>「型クラス」というのがキーワードですのでご調査を。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="bbb" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id5">[5]</a></td><td>反省の色がない。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="ddd" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id7">[6]</a></td><td>おい。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="eee" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id11">[7]</a></td><td><tt class="docutils literal"><span class="pre">Int</span></tt> あるいは <tt class="docutils literal"><span class="pre">Integer</span></tt></td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="fff" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id17">[8]</a></td><td>記事を書いていて一番怖い現象が起きた瞬間である。そのまま押し切る（おい）。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="zzz" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id8">[9]</a></td><td>【名】死刑執行、処刑</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

