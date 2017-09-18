---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年9月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>6. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>産業技術大学院・USP研究所・USP友の会　上田隆一<br />
<a class="footnote-reference" href="#id12" id="id1">[2]</a></p><br />
<blockquote><br />
<div>USP友の会のシェル芸勉強会<br />
（脚注：シェルのワンライナー勉強会）は、<br />
日々、他の言語からの他流試合に晒されているのである。<br />
そこで上田は、Haskellで自ら他流試合を行い、<br />
さらにシェル芸勉強会をいじめる自傷行為に手を<br />
染めるのであった。</div></blockquote><br />
<div class="section" id="id2"><br />
<h2>6.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　こんにちは。本も出たことだしもうちょっと<br />
大人にならなければならないような気がしないでもない上田です。<br />
<a class="footnote-reference" href="#id11" id="id3">[1]</a></p><br />
<p>　大学にいるとしょっちゅう高専生と間違われます。<br />
間違われるのは楽しいんだけどたまに横柄な扱いを受けます。<br />
私はいつもそんな目にあっているので、<br />
若い人をちゃんと敬う気持ちが欲しいなと日頃、思っております。<br />
自分の子供を見ていると分かりますが、<br />
若い世代の方が効率的に勉強してますしね。<br />
私のような年寄りは早くホロン部した方がよいような気がします。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>6.2. 今回の問題<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、いつになく真面目に<br />
<a class="footnote-reference" href="#id13" id="id5">[3]</a><br />
スタートしましたが、<br />
今回は第1回シェル芸勉強会の3問目の途中からです。<br />
<a class="footnote-reference" href="#id14" id="id6">[4]</a></p><br />
<blockquote><br />
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト<br />
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）<br />
について以下の操作をしてください。</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li><br />
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li><br />
</ul><br />
</div></blockquote><br />
<p>前回は、リスト1のように <tt class="docutils literal"><span class="pre">/etc</span></tt> 直下のファイルを列挙するところまで来ていました。</p><br />
<ul class="simple"><br />
<li>リスト1: ファイルのリストを作るプログラムと実行結果</li><br />
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
20</pre></div></td><td class="code"><div class="highlight"><pre>###こんなコード###<br />
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_2.hs<br />
import System.Directory<br />
<br />
main = ls &quot;/etc/&quot; &gt;&gt;= putStr . unlines<br />
<br />
ls :: String -&gt; IO [FilePath]<br />
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])<br />
###実行!!###<br />
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ ./q1_3_2 | head<br />
insserv<br />
blkid.tab<br />
tidy.conf<br />
logrotate.conf<br />
avserver.conf<br />
gshadow-<br />
iproute2<br />
localtime<br />
systemd<br />
dhcp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　「 <tt class="docutils literal"><span class="pre">/etc</span></tt> 下」というのは子のディレクトリ、孫のディレクトリ・・・<br />
と下のディレクトリのファイルも全部含むつもりで出題しました。<br />
ですので、再帰的にディレクトリを降りて行く処理の実装が必要になります。</p><br />
</div><br />
<div class="section" id="id7"><br />
<h2>6.3. パスを作る<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はまず、 <tt class="docutils literal"><span class="pre">q1_3_2</span></tt> の出力の頭に <tt class="docutils literal"><span class="pre">/etc/</span></tt><br />
をくっつけるところから始めましょう。<br />
このままだと、再帰的にディレクトリを降りてファイルのリストを作って行くとき、<br />
どのディレクトリのファイルか分からなくなってしまいます。<br />
リスト2のようにプログラムを書きかえます。</p><br />
<ul class="simple"><br />
<li>リスト2: パスをちゃんとするq1_3_3.hs</li><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_3.hs<br />
import System.Directory<br />
<br />
main = digdir &quot;/etc&quot; &gt;&gt;= putStr . unlines<br />
<br />
ls :: String -&gt; IO [FilePath]<br />
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])<br />
<br />
digdir :: FilePath -&gt; IO [FilePath]<br />
digdir dir = ls dir<br />
 &gt;&gt;= mapM (\\x -&gt; return $ dir ++ &quot;/&quot; ++ x)<br />
