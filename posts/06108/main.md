---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年12月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>9. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p><br />
<blockquote><br />
<div>USP友の会のシェル芸勉強会<br />
（脚注：シェルのワンライナー勉強会）は、<br />
日々、他の言語からの他流試合に晒されているのである。<br />
そこで上田は、Haskellで自ら他流試合を行い、<br />
さらにシェル芸勉強会をいじめる自傷行為に手を<br />
染めるのであった。</div></blockquote><br />
<div class="section" id="id1"><br />
<h2>9.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　こ <a class="footnote-reference" href="#aa1" id="id2">[1]</a> 。富山の産んだブラックエンジェル上田です。<br />
最近、次女が重たくなってきて、背負いながら物を書いていると<br />
けっこうしんどくなって参りました。<br />
俺はコオイムシ <a class="footnote-reference" href="#ee1" id="id3">[2]</a> かと、そういう気分になります。<br />
「魚類、モノアラガイ、他の昆虫等を先端に二対の爪がある<br />
鎌状の前肢で積極的に捕らえ、口針から消化液を送り込み<br />
溶けた肉質を吸入する体外消化を行う。」<br />
ことも、<br />
「オスは卵塊保護中は動きを制約されるが、<br />
通常と変わらない程度に給餌もし、<br />
時には他のオスが卵を背負ってる時に、<br />
その卵を襲って捕食してしまう事もある。」<br />
ことも、コオイムシと私に共通した特徴です <a class="footnote-reference" href="#ff1" id="id4">[3]</a> 。<br />
漢字で書くと「好意無視」となるのも、<br />
なかなか素敵であり、ただならぬシンパシーを感じます。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>9.2. 前回のおさらい<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、なんか精神状態を問われそうなスタートになりましたが<br />
<a class="footnote-reference" href="#gg1" id="id6">[4]</a> 、<br />
本題に入りましょう。<br />
現在解いているのは第1回勉強会の4問目です。<br />
こんな問題でした。</p><br />
<blockquote><br />
<div>次のような <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルを作り、<br />
<tt class="docutils literal"><span class="pre">ans</span></tt> のように集計してください。</div></blockquote><br />
<p>　 <tt class="docutils literal"><span class="pre">ages</span></tt> と <tt class="docutils literal"><span class="pre">ans</span></tt> は図1のようなファイルです。<br />
GitHubにアップしてあります <a class="footnote-reference" href="#hh1" id="id7">[5]</a> 。<br />
<tt class="docutils literal"><span class="pre">ages</span></tt> はでかいのでブラウザで見ると<br />
メモリ圧迫人生圧迫圧迫面接なのでご注意を。</p><br />
<ul class="simple"><br />
<li>リスト1: インプットする <tt class="docutils literal"><span class="pre">ages</span></tt> ファイルと解答ファイル <tt class="docutils literal"><span class="pre">ans</span></tt></li><br />
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
20</pre></div></td><td class="code"><div class="highlight"><pre>###agesは0〜109（年齢）をランダムに書いたもの###<br />
ueda\@remote:~/Study1_Q4/data$ head -n 5 ages<br />
91<br />
35<br />
11<br />
100<br />
94<br />
###ansはagesの度数分布表###<br />
ueda\@remote:~/Study1_Q4/data$ cat ans<br />
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
<p>　前回はリスト2の <tt class="docutils literal"><span class="pre">q1_4_2.hs</span></tt> までを作りました。<br />
出力と共に示します。<br />
もう既に「何十代なのか」のリストができているので、<br />
これらを集計するだけです。</p><br />
<ul class="simple"><br />
<li>リスト2: 前回作成したコードq1_4_2.hsと実行結果</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_4_2</span><span class="o">.</span><span class="n">hs</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">cs</span> <span class="ow">&lt;-</span> <span class="n">getContents</span><br />
 <span class="n">print</span> <span class="p">[</span> <span class="mi">10</span> <span class="o">*</span> <span class="p">(</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span> <span class="ow">::</span> <span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span> <span class="p">)</span> <span class="o">|</span> <span class="n">c</span> <span class="ow">&lt;-</span> <span class="n">lines</span> <span class="n">cs</span> <span class="p">]</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">ghc</span> <span class="n">q1_4_2</span><span class="o">.</span><span class="n">hs</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="kr">data</span><span class="o">/</span><span class="n">ages</span> <span class="o">|</span> <span class="o">./</span><span class="n">q1_4_2</span> <span class="o">|</span> <span class="n">head</span> <span class="o">-</span><span class="n">c</span> <span class="mi">20</span><br />
