---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2015年2月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>11. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア
状態なので，連載しながら開発しようと思い立った上田は，
不幸にも黒塗りの高級車に追突してしまう．後輩をかばい
すべての責任を負った上田に対し，車の主，暴力団員谷岡に
言い渡された示談の条件とは...．</div></blockquote>
<div class="section" id="id1">
<h2>11.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　 <a class="footnote-reference" href="#id11" id="id2">[1]</a> 。富山の徒花 <a class="footnote-reference" href="#id13" id="id3">[2]</a> 、
ブラックエンジェル上田です。冬ですね。
皆様は冬の楽しみと言えば何でしょうか？
私はありません。全くありません。</p>
</div>
<div class="section" id="id4">
<h2>11.2. 本日やること<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　と、あっという間に冒頭の挨拶が終わりましたので、
今月はたっぷりHaskellを書くことにしましょう。
前回からやっている通り、今回もHaskell版のOpen usp Tukubai
の開発を続けることとします。</p>
<p>　サンプルコードを含んだブランチは、</p>
<blockquote>
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote>
<p>にありますので，参考にしながらHaskellを勉強してみてください．</p>
<p>　前回はmapというコマンドを作っており、
標準入出力からの字の出し入れ、
終了ステータスの適切な出力を実装しました。
今回はいよいよmapで行う処理の中身に入っていきます。</p>
<p>　今回実装する機能を見ましょう。
図1のようなデータがあるとします。
区切り文字はすべて半角スペースです。</p>
<ul class="simple">
<li>図1: 入力データ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data
a あ 1
b い 2
b う 3
</pre></div>
</td></tr></table></div>
<p>このデータを、図2のように「第1フィールドを縦軸」、
「第2フィールドを横軸」にして表にするのがmapです。</p>
<ul class="simple">
<li>図2: 出力データ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>1 data
* あ い う
a 1 0 0
b 0 2 3
<span class="c">###出力を揃えるときにはketaを使う###</span>
<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>1 data | keta
* あ い う
a 1 0 0
b 0 2 3
</pre></div>
</td></tr></table></div>
<p>オプションで指定している <tt class="docutils literal"><span class="pre">num=1</span></tt>
は、左から1列目までを縦軸扱いするということです。</p>
</div>
<div class="section" id="id5">
<h2>11.3. オプションの処理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　んで、最初に実装するのは <tt class="docutils literal"><span class="pre">num=&lt;数字&gt;</span></tt>
の数字の部分を読み込む処理です。
ちょっと長いですが、この部分を実装した <tt class="docutils literal"><span class="pre">map.4.hs</span></tt>
を全部載っけておきます。</p>
<ul class="simple">
<li>図3: numオプションから数字を読み込む処理を入れたmap.4.hs</li>
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
40
41
42</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span>
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span>
<span class="kr">import</span> <span class="nn">System.IO</span>
<span class="kr">import</span> <span class="nn">System.Exit</span>
<span class="kr">import</span> <span class="nn">Text.Read</span>

<span class="nf">showUsage</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">showUsage</span> <span class="ow">=</span> <span class="kr">do</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span>
 <span class="s">&quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; </span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span>
 <span class="s">&quot;Thu Oct 23 08:52:44 JST 2014</span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span>
 <span class="s">&quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span>
 <span class="n">exitWith</span> <span class="p">(</span><span class="kt">ExitFailure</span> <span class="mi">1</span><span class="p">)</span>

<span class="nf">die</span> <span class="n">str</span> <span class="ow">=</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span>
 <span class="s">&quot;Error[map] : &quot;</span> <span class="o">++</span> <span class="n">str</span> <span class="o">++</span> <span class="s">&quot;</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="n">exitWith</span> <span class="p">(</span><span class="kt">ExitFailure</span> <span class="mi">1</span><span class="p">)</span>

