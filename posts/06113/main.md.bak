# USP Magazine 2015年1月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>10. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p><br />
<blockquote><br />
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア<br />
状態なので，連載しながら開発しようと思い立った上田は，<br />
不幸にも黒塗りの高級車に追突してしまう．後輩をかばい<br />
すべての責任を負った上田に対し，車の主，暴力団員谷岡に<br />
言い渡された示談の条件とは...．</div></blockquote><br />
<div class="section" id="id1"><br />
<h2>10.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　 <a class="footnote-reference" href="#aa1" id="id2">[1]</a> <a class="footnote-reference" href="#aa2" id="id3">[2]</a> <a class="footnote-reference" href="#aa3" id="id4">[3]</a> ．富山の産んだ，<br />
知の阪神 <a class="footnote-reference" href="#aa4" id="id5">[4]</a> ブラックエンジェル上田です．<br />
前回までシェル芸勉強会の問題をHaskellで解いて自己満足していた本連載ですが，<br />
マンネリ化していたので，年が変わって1月号に入ってしまったのをいいことに，<br />
編集部に無断で新しいことをやりたいと思います <a class="footnote-reference" href="#aa5" id="id6">[5]</a> ．</p><br />
<p>　んで，やることは冒頭で谷岡に言い渡されたように，<br />
Open usp TukubaiのHaskell版 <a class="footnote-reference" href="#aa6" id="id7">[6]</a><br />
を完成させる．つまりHaskellでコマンドを作る<br />
ということです．Haskell版はわてくしが趣味でコツコツ作っていたのですが，<br />
現在，非常に中途半端（半分くらい作って止まっている）な状態です．<br />
こいつを連載のついでに進めたい，<br />
という個人的一粒で二度美味しい感じでやってこうと思います．</p><br />
<p>　サンプルコードを含んだブランチを</p><br />
<blockquote><br />
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote><br />
<p>に用意しておきますので，参考にしながら<br />
Haskellを勉強してみてください．<br />
コマンド作りということで，<br />
内容も一段と実戦的になります．</p><br />
</div><br />
<div class="section" id="map"><br />
<h2>10.2. mapを作る<a class="headerlink" href="#map" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　ということでハエある最初の未実装コマンドには，<br />
<tt class="docutils literal"><span class="pre">map</span></tt> を選びました．<br />
<tt class="docutils literal"><span class="pre">map</span></tt> はクロス集計の表を作るコマンドで，<br />
基本的には図1のような挙動を示します．<br />
<tt class="docutils literal"><span class="pre">num=2</span></tt> というのは左から2列をキー扱いするという意味で，<br />
<tt class="docutils literal"><span class="pre">map</span></tt> の出力を見るとキーが縦軸，<br />
キーの隣のフィールド（AとかBとか書いてある列）<br />
が横軸になってデータが出力されています．<br />
これ，awkでやろうとすると結構面倒なので，<br />
無いと困るコマンドなのですがまだHaskell版では未実装です．<br />
残念無念．切腹．<br />
いや，切腹はやめて実装することにします．</p><br />
<ul class="simple"><br />
<li>図1: mapの挙動</li><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:~ ueda<span class="nv">$ </span>cat data<br />
001 鎌田 A 1<br />
001 鎌田 B 2<br />
002 濱田 A 3<br />
002 濱田 B 4<br />
003 上田 B 1<br />
uedambp:~ ueda<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>2 data<br />
* * A B<br />
001 鎌田 1 2<br />
002 濱田 3 4<br />
003 上田 0 1<br />
<span class="c">###ketaコマンドで整形###</span><br />
uedambp:~ ueda<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>2 data | keta<br />
 * * A B<br />
