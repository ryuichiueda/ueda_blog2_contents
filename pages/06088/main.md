---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年8月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<div class="section" id="haskell">
<h1>5. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院・USP研究所・USP友の会　上田のり平
<a class="footnote-reference" href="#id14" id="id1">[1]</a>
<a class="footnote-reference" href="#id15" id="id2">[2]</a></p>
<blockquote>
<div>USP友の会のシェル芸勉強会
（脚注：シェルのワンライナー勉強会）は、
日々、他の言語からの他流試合に晒されているのである。
そこで上田は、Haskellで自ら他流試合を行い、
さらにシェル芸勉強会をいじめる自傷行為に手を
染めるのであった。</div></blockquote>
<div class="section" id="id3">
<h2>5.1. はじめに<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　こんにつわ。富山のホワイトシュリンプ上田のり平
<a class="footnote-reference" href="#id16" id="id4">[3]</a>
です。
今、締め切りが過ぎているのに気づいて
出張先の富山からお送りしております。
帰省ではありません出張です。
ちなみに、茹でるとプラスチックみたいに変態します。
これ豆な。</p>
<p>さて、そんな私信はどうでもいいんです。
HaskellですHaskell。やりましょう。
今回は第1回シェル芸勉強会の3問目です。</p>
<blockquote>
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）
について以下の操作をしてください。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li>
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li>
</ul>
</div></blockquote>
<p>うわ・・・難しい・・・。どうしよ？リスカしよ
<a class="footnote-reference" href="#id17" id="id5">[4]</a>
。
・・・じゃなくて、とりあえずやりましょう。</p>
</div>
<div class="section" id="id6">
<h2>5.2. ディレクトリいじり<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、まずは <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下をまさぐるコードを書かねばいけません。
とりあえずリスト1のようなコードを書いてみました。
<tt class="docutils literal"><span class="pre">ls</span> <span class="pre">/etc/</span></tt> に相当するプログラムです。
今のところ <tt class="docutils literal"><span class="pre">ls</span></tt> のように1段目のディレクトリしか調べられませんが、
この後で2段目3段目とディレクトリを降りていって
全てのファイルのリストを作るコードにしていきます。</p>
<ul class="simple">
<li>リスト1: lsのようなもの（q1_3_1.hs）</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_3_1.hs
import System.Directory

