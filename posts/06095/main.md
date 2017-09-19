---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年9月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>6. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院・USP研究所・USP友の会　上田隆一
<a class="footnote-reference" href="#id12" id="id1">[2]</a></p>
<blockquote>
<div>USP友の会のシェル芸勉強会
（脚注：シェルのワンライナー勉強会）は、
日々、他の言語からの他流試合に晒されているのである。
そこで上田は、Haskellで自ら他流試合を行い、
さらにシェル芸勉強会をいじめる自傷行為に手を
染めるのであった。</div></blockquote>
<div class="section" id="id2">
<h2>6.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　こんにちは。本も出たことだしもうちょっと
大人にならなければならないような気がしないでもない上田です。
<a class="footnote-reference" href="#id11" id="id3">[1]</a></p>
<p>　大学にいるとしょっちゅう高専生と間違われます。
間違われるのは楽しいんだけどたまに横柄な扱いを受けます。
私はいつもそんな目にあっているので、
若い人をちゃんと敬う気持ちが欲しいなと日頃、思っております。
自分の子供を見ていると分かりますが、
若い世代の方が効率的に勉強してますしね。
私のような年寄りは早くホロン部した方がよいような気がします。</p>
</div>
<div class="section" id="id4">
<h2>6.2. 今回の問題<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、いつになく真面目に
<a class="footnote-reference" href="#id13" id="id5">[3]</a>
スタートしましたが、
今回は第1回シェル芸勉強会の3問目の途中からです。
<a class="footnote-reference" href="#id14" id="id6">[4]</a></p>
<blockquote>
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）
について以下の操作をしてください。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li>
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li>
</ul>
</div></blockquote>
<p>前回は、リスト1のように <tt class="docutils literal"><span class="pre">/etc</span></tt> 直下のファイルを列挙するところまで来ていました。</p>
<ul class="simple">
<li>リスト1: ファイルのリストを作るプログラムと実行結果</li>
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
20</pre></div></td><td class="code"><div class="highlight"><pre>###こんなコード###
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_2.hs
import System.Directory

main = ls &quot;/etc/&quot; &gt;&gt;= putStr . unlines

ls :: String -&gt; IO [FilePath]
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])
###実行!!###
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ ./q1_3_2 | head
insserv
blkid.tab
tidy.conf
logrotate.conf
avserver.conf
gshadow-
iproute2
localtime
systemd
dhcp
</pre></div>
</td></tr></table></div>
<p>　「 <tt class="docutils literal"><span class="pre">/etc</span></tt> 下」というのは子のディレクトリ、孫のディレクトリ・・・
と下のディレクトリのファイルも全部含むつもりで出題しました。
ですので、再帰的にディレクトリを降りて行く処理の実装が必要になります。</p>
</div>
<div class="section" id="id7">
<h2>6.3. パスを作る<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はまず、 <tt class="docutils literal"><span class="pre">q1_3_2</span></tt> の出力の頭に <tt class="docutils literal"><span class="pre">/etc/</span></tt>
をくっつけるところから始めましょう。
このままだと、再帰的にディレクトリを降りてファイルのリストを作って行くとき、
どのディレクトリのファイルか分からなくなってしまいます。
リスト2のようにプログラムを書きかえます。</p>
<ul class="simple">
<li>リスト2: パスをちゃんとするq1_3_3.hs</li>
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
18</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_3.hs
import System.Directory

main = digdir &quot;/etc&quot; &gt;&gt;= putStr . unlines

ls :: String -&gt; IO [FilePath]
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])

digdir :: FilePath -&gt; IO [FilePath]
digdir dir = ls dir
 &gt;&gt;= mapM (\\x -&gt; return $ dir ++ &quot;/&quot; ++ x)
