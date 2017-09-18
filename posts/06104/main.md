---
Copyright: (C) Ryuichi Ueda
---

# USP Magazine 2014年11月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>8. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p><br />
<blockquote><br />
<div>USP友の会のシェル芸勉強会<br />
（脚注：シェルのワンライナー勉強会）は、<br />
日々、他の言語からの他流試合に晒されているのである。<br />
そこで上田は、Haskellで自ら他流試合を行い、<br />
さらにシェル芸勉強会をいじめる自傷行為に手を<br />
染めるのであった。</div></blockquote><br />
<div class="section" id="id1"><br />
<h2>8.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　こんちには。富山の元虚弱少年、ヘルパンギーナ上田です。<br />
かれこれ10日間以上、喉にヘルパンギーナビールスを<br />
飼っておりますが、なかなかこいつら死にません。<br />
名前が似ているのでビールスはビールで消毒するとよいと思い、<br />
毎日ビールを1リッター注入しているのですが、<br />
死なないどころか悪化しております。<br />
きっと私の中のビールス人口は、増えているものと思われます。<br />
おそらくこの原稿がUSP Magazineに掲載される頃には、<br />
ビールスで私の体が置換されて、<br />
ビールスが本連載の原稿を書いていることでしょう。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>8.2. 前回のおさらい<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さてそんな前置きはどうでもいいんです。<br />
体がしんどいですが今回も第1回シェル芸勉強会の3問目の途中から。<br />
問題はこんなのです。</p><br />
<blockquote><br />
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト<br />
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）<br />
について以下の操作をしてください。</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li><br />
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li><br />
</ul><br />
</div></blockquote><br />
<p>　前回は <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下のbashスクリプトを発見するところまで書きました。<br />
リスト1に前回最後のコードを再掲します。</p><br />
<ul class="simple"><br />
<li>リスト1: q1_3_6.hs</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_3_6</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">FileTools</span><br />
<span class="kr">import</span> <span class="k">qualified</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">B</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">find</span> <span class="s">&quot;/etc&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="n">judgeBashFile</span> <span class="o">&gt;&gt;=</span> <span class="n">print</span><br />
<br />
<span class="nf">judgeBashFile</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">(</span><span class="kt">String</span><span class="p">,</span><span class="kt">Bool</span><span class="p">)</span><br />
<span class="nf">judgeBashFile</span> <span class="n">file</span> <span class="ow">=</span> <span class="n">cat</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="p">((,)</span> <span class="n">file</span><span class="p">)</span> <span class="o">.</span> <span class="n">isBash</span><br />
 <span class="kr">where</span> <span class="n">isBash</span> <span class="n">bs</span> <span class="ow">=</span> <span class="kt">B</span><span class="o">.</span><span class="n">take</span> <span class="mi">11</span> <span class="n">bs</span> <span class="o">==</span> <span class="kt">B</span><span class="o">.</span><span class="n">pack</span> <span class="s">&quot;#!/bin/bash&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　実行結果をリスト2に示します。<br />
出力に <tt class="docutils literal"><span class="pre">grep</span></tt> をかけて発見した<br />
bashスクリプトのリストだけを表示しています。<br />
この4つのファイルを <tt class="docutils literal"><span class="pre">~/hoge/</span></tt> ディレクトリに移し、<br />
そのときに「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」<br />
に変換すれば問題完了です。</p><br />
<ul class="simple"><br />
<li>リスト2: q1_3_6の実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_6 | tr <span class="s1">&#39;)&#39;</span> <span class="s1">&#39;\\n&#39;</span> | grep True<br />
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/fakeroot&quot;</span>,True<br />
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzfgrep&quot;</span>,True<br />
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzmore&quot;</span>,True<br />
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzdiff&quot;</span>,True<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id3"><br />
<h2>8.3. ファイルをディレクトリにコピー<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、作業を開始します。<br />
まず、ファイルを <tt class="docutils literal"><span class="pre">~/hoge/</span></tt><br />
下にコピーするコードを書いてみました。<br />
リスト3にコードを示します。</p><br />
<ul class="simple"><br />
<li>リスト3: ファイルをコピーするコードを追加したq1_3_7.hs</li><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>cat q1_3_7.hs<br />
import FileTools<br />
import System.FilePath<br />
import qualified Data.ByteString.Lazy.Char8 as B<br />
<br />
<span class="nv">main</span> <span class="o">=</span> find <span class="s2">&quot;/etc&quot;</span> &gt;&gt;<span class="o">=</span> mapM judgeBashFile &gt;&gt;<span class="o">=</span> mapM handleBashFile<br />
<br />
judgeBashFile :: FilePath -&gt; IO <span class="o">(</span>String,Bool<span class="o">)</span><br />
judgeBashFile <span class="nv">file</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> <span class="k">return</span> . <span class="o">(</span>,<span class="o">)</span> file . isBash<br />
 where isBash <span class="nv">bs</span> <span class="o">=</span> B.take 11 <span class="nv">bs</span> <span class="o">==</span> B.pack <span class="s2">&quot;#!/bin/bash&quot;</span><br />
