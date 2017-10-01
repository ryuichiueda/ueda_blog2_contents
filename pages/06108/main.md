---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年12月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>9. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>USP友の会のシェル芸勉強会
（脚注：シェルのワンライナー勉強会）は、
日々、他の言語からの他流試合に晒されているのである。
そこで上田は、Haskellで自ら他流試合を行い、
さらにシェル芸勉強会をいじめる自傷行為に手を
染めるのであった。</div></blockquote>
<div class="section" id="id1">
<h2>9.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　こ <a class="footnote-reference" href="#aa1" id="id2">[1]</a> 。富山の産んだブラックエンジェル上田です。
最近、次女が重たくなってきて、背負いながら物を書いていると
けっこうしんどくなって参りました。
俺はコオイムシ <a class="footnote-reference" href="#ee1" id="id3">[2]</a> かと、そういう気分になります。
「魚類、モノアラガイ、他の昆虫等を先端に二対の爪がある
鎌状の前肢で積極的に捕らえ、口針から消化液を送り込み
溶けた肉質を吸入する体外消化を行う。」
ことも、
「オスは卵塊保護中は動きを制約されるが、
通常と変わらない程度に給餌もし、
時には他のオスが卵を背負ってる時に、
その卵を襲って捕食してしまう事もある。」
ことも、コオイムシと私に共通した特徴です <a class="footnote-reference" href="#ff1" id="id4">[3]</a> 。
漢字で書くと「好意無視」となるのも、
なかなか素敵であり、ただならぬシンパシーを感じます。</p>
</div>
<div class="section" id="id5">
<h2>9.2. 前回のおさらい<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、なんか精神状態を問われそうなスタートになりましたが
<a class="footnote-reference" href="#gg1" id="id6">[4]</a> 、
本題に入りましょう。
現在解いているのは第1回勉強会の4問目です。
こんな問題でした。</p>
<blockquote>
<div>次のような <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを作り、
<tt class="docutils literal"><span class="pre">ans</span></tt> のように集計してください。</div></blockquote>
<p>　 <tt class="docutils literal"><span class="pre">ages</span></tt> と <tt class="docutils literal"><span class="pre">ans</span></tt> は図1のようなファイルです。
GitHubにアップしてあります <a class="footnote-reference" href="#hh1" id="id7">[5]</a> 。
<tt class="docutils literal"><span class="pre">ages</span></tt> はでかいのでブラウザで見ると
メモリ圧迫人生圧迫圧迫面接なのでご注意を。</p>
<ul class="simple">
<li>リスト1: インプットする <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルと解答ファイル <tt class="docutils literal"><span class="pre">ans</span></tt></li>
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
20</pre></div></td><td class="code"><div class="highlight"><pre>###agesは0〜109（年齢）をランダムに書いたもの###
ueda@remote:~/Study1_Q4/data$ head -n 5 ages
91
35
11
100
94
###ansはagesの度数分布表###
ueda@remote:~/Study1_Q4/data$ cat ans
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
<p>　前回はリスト2の <tt class="docutils literal"><span class="pre">q1_4_2.hs</span></tt> までを作りました。
出力と共に示します。
もう既に「何十代なのか」のリストができているので、
これらを集計するだけです。</p>
<ul class="simple">
<li>リスト2: 前回作成したコードq1_4_2.hsと実行結果</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_4_2</span><span class="o">.</span><span class="n">hs</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">cs</span> <span class="ow">&lt;-</span> <span class="n">getContents</span>
 <span class="n">print</span> <span class="p">[</span> <span class="mi">10</span> <span class="o">*</span> <span class="p">(</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span> <span class="ow">::</span> <span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span> <span class="p">)</span> <span class="o">|</span> <span class="n">c</span> <span class="ow">&lt;-</span> <span class="n">lines</span> <span class="n">cs</span> <span class="p">]</span>
