---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年10月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
<h1>7. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？<a class="headerlink" href="#haskell" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>産業技術大学院大学・USP研究所・USP友の会　上田隆一</p>
<blockquote>
<div>USP友の会のシェル芸勉強会
（脚注：シェルのワンライナー勉強会）は、
日々、他の言語からの他流試合に晒されているのである。
そこで上田は、Haskellで自ら他流試合を行い、
さらにシェル芸勉強会をいじめる自傷行為に手を
染めるのであった。</div></blockquote>
<div class="section" id="id1">
<h2>7.1. はじめに<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　こんにちは。富山の産んだ、
とれとれぴちぴちブラックエンジェル上田です
<a class="footnote-reference" href="#id14" id="id2">[1]</a>
。
先週、久々に国際学会に出かけていっていろいろ
ロボット屋さんの情報を仕入れてきました。
アトムを誰かが作っているとか、
その電池（原子力）がかなりヤバいらしいとか、
ガンダムを作ってパチンコガンダム
<a class="footnote-reference" href="#id15" id="id3">[2]</a>
に納品したとか、
いろいろ聞いてきました。</p>
<p>　・・・すんません嘘です。ほぼ100%、人事の話でした・・・。
学者も食ってかないといけないので、いろいろ大変です。</p>
</div>
<div class="section" id="id4">
<h2>7.2. 前回のおさらい<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　かつてはサンクチュアリであった学者の世界も
最近はすっかり世知辛くなり、
我々がすがることができるのはせいぜいシェル芸とHaskell
の世界のみです
<a class="footnote-reference" href="#id16" id="id5">[3]</a>
。
ということで、今回も第1回シェル芸勉強会の3問目の途中から
Haskellをやってみまっしょい。問題はこれ。</p>
<blockquote>
<div><p><tt class="docutils literal"><span class="pre">/etc</span></tt> の下にあるすべてのbashスクリプト
（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> で始まるもの）
について以下の操作をしてください。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">~/hoge</span></tt> というディレクトリにコピー</li>
<li>その際、 「 <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> 」を「 <tt class="docutils literal"><span class="pre">#!/usr/local/bin/bash</span></tt> 」 に変更</li>
</ul>
</div></blockquote>
<p>　前回は <tt class="docutils literal"><span class="pre">/etc/</span></tt> 下のファイルの一覧を作るところまで作りました。
コードをリスト1に示します。このコードに追加していきます。</p>
<ul class="simple">
<li>リスト1: q1_3_4.hs</li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="o">./</span><span class="n">q1_3_4</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">System.Directory</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">digdir</span> <span class="s">&quot;/etc&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">unlines</span>

<span class="nf">ls</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">ls</span> <span class="n">dir</span> <span class="ow">=</span> <span class="n">getDirectoryContents</span> <span class="n">dir</span> <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="n">filter</span> <span class="p">(`</span><span class="n">notElem</span><span class="p">`</span> <span class="p">[</span><span class="s">&quot;.&quot;</span><span class="p">,</span><span class="s">&quot;..&quot;</span><span class="p">])</span>

<span class="nf">digdir</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">digdir</span> <span class="n">dir</span> <span class="ow">=</span> <span class="n">ls</span> <span class="n">dir</span>
 <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="p">(</span><span class="nf">\\</span><span class="n">x</span> <span class="ow">-&gt;</span> <span class="n">return</span> <span class="o">$</span> <span class="n">dir</span> <span class="o">++</span> <span class="s">&quot;/&quot;</span> <span class="o">++</span> <span class="n">x</span><span class="p">)</span>
 <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="n">digdir&#39;</span>
 <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="n">concat</span>

