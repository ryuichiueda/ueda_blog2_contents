---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年10月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>22. 開眼シェルスクリプト 第22回 シェルでドキュメントを操る<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　皆様、今年の夏は暑かったでしょうか？
執筆時点で夏の入り口にいますが、
急に暑くなったので脳が溶けております。</p>
<p>　そんな季節の挨拶とは全く関係ありませんが、
今回、次回はメモ書きや原稿など、
不定形のテキストファイルのハンドリングを扱います。
今回はシェルスクリプトというよりは、
便利なコマンドの使い方を羅列していきます。</p>
<p>　ドキュメントを扱う方法は、筆者のようにテキストファイルで
html、reStructuredText、TeXを書く玄人気取りのやり方と、
表計算ソフトに方眼紙を作って書く
（脚注：ピンと来ない人は「エクセル方眼紙」で検索を）、
別の意味で玄人っぽい方法に二分されます。
いや、嘘です。ワープロソフトを使う人が多数派のような気がします。</p>
<p>　どの方法が良いかはその人に依るのですが、
おそらく、これらのやり方の違いが大きく増幅されるのは検索するときです。
基本、ワープロソフトや表計算ソフトに
テキストを書いておいて後から複数のファイルから文字を探すときは、
そのソフトのベンダが作った親切なツールを使う事になります。
しかし、ベンダの気まぐれで何が起こるか分からない怖い部分もあります。
一方、テキストファイルで持っていれば、ベンダの干渉を受けないでしょうが、
<tt class="docutils literal"><span class="pre">find</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> といったコマンドを使いこなす必要があります。</p>
<p>　この議論、やり出すとキリがないので、これ以上はやめておきます。
とにかく今回は、「テキストファイルならお手のもの」
とタイトルに書いてあるように、
テキストファイルを便利に使うスキルを上げないとね！
という立場で話を進めます。</p>
<p>　この連載の主張に呼応するように（嘘）、
国もこういう流れになってきたようです。</p>
<blockquote>
<div><p>(2) オープンデータ推進の意義
これまでも政府は、各府省のホームページ等を通じて保有するデータを公開して
きており、情報提供という観点では一定の成果が出ている。</p>
<p>ただ、これまでのホームページによる情報提供は、基本的に、人間が読む（画面
上で又は印刷して）という利用形態を念頭に置いた形で行われており、検索も難し
く、大量・多様なデータをコンピュータで高速に、横断的に又は組み合わせて処理・
利用することが難しい。</p>
<p>: 二次利用の促進のための府省のデータ公開に関する基本的考え方（ガイドライン）
（仮称）（案）より
<a class="reference external" href="http://www.kantei.go.jp/jp/singi/it2/densi/dai3/siryou6.pdf">http://www.kantei.go.jp/jp/singi/it2/densi/dai3/siryou6.pdf</a></p>
</div></blockquote>
<p>いつもと違ってお役所文章ですが、
これを格言代わりに本編に進みます。
余談ですが、これを引用したウェブの記事の一つに
「これを受けてデータはExcelで公開すべきだ。」
というものがあってひっくり返りました。そうじゃないでしょう・・・。
人が読むのは最終出力だけで原本はテキストで、
というのが大事だと筆者は考えています。</p>
<div class="section" id="id2">
<h2>22.1. 環境<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回もMacです。 <tt class="docutils literal"><span class="pre">gsed,</span> <span class="pre">gawk</span></tt>
のバージョンと共にリスト1にバージョンを示します。
コマンドの用例では <tt class="docutils literal"><span class="pre">gsed,</span> <span class="pre">gawk</span></tt> で統一してありますが、
Linuxの多くのディストリビューションでは、
<tt class="docutils literal"><span class="pre">gsed</span></tt> は <tt class="docutils literal"><span class="pre">sed</span></tt> 、 <tt class="docutils literal"><span class="pre">gawk</span></tt> は <tt class="docutils literal"><span class="pre">awk</span></tt> で大丈夫です。</p>
<ul class="simple">
<li>リスト1: 環境</li>
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
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64
uedamac:~ ueda<span class="nv">$ </span>gawk --version
GNU Awk 4.0.2
Copyright <span class="o">(</span>C<span class="o">)</span> 1989, 1991-2012 Free Software Foundation.
（以下略）
uedamac:~ ueda<span class="nv">$ </span>gsed --version
GNU sed version 4.2.1
Copyright <span class="o">(</span>C<span class="o">)</span> 2009 Free Software Foundation, Inc.
（以下略）
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id3">
<h2>22.2. 日本語原稿の文字数を数える<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まずは簡単なところから。
作文をしていて、何文字書いたか調べたいときがありますね。
え？無い？・・・あるということにしてください。</p>
<p>　例えば、リスト2のファイル <tt class="docutils literal"><span class="pre">mistery</span></tt>
内の文字数は、全角スペースを
入れてちょうど60文字です。</p>
<ul class="simple">
<li>リスト2: 例題ファイルその1</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery
　朝目覚めると、私は全身を繭で
覆われた蛹になっていたのです。
私は大変困ってしまいました。「
会社に休みの連絡ができない。」
</pre></div>
</td></tr></table></div>
<p>　こういうときは、リスト3のようにやります。</p>
<ul class="simple">
<li>リスト3: 文字数を数える</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | wc -m
 64
