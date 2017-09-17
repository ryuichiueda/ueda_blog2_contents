# USP Magazine 2015年2月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>11. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p><br />
<blockquote><br />
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア<br />
状態なので，連載しながら開発しようと思い立った上田は，<br />
不幸にも黒塗りの高級車に追突してしまう．後輩をかばい<br />
すべての責任を負った上田に対し，車の主，暴力団員谷岡に<br />
言い渡された示談の条件とは...．</div></blockquote><br />
<div class="section" id="id1"><br />
<h2>11.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　 <a class="footnote-reference" href="#id11" id="id2">[1]</a> 。富山の徒花 <a class="footnote-reference" href="#id13" id="id3">[2]</a> 、<br />
ブラックエンジェル上田です。冬ですね。<br />
皆様は冬の楽しみと言えば何でしょうか？<br />
私はありません。全くありません。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>11.2. 本日やること<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　と、あっという間に冒頭の挨拶が終わりましたので、<br />
今月はたっぷりHaskellを書くことにしましょう。<br />
前回からやっている通り、今回もHaskell版のOpen usp Tukubai<br />
の開発を続けることとします。</p><br />
<p>　サンプルコードを含んだブランチは、</p><br />
<blockquote><br />
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote><br />
<p>にありますので，参考にしながらHaskellを勉強してみてください．</p><br />
<p>　前回はmapというコマンドを作っており、<br />
標準入出力からの字の出し入れ、<br />
終了ステータスの適切な出力を実装しました。<br />
今回はいよいよmapで行う処理の中身に入っていきます。</p><br />
<p>　今回実装する機能を見ましょう。<br />
図1のようなデータがあるとします。<br />
区切り文字はすべて半角スペースです。</p><br />
<ul class="simple"><br />
<li>図1: 入力データ</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data<br />
a あ 1<br />
b い 2<br />
b う 3<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このデータを、図2のように「第1フィールドを縦軸」、<br />
「第2フィールドを横軸」にして表にするのがmapです。</p><br />
<ul class="simple"><br />
<li>図2: 出力データ</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>1 data<br />
* あ い う<br />
a 1 0 0<br />
b 0 2 3<br />
<span class="c">###出力を揃えるときにはketaを使う###</span><br />
<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>1 data | keta<br />
* あ い う<br />
a 1 0 0<br />
b 0 2 3<br />
</pre></div><br />
</td></tr></table></div><br />
<p>オプションで指定している <tt class="docutils literal"><span class="pre">num=1</span></tt><br />
は、左から1列目までを縦軸扱いするということです。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>11.3. オプションの処理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　んで、最初に実装するのは <tt class="docutils literal"><span class="pre">num=&lt;数字&gt;</span></tt><br />
の数字の部分を読み込む処理です。<br />
ちょっと長いですが、この部分を実装した <tt class="docutils literal"><span class="pre">map.4.hs</span></tt><br />
を全部載っけておきます。</p><br />
<ul class="simple"><br />
<li>図3: numオプションから数字を読み込む処理を入れたmap.4.hs</li><br />
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
18<br />
19<br />
20<br />
21<br />
22<br />
23<br />
24<br />
25<br />
26<br />
27<br />
28<br />
29<br />
30<br />
31<br />
32<br />
33<br />
34<br />
35<br />
36<br />
37<br />
38<br />
39<br />
40<br />
41<br />
42</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span><br />
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span><br />
<span class="kr">import</span> <span class="nn">System.IO</span><br />
<span class="kr">import</span> <span class="nn">System.Exit</span><br />
<span class="kr">import</span> <span class="nn">Text.Read</span><br />
<br />
<span class="nf">showUsage</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">showUsage</span> <span class="ow">=</span> <span class="kr">do</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span><br />
 <span class="s">&quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; </span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span><br />
 <span class="s">&quot;Thu Oct 23 08:52:44 JST 2014</span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span><br />
 <span class="s">&quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span><br />
 <span class="n">exitWith</span> <span class="p">(</span><span class="kt">ExitFailure</span> <span class="mi">1</span><span class="p">)</span><br />