<span class="nf">digdir&#39;</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">digdir&#39;</span> <span class="n">path</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">b</span> <span class="ow">&lt;-</span> <span class="n">doesDirectoryExist</span> <span class="n">path</span>
 <span class="kr">if</span> <span class="n">b</span> <span class="kr">then</span> <span class="n">digdir</span> <span class="n">path</span> <span class="kr">else</span> <span class="n">return</span> <span class="p">[</span><span class="n">path</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>　実行結果はリスト2の通りです。
<tt class="docutils literal"><span class="pre">/etc</span></tt> 下には一般ユーザで見られないファイルもあるので、
頭にsudo(1)
<a class="footnote-reference" href="#id17" id="id6">[4]</a>
を付けます。</p>
<ul class="simple">
<li>リスト2: q1_3_4の実行結果（headで省略しています）</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_4 | head -n 3
/etc/blkid.tab
/etc/tidy.conf
/etc/logrotate.conf
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h2>7.3. ファイルをモジュールに分けてみる<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、今回は4行目の <tt class="docutils literal"><span class="pre">digdir</span></tt> から出力される
ファイル名からファイルを順番に開いていく処理を書いていきます。
が、6行目以下は今後全然使いません。
全然使わないコードをリストにいちいち書いて原稿料を頂く方針もありますが、
それは大変申し訳ないのでコードを隠してみましょう。</p>
<ul class="simple">
<li>リスト3: FileTools.hs</li>
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
20</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="kt">FileTools</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">module</span> <span class="nn">FileTools</span> <span class="p">(</span>
<span class="nf">find</span><span class="p">,</span>
<span class="nf">ls</span>
<span class="p">)</span> <span class="kr">where</span>

<span class="kr">import</span> <span class="nn">System.Directory</span>

<span class="nf">ls</span> <span class="ow">::</span> <span class="kt">String</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">ls</span> <span class="n">dir</span> <span class="ow">=</span> <span class="n">getDirectoryContents</span> <span class="n">dir</span> <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="n">filter</span> <span class="p">(`</span><span class="n">notElem</span><span class="p">`</span> <span class="p">[</span><span class="s">&quot;.&quot;</span><span class="p">,</span><span class="s">&quot;..&quot;</span><span class="p">])</span>

<span class="nf">find</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">find</span> <span class="n">dir</span> <span class="ow">=</span> <span class="n">ls</span> <span class="n">dir</span>
 <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="p">(</span><span class="nf">\\</span><span class="n">x</span> <span class="ow">-&gt;</span> <span class="n">return</span> <span class="o">$</span> <span class="n">dir</span> <span class="o">++</span> <span class="s">&quot;/&quot;</span> <span class="o">++</span> <span class="n">x</span><span class="p">)</span>
 <span class="o">&gt;&gt;=</span> <span class="n">mapM</span> <span class="n">find&#39;</span>
 <span class="o">&gt;&gt;=</span> <span class="n">return</span> <span class="o">.</span> <span class="n">concat</span>

<span class="nf">find&#39;</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="p">[</span><span class="kt">FilePath</span><span class="p">]</span>
<span class="nf">find&#39;</span> <span class="n">path</span> <span class="ow">=</span> <span class="kr">do</span> <span class="n">b</span> <span class="ow">&lt;-</span> <span class="n">doesDirectoryExist</span> <span class="n">path</span>
 <span class="kr">if</span> <span class="n">b</span> <span class="kr">then</span> <span class="n">find</span> <span class="n">path</span> <span class="kr">else</span> <span class="n">return</span> <span class="p">[</span><span class="n">path</span><span class="p">]</span>