<span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">ghc</span> <span class="n">q1_4_2</span><span class="o">.</span><span class="n">hs</span>
<span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="kr">data</span><span class="o">/</span><span class="n">ages</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_4_2</span> <span class="o">|</span> <span class="n">head</span> <span class="o">-</span><span class="n">c</span> <span class="mi">20</span>
<span class="p">[</span><span class="mi">90</span><span class="p">,</span><span class="mi">30</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">100</span><span class="p">,</span><span class="mi">90</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">7</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h2>9.3. ソートする<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて続きですが、6月号でも出てきた <tt class="docutils literal"><span class="pre">sort</span></tt>
関数を使ってリストをソートします。
リスト3にソートまで記述したコードを示します。
リスト2では各年齢の1の位を切り捨てた後、10をかけていますが、
これは不要なので処理を消しました。
また、sort関数を使うには <tt class="docutils literal"><span class="pre">Data.List</span></tt> というモジュールを
インポートしますが、これも6月号で説明しました。</p>
<ul class="simple">
<li>リスト3: リストをソートする処理を加えたq1_4_3.hsとその実行結果</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/Study1_Q4$ cat q1_4_3.hs
import Data.List

main = do cs &lt;- getContents
 print $ sort [ (read c :: Int) `div` 10 | c &lt;- lines cs ]
ueda@remote:~/Study1_Q4$ ghc q1_4_3.hs
###とりあえずdat/agesの先頭の10行を渡してみる###
ueda@remote:~/Study1_Q4$ head data/ages | ./q1_4_3
[0,1,3,7,9,9,9,10,10,10]
</pre></div>
</td></tr></table></div>
<p>　リストの要素の個数をカウントするにはソートしない方法もあります。
またソートするのは無駄なようにも思えます。
しかし、ソートしない方法は
データや要素の種類の多寡で有利不利が出てしまうので、
あまり凝らずにソートに頼ることにしました。
ここら辺の判断については意見の分かれるところですが、
私は「いつ・誰が困るかどうか」で判断しています。</p>
<p>　なんかかっこいい人が「こうでなければならない！」
とか本に書いていてそれを鵜呑みにするのはやめましょう。
世の中に、無条件にこうでなければならないというものは、
ありません。</p>
</div>
<div class="section" id="id9">
<h2>9.4. カウント処理<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、リストの集計を行います。
<tt class="docutils literal"><span class="pre">count</span></tt> という関数をリスト4のように実装して、
<tt class="docutils literal"><span class="pre">main</span></tt> 関数の処理に挟み込みます。
<tt class="docutils literal"><span class="pre">count</span></tt> の出力は「n十代がm人いる」ことを示すリストです。
10行目の <tt class="docutils literal"><span class="pre">where</span></tt> で定義している <tt class="docutils literal"><span class="pre">h</span></tt>
は、リストの先頭の要素で、
その下の <tt class="docutils literal"><span class="pre">len</span></tt> が、 <tt class="docutils literal"><span class="pre">h</span></tt> が何個続いているか、
最後の <tt class="docutils literal"><span class="pre">d</span></tt> が、リストの先頭から <tt class="docutils literal"><span class="pre">h</span></tt>
の並びを切り落としたリストです。
<tt class="docutils literal"><span class="pre">d</span></tt> は、9行目で再び <tt class="docutils literal"><span class="pre">count</span></tt> に入力されます。</p>
<p>　 <tt class="docutils literal"><span class="pre">count</span></tt> 関数が二つ定義されているのは、
7月号で出てきた「パターンマッチ」ですね。
8行目の定義は、引数が <tt class="docutils literal"><span class="pre">[]</span></tt> 、つまり空の場合にマッチし、
この場合はそのまま空のリストを返します。
9行目以降の定義は、8行目以外の場合、
についてマッチします。</p>
<p>　Haskellは、普通の言語ではif文を使うような場合でも、
このような仕組みが充実しているのでif文を避けることができます。
これが見やすい・書きやすいかどうかは、
読み手・書き手次第ですが・・・。
ここら辺、読み手書き手にどれくらいのレベルや
慣れを要求するとちょうどいいのかという問題は、
おそらく答えが出ない話です。</p>
<ul class="simple">
<li>リスト4: count関数を実装したq1_4_4.hs</li>
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
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/Study1_Q4$ cat q1_4_4.hs
import Data.List

main = do cs &lt;- getContents
 print $ count $ sort [ (read c :: Int) `div` 10 | c &lt;- lines cs ]

count :: [Int] -&gt; [(Int,Int)]
count [] = []
count ns = (h,len) : count d
 where h = head ns
 len = length $ takeWhile (== h) ns
 d = dropWhile (== h) ns
###出力###
ueda@remote:~/Study1_Q4$ ghc q1_4_4.hs
ueda@remote:~/Study1_Q4$ head data/ages | ./q1_4_4
[(0,1),(1,1),(3,1),(7,1),(9,3),(10,3)]
</pre></div>
</td></tr></table></div>
<p>　11行目の <tt class="docutils literal"><span class="pre">takeWhile</span></tt> 関数については5月号でも出てきました。
12行目の <tt class="docutils literal"><span class="pre">dropWhile</span></tt> 関数と共に、
リスト5で挙動を見ておきましょう。</p>
<ul class="simple">
<li>リスト5: takeWhile、dropWhileの挙動</li>
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
11</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/Study1_Q4$ ghci
Prelude&gt; let ns = [0,0,1,2]
###takeWhileは関数にマッチするまでの要素を取り出す###
Prelude&gt; takeWhile (== 0) ns
[0,0]
###dropWhileは関数にマッチするまで要素を切り落とす###
Prelude&gt; dropWhile (== 0) ns
[1,2]
###型は次の通り。Boolを返す関数とリストを引数にとる。###
Prelude&gt; :t takeWhile
takeWhile :: (a -&gt; Bool) -&gt; [a] -&gt; [a]
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>9.5. 整形して完成<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　最後に、 <tt class="docutils literal"><span class="pre">count</span></tt> の返すリストを整形してこの問題を終わらせましょう。
リスト6のように、
<tt class="docutils literal"><span class="pre">print</span></tt> の代わりに <tt class="docutils literal"><span class="pre">out</span></tt> という関数を定義して使います。
この <tt class="docutils literal"><span class="pre">out</span></tt> では、リストの中の <tt class="docutils literal"><span class="pre">(n,m)</span></tt>
（n十代がm個）というデータを、一つずつ17、18行目で整形して出力しています。
16行目の左辺の <tt class="docutils literal"><span class="pre">((g,num):es)</span></tt> は、
<tt class="docutils literal"><span class="pre">(g,num)</span></tt> がリストの先頭、 <tt class="docutils literal"><span class="pre">es</span></tt> がそれ以外で、
リストの先頭の <tt class="docutils literal"><span class="pre">(g,num)</span></tt> が17行目の <tt class="docutils literal"><span class="pre">oneline</span></tt>
を作るために使われ、
<tt class="docutils literal"><span class="pre">es</span></tt> が再起的に <tt class="docutils literal"><span class="pre">out</span></tt> に渡されています。
んで、 <tt class="docutils literal"><span class="pre">oneline</span></tt> と <tt class="docutils literal"><span class="pre">out</span></tt> の間に <tt class="docutils literal"><span class="pre">&gt;&gt;</span></tt>
という謎の記号がありますが、これの型を、
これまでも何回か出て来た <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt>
の型とともにリスト7に示します。</p>
<ul class="simple">
<li>リスト6: 出力を整形するq1_4_5.hs（完成）</li>
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_4_5</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">Data.List</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">cs</span> <span class="ow">&lt;-</span> <span class="n">getContents</span>
 <span class="n">out</span> <span class="o">$</span> <span class="n">count</span> <span class="o">$</span> <span class="n">sort</span> <span class="p">[</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span> <span class="ow">::</span> <span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span> <span class="o">|</span> <span class="n">c</span> <span class="ow">&lt;-</span> <span class="n">lines</span> <span class="n">cs</span> <span class="p">]</span>

<span class="nf">count</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">Int</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">Int</span><span class="p">)]</span>
<span class="nf">count</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="kt">[]</span>
<span class="nf">count</span> <span class="n">ns</span> <span class="ow">=</span> <span class="p">(</span><span class="n">h</span><span class="p">,</span><span class="n">len</span><span class="p">)</span> <span class="kt">:</span> <span class="n">count</span> <span class="n">d</span>
 <span class="kr">where</span> <span class="n">h</span> <span class="ow">=</span> <span class="n">head</span> <span class="n">ns</span>
 <span class="n">len</span> <span class="ow">=</span> <span class="n">length</span> <span class="o">$</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">h</span><span class="p">)</span> <span class="n">ns</span>
 <span class="n">d</span> <span class="ow">=</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">h</span><span class="p">)</span> <span class="n">ns</span>

