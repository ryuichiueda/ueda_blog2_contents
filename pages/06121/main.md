---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2015年3月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>12. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア
状態なので、連載しながら開発しようと思い立った上田は、
不幸にも黒塗りの高級車に追突してしまう。後輩をかばい
すべての責任を負った上田に対し、車の主、暴力団員谷岡に
言い渡された示談の条件とは...。</div></blockquote>
<div class="section" id="id1">
<h2>12.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　みなさんこんにちは。これ書いているのが12/24深夜です。やさぐれています。
妻がいて、二人子供がいようがなんだろうが、
素直にクリスマスとかほざく気にはなりません。
突き詰めて考えると、非リア充かリア充かというのは
結局脳内麻薬が出ないか出るかだけですよ。境遇関係ありません。
ラリってる連中が面倒臭い。心底面倒臭い。
自分たちで楽しみ見つけやがれ。もっと申し訳なさそうに生きろ。</p>
<p>　みなさんこんにちは。富山の生んだブラックエンジェル
（エンジェルなのに浄土真宗）上田です。
え？私なにか言いました？何も言ってませんよ。
さっさと本題行きましょう。本題。</p>
</div>
<div class="section" id="id2">
<h2>12.2. 今月の作業<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　現在、 <tt class="docutils literal"><span class="pre">map</span></tt> というコマンドを作成中です。
前回はリスト1のように、「キー、サブキー、値」
というレコードを持つデータを、キーを縦軸、
サブキーを横軸にした表に変換するコマンドです。</p>
<ul class="simple">
<li>リスト1: mapの動作</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ~/data
a あ 1
b い 2
b う 3
<span class="nv">$ </span>cat ~/data | map <span class="nv">num</span><span class="o">=</span>1
* あ い う
a 1 0 0
b 0 2 3
</pre></div>
</td></tr></table></div>
<p>詳細な仕様は、リポジトリの <tt class="docutils literal"><span class="pre">MANUAL/map.txt</span></tt>
内にあります。</p>
<p>　前回は、リスト2のように、データを受け入れて
リストにするところまで作っていました。
リスト2で示した <tt class="docutils literal"><span class="pre">map.5.hs</span></tt> は</p>
<blockquote>
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote>
<p>にあります。
今回はこれをどんどん再集計に近づけます。</p>
<ul class="simple">
<li>リスト2: map.5.hsをコンパイルして実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data
a あ 1
b い 2
b う 3
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.5 <span class="nv">num</span><span class="o">=</span>1
<span class="o">[(</span><span class="s2">&quot;a&quot;</span>,<span class="s2">&quot;\\227\\129\\130&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\132&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;b&quot;</span>,<span class="s2">&quot;\\227\\129\\134&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id3">
<h2>12.3. 横軸を取り出す<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、最初にやるのはサブキーのリストを作るところです。
<tt class="docutils literal"><span class="pre">map</span></tt> が受け付けるデータはソート済みのデータですが、
ソート順が何か特別な順番になっているかもしれませんので、
順番を崩さないようにしないといけません。
縦軸は出てきた順に表示すればよいでしょうが、
横軸についてはちょっと頭を捻らないといけません。</p>
<p>　一つ例を出します。リスト3は、第2列目のサブキーがMon、Tue、Fri
と並んでますが、これをその順番で出さなければなりません
<a class="footnote-reference" href="#id9" id="id4">[1]</a> 。</p>
<ul class="simple">
<li>リスト3: サブキーの出力順の例</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data2
2013 Mon 1
2013 Tue 1
2014 Mon 2
2014 Fri 3
<span class="nv">$ </span>cat data2 | map <span class="nv">num</span><span class="o">=</span>1
* Mon Tue Fri
2013 1 1 0
2014 2 0 3
</pre></div>
</td></tr></table></div>
<p>サブキーを取り出してソートして重複を取り除けばできるのですが、
ややこしいことに、 <tt class="docutils literal"><span class="pre">map</span></tt> ではデータで出てきた
順番に表示しなければなりません。
ということで、リスト4のように <tt class="docutils literal"><span class="pre">map.6.hs</span></tt> を作りました。
変更したのはヘッダと <tt class="docutils literal"><span class="pre">main'</span></tt> 関数なので、
そこだけ示します。
<tt class="docutils literal"><span class="pre">Line</span></tt> 型については変更していませんが、
重要なので再掲します。</p>
<ul class="simple">
<li>リスト4: map.6.hs（map.5.hsからの変更部分のみ）</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>###ヘッダの変更###
import qualified Data.ByteString.Lazy.Char8 as BS
###Lineの型###
type Line = (Key,SubKey,Values)
###main&#39;の変更###
main&#39; :: Either String Int -&gt; BS.ByteString -&gt; IO ()
main&#39; (Left str) cs = die str
main&#39; (Right num) cs = print h_axis -- for debug
 where d = [ makeLine num ln | ln &lt;- BS.lines cs ]
 h_axis = hAxis $ map ( \\(_,s,_) -&gt; s ) d
 hAxis [] = []
 hAxis (e:es) = e : (hAxis $ filter ( /= e ) es )
</pre></div>
</td></tr></table></div>
<p>8行目で <tt class="docutils literal"><span class="pre">print</span></tt> している <tt class="docutils literal"><span class="pre">h_axis</span></tt> がサブキーのリストです。
10行目で作っていますが、結構ややこしい書き方をしていますので、
丁寧に説明していきます。</p>
<p>　まず <tt class="docutils literal"><span class="pre">map</span></tt> に渡している無名関数 <tt class="docutils literal"><span class="pre">\\(_,s,_)</span> <span class="pre">-&gt;</span> <span class="pre">s</span></tt>
ですが、これは <tt class="docutils literal"><span class="pre">Line</span></tt> 型を構成している
<tt class="docutils literal"><span class="pre">(Key,SubKey,Values)</span></tt> の組から <tt class="docutils literal"><span class="pre">SubKey</span></tt>
だけ出力するという意味になります。
ですので、10行目の <tt class="docutils literal"><span class="pre">hAxis</span></tt> 関数にはサブキーのリスト
が渡されます。このリストのキーは重複しているので、
<tt class="docutils literal"><span class="pre">hAxis</span></tt> 関数でそれを除去します。</p>
<p>　 <tt class="docutils literal"><span class="pre">hAxis</span></tt> は11、12行目で定義されています。
<tt class="docutils literal"><span class="pre">where</span></tt> の中で定義されており、 <tt class="docutils literal"><span class="pre">main'</span></tt> の中だけで使えます。
この <tt class="docutils literal"><span class="pre">hAxis</span></tt> は、データの重複を除去しているのですが、理解できるでしょうか。
12行目での入力されたリストを先頭の <tt class="docutils literal"><span class="pre">e</span></tt> とそれ以外の <tt class="docutils literal"><span class="pre">es</span></tt>
に分け、出力では <tt class="docutils literal"><span class="pre">e</span></tt> を残し、 <tt class="docutils literal"><span class="pre">es</span></tt> から <tt class="docutils literal"><span class="pre">e</span></tt> と同じ要素を
除去したものを再度 <tt class="docutils literal"><span class="pre">hAxis</span></tt> に渡し、その出力を <tt class="docutils literal"><span class="pre">e</span></tt> の後ろに
<tt class="docutils literal"><span class="pre">:</span></tt> で連結して出力としています。
結果、10行目の <tt class="docutils literal"><span class="pre">h_axis</span></tt> は、
入力順を崩さずに重複が除去されたリストになります。
動かしたものをリスト5に示しておきます。</p>
<ul class="simple">
<li>リスト5: map.6.hsをコンパイルして動作確認</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">$</span> <span class="n">cat</span> <span class="n">data2</span> <span class="o">|</span> <span class="o">./</span><span class="n">map</span><span class="o">.</span><span class="mi">6</span> <span class="n">num</span><span class="ow">=</span><span class="mi">1</span>
<span class="p">[</span><span class="s">&quot;Mon&quot;</span><span class="p">,</span><span class="s">&quot;Tue&quot;</span><span class="p">,</span><span class="s">&quot;Fri&quot;</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>　ところで、 <tt class="docutils literal"><span class="pre">map.6.hs</span></tt> のヘッダには、
<tt class="docutils literal"><span class="pre">map.5.hs</span></tt> にはなかった <tt class="docutils literal"><span class="pre">qualified</span></tt>
という文言をつけました。
これは、 <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> モジュール
の関数には必ず <tt class="docutils literal"><span class="pre">BS.</span></tt> をつけるようにしろという命令です。
前回までのように <tt class="docutils literal"><span class="pre">hiding</span></tt> でやっているときりがないので使いました。</p>
</div>
<div class="section" id="id5">
<h2>12.4. ヘッダを出力<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次はヘッダを出力しましょう。
キーのフィールド数だけ <tt class="docutils literal"><span class="pre">*</span></tt> を埋めて出力します。
リスト6に <tt class="docutils literal"><span class="pre">map.7.hs</span></tt> を示します。
<tt class="docutils literal"><span class="pre">header</span></tt> という名前の関数を実装して <tt class="docutils literal"><span class="pre">main'</span></tt>
で使っています。</p>
<ul class="simple">
<li>リスト6: ヘッダを出力するmap.7.hs</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;関数（リスト4の8行目を次のように変更）###
main&#39; (Right num) cs = header num h_axis
###新たにheader関数を実装###
header :: Int -&gt; [SubKey] -&gt; IO ()
header num ss = BS.putStrLn $ BS.unwords (keyf ++ ss)
 where keyf = replicate num (BS.pack &quot;*&quot;)
</pre></div>
</td></tr></table></div>
<p>　6行目の <tt class="docutils literal"><span class="pre">keyf</span></tt> には縦軸のキーフィールド数（ <tt class="docutils literal"><span class="pre">num</span></tt> ）
だけ <tt class="docutils literal"><span class="pre">*</span></tt> のリストを作っています。
<tt class="docutils literal"><span class="pre">replicate</span></tt> 関数は、第1引数で指定した個数だけ
第2引数の要素を持つリストを出力します。
<tt class="docutils literal"><span class="pre">BS.pack</span></tt> は、String型の文字列を <tt class="docutils literal"><span class="pre">ByteString</span></tt> 型に変換する関数です。
5行目で <tt class="docutils literal"><span class="pre">keyf</span></tt> を横軸のキーにくっつけて <tt class="docutils literal"><span class="pre">BS.unwords</span></tt>
で空白を挟んでリストを連結し、出力しています。</p>
<ul class="simple">
<li>リスト7: map.7.hsをコンパイルして動作確認</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat data2 | ./map.7 <span class="nv">num</span><span class="o">=</span>1
* Mon Tue Fri
<span class="nv">$ </span>cat data | ./map.7 <span class="nv">num</span><span class="o">=</span>1
* あ い う
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id6">
<h2>12.5. ボディーを出力<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　いよいよ本体の出力です。
ただ、いきなり出力するのではなく、
キーごとにデータを分けることからやっていきましょう。
<tt class="docutils literal"><span class="pre">map.7.hs</span></tt> からリスト8のように <tt class="docutils literal"><span class="pre">map.8.hs</span></tt> を作りました。</p>
<ul class="simple">
<li>リスト8: map.8.hs</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;のheader関数の後ろに追記###
main&#39; (Right num) cs = header num h_axis &gt;&gt; mapM_ print (splitByKey d)
###splitByKey関数を追加###
splitByKey :: [Line] -&gt; [[Line]]
splitByKey [] = []
splitByKey lns@((key,_,_):_) = a : splitByKey b
 where a = takeWhile (\\(k,_,_) -&gt; key == k) lns
 b = dropWhile (\\(k,_,_) -&gt; key == k) lns
</pre></div>
</td></tr></table></div>
<p>　先に実行して結果を見ておきましょう。
リスト9のようにキーごとにレコードが
まとまります。</p>
<ul class="simple">
<li>リスト9: map.8.hsをコンパイルして実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ./data2 | ./map.8 <span class="nv">num</span><span class="o">=</span>1
* Mon Tue Fri
<span class="o">[(</span><span class="s2">&quot;2013&quot;</span>,<span class="s2">&quot;Mon&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;2013&quot;</span>,<span class="s2">&quot;Tue&quot;</span>,<span class="o">[</span><span class="s2">&quot;1&quot;</span><span class="o">])]</span>
<span class="o">[(</span><span class="s2">&quot;2014&quot;</span>,<span class="s2">&quot;Mon&quot;</span>,<span class="o">[</span><span class="s2">&quot;2&quot;</span><span class="o">])</span>,<span class="o">(</span><span class="s2">&quot;2014&quot;</span>,<span class="s2">&quot;Fri&quot;</span>,<span class="o">[</span><span class="s2">&quot;3&quot;</span><span class="o">])]</span>
</pre></div>
</td></tr></table></div>
<p>　さて、リスト8は短いながらもたくさんのことをやっていますし、
新しいモノも登場しています。
まず、2行目の <tt class="docutils literal"><span class="pre">mapM_</span></tt> というへんちくりんな名前の関数ですが、
これは <tt class="docutils literal"><span class="pre">print</span></tt> のようにモナドを出す関数をmapするものです。
リスト10のように、 <tt class="docutils literal"><span class="pre">mapM_</span> <span class="pre">print</span></tt>
でリストのものを一つずつ出力するという意味になります。</p>
<ul class="simple">
<li>リスト10: <tt class="docutils literal"><span class="pre">mapM_</span></tt> の型と <tt class="docutils literal"><span class="pre">mapM_</span> <span class="pre">print</span></tt> の実行例</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM_</span>
<span class="nf">mapM_</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="nb">()</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM_</span> <span class="n">print</span>
<span class="nf">mapM_</span> <span class="n">print</span> <span class="ow">::</span> <span class="kt">Show</span> <span class="n">a</span> <span class="ow">=&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">mapM_</span> <span class="n">print</span> <span class="p">[</span><span class="s">&quot;This&quot;</span><span class="p">,</span><span class="s">&quot;is&quot;</span><span class="p">,</span><span class="s">&quot;a&quot;</span><span class="p">,</span><span class="s">&quot;pen&quot;</span><span class="p">]</span>
<span class="s">&quot;This&quot;</span>
<span class="s">&quot;is&quot;</span>
<span class="s">&quot;a&quot;</span>
<span class="s">&quot;pen&quot;</span>
</pre></div>
</td></tr></table></div>
<p>　さて次に、リスト8の <tt class="docutils literal"><span class="pre">splitByKey</span></tt> 関数の説明を。
これは <tt class="docutils literal"><span class="pre">[List]</span></tt> 型のデータ、
つまり各レコードのリストを入力されると、
キーが同じデータごとにぶった切られて
リストのリストを出します。
6行目の <tt class="docutils literal"><span class="pre">a</span></tt> がキーが同じレコードの塊で、
<tt class="docutils literal"><span class="pre">b</span></tt> が残りのレコードです。
<tt class="docutils literal"><span class="pre">b</span></tt> は再度 <tt class="docutils literal"><span class="pre">splitByKey</span></tt> にぶち込まれてぶった切られます。</p>
<p>　まず目新しいのは6行目の引数にある <tt class="docutils literal"><span class="pre">&#64;</span></tt>
だと思います。これは「アズパターン（as-pattern）」
というもので、要は <tt class="docutils literal"><span class="pre">lns&#64;((key,_,_):_)</span></tt>
と左辺にあれば、右辺では引数を <tt class="docutils literal"><span class="pre">lns</span></tt> として使っても
<tt class="docutils literal"><span class="pre">((key,s,v):_)</span></tt> として使ってもいいよということになります。
<tt class="docutils literal"><span class="pre">lns</span></tt> は7, 8行目の <tt class="docutils literal"><span class="pre">takeWhile,</span> <span class="pre">dropWhile</span></tt> の第二引数として、
<tt class="docutils literal"><span class="pre">key</span></tt> は7, 8行目の無名関数内で使用されています。
<tt class="docutils literal"><span class="pre">lns</span></tt> と <tt class="docutils literal"><span class="pre">key</span></tt> のどっちか一方しか使えないと、
コーディングが少々面倒くさくなるのですが、
実際どう面倒臭くなるかはご自身でお確かめください。
<tt class="docutils literal"><span class="pre">takeWhile,</span> <span class="pre">dropWhile</span></tt> は以前も出てきました。
第一引数の式を第二引数のリストの先頭の要素から適用し、
<tt class="docutils literal"><span class="pre">True</span></tt> を返してくる限り取得した/捨てたリストを返す関数です。</p>
<p>　さて、仕上げにかかりましょう。
リスト11に完成した <tt class="docutils literal"><span class="pre">map.hs</span></tt> の一部を示します。
<tt class="docutils literal"><span class="pre">map.8.hs</span></tt> からの変更部分だけ示しています。
2行目の <tt class="docutils literal"><span class="pre">print</span></tt> 関数が <tt class="docutils literal"><span class="pre">body</span> <span class="pre">h_axis</span></tt>
に置き換わり、 <tt class="docutils literal"><span class="pre">body</span></tt> 関数、 <tt class="docutils literal"><span class="pre">body'</span></tt>
関数が新たに実装されています。</p>
<ul class="simple">
<li>リスト11: 完成した <tt class="docutils literal"><span class="pre">map.hs</span></tt></li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>###main&#39;関数を変更（printをbody h_axisに置き換え）###
main&#39; (Right num) cs = header num h_axis &gt;&gt; mapM_ (body h_axis) (splitByKey d)
###body、body&#39;関数###
body :: [SubKey] -&gt; [Line] -&gt; IO ()
body ss lns@((k,_,_):_) = BS.putStrLn $ BS.unwords (k:(body&#39; ss lns))

body&#39; :: [SubKey] -&gt; [Line] -&gt; [Word]
body&#39; [] _ = []
body&#39; subs [] = replicate (length subs) (BS.pack &quot;0&quot;)
body&#39; (sub:subs) alns@((_,s,(v:_)):lns)
 | sub == s = v : body&#39; subs lns
 | otherwise = BS.pack &quot;0&quot; : body&#39; subs alns
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">body</span></tt> 関数のやっていることは、
出力の各行の先頭にキーをつけることだけです。
キー以降のデータは <tt class="docutils literal"><span class="pre">body'</span></tt> で作っています。
<tt class="docutils literal"><span class="pre">body'</span></tt> がかなりややこしくなっていますが、
サブキーに対応する数字を一つずつリスト化しているだけです。
まず8行目が、サブキーがなくなって <tt class="docutils literal"><span class="pre">body'</span></tt> の再帰を終える処理、
9行目が、サブキーは残っているけど <tt class="docutils literal"><span class="pre">Line</span></tt>
型のレコードがなくなったときの処理で、
ゼロを残ったサブキーの個数分だけリストにして返しています。
11行目は引数の先頭のサブキーと先頭のレコードのサブキーが一致したときに、
レコードの値をリストに追加する処理、
12行目はサブキーが一致しないときにゼロをリストに追加する処理です。
とにかくサブキー1個につき1個データをリストに加えていっているというのを
確かめながら読んでいくと、なんとか理解できるかと思います。</p>
<p>あと、 <tt class="docutils literal"><span class="pre">Line</span></tt> 型 <tt class="docutils literal"><span class="pre">(Key,SubKey,Values)</span></tt> 型では <tt class="docutils literal"><span class="pre">Values</span></tt>
のところが一つの値でなくリストになっており、これもややこしい原因になっています。
実は <tt class="docutils literal"><span class="pre">map</span></tt> コマンドはキー、サブキーに対して値を複数持たせることが
できるのでこのように <tt class="docutils literal"><span class="pre">List</span></tt> 型を定義しました。しかし、
本連載では複数の値があるときの処理は割愛したいと思います。
ということで、一応これで完成ということで、
次回からは別のコマンドを扱いたいと思います。</p>
</div>
<div class="section" id="id7">
<h2>12.6. おわりに<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は愚痴から始まり、 <tt class="docutils literal"><span class="pre">map</span></tt> （の最低限の機能）を
作るところまでを扱いました。
次回は上記のように別のコマンドに話題が移ります。
さてどのコマンドをやりましょうか・・・。
とりあえずもう眠いので寝てから考えることにします
<a class="footnote-reference" href="#id10" id="id8">[2]</a> 。</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id9" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[1]</a></td><td>実はPython版のmapはMon、Fri、Tueの順番で出力してしまいます。
ちょっと手がまわらないのでどなたか助けて・・・。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id10" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[2]</a></td><td>今回、脚注が少ないのはきっとクリスマスのスカラー電磁波の仕業です。</td></tr>
</tbody>
</table>
</div>
</div>

