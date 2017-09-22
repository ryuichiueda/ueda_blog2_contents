---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年11月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>8. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>USP友の会のシェル芸勉強会
（脚注：シェルのワンライナー勉強会）は、
日々、他の言語からの他流試合に晒されているのである。
そこで上田は、Haskellで自ら他流試合を行い、
さらにシェル芸勉強会をいじめる自傷行為に手を
染めるのであった。</div></blockquote>
<div class="section" id="id1">
<h2>8.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　こんちには。富山の元虚弱少年、ヘルパンギーナ上田です。
かれこれ10日間以上、喉にヘルパンギーナビールスを
飼っておりますが、なかなかこいつら死にません。
名前が似ているのでビールスはビールで消毒するとよいと思い、
毎日ビールを1リッター注入しているのですが、
死なないどころか悪化しております。
きっと私の中のビールス人口は、増えているものと思われます。
おそらくこの原稿がUSP Magazineに掲載される頃には、
ビールスで私の体が置換されて、
ビールスが本連載の原稿を書いていることでしょう。</p>
</div>
<div class="section" id="id2">
<h2>8.2. 前回のおさらい<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さてそんな前置きはどうでもいいんです。
体がしんどいですが今回も第1回シェル芸勉強会の3問目の途中から。
問題はこんなのです。</p>
<blockquote>
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）
について以下の操作をしてください。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li>
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li>
</ul>
</div></blockquote>
<p>　前回は <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下のbashスクリプトを発見するところまで書きました。
リスト1に前回最後のコードを再掲します。</p>
<ul class="simple">
<li>リスト1: q1_3_6.hs</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_3_6</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">FileTools</span>
<span class="kr">import</span> <span class="k">qualified</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">B</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">find</span> <span class="s">&quot;/etc&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="n">judgeBashFile</span> <span class="o">&gt;&gt;=</span> <span class="n">print</span>

<span class="nf">judgeBashFile</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">(</span><span class="kt">String</span><span class="p">,</span><span class="kt">Bool</span><span class="p">)</span>
<span class="nf">judgeBashFile</span> <span class="n">file</span> <span class="ow">=</span> <span class="n">cat</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="p">((,)</span> <span class="n">file</span><span class="p">)</span> <span class="o">.</span> <span class="n">isBash</span>
 <span class="kr">where</span> <span class="n">isBash</span> <span class="n">bs</span> <span class="ow">=</span> <span class="kt">B</span><span class="o">.</span><span class="n">take</span> <span class="mi">11</span> <span class="n">bs</span> <span class="o">==</span> <span class="kt">B</span><span class="o">.</span><span class="n">pack</span> <span class="s">&quot;#!/bin/bash&quot;</span>
</pre></div>
</td></tr></table></div>
<p>　実行結果をリスト2に示します。
出力に <tt class="docutils literal"><span class="pre">grep</span></tt> をかけて発見した
bashスクリプトのリストだけを表示しています。
この4つのファイルを <tt class="docutils literal"><span class="pre">~/hoge/</span></tt> ディレクトリに移し、
そのときに「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」
に変換すれば問題完了です。</p>
<ul class="simple">
<li>リスト2: q1_3_6の実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_6 | tr <span class="s1">&#39;)&#39;</span> <span class="s1">&#39;\\n&#39;</span> | grep True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/fakeroot&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzfgrep&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzmore&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzdiff&quot;</span>,True
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id3">
<h2>8.3. ファイルをディレクトリにコピー<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、作業を開始します。
まず、ファイルを <tt class="docutils literal"><span class="pre">~/hoge/</span></tt>
下にコピーするコードを書いてみました。
リスト3にコードを示します。</p>
<ul class="simple">
<li>リスト3: ファイルをコピーするコードを追加したq1_3_7.hs</li>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>cat q1_3_7.hs
import FileTools
import System.FilePath
import qualified Data.ByteString.Lazy.Char8 as B