001 鎌田 1 2<br />
002 濱田 3 4<br />
003 上田 0 1<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>10.3. まずファイルを読み込めるようにする<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　コマンドを作るときは，まず <tt class="docutils literal"><span class="pre">cat(1)</span></tt> コマンドに相当する<br />
部分から書いていきます．<br />
書いて行くというよりは，どこかからコピーしていきます．<br />
コピーするならライブラリにまとめればいいじゃんという<br />
意見もあると思いますが，コマンドは1個のファイルを<br />
コンパイルしたら使えるというのが理想なので，<br />
コピーで済ませます．</p><br />
<p>　そこまで書いたものを図2に示します．<br />
実行してみると図3のような出力になります．</p><br />
<ul class="simple"><br />
<li>図2: ファイルをcatするmap.1.hs</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span><br />
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span><br />
<br />
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span><br />
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span><br />
<br />
<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span><br />
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span><br />
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span><br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>図3: map.1の出力</li><br />
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###コンパイル###</span><br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>ghc -O2 map.1.hs<br />
<span class="o">[</span>1 of 1<span class="o">]</span> Compiling Main <span class="o">(</span> map.1.hs, map.1.o <span class="o">)</span><br />
Linking map.1 ...<br />
<span class="c">###元のデータ###</span><br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data<br />
001 鎌田 A 1<br />
001 鎌田 B 2<br />
002 濱田 A 3<br />
002 濱田 B 4<br />
003 上田 B 1<br />
<span class="c">###ファイル名を指定###</span><br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.1 <span class="nv">num</span><span class="o">=</span>1 ~/data<br />
001 鎌田 A 1<br />
001 鎌田 B 2<br />
002 濱田 A 3<br />
002 濱田 B 4<br />
003 上田 B 1<br />
<span class="c">###パイプを使う（その1）###</span><br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.1 <span class="nv">num</span><span class="o">=</span>1<br />
（出力略）<br />
<span class="c">###パイプを使う（その2）###</span><br />
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.1 <span class="nv">num</span><span class="o">=</span>1 -<br />
（出力略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて，図2の解説をしていきます．<br />
シェル芸のときの解説と違っていきなり結構難しいですが，<br />
落ち着いて読んでいきましょう．<br />
まず，10行目からの <tt class="docutils literal"><span class="pre">readF</span></tt> 関数ですが，<br />
これはファイルあるいは標準入力を読んで別の関数に渡す関数です．<br />
パターンマッチを使っており，<br />
11, 12行目はそれぞれ標準入力，ファイルから読む場合に対応しています．</p><br />
<p>　ファイルから読み込んだ文字列は，String型ではなく，<br />
これまでも使ってきたByteString型として読み込みます．<br />
これまでのシェル芸ならともかく，<br />
コマンドだとスピードが求められ，<br />
そうなるとString型では手に負えなくなります．<br />
読み込むモジュールは2行目のように<br />
<tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> を選びます．</p><br />
<p>　10行目を見ると分かるように，<br />
<tt class="docutils literal"><span class="pre">readF</span></tt> 関数の出力は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">BS.ByteString</span></tt> となります．<br />
<tt class="docutils literal"><span class="pre">BS.ByteString</span></tt> なら分かりやすいのですが，<br />
ファイルから読み込んでいるので頭に <tt class="docutils literal"><span class="pre">IO</span></tt> がくっつきます．</p><br />
<p>　11, 12行目で使っている関数の型を一応，図4に示しておきます．<br />
<tt class="docutils literal"><span class="pre">readFile</span></tt> の引数にはこれまで連載中に何回も出て来た<br />
<tt class="docutils literal"><span class="pre">FilePath</span></tt> という型が出て来ますが，<br />
この図のように <tt class="docutils literal"><span class="pre">:i</span></tt> で型の情報を調べることができます．<br />
これを見ると， String型の別名であることが分かります．</p><br />
<ul class="simple"><br />
<li>図4: getContentsとreadFileの型とFilePathの正体</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:USPMAG ueda$ ghci<br />
（略）<br />
Prelude&gt; import Data.ByteString.Lazy.Char8 as BS<br />
Prelude BS&gt; :t BS.getContents<br />
BS.getContents :: IO ByteString<br />
Prelude BS&gt; :t BS.readFile<br />
BS.readFile :: FilePath -&gt; IO ByteString<br />
Prelude BS&gt; :i FilePath<br />
type FilePath = String -- Defined in `GHC.IO&#39;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて， <tt class="docutils literal"><span class="pre">readF</span></tt> が分かったところで <a class="footnote-reference" href="#aa7" id="id9">[7]</a> ，<br />
次に <tt class="docutils literal"><span class="pre">main</span></tt> 関数に移りましょう．<br />
まず5行目の左辺の <tt class="docutils literal"><span class="pre">getArgs</span></tt> の説明をします．<br />
この関数は引数を読み込むためにあります．<br />
図5に型を示しますが，出力がString型のリストに<br />
IOをくっつけたものであることが分かります．<br />
5行目では，このリストに<br />
<tt class="docutils literal"><span class="pre">&lt;-</span></tt> で <tt class="docutils literal"><span class="pre">args</span></tt> という名前を付けています．<br />
で， <tt class="docutils literal"><span class="pre">main</span></tt> 関数は2014年9月号でも出て来た <tt class="docutils literal"><span class="pre">do</span></tt><br />
で書かれているので，<br />
普通の手続き型の言語のように次行に処理の流れが進みます．</p><br />
<ul class="simple"><br />
<li>図5: getArgsの型</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="nn">System.Environment</span><br />
<span class="kt">Prelude</span> <span class="kt">System</span><span class="o">.</span><span class="kt">Environment</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">getArgs</span><br />
<span class="nf">getArgs</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　6行目では本連載で始めてとなる「case式」<br />
が出てきました．「case文」ではなく「case式」です.<br />
case式では分岐の基準となるもの（ここではargs）<br />
のパターンを書いていき，場合分けを表現します．<br />
パターンは <tt class="docutils literal"><span class="pre">-&gt;</span></tt> の左側，パターンにマッチした時の処理は右側に書きます．<br />
7行目は <tt class="docutils literal"><span class="pre">args</span></tt> ，つまり引数が一つであるとき（例: <tt class="docutils literal"><span class="pre">map</span> <span class="pre">num=1</span></tt> ）<br />
のようなときに適合します．<br />
8行目はファイル名の指定があるときに適合します．<br />
この場合分けと， <tt class="docutils literal"><span class="pre">readF</span></tt> 関数のパターンマッチによって，<br />
ファイル名が指定されたとき，指定されなかったとき，<br />
ファイル名の代わりに「 <tt class="docutils literal"><span class="pre">-</span></tt> 」が指定されたときで，<br />
読み込む先がファイル名になったり標準入力になったりと，<br />
適切な挙動が実現されます．</p><br />
<p>　引数がそれ以外のパターンの場合は，この例では次のように<br />
エラーとなります．</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.1 hoge hoge hoge<br />
map.1: map.1.hs:<span class="o">(</span>6,11<span class="o">)</span>-<span class="o">(</span>8,52<span class="o">)</span>: Non-exhaustive patterns in <span class="k">case</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="usage"><br />
<h2>10.4. usageをつける<a class="headerlink" href="#usage" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次に，コマンドの使い方を説明するusageをつけます．usageは，<br />
引数のパターンにマッチしなかったときに表示することにしましょう．<br />
図6のようにヘルプを付け加えました．<br />
ヘルプを出す関数が <tt class="docutils literal"><span class="pre">showUsage</span></tt> で，<br />
それを <tt class="docutils literal"><span class="pre">main</span></tt> 関数のcase式で<br />
パターンにマッチするときに呼び出しています．<br />
パターンの一番下，18行目の <tt class="docutils literal"><span class="pre">_</span></tt> は，上のパターンが全て<br />
マッチしなかったときにマッチする記号です．</p><br />
<ul class="simple"><br />
<li>図6: map.2.hs</li><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span><br />
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span><br />
<span class="kr">import</span> <span class="nn">System.IO</span><br />
<br />
<span class="nf">showUsage</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">showUsage</span> <span class="ow">=</span> <span class="kr">do</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span><br />
 <span class="s">&quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; </span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span><br />
 <span class="s">&quot;Thu Oct 23 08:52:44 JST 2014</span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span><br />
 <span class="s">&quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span><br />
<br />
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span><br />
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span><br />
 <span class="p">[</span><span class="s">&quot;-h&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
 <span class="p">[</span><span class="s">&quot;--help&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span><br />
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span><br />
 <span class="kr">_</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span><br />
<br />
<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span><br />
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span><br />
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　標準エラー出力に何かを出力するときには，<br />
6行目のように <tt class="docutils literal"><span class="pre">System.IO.hPutStr</span></tt> を使います．<br />
この関数を使用するために，3行目で <tt class="docutils literal"><span class="pre">System.IO</span></tt><br />
をインポートしました．<br />
型を見ると次のようになっており，<br />
<tt class="docutils literal"><span class="pre">GHC.IO.Handle.Types.Handle</span></tt> に出力先<br />
（ <tt class="docutils literal"><span class="pre">map.2.hs</span></tt> の場合は <tt class="docutils literal"><span class="pre">stderr</span></tt> ）<br />
を指定し，その後に出したい文字列をString型で指定します．</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span><br />
<span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="ow">::</span> <span class="kt">GHC</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="kt">Handle</span><span class="o">.</span><span class="kt">Types</span><span class="o">.</span><span class="kt">Handle</span> <span class="ow">-&gt;</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">map.2.hs</span></tt> でちゃんと出力されるか確認しておきましょう．<br />
図7のように出たらOKです．</p><br />
<ul class="simple"><br />
<li>図7: map.2.hsの動作確認</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda$ ghc -O2 map.2.hs<br />
[1 of 1] Compiling Main ( map.2.hs, map.2.o )<br />
Linking map.2 ...<br />
uedambp:COMMANDS.HS ueda$ ./map.2<br />
Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt;<br />
Thu Oct 23 08:52:44 JST 2014<br />
Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.<br />
uedambp:COMMANDS.HS ueda$ ./map.2 -h<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>10.5. 終了ステータスの指定<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて，これで今号は最後にしておきますが，<br />
usageを表示したら終了ステータス1を返すようにしておきましょう．<br />
コマンドは，終了ステータスで呼び出し元に処理がうまくいったか<br />
どうかを返すわけですが，usageを出すのは<br />
そのコマンドの本職の処理ではないので，異常を示す1を返します．</p><br />
<p>　図8に終了ステータスの処理を加えた <tt class="docutils literal"><span class="pre">map.3.hs</span></tt><br />
と，その動作を示します．加えたと言っても，4行目に<br />
<tt class="docutils literal"><span class="pre">System.Exit</span></tt> というモジュール，<br />
11行目に <tt class="docutils literal"><span class="pre">exitWith</span></tt> という関数を加えただけです．</p><br />
<ul class="simple"><br />
<li>図8: map.3.hsのコードと動作確認</li><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre>import System.Environment<br />
import Data.ByteString.Lazy.Char8 as BS<br />
import System.IO<br />
import System.Exit<br />
<br />
showUsage :: IO ()<br />
showUsage = do System.IO.hPutStr stderr (<br />
 &quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; \\n&quot; ++<br />
 &quot;Thu Oct 23 08:52:44 JST 2014\\n&quot; ++<br />
 &quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.\\n&quot;)<br />
 exitWith (ExitFailure 1)<br />
（以下略）<br />
uedambp:COMMANDS.HS ueda$ ghc -O2 map.3.hs<br />
[1 of 1] Compiling Main ( map.3.hs, map.3.o )<br />
Linking map.3 ...<br />
uedambp:COMMANDS.HS ueda$ ./map.3<br />
Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt;<br />
Thu Oct 23 08:52:44 JST 2014<br />
Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.<br />
###終了ステータスの確認###<br />
uedambp:COMMANDS.HS ueda$ echo $?<br />
1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">exitWith</span></tt> の型は次の通り．Int型を引数にとるわけではないので，<br />
<tt class="docutils literal"><span class="pre">ExitFailure</span></tt> というデータコンストラクタを使っています．<br />
面倒ですが，型のためには面倒を厭わないのがHaskellerというものです<br />
<a class="footnote-reference" href="#aa8" id="id11">[8]</a> ．</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">System</span><span class="o">.</span><span class="kt">Exit</span><span class="o">.</span><span class="n">exitWith</span><br />
<span class="kt">System</span><span class="o">.</span><span class="kt">Exit</span><span class="o">.</span><span class="n">exitWith</span> <span class="ow">::</span> <span class="kt">GHC</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="kt">Exception</span><span class="o">.</span><span class="kt">ExitCode</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="n">a</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id12"><br />
<h2>10.6. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はHaskell版のOpen usp Tukubaiを作るにあたっての<br />
基礎の部分である，ファイルの読み込み，引数の読み込み，<br />
usageの表示，終了ステータスの操作を扱いました．<br />
次号から，mapの処理を書いて行きましょう．</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="aa1" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>こん</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa2" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>に</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa3" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>ちわ</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa4" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id5">[4]</a></td><td>編集部注: 「知の巨人」にかけているらしいです．</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa5" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id6">[5]</a></td><td>編集部御中，自由すぎてすんません．</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa6" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id7">[6]</a></td><td><a class="reference external" href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS">https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS</a></td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa7" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id9">[7]</a></td><td>うーん．どうなんでしょう？どれだけの人がついてきているかどうかは，実際にはよく分からなかったり．&#64;ryuichiuedaで公開でどんな感じかお伝えしていただければ，と．</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="aa8" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id11">[8]</a></td><td>いや・・・面倒です．</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div>