</pre></div>
</td></tr></table></div>
<p>　まず、 <tt class="docutils literal"><span class="pre">q1_3_4.hs</span></tt> をコピーして、リスト3のようなファイル
<tt class="docutils literal"><span class="pre">FileTools.hs</span></tt> を作ります。
<tt class="docutils literal"><span class="pre">q1_3_4.hs</span></tt> からの変更は次の3点です。
<tt class="docutils literal"><span class="pre">digdir</span></tt> という名前を <tt class="docutils literal"><span class="pre">find</span></tt> に変更したのは、
使い回すならコマンドのfind(1)と名前を
一緒にしておいた方がよいだろうという判断です。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">module</span> <span class="pre">...</span> <span class="pre">where</span></tt> を追加</li>
<li><tt class="docutils literal"><span class="pre">main</span></tt> 関数を削除</li>
<li><tt class="docutils literal"><span class="pre">digdir</span></tt> を <tt class="docutils literal"><span class="pre">find</span></tt> に変更</li>
</ul>
<p>2〜4行目の <tt class="docutils literal"><span class="pre">module</span> <span class="pre">...</span> <span class="pre">where</span></tt> は、
「FileToolsというモジュールを定義して、
その中のfind関数とls関数を公開する」
という意味になります。
公開する関数は丸括弧の中にカンマ区切りで書きます。</p>
<p>　今度は作ったモジュールを使う側を書いてみましょう。
<tt class="docutils literal"><span class="pre">q1_3_4.hs</span></tt> を <tt class="docutils literal"><span class="pre">q1_3_5.hs</span></tt> のように変更します。
<tt class="docutils literal"><span class="pre">main</span></tt> 以外の関数を削除し、
<tt class="docutils literal"><span class="pre">import</span></tt> を <tt class="docutils literal"><span class="pre">FileTools</span></tt> に変更します。
そうするとリスト4のように3行になってしまいます。</p>
<ul class="simple">
<li>リスト4: <tt class="docutils literal"><span class="pre">FileTools.hs</span></tt> を使う <tt class="docutils literal"><span class="pre">q1_3_5.hs</span></tt></li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">cat</span> <span class="n">q1_3_5</span><span class="o">.</span><span class="n">hs</span>
<span class="kr">import</span> <span class="nn">FileTools</span>

<span class="nf">main</span> <span class="ow">=</span> <span class="n">find</span> <span class="s">&quot;/etc&quot;</span> <span class="o">&gt;&gt;=</span> <span class="n">putStr</span> <span class="o">.</span> <span class="n">unlines</span>
</pre></div>
</td></tr></table></div>
<p>　実行するときは <tt class="docutils literal"><span class="pre">q1_3_5.hs</span></tt> をコンパイルします。
<tt class="docutils literal"><span class="pre">FileTools.hs</span></tt> も勝手にコンパイルされます
<a class="footnote-reference" href="#id18" id="id8">[5]</a> 。</p>
<ul class="simple">
<li>リスト5: 使うモジュールもろともコンパイルして実行</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>ghc q1_3_5.hs
<span class="o">[</span>1 of 2<span class="o">]</span> Compiling FileTools <span class="o">(</span> FileTools.hs, FileTools.o <span class="o">)</span>
<span class="o">[</span>2 of 2<span class="o">]</span> Compiling Main <span class="o">(</span> q1_3_5.hs, q1_3_5.o <span class="o">)</span>
Linking q1_3_5 ...
<span class="c">###実行!!!###</span>
ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_5 | head -n 3
/etc/blkid.tab
/etc/tidy.conf
/etc/logrotate.conf
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">FileTools.hs</span></tt> と <tt class="docutils literal"><span class="pre">q1_3_5.hs</span></tt> は同じディレクトリに置いておいてください。</p>
<p>　また、モジュールはGHCiからも使えます。</p>
<ul class="simple">
<li>リスト6: モジュールをGHCiから利用</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###モジュールのあるところでGHCiを起動###</span>
ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>ghci
Prelude&gt; :load FileTools
Prelude FileTools&gt; ls <span class="s2">&quot;.&quot;</span>
<span class="o">[</span><span class="s2">&quot;q1_3_5.hi&quot;</span>,<span class="s2">&quot;q1_3_2&quot;</span>,<span class="s2">&quot;q1_3_2.hs&quot;</span>,<span class="s2">&quot;do.hs&quot;</span>,<span class="s2">&quot;FileTools.o&quot;</span>,<span class="s2">&quot;bind&quot;</span>
,<span class="s2">&quot;FileTools.hs&quot;</span>,<span class="s2">&quot;q1_3_5&quot;</span>,<span class="s2">&quot;FileTools.hi&quot;</span>,<span class="s2">&quot;q1_3_3&quot;</span>,<span class="s2">&quot;q1_3_1.hs&quot;</span>,<span class="s2">&quot;</span>
<span class="s2">do&quot;</span>,<span class="s2">&quot;q1_3_5.o&quot;</span>,<span class="s2">&quot;bind.hs&quot;</span>,<span class="s2">&quot;q1_3_4&quot;</span>,<span class="s2">&quot;q1_3_4.hs&quot;</span>,<span class="s2">&quot;q1_3_3.hs&quot;</span>,<span class="s2">&quot;q1_</span>
<span class="s2">3_5.hs&quot;</span><span class="o">]</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id9">
<h2>7.4. ファイルを開く関数の実装<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、次はいよいよファイルの中身を見て行くわけですが、
ここで <tt class="docutils literal"><span class="pre">FileTools.hs</span></tt> に
ファイルを開いて中身を返す関数 <tt class="docutils literal"><span class="pre">cat</span></tt> を実装しましょう。
リスト7のように <tt class="docutils literal"><span class="pre">module</span></tt> 中に <tt class="docutils literal"><span class="pre">cat</span></tt> を書き入れ、
<tt class="docutils literal"><span class="pre">import</span></tt> を二つ書き込み、その下に <tt class="docutils literal"><span class="pre">cat</span></tt> 関数を実装します。</p>
<ul class="simple">
<li>リスト7: cat関数を実装</li>
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
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3$ cat FileTools.hs
module FileTools (
find,
ls,
cat
) where