###実行してみましょう。/etc/、ついてますね###
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ ./q1_3_3
/etc/insserv
/etc/blkid.tab
/etc/tidy.conf
/etc/logrotate.conf
（以下略）
</pre></div>
</td></tr></table></div>
<p>　変更点は、4行目の <tt class="docutils literal"><span class="pre">main</span></tt> で <tt class="docutils literal"><span class="pre">ls</span></tt> 関数
を使っていたものを <tt class="docutils literal"><span class="pre">digdir</span></tt> に代えました。
ディレクトリを下がって行く準備です。</p>
<p>　 <tt class="docutils literal"><span class="pre">digdir</span></tt> ですが、 <tt class="docutils literal"><span class="pre">ls</span></tt> と同様、
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> （バインド演算子）で処理をつないだ作りになっています。
右にどんどんつないでいくと長くなりすぎるので、改行を入れました。
インデントは、10行目の <tt class="docutils literal"><span class="pre">ls</span></tt> のところに合わせました。</p>
<p>　 <tt class="docutils literal"><span class="pre">digdir</span></tt> の中身には初めて出て来たものが多いので、
ゆっくり説明して行きます。
まず、11行目の <tt class="docutils literal"><span class="pre">mapM</span></tt> ですが、こんな型です。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">mapM</span>
<span class="nf">mapM</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="p">[</span><span class="n">b</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">Monad</span> <span class="pre">m</span> <span class="pre">=&gt;</span></tt> とありますが、
とりあえず <tt class="docutils literal"><span class="pre">m</span></tt> は <tt class="docutils literal"><span class="pre">IO</span></tt> であると考えましょう。</p>
<p>　リスト2のコードにおいては、実際の型はこうなります。</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="p">(</span><span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">FilePath</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>つまり、 <tt class="docutils literal"><span class="pre">mapM</span></tt> の入出力を説明すると、</p>
<ul class="simple">
<li>第一引数に「FilePath型をとってIO FilePath型を返す関数」をとる</li>
<li>第二引数に「FilePathのリスト」をとる</li>
<li>出力には「FilePathのリストにIOをつけたもの」</li>
</ul>
<p>となります。動作は、
「FilePathのリストを受け取って、第一引数の関数に次々と突っ込み、
次々と突っ込んだ結果を再度リストにまとめてIOをくっつけて出荷する」
ということになります。
第二引数の「FilePathのリスト」は、
<tt class="docutils literal"><span class="pre">ls</span> <span class="pre">dir</span></tt> の出力です。ただ、 <tt class="docutils literal"><span class="pre">ls</span> <span class="pre">dir</span></tt> の出力の型は
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> ですが、 <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> を介すと <tt class="docutils literal"><span class="pre">IO</span></tt>
を取って演算できるのでした。</p>
<p>　ちなみにこれまでも出てきた <tt class="docutils literal"><span class="pre">map</span></tt> の型は、</p>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">map</span>
<span class="nf">map</span> <span class="ow">::</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">b</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>でした。
<tt class="docutils literal"><span class="pre">mapM</span></tt> は、 <tt class="docutils literal"><span class="pre">map</span></tt> のように振る舞いながら、
さらに <tt class="docutils literal"><span class="pre">IO</span></tt> を頭にくっつけるという動作になります。</p>
<p>　次、 <tt class="docutils literal"><span class="pre">mapM</span></tt> の第一引数の</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="se">\\x</span> -&gt; <span class="k">return</span> <span class="nv">$ </span>dir ++ <span class="s2">&quot;/&quot;</span> ++ x
</pre></div>
</div>
<p>ですが、これは</p>
<div class="highlight-bash"><div class="highlight"><pre>somefunc <span class="nv">x</span> <span class="o">=</span> <span class="k">return</span> <span class="nv">$ </span>dir ++ <span class="s2">&quot;/&quot;</span> ++ x
</pre></div>
</div>
<p>という関数と等価です。
<tt class="docutils literal"><span class="pre">return</span></tt> とかややこしいことが書いてありますが、
それは関係なく、単に関数を書くときには
リスト3のように、二つの書き方ができるということです。
上の「 <tt class="docutils literal"><span class="pre">somefunc</span></tt> 」やリスト3の下の例
「 <tt class="docutils literal"><span class="pre">f</span></tt> 」のように名前をつけてしまうと
<tt class="docutils literal"><span class="pre">mapM</span></tt> に直接渡せないので、
「 <tt class="docutils literal"><span class="pre">\\x</span> <span class="pre">-&gt;</span> <span class="pre">...</span></tt> 」のような書き方をしています。
このように書かれた関数は「無名関数」や「ラムダ式」
と呼ばれます。</p>
<ul class="simple">
<li>リスト3: 二つの関数の書き方</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="se">\\x</span> -&gt; 1 + x
f <span class="nv">x</span> <span class="o">=</span> 1 + x
</pre></div>
</td></tr></table></div>
<p>　で、最後の重要な話に <tt class="docutils literal"><span class="pre">return</span></tt> 関数があります。
これは、 <tt class="docutils literal"><span class="pre">dir</span> <span class="pre">++</span> <span class="pre">&quot;/&quot;</span> <span class="pre">++</span> <span class="pre">x</span></tt>
の型FilePathにIOをくっつけて <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">FilePath</span></tt>
にするための関数です。
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> でつながれた演算の中では、
型を合わせるためにしばしば登場します。
普通のプログラミング言語の <tt class="docutils literal"><span class="pre">return</span></tt>
とは違うものですのでご注意を。
型を示しておきます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="k">return</span>
<span class="k">return</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; a -&gt; m a
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h2>6.4. 再帰的にディレクトリを調査<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次にやる事は、 <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下の子供、孫、ひ孫、玄孫・・・
のディレクトリも調査することです。
<tt class="docutils literal"><span class="pre">digdir</span></tt> をいじって、次のような処理を組み込みます。</p>
<ul class="simple">
<li>FilePathのリスト中の要素が、ファイルならばそのまま残す</li>
<li>FilePathのリスト中の要素が、ディレクトリならばそのディレクトリ下のリストでその要素を置き換える</li>
</ul>
<p>ということで実装したものをリスト4に示します。
<tt class="docutils literal"><span class="pre">digdir</span></tt> に2行加えて、あとは <tt class="docutils literal"><span class="pre">digdir'</span></tt> という関数を定義しています。</p>
<ul class="simple">
<li>リスト4: 再帰的にディレクトリを検索してファイルパスを返すq1_3_4.hs</li>
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
24
25
26
27
28
29
30</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat q1_3_4.hs
import System.Directory

main = digdir &quot;/etc&quot; &gt;&gt;= putStr . unlines

ls :: String -&gt; IO [FilePath]
ls dir = getDirectoryContents dir &gt;&gt;= return . filter (`notElem` [&quot;.&quot;,&quot;..&quot;])

digdir :: FilePath -&gt; IO [FilePath]
digdir dir = ls dir
 &gt;&gt;= mapM (\\x -&gt; return $ dir ++ &quot;/&quot; ++ x)
 &gt;&gt;= mapM digdir&#39;
 &gt;&gt;= return . concat

digdir&#39; :: FilePath -&gt; IO [FilePath]
digdir&#39; path = do b &lt;- doesDirectoryExist path
 if b then digdir path else return [path]
###実行!!!（rootになってください）###
ueda\@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ sudo ./q1_3_4
/etc/blkid.tab
/etc/tidy.conf
/etc/logrotate.conf
/etc/avserver.conf
/etc/gshadow-
/etc/iproute2/rt_dsfield
/etc/iproute2/rt_realms
（中略）
/etc/dhcp/dhclient-enter-hooks.d/resolvconf
/etc/dhcp/dhclient-enter-hooks.d/debug
（以下略）
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="you-do">
<h2>6.5. ヘイ！you！doしちゃいなよ<a class="headerlink" href="#you-do" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まず、 <tt class="docutils literal"><span class="pre">digdir'</span></tt> から説明して行きます。
<tt class="docutils literal"><span class="pre">do</span></tt> の説明をしないといけないでしょう。
理屈でなく単純に説明すると、
<tt class="docutils literal"><span class="pre">do</span></tt> は <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> のように一直線にアクションをさばくとややこしいときに、
<tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の代わりに使うものです。
例えば、リスト5の二つのコードは等価です。</p>
<ul class="simple">
<li>リスト5: doとbind演算子の書き方比較</li>
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="n">bind</span><span class="o">.</span><span class="n">hs</span>
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="n">getContents</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span>
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="kr">do</span><span class="o">.</span><span class="n">hs</span>
<span class="nf">main</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="nb">()</span>
<span class="nf">main</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">str</span> <span class="ow">&lt;-</span> <span class="n">getContents</span>
 <span class="n">putStr</span> <span class="n">str</span>
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">echo</span> <span class="n">aho</span> <span class="o">|</span> <span class="o">./</span><span class="n">bind</span>
<span class="nf">aho</span>
<span class="nf">ueda</span><span class="o">\@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">echo</span> <span class="n">aho</span> <span class="o">|</span> <span class="o">./</span><span class="kr">do</span>
<span class="nf">aho</span>
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">bind.hs</span></tt> の方は今までも使っていたバインド演算子を使ったやり方です。
型を調べておきましょう。リスト6のようになります。</p>
<ul class="simple">
<li>リスト6: bind.hsに関する関数の型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">getContents</span>
<span class="nf">getContents</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="kt">String</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span>
<span class="p">(</span><span class="o">&gt;&gt;=</span><span class="p">)</span> <span class="ow">::</span> <span class="kt">Monad</span> <span class="n">m</span> <span class="ow">=&gt;</span> <span class="n">m</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="n">a</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="n">m</span> <span class="n">b</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">putStr</span>
<span class="nf">putStr</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="nb">()</span>
</pre></div>
</td></tr></table></div>
<p>ここから読み取るのは大変かもしれませんが、
引数に <tt class="docutils literal"><span class="pre">String</span></tt> をとる <tt class="docutils literal"><span class="pre">putStr</span></tt> 関数を使うために <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> で
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">String</span></tt> から <tt class="docutils literal"><span class="pre">IO</span></tt> を取っ払っています。</p>
<p><tt class="docutils literal"><span class="pre">do.hs</span></tt> でもやっていることは全く同じです。
基本的な考え方は、 <tt class="docutils literal"><span class="pre">do</span></tt> の中では <tt class="docutils literal"><span class="pre">IO</span></tt>
の部分を気にしなくてよいということです。
<tt class="docutils literal"><span class="pre">str</span> <span class="pre">&lt;-</span> <span class="pre">getContents</span></tt> の <tt class="docutils literal"><span class="pre">&lt;-</span></tt>
（左向き矢印演算子）は、 <tt class="docutils literal"><span class="pre">getContents</span></tt>
の <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">String</span></tt> の出力から、
<tt class="docutils literal"><span class="pre">String</span></tt> の部分だけ <tt class="docutils literal"><span class="pre">str</span></tt> に関連づけます。
その下の行で、 <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">str</span></tt>
してこの <tt class="docutils literal"><span class="pre">do</span></tt> は終わりますが、
終わったときの <tt class="docutils literal"><span class="pre">putStr</span></tt> の出力の型は
<tt class="docutils literal"><span class="pre">IO</span> <span class="pre">()</span></tt> なので、 <tt class="docutils literal"><span class="pre">main</span></tt> の型と一致します。</p>
<p>　ところで、なんで <tt class="docutils literal"><span class="pre">digdir'</span></tt> 関数で
<tt class="docutils literal"><span class="pre">do</span></tt> を使わなければならないかというと、
パスがディレクトリかどうか判断する
<tt class="docutils literal"><span class="pre">doesDirectoryExist</span></tt> 関数の出力が、
残念なことに <tt class="docutils literal"><span class="pre">Bool</span></tt> ではなく、</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; import System.Directory
Prelude System.Directory&gt; :t doesDirectoryExist
doesDirectoryExist :: FilePath -&gt; IO Bool
</pre></div>
</td></tr></table></div>
<p>・・・と <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">Bool</span></tt> なので、
そのまま <tt class="docutils literal"><span class="pre">if</span></tt> 関数に突っ込めないからです。
<tt class="docutils literal"><span class="pre">if</span></tt> に突っ込むには <tt class="docutils literal"><span class="pre">IO</span></tt> を取らなければいけないのですが、
それをやるために16行目で左向き矢印演算子を使っています。
16行目のように <tt class="docutils literal"><span class="pre">b</span> <span class="pre">&lt;-</span></tt> を使うと、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">Bool</span></tt>
のうちの <tt class="docutils literal"><span class="pre">Bool</span></tt> に相当するものだけを指すようになります。
で、17行目で <tt class="docutils literal"><span class="pre">b</span></tt> を <tt class="docutils literal"><span class="pre">if</span></tt> 関数に突っ込んでいます。
<tt class="docutils literal"><span class="pre">if</span></tt> 関数は、 <tt class="docutils literal"><span class="pre">b</span></tt> が <tt class="docutils literal"><span class="pre">True</span></tt> （ <tt class="docutils literal"><span class="pre">path</span></tt> がディレクトリを指す）
ならば <tt class="docutils literal"><span class="pre">digdir</span> <span class="pre">path</span></tt> を返し（再帰となる）、
そうでなければそのまま <tt class="docutils literal"><span class="pre">path</span></tt> を要素1個のリストにして、
<tt class="docutils literal"><span class="pre">return</span></tt> で <tt class="docutils literal"><span class="pre">IO</span></tt> をくっつけて返します。</p>
<p>　最後、13行目の <tt class="docutils literal"><span class="pre">return</span> <span class="pre">.</span> <span class="pre">concat</span></tt> を説明しておきます。
<tt class="docutils literal"><span class="pre">concat</span></tt> は、リスト7のように、
リストがリストになっているものを一つのリストに再構成するものです。</p>
<ul class="simple">
<li>リスト7: concatの型と挙動</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">concat</span>
<span class="nf">concat</span> <span class="ow">::</span> <span class="p">[[</span><span class="n">a</span><span class="p">]]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="n">concat</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],[</span><span class="mi">3</span><span class="p">],[</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">]]</span>
<span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>ですので、 <tt class="docutils literal"><span class="pre">mapM</span> <span class="pre">digdir'</span> <span class="pre">&gt;&gt;=</span></tt> で <tt class="docutils literal"><span class="pre">[[FilePath]]</span></tt>
が渡って来たものを <tt class="docutils literal"><span class="pre">[FilePath]</span></tt> にならし、
<tt class="docutils literal"><span class="pre">return</span></tt> で <tt class="docutils literal"><span class="pre">IO</span></tt> をくっつけて <tt class="docutils literal"><span class="pre">digdir</span></tt>
の最終的な出力型 <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> を実現しています。</p>
</div>
<div class="section" id="id9">
<h2>6.6. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は第1回の3問目で、 <tt class="docutils literal"><span class="pre">/etc</span></tt> 下のファイルリストを、
複数階層下までファイルを探して作るまでを行いました。
次回以降、探したファイルをコピーしたり書き換えたりと、
ゴリゴリ処理していきます。</p>
<p>　・・・しかし、これシェル芸だと一瞬で終わってしまうことを
何ヶ月もかけてやっているような。
シェル芸って本当に便利ね・・・。</p>
</div>
<div class="section" id="id10">
<h2>6.7. お知らせ：コード募集<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id11" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[1]</a></td><td>これ、働き始めた26歳からずーっと言い続けているような気がしないでもない。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id12" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[2]</a></td><td>順に助教、アドバイザリーフェロー、会長。肩書き好きの天下り官僚のような並び方である。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id13" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id5">[3]</a></td><td>真面目に見せかけて酷いことを書いている。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>問題は <tt class="docutils literal"><span class="pre">http://blog.ueda.asia/?page_id=684</span></tt> から。</td></tr>
</tbody>
</table>
</div>
</div>