<span class="p">[</span><span class="mi">90</span><span class="p">,</span><span class="mi">30</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">100</span><span class="p">,</span><span class="mi">90</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">7</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>9.3. ソートする<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて続きですが、6月号でも出てきた <tt class="docutils literal"><span class="pre">sort</span></tt><br />
関数を使ってリストをソートします。<br />
リスト3にソートまで記述したコードを示します。<br />
リスト2では各年齢の1の位を切り捨てた後、10をかけていますが、<br />
これは不要なので処理を消しました。<br />
また、sort関数を使うには <tt class="docutils literal"><span class="pre">Data.List</span></tt> というモジュールを<br />
インポートしますが、これも6月号で説明しました。</p><br />
<ul class="simple"><br />
<li>リスト3: リストをソートする処理を加えたq1_4_3.hsとその実行結果</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4$ cat q1_4_3.hs<br />
import Data.List<br />
<br />
main = do cs &lt;- getContents<br />
 print $ sort [ (read c :: Int) `div` 10 | c &lt;- lines cs ]<br />
ueda\@remote:~/Study1_Q4$ ghc q1_4_3.hs<br />
###とりあえずdat/agesの先頭の10行を渡してみる###<br />
ueda\@remote:~/Study1_Q4$ head data/ages | ./q1_4_3<br />
[0,1,3,7,9,9,9,10,10,10]<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リストの要素の個数をカウントするにはソートしない方法もあります。<br />
またソートするのは無駄なようにも思えます。<br />
しかし、ソートしない方法は<br />
データや要素の種類の多寡で有利不利が出てしまうので、<br />
あまり凝らずにソートに頼ることにしました。<br />
ここら辺の判断については意見の分かれるところですが、<br />
私は「いつ・誰が困るかどうか」で判断しています。</p><br />
<p>　なんかかっこいい人が「こうでなければならない！」<br />
とか本に書いていてそれを鵜呑みにするのはやめましょう。<br />
世の中に、無条件にこうでなければならないというものは、<br />
ありません。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h2>9.4. カウント処理<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、リストの集計を行います。<br />
<tt class="docutils literal"><span class="pre">count</span></tt> という関数をリスト4のように実装して、<br />
<tt class="docutils literal"><span class="pre">main</span></tt> 関数の処理に挟み込みます。<br />
<tt class="docutils literal"><span class="pre">count</span></tt> の出力は「n十代がm人いる」ことを示すリストです。<br />
10行目の <tt class="docutils literal"><span class="pre">where</span></tt> で定義している <tt class="docutils literal"><span class="pre">h</span></tt><br />
は、リストの先頭の要素で、<br />
その下の <tt class="docutils literal"><span class="pre">len</span></tt> が、 <tt class="docutils literal"><span class="pre">h</span></tt> が何個続いているか、<br />
最後の <tt class="docutils literal"><span class="pre">d</span></tt> が、リストの先頭から <tt class="docutils literal"><span class="pre">h</span></tt><br />
の並びを切り落としたリストです。<br />
<tt class="docutils literal"><span class="pre">d</span></tt> は、9行目で再び <tt class="docutils literal"><span class="pre">count</span></tt> に入力されます。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">count</span></tt> 関数が二つ定義されているのは、<br />
7月号で出てきた「パターンマッチ」ですね。<br />
8行目の定義は、引数が <tt class="docutils literal"><span class="pre">[]</span></tt> 、つまり空の場合にマッチし、<br />
この場合はそのまま空のリストを返します。<br />
9行目以降の定義は、8行目以外の場合、<br />
についてマッチします。</p><br />
<p>　Haskellは、普通の言語ではif文を使うような場合でも、<br />
このような仕組みが充実しているのでif文を避けることができます。<br />
これが見やすい・書きやすいかどうかは、<br />
読み手・書き手次第ですが・・・。<br />
ここら辺、読み手書き手にどれくらいのレベルや<br />
慣れを要求するとちょうどいいのかという問題は、<br />
おそらく答えが出ない話です。</p><br />
<ul class="simple"><br />
<li>リスト4: count関数を実装したq1_4_4.hs</li><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4$ cat q1_4_4.hs<br />
import Data.List<br />
<br />
main = do cs &lt;- getContents<br />
 print $ count $ sort [ (read c :: Int) `div` 10 | c &lt;- lines cs ]<br />
<br />
count :: [Int] -&gt; [(Int,Int)]<br />
count [] = []<br />
count ns = (h,len) : count d<br />
 where h = head ns<br />
 len = length $ takeWhile (== h) ns<br />
 d = dropWhile (== h) ns<br />
###出力###<br />
ueda\@remote:~/Study1_Q4$ ghc q1_4_4.hs<br />
ueda\@remote:~/Study1_Q4$ head data/ages | ./q1_4_4<br />
[(0,1),(1,1),(3,1),(7,1),(9,3),(10,3)]<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　11行目の <tt class="docutils literal"><span class="pre">takeWhile</span></tt> 関数については5月号でも出てきました。<br />
12行目の <tt class="docutils literal"><span class="pre">dropWhile</span></tt> 関数と共に、<br />
リスト5で挙動を見ておきましょう。</p><br />
<ul class="simple"><br />
<li>リスト5: takeWhile、dropWhileの挙動</li><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4$ ghci<br />
Prelude&gt; let ns = [0,0,1,2]<br />
###takeWhileは関数にマッチするまでの要素を取り出す###<br />
Prelude&gt; takeWhile (== 0) ns<br />
[0,0]<br />
###dropWhileは関数にマッチするまで要素を切り落とす###<br />
Prelude&gt; dropWhile (== 0) ns<br />
[1,2]<br />
###型は次の通り。Boolを返す関数とリストを引数にとる。###<br />
Prelude&gt; :t takeWhile<br />
takeWhile :: (a -&gt; Bool) -&gt; [a] -&gt; [a]<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>9.5. 整形して完成<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　最後に、 <tt class="docutils literal"><span class="pre">count</span></tt> の返すリストを整形してこの問題を終わらせましょう。<br />
リスト6のように、<br />
<tt class="docutils literal"><span class="pre">print</span></tt> の代わりに <tt class="docutils literal"><span class="pre">out</span></tt> という関数を定義して使います。<br />
この <tt class="docutils literal"><span class="pre">out</span></tt> では、リストの中の <tt class="docutils literal"><span class="pre">(n,m)</span></tt><br />
（n十代がm個）というデータを、一つずつ17、18行目で整形して出力しています。<br />
16行目の左辺の <tt class="docutils literal"><span class="pre">((g,num):es)</span></tt> は、<br />
<tt class="docutils literal"><span class="pre">(g,num)</span></tt> がリストの先頭、 <tt class="docutils literal"><span class="pre">es</span></tt> がそれ以外で、<br />
リストの先頭の <tt class="docutils literal"><span class="pre">(g,num)</span></tt> が17行目の <tt class="docutils literal"><span class="pre">oneline</span></tt><br />
を作るために使われ、<br />
<tt class="docutils literal"><span class="pre">es</span></tt> が再起的に <tt class="docutils literal"><span class="pre">out</span></tt> に渡されています。<br />
んで、 <tt class="docutils literal"><span class="pre">oneline</span></tt> と <tt class="docutils literal"><span class="pre">out</span></tt> の間に <tt class="docutils literal"><span class="pre">&gt;&gt;</span></tt><br />
という謎の記号がありますが、これの型を、<br />
これまでも何回か出て来た <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt><br />
の型とともにリスト7に示します。</p><br />
<ul class="simple"><br />
<li>リスト6: 出力を整形するq1_4_5.hs（完成）</li><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/Study1_Q4</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_4_5</span><span class="o">.</span><span class="n">hs</span><br />
<span class="kr">import</span> <span class="nn">Data.List</span><br />
<br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">cs</span> <span class="ow">&lt;-</span> <span class="n">getContents</span><br />
 <span class="n">out</span> <span class="o">$</span> <span class="n">count</span> <span class="o">$</span> <span class="n">sort</span> <span class="p">[</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span> <span class="ow">::</span> <span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span> <span class="o">|</span> <span class="n">c</span> <span class="ow">&lt;-</span> <span class="n">lines</span> <span class="n">cs</span> <span class="p">]</span><br />
<br />
<span class="nf">count</span> <span class="ow">::</span> <span class="p">[</span><span class="kt">Int</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">Int</span><span class="p">)]</span><br />
<span class="nf">count</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="kt">[]</span><br />
<span class="nf">count</span> <span class="n">ns</span> <span class="ow">=</span> <span class="p">(</span><span class="n">h</span><span class="p">,</span><span class="n">len</span><span class="p">)</span> <span class="kt">:</span> <span class="n">count</span> <span class="n">d</span><br />
 <span class="kr">where</span> <span class="n">h</span> <span class="ow">=</span> <span class="n">head</span> <span class="n">ns</span><br />
 <span class="n">len</span> <span class="ow">=</span> <span class="n">length</span> <span class="o">$</span> <span class="n">takeWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">h</span><span class="p">)</span> <span class="n">ns</span><br />
 <span class="n">d</span> <span class="ow">=</span> <span class="n">dropWhile</span> <span class="p">(</span><span class="o">==</span> <span class="n">h</span><span class="p">)</span> <span class="n">ns</span><br />
<br />
<span class="nf">out</span> <span class="ow">::</span> <span class="p">[(</span><span class="kt">Int</span><span class="p">,</span><span class="kt">Int</span><span class="p">)]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">out</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="n">return</span> <span class="nb">()</span><br />
<span class="nf">out</span> <span class="p">((</span><span class="n">g</span><span class="p">,</span><span class="n">num</span><span class="p">)</span><span class="kt">:</span><span class="n">es</span><span class="p">)</span> <span class="ow">=</span> <span class="n">putStrLn</span> <span class="n">oneline</span> <span class="o">&gt;&gt;</span> <span class="n">out</span> <span class="n">es</span><br />
 <span class="kr">where</span> <span class="n">oneline</span> <span class="ow">=</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="n">g</span><span class="o">*</span><span class="mi">10</span><span class="p">))</span> <span class="o">++</span> <span class="s">&quot;〜&quot;</span> <span class="o">++</span> <span class="p">(</span><span class="n">show</span> <span class="p">(</span><span class="n">g</span><span class="o">*</span><span class="mi">10</span><span class="o">+</span><span class="mi">9</span><span class="p">))</span><br />
 <span class="o">++</span> <span class="s">&quot; &quot;</span> <span class="o">++</span> <span class="p">(</span><span class="n">show</span> <span class="n">num</span><span class="p">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>リスト7: &gt;&gt;と&gt;&gt;=の違い</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">uedambp</span><span class="kt">:~</span> <span class="n">ueda</span><span class="o">$</span> <span class="n">ghci</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;</span><span class="p">)</span><br />
<span class="p">(</span><span class="o">&gt;&gt;</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span><br />
<span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これだけ見てもピンと来ないかもしれませんが、<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> は <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt><br />
の左側の出力を右側に渡しますが、<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;</span></tt> は渡しません。型を見たら分かるのですが、<br />
<tt class="docutils literal"><span class="pre">m</span> <span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span> <span class="pre">-&gt;</span> <span class="pre">m</span> <span class="pre">b</span></tt> の <tt class="docutils literal"><span class="pre">a</span></tt> が出力に残ってません。<br />
ですので、 <tt class="docutils literal"><span class="pre">putStrLn</span></tt> のように、<br />
関数としては何も出力しない<br />
<a class="footnote-reference" href="#cc1" id="id11">[6]</a><br />
ものが左側にあるときに使います。<br />
おそらく、ghciでリスト8のような例を示しておけばなんとなく分かるかと。</p><br />
<ul class="simple"><br />
<li>リスト8: &gt;&gt;の使用例</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">print</span> <span class="s">&quot;a&quot;</span> <span class="o">&gt;&gt;</span> <span class="n">print</span> <span class="s">&quot;b&quot;</span> <span class="o">&gt;&gt;</span> <span class="n">print</span> <span class="s">&quot;c&quot;</span><br />
<span class="s">&quot;a&quot;</span><br />
<span class="s">&quot;b&quot;</span><br />
<span class="s">&quot;c&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の使い方も触れておくために、<br />
<tt class="docutils literal"><span class="pre">q1_4_5.hs</span></tt> の <tt class="docutils literal"><span class="pre">main</span></tt> 関数を<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を使って書き直したのでリスト9<br />
に示します。<br />
ほとんどシェル芸です・・・。<br />
唯一違うのは右から左に読まなければならんことですが<br />
<a class="footnote-reference" href="#jj1" id="id12">[7]</a> 。</p><br />
<ul class="simple"><br />
<li>リスト9: &gt;&gt;=を使ってmain関数を書き直したもの</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">out</span> <span class="o">.</span> <span class="n">count</span> <span class="o">.</span> <span class="n">sort</span> <span class="o">.</span><br />
 <span class="n">map</span> <span class="p">(</span><span class="nf">\\</span><span class="n">c</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">read</span> <span class="n">c</span><span class="ow">::</span><span class="kt">Int</span><span class="p">)</span> <span class="p">`</span><span class="n">div</span><span class="p">`</span> <span class="mi">10</span><span class="p">)</span> <span class="o">.</span> <span class="n">lines</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　最後に動かして本稿を締めます。<br />
リスト10のように、動作しました。<br />
しかし、100代が多いですね・・・。<br />
高齢化社会です <a class="footnote-reference" href="#bb1" id="id13">[8]</a> 。</p><br />
<ul class="simple"><br />
<li>リスト10: 動作確認</li><br />
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
13</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/Study1_Q4$ ghc q1_4_5.hs<br />
ueda\@remote:~/Study1_Q4$ cat data/ages | ./q1_4_5<br />
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
<div class="section" id="id14"><br />
<h2>9.6. おわりに<a class="headerlink" href="#id14" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は第1回勉強会4問目の問題を片付けました。<br />
次回、5問目を・・・というところですが、<br />
ここまでやってきてちっとも前に進まないので、<br />
記事の趣旨を変えてOpen usp Tukubai<br />
のHaskell版の話をしようかちょっと迷っています。<br />
OK貰えたらOpen usp Tukubaiの話をやってみようかと思います。<br />
より、実践的な内容になると思います。</p><br />
<p>　そりでは。</p><br />
</div><br />
<div class="section" id="id15"><br />
<h2>9.7. お知らせ：コード募集<a class="headerlink" href="#id15" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　本稿で出た問題のHaskellのコードを、<br />
名前あるいはハンドルネームと共に送ってください。<br />
短いもの、あるいは変態的なものをお願いいたします。</p><br />
<p>email: 編集部のメールアドレス</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="aa1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>編集部注: 本人にこれは何だと確認したら「こんにちは。」の略だが書くのが面倒だったのこと。なめてんのか。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="ee1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>水の中の昆虫です。新橋界隈、特にニュー新橋ビルではあんまり見かけないですね。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="ff1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>「<a class="reference external" href="http://ja.wikipedia.org/wiki">http://ja.wikipedia.org/wiki</a>/コオイムシ」より引用。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="gg1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>こんなにフリーダムに書いていて精神状態が悪いわけは無い。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="hh1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id7">[5]</a></td><td><tt class="docutils literal"><span class="pre">https://github.com/ryuichiueda/UspMagazineHaskell/tree/master/Study1_Q4/data</span></tt></td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="cc1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id11">[6]</a></td><td>正確には <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> を返す。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="jj1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id12">[7]</a></td><td>これ、なんとかなりませんかね？&gt; Haskellのエロい人。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="bb1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id13">[8]</a></td><td>違う。</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