</pre></div>
</td></tr></table></div>
<p>リスト3のように、 <tt class="docutils literal"><span class="pre">wc</span></tt> にオプション <tt class="docutils literal"><span class="pre">-m</span></tt> をつけると、
今のロケールに合わせて文字数を数えてくれます。
ロケールを変えるとリスト4のように出力に違いが出ます。</p>
<ul class="simple">
<li>リスト4: ロケール（環境変数 <tt class="docutils literal"><span class="pre">LANG</span></tt> ）で挙動が変わる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span>
ja_JP.UTF-8
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | <span class="nv">LANG</span><span class="o">=</span>C wc -m
 184
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | <span class="nv">LANG</span><span class="o">=</span>ja_JP.UTF-8 wc -m
 64
</pre></div>
</td></tr></table></div>
<p>　しかし、これだと改行も記号も文字数に
カウントされてしまっています。
次のように <tt class="docutils literal"><span class="pre">tr</span></tt> や <tt class="docutils literal"><span class="pre">sed</span></tt>
で字を削っておくと正解が出るので、
正確に数えたいならこのようにします。</p>
<ul class="simple">
<li>リスト5: 文字数を正確に数える</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | tr -d <span class="s1">&#39;\\n&#39;</span> | wc -m
 60
<span class="c">#全角スペースも数えたくない場合</span>
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | tr -d <span class="s1">&#39;\\n&#39;</span> |
gsed <span class="s1">&#39;s/　//g&#39;</span> | wc -m
 59
</pre></div>
</td></tr></table></div>
<p>　もう1,2数え方をリスト6に紹介しておきます。
<tt class="docutils literal"><span class="pre">gsed</span></tt> を使う方法は、私の手癖になっているものです。
<tt class="docutils literal"><span class="pre">gawk</span></tt> の方法は、ロケールが日本語でも
AWKのコマンドの種類によっては
バイト数になってしまうので注意が必要です。</p>
<ul class="simple">
<li>リスト6: 文字数を正確に数える</li>
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
14</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |
wc -l
 64
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |
gawk <span class="s1">&#39;NF!=0&#39;</span> | wc -l
 60
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery |
gawk <span class="s1">&#39;{a+=length($0)}END{print a}&#39;</span>
60
<span class="c">#Mac等ではgawkを明示的に指定しないと</span>
<span class="c">#このようになってしまうので注意</span>
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery |
awk <span class="s1">&#39;{a+=length($0)}END{print a}&#39;</span>
180
</pre></div>
</td></tr></table></div>
<p>　もっと長い文章について、
どれだけ書いたかざっくり知りたい場合は、
バイト数で考えてもよいでしょう。
例えば筆者はこの原稿を毎月6ページずつ書くのですが、
他の月と比較してどれだけ書いたか、
<tt class="docutils literal"><span class="pre">wc</span></tt> コマンドでリスト7のように調査しています。</p>
<ul class="simple">
<li>リスト7: どれだけ書いたかバイト数や行数でざっくり調べる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>wc 201???.rst
 549 803 24653 201201.rst
 428 1064 19469 201202.rst
 （中略）
 514 945 20703 201307.rst
 554 948 18805 201308.rst
 482 905 20520 201309.rst
 165 314 6616 201310.rst
 11016 21368 448677 total