<br />
<span class="nf">die</span> <span class="n">str</span> <span class="ow">=</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span><br />
 <span class="s">&quot;Error[map] : &quot;</span> <span class="o">++</span> <span class="n">str</span> <span class="o">++</span> <span class="s">&quot;</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="n">exitWith</span> <span class="p">(</span><span class="kt">ExitFailure</span> <span class="mi">1</span><span class="p">)</span><br />
<br />
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span><br />
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span><br />
 <span class="p">[</span><span class="s">&quot;-h&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
 <span class="p">[</span><span class="s">&quot;--help&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">main&#39;</span> <span class="p">(</span><span class="n">getNum</span> <span class="n">num</span><span class="p">)</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="n">main&#39;</span> <span class="p">(</span><span class="n">getNum</span> <span class="n">num</span><span class="p">)</span><br />
 <span class="kr">_</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
<br />
<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span><br />
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span><br />
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span><br />
<br />
<span class="nf">main&#39;</span> <span class="ow">::</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span> <span class="ow">-&gt;</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main&#39;</span> <span class="p">(</span><span class="kt">Left</span> <span class="n">str</span><span class="p">)</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">die</span> <span class="n">str</span><br />
<span class="nf">main&#39;</span> <span class="p">(</span><span class="kt">Right</span> <span class="n">num</span><span class="p">)</span> <span class="n">cs</span> <span class="ow">=</span> <span class="n">print</span> <span class="n">num</span> <span class="c1">-- for debug</span><br />
<br />
<span class="nf">getNum</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span><br />
<span class="nf">getNum</span> <span class="p">(</span><span class="n">&#39;n&#39;</span><span class="kt">:</span><span class="n">&#39;u&#39;</span><span class="kt">:</span><span class="n">&#39;m&#39;</span><span class="kt">:</span><span class="sc">&#39;=&#39;</span><span class="kt">:</span><span class="n">str</span><span class="p">)</span> <span class="ow">=</span> <span class="n">getNum&#39;</span> <span class="p">(</span><span class="n">readMaybe</span> <span class="n">str</span><span class="p">)</span><br />
<span class="nf">getNum</span> <span class="kr">_</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;no num option&quot;</span><br />
<br />
<span class="nf">getNum&#39;</span> <span class="ow">::</span> <span class="kt">Maybe</span> <span class="kt">Int</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="kt">String</span> <span class="kt">Int</span><br />
<span class="nf">getNum&#39;</span> <span class="kt">Nothing</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;invalid number for num option&quot;</span><br />
<span class="nf">getNum&#39;</span> <span class="p">(</span><span class="kt">Just</span> <span class="n">n</span><span class="p">)</span><br />
 <span class="o">|</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">=</span> <span class="kt">Right</span> <span class="n">n</span><br />
 <span class="o">|</span> <span class="n">otherwise</span> <span class="ow">=</span> <span class="kt">Left</span> <span class="s">&quot;invalid number for num option&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　・・・大変です。普通の言語なら関数を<br />
一個作ってちょろっと試せばよいのですが、<br />
Haskellの場合は型と関数の接続先を<br />
考えてからでないと関数を書けないので大変です。<br />
ただ、この方がトップダウンな思考は身につくと思います。</p><br />
<p>　さて、このコードで重要なのは何と言っても<br />
<tt class="docutils literal"><span class="pre">getNum</span></tt> 関数です。この関数は、オプションを読み込んで、<br />
<tt class="docutils literal"><span class="pre">num=</span></tt> の後ろの数字をInt型で返すのが第一の目的です。<br />
ただ、話はそんなに簡単ではありません。<br />
変な数字が入っていたらそれを通知しなければなりません。<br />
このとき、例えば数字でなくて <tt class="docutils literal"><span class="pre">num=aaa</span></tt> とか書いてあったら<br />
-1を返すなど、Int型で済ませる方法もありますが、<br />
ここではもう少しこだわって <tt class="docutils literal"><span class="pre">Either</span></tt> と <tt class="docutils literal"><span class="pre">Maybe</span></tt><br />
というものを使っています。</p><br />
<p>　まず、35〜42行目に出てくる <tt class="docutils literal"><span class="pre">Left</span></tt> と <tt class="docutils literal"><span class="pre">Right</span></tt> から、<br />
<tt class="docutils literal"><span class="pre">Either</span></tt> を理解してみましょう。<br />
図4を見ながら説明すると分かりやすいと思いますが、<br />
<tt class="docutils literal"><span class="pre">Left</span></tt> は引数にとったものを <tt class="docutils literal"><span class="pre">Either</span> <span class="pre">a</span> <span class="pre">b</span></tt><br />
の左側の <tt class="docutils literal"><span class="pre">a</span></tt> に、 <tt class="docutils literal"><span class="pre">Right</span></tt> は右側の <tt class="docutils literal"><span class="pre">b</span></tt><br />
に包んで返します。</p><br />
<ul class="simple"><br />
<li>図4: LeftとRightの型</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Left</span><br />
<span class="kt">Left</span> <span class="ow">::</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="n">a</span> <span class="n">b</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Right</span><br />
<span class="kt">Right</span> <span class="ow">::</span> <span class="n">b</span> <span class="ow">-&gt;</span> <span class="kt">Either</span> <span class="n">a</span> <span class="n">b</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この包みは、図3の30〜32行目の <tt class="docutils literal"><span class="pre">main'</span></tt><br />
で荷ほどきされています。<br />
<tt class="docutils literal"><span class="pre">main'</span></tt> ではパターンマッチが行われており、<br />
<tt class="docutils literal"><span class="pre">getNum</span></tt> が <tt class="docutils literal"><span class="pre">Left</span></tt> で値を返してきたか<br />
<tt class="docutils literal"><span class="pre">Right</span></tt> で返してきたかで挙動を変えています。</p><br />
<p>　ここまで来て核心を言うと、<br />
<tt class="docutils literal"><span class="pre">Either</span></tt> は、この例のように<br />
異なる型を返したいときに使われます。<br />
<tt class="docutils literal"><span class="pre">main</span></tt> では、 <tt class="docutils literal"><span class="pre">Left</span></tt> で文字列<br />
（エラーメッセージ）が返ってきたら<br />
<tt class="docutils literal"><span class="pre">die</span></tt> 関数を呼び、 <tt class="docutils literal"><span class="pre">Right</span></tt> で数字が返ってきたら<br />
デバッグ用にその数字を表示しています。<br />
<tt class="docutils literal"><span class="pre">die</span></tt> 関数は、14, 15行目で定義されており、<br />
エラーメッセージを標準エラー出力に出して終了ステータス1<br />
でこのプログラムを終わらせる関数です。<br />
22, 23行目は <tt class="docutils literal"><span class="pre">main'</span></tt> と <tt class="docutils literal"><span class="pre">getNum</span></tt> を呼び出すために<br />
前回の <tt class="docutils literal"><span class="pre">map.3.hs</span></tt> から<br />
書き換えられているので、これもチェックしておいてください。</p><br />
<p>　次に <tt class="docutils literal"><span class="pre">Maybe</span></tt> です。35行目の <tt class="docutils literal"><span class="pre">readMaybe</span></tt><br />
は、これまで何回か使ってきた <tt class="docutils literal"><span class="pre">read</span></tt> 関数の変種です。<br />
<tt class="docutils literal"><span class="pre">read</span></tt> は文字列が数字に変換できないとその場でプログラム<br />
共々自爆するという悪い癖があるのですが、<br />
<tt class="docutils literal"><span class="pre">readMaybe</span></tt> は、次のような型を返すことでそれを回避します。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">Text</span><span class="o">.</span><span class="kt">Read</span><span class="o">.</span><span class="n">readMaybe</span><br />
<span class="kt">Text</span><span class="o">.</span><span class="kt">Read</span><span class="o">.</span><span class="n">readMaybe</span> <span class="ow">::</span> <span class="kt">Read</span> <span class="n">a</span> <span class="ow">=&gt;</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">Maybe</span> <span class="n">a</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">map.4.hs</span></tt> の使い方だと、 <tt class="docutils literal"><span class="pre">a</span></tt> には <tt class="docutils literal"><span class="pre">Int</span></tt><br />
が入ります。つまり <tt class="docutils literal"><span class="pre">readMaybe</span></tt> は、<br />
<tt class="docutils literal"><span class="pre">Maybe</span> <span class="pre">Int</span></tt> （Intかもね〜〜〜。そうじゃないかもね〜〜）<br />
というふざけた型のものを出力します。</p><br />
<p>　んで、 <tt class="docutils literal"><span class="pre">Maybe</span> <span class="pre">Int</span></tt> の入力をさばいているのが <tt class="docutils literal"><span class="pre">getNum'</span></tt><br />
関数です。パターンを見ると、 <tt class="docutils literal"><span class="pre">Just</span> <span class="pre">n</span></tt> と <tt class="docutils literal"><span class="pre">Nothing</span></tt><br />
というのがあります。このうち、 <tt class="docutils literal"><span class="pre">Just</span> <span class="pre">n</span></tt><br />
が、「数字が読めてその数字はnだ」という意味で、<br />
<tt class="docutils literal"><span class="pre">Nothing</span></tt> が、「読み取りできなかった」という意味です。<br />
これに合わせて、 <tt class="docutils literal"><span class="pre">getNum'</span></tt> はRightかLeftを返しています。<br />
また、nが0以下の場合にもLeftを返すためにガードも使っています。</p><br />
<p>　実は <tt class="docutils literal"><span class="pre">Either</span></tt> も <tt class="docutils literal"><span class="pre">Maybe</span></tt> の「モナド」です。<br />
「Haskell=モナド」、「モナドを制す者はHaskellを制す」<br />
というような風潮もないことはないのですが、<br />
あまり最初は考えずに使い方から入っていけばよいと思います。<br />
私もよく分かってません。<br />
何をもって分かったというのかも分かりませんので、<br />
とりあえずは使えるようにしましょう <a class="footnote-reference" href="#id16" id="id6">[4]</a> 。</p><br />
<p>　ところで、 <tt class="docutils literal"><span class="pre">getNum</span></tt> では <tt class="docutils literal"><span class="pre">Left</span></tt> にエラーメッセージ、<br />
<tt class="docutils literal"><span class="pre">Right</span></tt> に数字を指定しています。<br />
英語では「Right=正しい」ですので、<br />
逆にするといけないことになっているようです <a class="footnote-reference" href="#id17" id="id7">[5]</a> 。<br />
また、 <tt class="docutils literal"><span class="pre">getNum</span></tt> のパターンマッチが随分無理やりですが、<br />
<tt class="docutils literal"><span class="pre">'n':'u':'m':'='</span></tt> で文字列の頭が <tt class="docutils literal"><span class="pre">num=</span></tt><br />
のときのパターンを作っています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">map.4.hs</span></tt> の動作確認の様子を図5に示しておきます。</p><br />
<ul class="simple"><br />
<li>図5: map.4.hsの動作確認</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>ghc map.4.hs<br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span>100<br />
100<br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span>-1<br />
Error<span class="o">[</span>map<span class="o">]</span> : invalid number <span class="k">for </span>num option<br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 <span class="nv">num</span><span class="o">=</span><br />
Error<span class="o">[</span>map<span class="o">]</span> : invalid number <span class="k">for </span>num option<br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.4 aaa<br />
Error<span class="o">[</span>map<span class="o">]</span> : no num option<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>11.4. データを型にはめる<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　やっと本題中の本題です。<br />
<tt class="docutils literal"><span class="pre">main'</span></tt> 関数内に標準入力の処理を書いていきましょう。<br />
図6は <tt class="docutils literal"><span class="pre">main'</span></tt> 関数と、その前後に付け足したコード、<br />
そしてヘッダ部分の変更を示します。</p><br />
<ul class="simple"><br />
<li>図6: map.5.hsの一部</li><br />
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
18<br />
19<br />
20<br />
21<br />
22</pre></div></td><td class="code"><div class="highlight"><pre>import Data.ByteString.Lazy.Char8 as BS hiding (take,drop,head)<br />
（中略）<br />
<br />
type Word = BS.ByteString<br />
type Key = BS.ByteString<br />
type SubKey = BS.ByteString<br />
type Values = [Word]<br />
type Line = (Key,SubKey,Values)<br />
type Data = [Line]<br />
<br />
main&#39; :: Either String Int -&gt; BS.ByteString -&gt; IO ()<br />
main&#39; (Left str) cs = die str<br />
main&#39; (Right num) cs = print d -- for debug<br />
 where d = [ makeLine num ln | ln &lt;- BS.lines cs ]<br />
<br />
makeLine :: Int -&gt; BS.ByteString -&gt; Line<br />
makeLine num ln = (k,s,v)<br />
 where k = BS.unwords $ take num $ BS.words ln<br />
 s = head $ drop num $ BS.words ln<br />
 v = drop (num + 1) $ BS.words ln<br />
<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>まず1行目の、 <tt class="docutils literal"><span class="pre">hiding</span> <span class="pre">...</span></tt> の説明から。<br />
これは <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> モジュールが<br />
<tt class="docutils literal"><span class="pre">take,</span> <span class="pre">drop,</span> <span class="pre">head</span></tt> という関数を持っており、<br />
これがデフォルトの <tt class="docutils literal"><span class="pre">take,</span> <span class="pre">drop,</span> <span class="pre">head</span></tt><br />
と名前が衝突してしまうので、<br />
隠しておしまいなさい <a class="footnote-reference" href="#id19" id="id9">[7]</a> という意味です。<br />
ちなみに「デフォルト」で定義されている関数というのは、<br />
<tt class="docutils literal"><span class="pre">Prelude</span></tt> というモジュールにあります。<br />
<tt class="docutils literal"><span class="pre">Prelude</span></tt> モジュールは、明示的に書かなくてもインポートされているので、<br />
我々は <tt class="docutils literal"><span class="pre">map</span></tt> や <tt class="docutils literal"><span class="pre">head</span></tt> 等を使えることができるという<br />
仕掛けになっています。</p><br />
<p>　次、4〜9行目ですが、<br />
ここでは <tt class="docutils literal"><span class="pre">type</span></tt> という呪文（type宣言）を使い、<br />
<tt class="docutils literal"><span class="pre">BS.ByteString</span></tt> 型に<br />
<tt class="docutils literal"><span class="pre">Word</span></tt> やら <tt class="docutils literal"><span class="pre">Key</span></tt> やら自分で勝手に別名をつけ、<br />
それらを組み合わせて型を作っています。<br />
このように型を作っていく作業は、<br />
Haskellというかプログラムでは重要な作業です。<br />
例えば8行目では、 <tt class="docutils literal"><span class="pre">Line</span></tt> （一行）<br />
が <tt class="docutils literal"><span class="pre">key</span></tt> （キー、縦軸）、 <tt class="docutils literal"><span class="pre">SubKey</span></tt> （サブキー、横軸）、<br />
<tt class="docutils literal"><span class="pre">Values</span></tt> （複数の値）であると定義しています。<br />
プログラムは、この型に合わせて各行を解析していくわけですが、<br />
このように型を先にはっきりさせておくと、<br />
入出力が何であるかを意識してプログラミングすることになります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">main'</span></tt> 関数は、13, 14行目が修正されています。<br />
13行目にはデバッグ用の <tt class="docutils literal"><span class="pre">print</span></tt> が書いてあります。<br />
14行目は読み込んだデータを行ごとに分解し、<br />
8行目で宣言した <tt class="docutils literal"><span class="pre">Line</span></tt> 型に各行を加工しています。<br />
ここで使っている <tt class="docutils literal"><span class="pre">makeLine</span></tt> は16〜20行目で定義されています。</p><br />
<p>　話を <tt class="docutils literal"><span class="pre">makeLine</span></tt> 関数に移しましょう。<br />
この関数は、キーのフィールド数と一行を受け取り、<br />
<tt class="docutils literal"><span class="pre">Line</span></tt> 型に行を加工して返します。<br />
<tt class="docutils literal"><span class="pre">k,s,v</span></tt> がそれぞれ縦軸にするキー、<br />
横軸にするキー、値です。<br />
では、 <tt class="docutils literal"><span class="pre">map.5.hs</span></tt> を動かしてみましょう。<br />
図7のようになりました。</p><br />
<ul class="simple"><br />
<li>図7: map.5.hsの動作確認</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghc map.5.hs<br />
<span class="nv">$ </span>cat ~/data | ./map.5 <span class="nv">num</span><span class="o">=</span>1<br />
<span class="o">[(</span><span class="s2">&quot;a&quot;</span>,<span class="s2">&quot;\\227\\129\\130&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\132&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\134&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>11.5. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はmapコマンドの作成の途中までを行いました。<br />
エラー処理、オプションの処理、<br />
データを型に合わせて加工するコードを扱いました。<br />
エラー処理ではモナドである<br />
<tt class="docutils literal"><span class="pre">Either</span></tt> と <tt class="docutils literal"><span class="pre">Maybe</span></tt> が出てきました。<br />
これらが使えると、「返す値の型は一つだけ」<br />
というHaskellの厳しさが緩和されます。<br />
また <tt class="docutils literal"><span class="pre">type</span></tt> で既存の型から型を定義することで、<br />
行をどのように解釈するかを決めました。<br />
というように今回は型絡みの話が多かったのですが、<br />
結局のところ、「型を制すものはHaskellを制す」<br />
ということなんでしょう。よくわからんけど。</p><br />
<p>　次回は、最低限の <tt class="docutils literal"><span class="pre">map</span></tt><br />
の機能は実装したいなと考えております。<br />
んでは。</p><br />
</div><br />
<div class="section" id="haskell"><br />
<h2>11.6. コラム: コマンドとHaskellの関数<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　え？また余白ですか。すんません。<br />
では、フリーダムコラムを書かせていただきます。</p><br />
<p>　シェル芸は関数型というのは、全国1億2千万人のシェル芸人には周知の事実です。<br />
ただ、シェル芸人兼Haskellerという人になると桁が7個くらい落ちるので、<br />
根拠資料を出させていただきます。<br />
コマンドとHaskellの関数の対応表です。表1に示します。</p><br />
<p>　この表では、ファイルの1行をHaskellのリストの一要素、<br />
ファイルでスペース区切りの2次元テーブルとして作ったデータを<br />
Haskellの二次元リスト（リストのリスト）とみなしています。</p><br />
<ul class="simple"><br />
<li>表1: Haskellの関数とコマンドの対応表</li><br />
</ul><br />
<p>（201502.table.htmlをここに挿入。）</p><br />
<p>　どうです？一緒でしょ？え？一緒じゃない？<br />
無理やり一緒だと思えば<br />
Haskellが書けるようになるかもしれません。</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id11" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td><a class="footnote-reference" href="#id14" id="id12">[3]</a> を参照のこと。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id13" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>咲いても実を結ばずに散る花。転じて、実(じつ)を伴わない物事。<br />
（「デジタル大辞泉」より）</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id14" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id12">[3]</a></td><td><a class="footnote-reference" href="#id18" id="id15">[6]</a> を参照のこと。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id16" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>要はHaskell好きがこういう議論を好むだけの話なので、<br />
使うだけなら巻き込まれない方が利口です。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id17" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td>なんかしゃらくさい。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id18" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id15">[6]</a></td><td>こんにちわわ</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id19" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id9">[7]</a></td><td>水戸黄門風に読んでください。</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