<span class="nf">out</span> <span class="ow">::</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">Int</span><span class="p">)]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">out</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="n">return</span> <span class="nb">()</span>
<span class="nf">out</span> <span class="p">((</span><span class="n">g</span><span class="p">,</span><span class="n">num</span><span class="p">)</span><span class="kt">:</span><span class="n">es</span><span class="p">)</span> <span class="ow">=</span> <span class="n">putStrLn</span> <span class="n">oneline</span> <span class="o">&gt;&gt;</span> <span class="n">out</span> <span class="n">es</span>
 <span class="kr">where</span> <span class="n">oneline</span> <span class="ow">=</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="n">g</span><span class="o">*</span><span class="mi">10</span><span class="p">))</span> <span class="o">++</span> <span class="s">&quot;〜&quot;</span> <span class="o">++</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="n">g</span><span class="o">*</span><span class="mi">10</span><span class="o">+</span><span class="mi">9</span><span class="p">))</span>
 <span class="o">++</span> <span class="s">&quot; &quot;</span> <span class="o">++</span> <span class="p">(</span><span class="n">show</span> <span class="n">num</span><span class="p">)</span>
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>リスト7: &gt;&gt;と&gt;&gt;=の違い</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">uedambp</span><span class="kt">:~</span> <span class="n">ueda</span><span class="o">$</span> <span class="n">ghci</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;</span><span class="p">)</span>
<span class="p">(</span><span class="o">&gt;&gt;</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span>
<span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span>
</pre></div>
</td></tr></table></div>
<p>これだけ見てもピンと来ないかもしれませんが、
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> は <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt>
の左側の出力を右側に渡しますが、
<tt class="docutils literal"><span class="pre">&gt;&gt;</span></tt> は渡しません。型を見たら分かるのですが、
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> の <tt class="docutils literal"><span class="pre">a</span></tt> が出力に残ってません。
ですので、 <tt class="docutils literal"><span class="pre">putStrLn</span></tt> のように、
関数としては何も出力しない
<a class="footnote-reference" href="#cc1" id="id11">[6]</a>
ものが左側にあるときに使います。
おそらく、ghciでリスト8のような例を示しておけばなんとなく分かるかと。</p>
<ul class="simple">
<li>リスト8: &gt;&gt;の使用例</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">print</span> <span class="s">&quot;a&quot;</span> <span class="o">&gt;&gt;</span> <span class="n">print</span> <span class="s">&quot;b&quot;</span> <span class="o">&gt;&gt;</span> <span class="n">print</span> <span class="s">&quot;c&quot;</span>
<span class="s">&quot;a&quot;</span>
<span class="s">&quot;b&quot;</span>
<span class="s">&quot;c&quot;</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の使い方も触れておくために、
<tt class="docutils literal"><span class="pre">q1_4_5.hs</span></tt> の <tt class="docutils literal"><span class="pre">main</span></tt> 関数を
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を使って書き直したのでリスト9
に示します。
ほとんどシェル芸です・・・。
唯一違うのは右から左に読まなければならんことですが
<a class="footnote-reference" href="#jj1" id="id12">[7]</a> 。</p>
<ul class="simple">
<li>リスト9: &gt;&gt;=を使ってmain関数を書き直したもの</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">out</span> <span class="o">.</span> <span class="n">count</span> <span class="o">.</span> <span class="n">sort</span> <span class="o">.</span>
 <span class="n">map</span> <span class="p">(</span><span class="nf">\\</span><span class="n">c</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span><span class="ow">::</span><span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span><span class="p">)</span> <span class="o">.</span> <span class="n">lines</span>
</pre></div>
</td></tr></table></div>
<p>　最後に動かして本稿を締めます。
リスト10のように、動作しました。
しかし、100代が多いですね・・・。
高齢化社会です <a class="footnote-reference" href="#bb1" id="id13">[8]</a> 。</p>
<ul class="simple">
<li>リスト10: 動作確認</li>
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
13</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/Study1_Q4$ ghc q1_4_5.hs
ueda@remote:~/Study1_Q4$ cat data/ages | ./q1_4_5
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
<div class="section" id="id14">
<h2>9.6. おわりに<a class="headerlink" href="#id14" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は第1回勉強会4問目の問題を片付けました。
次回、5問目を・・・というところですが、
ここまでやってきてちっとも前に進まないので、
記事の趣旨を変えてOpen usp Tukubai
のHaskell版の話をしようかちょっと迷っています。
OK貰えたらOpen usp Tukubaiの話をやってみようかと思います。
より、実践的な内容になると思います。</p>
<p>　そりでは。</p>
</div>
<div class="section" id="id15">
<h2>9.7. お知らせ：コード募集<a class="headerlink" href="#id15" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="aa1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>編集部注: 本人にこれは何だと確認したら「こんにちは。」の略だが書くのが面倒だったのこと。なめてんのか。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="ee1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>水の中の昆虫です。新橋界隈、特にニュー新橋ビルではあんまり見かけないですね。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="ff1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>「<a class="reference external" href="http://ja.wikipedia.org/wiki">http://ja.wikipedia.org/wiki</a>/コオイムシ」より引用。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="gg1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>こんなにフリーダムに書いていて精神状態が悪いわけは無い。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="hh1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td><tt class="docutils literal"><span class="pre">https://github.com/ryuichiueda/UspMagazineHaskell/tree/master/Study1_Q4/data</span></tt></td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="cc1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[6]</a></td><td>正確には <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> を返す。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="jj1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id12">[7]</a></td><td>これ、なんとかなりませんかね？&gt; Haskellのエロい人。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="bb1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id13">[8]</a></td><td>違う。</td></tr>
</tbody>
</table>
</div>
</div>