</pre></div>
</td></tr></table></div>
<p>・・・あと4ページくらい書かなければ原稿料を頂けないようです。
これでバイトあたりの原稿料が計算できますが、
雑念が入るので計算しないでおきます。</p>
</div>
<div class="section" id="id4">
<h2>22.3. 文章の抜き出し<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次に扱うのは、テキストファイルの一部分を抜き出すテクニックです。
例えば、次のような連絡先メモがあるとします。</p>
<ul class="simple">
<li>リスト8: 例題ファイルその2</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>cat address
&lt;幹事会&gt;

- 鎌田
 - 略称: <span class="o">(</span>鎌<span class="o">)</span>
 - TEL: 090-1234-xxxx
 - email: kama@kama.gov

- 濱田
 - 略称: <span class="o">(</span>ハ<span class="o">)</span>
 - TEL: 080-5678-xxxx
 - email: ha@haisyou.ac.jp
</pre></div>
</td></tr></table></div>
<p>　例えば濱田さんの電話番号が知りたいとします。
このようなとき、普通に <tt class="docutils literal"><span class="pre">grep</span></tt> を使おうとしても、</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 濱田 address
- 濱田
</pre></div>
</div>
<p>という残念な目にあったことのある人もいると思います。</p>
<p>　実は、 <tt class="docutils literal"><span class="pre">grep</span></tt> には <tt class="docutils literal"><span class="pre">-A</span></tt> というオプションがあります。
これを使うとリスト9のように、
検索で引っかかった行の後ろも出力してくれます。
これでいちいち <tt class="docutils literal"><span class="pre">less</span></tt> を使ったりエディタ開いたりしなくて済みます。
<tt class="docutils literal"><span class="pre">less</span></tt> を使うのはそこまで面倒くさがることでもないですが・・・。</p>
<ul class="simple">
<li>リスト9: <tt class="docutils literal"><span class="pre">grep</span></tt> の <tt class="docutils literal"><span class="pre">-A</span></tt> オプション</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 濱田 -A 3 address
- 濱田
 - 略称: <span class="o">(</span>ハ<span class="o">)</span>
 - TEL: 080-5678-xxxx
 - email: ha@haisyou.ac.jp
</pre></div>
</td></tr></table></div>
<p>　逆に、電話番号から人の名前を検索してみましょう。
リスト10のようにします。</p>
<ul class="simple">
<li>リスト10: <tt class="docutils literal"><span class="pre">grep</span></tt> の <tt class="docutils literal"><span class="pre">-B</span></tt> オプション</li>
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
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 080-5678-xxxx -B 2 address
- 濱田
 - 略称: <span class="o">(</span>ハ<span class="o">)</span>
 - TEL: 080-5678-xxxx
<span class="c">#補足：-Aと-Bを併用することも可能</span>
uedamac:201310 ueda<span class="nv">$ </span>grep 080-5678-xxxx -B 2 -A 1 address
- 濱田
 - 略称: <span class="o">(</span>ハ<span class="o">)</span>
 - TEL: 080-5678-xxxx
 - email: ha@haisyou.ac.jp
