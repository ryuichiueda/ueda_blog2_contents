---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年10月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>22. 開眼シェルスクリプト 第22回 シェルでドキュメントを操る<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　皆様、今年の夏は暑かったでしょうか？<br />
執筆時点で夏の入り口にいますが、<br />
急に暑くなったので脳が溶けております。</p><br />
<p>　そんな季節の挨拶とは全く関係ありませんが、<br />
今回、次回はメモ書きや原稿など、<br />
不定形のテキストファイルのハンドリングを扱います。<br />
今回はシェルスクリプトというよりは、<br />
便利なコマンドの使い方を羅列していきます。</p><br />
<p>　ドキュメントを扱う方法は、筆者のようにテキストファイルで<br />
html、reStructuredText、TeXを書く玄人気取りのやり方と、<br />
表計算ソフトに方眼紙を作って書く<br />
（脚注：ピンと来ない人は「エクセル方眼紙」で検索を）、<br />
別の意味で玄人っぽい方法に二分されます。<br />
いや、嘘です。ワープロソフトを使う人が多数派のような気がします。</p><br />
<p>　どの方法が良いかはその人に依るのですが、<br />
おそらく、これらのやり方の違いが大きく増幅されるのは検索するときです。<br />
基本、ワープロソフトや表計算ソフトに<br />
テキストを書いておいて後から複数のファイルから文字を探すときは、<br />
そのソフトのベンダが作った親切なツールを使う事になります。<br />
しかし、ベンダの気まぐれで何が起こるか分からない怖い部分もあります。<br />
一方、テキストファイルで持っていれば、ベンダの干渉を受けないでしょうが、<br />
<tt class="docutils literal"><span class="pre">find</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> といったコマンドを使いこなす必要があります。</p><br />
<p>　この議論、やり出すとキリがないので、これ以上はやめておきます。<br />
とにかく今回は、「テキストファイルならお手のもの」<br />
とタイトルに書いてあるように、<br />
テキストファイルを便利に使うスキルを上げないとね！<br />
という立場で話を進めます。</p><br />
<p>　この連載の主張に呼応するように（嘘）、<br />
国もこういう流れになってきたようです。</p><br />
<blockquote><br />
<div><p>(2) オープンデータ推進の意義<br />
これまでも政府は、各府省のホームページ等を通じて保有するデータを公開して<br />
きており、情報提供という観点では一定の成果が出ている。</p><br />
<p>ただ、これまでのホームページによる情報提供は、基本的に、人間が読む（画面<br />
上で又は印刷して）という利用形態を念頭に置いた形で行われており、検索も難し<br />
く、大量・多様なデータをコンピュータで高速に、横断的に又は組み合わせて処理・<br />
利用することが難しい。</p><br />
<p>: 二次利用の促進のための府省のデータ公開に関する基本的考え方（ガイドライン）<br />
（仮称）（案）より<br />
<a class="reference external" href="http://www.kantei.go.jp/jp/singi/it2/densi/dai3/siryou6.pdf">http://www.kantei.go.jp/jp/singi/it2/densi/dai3/siryou6.pdf</a></p><br />
</div></blockquote><br />
<p>いつもと違ってお役所文章ですが、<br />
これを格言代わりに本編に進みます。<br />
余談ですが、これを引用したウェブの記事の一つに<br />
「これを受けてデータはExcelで公開すべきだ。」<br />
というものがあってひっくり返りました。そうじゃないでしょう・・・。<br />
人が読むのは最終出力だけで原本はテキストで、<br />
というのが大事だと筆者は考えています。</p><br />
<div class="section" id="id2"><br />
<h2>22.1. 環境<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回もMacです。 <tt class="docutils literal"><span class="pre">gsed,</span> <span class="pre">gawk</span></tt><br />
のバージョンと共にリスト1にバージョンを示します。<br />
コマンドの用例では <tt class="docutils literal"><span class="pre">gsed,</span> <span class="pre">gawk</span></tt> で統一してありますが、<br />
Linuxの多くのディストリビューションでは、<br />
<tt class="docutils literal"><span class="pre">gsed</span></tt> は <tt class="docutils literal"><span class="pre">sed</span></tt> 、 <tt class="docutils literal"><span class="pre">gawk</span></tt> は <tt class="docutils literal"><span class="pre">awk</span></tt> で大丈夫です。</p><br />
<ul class="simple"><br />
<li>リスト1: 環境</li><br />
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
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64<br />
uedamac:~ ueda<span class="nv">$ </span>gawk --version<br />
GNU Awk 4.0.2<br />
Copyright <span class="o">(</span>C<span class="o">)</span> 1989, 1991-2012 Free Software Foundation.<br />
（以下略）<br />
uedamac:~ ueda<span class="nv">$ </span>gsed --version<br />
GNU sed version 4.2.1<br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2009 Free Software Foundation, Inc.<br />
（以下略）<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id3"><br />
<h2>22.2. 日本語原稿の文字数を数える<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まずは簡単なところから。<br />
作文をしていて、何文字書いたか調べたいときがありますね。<br />
え？無い？・・・あるということにしてください。</p><br />
<p>　例えば、リスト2のファイル <tt class="docutils literal"><span class="pre">mistery</span></tt><br />
内の文字数は、全角スペースを<br />
入れてちょうど60文字です。</p><br />
<ul class="simple"><br />
<li>リスト2: 例題ファイルその1</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery<br />
　朝目覚めると、私は全身を繭で<br />
覆われた蛹になっていたのです。<br />
私は大変困ってしまいました。「<br />
会社に休みの連絡ができない。」<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　こういうときは、リスト3のようにやります。</p><br />
<ul class="simple"><br />
<li>リスト3: 文字数を数える</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | wc -m<br />
 64<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト3のように、 <tt class="docutils literal"><span class="pre">wc</span></tt> にオプション <tt class="docutils literal"><span class="pre">-m</span></tt> をつけると、<br />