import System.Directory
import System.IO.Error
import qualified Data.ByteString.Lazy.Char8 as B

cat :: FilePath -&gt; IO B.ByteString
cat file = catchIOError (B.readFile file) (\\e -&gt; return $ B.pack [])
（以下略）
</pre></div>
</td></tr></table></div>
<p>　この <tt class="docutils literal"><span class="pre">cat</span></tt> 関数が今回の山場になりそうなのでじっくり解説していきます。
まず、ファイルの中身は <tt class="docutils literal"><span class="pre">String</span></tt> でなくて
<tt class="docutils literal"><span class="pre">ByteString</span></tt> という型で出力します。
バイナリファイルを <tt class="docutils literal"><span class="pre">String</span></tt> で読み込むと、
エラーが出てしまうからです。
<tt class="docutils literal"><span class="pre">ByteString</span></tt> はC言語の配列に近いものと考えるとよいでしょう。
で、この型を使うにはモジュールをインポートしないといけません。
それをやっているのが10行目です。
この10行目も相当ややこしいです。
まず、 <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt> ですが、
これは <tt class="docutils literal"><span class="pre">ByteString</span></tt> を使うときの基本のモジュールです。
他にもいろいろありますが、これを指定します。
次に、 <tt class="docutils literal"><span class="pre">qualified</span> <span class="pre">なんとか</span> <span class="pre">as</span> <span class="pre">B</span></tt> ですが、
これは <tt class="docutils literal"><span class="pre">Data.ByteString.Lazy.Char8</span></tt>
の中で定義された関数には <tt class="docutils literal"><span class="pre">B.</span></tt>
と頭につけないと使えないですよという指定です。
13行目の <tt class="docutils literal"><span class="pre">readFile</span></tt> には <tt class="docutils literal"><span class="pre">B.</span></tt> がついていますね。
先ほど <tt class="docutils literal"><span class="pre">q1_3_5.hs</span></tt> から <tt class="docutils literal"><span class="pre">FileTools</span></tt>
を使ったときには <tt class="docutils literal"><span class="pre">qualified</span></tt> を指定しなかったので、
中に定義された <tt class="docutils literal"><span class="pre">find</span></tt> 関数はそのまま使えましたが、
<tt class="docutils literal"><span class="pre">qualified</span></tt> を使った方がどのモジュール由来の関数なのか
分かって良いという考え方もあります。</p>
<p>　 <tt class="docutils literal"><span class="pre">B.readFile</span></tt> の型を確認しておきます。
リスト5のようにそのまま <tt class="docutils literal"><span class="pre">import</span> <span class="pre">qualified</span> <span class="pre">...</span></tt>
と書いて読み込むとよいでしょう。</p>
<ul class="simple">
<li>リスト5: readFileの型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">ghci</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="k">qualified</span> <span class="nn">Data.ByteString.Lazy.Char8</span> <span class="k">as</span> <span class="n">B</span>
<span class="kt">Prelude</span> <span class="kt">B</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="kt">B</span><span class="o">.</span><span class="n">readFile</span>
<span class="kt">B</span><span class="o">.</span><span class="n">readFile</span> <span class="ow">::</span> <span class="kt">FilePath</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="kt">B</span><span class="o">.</span><span class="kt">ByteString</span>
</pre></div>
</td></tr></table></div>
<p>　さて、13行目にはもう一つややこしい <tt class="docutils literal"><span class="pre">catchIOError</span></tt>
という関数がいます。この関数を使うために、
9行目で <tt class="docutils literal"><span class="pre">System.IO.Error</span></tt>
というモジュールを読み込んでいます。</p>
<p>　 <tt class="docutils literal"><span class="pre">catchIOError</span></tt> は、例外処理のための関数です。
先に型を確認しておきましょう。リスト9のようになります。</p>
<ul class="simple">
<li>リスト9: catchIOErrorの型</li>
</ul>
<div class="highlight-hs"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nf">ueda</span><span class="o">@</span><span class="n">remote</span><span class="kt">:~/GIT</span><span class="o">/</span><span class="kt">UspMagazineHaskell</span><span class="o">/</span><span class="kt">Study1_Q3</span><span class="o">$</span> <span class="n">ghci</span>
<span class="kt">Prelude</span><span class="o">&gt;</span> <span class="kr">import</span> <span class="nn">System.IO.Error</span>
<span class="kt">Prelude</span> <span class="kt">System</span><span class="o">.</span><span class="kt">IO</span><span class="o">.</span><span class="kt">Error</span><span class="o">&gt;</span> <span class="kt">:</span><span class="n">t</span> <span class="n">catchIOError</span>
<span class="nf">catchIOError</span> <span class="ow">::</span> <span class="kt">IO</span> <span class="n">a</span> <span class="ow">-&gt;</span> <span class="p">(</span><span class="kt">IOError</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="n">a</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="kt">IO</span> <span class="n">a</span>
</pre></div>
</td></tr></table></div>
<p>ただ、これは実際に使い方を見た方が分かりやすくて、
リスト7の13行目を見ると、 <tt class="docutils literal"><span class="pre">catchIOError</span></tt> の引数に、
最初に実際にやりたい処理を書いて、
次に例外が発生したときの処理を書きます。
例外が発生したときの処理 <tt class="docutils literal"><span class="pre">\\e</span> <span class="pre">-&gt;</span> <span class="pre">return...</span></tt> は
先月号で出て来た無名関数です。
<tt class="docutils literal"><span class="pre">-&gt;</span></tt> の左側の <tt class="docutils literal"><span class="pre">e</span></tt> が入力、右側が出力です。
ただ、この無名関数では入力を使っておらず、
ただ空文字を返しているだけです。
つまり例外が発生したら空文字を返すという適当実装ですが、
この連載では問題が解ければよいのでこれで十分です。
<tt class="docutils literal"><span class="pre">B.pack</span></tt> の型は次の通りです。
<tt class="docutils literal"><span class="pre">cat</span></tt> の出力型は <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">B.ByteString</span></tt> なので、
<tt class="docutils literal"><span class="pre">return</span></tt> 関数で <tt class="docutils literal"><span class="pre">IO</span></tt> を <tt class="docutils literal"><span class="pre">B.pack</span></tt>
の出力にくっつけています。</p>
<ul class="simple">
<li>リスト10: packの型</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~<span class="nv">$ </span>ghci
Prelude&gt; import qualified Data.ByteString.Lazy.Char8 as B
Prelude B&gt; :t B.pack
B.pack :: <span class="o">[</span>Char<span class="o">]</span> -&gt; B.ByteString
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h2>7.5. シバンを検知<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、 <tt class="docutils literal"><span class="pre">cat</span></tt> が実装できましたので、
これを使ってbashスクリプトのファイルを見つけてみましょう。
リスト11のようなコードを書きました。</p>
<ul class="simple">
<li>リスト11: bashのシバンを発見するq1_3_6.hs</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>cat q1_3_6.hs
import FileTools
import qualified Data.ByteString.Lazy.Char8 as B

<span class="nv">main</span> <span class="o">=</span> find <span class="s2">&quot;/etc&quot;</span> &gt;&gt;<span class="o">=</span> mapM judgeBashFile &gt;&gt;<span class="o">=</span> print

judgeBashFile :: FilePath -&gt; IO <span class="o">(</span>String,Bool<span class="o">)</span>
judgeBashFile <span class="nv">file</span> <span class="o">=</span> cat file &gt;&gt;<span class="o">=</span> <span class="k">return</span> . <span class="o">((</span>,<span class="o">)</span> file<span class="o">)</span> . isBash
 where isBash <span class="nv">bs</span> <span class="o">=</span> B.take 11 <span class="nv">bs</span> <span class="o">==</span> B.pack <span class="s2">&quot;#!/bin/bash&quot;</span>
</pre></div>
</td></tr></table></div>
<p>実行してみます。リスト12のように、
bashのシバン
<a class="footnote-reference" href="#id19" id="id11">[6]</a>
のあるファイル名にはTrueがつきます。
ないものにはFalseがつきます。</p>
<ul class="simple">
<li>リスト12: q1_3_6の実行（と若干のシェル芸）</li>
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
13</pre></div></td><td class="code"><div class="highlight"><pre>ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_6 | tr <span class="s1">&#39;)&#39;</span> <span class="s1">&#39;\\n&#39;</span> | head -n 3
<span class="o">[(</span><span class="s2">&quot;/etc/blkid.tab&quot;</span>,False
,<span class="o">(</span><span class="s2">&quot;/etc/tidy.conf&quot;</span>,False
,<span class="o">(</span><span class="s2">&quot;/etc/logrotate.conf&quot;</span>,False
<span class="c">###どうやら4個bashのスクリプトが存在###</span>
ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>sudo ./q1_3_6 | tr <span class="s1">&#39;)&#39;</span> <span class="s1">&#39;\\n&#39;</span> | grep True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/fakeroot&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzfgrep&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzmore&quot;</span>,True
,<span class="o">(</span><span class="s2">&quot;/etc/alternatives/lzdiff&quot;</span>,True
<span class="c">###覗き見###</span>
ueda@remote:~/GIT/UspMagazineHaskell/Study1_Q3<span class="nv">$ </span>head -n 1 /etc/alternatives/fakeroot
<span class="c">#!/bin/bash</span>
</pre></div>
</td></tr></table></div>
<p>　リスト11を解説します。
まず9行目の <tt class="docutils literal"><span class="pre">isBash</span></tt> 関数ですが、これはファイルの中身がbashスクリプトかどうか
見分けるためのコアになる関数です。
<tt class="docutils literal"><span class="pre">==</span></tt> の右側がファイルの中身 <tt class="docutils literal"><span class="pre">bs</span></tt> から11バイト取り出す関数で、
右側がシバンです。 <tt class="docutils literal"><span class="pre">B.pack</span></tt> で型を <tt class="docutils literal"><span class="pre">B.ByteString</span></tt> に合わせています。
<tt class="docutils literal"><span class="pre">B.take</span></tt> ですが、ファイルの中身が11バイト未満の場合は、
ファイルの中身をそのまま返します。
<tt class="docutils literal"><span class="pre">isBash</span></tt> 関数のこの定義では、例えば <tt class="docutils literal"><span class="pre">#!/bin/bashx</span></tt>
というシバンがあったらこれもbashスクリプトと判定していしまいますが、
まあそんなもの無いからいいでしょう。手抜きですが。</p>
<p>　で、8行目が若干変態です。 <tt class="docutils literal"><span class="pre">(,)</span></tt> ですが、
実はこんな関数として扱われます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span>,<span class="o">)</span>
<span class="o">(</span>,<span class="o">)</span> :: a -&gt; b -&gt; <span class="o">(</span>a, b<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>つまり引数二つをとってタプルを返す関数という解釈になります。
実は、「 <tt class="docutils literal"><span class="pre">(a,b)</span></tt> 」と「 <tt class="docutils literal"><span class="pre">(,)</span> <span class="pre">a</span> <span class="pre">b</span></tt> 」
は同じものとして扱われているのです。
<tt class="docutils literal"><span class="pre">(,)</span> <span class="pre">file</span></tt> というのは、一つ引数をとって <tt class="docutils literal"><span class="pre">(file,)</span></tt>
となって欠けているタプルを完成させる関数という解釈ができます。
その欠けている引数は <tt class="docutils literal"><span class="pre">isBash</span></tt> の出力です。
で、 <tt class="docutils literal"><span class="pre">return</span></tt> は完成したタプルを引数にとって型の頭に
<tt class="docutils literal"><span class="pre">IO</span></tt> をつけて出力を完成させます。</p>
<p>　5行目の <tt class="docutils literal"><span class="pre">mapM</span></tt> は前回も出てきました。
ここでは <tt class="docutils literal"><span class="pre">IO</span> <span class="pre">[FilePath]</span></tt> という型の入力から <tt class="docutils literal"><span class="pre">IO</span></tt>
を取払い、リストに入った <tt class="docutils literal"><span class="pre">FilePath</span></tt> を一つずつ
<tt class="docutils literal"><span class="pre">judgeBashFile</span></tt> 関数に渡す役割をしています。</p>
</div>
<div class="section" id="id12">
<h2>7.6. おわりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて今回は第一回シェル芸勉強会の第三問の途中までとなりました。
前回もそうでしたが、やはりファイルを操作しだすと <tt class="docutils literal"><span class="pre">IO</span></tt>
だらけになって、なかなかややこしいコードになってしまいます。
こんなに苦労してファイルを扱うのが必要なのか、
という疑問もあります。
が、何でも厳密に扱おうとしたら
大変だということで納得し、
次回もHaskell道を逝くことにしましょう。</p>
</div>
<div class="section" id="id13">
<h2>7.7. お知らせ：コード募集<a class="headerlink" href="#id13" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　本稿で出た問題のHaskellのコードを、
名前あるいはハンドルネームと共に送ってください。
短いもの、あるいは変態的なものをお願いいたします。</p>
<p>email: 編集部のメールアドレス</p>
<p class="rubric">脚注</p>
<table class="docutils footnote" frame="void" id="id14" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>正確には、とれとれぴちぴちキダタロー。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id15" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[2]</a></td><td><a class="reference external" href="http://ja.wikipedia.org/wiki">http://ja.wikipedia.org/wiki</a>/パチンコガンダム駅</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id16" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id5">[3]</a></td><td>なんだそりゃ？</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id17" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id6">[4]</a></td><td>須藤。</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id18" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[5]</a></td><td>いいっすね。C++だと(ry</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id19" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id11">[6]</a></td><td>シバンっつーのは、シェルスクリプト等にある <tt class="docutils literal"><span class="pre">#!</span></tt> から始まるアレです。
スクリプトを解釈して実行するためのインタプリタを指定する仕組みです。
ま、我々はHaskell使いだから必要ないんですけどね（おい）。</td></tr>
</tbody>
</table>
</div>
</div>