</pre></div>
</td></tr></table></div>
<p>　次はHTMLファイルを扱ってみましょう。
HTMLから狙ったところをワンライナーで切り出してみましょう。
これから扱うような処理は、
ブラウザでソースを表示してマウスでコピペでもよいのですが、
何十、何百も同じ処理を繰り返すことになったらそうもいきません。</p>
<p>　まず、筆者のブログからコードの部分だけ切り取るということをやってみます。
2013年7月14日現在で、筆者のブログのトップページにはいくつかコードが
掲載されているのですが、コードはHTML上で <tt class="docutils literal"><span class="pre">&lt;pre&gt;</span></tt> と
<tt class="docutils literal"><span class="pre">&lt;/pre&gt;</span></tt> に囲まれています。
リスト11のリストのように <tt class="docutils literal"><span class="pre">curl</span></tt> コマンドでHTMLを取得して
<tt class="docutils literal"><span class="pre">less</span></tt> で読んでみましょう。
このような部分がいくつか出現します。</p>
<ul class="simple">
<li>リスト11: 例題のHTML</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>curl  | less
（略）
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;
Python 2.7.2 <span class="o">(</span>default, Oct 11 2012, 20:14:37<span class="o">)</span>
（略）
&amp;gt;&amp;gt;&amp;gt; round<span class="o">(</span>-1.1,-1<span class="o">)</span>*1.0
-0.0
&lt;/pre&gt;
（略）
</pre></div>
</td></tr></table></div>
<p>　このような抽出は <tt class="docutils literal"><span class="pre">sed</span></tt> の得意技で、
リスト12のようにコマンドを書けばコード
（pre要素）だけ抽出することができます。</p>
<ul class="simple">
<li>リスト12: コードだけ取り出す</li>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>...
uedamac:~ ueda<span class="nv">$ </span>curl  2&gt; /dev/null |
nkf -wLux | gsed -n <span class="s1">&#39;/&lt;pre/,/&lt;\\/pre/p&#39;</span> &gt; ans
uedamac:~ ueda<span class="nv">$ </span>less ans
（略）
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;
Python 2.7.2 <span class="o">(</span>default, Oct 11 2012, 20:14:37<span class="o">)</span>
（略）
&lt;/pre&gt;
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;
uedamac:~ ueda<span class="nv">$ </span>cat hoge.sh
<span class="c">#!/bin/bash -xv</span>
（略）
&lt;/pre&gt;
...
</pre></div>
</td></tr></table></div>
<p>　ここでのポイントは、 <tt class="docutils literal"><span class="pre">sed</span></tt> の使い方と、
<tt class="docutils literal"><span class="pre">curl</span></tt> したらすぐに <tt class="docutils literal"><span class="pre">nkf</span></tt> をすることの2点でしょう。</p>
<p>　 <tt class="docutils literal"><span class="pre">sed</span></tt> については、
本連載では文字列の置換で使うことがほとんどですが、
<tt class="docutils literal"><span class="pre">/&lt;正規表現1&gt;/,/&lt;正規表現2/p</span></tt> （pコマンド）で、
正規表現1にマッチする行から正規表現2
にマッチする行まで抜き出すことができます。
この処理は正規表現2のマッチが終わると再度実行されるので、
上の例ではいくつもpre要素を抜き出す事ができています。
オプション <tt class="docutils literal"><span class="pre">-n</span></tt> は、 <tt class="docutils literal"><span class="pre">sed</span></tt> はデフォルトで全行を出力するので、
それを抑制するために使います。
<tt class="docutils literal"><span class="pre">-n</span></tt> をつけておかないと、pコマンドの出力対象行が2行ずつ、
その他の行が1行ずつ出力されてしまいます。</p>
<p>　 <tt class="docutils literal"><span class="pre">curl</span></tt> の出力は、例え読み取ったHTMLがUTF-8
で書いてあっても改行コードが
UNIX標準のものと違っている可能性があるので、
このようなときは必ず通します。
オプションは <tt class="docutils literal"><span class="pre">-wLux</span></tt> が私の場合は手癖になっており、</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">w</span></tt> : UTF-8に変換</li>
<li><tt class="docutils literal"><span class="pre">Lu</span></tt> : 改行コードをLF（0x0a）に</li>
<li><tt class="docutils literal"><span class="pre">x</span></tt> : 半角カナから全角カナへの変換を抑制</li>
</ul>
<p>という意味があります。</p>
<p>　ただ、このようにHTMLがきれいに
改行されていればあまり苦労もないのですが、
実際はそうもいきません。
リスト13のようなHTMLもあるでしょう。</p>
<ul class="simple">
<li>リスト13: 例題ファイルその3</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>cat kitanai.html
&lt;pre&gt;#!/bin/bash