###実行してみましょう。/etc/、ついてますね###<br />
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ ./q1_3_3<br />
/etc/insserv<br />
/etc/blkid.tab<br />
/etc/tidy.conf<br />
/etc/logrotate.conf<br />
（以下略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　変更点は、4行目の <tt class="docutils literal"><span class="pre">main</span></tt> で <tt class="docutils literal"><span class="pre">ls</span></tt> 関数<br />
を使っていたものを <tt class="docutils literal"><span class="pre">digdir</span></tt> に代えました。<br />
ディレクトリを下がって行く準備です。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">digdir</span></tt> ですが、 <tt class="docutils literal"><span class="pre">ls</span></tt> と同様、<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> （バインド演算子）で処理をつないだ作りになっています。<br />
右にどんどんつないでいくと長くなりすぎるので、改行を入れました。<br />
インデントは、10行目の <tt class="docutils literal"><span class="pre">ls</span></tt> のところに合わせました。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">digdir</span></tt> の中身には初めて出て来たものが多いので、<br />
ゆっくり説明して行きます。<br />
まず、11行目の <tt class="docutils literal"><span class="pre">mapM</span></tt> ですが、こんな型です。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM</span><br />
<span class="nf">mapM</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="p">[</span><span class="n">b</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">Monad</span> <span class="pre">m</span> <span class="pre">=&gt;</span></tt> とありますが、<br />
とりあえず <tt class="docutils literal"><span class="pre">m</span></tt> は <tt class="docutils literal"><span class="pre">IO</span></tt> であると考えましょう。</p><br />
<p>　リスト2のコードにおいては、実際の型はこうなります。</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="p">(</span><span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">FilePath</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>つまり、 <tt class="docutils literal"><span class="pre">mapM</span></tt> の入出力を説明すると、</p><br />
<ul class="simple"><br />
<li>第一引数に「FilePath型をとってIO FilePath型を返す関数」をとる</li><br />
<li>第二引数に「FilePathのリスト」をとる</li><br />
<li>出力には「FilePathのリストにIOをつけたもの」</li><br />
</ul><br />
<p>となります。動作は、<br />
「FilePathのリストを受け取って、第一引数の関数に次々と突っ込み、<br />
次々と突っ込んだ結果を再度リストにまとめてIOをくっつけて出荷する」<br />
ということになります。<br />
第二引数の「FilePathのリスト」は、<br />
<tt class="docutils literal"><span class="pre">ls</span> <span class="pre">dir</span></tt> の出力です。ただ、 <tt class="docutils literal"><span class="pre">ls</span> <span class="pre">dir</span></tt> の出力の型は<br />
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> ですが、 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を介すと <tt class="docutils literal"><span class="pre">IO</span></tt><br />
を取って演算できるのでした。</p><br />
<p>　ちなみにこれまでも出てきた <tt class="docutils literal"><span class="pre">map</span></tt> の型は、</p><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">map</span><br />
<span class="nf">map</span> <span class="ow">::</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">b</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>でした。<br />
<tt class="docutils literal"><span class="pre">mapM</span></tt> は、 <tt class="docutils literal"><span class="pre">map</span></tt> のように振る舞いながら、<br />
さらに <tt class="docutils literal"><span class="pre">IO</span></tt> を頭にくっつけるという動作になります。</p><br />
<p>　次、 <tt class="docutils literal"><span class="pre">mapM</span></tt> の第一引数の</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="se">\\x</span> -&gt; <span class="k">return</span> <span class="nv">$ </span>dir ++ <span class="s2">&quot;/&quot;</span> ++ x<br />
</pre></div><br />
</div><br />
<p>ですが、これは</p><br />
<div class="highlight-bash"><div class="highlight"><pre>somefunc <span class="nv">x</span> <span class="o">=</span> <span class="k">return</span> <span class="nv">$ </span>dir ++ <span class="s2">&quot;/&quot;</span> ++ x<br />
</pre></div><br />
</div><br />
<p>という関数と等価です。<br />
<tt class="docutils literal"><span class="pre">return</span></tt> とかややこしいことが書いてありますが、<br />
それは関係なく、単に関数を書くときには<br />
リスト3のように、二つの書き方ができるということです。<br />
上の「 <tt class="docutils literal"><span class="pre">somefunc</span></tt> 」やリスト3の下の例<br />
「 <tt class="docutils literal"><span class="pre">f</span></tt> 」のように名前をつけてしまうと<br />
<tt class="docutils literal"><span class="pre">mapM</span></tt> に直接渡せないので、<br />
「 <tt class="docutils literal"><span class="pre">\\x</span> <span class="pre">-&gt;</span> <span class="pre">...</span></tt> 」のような書き方をしています。<br />
このように書かれた関数は「無名関数」や「ラムダ式」<br />
と呼ばれます。</p><br />
<ul class="simple"><br />
<li>リスト3: 二つの関数の書き方</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="se">\\x</span> -&gt; 1 + x<br />
f <span class="nv">x</span> <span class="o">=</span> 1 + x<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　で、最後の重要な話に <tt class="docutils literal"><span class="pre">return</span></tt> 関数があります。<br />
これは、 <tt class="docutils literal"><span class="pre">dir</span> <span class="pre">++</span> <span class="pre">&quot;/&quot;</span> <span class="pre">++</span> <span class="pre">x</span></tt><br />
の型FilePathにIOをくっつけて <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">FilePath</span></tt><br />
にするための関数です。<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> でつながれた演算の中では、<br />
型を合わせるためにしばしば登場します。<br />
普通のプログラミング言語の <tt class="docutils literal"><span class="pre">return</span></tt><br />
とは違うものですのでご注意を。<br />
型を示しておきます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="k">return</span><br />
<span class="k">return</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; a -&gt; m a<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>6.4. 再帰的にディレクトリを調査<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次にやる事は、 <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下の子供、孫、ひ孫、玄孫・・・<br />
のディレクトリも調査することです。<br />
<tt class="docutils literal"><span class="pre">digdir</span></tt> をいじって、次のような処理を組み込みます。</p><br />
<ul class="simple"><br />
<li>FilePathのリスト中の要素が、ファイルならばそのまま残す</li><br />
<li>FilePathのリスト中の要素が、ディレクトリならばそのディレクトリ下のリストでその要素を置き換える</li><br />
</ul><br />
<p>ということで実装したものをリスト4に示します。<br />
<tt class="docutils literal"><span class="pre">digdir</span></tt> に2行加えて、あとは <tt class="docutils literal"><span class="pre">digdir'</span></tt> という関数を定義しています。</p><br />
<ul class="simple"><br />
<li>リスト4: 再帰的にディレクトリを検索してファイルパスを返すq1_3_4.hs</li><br />
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
24<br />
25<br />
26<br />
27<br />
28<br />
29<br />
30</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_4.hs<br />
import System.Directory<br />
<br />
main = digdir &quot;/etc&quot; &gt;&gt;= putStr . unlines<br />
<br />
ls :: String -&gt; IO [FilePath]<br />
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])<br />
<br />
digdir :: FilePath -&gt; IO [FilePath]<br />
digdir dir = ls dir<br />
 &gt;&gt;= mapM (\\x -&gt; return $ dir ++ &quot;/&quot; ++ x)<br />
 &gt;&gt;= mapM digdir&#39;<br />
 &gt;&gt;= return . concat<br />