<br />
handleBashFile :: <span class="o">(</span>String,Bool<span class="o">)</span> -&gt; IO <span class="o">()</span><br />
handleBashFile <span class="o">(</span>file,False<span class="o">)</span> <span class="o">=</span> <span class="k">return</span> <span class="o">()</span><br />
handleBashFile <span class="o">(</span>file,True<span class="o">)</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> B.writeFile dest<br />
 where <span class="nv">dest</span> <span class="o">=</span> <span class="s2">&quot;/home/ueda/hoge/&quot;</span> ++ takeFileName file<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">main</span></tt> 関数で <tt class="docutils literal"><span class="pre">judgeBashFile</span></tt> の後ろに<br />
<tt class="docutils literal"><span class="pre">mapM</span> <span class="pre">handleBashFile</span></tt> と関数をつなげ、<br />
12〜15行目のように <tt class="docutils literal"><span class="pre">handleBashFile</span></tt> を実装します。<br />
13〜14行目ではパターンマッチをやっています。<br />
13行目はbashスクリプトでないものを無視する処理、<br />
14行目はコピー処理です。<br />
13行目の <tt class="docutils literal"><span class="pre">return</span> <span class="pre">()</span></tt> ですが、<br />
12行目の型が示すように型は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> です。<br />
なにも返すものがないときにこう書きます。<br />
ちなみに <tt class="docutils literal"><span class="pre">print</span></tt> 関数も型は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> です。<br />
<tt class="docutils literal"><span class="pre">print</span></tt> は画面に何か書き出しますが、<br />
関数としては何も返さないのでこうなります。</p><br />
<ul class="simple"><br />
<li>リスト4: printの型はIO ()</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t print<br />
print :: Show <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; IO <span class="o">()</span><br />
Prelude&gt; :t print <span class="s2">&quot;hell&quot;</span><br />
print <span class="s2">&quot;hell&quot;</span> :: IO <span class="o">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>この話はこれで終わりにしておきます。<br />
とにかく型を合わせる方法として覚えておくので<br />
構わないと考えます。</p><br />
<p>　処理として実際に重要なのは14, 15行目です。<br />
14行目では、先月号で <tt class="docutils literal"><span class="pre">FileTools.hs</span></tt><br />
内に定義した <tt class="docutils literal"><span class="pre">cat</span></tt> 関数で引っ張りだして、<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> で右側の <tt class="docutils literal"><span class="pre">B.writeFile</span></tt><br />
に渡しています。<br />
<tt class="docutils literal"><span class="pre">B.writeFile</span></tt> はその名の通りファイルに<br />
データを書き出す関数です。<br />
リスト5のように型を見ておきましょう。</p><br />
<ul class="simple"><br />
<li>リスト5: writeFileの型</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import qualified Data.ByteString.Lazy.Char8 as B<br />
Prelude B&gt; :t B.writeFile<br />
B.writeFile :: FilePath -&gt; B.ByteString -&gt; IO <span class="o">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">B.writeFile</span></tt> に渡している引数 <tt class="docutils literal"><span class="pre">dest</span></tt><br />
は、書き出し先のファイル名です。<br />
これは15行目で作っています。<br />
<tt class="docutils literal"><span class="pre">file</span></tt> からディレクトリの部分を除去して、<br />
<tt class="docutils literal"><span class="pre">/home/ueda/hoge/</span></tt> と行き先のディレクトリを<br />
ハードコーディングしています<br />
<a class="footnote-reference" href="#id14" id="id4">[6]</a><br />
。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>8.4. 改ざん処理を加える<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、さっさと終わらせましょう。<br />
1行目のシバン（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> ）<br />
を（ <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> ）<br />
に改ざん<br />
<a class="footnote-reference" href="#id15" id="id6">[7]</a><br />
します。</p><br />
<ul class="simple"><br />
<li>リスト6: シバンを変更する処理を加えたq1_3_8.hs</li><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>cat q1_3_8.hs<br />
import FileTools<br />
import System.FilePath<br />
import qualified Data.ByteString.Lazy.Char8 as B<br />
<br />
<span class="nv">main</span> <span class="o">=</span> find <span class="s2">&quot;/etc&quot;</span> &gt;&gt;<span class="o">=</span> mapM judgeBashFile &gt;&gt;<span class="o">=</span> mapM handleBashFile<br />
<br />
judgeBashFile :: FilePath -&gt; IO <span class="o">(</span>String,Bool<span class="o">)</span><br />
judgeBashFile <span class="nv">file</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> <span class="k">return</span> . <span class="o">(</span>,<span class="o">)</span> file . isBash<br />
 where isBash <span class="nv">bs</span> <span class="o">=</span> B.take 11 <span class="nv">bs</span> <span class="o">==</span> B.pack <span class="s2">&quot;#!/bin/bash&quot;</span><br />