<span class="nb">echo</span> <span class="s2">&quot;きたない&quot;</span>&lt;/pre&gt;あははは&lt;pre&gt;
<span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="s2">&quot;きたなすぎる&quot;</span>
&lt;/pre&gt;
</pre></div>
</td></tr></table></div>
<p>こういうときは、リスト14のように自分で掃除するしかありません。
このsedのワンライナーはお世辞にもきれいとは言えないので、
ちゃんとプログラムを書いた方がいいかもしれません。
ただ、結局この方が早いことが多いです。</p>
<ul class="simple">
<li>リスト14: きたないHTMLを掃除するワンライナー</li>
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
20</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>cat kitanai.html |
<span class="c">#&lt;pre&gt;の後に何か文字があると改行を差し込む</span>
gsed <span class="s1">&#39;s;\\(&lt;pre[^&gt;]*&gt;\\)\\(..*\\);\\1\\n\\2;g&#39;</span> |
<span class="c">#&lt;pre&gt;の前に何か文字があると改行を差し込む</span>
gsed <span class="s1">&#39;s;\\(..*\\)\\(&lt;pre[^&gt;]*&gt;\\);\\1\\n\\2;g&#39;</span> |
<span class="c">#&lt;/pre&gt;の前に何か文字があると改行を差し込む</span>
gsed <span class="s1">&#39;s;\\(..*\\)&lt;/pre&gt;;\\1\\n&lt;/pre&gt;;g&#39;</span> |
<span class="c">#&lt;/pre&gt;の後に何か文字があると改行を差し込む</span>
gsed <span class="s1">&#39;s;&lt;/pre&gt;\\(..*\\);&lt;/pre&gt;\\n\\1;g&#39;</span>
&lt;pre&gt;
<span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="s2">&quot;きたない&quot;</span>
&lt;/pre&gt;
あははは
&lt;pre&gt;
<span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="s2">&quot;きたなすぎる&quot;</span>
&lt;/pre&gt;
</pre></div>
</td></tr></table></div>
<p>　この例題の最後に便利な小ネタを。
さきほどpreで抜き出したHTMLには</p>
<div class="highlight-bash"><div class="highlight"><pre>&amp;gt;&amp;gt;&amp;gt; round<span class="o">(</span>-1.1,-1<span class="o">)</span>
</pre></div>
</div>
<p>などと、記号の一部が文字実体参照に変換されています。
例えば <tt class="docutils literal"><span class="pre">&amp;gt;</span></tt> は <tt class="docutils literal"><span class="pre">&gt;</span></tt> が置き換わったものです。</p>
<p>　また、次のように数値参照になっているときもあります。</p>
<div class="highlight-bash"><div class="highlight"><pre>&amp;#x4e0a;&amp;#x7530;&amp;#x53c2;&amp;#x4e0a;
</pre></div>
</div>
<p>HTMLから抜き出して来たら、
このままにするより元に戻した方がよいでしょう。</p>
<p>　数値参照の方はリスト15のように <tt class="docutils literal"><span class="pre">nkf</span></tt> でできます。</p>
<ul class="simple">
<li>リスト15: 数値参照を <tt class="docutils literal"><span class="pre">nkf</span></tt> でデコードする</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;&amp;#x4e0a;&amp;#x7530;&amp;#x53c2;&amp;#x4e0a;&#39;</span> |
nkf --numchar-input
上田参上
</pre></div>
</td></tr></table></div>
<p>　文字実体参照の方は <tt class="docutils literal"><span class="pre">nkf</span></tt> でできません。残念。
しかし、 <tt class="docutils literal"><span class="pre">&quot;&amp;&lt;&gt;</span></tt> とスペース程度ならあまり個数がないので
リスト16のようにsedスクリプトを書くとよいでしょう。
コマンド化してもいいですね。</p>
<ul class="simple">
<li>リスト16: 文字実体参照を置換するsedスクリプトを作って使う</li>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>#このようなsedスクリプトを作る
uedamac:~ ueda$ cat ref.sed
s/&amp;lt;/&lt;/g
s/&amp;gt;/&gt;/g
s/&amp;quot;/&quot;/g
s/&amp;amp;/\\&amp;/g
s/&amp;nbsp;/ /g
uedamac:~ ueda$ curl  2&gt; /dev/null |
sed -n &#39;/&lt;pre/,/&lt;\\/pre/p&#39; | gsed -n &#39;1,/&lt;\\/pre/p&#39; |
sed -f ./ref.sed
&lt;pre class=&quot;brush: bash; title: ; notranslate&quot; title=&quot;&quot;&gt;
（略）
&gt;&gt;&gt; round(-1.1,-1)*1.0
-0.0
&lt;/pre&gt;
</pre></div>
</td></tr></table></div>
<p>　他の文字実体参照も変換しなければならないときは、
他の言語のライブラリを使って
変換コマンドを書くのが一番簡単な方法です。
・・・しかし、皆さんには文字実体参照の一覧を掲載した
ウェブサイトからtableを抜き出し、
<tt class="docutils literal"><span class="pre">ref.sed</span></tt> のようなスクリプトを
ワンライナーで作ることをおすすめしておきます。</p>
</div>
<div class="section" id="find-grep-xargs">
<h2>22.4. find, grep, xargsの組み合わせ<a class="headerlink" href="#find-grep-xargs" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　最後にファイルの検索をやってみます。
ディレクトリの中から何かテキストを探すときは、
<tt class="docutils literal"><span class="pre">find</span></tt> と <tt class="docutils literal"><span class="pre">xargs</span></tt>
を組み合わせると自由自在な感じになります。</p>
<p>　 <tt class="docutils literal"><span class="pre">find</span></tt> については、
名前で誤解を受けやすいのですが、
単に指定したディレクトリの下のファイルや
ディレクトリを延々と出力するだけです。
<tt class="docutils literal"><span class="pre">find</span></tt> はオプションが多い事でも知られていますが、
リスト17のような使い方だけ知っておけばよいと思います。
オプションの <tt class="docutils literal"><span class="pre">.</span></tt> はカレントディレクトリ、
<tt class="docutils literal"><span class="pre">-type</span> <span class="pre">f</span></tt> はファイルだけ表示しろということです。</p>
<ul class="simple">
<li>リスト17: <tt class="docutils literal"><span class="pre">find</span></tt> を使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>find . -type f | head -n 4
./.201203.rst.swp
./.201310.rst.swp
./.DS_Store
./.git/COMMIT_EDITMSG
</pre></div>
</td></tr></table></div>
<p>　出力は1レコード1ファイルorディレクトリと、
UNIXの教科書通りなので、
ファイル名で検索するときはパイプで <tt class="docutils literal"><span class="pre">grep</span></tt>
をつなげばよいということになります。</p>
<p>　例えば、ミーティング中にとっさにとったメモ
をどこに保存したか忘れたが、何を書いたかはうっすら覚えている場合、
（そしてメモを取るときは必ずファイル名に
<tt class="docutils literal"><span class="pre">memo</span></tt> か <tt class="docutils literal"><span class="pre">MEMO</span></tt> を入れている場合、）
リスト18のようなワンライナーで探し出すことができます。</p>
<ul class="simple">
<li>リスト18: <tt class="docutils literal"><span class="pre">find</span></tt> と <tt class="docutils literal"><span class="pre">grep</span></tt> 、 <tt class="docutils literal"><span class="pre">xargs</span></tt> を組み合わせる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>find ~ -type f | fgrep -v <span class="s2">&quot;/.&quot;</span> | grep -i memo | xargs grep 徹夜 | gsed <span class="s1">&#39;s/:.*//&#39;</span> &gt; hoge
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat hoge
/Users/ueda/Dropbox/USP/memo/memo
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat hoge | xargs cat
徹夜で仕事しろと言われた（このメモはフィクションです。）
</pre></div>
</td></tr></table></div>
<p>　これが自在にできれば、
某OSで検索のときに出て来る犬に頼る必要はありません。
<tt class="docutils literal"><span class="pre">find</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> で検索をかけるときによく使うイディオムを挙げておきます。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">find</span> <span class="pre">.</span> <span class="pre">|</span> <span class="pre">grep</span> <span class="pre">hoge</span></tt> : ファイル名の検索</li>
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span></tt> : ディレクトリ下の全ファイルの中身を検索</li>
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span> <span class="pre">|</span> <span class="pre">gsed</span> <span class="pre">'s/:.*/'</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> : ディレクトリ下の全ファイルの中身を検索し、ファイル名のリストを抽出</li>
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span> <span class="pre">|</span> <span class="pre">gsed</span> <span class="pre">'s/:.*/'</span> <span class="pre">|</span> <span class="pre">uniq</span> <span class="pre">|</span> <span class="pre">xargs</span> <span class="pre">cat</span></tt> : ディレクトリ下の全ファイルの中身を検索し、ファイル名のリストを抽出し、抽出したファイルの中身を表示</li>
</ul>
</div>
<div class="section" id="id5">
<h2>22.5. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はテキストファイルをハンドリングする
ノウハウをいくつか紹介しました。
この手のノウハウは無数にあり、ほんの一部分を
つまみ食いでだらだら紹介してしまった感もありますが、
CUIで自分の文章を管理するときに実際にどんな
コマンドの使い方をしているのか、
雰囲気くらいはお伝えできたかと思います。</p>
<p>　次回は表記揺れに的をしぼって、何か作り物をしてみる予定です。
表記ゆれのテストスクリプトを書きます。
原稿書きもテストファーストの時代へ・・・（大げさ）</p>
</div>
</div>