<span class="nv">main</span> <span class="o">=</span> getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines
</pre></div>
</td></tr></table></div>
<p>実行してみましょう。リスト2のようにずらずらとファイルや
ディレクトリの名前が出てきます。</p>
<ul class="simple">
<li>リスト2: q1_3_1の実行</li>
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
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_3_1.hs
ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_1 | head -n 3
insserv
blkid.tab
tidy.conf
<span class="c">###ls -f /etc/と同じ出力###</span>
ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ls -f /etc/ | head -n 3
insserv
blkid.tab
tidy.conf
</pre></div>
</td></tr></table></div>
<p>　リスト1のコードですが、次のような意味があります。
まず、 <tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> の型はリスト3のように、
<tt class="docutils literal"><span class="pre">FilePath</span></tt> を引数にとって、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt>
を返すというものです。
<tt class="docutils literal"><span class="pre">FilePath</span></tt> というのは <tt class="docutils literal"><span class="pre">String</span></tt> の別名なのですが、
それはリスト3の後の二行のように、 <tt class="docutils literal"><span class="pre">:i</span></tt> （info）
というコマンドで調べることができます。</p>
<ul class="simple">
<li>リスト3: getDirectoryContentsの型とFilePathの情報</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/ :? for help
（略）
Prelude&gt; import System.Directory
Prelude System.Directory&gt; :t getDirectoryContents
getDirectoryContents :: FilePath -&gt; IO [FilePath]
Prelude System.Directory&gt; :i FilePath
type FilePath = String -- Defined in `GHC.IO&#39;
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の右側の <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt>
は、リストを <tt class="docutils literal"><span class="pre">unlines</span></tt> で1レコード1行にして、
<tt class="docutils literal"><span class="pre">putStr</span></tt> で標準出力に吐き出すということです。</p>
</div>
<div class="section" id="io">
<h2>5.3. IOってなんじゃい<a class="headerlink" href="#io" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　んで、とうとう <tt class="docutils literal"><span class="pre">IO</span></tt> の説明をするときがやってきてしまいました。
これが、Haskellを勉強しようとした100人のうち、
90人が死亡する原因となっているものです。</p>
<p>　今回はこれでおしまい。comming soon。</p>
<p>　・・・じゃなくて、真面目にやってきます。
えーっと、 <tt class="docutils literal"><span class="pre">IO</span></tt> というのは、
外から何か読み込んだものにつけるレッテルみたいなものです。
外というのは例えば標準入力であったり、
あるいは <tt class="docutils literal"><span class="pre">q1_3_1</span></tt> みたいにファイルの情報
だったりのことで、要はHaskellの世界に元々ないものです。
Haskellの世界には関数とその入出力しかないわけですが、
「外から読んだもの」は、そのどちらでもありません。
ですので、腫れ物のように扱われます。
その「腫れ物」である印が <tt class="docutils literal"><span class="pre">IO</span></tt> です。
外から読み込んで計算が修了するまで、
型についた「 <tt class="docutils literal"><span class="pre">IO</span></tt> 」は取り払うことができず、
普通の関数は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">hogehgoe</span></tt> という型を扱う事ができません。
しかし、少しだけ例外があり、
その例外の中でコソコソと普通の関数を使います。</p>
<p>　リスト1の4行目について、
行全体（main関数）の型を見てみましょう。
リストdddのようになります。</p>
<p>リストddd: q1_3_1.hsのmain関数の型</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import System.Directory
Prelude System.Directory&gt; :t <span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<span class="o">)</span>
<span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines<span class="o">)</span> :: IO <span class="o">()</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> という型であると分かりました。
関数としては何も引数にとらず、
ただ <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> を返すという意味になります。
<tt class="docutils literal"><span class="pre">()</span></tt> は「何にもねえよ」という意味です。
つまり、何も入出力しない関数であるとも解釈できますが、
プログラムを実行するとファイルのリストを標準出力に表示します。
実は、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> というのは、
「標準出力に何か表示する」という行為のことを指しています。
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">hogehoge</span></tt> という型を持っているものは、
「アクション」
<a class="footnote-reference" href="#id18" id="id7">[5]</a>
と呼ばれます。</p>
<p>　まだちょっと良く状況が分からんというところだと思いますが、
とりあえず次に行きます。
<tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> の型はリスト3で調べたので、
次は <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt> について。</p>
<ul class="simple">
<li>リスト4: putStr . unlinesの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t putStr
putStr :: String -&gt; IO <span class="o">()</span>
Prelude System.Directory&gt; :t unlines
unlines :: <span class="o">[</span>String<span class="o">]</span> -&gt; String
Prelude System.Directory&gt; :t <span class="o">(</span>putStr . unlines<span class="o">)</span>
<span class="o">(</span>putStr . unlines<span class="o">)</span> :: <span class="o">[</span>String<span class="o">]</span> -&gt; IO <span class="o">()</span>
</pre></div>
</td></tr></table></div>
<p>リスト4のように、 <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt>
の型は「文字列のリストを受け取ってアクションを返す」
です。</p>
<p>　次、謎の記号 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> ですが、リスト5のような感じです。
ちなみに <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> はバインド演算子と呼ばれます。</p>
<ul class="simple">
<li>リスト5: &gt;&gt;=の型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t <span class="o">(</span>&gt;&gt;<span class="o">=)</span>
<span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">Monad</span> <span class="pre">m</span> <span class="pre">=&gt;</span></tt> というのはまた別の機会に説明するとして
<a class="footnote-reference" href="#id19" id="id8">[6]</a>
とりあえず <tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">(a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b)</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt>
を解釈してみましょう。
これは <tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span></tt> と <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> という関数をとって、
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">b</span></tt> を返すということです。
リスト1の4行目について、書き換えてみましょう。
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を演算子ではなく関数のように扱ってみます。
リストgggのように、ちゃんと動きます。</p>
<ul class="simple">
<li>リストggg: <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を関数のように扱う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; <span class="o">(</span>&gt;&gt;<span class="o">=)</span> <span class="o">(</span>getDirectoryContents <span class="s2">&quot;/etc/&quot;</span><span class="o">)</span> <span class="o">(</span>putStr . unlines<span class="o">)</span>
（中略）
.
..
afpovertcp.cfg
aliases
aliases.db
...
</pre></div>
</td></tr></table></div>
<p>リスト5の型とリストgggを比べてみましょう。
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">getDirectoryContents</span> <span class="pre">&quot;/etc/&quot;</span></tt>
の型 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> に相当するので、
<tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> 、 <tt class="docutils literal"><span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">[FilePath]</span></tt>
ということになります。
そして、 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> は <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">unlines</span></tt>
の型 <tt class="docutils literal"><span class="pre">[String]</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">()</span></tt> に対応します。
<tt class="docutils literal"><span class="pre">a</span></tt> が <tt class="docutils literal"><span class="pre">[String]</span></tt> つまり <tt class="docutils literal"><span class="pre">[FilePath]</span></tt> 、
<tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> 、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">()</span></tt>
となります。ちょっと紙に書いて確かめていただきたいのですが、
型は互いに矛盾していません。</p>
</div>
<div class="section" id="id9">
<h2>5.4. アクションを避けて普通の関数を使う<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　型は矛盾していないのですが、また疑問が浮かびます。
リスト6のように、 <tt class="docutils literal"><span class="pre">unlines</span></tt> 関数はアクションとは無関係の関数です。
が、アクションだらけのところで使う事ができています。
これはなぜでしょう？</p>
<ul class="simple">
<li>リスト6: unlinesの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude System.Directory&gt; :t unlines
unlines :: <span class="o">[</span>String<span class="o">]</span> -&gt; String
</pre></div>
</td></tr></table></div>
<p>　もう一度 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt>
の型を見てみます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b
</pre></div>
</div>
<p>これの <tt class="docutils literal"><span class="pre">m</span></tt> が <tt class="docutils literal"><span class="pre">IO</span></tt> に対応するので、
置き換えてみましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre>IO a -&gt; <span class="o">(</span>a -&gt; IO b<span class="o">)</span> -&gt; IO b
</pre></div>
</div>
<p>関数の型 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">b</span></tt> のところで、
<tt class="docutils literal"><span class="pre">a</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> が取れています。
結局これが <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の役割で、
アクションの中身（ <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">a</span></tt> の <tt class="docutils literal"><span class="pre">a</span></tt> の部分）
に普通の関数を適用できるようにしています。
ただし、 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">b</span></tt> とあるように、
普通の関数を適用した後の出力には再び
<tt class="docutils literal"><span class="pre">IO</span></tt> をかぶせなければなりません。</p>
</div>
<div class="section" id="id10">
<h2>5.5. 親と自分を消し去る<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、 <tt class="docutils literal"><span class="pre">q1_3_1</span></tt> の出力のなかには、
リスト7のように親を指す <tt class="docutils literal"><span class="pre">..</span></tt>
と、自分を指す <tt class="docutils literal"><span class="pre">.</span></tt> が混ざっています。
もう一度やりたいことをおさらいすると、
今はこのコードを加筆して <tt class="docutils literal"><span class="pre">/etc/</span></tt>
下のファイルのリストを再帰的に作りたいのですが、
<tt class="docutils literal"><span class="pre">..</span></tt> や <tt class="docutils literal"><span class="pre">.</span></tt> が混ざっていると再帰処理が終わりません。</p>
<ul class="simple">
<li>リスト7: &#8221;.&#8221;と&#8221;..&#8221;が混ざりんぐ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_1 | grep <span class="s1">&#39;^\\.\\.*$&#39;</span>
.
..
</pre></div>
</td></tr></table></div>
<p>ということで、少し書き進めてリスト8のようなコードを作りました。
<tt class="docutils literal"><span class="pre">ls</span></tt> という関数を作りました。</p>
<ul class="simple">
<li>リスト8: q1_3_2.hs</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>cat q1_3_2.hs
import System.Directory

<span class="nv">main</span> <span class="o">=</span> ls <span class="s2">&quot;/etc/&quot;</span> &gt;&gt;<span class="o">=</span> putStr . unlines

ls :: String -&gt; IO <span class="o">[</span>FilePath<span class="o">]</span>
ls <span class="nv">dir</span> <span class="o">=</span> getDirectoryContents dir &gt;&gt;<span class="o">=</span> <span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">..</span></tt> と <tt class="docutils literal"><span class="pre">.</span></tt> が消えていることを確認しましょう。
リスト9のように、ドットで始まる行を抽出することで確認しました。</p>
<ul class="simple">
<li>リスト9: q1_3_2の実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>ghc q1_3_2.hs
ueda@remote:~/GIT/USPMAG/SRC<span class="nv">$ </span>./q1_3_2 | grep <span class="s1">&#39;^\\.&#39;</span>
.pwd.lock
</pre></div>
</td></tr></table></div>
<p>　さて、リスト8の6,7行目の型を追っていきましょう。
6行目のように関数 <tt class="docutils literal"><span class="pre">ls</span></tt> <a class="footnote-reference" href="#id20" id="id11">[7]</a>
の型は <tt class="docutils literal"><span class="pre">String</span> <span class="pre">-&gt;</span> <span class="pre">IO</span> <span class="pre">[FilePath]</span></tt>
ということで、 <tt class="docutils literal"><span class="pre">getDirectoryContents</span></tt> と同じです。
7行目の <tt class="docutils literal"><span class="pre">ls</span></tt> の中身は、
<tt class="docutils literal"><span class="pre">getDirectoryContents</span> <span class="pre">dir</span> <span class="pre">&gt;&gt;=</span></tt>
で、 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> をはぎ取って、
<tt class="docutils literal"><span class="pre">return</span> <span class="pre">.</span> <span class="pre">filter</span> <span class="pre">(`notElem`</span> <span class="pre">[&quot;.&quot;,&quot;..&quot;])</span></tt> に渡しています。
この部分（「右辺」と呼びましょう）の型は、
リスト10のようになります。
<tt class="docutils literal"><span class="pre">[[Char]]</span></tt> を <tt class="docutils literal"><span class="pre">[FilePath]</span></tt>
に置き換えて読むと、
ファイルパスのリストを受け取って、
ファイルパスのリストに
<tt class="docutils literal"><span class="pre">m</span></tt> つまり <tt class="docutils literal"><span class="pre">IO</span></tt> をかぶせて出力するというものになっています。</p>
<ul class="simple">
<li>リスト10: return...の型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span><span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span> <span class="o">)</span>
<span class="o">(</span><span class="k">return</span> . filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>,<span class="s2">&quot;..&quot;</span><span class="o">])</span> <span class="o">)</span>
 :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; <span class="o">[[</span>Char<span class="o">]]</span> -&gt; m <span class="o">[[</span>Char<span class="o">]]</span>
</pre></div>
</td></tr></table></div>
<p>右辺で面白いのは <tt class="docutils literal"><span class="pre">return</span></tt> です。
これも関数で、普通の言語の <tt class="docutils literal"><span class="pre">return</span></tt>
とは全然違うものです。
リスト11のように、普通の型に <tt class="docutils literal"><span class="pre">IO</span></tt>
をかぶせて出力します。
<tt class="docutils literal"><span class="pre">q1_3_2.hs</span></tt> では、「 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の出力には <tt class="docutils literal"><span class="pre">IO</span></tt>
がかぶさっていないといけない」
という条件を満たすために利用しています。</p>
<ul class="simple">
<li>リスト11: returnの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="k">return</span>
<span class="k">return</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; a -&gt; m a
</pre></div>
</td></tr></table></div>
<p>ということは、右辺から <tt class="docutils literal"><span class="pre">return</span></tt> を除いた
<tt class="docutils literal"><span class="pre">filter</span> <span class="pre">(`notElem`</span> <span class="pre">[&quot;.&quot;,</span> <span class="pre">&quot;..&quot;])</span></tt> の部分は、
リスト12のように <tt class="docutils literal"><span class="pre">IO</span></tt> の呪縛から解放され、
文字列を処理することに専念できるようになります。</p>
<ul class="simple">
<li>リスト12: IOの呪縛から解放された部分</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>, <span class="s2">&quot;..&quot;</span><span class="o">])</span>
filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span><span class="s2">&quot;.&quot;</span>, <span class="s2">&quot;..&quot;</span><span class="o">])</span> :: <span class="o">[[</span>Char<span class="o">]]</span> -&gt; <span class="o">[[</span>Char<span class="o">]]</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">notElem</span></tt> の使い方をリスト13に示して、
今回はおしまいとします。</p>
<ul class="simple">
<li>リスト13: notElem関数</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t notElem
notElem :: Eq <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; Bool
Prelude&gt; notElem 1 <span class="o">[</span>1,2,3<span class="o">]</span>
False
Prelude&gt; notElem 4 <span class="o">[</span>1,2,3<span class="o">]</span>
True
<span class="c">###関数を演算子として使うときには``で関数を囲む###</span>
Prelude&gt; 1 <span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span>1,2,3<span class="o">]</span>
False
<span class="c">###filterと併用するとリストから指定した要素を削除できる###</span>
Prelude&gt; filter <span class="o">(</span><span class="sb">`</span>notElem<span class="sb">`</span> <span class="o">[</span>1,2,3<span class="o">])</span> <span class="o">[</span>1,2,3,4,5<span class="o">]</span>
<span class="o">[</span>4,5<span class="o">]</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id12">
<h2>5.6. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は第1回シェル芸勉強会の3問目で、
ファイルの一覧をHaskellで処理する部分を書きました。
「アクション」面倒ですね・・・。
慣れが必要です。
ただ、私も完全に理解してはいないのですが、
数学的に正しいことを突き詰めた結果、
面倒くさいことになっているようです。
この手のものは慣れたらかえって自然に感じるものです。
こうやって、慣れた人と慣れていない人の溝は、
深まるばかりなんだなあ・・・。</p>
</div>
<div class="section" id="id13">
<h2>5.7. お知らせ：コード募集<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>USP友の会の幹事Uさんの夢の中でこのペンネームが誕生。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id15" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>順に助教、アドバイザリーフェロー、会長。ただし、今回はペンネームなので、名乗ってよいのかどうかは微妙。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id16" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>蛇足であるが本名は富山のブラックエンジェル上田隆一である。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id17" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id5">[4]</a></td><td>お菓子ではない。おかしいことは認める。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id18" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td>当然、漫画雑誌のことではない。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id19" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[6]</a></td><td>先月号で <tt class="docutils literal"><span class="pre">show</span></tt> の型を説明するときにも <tt class="docutils literal"><span class="pre">=&gt;</span></tt> が出てきました。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id20" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[7]</a></td><td>紛らわしい・・・</td></tr>
</tbody>
</table>
</div>
</div>