今のロケールに合わせて文字数を数えてくれます。<br />
ロケールを変えるとリスト4のように出力に違いが出ます。</p><br />
<ul class="simple"><br />
<li>リスト4: ロケール（環境変数 <tt class="docutils literal"><span class="pre">LANG</span></tt> ）で挙動が変わる</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span><br />
ja_JP.UTF-8<br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | <span class="nv">LANG</span><span class="o">=</span>C wc -m<br />
 184<br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | <span class="nv">LANG</span><span class="o">=</span>ja_JP.UTF-8 wc -m<br />
 64<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　しかし、これだと改行も記号も文字数に<br />
カウントされてしまっています。<br />
次のように <tt class="docutils literal"><span class="pre">tr</span></tt> や <tt class="docutils literal"><span class="pre">sed</span></tt><br />
で字を削っておくと正解が出るので、<br />
正確に数えたいならこのようにします。</p><br />
<ul class="simple"><br />
<li>リスト5: 文字数を正確に数える</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | tr -d <span class="s1">&#39;\\n&#39;</span> | wc -m<br />
 60<br />
<span class="c">#全角スペースも数えたくない場合</span><br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | tr -d <span class="s1">&#39;\\n&#39;</span> |<br />
gsed <span class="s1">&#39;s/　//g&#39;</span> | wc -m<br />
 59<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もう1,2数え方をリスト6に紹介しておきます。<br />
<tt class="docutils literal"><span class="pre">gsed</span></tt> を使う方法は、私の手癖になっているものです。<br />
<tt class="docutils literal"><span class="pre">gawk</span></tt> の方法は、ロケールが日本語でも<br />
AWKのコマンドの種類によっては<br />
バイト数になってしまうので注意が必要です。</p><br />
<ul class="simple"><br />
<li>リスト6: 文字数を正確に数える</li><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |<br />
wc -l<br />
 64<br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |<br />
gawk <span class="s1">&#39;NF!=0&#39;</span> | wc -l<br />
 60<br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery |<br />