<span class="nv">main</span> <span class="o">=</span> find <span class="s2">&quot;/etc&quot;</span> &gt;&gt;<span class="o">=</span> mapM judgeBashFile &gt;&gt;<span class="o">=</span> mapM handleBashFile

judgeBashFile :: FilePath -&gt; IO <span class="o">(</span>String,Bool<span class="o">)</span>
judgeBashFile <span class="nv">file</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> <span class="k">return</span> . <span class="o">(</span>,<span class="o">)</span> file . isBash
 where isBash <span class="nv">bs</span> <span class="o">=</span> B.take 11 <span class="nv">bs</span> <span class="o">==</span> B.pack <span class="s2">&quot;#!/bin/bash&quot;</span>

handleBashFile :: <span class="o">(</span>String,Bool<span class="o">)</span> -&gt; IO <span class="o">()</span>
handleBashFile <span class="o">(</span>file,False<span class="o">)</span> <span class="o">=</span> <span class="k">return</span> <span class="o">()</span>
handleBashFile <span class="o">(</span>file,True<span class="o">)</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> B.writeFile dest
 where <span class="nv">dest</span> <span class="o">=</span> <span class="s2">&quot;/home/ueda/hoge/&quot;</span> ++ takeFileName file
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">main</span></tt> 関数で <tt class="docutils literal"><span class="pre">judgeBashFile</span></tt> の後ろに
<tt class="docutils literal"><span class="pre">mapM</span> <span class="pre">handleBashFile</span></tt> と関数をつなげ、
12〜15行目のように <tt class="docutils literal"><span class="pre">handleBashFile</span></tt> を実装します。
13〜14行目ではパターンマッチをやっています。
13行目はbashスクリプトでないものを無視する処理、
14行目はコピー処理です。
13行目の <tt class="docutils literal"><span class="pre">return</span> <span class="pre">()</span></tt> ですが、
12行目の型が示すように型は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> です。
なにも返すものがないときにこう書きます。
ちなみに <tt class="docutils literal"><span class="pre">print</span></tt> 関数も型は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> です。
<tt class="docutils literal"><span class="pre">print</span></tt> は画面に何か書き出しますが、
関数としては何も返さないのでこうなります。</p>
<ul class="simple">
<li>リスト4: printの型はIO ()</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t print
print :: Show <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; IO <span class="o">()</span>
Prelude&gt; :t print <span class="s2">&quot;hell&quot;</span>
print <span class="s2">&quot;hell&quot;</span> :: IO <span class="o">()</span>
</pre></div>
</td></tr></table></div>
<p>この話はこれで終わりにしておきます。
とにかく型を合わせる方法として覚えておくので
構わないと考えます。</p>
<p>　処理として実際に重要なのは14, 15行目です。
14行目では、先月号で <tt class="docutils literal"><span class="pre">FileTools.hs</span></tt>
内に定義した <tt class="docutils literal"><span class="pre">cat</span></tt> 関数で引っ張りだして、
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> で右側の <tt class="docutils literal"><span class="pre">B.writeFile</span></tt>
に渡しています。
<tt class="docutils literal"><span class="pre">B.writeFile</span></tt> はその名の通りファイルに
データを書き出す関数です。
リスト5のように型を見ておきましょう。</p>
<ul class="simple">
<li>リスト5: writeFileの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import qualified Data.ByteString.Lazy.Char8 as B
Prelude B&gt; :t B.writeFile
B.writeFile :: FilePath -&gt; B.ByteString -&gt; IO <span class="o">()</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">B.writeFile</span></tt> に渡している引数 <tt class="docutils literal"><span class="pre">dest</span></tt>
は、書き出し先のファイル名です。
これは15行目で作っています。
<tt class="docutils literal"><span class="pre">file</span></tt> からディレクトリの部分を除去して、
<tt class="docutils literal"><span class="pre">/home/ueda/hoge/</span></tt> と行き先のディレクトリを
ハードコーディングしています
<a class="footnote-reference" href="#id14" id="id4">[6]</a>
。</p>
</div>
<div class="section" id="id5">
<h2>8.4. 改ざん処理を加える<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、さっさと終わらせましょう。
1行目のシバン（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> ）
を（ <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> ）
に改ざん
<a class="footnote-reference" href="#id15" id="id6">[7]</a>
します。</p>
<ul class="simple">
<li>リスト6: シバンを変更する処理を加えたq1_3_8.hs</li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>cat q1_3_8.hs
import FileTools
import System.FilePath
import qualified Data.ByteString.Lazy.Char8 as B

