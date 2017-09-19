---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2015年1月号「Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？」
<h1>10. Haskell版Open usp Tukubai完成させるぞ企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskellopen-usp-tukubai-haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>Open usp TukubaiのHaskell版がまるでサグラダ・ファミリア
状態なので，連載しながら開発しようと思い立った上田は，
不幸にも黒塗りの高級車に追突してしまう．後輩をかばい
すべての責任を負った上田に対し，車の主，暴力団員谷岡に
言い渡された示談の条件とは...．</div></blockquote>
<div class="section" id="id1">
<h2>10.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　 <a class="footnote-reference" href="#aa1" id="id2">[1]</a> <a class="footnote-reference" href="#aa2" id="id3">[2]</a> <a class="footnote-reference" href="#aa3" id="id4">[3]</a> ．富山の産んだ，
知の阪神 <a class="footnote-reference" href="#aa4" id="id5">[4]</a> ブラックエンジェル上田です．
前回までシェル芸勉強会の問題をHaskellで解いて自己満足していた本連載ですが，
マンネリ化していたので，年が変わって1月号に入ってしまったのをいいことに，
編集部に無断で新しいことをやりたいと思います <a class="footnote-reference" href="#aa5" id="id6">[5]</a> ．</p>
<p>　んで，やることは冒頭で谷岡に言い渡されたように，
Open usp TukubaiのHaskell版 <a class="footnote-reference" href="#aa6" id="id7">[6]</a>
を完成させる．つまりHaskellでコマンドを作る
ということです．Haskell版はわてくしが趣味でコツコツ作っていたのですが，
現在，非常に中途半端（半分くらい作って止まっている）な状態です．
こいつを連載のついでに進めたい，
という個人的一粒で二度美味しい感じでやってこうと思います．</p>
<p>　サンプルコードを含んだブランチを</p>
<blockquote>
<div><a class="reference external" href="https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag">https://github.com/ryuichiueda/Open-usp-Tukubai/tree/uspmag</a></div></blockquote>
<p>に用意しておきますので，参考にしながら
Haskellを勉強してみてください．
コマンド作りということで，
内容も一段と実戦的になります．</p>
</div>
<div class="section" id="map">
<h2>10.2. mapを作る<a class="headerlink" href="#map" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　ということでハエある最初の未実装コマンドには，
<tt class="docutils literal"><span class="pre">map</span></tt> を選びました．
<tt class="docutils literal"><span class="pre">map</span></tt> はクロス集計の表を作るコマンドで，
基本的には図1のような挙動を示します．
<tt class="docutils literal"><span class="pre">num=2</span></tt> というのは左から2列をキー扱いするという意味で，
<tt class="docutils literal"><span class="pre">map</span></tt> の出力を見るとキーが縦軸，
キーの隣のフィールド（AとかBとか書いてある列）
が横軸になってデータが出力されています．
これ，awkでやろうとすると結構面倒なので，
無いと困るコマンドなのですがまだHaskell版では未実装です．
残念無念．切腹．
いや，切腹はやめて実装することにします．</p>
<ul class="simple">
<li>図1: mapの挙動</li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:~ ueda<span class="nv">$ </span>cat data
001 鎌田 A 1
001 鎌田 B 2
002 濱田 A 3
002 濱田 B 4
003 上田 B 1
uedambp:~ ueda<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>2 data
* * A B
001 鎌田 1 2
002 濱田 3 4
003 上田 0 1
<span class="c">###ketaコマンドで整形###</span>
uedambp:~ ueda<span class="nv">$ </span>map <span class="nv">num</span><span class="o">=</span>2 data | keta
 * * A B
001 鎌田 1 2
002 濱田 3 4
003 上田 0 1
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h2>10.3. まずファイルを読み込めるようにする<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　コマンドを作るときは，まず <tt class="docutils literal"><span class="pre">cat(1)</span></tt> コマンドに相当する
部分から書いていきます．
書いて行くというよりは，どこかからコピーしていきます．
コピーするならライブラリにまとめればいいじゃんという
意見もあると思いますが，コマンドは1個のファイルを
コンパイルしたら使えるというのが理想なので，
コピーで済ませます．</p>
<p>　そこまで書いたものを図2に示します．
実行してみると図3のような出力になります．</p>
<ul class="simple">
<li>図2: ファイルをcatするmap.1.hs</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span>
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span>

<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span>
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span>
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span>
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span>

