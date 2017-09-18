---
Copyright: (C) Ryuichi Ueda
---

# USP Magazine 2015年3月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>12. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p><br />
<blockquote><br />
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア<br />
状態なので、連載しながら開発しようと思い立った上田は、<br />
不幸にも黒塗りの高級車に追突してしまう。後輩をかばい<br />
すべての責任を負った上田に対し、車の主、暴力団員谷岡に<br />
言い渡された示談の条件とは...。</div></blockquote><br />
<div class="section" id="id1"><br />
<h2>12.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　みなさんこんにちは。これ書いているのが12/24深夜です。やさぐれています。<br />
妻がいて、二人子供がいようがなんだろうが、<br />
素直にクリスマスとかほざく気にはなりません。<br />
突き詰めて考えると、非リア充かリア充かというのは<br />
結局脳内麻薬が出ないか出るかだけですよ。境遇関係ありません。<br />
ラリってる連中が面倒臭い。心底面倒臭い。<br />
自分たちで楽しみ見つけやがれ。もっと申し訳なさそうに生きろ。</p><br />
<p>　みなさんこんにちは。富山の生んだブラックエンジェル<br />
（エンジェルなのに浄土真宗）上田です。<br />
え？私なにか言いました？何も言ってませんよ。<br />
さっさと本題行きましょう。本題。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>12.2. 今月の作業<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　現在、 <tt class="docutils literal"><span class="pre">map</span></tt> というコマンドを作成中です。<br />
前回はリスト1のように、「キー、サブキー、値」<br />
というレコードを持つデータを、キーを縦軸、<br />
サブキーを横軸にした表に変換するコマンドです。</p><br />
<ul class="simple"><br />
<li>リスト1: mapの動作</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ~/data<br />
a あ 1<br />
b い 2<br />
b う 3<br />
<span class="nv">$ </span>cat ~/data | map <span class="nv">num</span><span class="o">=</span>1<br />
* あ い う<br />
a 1 0 0<br />
b 0 2 3<br />
</pre></div><br />
</td></tr></table></div><br />
<p>詳細な仕様は、リポジトリの <tt class="docutils literal"><span class="pre">MANUAL/map.txt</span></tt><br />
内にあります。</p><br />
<p>　前回は、リスト2のように、データを受け入れて<br />
リストにするところまで作っていました。<br />
リスト2で示した <tt class="docutils literal"><span class="pre">map.5.hs</span></tt> は</p><br />
<blockquote><br />
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote><br />
<p>にあります。<br />
今回はこれをどんどん再集計に近づけます。</p><br />
<ul class="simple"><br />
<li>リスト2: map.5.hsをコンパイルして実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data<br />
a あ 1<br />
b い 2<br />
b う 3<br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.5 <span class="nv">num</span><span class="o">=</span>1<br />
<span class="o">[(</span><span class="s2">&quot;a&quot;</span>,<span class="s2">&quot;\\227\\129\\130&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\132&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\134&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id3"><br />
<h2>12.3. 横軸を取り出す<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、最初にやるのはサブキーのリストを作るところです。<br />
<tt class="docutils literal"><span class="pre">map</span></tt> が受け付けるデータはソート済みのデータですが、<br />
ソート順が何か特別な順番になっているかもしれませんので、<br />
順番を崩さないようにしないといけません。<br />
縦軸は出てきた順に表示すればよいでしょうが、<br />
横軸についてはちょっと頭を捻らないといけません。</p><br />
<p>　一つ例を出します。リスト3は、第2列目のサブキーがMon、Tue、Fri<br />
と並んでますが、これをその順番で出さなければなりません<br />
<a class="footnote-reference" href="#id9" id="id4">[1]</a> 。</p><br />
<ul class="simple"><br />
<li>リスト3: サブキーの出力順の例</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data2<br />
2013 Mon 1<br />
2013 Tue 1<br />
2014 Mon 2<br />
2014 Fri 3<br />
<span class="nv">$ </span>cat data2 | map <span class="nv">num</span><span class="o">=</span>1<br />
* Mon Tue Fri<br />
2013 1 1 0<br />
2014 2 0 3<br />
</pre></div><br />
</td></tr></table></div><br />
<p>サブキーを取り出してソートして重複を取り除けばできるのですが、<br />
ややこしいことに、 <tt class="docutils literal"><span class="pre">map</span></tt> ではデータで出てきた<br />
順番に表示しなければなりません。<br />
ということで、リスト4のように <tt class="docutils literal"><span class="pre">map.6.hs</span></tt> を作りました。<br />
変更したのはヘッダと <tt class="docutils literal"><span class="pre">main'</span></tt> 関数なので、<br />
そこだけ示します。<br />
<tt class="docutils literal"><span class="pre">Line</span></tt> 型については変更していませんが、<br />
重要なので再掲します。</p><br />
<ul class="simple"><br />
<li>リスト4: map.6.hs（map.5.hsからの変更部分のみ）</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>###ヘッダの変更###<br />
import qualified Data.ByteString.Lazy.Char8 as BS<br />
###Lineの型###<br />
type Line = (Key,SubKey,Values)<br />
###main&#39;の変更###<br />
main&#39; :: Either String Int -&gt; BS.ByteString -&gt; IO ()<br />
main&#39; (Left str) cs = die str<br />
main&#39; (Right num) cs = print h_axis -- for debug<br />
 where d = [ makeLine num ln | ln &lt;- BS.lines cs ]<br />
 h_axis = hAxis $ map ( \\(_,s,_) -&gt; s ) d<br />
 hAxis [] = []<br />
 hAxis (e:es) = e : (hAxis $ filter ( /= e ) es )<br />
</pre></div><br />
</td></tr></table></div><br />
<p>8行目で <tt class="docutils literal"><span class="pre">print</span></tt> している <tt class="docutils literal"><span class="pre">h_axis</span></tt> がサブキーのリストです。<br />
10行目で作っていますが、結構ややこしい書き方をしていますので、<br />
丁寧に説明していきます。</p><br />
<p>　まず <tt class="docutils literal"><span class="pre">map</span></tt> に渡している無名関数 <tt class="docutils literal"><span class="pre">\\(_,s,_)</span> <span class="pre">-&gt;</span> <span class="pre">s</span></tt><br />
ですが、これは <tt class="docutils literal"><span class="pre">Line</span></tt> 型を構成している<br />
<tt class="docutils literal"><span class="pre">(Key,SubKey,Values)</span></tt> の組から <tt class="docutils literal"><span class="pre">SubKey</span></tt><br />
だけ出力するという意味になります。<br />
ですので、10行目の <tt class="docutils literal"><span class="pre">hAxis</span></tt> 関数にはサブキーのリスト<br />
が渡されます。このリストのキーは重複しているので、<br />
<tt class="docutils literal"><span class="pre">hAxis</span></tt> 関数でそれを除去します。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">hAxis</span></tt> は11、12行目で定義されています。<br />
<tt class="docutils literal"><span class="pre">where</span></tt> の中で定義されており、 <tt class="docutils literal"><span class="pre">main'</span></tt> の中だけで使えます。<br />
この <tt class="docutils literal"><span class="pre">hAxis</span></tt> は、データの重複を除去しているのですが、理解できるでしょうか。<br />
12行目での入力されたリストを先頭の <tt class="docutils literal"><span class="pre">e</span></tt> とそれ以外の <tt class="docutils literal"><span class="pre">es</span></tt><br />
に分け、出力では <tt class="docutils literal"><span class="pre">e</span></tt> を残し、 <tt class="docutils literal"><span class="pre">es</span></tt> から <tt class="docutils literal"><span class="pre">e</span></tt> と同じ要素を<br />
除去したものを再度 <tt class="docutils literal"><span class="pre">hAxis</span></tt> に渡し、その出力を <tt class="docutils literal"><span class="pre">e</span></tt> の後ろに<br />
<tt class="docutils literal"><span class="pre">:</span></tt> で連結して出力としています。<br />
結果、10行目の <tt class="docutils literal"><span class="pre">h_axis</span></tt> は、<br />
入力順を崩さずに重複が除去されたリストになります。<br />
動かしたものをリスト5に示しておきます。</p><br />
<ul class="simple"><br />
<li>リスト5: map.6.hsをコンパイルして動作確認</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">data2</span> <span class="o">|</span> <span class="o">./</span><span class="n">map</span><span class="o">.</span><span class="mi">6</span> <span class="n">num</span><span class="ow">=</span><span class="mi">1</span><br />
<span class="p">[</span><span class="s">&quot;Mon&quot;</span><span class="p">,</span><span class="s">&quot;Tue&quot;</span><span class="p">,</span><span class="s">&quot;Fri&quot;</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ところで、 <tt class="docutils literal"><span class="pre">map.6.hs</span></tt> のヘッダには、<br />
<tt class="docutils literal"><span class="pre">map.5.hs</span></tt> にはなかった <tt class="docutils literal"><span class="pre">qualified</span></tt><br />
という文言をつけました。<br />
これは、 <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> モジュール<br />
の関数には必ず <tt class="docutils literal"><span class="pre">BS.</span></tt> をつけるようにしろという命令です。<br />
前回までのように <tt class="docutils literal"><span class="pre">hiding</span></tt> でやっているときりがないので使いました。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>12.4. ヘッダを出力<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次はヘッダを出力しましょう。<br />
キーのフィールド数だけ <tt class="docutils literal"><span class="pre">*</span></tt> を埋めて出力します。<br />
リスト6に <tt class="docutils literal"><span class="pre">map.7.hs</span></tt> を示します。<br />
<tt class="docutils literal"><span class="pre">header</span></tt> という名前の関数を実装して <tt class="docutils literal"><span class="pre">main'</span></tt><br />
で使っています。</p><br />
<ul class="simple"><br />
<li>リスト6: ヘッダを出力するmap.7.hs</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;関数（リスト4の8行目を次のように変更）###<br />
main&#39; (Right num) cs = header num h_axis<br />
###新たにheader関数を実装###<br />
header :: Int -&gt; [SubKey] -&gt; IO ()<br />
header num ss = BS.putStrLn $ BS.unwords (keyf ++ ss)<br />
 where keyf = replicate num (BS.pack &quot;*&quot;)<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　6行目の <tt class="docutils literal"><span class="pre">keyf</span></tt> には縦軸のキーフィールド数（ <tt class="docutils literal"><span class="pre">num</span></tt> ）<br />
だけ <tt class="docutils literal"><span class="pre">*</span></tt> のリストを作っています。<br />
<tt class="docutils literal"><span class="pre">replicate</span></tt> 関数は、第1引数で指定した個数だけ<br />
第2引数の要素を持つリストを出力します。<br />
<tt class="docutils literal"><span class="pre">BS.pack</span></tt> は、String型の文字列を <tt class="docutils literal"><span class="pre">ByteString</span></tt> 型に変換する関数です。<br />
5行目で <tt class="docutils literal"><span class="pre">keyf</span></tt> を横軸のキーにくっつけて <tt class="docutils literal"><span class="pre">BS.unwords</span></tt><br />
で空白を挟んでリストを連結し、出力しています。</p><br />
<ul class="simple"><br />
<li>リスト7: map.7.hsをコンパイルして動作確認</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data2 | ./map.7 <span class="nv">num</span><span class="o">=</span>1<br />
* Mon Tue Fri<br />
<span class="nv">$ </span>cat data | ./map.7 <span class="nv">num</span><span class="o">=</span>1<br />
* あ い う<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>12.5. ボディーを出力<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　いよいよ本体の出力です。<br />
ただ、いきなり出力するのではなく、<br />
キーごとにデータを分けることからやっていきましょう。<br />
<tt class="docutils literal"><span class="pre">map.7.hs</span></tt> からリスト8のように <tt class="docutils literal"><span class="pre">map.8.hs</span></tt> を作りました。</p><br />
<ul class="simple"><br />
<li>リスト8: map.8.hs</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;のheader関数の後ろに追記###<br />
main&#39; (Right num) cs = header num h_axis &gt;&gt; mapM_ print (splitByKey d)<br />
###splitByKey関数を追加###<br />
splitByKey :: [Line] -&gt; [[Line]]<br />
splitByKey [] = []<br />
splitByKey lns\@((key,_,_):_) = a : splitByKey b<br />
 where a = takeWhile (\\(k,_,_) -&gt; key == k) lns<br />
 b = dropWhile (\\(k,_,_) -&gt; key == k) lns<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　先に実行して結果を見ておきましょう。<br />
リスト9のようにキーごとにレコードが<br />
まとまります。</p><br />
<ul class="simple"><br />
<li>リスト9: map.8.hsをコンパイルして実行</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ./data2 | ./map.8 <span class="nv">num</span><span class="o">=</span>1<br />
* Mon Tue Fri<br />
<span class="o">[(</span><span class="s2">&quot;2013&quot;</span>,<span class="s2">&quot;Mon&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;2013&quot;</span>,<span class="s2">&quot;Tue&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])]</span><br />
<span class="o">[(</span><span class="s2">&quot;2014&quot;</span>,<span class="s2">&quot;Mon&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;2014&quot;</span>,<span class="s2">&quot;Fri&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、リスト8は短いながらもたくさんのことをやっていますし、<br />
新しいモノも登場しています。<br />
まず、2行目の <tt class="docutils literal"><span class="pre">mapM_</span></tt> というへんちくりんな名前の関数ですが、<br />
これは <tt class="docutils literal"><span class="pre">print</span></tt> のようにモナドを出す関数をmapするものです。<br />
リスト10のように、 <tt class="docutils literal"><span class="pre">mapM_</span> <span class="pre">print</span></tt><br />
でリストのものを一つずつ出力するという意味になります。</p><br />
<ul class="simple"><br />
<li>リスト10: <tt class="docutils literal"><span class="pre">mapM_</span></tt> の型と <tt class="docutils literal"><span class="pre">mapM_</span> <span class="pre">print</span></tt> の実行例</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM_</span><br />
<span class="nf">mapM_</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="nb">()</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM_</span> <span class="n">print</span><br />
<span class="nf">mapM_</span> <span class="n">print</span> <span class="ow">::</span> <span class="kt">Show</span> <span class="n">a</span> <span class="ow">=&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">mapM_</span> <span class="n">print</span> <span class="p">[</span><span class="s">&quot;This&quot;</span><span class="p">,</span><span class="s">&quot;is&quot;</span><span class="p">,</span><span class="s">&quot;a&quot;</span><span class="p">,</span><span class="s">&quot;pen&quot;</span><span class="p">]</span><br />
<span class="s">&quot;This&quot;</span><br />
<span class="s">&quot;is&quot;</span><br />
<span class="s">&quot;a&quot;</span><br />
<span class="s">&quot;pen&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて次に、リスト8の <tt class="docutils literal"><span class="pre">splitByKey</span></tt> 関数の説明を。<br />
これは <tt class="docutils literal"><span class="pre">[List]</span></tt> 型のデータ、<br />
つまり各レコードのリストを入力されると、<br />
キーが同じデータごとにぶった切られて<br />
リストのリストを出します。<br />
6行目の <tt class="docutils literal"><span class="pre">a</span></tt> がキーが同じレコードの塊で、<br />
<tt class="docutils literal"><span class="pre">b</span></tt> が残りのレコードです。<br />
<tt class="docutils literal"><span class="pre">b</span></tt> は再度 <tt class="docutils literal"><span class="pre">splitByKey</span></tt> にぶち込まれてぶった切られます。</p><br />
<p>　まず目新しいのは6行目の引数にある <tt class="docutils literal"><span class="pre">&#64;</span></tt><br />
だと思います。これは「アズパターン（as-pattern）」<br />
というもので、要は <tt class="docutils literal"><span class="pre">lns&#64;((key,_,_):_)</span></tt><br />
と左辺にあれば、右辺では引数を <tt class="docutils literal"><span class="pre">lns</span></tt> として使っても<br />
<tt class="docutils literal"><span class="pre">((key,s,v):_)</span></tt> として使ってもいいよということになります。<br />
<tt class="docutils literal"><span class="pre">lns</span></tt> は7, 8行目の <tt class="docutils literal"><span class="pre">takeWhile,</span> <span class="pre">dropWhile</span></tt> の第二引数として、<br />
<tt class="docutils literal"><span class="pre">key</span></tt> は7, 8行目の無名関数内で使用されています。<br />
<tt class="docutils literal"><span class="pre">lns</span></tt> と <tt class="docutils literal"><span class="pre">key</span></tt> のどっちか一方しか使えないと、<br />
コーディングが少々面倒くさくなるのですが、<br />
実際どう面倒臭くなるかはご自身でお確かめください。<br />
<tt class="docutils literal"><span class="pre">takeWhile,</span> <span class="pre">dropWhile</span></tt> は以前も出てきました。<br />
第一引数の式を第二引数のリストの先頭の要素から適用し、<br />
<tt class="docutils literal"><span class="pre">True</span></tt> を返してくる限り取得した/捨てたリストを返す関数です。</p><br />
<p>　さて、仕上げにかかりましょう。<br />
リスト11に完成した <tt class="docutils literal"><span class="pre">map.hs</span></tt> の一部を示します。<br />
<tt class="docutils literal"><span class="pre">map.8.hs</span></tt> からの変更部分だけ示しています。<br />
2行目の <tt class="docutils literal"><span class="pre">print</span></tt> 関数が <tt class="docutils literal"><span class="pre">body</span> <span class="pre">h_axis</span></tt><br />
に置き換わり、 <tt class="docutils literal"><span class="pre">body</span></tt> 関数、 <tt class="docutils literal"><span class="pre">body'</span></tt><br />
関数が新たに実装されています。</p><br />
<ul class="simple"><br />
<li>リスト11: 完成した <tt class="docutils literal"><span class="pre">map.hs</span></tt></li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;関数を変更（printをbody h_axisに置き換え）###<br />
main&#39; (Right num) cs = header num h_axis &gt;&gt; mapM_ (body h_axis) (splitByKey d)<br />
###body、body&#39;関数###<br />
body :: [SubKey] -&gt; [Line] -&gt; IO ()<br />
body ss lns\@((k,_,_):_) = BS.putStrLn $ BS.unwords (k:(body&#39; ss lns))<br />
<br />
body&#39; :: [SubKey] -&gt; [Line] -&gt; [Word]<br />
body&#39; [] _ = []<br />
body&#39; subs [] = replicate (length subs) (BS.pack &quot;0&quot;)<br />
body&#39; (sub:subs) alns\@((_,s,(v:_)):lns)<br />
 | sub == s = v : body&#39; subs lns<br />
 | otherwise = BS.pack &quot;0&quot; : body&#39; subs alns<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">body</span></tt> 関数のやっていることは、<br />
出力の各行の先頭にキーをつけることだけです。<br />
キー以降のデータは <tt class="docutils literal"><span class="pre">body'</span></tt> で作っています。<br />
<tt class="docutils literal"><span class="pre">body'</span></tt> がかなりややこしくなっていますが、<br />
サブキーに対応する数字を一つずつリスト化しているだけです。<br />
まず8行目が、サブキーがなくなって <tt class="docutils literal"><span class="pre">body'</span></tt> の再帰を終える処理、<br />
9行目が、サブキーは残っているけど <tt class="docutils literal"><span class="pre">Line</span></tt><br />
型のレコードがなくなったときの処理で、<br />
ゼロを残ったサブキーの個数分だけリストにして返しています。<br />
11行目は引数の先頭のサブキーと先頭のレコードのサブキーが一致したときに、<br />
レコードの値をリストに追加する処理、<br />
12行目はサブキーが一致しないときにゼロをリストに追加する処理です。<br />
とにかくサブキー1個につき1個データをリストに加えていっているというのを<br />
確かめながら読んでいくと、なんとか理解できるかと思います。</p><br />
<p>あと、 <tt class="docutils literal"><span class="pre">Line</span></tt> 型 <tt class="docutils literal"><span class="pre">(Key,SubKey,Values)</span></tt> 型では <tt class="docutils literal"><span class="pre">Values</span></tt><br />
のところが一つの値でなくリストになっており、これもややこしい原因になっています。<br />
実は <tt class="docutils literal"><span class="pre">map</span></tt> コマンドはキー、サブキーに対して値を複数持たせることが<br />
できるのでこのように <tt class="docutils literal"><span class="pre">List</span></tt> 型を定義しました。しかし、<br />
本連載では複数の値があるときの処理は割愛したいと思います。<br />
ということで、一応これで完成ということで、<br />
次回からは別のコマンドを扱いたいと思います。</p><br />
</div><br />
<div class="section" id="id7"><br />
<h2>12.6. おわりに<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は愚痴から始まり、 <tt class="docutils literal"><span class="pre">map</span></tt> （の最低限の機能）を<br />
作るところまでを扱いました。<br />
次回は上記のように別のコマンドに話題が移ります。<br />
さてどのコマンドをやりましょうか・・・。<br />
とりあえずもう眠いので寝てから考えることにします<br />
<a class="footnote-reference" href="#id10" id="id8">[2]</a> 。</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id9" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[1]</a></td><td>実はPython版のmapはMon、Fri、Tueの順番で出力してしまいます。<br />
ちょっと手がまわらないのでどなたか助けて・・・。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id10" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id8">[2]</a></td><td>今回、脚注が少ないのはきっとクリスマスのスカラー電磁波の仕業です。</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div><br />

