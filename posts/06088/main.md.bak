# USP Magazine 2014年8月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<div class="section" id="haskell"><br />
<h1>5. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院・USP研究所・USP友の会　上田のり平<br />
<a class="footnote-reference" href="#id14" id="id1">[1]</a><br />
<a class="footnote-reference" href="#id15" id="id2">[2]</a></p><br />
<blockquote><br />
<div>USP友の会のシェル芸勉強会<br />
（脚注：シェルのワンライナー勉強会）は、<br />
日々、他の言語からの他流試合に晒されているのである。<br />
そこで上田は、Haskellで自ら他流試合を行い、<br />
さらにシェル芸勉強会をいじめる自傷行為に手を<br />
染めるのであった。</div></blockquote><br />
<div class="section" id="id3"><br />
<h2>5.1. はじめに<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　こんにつわ。富山のホワイトシュリンプ上田のり平<br />
<a class="footnote-reference" href="#id16" id="id4">[3]</a><br />
です。<br />
今、締め切りが過ぎているのに気づいて<br />
出張先の富山からお送りしております。<br />
帰省ではありません出張です。<br />
ちなみに、茹でるとプラスチックみたいに変態します。<br />
これ豆な。</p><br />
<p>さて、そんな私信はどうでもいいんです。<br />
HaskellですHaskell。やりましょう。<br />
今回は第1回シェル芸勉強会の3問目です。</p><br />
<blockquote><br />
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト<br />
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）<br />
について以下の操作をしてください。</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li><br />
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li><br />
</ul><br />
</div></blockquote><br />
<p>うわ・・・難しい・・・。どうしよ？リスカしよ<br />
<a class="footnote-reference" href="#id17" id="id5">[4]</a><br />
。<br />
・・・じゃなくて、とりあえずやりましょう。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h2>5.2. ディレクトリいじり<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、まずは <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下をまさぐるコードを書かねばいけません。<br />
とりあえずリスト1のようなコードを書いてみました。<br />
<tt class="docutils literal"><span class="pre">ls</span> <span class="pre">/etc/</span></tt> に相当するプログラムです。<br />
今のところ <tt class="docutils literal"><span class="pre">ls</span></tt> のように1段目のディレクトリしか調べられませんが、<br />
この後で2段目3段目とディレクトリを降りていって<br />
全てのファイルのリストを作るコードにしていきます。</p><br />
<ul class="simple"><br />
<li>リスト1: lsのようなもの（q1_3_1.hs）</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_3_1.hs<br />
import System.Directory<br />
<br />
<span class="nv">main</span> <span class="o">=</span> getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<br />
</pre></div><br />
</td></tr></table></div><br />
<p>実行してみましょう。リスト2のようにずらずらとファイルや<br />
ディレクトリの名前が出てきます。</p><br />
<ul class="simple"><br />
<li>リスト2: q1_3_1の実行</li><br />
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
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_3_1.hs<br />
ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_1 | head -n 3<br />
insserv<br />
blkid.tab<br />
tidy.conf<br />
<span class="c">###ls -f /etc/と同じ出力###</span><br />
ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ls -f /etc/ | head -n 3<br />
insserv<br />
blkid.tab<br />
tidy.conf<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト1のコードですが、次のような意味があります。<br />
まず、 <tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> の型はリスト3のように、<br />
<tt class="docutils literal"><span class="pre">FilePath</span></tt> を引数にとって、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt><br />
を返すというものです。<br />
<tt class="docutils literal"><span class="pre">FilePath</span></tt> というのは <tt class="docutils literal"><span class="pre">String</span></tt> の別名なのですが、<br />
それはリスト3の後の二行のように、 <tt class="docutils literal"><span class="pre">:i</span></tt> （info）<br />
というコマンドで調べることができます。</p><br />
<ul class="simple"><br />
<li>リスト3: getDirectoryContentsの型とFilePathの情報</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC$ ghci<br />
GHCi, version 7.6.3: http://www.haskell.org/ghc/ :? for help<br />
（略）<br />
Prelude&gt; import System.Directory<br />
Prelude System.Directory&gt; :t getDirectoryContents<br />
getDirectoryContents :: FilePath -&gt; IO [FilePath]<br />
Prelude System.Directory&gt; :i FilePath<br />
type FilePath = String -- Defined in `GHC.IO&#39;<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の右側の <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt><br />
は、リストを <tt class="docutils literal"><span class="pre">unlines</span></tt> で1レコード1行にして、<br />
<tt class="docutils literal"><span class="pre">putStr</span></tt> で標準出力に吐き出すということです。</p><br />
</div><br />
<div class="section" id="io"><br />
<h2>5.3. IOってなんじゃい<a class="headerlink" href="#io" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　んで、とうとう <tt class="docutils literal"><span class="pre">IO</span></tt> の説明をするときがやってきてしまいました。<br />
これが、Haskellを勉強しようとした100人のうち、<br />
90人が死亡する原因となっているものです。</p><br />
<p>　今回はこれでおしまい。comming soon。</p><br />
<p>　・・・じゃなくて、真面目にやってきます。<br />
えーっと、 <tt class="docutils literal"><span class="pre">IO</span></tt> というのは、<br />
外から何か読み込んだものにつけるレッテルみたいなものです。<br />
外というのは例えば標準入力であったり、<br />
あるいは <tt class="docutils literal"><span class="pre">q1_3_1</span></tt> みたいにファイルの情報<br />
だったりのことで、要はHaskellの世界に元々ないものです。<br />
Haskellの世界には関数とその入出力しかないわけですが、<br />
「外から読んだもの」は、そのどちらでもありません。<br />
ですので、腫れ物のように扱われます。<br />
その「腫れ物」である印が <tt class="docutils literal"><span class="pre">IO</span></tt> です。<br />
外から読み込んで計算が修了するまで、<br />
型についた「 <tt class="docutils literal"><span class="pre">IO</span></tt> 」は取り払うことができず、<br />
普通の関数は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">hogehgoe</span></tt> という型を扱う事ができません。<br />
しかし、少しだけ例外があり、<br />
その例外の中でコソコソと普通の関数を使います。</p><br />
<p>　リスト1の4行目について、<br />
行全体（main関数）の型を見てみましょう。<br />
リストdddのようになります。</p><br />
<p>リストddd: q1_3_1.hsのmain関数の型</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import System.Directory<br />
Prelude System.Directory&gt; :t <span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<span class="o">)</span><br />
<span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<span class="o">)</span> :: IO <span class="o">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> という型であると分かりました。<br />
関数としては何も引数にとらず、<br />
ただ <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> を返すという意味になります。<br />
<tt class="docutils literal"><span class="pre">()</span></tt> は「何にもねえよ」という意味です。<br />
つまり、何も入出力しない関数であるとも解釈できますが、<br />
プログラムを実行するとファイルのリストを標準出力に表示します。<br />
実は、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> というのは、<br />
「標準出力に何か表示する」という行為のことを指しています。<br />
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">hogehoge</span></tt> という型を持っているものは、<br />
「アクション」<br />
<a class="footnote-reference" href="#id18" id="id7">[5]</a><br />
と呼ばれます。</p><br />
<p>　まだちょっと良く状況が分からんというところだと思いますが、<br />
とりあえず次に行きます。<br />
<tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> の型はリスト3で調べたので、<br />
次は <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt> について。</p><br />
<ul class="simple"><br />
<li>リスト4: putStr . unlinesの型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t putStr<br />
putStr :: String -&gt; IO <span class="o">()</span><br />
Prelude System.Directory&gt; :t unlines<br />
unlines :: <span class="o">[</span>String<span class="o">]</span> -&gt; String<br />
Prelude System.Directory&gt; :t <span class="o">(</span>putStr . unlines<span class="o">)</span><br />
<span class="o">(</span>putStr . unlines<span class="o">)</span> :: <span class="o">[</span>String<span class="o">]</span> -&gt; IO <span class="o">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト4のように、 <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt><br />
の型は「文字列のリストを受け取ってアクションを返す」<br />
です。</p><br />
<p>　次、謎の記号 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> ですが、リスト5のような感じです。<br />
ちなみに <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> はバインド演算子と呼ばれます。</p><br />
<ul class="simple"><br />
<li>リスト5: &gt;&gt;=の型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t <span class="o">(</span>&gt;&gt;<span class="o">=)</span><br />
<span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">Monad</span> <span class="pre">m</span> <span class="pre">=&gt;</span></tt> というのはまた別の機会に説明するとして<br />
<a class="footnote-reference" href="#id19" id="id8">[6]</a><br />
とりあえず <tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">(a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b)</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt><br />
を解釈してみましょう。<br />
これは <tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span></tt> と <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> という関数をとって、<br />
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">b</span></tt> を返すということです。<br />
リスト1の4行目について、書き換えてみましょう。<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を演算子ではなく関数のように扱ってみます。<br />
リストgggのように、ちゃんと動きます。</p><br />
<ul class="simple"><br />
<li>リストggg: <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を関数のように扱う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; <span class="o">(</span>&gt;&gt;<span class="o">=)</span> <span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span><span class="o">)</span> <span class="o">(</span>putStr . unlines<span class="o">)</span><br />
（中略）<br />
.<br />
..<br />
afpovertcp.cfg<br />
aliases<br />
aliases.db<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト5の型とリストgggを比べてみましょう。<br />
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">getDirectoryContents</span> <span class="pre">&quot;/etc/&quot;</span></tt><br />
の型 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> に相当するので、<br />
<tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> 、 <tt class="docutils literal"><span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">[FilePath]</span></tt><br />
ということになります。<br />
そして、 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> は <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt><br />
の型 <tt class="docutils literal"><span class="pre">[String]</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">()</span></tt> に対応します。<br />
<tt class="docutils literal"><span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">[String]</span></tt> つまり <tt class="docutils literal"><span class="pre">[FilePath]</span></tt> 、<br />
<tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> 、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">()</span></tt><br />
となります。ちょっと紙に書いて確かめていただきたいのですが、<br />
型は互いに矛盾していません。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h2>5.4. アクションを避けて普通の関数を使う<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　型は矛盾していないのですが、また疑問が浮かびます。<br />
リスト6のように、 <tt class="docutils literal"><span class="pre">unlines</span></tt> 関数はアクションとは無関係の関数です。<br />
が、アクションだらけのところで使う事ができています。<br />
これはなぜでしょう？</p><br />
<ul class="simple"><br />
<li>リスト6: unlinesの型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t unlines<br />
unlines :: <span class="o">[</span>String<span class="o">]</span> -&gt; String<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もう一度 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt><br />
の型を見てみます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b<br />
</pre></div><br />
</div><br />
<p>これの <tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> に対応するので、<br />
置き換えてみましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>IO a -&gt; <span class="o">(</span>a -&gt; IO b<span class="o">)</span> -&gt; IO b<br />
</pre></div><br />
</div><br />
<p>関数の型 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">b</span></tt> のところで、<br />
<tt class="docutils literal"><span class="pre">a</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> が取れています。<br />
結局これが <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の役割で、<br />
アクションの中身（ <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">a</span></tt> の <tt class="docutils literal"><span class="pre">a</span></tt> の部分）<br />
に普通の関数を適用できるようにしています。<br />
ただし、 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">b</span></tt> とあるように、<br />
普通の関数を適用した後の出力には再び<br />
<tt class="docutils literal"><span class="pre">IO</span></tt> をかぶせなければなりません。</p><br />
</div><br />
<div class="section" id="id10"><br />
<h2>5.5. 親と自分を消し去る<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、 <tt class="docutils literal"><span class="pre">q1_3_1</span></tt> の出力のなかには、<br />
リスト7のように親を指す <tt class="docutils literal"><span class="pre">..</span></tt><br />
と、自分を指す <tt class="docutils literal"><span class="pre">.</span></tt> が混ざっています。<br />
もう一度やりたいことをおさらいすると、<br />
今はこのコードを加筆して <tt class="docutils literal"><span class="pre">/etc/</span></tt><br />
下のファイルのリストを再帰的に作りたいのですが、<br />
<tt class="docutils literal"><span class="pre">..</span></tt> や <tt class="docutils literal"><span class="pre">.</span></tt> が混ざっていると再帰処理が終わりません。</p><br />
<ul class="simple"><br />
<li>リスト7: &#8221;.&#8221;と&#8221;..&#8221;が混ざりんぐ</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_1 | grep <span class="s1">&#39;^\\.\\.*$&#39;</span><br />
.<br />
..<br />
</pre></div><br />
</td></tr></table></div><br />
<p>ということで、少し書き進めてリスト8のようなコードを作りました。<br />
<tt class="docutils literal"><span class="pre">ls</span></tt> という関数を作りました。</p><br />
<ul class="simple"><br />
<li>リスト8: q1_3_2.hs</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_3_2.hs<br />
import System.Directory<br />
<br />
<span class="nv">main</span> <span class="o">=</span> ls <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<br />
<br />
ls :: String -&gt; IO <span class="o">[</span>FilePath<span class="o">]</span><br />
ls <span class="nv">dir</span> <span class="o">=</span> getDirectoryContents dir &gt;&gt;<span class="o">=</span> <span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">..</span></tt> と <tt class="docutils literal"><span class="pre">.</span></tt> が消えていることを確認しましょう。<br />
リスト9のように、ドットで始まる行を抽出することで確認しました。</p><br />
<ul class="simple"><br />
<li>リスト9: q1_3_2の実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_3_2.hs<br />
ueda\@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_2 | grep <span class="s1">&#39;^\\.&#39;</span><br />
.pwd.lock<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、リスト8の6,7行目の型を追っていきましょう。<br />
6行目のように関数 <tt class="docutils literal"><span class="pre">ls</span></tt> <a class="footnote-reference" href="#id20" id="id11">[7]</a><br />
の型は <tt class="docutils literal"><span class="pre">String</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">[FilePath]</span></tt><br />
ということで、 <tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> と同じです。<br />
7行目の <tt class="docutils literal"><span class="pre">ls</span></tt> の中身は、<br />
<tt class="docutils literal"><span class="pre">getDirectoryContents</span> <span class="pre">dir</span> <span class="pre">&gt;&gt;=</span></tt><br />
で、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> をはぎ取って、<br />
<tt class="docutils literal"><span class="pre">return</span> <span class="pre">.</span> <span class="pre">filter</span> <span class="pre">(`notElem`</span> <span class="pre">[&quot;.&quot;,&quot;..&quot;])</span></tt> に渡しています。<br />
この部分（「右辺」と呼びましょう）の型は、<br />
リスト10のようになります。<br />
<tt class="docutils literal"><span class="pre">[[Char]]</span></tt> を <tt class="docutils literal"><span class="pre">[FilePath]</span></tt><br />
に置き換えて読むと、<br />
ファイルパスのリストを受け取って、<br />
ファイルパスのリストに<br />
<tt class="docutils literal"><span class="pre">m</span></tt> つまり <tt class="docutils literal"><span class="pre">IO</span></tt> をかぶせて出力するというものになっています。</p><br />
<ul class="simple"><br />
<li>リスト10: return...の型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span><span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span> <span class="o">)</span><br />
<span class="o">(</span><span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span> <span class="o">)</span><br />
 :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; <span class="o">[[</span>Char<span class="o">]]</span> -&gt; m <span class="o">[[</span>Char<span class="o">]]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>右辺で面白いのは <tt class="docutils literal"><span class="pre">return</span></tt> です。<br />
これも関数で、普通の言語の <tt class="docutils literal"><span class="pre">return</span></tt><br />
とは全然違うものです。<br />
リスト11のように、普通の型に <tt class="docutils literal"><span class="pre">IO</span></tt><br />
をかぶせて出力します。<br />
<tt class="docutils literal"><span class="pre">q1_3_2.hs</span></tt> では、「 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の出力には <tt class="docutils literal"><span class="pre">IO</span></tt><br />
がかぶさっていないといけない」<br />
という条件を満たすために利用しています。</p><br />
<ul class="simple"><br />
<li>リスト11: returnの型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="k">return</span><br />
<span class="k">return</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; a -&gt; m a<br />
</pre></div><br />
</td></tr></table></div><br />
<p>ということは、右辺から <tt class="docutils literal"><span class="pre">return</span></tt> を除いた<br />
<tt class="docutils literal"><span class="pre">filter</span> <span class="pre">(`notElem`</span> <span class="pre">[&quot;.&quot;,</span> <span class="pre">&quot;..&quot;])</span></tt> の部分は、<br />
リスト12のように <tt class="docutils literal"><span class="pre">IO</span></tt> の呪縛から解放され、<br />
文字列を処理することに専念できるようになります。</p><br />
<ul class="simple"><br />
<li>リスト12: IOの呪縛から解放された部分</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>, <span class="s2">&quot;..&quot;</span><span class="o">])</span><br />
filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>, <span class="s2">&quot;..&quot;</span><span class="o">])</span> :: <span class="o">[[</span>Char<span class="o">]]</span> -&gt; <span class="o">[[</span>Char<span class="o">]]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">notElem</span></tt> の使い方をリスト13に示して、<br />
今回はおしまいとします。</p><br />
<ul class="simple"><br />
<li>リスト13: notElem関数</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t notElem<br />
notElem :: Eq <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; Bool<br />
Prelude&gt; notElem 1 <span class="o">[</span>1,2,3<span class="o">]</span><br />
False<br />
Prelude&gt; notElem 4 <span class="o">[</span>1,2,3<span class="o">]</span><br />
True<br />
<span class="c">###関数を演算子として使うときには``で関数を囲む###</span><br />
Prelude&gt; 1 <span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span>1,2,3<span class="o">]</span><br />
False<br />
<span class="c">###filterと併用するとリストから指定した要素を削除できる###</span><br />
Prelude&gt; filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span>1,2,3<span class="o">])</span> <span class="o">[</span>1,2,3,4,5<span class="o">]</span><br />
<span class="o">[</span>4,5<span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id12"><br />
<h2>5.6. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は第1回シェル芸勉強会の3問目で、<br />
ファイルの一覧をHaskellで処理する部分を書きました。<br />
「アクション」面倒ですね・・・。<br />
慣れが必要です。<br />
ただ、私も完全に理解してはいないのですが、<br />
数学的に正しいことを突き詰めた結果、<br />
面倒くさいことになっているようです。<br />
この手のものは慣れたらかえって自然に感じるものです。<br />
こうやって、慣れた人と慣れていない人の溝は、<br />
深まるばかりなんだなあ・・・。</p><br />
</div><br />
<div class="section" id="id13"><br />
<h2>5.7. お知らせ：コード募集<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>本稿で出た問題のHaskellのコードを、<br />
名前あるいはハンドルネームと共に送ってください。<br />
短いもの、あるいは変態的なものをお願いいたします。</p><br />
<p>email: 編集部のメールアドレス</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id14" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>USP友の会の幹事Uさんの夢の中でこのペンネームが誕生。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id15" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>順に助教、アドバイザリーフェロー、会長。ただし、今回はペンネームなので、名乗ってよいのかどうかは微妙。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id16" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>蛇足であるが本名は富山のブラックエンジェル上田隆一である。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id17" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id5">[4]</a></td><td>お菓子ではない。おかしいことは認める。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id18" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td>当然、漫画雑誌のことではない。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id19" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id8">[6]</a></td><td>先月号で <tt class="docutils literal"><span class="pre">show</span></tt> の型を説明するときにも <tt class="docutils literal"><span class="pre">=&gt;</span></tt> が出てきました。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id20" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id11">[7]</a></td><td>紛らわしい・・・</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

