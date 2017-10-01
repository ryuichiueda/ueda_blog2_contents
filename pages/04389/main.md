---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年7月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典: USP magazine 7月号

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=490480709X" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>



<a href="/?page=02944">各号の一覧へ</a>

<h1>4. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1>
<div class="section" id="id2">
<h2>4.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　皆さん、しらばっくれてますか？
締め切り後からおもむろに書き始める、
ダメな感じ満載の上田です
<a class="footnote-reference" href="#aaa" id="id3">[2]</a>
。
いやあね、もう歳で、とにかく物忘れが酷い酷い。
この前なんか、
自首しようと思ったのに忘れていて、
家までFBIが来て大変でした
<a class="footnote-reference" href="#ccc" id="id4">[3]</a>
。</p>
<p>　反省はほどほどに、はじめましょう
<a class="footnote-reference" href="#bbb" id="id5">[5]</a>
。
まず一つご報告ですが、
Haskellのインストール等の情報を私のサイトにまとめました。</p>
<p><tt class="docutils literal"><span class="pre">/?page_id=2944</span></tt></p>
<p>にあります。続きはWebで。面会は刑務所で。</p>
</div>
<div class="section" id="id6">
<h2>4.2. おさらい<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回からシェル芸勉強会の第1回2問目をやっちょります。
環境はLinuxを想定しています。</p>
<blockquote>
<div>/etc/passwd から、次を調べてください。
「ログインシェルがbashのユーザとshのユーザ、どっちが多い？」</div></blockquote>
<p>ほんと、しらねーよという感じですが
<a class="footnote-reference" href="#ddd" id="id7">[6]</a>
、前回から真面目に取り組んできました。
前回までで完成したコードを図1に示します。</p>
<ul class="simple">
<li>図1: 前回の最後のコードq1_2_3.hs</li>
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
18</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_3.hs
import Data.List
import Data.List.Split

<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . main<span class="s1">&#39;</span>

<span class="s1">main&#39;</span> :: String -&gt; String
main<span class="s1">&#39; cs = unlines $ shellCount $ map getShell (lines cs)</span>

<span class="s1">getShell :: String -&gt; String</span>
<span class="s1">getShell ln = last $ splitOn &quot;:&quot; ln</span>

<span class="s1">shellCount :: [String] -&gt; [String]</span>
<span class="s1">shellCount shs = map f $ shellCount&#39;</span> <span class="o">[</span> <span class="o">(</span>1,s<span class="o">)</span> | s &lt;- <span class="o">(</span>sort shs<span class="o">)</span> <span class="o">]</span>
 where f <span class="o">(</span>n,str<span class="o">)</span> <span class="o">=</span> unwords <span class="o">[</span>show n,str<span class="o">]</span>

shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span>
<span class="s1">shellCount&#39;</span> <span class="nv">shs</span> <span class="o">=</span> shs
</pre></div>
</td></tr></table></div>
<p>　関数 <tt class="docutils literal"><span class="pre">shellCount'</span></tt> が今のところダミーになっています。
実行すると図2のような出力が出ます。</p>
<ul class="simple">
<li>図2: q1_2_3をexecution <a class="footnote-reference" href="#zzz" id="id8">[9]</a></li>
</ul>
<p>　おさらいついでにもう一つ補足すると、
図1の <tt class="docutils literal"><span class="pre">q1_2_3.hs</span></tt> の15行目の
<tt class="docutils literal"><span class="pre">show</span></tt> 関数は、数値等を文字列に変換する関数です。
ghciで調べると、図3のような型です。</p>
<ul class="simple">
<li>図3: showの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t show
show :: Show <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; String
</pre></div>
</td></tr></table></div>
<p>ここで、 <tt class="docutils literal"><span class="pre">Show</span> <span class="pre">a</span></tt> というのは、
「 <tt class="docutils literal"><span class="pre">show</span></tt> が使える任意の型」という意味です。
そのような型がどのように定義されるのかは、
死人が出そうなので説明をやめておきます
<a class="footnote-reference" href="#ggg" id="id9">[4]</a>
。代わりに <tt class="docutils literal"><span class="pre">show</span></tt> の動作を図4にお見せします。</p>
<ul class="simple">
<li>図4: showの動作</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mf">0.1</span>
<span class="s">&quot;0.1&quot;</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mi">1</span>
<span class="s">&quot;1&quot;</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">show</span> <span class="mf">1e+100</span>
<span class="s">&quot;1.0e100&quot;</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>4.3. 開始！<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　Haskellの内部では各レコードは次のような二つの値の対になっています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>
</pre></div>
</div>
<p>このような対をHaskellでは「タプル」と呼びます。
この例のタプルの型は図5のような感じ。</p>
<ul class="simple">
<li>図5: タプルの型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="s">&quot;/bin/bash&quot;</span><span class="p">)</span>
<span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="s">&quot;/bin/bash&quot;</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Num</span> <span class="n">t</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="p">[</span><span class="kt">Char</span><span class="p">])</span>
</pre></div>
</td></tr></table></div>
<p>また、 <tt class="docutils literal"><span class="pre">show</span></tt> の型のように <tt class="docutils literal"><span class="pre">Num</span> <span class="pre">t</span> <span class="pre">=&gt;</span></tt> というのが
出てきましたが、これも数字に属する任意の型 <tt class="docutils literal"><span class="pre">t</span></tt>
という意味になります。
「1」の型が不定
<a class="footnote-reference" href="#eee" id="id11">[7]</a>
なのでややこしい出力になってしまいましたが、
要は数字と文字列のタプルです。
これがリストになったものが、18行目の入力 <tt class="docutils literal"><span class="pre">shs</span></tt>
です。
18行目の右辺で、例えば</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/sh&quot;</span><span class="o">)]</span>
</pre></div>
</div>
<p>とあったら</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[(</span>2,<span class="s2">&quot;/bin/bash&quot;</span><span class="o">)</span>, <span class="o">(</span>1,<span class="s2">&quot;/bin/sh&quot;</span><span class="o">)]</span>
</pre></div>
</div>
<p>とまとめるコードを右辺に書きます。</p>
</div>
<div class="section" id="id12">
<h2>4.4. パターンマッチで場合分け<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まとめる戦略を次のように考えます。
リスト <tt class="docutils literal"><span class="pre">[a,b,c,...]</span></tt> （a,b,cがそれぞれタプル）に対して、</p>
<ol class="arabic simple">
<li>リストの先頭二つの要素aとbを比較</li>
<li>aとbに入っているシェルの名前が一致: タプル中の数字を足し合わせて一つの要素にまとめる</li>
<li>一致しない: aをそのままにして、bとcを比較</li>
</ol>
<p>という手続きを書いていこうと思います。</p>
<p>　しかしその前に、
じゃあリストに1個しか要素が無かったとき、
あるいは0個だったときのことも考えておかないといけません。
Haskellでは図6のようなコードを書きます。</p>
<ul class="simple">
<li>図6: パターンマッチを書いたq1_2_4.hs</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC$ cat q1_2_4.hs
（中略）
shellCount&#39; :: [(Int,String)] -&gt; [(Int,String)]
shellCount&#39; [] = []
shellCount&#39; [a] = [a]
shellCount&#39; shs = shs
</pre></div>
</td></tr></table></div>
<p>　これは4行目がリストが空だったときの対応、
5行目がリストの要素が1個だったときの対応を示しています。
このように、Haskellでは関数を複数定義することができ、
引数の条件によって適用される関数を変えることができます。
この機能は「パターンマッチ」と呼ばれます。
引数の条件（パターン）は、上から順に照合され、
マッチしたらその行の関数が適用されます。
従って、要素数が二つ以上の場合は、6行目の関数が適用されます。</p>
</div>
<div class="section" id="id13">
<h2>4.5. パターンの書き方<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、図6の6行目の <tt class="docutils literal"><span class="pre">shellCount'</span></tt> に、
リストをまとめる処理を書きましょう。
まだ完成ではありませんが、
まず次のように6行目の関数を書き換えます。</p>
<p>　まず、6行目の引数が <tt class="docutils literal"><span class="pre">((n1,s1):(n2,s2):ss)</span></tt>
と書き変わっています。
まず、「 <tt class="docutils literal"><span class="pre">:</span></tt> 」ですが、これは図7のような型の演算子です。
演算子の型を調べるときは括弧で囲みます。</p>
<ul class="simple">
<li>図7: 「:」の型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span>:<span class="o">)</span>
<span class="o">(</span>:<span class="o">)</span> :: a -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>これだけでは分かりませんが、 <tt class="docutils literal"><span class="pre">:</span></tt> は
「要素一つをリストの先頭にくっつける」
という演算子です。</p>
<p>　ですので <tt class="docutils literal"><span class="pre">((n1,s1):(n2,s2):ss)</span></tt> は、
「 <tt class="docutils literal"><span class="pre">ss</span></tt> という名前のリストに <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt>
と <tt class="docutils literal"><span class="pre">(n2,s2)</span></tt> をくっつけたもの」
という意味になります。
<tt class="docutils literal"><span class="pre">ss</span></tt> は空リストでもよいので、
パターンとして見ると、
要素数が2個以上のリストを意味することになります。</p>
<p>　そして、ここで使った <tt class="docutils literal"><span class="pre">n1,s1,n2...</span></tt>
は、右辺で自由に使えます。</p>
</div>
<div class="section" id="id14">
<h2>4.6. ガードでも場合分け<a class="headerlink" href="#id14" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次に、図8のところまで書き進めてみました。
7,8行目にまた珍妙な書き方が登場しましたが、
これは「ガード」と呼ばれるものです。
これも関数の定義を場合分けしている書き方で、
7行目が <tt class="docutils literal"><span class="pre">s1</span></tt> と <tt class="docutils literal"><span class="pre">s2</span></tt> が一致している場合に
7行目の右側を評価する、
その他の場合には8行目の右辺を評価するという意味になります。</p>
<ul class="simple">
<li>図8: ガードを使ったq1_2_5.hs</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_5.hs
（中略）
shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span>
<span class="s1">shellCount&#39;</span> <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span>
shellCount<span class="s1">&#39; [a] = [a]</span>
<span class="s1">shellCount&#39;</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span>
 | <span class="nv">s1</span> <span class="o">==</span> <span class="nv">s2</span> <span class="o">=</span> <span class="o">(</span>n1+n2,s1<span class="o">)</span>:ss
 | <span class="nv">otherwise</span> <span class="o">=</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>　パターンマッチと違って、ガードでは値の比較ができます。