<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span>
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span>
 <span class="p">[</span><span class="s">&quot;-h&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>
 <span class="p">[</span><span class="s">&quot;--help&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">main&#39;</span> <span class="p">(</span><span class="n">getNum</span> <span class="n">num</span><span class="p">)</span>
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="n">main&#39;</span> <span class="p">(</span><span class="n">getNum</span> <span class="n">num</span><span class="p">)</span>
 <span class="kr">_</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>

<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span>
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span>
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span>

<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span> <span class="ow">-&gt;</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main&#39;</span> <span class="p">(</span><span class="kt">Left</span> <span class="n">str</span><span class="p">)</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">die</span> <span class="n">str</span>
<span class="nf">main&#39;</span> <span class="p">(</span><span class="kt">Right</span> <span class="n">num</span><span class="p">)</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">print</span> <span class="n">num</span> <span class="c1">-- for debug</span>

<span class="nf">getNum</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span>
<span class="nf">getNum</span> <span class="p">(</span><span class="n">&#39;n&#39;</span><span class="kt">:</span><span class="n">&#39;u&#39;</span><span class="kt">:</span><span class="n">&#39;m&#39;</span><span class="kt">:</span><span class="sc">&#39;=&#39;</span><span class="kt">:</span><span class="n">str</span><span class="p">)</span> <span class="ow">=</span> <span class="n">getNum&#39;</span> <span class="p">(</span><span class="n">readMaybe</span> <span class="n">str</span><span class="p">)</span>
<span class="nf">getNum</span> <span class="kr">_</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;no num option&quot;</span>

<span class="nf">getNum&#39;</span> <span class="ow">::</span> <span class="kt">Maybe</span> <span class="kt">Int</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span>
<span class="nf">getNum&#39;</span> <span class="kt">Nothing</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;invalid number for num option&quot;</span>
<span class="nf">getNum&#39;</span> <span class="p">(</span><span class="kt">Just</span> <span class="n">n</span><span class="p">)</span>
 <span class="o">|</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">=</span> <span class="kt">Right</span> <span class="n">n</span>
 <span class="o">|</span> <span class="n">otherwise</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;invalid number for num option&quot;</span>
</pre></div>
</td></tr></table></div>
<p>　・・・大変です。普通の言語なら関数を
一個作ってちょろっと試せばよいのですが、
Haskellの場合は型と関数の接続先を
考えてからでないと関数を書けないので大変です。
ただ、この方がトップダウンな思考は身につくと思います。</p>
<p>　さて、このコードで重要なのは何と言っても
<tt class="docutils literal"><span class="pre">getNum</span></tt> 関数です。この関数は、オプションを読み込んで、
<tt class="docutils literal"><span class="pre">num=</span></tt> の後ろの数字をInt型で返すのが第一の目的です。
ただ、話はそんなに簡単ではありません。
変な数字が入っていたらそれを通知しなければなりません。
このとき、例えば数字でなくて <tt class="docutils literal"><span class="pre">num=aaa</span></tt> とか書いてあったら
-1を返すなど、Int型で済ませる方法もありますが、
ここではもう少しこだわって <tt class="docutils literal"><span class="pre">Either</span></tt> と <tt class="docutils literal"><span class="pre">Maybe</span></tt>
というものを使っています。</p>
<p>　まず、35〜42行目に出てくる <tt class="docutils literal"><span class="pre">Left</span></tt> と <tt class="docutils literal"><span class="pre">Right</span></tt> から、
<tt class="docutils literal"><span class="pre">Either</span></tt> を理解してみましょう。
図4を見ながら説明すると分かりやすいと思いますが、
<tt class="docutils literal"><span class="pre">Left</span></tt> は引数にとったものを <tt class="docutils literal"><span class="pre">Either</span> <span class="pre">a</span> <span class="pre">b</span></tt>
の左側の <tt class="docutils literal"><span class="pre">a</span></tt> に、 <tt class="docutils literal"><span class="pre">Right</span></tt> は右側の <tt class="docutils literal"><span class="pre">b</span></tt>
に包んで返します。</p>
<ul class="simple">
<li>図4: LeftとRightの型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Left</span>
<span class="kt">Left</span> <span class="ow">::</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="n">a</span> <span class="n">b</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Right</span>
<span class="kt">Right</span> <span class="ow">::</span> <span class="n">b</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="n">a</span> <span class="n">b</span>
</pre></div>
</td></tr></table></div>
<p>　この包みは、図3の30〜32行目の <tt class="docutils literal"><span class="pre">main'</span></tt>
で荷ほどきされています。
<tt class="docutils literal"><span class="pre">main'</span></tt> ではパターンマッチが行われており、
<tt class="docutils literal"><span class="pre">getNum</span></tt> が <tt class="docutils literal"><span class="pre">Left</span></tt> で値を返してきたか
<tt class="docutils literal"><span class="pre">Right</span></tt> で返してきたかで挙動を変えています。</p>
<p>　ここまで来て核心を言うと、
<tt class="docutils literal"><span class="pre">Either</span></tt> は、この例のように
異なる型を返したいときに使われます。
<tt class="docutils literal"><span class="pre">main</span></tt> では、 <tt class="docutils literal"><span class="pre">Left</span></tt> で文字列
（エラーメッセージ）が返ってきたら
<tt class="docutils literal"><span class="pre">die</span></tt> 関数を呼び、 <tt class="docutils literal"><span class="pre">Right</span></tt> で数字が返ってきたら
デバッグ用にその数字を表示しています。
<tt class="docutils literal"><span class="pre">die</span></tt> 関数は、14, 15行目で定義されており、
エラーメッセージを標準エラー出力に出して終了ステータス1
でこのプログラムを終わらせる関数です。
22, 23行目は <tt class="docutils literal"><span class="pre">main'</span></tt> と <tt class="docutils literal"><span class="pre">getNum</span></tt> を呼び出すために
前回の <tt class="docutils literal"><span class="pre">map.3.hs</span></tt> から
書き換えられているので、これもチェックしておいてください。</p>
<p>　次に <tt class="docutils literal"><span class="pre">Maybe</span></tt> です。35行目の <tt class="docutils literal"><span class="pre">readMaybe</span></tt>
は、これまで何回か使ってきた <tt class="docutils literal"><span class="pre">read</span></tt> 関数の変種です。
<tt class="docutils literal"><span class="pre">read</span></tt> は文字列が数字に変換できないとその場でプログラム
共々自爆するという悪い癖があるのですが、
<tt class="docutils literal"><span class="pre">readMaybe</span></tt> は、次のような型を返すことでそれを回避します。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Text</span><span class="o">.</span><span class="kt">Read</span><span class="o">.</span><span class="n">readMaybe</span>
<span class="kt">Text</span><span class="o">.</span><span class="kt">Read</span><span class="o">.</span><span class="n">readMaybe</span> <span class="ow">::</span> <span class="kt">Read</span> <span class="n">a</span> <span class="ow">=&gt;</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">Maybe</span> <span class="n">a</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">map.4.hs</span></tt> の使い方だと、 <tt class="docutils literal"><span class="pre">a</span></tt> には <tt class="docutils literal"><span class="pre">Int</span></tt>
が入ります。つまり <tt class="docutils literal"><span class="pre">readMaybe</span></tt> は、
<tt class="docutils literal"><span class="pre">Maybe</span> <span class="pre">Int</span></tt> （Intかもね〜〜〜。そうじゃないかもね〜〜）
というふざけた型のものを出力します。</p>
<p>　んで、 <tt class="docutils literal"><span class="pre">Maybe</span> <span class="pre">Int</span></tt> の入力をさばいているのが <tt class="docutils literal"><span class="pre">getNum'</span></tt>
関数です。パターンを見ると、 <tt class="docutils literal"><span class="pre">Just</span> <span class="pre">n</span></tt> と <tt class="docutils literal"><span class="pre">Nothing</span></tt>
というのがあります。このうち、 <tt class="docutils literal"><span class="pre">Just</span> <span class="pre">n</span></tt>
が、「数字が読めてその数字はnだ」という意味で、
<tt class="docutils literal"><span class="pre">Nothing</span></tt> が、「読み取りできなかった」という意味です。
これに合わせて、 <tt class="docutils literal"><span class="pre">getNum'</span></tt> はRightかLeftを返しています。
また、nが0以下の場合にもLeftを返すためにガードも使っています。</p>
<p>　実は <tt class="docutils literal"><span class="pre">Either</span></tt> も <tt class="docutils literal"><span class="pre">Maybe</span></tt> の「モナド」です。
「Haskell=モナド」、「モナドを制す者はHaskellを制す」
というような風潮もないことはないのですが、
あまり最初は考えずに使い方から入っていけばよいと思います。
私もよく分かってません。
何をもって分かったというのかも分かりませんので、
とりあえずは使えるようにしましょう <a class="footnote-reference" href="#id16" id="id6">[4]</a> 。</p>
<p>　ところで、 <tt class="docutils literal"><span class="pre">getNum</span></tt> では <tt class="docutils literal"><span class="pre">Left</span></tt> にエラーメッセージ、
<tt class="docutils literal"><span class="pre">Right</span></tt> に数字を指定しています。
英語では「Right=正しい」ですので、
逆にするといけないことになっているようです <a class="footnote-reference" href="#id17" id="id7">[5]</a> 。
また、 <tt class="docutils literal"><span class="pre">getNum</span></tt> のパターンマッチが随分無理やりですが、
<tt class="docutils literal"><span class="pre">'n':'u':'m':'='</span></tt> で文字列の頭が <tt class="docutils literal"><span class="pre">num=</span></tt>
のときのパターンを作っています。</p>
<p>　 <tt class="docutils literal"><span class="pre">map.4.hs</span></tt> の動作確認の様子を図5に示しておきます。</p>
<ul class="simple">
<li>図5: map.4.hsの動作確認</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>ghc map.4.hs
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span>100
100
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span>-1
Error<span class="o">[</span>map<span class="o">]</span> : invalid number <span class="k">for </span>num option
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span>
Error<span class="o">[</span>map<span class="o">]</span> : invalid number <span class="k">for </span>num option
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 aaa
Error<span class="o">[</span>map<span class="o">]</span> : no num option
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h2>11.4. データを型にはめる<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　やっと本題中の本題です。
<tt class="docutils literal"><span class="pre">main'</span></tt> 関数内に標準入力の処理を書いていきましょう。
図6は <tt class="docutils literal"><span class="pre">main'</span></tt> 関数と、その前後に付け足したコード、
そしてヘッダ部分の変更を示します。</p>
<ul class="simple">
<li>図6: map.5.hsの一部</li>
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
18
19
20
21
22</pre></div></td><td class="code"><div class="highlight"><pre>import Data.ByteString.Lazy.Char8 as BS hiding (take,drop,head)
（中略）

type Word = BS.ByteString
type Key = BS.ByteString
type SubKey = BS.ByteString
type Values = [Word]
type Line = (Key,SubKey,Values)
type Data = [Line]

main&#39; :: Either String Int -&gt; BS.ByteString -&gt; IO ()
main&#39; (Left str) cs = die str
main&#39; (Right num) cs = print d -- for debug
 where d = [ makeLine num ln | ln &lt;- BS.lines cs ]

makeLine :: Int -&gt; BS.ByteString -&gt; Line
makeLine num ln = (k,s,v)
 where k = BS.unwords $ take num $ BS.words ln
 s = head $ drop num $ BS.words ln
 v = drop (num + 1) $ BS.words ln

（略）
</pre></div>
</td></tr></table></div>
<p>まず1行目の、 <tt class="docutils literal"><span class="pre">hiding</span> <span class="pre">...</span></tt> の説明から。
これは <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> モジュールが
<tt class="docutils literal"><span class="pre">take,</span> <span class="pre">drop,</span> <span class="pre">head</span></tt> という関数を持っており、
これがデフォルトの <tt class="docutils literal"><span class="pre">take,</span> <span class="pre">drop,</span> <span class="pre">head</span></tt>
と名前が衝突してしまうので、
隠しておしまいなさい <a class="footnote-reference" href="#id19" id="id9">[7]</a> という意味です。
ちなみに「デフォルト」で定義されている関数というのは、
<tt class="docutils literal"><span class="pre">Prelude</span></tt> というモジュールにあります。
<tt class="docutils literal"><span class="pre">Prelude</span></tt> モジュールは、明示的に書かなくてもインポートされているので、
我々は <tt class="docutils literal"><span class="pre">map</span></tt> や <tt class="docutils literal"><span class="pre">head</span></tt> 等を使えることができるという
仕掛けになっています。</p>
<p>　次、4〜9行目ですが、
ここでは <tt class="docutils literal"><span class="pre">type</span></tt> という呪文（type宣言）を使い、
<tt class="docutils literal"><span class="pre">BS.ByteString</span></tt> 型に
<tt class="docutils literal"><span class="pre">Word</span></tt> やら <tt class="docutils literal"><span class="pre">Key</span></tt> やら自分で勝手に別名をつけ、
それらを組み合わせて型を作っています。
このように型を作っていく作業は、
Haskellというかプログラムでは重要な作業です。
例えば8行目では、 <tt class="docutils literal"><span class="pre">Line</span></tt> （一行）
が <tt class="docutils literal"><span class="pre">key</span></tt> （キー、縦軸）、 <tt class="docutils literal"><span class="pre">SubKey</span></tt> （サブキー、横軸）、
<tt class="docutils literal"><span class="pre">Values</span></tt> （複数の値）であると定義しています。
プログラムは、この型に合わせて各行を解析していくわけですが、
このように型を先にはっきりさせておくと、
入出力が何であるかを意識してプログラミングすることになります。</p>
<p>　 <tt class="docutils literal"><span class="pre">main'</span></tt> 関数は、13, 14行目が修正されています。
13行目にはデバッグ用の <tt class="docutils literal"><span class="pre">print</span></tt> が書いてあります。
14行目は読み込んだデータを行ごとに分解し、
8行目で宣言した <tt class="docutils literal"><span class="pre">Line</span></tt> 型に各行を加工しています。
ここで使っている <tt class="docutils literal"><span class="pre">makeLine</span></tt> は16〜20行目で定義されています。</p>
<p>　話を <tt class="docutils literal"><span class="pre">makeLine</span></tt> 関数に移しましょう。
この関数は、キーのフィールド数と一行を受け取り、
<tt class="docutils literal"><span class="pre">Line</span></tt> 型に行を加工して返します。
<tt class="docutils literal"><span class="pre">k,s,v</span></tt> がそれぞれ縦軸にするキー、
横軸にするキー、値です。
では、 <tt class="docutils literal"><span class="pre">map.5.hs</span></tt> を動かしてみましょう。
図7のようになりました。</p>
<ul class="simple">
<li>図7: map.5.hsの動作確認</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghc map.5.hs
<span class="nv">$ </span>cat ~/data | ./map.5 <span class="nv">num</span><span class="o">=</span>1
<span class="o">[(</span><span class="s2">&quot;a&quot;</span>,<span class="s2">&quot;\\227\\129\\130&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\132&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\134&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>11.5. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はmapコマンドの作成の途中までを行いました。
エラー処理、オプションの処理、
データを型に合わせて加工するコードを扱いました。
エラー処理ではモナドである
<tt class="docutils literal"><span class="pre">Either</span></tt> と <tt class="docutils literal"><span class="pre">Maybe</span></tt> が出てきました。
これらが使えると、「返す値の型は一つだけ」
というHaskellの厳しさが緩和されます。
また <tt class="docutils literal"><span class="pre">type</span></tt> で既存の型から型を定義することで、
行をどのように解釈するかを決めました。
というように今回は型絡みの話が多かったのですが、
結局のところ、「型を制すものはHaskellを制す」
ということなんでしょう。よくわからんけど。</p>
<p>　次回は、最低限の <tt class="docutils literal"><span class="pre">map</span></tt>
の機能は実装したいなと考えております。
んでは。</p>
</div>
<div class="section" id="haskell">
<h2>11.6. コラム: コマンドとHaskellの関数<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　え？また余白ですか。すんません。
では、フリーダムコラムを書かせていただきます。</p>
<p>　シェル芸は関数型というのは、全国1億2千万人のシェル芸人には周知の事実です。
ただ、シェル芸人兼Haskellerという人になると桁が7個くらい落ちるので、
根拠資料を出させていただきます。
コマンドとHaskellの関数の対応表です。表1に示します。</p>
<p>　この表では、ファイルの1行をHaskellのリストの一要素、
ファイルでスペース区切りの2次元テーブルとして作ったデータを
Haskellの二次元リスト（リストのリスト）とみなしています。</p>
<ul class="simple">
<li>表1: Haskellの関数とコマンドの対応表</li>
</ul>
<p>（201502.table.htmlをここに挿入。）</p>
<p>　どうです？一緒でしょ？え？一緒じゃない？
無理やり一緒だと思えば
Haskellが書けるようになるかもしれません。</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id11" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td><a class="footnote-reference" href="#id14" id="id12">[3]</a> を参照のこと。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id13" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>咲いても実を結ばずに散る花。転じて、実(じつ)を伴わない物事。
（「デジタル大辞泉」より）</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id12">[3]</a></td><td><a class="footnote-reference" href="#id18" id="id15">[6]</a> を参照のこと。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id16" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>要はHaskell好きがこういう議論を好むだけの話なので、
使うだけなら巻き込まれない方が利口です。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id17" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td>なんかしゃらくさい。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id18" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id15">[6]</a></td><td>こんにちわわ</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id19" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id9">[7]</a></td><td>水戸黄門風に読んでください。</td></tr>
</tbody>
</table>
</div>
</div>