gawk <span class="s1">&#39;{a+=length($0)}END{print a}&#39;</span><br />
60<br />
<span class="c">#Mac等ではgawkを明示的に指定しないと</span><br />
<span class="c">#このようになってしまうので注意</span><br />
uedamac:MEMO ueda<span class="nv">$ </span>cat mistery |<br />
awk <span class="s1">&#39;{a+=length($0)}END{print a}&#39;</span><br />
180<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もっと長い文章について、<br />
どれだけ書いたかざっくり知りたい場合は、<br />
バイト数で考えてもよいでしょう。<br />
例えば筆者はこの原稿を毎月6ページずつ書くのですが、<br />
他の月と比較してどれだけ書いたか、<br />
<tt class="docutils literal"><span class="pre">wc</span></tt> コマンドでリスト7のように調査しています。</p><br />
<ul class="simple"><br />
<li>リスト7: どれだけ書いたかバイト数や行数でざっくり調べる</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>wc 201???.rst<br />
 549 803 24653 201201.rst<br />
 428 1064 19469 201202.rst<br />
 （中略）<br />
 514 945 20703 201307.rst<br />
 554 948 18805 201308.rst<br />
 482 905 20520 201309.rst<br />
 165 314 6616 201310.rst<br />
 11016 21368 448677 total<br />
</pre></div><br />
</td></tr></table></div><br />
<p>・・・あと4ページくらい書かなければ原稿料を頂けないようです。<br />
これでバイトあたりの原稿料が計算できますが、<br />
雑念が入るので計算しないでおきます。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>22.3. 文章の抜き出し<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次に扱うのは、テキストファイルの一部分を抜き出すテクニックです。<br />
例えば、次のような連絡先メモがあるとします。</p><br />
<ul class="simple"><br />
<li>リスト8: 例題ファイルその2</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>cat address<br />
&lt;幹事会&gt;<br />
<br />
- 鎌田<br />
 - 略称: <span class="o">(</span>鎌<span class="o">)</span><br />
 - TEL: 090-1234-xxxx<br />
 - email: kama\@kama.gov<br />
<br />
- 濱田<br />
 - 略称: <span class="o">(</span>ハ<span class="o">)</span><br />
 - TEL: 080-5678-xxxx<br />
 - email: ha\@haisyou.ac.jp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　例えば濱田さんの電話番号が知りたいとします。<br />
このようなとき、普通に <tt class="docutils literal"><span class="pre">grep</span></tt> を使おうとしても、</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 濱田 address<br />
- 濱田<br />
</pre></div><br />
</div><br />
<p>という残念な目にあったことのある人もいると思います。</p><br />
<p>　実は、 <tt class="docutils literal"><span class="pre">grep</span></tt> には <tt class="docutils literal"><span class="pre">-A</span></tt> というオプションがあります。<br />
これを使うとリスト9のように、<br />
検索で引っかかった行の後ろも出力してくれます。<br />
これでいちいち <tt class="docutils literal"><span class="pre">less</span></tt> を使ったりエディタ開いたりしなくて済みます。<br />
<tt class="docutils literal"><span class="pre">less</span></tt> を使うのはそこまで面倒くさがることでもないですが・・・。</p><br />
<ul class="simple"><br />
<li>リスト9: <tt class="docutils literal"><span class="pre">grep</span></tt> の <tt class="docutils literal"><span class="pre">-A</span></tt> オプション</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 濱田 -A 3 address<br />
- 濱田<br />
 - 略称: <span class="o">(</span>ハ<span class="o">)</span><br />
 - TEL: 080-5678-xxxx<br />
 - email: ha\@haisyou.ac.jp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　逆に、電話番号から人の名前を検索してみましょう。<br />
リスト10のようにします。</p><br />
<ul class="simple"><br />
<li>リスト10: <tt class="docutils literal"><span class="pre">grep</span></tt> の <tt class="docutils literal"><span class="pre">-B</span></tt> オプション</li><br />
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
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>grep 080-5678-xxxx -B 2 address<br />
- 濱田<br />
 - 略称: <span class="o">(</span>ハ<span class="o">)</span><br />
 - TEL: 080-5678-xxxx<br />