<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span>
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span>
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span>
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>図3: map.1の出力</li>
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###コンパイル###</span>
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>ghc -O2 map.1.hs
<span class="o">[</span>1 of 1<span class="o">]</span> Compiling Main <span class="o">(</span> map.1.hs, map.1.o <span class="o">)</span>
Linking map.1 ...
<span class="c">###元のデータ###</span>
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data
001 鎌田 A 1
001 鎌田 B 2
002 濱田 A 3
002 濱田 B 4
003 上田 B 1
<span class="c">###ファイル名を指定###</span>
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.1 <span class="nv">num</span><span class="o">=</span>1 ~/data
001 鎌田 A 1
001 鎌田 B 2
002 濱田 A 3
002 濱田 B 4
003 上田 B 1
<span class="c">###パイプを使う（その1）###</span>
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.1 <span class="nv">num</span><span class="o">=</span>1
（出力略）
<span class="c">###パイプを使う（その2）###</span>
uedambp:COMMANDS.HS ueda<span class="nv">$ </span>cat ~/data | ./map.1 <span class="nv">num</span><span class="o">=</span>1 -
（出力略）
</pre></div>
</td></tr></table></div>
<p>　さて，図2の解説をしていきます．
シェル芸のときの解説と違っていきなり結構難しいですが，
落ち着いて読んでいきましょう．
まず，10行目からの <tt class="docutils literal"><span class="pre">readF</span></tt> 関数ですが，
これはファイルあるいは標準入力を読んで別の関数に渡す関数です．
パターンマッチを使っており，
11, 12行目はそれぞれ標準入力，ファイルから読む場合に対応しています．</p>
<p>　ファイルから読み込んだ文字列は，String型ではなく，
これまでも使ってきたByteString型として読み込みます．
これまでのシェル芸ならともかく，
コマンドだとスピードが求められ，
そうなるとString型では手に負えなくなります．
読み込むモジュールは2行目のように
<tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> を選びます．</p>
<p>　10行目を見ると分かるように，
<tt class="docutils literal"><span class="pre">readF</span></tt> 関数の出力は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">BS.ByteString</span></tt> となります．
<tt class="docutils literal"><span class="pre">BS.ByteString</span></tt> なら分かりやすいのですが，
ファイルから読み込んでいるので頭に <tt class="docutils literal"><span class="pre">IO</span></tt> がくっつきます．</p>
<p>　11, 12行目で使っている関数の型を一応，図4に示しておきます．
<tt class="docutils literal"><span class="pre">readFile</span></tt> の引数にはこれまで連載中に何回も出て来た
<tt class="docutils literal"><span class="pre">FilePath</span></tt> という型が出て来ますが，
この図のように <tt class="docutils literal"><span class="pre">:i</span></tt> で型の情報を調べることができます．
これを見ると， String型の別名であることが分かります．</p>
<ul class="simple">
<li>図4: getContentsとreadFileの型とFilePathの正体</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:USPMAG ueda$ ghci
（略）
Prelude&gt; import Data.ByteString.Lazy.Char8 as BS
Prelude BS&gt; :t BS.getContents
BS.getContents :: IO ByteString
Prelude BS&gt; :t BS.readFile
BS.readFile :: FilePath -&gt; IO ByteString
Prelude BS&gt; :i FilePath
type FilePath = String -- Defined in `GHC.IO&#39;
</pre></div>
</td></tr></table></div>
<p>　さて， <tt class="docutils literal"><span class="pre">readF</span></tt> が分かったところで <a class="footnote-reference" href="#aa7" id="id9">[7]</a> ，
次に <tt class="docutils literal"><span class="pre">main</span></tt> 関数に移りましょう．
まず5行目の左辺の <tt class="docutils literal"><span class="pre">getArgs</span></tt> の説明をします．
この関数は引数を読み込むためにあります．
図5に型を示しますが，出力がString型のリストに
IOをくっつけたものであることが分かります．
5行目では，このリストに
<tt class="docutils literal"><span class="pre">&lt;-</span></tt> で <tt class="docutils literal"><span class="pre">args</span></tt> という名前を付けています．
で， <tt class="docutils literal"><span class="pre">main</span></tt> 関数は2014年9月号でも出て来た <tt class="docutils literal"><span class="pre">do</span></tt>
で書かれているので，
普通の手続き型の言語のように次行に処理の流れが進みます．</p>
<ul class="simple">
<li>図5: getArgsの型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="nn">System.Environment</span>
<span class="kt">Prelude</span> <span class="kt">System</span><span class="o">.</span><span class="kt">Environment</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">getArgs</span>
<span class="nf">getArgs</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>　6行目では本連載で始めてとなる「case式」
が出てきました．「case文」ではなく「case式」です.
case式では分岐の基準となるもの（ここではargs）
のパターンを書いていき，場合分けを表現します．
パターンは <tt class="docutils literal"><span class="pre">-&gt;</span></tt> の左側，パターンにマッチした時の処理は右側に書きます．
7行目は <tt class="docutils literal"><span class="pre">args</span></tt> ，つまり引数が一つであるとき（例: <tt class="docutils literal"><span class="pre">map</span> <span class="pre">num=1</span></tt> ）
のようなときに適合します．
8行目はファイル名の指定があるときに適合します．
この場合分けと， <tt class="docutils literal"><span class="pre">readF</span></tt> 関数のパターンマッチによって，
ファイル名が指定されたとき，指定されなかったとき，
ファイル名の代わりに「 <tt class="docutils literal"><span class="pre">-</span></tt> 」が指定されたときで，
読み込む先がファイル名になったり標準入力になったりと，
適切な挙動が実現されます．</p>
<p>　引数がそれ以外のパターンの場合は，この例では次のように
エラーとなります．</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda<span class="nv">$ </span>./map.1 hoge hoge hoge
map.1: map.1.hs:<span class="o">(</span>6,11<span class="o">)</span>-<span class="o">(</span>8,52<span class="o">)</span>: Non-exhaustive patterns in <span class="k">case</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="usage">
<h2>10.4. usageをつける<a class="headerlink" href="#usage" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次に，コマンドの使い方を説明するusageをつけます．usageは，
引数のパターンにマッチしなかったときに表示することにしましょう．
図6のようにヘルプを付け加えました．
ヘルプを出す関数が <tt class="docutils literal"><span class="pre">showUsage</span></tt> で，
それを <tt class="docutils literal"><span class="pre">main</span></tt> 関数のcase式で
パターンにマッチするときに呼び出しています．
パターンの一番下，18行目の <tt class="docutils literal"><span class="pre">_</span></tt> は，上のパターンが全て
マッチしなかったときにマッチする記号です．</p>
<ul class="simple">
<li>図6: map.2.hs</li>
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="kr">import</span> <span class="nn">System.Environment</span>
<span class="kr">import</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">BS</span>
<span class="kr">import</span> <span class="nn">System.IO</span>

<span class="nf">showUsage</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">showUsage</span> <span class="ow">=</span> <span class="kr">do</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="n">stderr</span> <span class="p">(</span>
 <span class="s">&quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; </span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span>
 <span class="s">&quot;Thu Oct 23 08:52:44 JST 2014</span><span class="se">\\n</span><span class="s">&quot;</span> <span class="o">++</span>
 <span class="s">&quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.</span><span class="se">\\n</span><span class="s">&quot;</span><span class="p">)</span>

<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">args</span> <span class="ow">&lt;-</span> <span class="n">getArgs</span>
 <span class="kr">case</span> <span class="n">args</span> <span class="kr">of</span>
 <span class="p">[</span><span class="s">&quot;-h&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>
 <span class="p">[</span><span class="s">&quot;--help&quot;</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>
 <span class="p">[</span><span class="n">num</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="s">&quot;-&quot;</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span>
 <span class="p">[</span><span class="n">num</span><span class="p">,</span><span class="n">file</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">readF</span> <span class="n">file</span> <span class="o">&gt;&gt;=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">putStr</span>
 <span class="kr">_</span> <span class="ow">-&gt;</span> <span class="n">showUsage</span>

<span class="nf">readF</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">BS</span><span class="o">.</span><span class="kt">ByteString</span>
<span class="nf">readF</span> <span class="s">&quot;-&quot;</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">getContents</span>
<span class="nf">readF</span> <span class="n">f</span> <span class="ow">=</span> <span class="kt">BS</span><span class="o">.</span><span class="n">readFile</span> <span class="n">f</span>
</pre></div>
</td></tr></table></div>
<p>　標準エラー出力に何かを出力するときには，
6行目のように <tt class="docutils literal"><span class="pre">System.IO.hPutStr</span></tt> を使います．
この関数を使用するために，3行目で <tt class="docutils literal"><span class="pre">System.IO</span></tt>
をインポートしました．
型を見ると次のようになっており，
<tt class="docutils literal"><span class="pre">GHC.IO.Handle.Types.Handle</span></tt> に出力先
（ <tt class="docutils literal"><span class="pre">map.2.hs</span></tt> の場合は <tt class="docutils literal"><span class="pre">stderr</span></tt> ）
を指定し，その後に出したい文字列をString型で指定します．</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span>
<span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="n">hPutStr</span> <span class="ow">::</span> <span class="kt">GHC</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="kt">Handle</span><span class="o">.</span><span class="kt">Types</span><span class="o">.</span><span class="kt">Handle</span> <span class="ow">-&gt;</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span>
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">map.2.hs</span></tt> でちゃんと出力されるか確認しておきましょう．
図7のように出たらOKです．</p>
<ul class="simple">
<li>図7: map.2.hsの動作確認</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:COMMANDS.HS ueda$ ghc -O2 map.2.hs
[1 of 1] Compiling Main ( map.2.hs, map.2.o )
Linking map.2 ...
uedambp:COMMANDS.HS ueda$ ./map.2
Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt;
Thu Oct 23 08:52:44 JST 2014
Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.
uedambp:COMMANDS.HS ueda$ ./map.2 -h
（略）
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>10.5. 終了ステータスの指定<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて，これで今号は最後にしておきますが，
usageを表示したら終了ステータス1を返すようにしておきましょう．
コマンドは，終了ステータスで呼び出し元に処理がうまくいったか
どうかを返すわけですが，usageを出すのは
そのコマンドの本職の処理ではないので，異常を示す1を返します．</p>
<p>　図8に終了ステータスの処理を加えた <tt class="docutils literal"><span class="pre">map.3.hs</span></tt>
と，その動作を示します．加えたと言っても，4行目に
<tt class="docutils literal"><span class="pre">System.Exit</span></tt> というモジュール，
11行目に <tt class="docutils literal"><span class="pre">exitWith</span></tt> という関数を加えただけです．</p>
<ul class="simple">
<li>図8: map.3.hsのコードと動作確認</li>
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
22</pre></div></td><td class="code"><div class="highlight"><pre>import System.Environment
import Data.ByteString.Lazy.Char8 as BS
import System.IO
import System.Exit

showUsage :: IO ()
showUsage = do System.IO.hPutStr stderr (
 &quot;Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt; \\n&quot; ++
 &quot;Thu Oct 23 08:52:44 JST 2014\\n&quot; ++
 &quot;Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.\\n&quot;)
 exitWith (ExitFailure 1)
（以下略）
uedambp:COMMANDS.HS ueda$ ghc -O2 map.3.hs
[1 of 1] Compiling Main ( map.3.hs, map.3.o )
Linking map.3 ...
uedambp:COMMANDS.HS ueda$ ./map.3
Usage : map &lt;num=&lt;n&gt;&gt; &lt;file&gt;
Thu Oct 23 08:52:44 JST 2014
Open usp Tukubai (LINUX+FREEBSD+Mac), Haskell ver.
###終了ステータスの確認###
uedambp:COMMANDS.HS ueda$ echo $?
1
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">exitWith</span></tt> の型は次の通り．Int型を引数にとるわけではないので，
<tt class="docutils literal"><span class="pre">ExitFailure</span></tt> というデータコンストラクタを使っています．
面倒ですが，型のためには面倒を厭わないのがHaskellerというものです
<a class="footnote-reference" href="#aa8" id="id11">[8]</a> ．</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">System</span><span class="o">.</span><span class="kt">Exit</span><span class="o">.</span><span class="n">exitWith</span>
<span class="kt">System</span><span class="o">.</span><span class="kt">Exit</span><span class="o">.</span><span class="n">exitWith</span> <span class="ow">::</span> <span class="kt">GHC</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="kt">Exception</span><span class="o">.</span><span class="kt">ExitCode</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="n">a</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id12">
<h2>10.6. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はHaskell版のOpen usp Tukubaiを作るにあたっての
基礎の部分である，ファイルの読み込み，引数の読み込み，
usageの表示，終了ステータスの操作を扱いました．
次号から，mapの処理を書いて行きましょう．</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="aa1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>こん</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa2" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td>に</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa3" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id4">[3]</a></td><td>ちわ</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa4" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id5">[4]</a></td><td>編集部注: 「知の巨人」にかけているらしいです．</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa5" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[5]</a></td><td>編集部御中，自由すぎてすんません．</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa6" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[6]</a></td><td><a class="reference external" href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS">https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS</a></td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa7" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id9">[7]</a></td><td>うーん．どうなんでしょう？どれだけの人がついてきているかどうかは，実際にはよく分からなかったり．&#64;ryuichiuedaで公開でどんな感じかお伝えしていただければ，と．</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="aa8" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[8]</a></td><td>いや・・・面倒です．</td></tr>
</tbody>
</table>
</div>
</div>