パターンマッチは型の比較しかできません。</p>
<p>　さて、肝心の7, 8行目の右辺の処理ですが、
7行目は二つの要素をまとめて、残りのリストとくっつけています。
8行目はそのままリストを返しています。</p>
</div>
<div class="section" id="id15">
<h2>4.7. 再帰処理を行う<a class="headerlink" href="#id15" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　このままこのコードをコンパイルして実行してみると、
図9のように先頭の2行だけ集計されて出力されます。
処理が連鎖するように、もうちょっとだけ加筆が必要です。</p>
<ul class="simple">
<li>図9: q1_2_5の実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat /etc/passwd |
 ./q1_2_5 | head -n 3
2 /bin/bash
1 /bin/bash
1 /bin/false
</pre></div>
</td></tr></table></div>
<p>　完成したコード全体を図10に示します。</p>
<ul class="simple">
<li>図10: 完成！（q1_2_6.hs）</li>
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
22</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_6.hs
import Data.List
import Data.List.Split

<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . main<span class="s1">&#39;</span>

<span class="s1">main&#39;</span> :: String -&gt; String
main<span class="s1">&#39; cs = unlines $ shellCount $ map getShell (lines cs)</span>

<span class="s1">getShell :: String -&gt; String</span>
<span class="s1">getShell ln = last $ splitOn &quot;:&quot; ln</span>

<span class="s1">shellCount :: [String] -&gt; [String]</span>
<span class="s1">shellCount shs = map f $ shellCount&#39;</span> <span class="o">[</span> <span class="o">(</span>1,s<span class="o">)</span> | s &lt;- <span class="o">(</span>sort shs<span class="o">)</span> <span class="o">]</span>
 where f <span class="o">(</span>n,str<span class="o">)</span> <span class="o">=</span> unwords <span class="o">[</span>show n,str<span class="o">]</span>

shellCount<span class="s1">&#39; :: [(Int,String)] -&gt; [(Int,String)]</span>
<span class="s1">shellCount&#39;</span> <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span>
shellCount<span class="s1">&#39; [a] = [a]</span>
<span class="s1">shellCount&#39;</span> <span class="o">((</span>n1,s1<span class="o">)</span>:<span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span>
 | <span class="nv">s1</span> <span class="o">==</span> <span class="nv">s2</span> <span class="o">=</span> shellCount<span class="s1">&#39; $ (n1+n2,s1):ss</span>