<span class="c">#補足：-Aと-Bを併用することも可能</span><br />
uedamac:201310 ueda<span class="nv">$ </span>grep 080-5678-xxxx -B 2 -A 1 address<br />
- 濱田<br />
 - 略称: <span class="o">(</span>ハ<span class="o">)</span><br />
 - TEL: 080-5678-xxxx<br />
 - email: ha\@haisyou.ac.jp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次はHTMLファイルを扱ってみましょう。<br />
HTMLから狙ったところをワンライナーで切り出してみましょう。<br />
これから扱うような処理は、<br />
ブラウザでソースを表示してマウスでコピペでもよいのですが、<br />
何十、何百も同じ処理を繰り返すことになったらそうもいきません。</p><br />
<p>　まず、筆者のブログからコードの部分だけ切り取るということをやってみます。<br />
2013年7月14日現在で、筆者のブログのトップページにはいくつかコードが<br />
掲載されているのですが、コードはHTML上で <tt class="docutils literal"><span class="pre">&lt;pre&gt;</span></tt> と<br />
<tt class="docutils literal"><span class="pre">&lt;/pre&gt;</span></tt> に囲まれています。<br />
リスト11のリストのように <tt class="docutils literal"><span class="pre">curl</span></tt> コマンドでHTMLを取得して<br />
<tt class="docutils literal"><span class="pre">less</span></tt> で読んでみましょう。<br />
このような部分がいくつか出現します。</p><br />
<ul class="simple"><br />
<li>リスト11: 例題のHTML</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>curl http://blog.ueda.asia | less<br />
（略）<br />
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;<br />
Python 2.7.2 <span class="o">(</span>default, Oct 11 2012, 20:14:37<span class="o">)</span><br />
（略）<br />
&amp;gt;&amp;gt;&amp;gt; round<span class="o">(</span>-1.1,-1<span class="o">)</span>*1.0<br />
-0.0<br />
&lt;/pre&gt;<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このような抽出は <tt class="docutils literal"><span class="pre">sed</span></tt> の得意技で、<br />
リスト12のようにコマンドを書けばコード<br />
（pre要素）だけ抽出することができます。</p><br />
<ul class="simple"><br />
<li>リスト12: コードだけ取り出す</li><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>...<br />
uedamac:~ ueda<span class="nv">$ </span>curl http://blog.ueda.asia 2&gt; /dev/null |<br />
nkf -wLux | gsed -n <span class="s1">&#39;/&lt;pre/,/&lt;\\/pre/p&#39;</span> &gt; ans<br />
uedamac:~ ueda<span class="nv">$ </span>less ans<br />
（略）<br />
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;<br />
Python 2.7.2 <span class="o">(</span>default, Oct 11 2012, 20:14:37<span class="o">)</span><br />
（略）<br />
&lt;/pre&gt;<br />
&lt;pre <span class="nv">class</span><span class="o">=</span><span class="s2">&quot;brush: bash; title: ; notranslate&quot;</span> <span class="nv">title</span><span class="o">=</span><span class="s2">&quot;&quot;</span>&gt;<br />
uedamac:~ ueda<span class="nv">$ </span>cat hoge.sh<br />
<span class="c">#!/bin/bash -xv</span><br />
（略）<br />
&lt;/pre&gt;<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ここでのポイントは、 <tt class="docutils literal"><span class="pre">sed</span></tt> の使い方と、<br />
<tt class="docutils literal"><span class="pre">curl</span></tt> したらすぐに <tt class="docutils literal"><span class="pre">nkf</span></tt> をすることの2点でしょう。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">sed</span></tt> については、<br />
本連載では文字列の置換で使うことがほとんどですが、<br />
<tt class="docutils literal"><span class="pre">/&lt;正規表現1&gt;/,/&lt;正規表現2/p</span></tt> （pコマンド）で、<br />
正規表現1にマッチする行から正規表現2<br />
にマッチする行まで抜き出すことができます。<br />
この処理は正規表現2のマッチが終わると再度実行されるので、<br />
上の例ではいくつもpre要素を抜き出す事ができています。<br />
オプション <tt class="docutils literal"><span class="pre">-n</span></tt> は、 <tt class="docutils literal"><span class="pre">sed</span></tt> はデフォルトで全行を出力するので、<br />
それを抑制するために使います。<br />
<tt class="docutils literal"><span class="pre">-n</span></tt> をつけておかないと、pコマンドの出力対象行が2行ずつ、<br />
その他の行が1行ずつ出力されてしまいます。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">curl</span></tt> の出力は、例え読み取ったHTMLがUTF-8<br />
で書いてあっても改行コードが<br />
UNIX標準のものと違っている可能性があるので、<br />
このようなときは必ず通します。<br />
オプションは <tt class="docutils literal"><span class="pre">-wLux</span></tt> が私の場合は手癖になっており、</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">w</span></tt> : UTF-8に変換</li><br />
<li><tt class="docutils literal"><span class="pre">Lu</span></tt> : 改行コードをLF（0x0a）に</li><br />
<li><tt class="docutils literal"><span class="pre">x</span></tt> : 半角カナから全角カナへの変換を抑制</li><br />
</ul><br />
<p>という意味があります。</p><br />
<p>　ただ、このようにHTMLがきれいに<br />
改行されていればあまり苦労もないのですが、<br />
実際はそうもいきません。<br />
リスト13のようなHTMLもあるでしょう。</p><br />
<ul class="simple"><br />
<li>リスト13: 例題ファイルその3</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201310 ueda<span class="nv">$ </span>cat kitanai.html<br />
&lt;pre&gt;#!/bin/bash<br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;きたない&quot;</span>&lt;/pre&gt;あははは&lt;pre&gt;<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;きたなすぎる&quot;</span><br />
&lt;/pre&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>こういうときは、リスト14のように自分で掃除するしかありません。<br />
このsedのワンライナーはお世辞にもきれいとは言えないので、<br />
ちゃんとプログラムを書いた方がいいかもしれません。<br />
ただ、結局この方が早いことが多いです。</p><br />
<ul class="simple"><br />
<li>リスト14: きたないHTMLを掃除するワンライナー</li><br />
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
20</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>cat kitanai.html |<br />
<span class="c">#&lt;pre&gt;の後に何か文字があると改行を差し込む</span><br />
gsed <span class="s1">&#39;s;\\(&lt;pre[^&gt;]*&gt;\\)\\(..*\\);\\1\\n\\2;g&#39;</span> |<br />
<span class="c">#&lt;pre&gt;の前に何か文字があると改行を差し込む</span><br />
gsed <span class="s1">&#39;s;\\(..*\\)\\(&lt;pre[^&gt;]*&gt;\\);\\1\\n\\2;g&#39;</span> |<br />
<span class="c">#&lt;/pre&gt;の前に何か文字があると改行を差し込む</span><br />
gsed <span class="s1">&#39;s;\\(..*\\)&lt;/pre&gt;;\\1\\n&lt;/pre&gt;;g&#39;</span> |<br />
<span class="c">#&lt;/pre&gt;の後に何か文字があると改行を差し込む</span><br />
gsed <span class="s1">&#39;s;&lt;/pre&gt;\\(..*\\);&lt;/pre&gt;\\n\\1;g&#39;</span><br />
&lt;pre&gt;<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;きたない&quot;</span><br />
&lt;/pre&gt;<br />
あははは<br />
&lt;pre&gt;<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;きたなすぎる&quot;</span><br />
&lt;/pre&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この例題の最後に便利な小ネタを。<br />
さきほどpreで抜き出したHTMLには</p><br />
<div class="highlight-bash"><div class="highlight"><pre>&amp;gt;&amp;gt;&amp;gt; round<span class="o">(</span>-1.1,-1<span class="o">)</span><br />
</pre></div><br />
</div><br />
<p>などと、記号の一部が文字実体参照に変換されています。<br />
例えば <tt class="docutils literal"><span class="pre">&amp;gt;</span></tt> は <tt class="docutils literal"><span class="pre">&gt;</span></tt> が置き換わったものです。</p><br />
<p>　また、次のように数値参照になっているときもあります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>&amp;#x4e0a;&amp;#x7530;&amp;#x53c2;&amp;#x4e0a;<br />
</pre></div><br />
</div><br />
<p>HTMLから抜き出して来たら、<br />
このままにするより元に戻した方がよいでしょう。</p><br />
<p>　数値参照の方はリスト15のように <tt class="docutils literal"><span class="pre">nkf</span></tt> でできます。</p><br />
<ul class="simple"><br />
<li>リスト15: 数値参照を <tt class="docutils literal"><span class="pre">nkf</span></tt> でデコードする</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;&amp;#x4e0a;&amp;#x7530;&amp;#x53c2;&amp;#x4e0a;&#39;</span> |<br />
nkf --numchar-input<br />
上田参上<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　文字実体参照の方は <tt class="docutils literal"><span class="pre">nkf</span></tt> でできません。残念。<br />
しかし、 <tt class="docutils literal"><span class="pre">&quot;&amp;&lt;&gt;</span></tt> とスペース程度ならあまり個数がないので<br />
リスト16のようにsedスクリプトを書くとよいでしょう。<br />
コマンド化してもいいですね。</p><br />
<ul class="simple"><br />
<li>リスト16: 文字実体参照を置換するsedスクリプトを作って使う</li><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>#このようなsedスクリプトを作る<br />
uedamac:~ ueda$ cat ref.sed<br />
s/&amp;lt;/&lt;/g<br />
s/&amp;gt;/&gt;/g<br />
s/&amp;quot;/&quot;/g<br />
s/&amp;amp;/\\&amp;/g<br />
s/&amp;nbsp;/ /g<br />
uedamac:~ ueda$ curl http://blog.ueda.asia 2&gt; /dev/null |<br />
sed -n &#39;/&lt;pre/,/&lt;\\/pre/p&#39; | gsed -n &#39;1,/&lt;\\/pre/p&#39; |<br />
sed -f ./ref.sed<br />
&lt;pre class=&quot;brush: bash; title: ; notranslate&quot; title=&quot;&quot;&gt;<br />
（略）<br />
&gt;&gt;&gt; round(-1.1,-1)*1.0<br />
-0.0<br />
&lt;/pre&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　他の文字実体参照も変換しなければならないときは、<br />
他の言語のライブラリを使って<br />
変換コマンドを書くのが一番簡単な方法です。<br />
・・・しかし、皆さんには文字実体参照の一覧を掲載した<br />
ウェブサイトからtableを抜き出し、<br />
<tt class="docutils literal"><span class="pre">ref.sed</span></tt> のようなスクリプトを<br />
ワンライナーで作ることをおすすめしておきます。</p><br />
</div><br />
<div class="section" id="find-grep-xargs"><br />
<h2>22.4. find, grep, xargsの組み合わせ<a class="headerlink" href="#find-grep-xargs" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　最後にファイルの検索をやってみます。<br />
ディレクトリの中から何かテキストを探すときは、<br />
<tt class="docutils literal"><span class="pre">find</span></tt> と <tt class="docutils literal"><span class="pre">xargs</span></tt><br />
を組み合わせると自由自在な感じになります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">find</span></tt> については、<br />
名前で誤解を受けやすいのですが、<br />
単に指定したディレクトリの下のファイルや<br />
ディレクトリを延々と出力するだけです。<br />
<tt class="docutils literal"><span class="pre">find</span></tt> はオプションが多い事でも知られていますが、<br />
リスト17のような使い方だけ知っておけばよいと思います。<br />
オプションの <tt class="docutils literal"><span class="pre">.</span></tt> はカレントディレクトリ、<br />
<tt class="docutils literal"><span class="pre">-type</span> <span class="pre">f</span></tt> はファイルだけ表示しろということです。</p><br />
<ul class="simple"><br />
<li>リスト17: <tt class="docutils literal"><span class="pre">find</span></tt> を使う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>find . -type f | head -n 4<br />
./.201203.rst.swp<br />
./.201310.rst.swp<br />
./.DS_Store<br />
./.git/COMMIT_EDITMSG<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　出力は1レコード1ファイルorディレクトリと、<br />
UNIXの教科書通りなので、<br />
ファイル名で検索するときはパイプで <tt class="docutils literal"><span class="pre">grep</span></tt><br />
をつなげばよいということになります。</p><br />
<p>　例えば、ミーティング中にとっさにとったメモ<br />
をどこに保存したか忘れたが、何を書いたかはうっすら覚えている場合、<br />
（そしてメモを取るときは必ずファイル名に<br />
<tt class="docutils literal"><span class="pre">memo</span></tt> か <tt class="docutils literal"><span class="pre">MEMO</span></tt> を入れている場合、）<br />
リスト18のようなワンライナーで探し出すことができます。</p><br />
<ul class="simple"><br />
<li>リスト18: <tt class="docutils literal"><span class="pre">find</span></tt> と <tt class="docutils literal"><span class="pre">grep</span></tt> 、 <tt class="docutils literal"><span class="pre">xargs</span></tt> を組み合わせる</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>find ~ -type f | fgrep -v <span class="s2">&quot;/.&quot;</span> | grep -i memo | xargs grep 徹夜 | gsed <span class="s1">&#39;s/:.*//&#39;</span> &gt; hoge<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat hoge<br />
/Users/ueda/Dropbox/USP/memo/memo<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat hoge | xargs cat<br />
徹夜で仕事しろと言われた（このメモはフィクションです。）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これが自在にできれば、<br />
某OSで検索のときに出て来る犬に頼る必要はありません。<br />
<tt class="docutils literal"><span class="pre">find</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> で検索をかけるときによく使うイディオムを挙げておきます。</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">find</span> <span class="pre">.</span> <span class="pre">|</span> <span class="pre">grep</span> <span class="pre">hoge</span></tt> : ファイル名の検索</li><br />
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span></tt> : ディレクトリ下の全ファイルの中身を検索</li><br />
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span> <span class="pre">|</span> <span class="pre">gsed</span> <span class="pre">'s/:.*/'</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> : ディレクトリ下の全ファイルの中身を検索し、ファイル名のリストを抽出</li><br />
<li><tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-r</span> <span class="pre">hoge</span> <span class="pre">./</span> <span class="pre">|</span> <span class="pre">gsed</span> <span class="pre">'s/:.*/'</span> <span class="pre">|</span> <span class="pre">uniq</span> <span class="pre">|</span> <span class="pre">xargs</span> <span class="pre">cat</span></tt> : ディレクトリ下の全ファイルの中身を検索し、ファイル名のリストを抽出し、抽出したファイルの中身を表示</li><br />
</ul><br />
</div><br />
<div class="section" id="id5"><br />
<h2>22.5. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はテキストファイルをハンドリングする<br />
ノウハウをいくつか紹介しました。<br />
この手のノウハウは無数にあり、ほんの一部分を<br />
つまみ食いでだらだら紹介してしまった感もありますが、<br />
CUIで自分の文章を管理するときに実際にどんな<br />
コマンドの使い方をしているのか、<br />
雰囲気くらいはお伝えできたかと思います。</p><br />
<p>　次回は表記揺れに的をしぼって、何か作り物をしてみる予定です。<br />
表記ゆれのテストスクリプトを書きます。<br />
原稿書きもテストファーストの時代へ・・・（大げさ）</p><br />
</div><br />
</div><br />
<br />