<br />
digdir&#39; :: FilePath -&gt; IO [FilePath]<br />
digdir&#39; path = do b &lt;- doesDirectoryExist path<br />
 if b then digdir path else return [path]<br />
###実行!!!（rootになってください）###<br />
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ sudo ./q1_3_4<br />
/etc/blkid.tab<br />
/etc/tidy.conf<br />
/etc/logrotate.conf<br />
/etc/avserver.conf<br />
/etc/gshadow-<br />
/etc/iproute2/rt_dsfield<br />
/etc/iproute2/rt_realms<br />
（中略）<br />
/etc/dhcp/dhclient-enter-hooks.d/resolvconf<br />
/etc/dhcp/dhclient-enter-hooks.d/debug<br />
（以下略）<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="you-do"><br />
<h2>6.5. ヘイ！you！doしちゃいなよ<a class="headerlink" href="#you-do" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まず、 <tt class="docutils literal"><span class="pre">digdir'</span></tt> から説明して行きます。<br />
<tt class="docutils literal"><span class="pre">do</span></tt> の説明をしないといけないでしょう。<br />
理屈でなく単純に説明すると、<br />
<tt class="docutils literal"><span class="pre">do</span></tt> は <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> のように一直線にアクションをさばくとややこしいときに、<br />
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の代わりに使うものです。<br />
例えば、リスト5の二つのコードは等価です。</p><br />
<ul class="simple"><br />
<li>リスト5: doとbind演算子の書き方比較</li><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="n">bind</span><span class="o">.</span><span class="n">hs</span><br />
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="kr">do</span><span class="o">.</span><span class="n">hs</span><br />
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span><br />
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">str</span> <span class="ow">&lt;-</span> <span class="n">getContents</span><br />
 <span class="n">putStr</span> <span class="n">str</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">echo</span> <span class="n">aho</span> <span class="o">|</span> <span class="o">./</span><span class="n">bind</span><br />