<br />
handleBashFile :: <span class="o">(</span>String,Bool<span class="o">)</span> -&gt; IO <span class="o">()</span><br />
handleBashFile <span class="o">(</span>file,False<span class="o">)</span> <span class="o">=</span> <span class="k">return</span> <span class="o">()</span><br />
handleBashFile <span class="o">(</span>file,True<span class="o">)</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> B.writeFile dest . chg<br />
 where <span class="nv">dest</span> <span class="o">=</span> <span class="s2">&quot;/home/ueda/hoge/&quot;</span> ++ takeFileName file<br />
 chg <span class="nv">cs</span> <span class="o">=</span> B.append <span class="o">(</span>B.pack <span class="s2">&quot;#!/usr/local/bin/bash\\n&quot;</span><span class="o">)</span><br />
 <span class="o">(</span>B.unlines <span class="nv">$ </span>drop 1 <span class="nv">$ </span>B.lines cs<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト6に完成したコードを示します。<br />
<tt class="docutils literal"><span class="pre">copyBashFile</span></tt> 関数の名前は、<br />
処理にあわせて <tt class="docutils literal"><span class="pre">handleBashFile</span></tt> に変更しました。<br />
ファイルの中身を改ざんするため、<br />
16行目に <tt class="docutils literal"><span class="pre">chg</span></tt> という関数を定義して、<br />
14行目の一番後ろにくっつけています。<br />
これで、 <tt class="docutils literal"><span class="pre">B.writeFile</span> <span class="pre">dest</span></tt> に変更された内容が渡されます。<br />
16行目の <tt class="docutils literal"><span class="pre">B.append</span></tt> は二つの <tt class="docutils literal"><span class="pre">B.ByteString</span></tt><br />
をくっつけるて返す関数です。<br />
<tt class="docutils literal"><span class="pre">B.append</span></tt> の最初の引数は1行目のシバンと改行文字、<br />
次の引数は元のファイルの2行目以降です。</p><br />
<p>実行してみましょう。リスト7のように、<br />
<tt class="docutils literal"><span class="pre">hoge</span></tt> ディレクトリ中のファイルのシバンが<br />
<tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> になっていることが分かります。<br />
めでたしめでたし。</p><br />
<ul class="simple"><br />
<li>リスト7: q1_3_8の実行</li><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_8<br />
ueda\@remote:~/Study1_Q3<span class="nv">$ </span><span class="nb">cd</span> ~/hoge<br />
ueda\@remote:~/hoge<span class="nv">$ </span>head -n 1 *<br />
<span class="o">==</span>&gt; fakeroot &lt;<span class="o">==</span><br />
<span class="c">#!/usr/local/bin/bash</span><br />
<br />
<span class="o">==</span>&gt; lzdiff &lt;<span class="o">==</span><br />
<span class="c">#!/usr/local/bin/bash</span><br />
<br />
<span class="o">==</span>&gt; lzfgrep &lt;<span class="o">==</span><br />
<span class="c">#!/usr/local/bin/bash</span><br />
<br />
<span class="o">==</span>&gt; lzmore &lt;<span class="o">==</span><br />
<span class="c">#!/usr/local/bin/bash</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h2>8.5. 第一回勉強会4問目<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、地獄のような3問目がようやく終了したので、<br />
次に4問目に参ります<br />
<a class="footnote-reference" href="#id16" id="id8">[8]</a><br />
。4問目はこんな問題。</p><br />
<blockquote><br />
<div>次のような <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを作り、<br />
<tt class="docutils literal"><span class="pre">ans</span></tt> のように集計してください。</div></blockquote><br />
<p>　 <tt class="docutils literal"><span class="pre">ages</span></tt> と <tt class="docutils literal"><span class="pre">ans</span></tt> は図8のようなファイルです。<br />
どっちもシェル芸で簡単に<br />
<a class="footnote-reference" href="#id17" id="id9">[9]</a><br />
作れます。</p><br />
<ul class="simple"><br />
<li>リスト8: インプットする <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルと解答ファイル <tt class="docutils literal"><span class="pre">ans</span></tt></li><br />
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
22<br />
23<br />
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###agesは0〜109（年齢）をランダムに書いたもの###</span><br />
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span><span class="k">while</span> : ; <span class="k">do </span><span class="nb">echo</span> <span class="k">$((</span>RANDOM <span class="o">%</span> <span class="m">110</span><span class="k">))</span> ; <span class="k">done</span> |<br />
 head -n 100000 &gt; ages<br />
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>head -n 5 ages<br />
91<br />
35<br />
11<br />
100<br />
94<br />
<span class="c">###ansはagesの度数分布表###</span><br />
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>cat ages | awk <span class="s1">&#39;{print int($1/10)}&#39;</span> |<br />
 sort -n | count 1 1 | awk <span class="s1">&#39;{print $1*10&quot;〜&quot;$1*10+9,$2}&#39;</span> &gt; ans<br />
ueda\@remote:~/Study1_Q4/data<span class="nv">$ </span>cat ans<br />
0〜9 9158<br />
10〜19 9142<br />
20〜29 9052<br />
30〜39 9208<br />
40〜49 9081<br />
50〜59 9161<br />
60〜69 8938<br />
70〜79 8959<br />
80〜89 9143<br />
90〜99 9047<br />
100〜109 9111<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>8.6. 文字列を数字に変換<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、まず <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを読んでみましょう。<br />
読み込む際に、文字列から数字（Int型）に変換します。<br />
まず、リスト9の <tt class="docutils literal"><span class="pre">q1_4_1.hs</span></tt> を作ってみました。</p><br />
<ul class="simple"><br />
<li>リスト9: 標準入力からファイルを読み込んで数字のリストにするq1_4_1.hs</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q4<span class="nv">$ </span>cat q1_4_1.hs<br />
<span class="nv">main</span> <span class="o">=</span> <span class="k">do </span>cs &lt;- getContents<br />
 print <span class="o">[</span> <span class="nb">read </span>c :: Int | c &lt;- lines cs <span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>実行してみましょう。リスト10のように、<br />
Haskellのプログラム内部で数字のリストになっているのが分かります<br />
<a class="footnote-reference" href="#id18" id="id11">[10]</a><br />
。</p><br />
<ul class="simple"><br />
<li>リスト10: <tt class="docutils literal"><span class="pre">q1_4_1</span></tt> の出力</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4<span class="nv">$ </span>cat ./data/ages | ./q1_4_1 | head -c 30<br />
<span class="o">[</span>91,35,11,100,94,9,72,105,97,1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト9のコードでは、<br />
6月号で出て来たリスト内包表記が使われています。<br />
<tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> の出力は読み込んだテキストファイルを<br />
1行1要素のリストにしたもので、そこから一つずつ<br />
<tt class="docutils literal"><span class="pre">read</span></tt> 関数で数字に変換しています。<br />
Python書く人にはなじみ深いかと思います。</p><br />
<p>　次に <tt class="docutils literal"><span class="pre">read</span> <span class="pre">c</span> <span class="pre">::</span> <span class="pre">Int</span></tt> を説明します。<br />
この呪文は、入力 <tt class="docutils literal"><span class="pre">c</span></tt> を<br />
Int型にして出力するという意味になります。<br />
次のように、出力の型が決まっていないので、<br />
なんらかの方法で指定しなければいけませんが、<br />
リストのように <tt class="docutils literal"><span class="pre">::</span> <span class="pre">Int</span></tt> と書いてInt型を指定します。<br />
ちょっと不格好ですね。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="nb">read</span><br />
<span class="nb">read</span> :: Read <span class="nv">a</span> <span class="o">=</span>&gt; String -&gt; a<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次に、何十代かをカウントするというお題なので、<br />
各年齢を、例えば19なら10、8なら0と1の位をゼロにします。</p><br />
<ul class="simple"><br />
<li>リスト12: <tt class="docutils literal"><span class="pre">q1_4_1</span></tt> の出力</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4<span class="nv">$ </span>cat q1_4_2.hs<br />
<span class="nv">main</span> <span class="o">=</span> <span class="k">do </span>cs &lt;- getContents<br />
 print <span class="o">[</span> 10 * <span class="o">(</span> <span class="o">(</span><span class="nb">read </span>c :: Int<span class="o">)</span> <span class="sb">`</span>div<span class="sb">`</span> 10 <span class="o">)</span> | c &lt;- lines cs <span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>整数の割り算には <tt class="docutils literal"><span class="pre">div</span></tt> を使います。<br />
次のように、divと <tt class="docutils literal"><span class="pre">/</span></tt> では扱う型が違います。<br />
<tt class="docutils literal"><span class="pre">div</span></tt> で整数を割ると、余りは切り捨てられます。<br />
リスト12の計算は、<br />
10で割って余りを切り捨てて後から<br />
10をかけるというものになっています。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t div<br />
div :: Integral <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; a<br />
Prelude&gt; :t <span class="o">(</span>/<span class="o">)</span><br />
<span class="o">(</span>/<span class="o">)</span> :: Fractional <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; a<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ところで、 <tt class="docutils literal"><span class="pre">div</span></tt> の両側にはバッククォートがついていますが、<br />
つけるとつけないでは、このように書く順番が変わります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; 6 <span class="sb">`</span>div<span class="sb">`</span> 3<br />
2<br />
Prelude&gt; div 6 3<br />
2<br />
</pre></div><br />
</td></tr></table></div><br />
<p>要は数字を両側に置かないと演算子っぽくないので、<br />
バッククォートをつけると真ん中に置けるよという<br />
決まりになっているのです。<br />
考えてみれば関数も演算子も、<br />
引数をいくつかとって答えを出力するものなので、<br />
実は本質的な違いがないものだと言えます。</p><br />
<p>では、今月はここまでにしましょう。<br />
でもこの問題、3問目と違ってすぐに終わりそうですね。</p><br />
</div><br />
<div class="section" id="id12"><br />
<h2>8.7. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は第一回シェル芸勉強会の3問目の解答を完成させ、<br />
4問目に突入しました。<br />
3問目はHaskell入門というには難しすぎましたが、<br />
4問目はなんとかなりそうです。<br />
本連載、シェル芸勉強会で出題した順で扱っているので、<br />
難易度は簡単になったり難しくなったりします。<br />
ですので、ちょっと待っていれば自分のスキルにあった<br />
問題が出るかもしれません。辛抱強くお付き合いを。</p><br />
</div><br />
<div class="section" id="id13"><br />
<h2>8.8. お知らせ：コード募集<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　本稿で出た問題のHaskellのコードを、<br />
名前あるいはハンドルネームと共に送ってください。<br />
短いもの、あるいは変態的なものをお願いいたします。</p><br />
<p>email: 編集部のメールアドレス</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id14" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[6]</a></td><td>いい加減といえばいい加減。<br />
しかし、万が一再利用するときにリファクタリングすればいいだけの話だと思う。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id15" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id6">[7]</a></td><td>正しくは置換あるいは変更。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id16" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id8">[8]</a></td><td>しんどい</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id17" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id9">[9]</a></td><td>簡単かどうかは、貴方次第！</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id18" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id11">[10]</a></td><td>printしたらまた文字列に戻ってしまいますが。</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