<span class="nv">main</span> <span class="o">=</span> find <span class="s2">&quot;/etc&quot;</span> &gt;&gt;<span class="o">=</span> mapM judgeBashFile &gt;&gt;<span class="o">=</span> mapM handleBashFile

judgeBashFile :: FilePath -&gt; IO <span class="o">(</span>String,Bool<span class="o">)</span>
judgeBashFile <span class="nv">file</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> <span class="k">return</span> . <span class="o">(</span>,<span class="o">)</span> file . isBash
 where isBash <span class="nv">bs</span> <span class="o">=</span> B.take 11 <span class="nv">bs</span> <span class="o">==</span> B.pack <span class="s2">&quot;#!/bin/bash&quot;</span>

handleBashFile :: <span class="o">(</span>String,Bool<span class="o">)</span> -&gt; IO <span class="o">()</span>
handleBashFile <span class="o">(</span>file,False<span class="o">)</span> <span class="o">=</span> <span class="k">return</span> <span class="o">()</span>
handleBashFile <span class="o">(</span>file,True<span class="o">)</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> B.writeFile dest . chg
 where <span class="nv">dest</span> <span class="o">=</span> <span class="s2">&quot;/home/ueda/hoge/&quot;</span> ++ takeFileName file
 chg <span class="nv">cs</span> <span class="o">=</span> B.append <span class="o">(</span>B.pack <span class="s2">&quot;#!/usr/local/bin/bash\\n&quot;</span><span class="o">)</span>
 <span class="o">(</span>B.unlines <span class="nv">$ </span>drop 1 <span class="nv">$ </span>B.lines cs<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>リスト6に完成したコードを示します。
<tt class="docutils literal"><span class="pre">copyBashFile</span></tt> 関数の名前は、
処理にあわせて <tt class="docutils literal"><span class="pre">handleBashFile</span></tt> に変更しました。
ファイルの中身を改ざんするため、
16行目に <tt class="docutils literal"><span class="pre">chg</span></tt> という関数を定義して、
14行目の一番後ろにくっつけています。
これで、 <tt class="docutils literal"><span class="pre">B.writeFile</span> <span class="pre">dest</span></tt> に変更された内容が渡されます。
16行目の <tt class="docutils literal"><span class="pre">B.append</span></tt> は二つの <tt class="docutils literal"><span class="pre">B.ByteString</span></tt>
をくっつけるて返す関数です。
<tt class="docutils literal"><span class="pre">B.append</span></tt> の最初の引数は1行目のシバンと改行文字、
次の引数は元のファイルの2行目以降です。</p>
<p>実行してみましょう。リスト7のように、
<tt class="docutils literal"><span class="pre">hoge</span></tt> ディレクトリ中のファイルのシバンが
<tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> になっていることが分かります。
めでたしめでたし。</p>
<ul class="simple">
<li>リスト7: q1_3_8の実行</li>
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
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_8
ueda\@remote:~/Study1_Q3<span class="nv">$ </span><span class="nb">cd</span> ~/hoge
ueda\@remote:~/hoge<span class="nv">$ </span>head -n 1 *
<span class="o">==</span>&gt; fakeroot &lt;<span class="o">==</span>
<span class="c">#!/usr/local/bin/bash</span>

<span class="o">==</span>&gt; lzdiff &lt;<span class="o">==</span>
<span class="c">#!/usr/local/bin/bash</span>

<span class="o">==</span>&gt; lzfgrep &lt;<span class="o">==</span>
<span class="c">#!/usr/local/bin/bash</span>

<span class="o">==</span>&gt; lzmore &lt;<span class="o">==</span>
<span class="c">#!/usr/local/bin/bash</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h2>8.5. 第一回勉強会4問目<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、地獄のような3問目がようやく終了したので、
次に4問目に参ります
<a class="footnote-reference" href="#id16" id="id8">[8]</a>
。4問目はこんな問題。</p>
<blockquote>
<div>次のような <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを作り、
<tt class="docutils literal"><span class="pre">ans</span></tt> のように集計してください。</div></blockquote>
<p>　 <tt class="docutils literal"><span class="pre">ages</span></tt> と <tt class="docutils literal"><span class="pre">ans</span></tt> は図8のようなファイルです。
どっちもシェル芸で簡単に
<a class="footnote-reference" href="#id17" id="id9">[9]</a>
作れます。</p>
<ul class="simple">
<li>リスト8: インプットする <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルと解答ファイル <tt class="docutils literal"><span class="pre">ans</span></tt></li>
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###agesは0〜109（年齢）をランダムに書いたもの###</span>
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span><span class="k">while</span> : ; <span class="k">do </span><span class="nb">echo</span> <span class="k">$((</span>RANDOM <span class="o">%</span> <span class="m">110</span><span class="k">))</span> ; <span class="k">done</span> |
 head -n 100000 &gt; ages
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>head -n 5 ages
91
35
11
100
94
<span class="c">###ansはagesの度数分布表###</span>
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>cat ages | awk <span class="s1">&#39;{print int($1/10)}&#39;</span> |
 sort -n | count 1 1 | awk <span class="s1">&#39;{print $1*10&quot;〜&quot;$1*10+9,$2}&#39;</span> &gt; ans
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>cat ans
0〜9 9158
10〜19 9142
20〜29 9052
30〜39 9208
40〜49 9081
50〜59 9161
60〜69 8938
70〜79 8959
80〜89 9143
90〜99 9047
100〜109 9111
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>8.6. 文字列を数字に変換<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、まず <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを読んでみましょう。
読み込む際に、文字列から数字（Int型）に変換します。
まず、リスト9の <tt class="docutils literal"><span class="pre">q1_4_1.hs</span></tt> を作ってみました。</p>
<ul class="simple">
<li>リスト9: 標準入力からファイルを読み込んで数字のリストにするq1_4_1.hs</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q4<span class="nv">$ </span>cat q1_4_1.hs
<span class="nv">main</span> <span class="o">=</span> <span class="k">do </span>cs &lt;- getContents
 print <span class="o">[</span> <span class="nb">read </span>c :: Int | c &lt;- lines cs <span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>実行してみましょう。リスト10のように、
Haskellのプログラム内部で数字のリストになっているのが分かります
<a class="footnote-reference" href="#id18" id="id11">[10]</a>
。</p>
<ul class="simple">
<li>リスト10: <tt class="docutils literal"><span class="pre">q1_4_1</span></tt> の出力</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4<span class="nv">$ </span>cat ./data/ages | ./q1_4_1 | head -c 30
<span class="o">[</span>91,35,11,100,94,9,72,105,97,1
</pre></div>
</td></tr></table></div>
<p>　リスト9のコードでは、
6月号で出て来たリスト内包表記が使われています。
<tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> の出力は読み込んだテキストファイルを
1行1要素のリストにしたもので、そこから一つずつ
<tt class="docutils literal"><span class="pre">read</span></tt> 関数で数字に変換しています。
Python書く人にはなじみ深いかと思います。</p>
<p>　次に <tt class="docutils literal"><span class="pre">read</span> <span class="pre">c</span> <span class="pre">::</span> <span class="pre">Int</span></tt> を説明します。
この呪文は、入力 <tt class="docutils literal"><span class="pre">c</span></tt> を
Int型にして出力するという意味になります。
次のように、出力の型が決まっていないので、
なんらかの方法で指定しなければいけませんが、
リストのように <tt class="docutils literal"><span class="pre">::</span> <span class="pre">Int</span></tt> と書いてInt型を指定します。
ちょっと不格好ですね。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="nb">read</span>
<span class="nb">read</span> :: Read <span class="nv">a</span> <span class="o">=</span>&gt; String -&gt; a
</pre></div>
</td></tr></table></div>
<p>　次に、何十代かをカウントするというお題なので、
各年齢を、例えば19なら10、8なら0と1の位をゼロにします。</p>
<ul class="simple">
<li>リスト12: <tt class="docutils literal"><span class="pre">q1_4_1</span></tt> の出力</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4<span class="nv">$ </span>cat q1_4_2.hs
<span class="nv">main</span> <span class="o">=</span> <span class="k">do </span>cs &lt;- getContents
 print <span class="o">[</span> 10 * <span class="o">(</span> <span class="o">(</span><span class="nb">read </span>c :: Int<span class="o">)</span> <span class="sb">`</span>div<span class="sb">`</span> 10 <span class="o">)</span> | c &lt;- lines cs <span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>整数の割り算には <tt class="docutils literal"><span class="pre">div</span></tt> を使います。
次のように、divと <tt class="docutils literal"><span class="pre">/</span></tt> では扱う型が違います。
<tt class="docutils literal"><span class="pre">div</span></tt> で整数を割ると、余りは切り捨てられます。
リスト12の計算は、
10で割って余りを切り捨てて後から
10をかけるというものになっています。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t div
div :: Integral <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; a
Prelude&gt; :t <span class="o">(</span>/<span class="o">)</span>
<span class="o">(</span>/<span class="o">)</span> :: Fractional <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; a
</pre></div>
</td></tr></table></div>
<p>　ところで、 <tt class="docutils literal"><span class="pre">div</span></tt> の両側にはバッククォートがついていますが、
つけるとつけないでは、このように書く順番が変わります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; 6 <span class="sb">`</span>div<span class="sb">`</span> 3
2
Prelude&gt; div 6 3
2
</pre></div>
</td></tr></table></div>
<p>要は数字を両側に置かないと演算子っぽくないので、
バッククォートをつけると真ん中に置けるよという
決まりになっているのです。
考えてみれば関数も演算子も、
引数をいくつかとって答えを出力するものなので、
実は本質的な違いがないものだと言えます。</p>
<p>では、今月はここまでにしましょう。
でもこの問題、3問目と違ってすぐに終わりそうですね。</p>
</div>
<div class="section" id="id12">
<h2>8.7. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は第一回シェル芸勉強会の3問目の解答を完成させ、
4問目に突入しました。
3問目はHaskell入門というには難しすぎましたが、
4問目はなんとかなりそうです。
本連載、シェル芸勉強会で出題した順で扱っているので、
難易度は簡単になったり難しくなったりします。
ですので、ちょっと待っていれば自分のスキルにあった
問題が出るかもしれません。辛抱強くお付き合いを。</p>
</div>
<div class="section" id="id13">
<h2>8.8. お知らせ：コード募集<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[6]</a></td><td>いい加減といえばいい加減。
しかし、万が一再利用するときにリファクタリングすればいいだけの話だと思う。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id15" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[7]</a></td><td>正しくは置換あるいは変更。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id16" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[8]</a></td><td>しんどい</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id17" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id9">[9]</a></td><td>簡単かどうかは、貴方次第！</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id18" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[10]</a></td><td>printしたらまた文字列に戻ってしまいますが。</td></tr>
</tbody>
</table>
</div>
</div>