<span class="s1"> | otherwise = (n1,s1):(shellCount&#39;</span> <span class="nv">$ </span><span class="o">(</span>n2,s2<span class="o">)</span>:ss<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>　さて、コードの解説をば。 <tt class="docutils literal"><span class="pre">q1_2_5.hs</span></tt>
と <tt class="docutils literal"><span class="pre">q1_2_6.hs</span></tt> の違いですが、まず、
<tt class="docutils literal"><span class="pre">q1_2_6.hs</span></tt> の21行目で、作ったリストに再度、
自分自身 <tt class="docutils literal"><span class="pre">shellCount`</span></tt> を適用しています。
22行目では、最初の要素 <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt> をどけて、
二番目以降のリスト <tt class="docutils literal"><span class="pre">(n2,s2):ss</span></tt>
に <tt class="docutils literal"><span class="pre">shellCount'</span></tt> を適用し、
その出力と <tt class="docutils literal"><span class="pre">(n1,s1)</span></tt> をくっつけています。</p>
<p>　これで、リストに同じシェルのタプルが続けば
どんどんタプル中の数字が加算されていき、
そうでなければ次のシェルの個数の集計が始まるという
処理になりました。このような再帰処理は、
for文の代わりとなるため、
Haskellではよく使います。</p>
<p>　実行してみましょう。図11のように答えが出ます。</p>
<ul class="simple">
<li>図11: q1_2_6の実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat /etc/passwd | ./q1_2_6
3 /bin/bash
4 /bin/false
17 /bin/sh
1 /bin/sync
1 /usr/sbin/nologin
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id16">
<h2>4.8. もっと良い別解<a class="headerlink" href="#id16" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　・・・でめでだしめでたしだったのですが、
一通り説明を終えて、
「もっと単純化できるんじゃね？」
と気づいたので、そちらのコードも図12に晒しておきます
<a class="footnote-reference" href="#fff" id="id17">[8]</a>
。
回答は無限にあるので、もっといい方法があったら教えてください。
それにしても、ちょっと回りくどかったかもしれません・・・。</p>
<ul class="simple">
<li>図12: 回りくどくないq1_2_7.hs</li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">USPMAG</span><span class="o">/</span><span class="kt">SRC</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_2_7</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">Data.List</span>
<span class="kr">import</span> <span class="nn">Data.List.Split</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">main&#39;</span>

<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">main&#39;</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">unlines</span> <span class="o">$</span> <span class="n">shellCount</span> <span class="o">$</span> <span class="n">sort</span> <span class="o">$</span> <span class="n">map</span> <span class="n">getShell</span> <span class="p">(</span><span class="n">lines</span> <span class="n">cs</span><span class="p">)</span>

<span class="nf">getShell</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">String</span>
<span class="nf">getShell</span> <span class="n">ln</span> <span class="ow">=</span> <span class="n">last</span> <span class="o">$</span> <span class="n">splitOn</span> <span class="s">&quot;:&quot;</span> <span class="n">ln</span>

<span class="nf">shellCount</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span>
<span class="nf">shellCount</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="kt">[]</span>
<span class="nf">shellCount</span> <span class="p">(</span><span class="n">s</span><span class="kt">:</span><span class="n">ss</span><span class="p">)</span> <span class="ow">=</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">length</span> <span class="n">t</span><span class="p">)</span> <span class="o">++</span> <span class="p">(</span><span class="sc">&#39; &#39;</span><span class="kt">:</span><span class="n">s</span><span class="p">))</span> <span class="kt">:</span> <span class="n">shellCount</span> <span class="n">d</span>
 <span class="kr">where</span> <span class="n">t</span> <span class="ow">=</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">s</span><span class="p">)</span> <span class="n">ss</span>
 <span class="n">d</span> <span class="ow">=</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">s</span><span class="p">)</span> <span class="n">ss</span>
</pre></div>
</td></tr></table></div>
<p>　このコードでは <tt class="docutils literal"><span class="pre">main'</span></tt> で <tt class="docutils literal"><span class="pre">getShell</span></tt> からシェルの名前を受け取ったら
すぐに <tt class="docutils literal"><span class="pre">sort</span></tt> して <tt class="docutils literal"><span class="pre">shellCount</span></tt>
に渡しています。
<tt class="docutils literal"><span class="pre">shellCount</span></tt> はシェルの名前が入った文字列のリスト
<tt class="docutils literal"><span class="pre">[String]</span></tt> を受け取りますが、
それを <tt class="docutils literal"><span class="pre">where</span></tt> 以下で「先頭と同じシェルのリスト」
と、「それ以外のリスト」に分けています。
それぞれ「 <tt class="docutils literal"><span class="pre">t</span></tt> 、 <tt class="docutils literal"><span class="pre">d</span></tt> 」と名付けています。</p>
<p>　 <tt class="docutils literal"><span class="pre">takeWhile</span></tt> と <tt class="docutils literal"><span class="pre">dropWhile</span></tt> の動作を図13に示しておきます。</p>
<ul class="simple">
<li>図13: takeWhile, dropWhile</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span><span class="mi">1</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span>
<span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span><span class="mi">1</span><span class="p">)</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span>
<span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>　これで、 <tt class="docutils literal"><span class="pre">t</span></tt> の長さに1を足したものが該当するシェルの個数となります。
また、 <tt class="docutils literal"><span class="pre">d</span></tt> を再度 <tt class="docutils literal"><span class="pre">shellCount</span></tt> に入力すれば、
再帰的に各シェルの個数を集計できます。</p>
<p>　さらにこのコードを図14のように縮めてみます。
だんだんシェル芸に見えてきませんでしたか？
だんだんシェル芸に見えてきませんでしたか？</p>
<ul class="simple">
<li>図14: mainがシェル芸っぽいq1_2_8.hs</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_2_8.hs
import Data.List
import Data.List.Split

<span class="nv">main</span> <span class="o">=</span> getContents &gt;&gt;<span class="o">=</span> putStr . unlines . shellCount .
 sort . map <span class="o">(</span>last . splitOn <span class="s2">&quot;:&quot;</span><span class="o">)</span> . lines

shellCount :: <span class="o">[</span>String<span class="o">]</span> -&gt; <span class="o">[</span>String<span class="o">]</span>
shellCount <span class="o">[]</span> <span class="o">=</span> <span class="o">[]</span>
shellCount <span class="o">(</span>s:ss<span class="o">)</span> <span class="o">=</span> <span class="o">(</span>show <span class="o">(</span>1 + length t<span class="o">)</span> ++ <span class="o">(</span><span class="s1">&#39; &#39;</span>:s<span class="o">))</span> : shellCount d
 where <span class="nv">t</span> <span class="o">=</span> takeWhile <span class="o">(==</span> s<span class="o">)</span> ss
 <span class="nv">d</span> <span class="o">=</span> dropWhile <span class="o">(==</span> s<span class="o">)</span> ss
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id18">
<h2>4.9. 終わりに<a class="headerlink" href="#id18" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は第1回シェル芸勉強会の2問目の答えまで行き着きました。
パターンマッチ、ガード、再帰処理と、
Haskellっぽいものがたくさんでてきましたが、
粘り強く文法を確認していただければと。</p>
<p>　次回は3問目から！キリがよい！</p>
</div>
<div class="section" id="id19">
<h2>4.10. お知らせ：コード募集<a class="headerlink" href="#id19" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id20" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>順に助教、アドバイザリーフェロー、会長。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aaa" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>ごめんなさいごめんなさい。ウルトラスーパーごめんなさい。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="ccc" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>この物語はノンフィクションです。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="ggg" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id9">[4]</a></td><td>「型クラス」というのがキーワードですのでご調査を。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="bbb" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id5">[5]</a></td><td>反省の色がない。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="ddd" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[6]</a></td><td>おい。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="eee" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[7]</a></td><td><tt class="docutils literal"><span class="pre">Int</span></tt> あるいは <tt class="docutils literal"><span class="pre">Integer</span></tt></td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="fff" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id17">[8]</a></td><td>記事を書いていて一番怖い現象が起きた瞬間である。そのまま押し切る（おい）。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="zzz" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[9]</a></td><td>【名】死刑執行、処刑</td></tr>
</tbody>
</table>
</div>
</div>