<span class="nf">aho</span><br />
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">echo</span> <span class="n">aho</span> <span class="o">|</span> <span class="o">./</span><span class="kr">do</span><br />
<span class="nf">aho</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">bind.hs</span></tt> の方は今までも使っていたバインド演算子を使ったやり方です。<br />
型を調べておきましょう。リスト6のようになります。</p><br />
<ul class="simple"><br />
<li>リスト6: bind.hsに関する関数の型</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">getContents</span><br />
<span class="nf">getContents</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="kt">String</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span><br />
<span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">putStr</span><br />
<span class="nf">putStr</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>ここから読み取るのは大変かもしれませんが、<br />
引数に <tt class="docutils literal"><span class="pre">String</span></tt> をとる <tt class="docutils literal"><span class="pre">putStr</span></tt> 関数を使うために <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> で<br />
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">String</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> を取っ払っています。</p><br />
<p><tt class="docutils literal"><span class="pre">do.hs</span></tt> でもやっていることは全く同じです。<br />
基本的な考え方は、 <tt class="docutils literal"><span class="pre">do</span></tt> の中では <tt class="docutils literal"><span class="pre">IO</span></tt><br />
の部分を気にしなくてよいということです。<br />
<tt class="docutils literal"><span class="pre">str</span> <span class="pre">&lt;-</span> <span class="pre">getContents</span></tt> の <tt class="docutils literal"><span class="pre">&lt;-</span></tt><br />
（左向き矢印演算子）は、 <tt class="docutils literal"><span class="pre">getContents</span></tt><br />
の <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">String</span></tt> の出力から、<br />
<tt class="docutils literal"><span class="pre">String</span></tt> の部分だけ <tt class="docutils literal"><span class="pre">str</span></tt> に関連づけます。<br />
その下の行で、 <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">str</span></tt><br />
してこの <tt class="docutils literal"><span class="pre">do</span></tt> は終わりますが、<br />
終わったときの <tt class="docutils literal"><span class="pre">putStr</span></tt> の出力の型は<br />
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> なので、 <tt class="docutils literal"><span class="pre">main</span></tt> の型と一致します。</p><br />
<p>　ところで、なんで <tt class="docutils literal"><span class="pre">digdir'</span></tt> 関数で<br />
<tt class="docutils literal"><span class="pre">do</span></tt> を使わなければならないかというと、<br />
パスがディレクトリかどうか判断する<br />
<tt class="docutils literal"><span class="pre">doesDirectoryExist</span></tt> 関数の出力が、<br />
残念なことに <tt class="docutils literal"><span class="pre">Bool</span></tt> ではなく、</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import System.Directory<br />
Prelude System.Directory&gt; :t doesDirectoryExist<br />
doesDirectoryExist :: FilePath -&gt; IO Bool<br />
</pre></div><br />
</td></tr></table></div><br />
<p>・・・と <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">Bool</span></tt> なので、<br />
そのまま <tt class="docutils literal"><span class="pre">if</span></tt> 関数に突っ込めないからです。<br />
<tt class="docutils literal"><span class="pre">if</span></tt> に突っ込むには <tt class="docutils literal"><span class="pre">IO</span></tt> を取らなければいけないのですが、<br />
それをやるために16行目で左向き矢印演算子を使っています。<br />
16行目のように <tt class="docutils literal"><span class="pre">b</span> <span class="pre">&lt;-</span></tt> を使うと、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">Bool</span></tt><br />
のうちの <tt class="docutils literal"><span class="pre">Bool</span></tt> に相当するものだけを指すようになります。<br />
で、17行目で <tt class="docutils literal"><span class="pre">b</span></tt> を <tt class="docutils literal"><span class="pre">if</span></tt> 関数に突っ込んでいます。<br />
<tt class="docutils literal"><span class="pre">if</span></tt> 関数は、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">True</span></tt> （ <tt class="docutils literal"><span class="pre">path</span></tt> がディレクトリを指す）<br />
ならば <tt class="docutils literal"><span class="pre">digdir</span> <span class="pre">path</span></tt> を返し（再帰となる）、<br />
そうでなければそのまま <tt class="docutils literal"><span class="pre">path</span></tt> を要素1個のリストにして、<br />
<tt class="docutils literal"><span class="pre">return</span></tt> で <tt class="docutils literal"><span class="pre">IO</span></tt> をくっつけて返します。</p><br />
<p>　最後、13行目の <tt class="docutils literal"><span class="pre">return</span> <span class="pre">.</span> <span class="pre">concat</span></tt> を説明しておきます。<br />
<tt class="docutils literal"><span class="pre">concat</span></tt> は、リスト7のように、<br />
リストがリストになっているものを一つのリストに再構成するものです。</p><br />
<ul class="simple"><br />
<li>リスト7: concatの型と挙動</li><br />
</ul><br />
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">concat</span><br />
<span class="nf">concat</span> <span class="ow">::</span> <span class="p">[[</span><span class="n">a</span><span class="p">]]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span><br />
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">concat</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],[</span><span class="mi">3</span><span class="p">],[</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">]]</span><br />
<span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>ですので、 <tt class="docutils literal"><span class="pre">mapM</span> <span class="pre">digdir'</span> <span class="pre">&gt;&gt;=</span></tt> で <tt class="docutils literal"><span class="pre">[[FilePath]]</span></tt><br />
が渡って来たものを <tt class="docutils literal"><span class="pre">[FilePath]</span></tt> にならし、<br />
<tt class="docutils literal"><span class="pre">return</span></tt> で <tt class="docutils literal"><span class="pre">IO</span></tt> をくっつけて <tt class="docutils literal"><span class="pre">digdir</span></tt><br />
の最終的な出力型 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> を実現しています。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h2>6.6. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は第1回の3問目で、 <tt class="docutils literal"><span class="pre">/etc</span></tt> 下のファイルリストを、<br />
複数階層下までファイルを探して作るまでを行いました。<br />
次回以降、探したファイルをコピーしたり書き換えたりと、<br />
ゴリゴリ処理していきます。</p><br />
<p>　・・・しかし、これシェル芸だと一瞬で終わってしまうことを<br />
何ヶ月もかけてやっているような。<br />
シェル芸って本当に便利ね・・・。</p><br />
</div><br />
<div class="section" id="id10"><br />
<h2>6.7. お知らせ：コード募集<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　本稿で出た問題のHaskellのコードを、<br />
名前あるいはハンドルネームと共に送ってください。<br />
短いもの、あるいは変態的なものをお願いいたします。</p><br />
<p>email: 編集部のメールアドレス</p><br />
<p class="rubric">脚注</p><br />
<table class="docutils footnote" frame="void" id="id11" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id3">[1]</a></td><td>これ、働き始めた26歳からずーっと言い続けているような気がしないでもない。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id12" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id1">[2]</a></td><td>順に助教、アドバイザリーフェロー、会長。肩書き好きの天下り官僚のような並び方である。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id13" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id5">[3]</a></td><td>真面目に見せかけて酷いことを書いている。</td></tr><br />
</tbody><br />
</table><br />
<table class="docutils footnote" frame="void" id="id14" rules="none"><br />
<colgroup><col class="label" /><col /></colgroup><br />
<tbody valign="top"><br />
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>問題は <tt class="docutils literal"><span class="pre">http://blog.ueda.asia/?page_id=684</span></tt> から。</td></tr><br />
</tbody><br />
</table><br />
</div><br />
</div>
