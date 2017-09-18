---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年5月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="awk"><br />
<h1>17. 開眼シェルスクリプト 第17回awkでちょっと面倒な処理をする<a class="headerlink" href="#awk" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　今回の開眼シェルスクリプトは、<br />
作り物を休んでテキスト処理のパズルを扱います。<br />
今回の内容はUSP友の会の<br />
「シェル芸勉強会」で出題しているような問題です。<br />
もしご興味があれば、筆者自らビシビシ鍛えますので、<br />
ぜひ遊びに来てください。参加費500円也。</p><br />
<p>　そのシェル芸勉強会でも本連載でも再三にわたって訴えていることですが、<br />
シェルでのコマンドの使い方を覚えると、<br />
わざわざプログラム（シェルスクリプトを含む）を書いたりせず、<br />
電卓を叩くようにテキスト処理ができるようになります。</p><br />
<p>　ただし、端末上でテキストをいじることには一つの「壁」があります。<br />
その壁とは、「本当に自分の欲しい出力が得られるのだろうか？」<br />
という恐怖というか、時間を無駄にするかもしれないことに対する抵抗感です。<br />
UNIXができた当初ならいざ知らず、今はいろんな「逃げ方」があるので、<br />
抵抗感を持つと、筆者が「この方法が一番手っ取り早い」<br />
と言っても、なかなかやってみようという気にはならないでしょう。</p><br />
<p>　この壁を少しでも低くするために、<br />
筆者は度々AWKを使ってもらうように宣伝します。<br />
AWKの場合、例えば <tt class="docutils literal"><span class="pre">cat</span> <span class="pre">hoge</span> <span class="pre">|</span> <span class="pre">awk</span> <span class="pre">{print</span> <span class="pre">$1}</span></tt><br />
だけでも役立つ場面が多いので、<br />
シェルスクリプトが云々と言うよりとっかかりが早いのです。</p><br />
<p>　既に「こちらの世界」に入ってしまった人にとっても、<br />
AWKのスキルはツブしを効かせることに絶大な効果があります。<br />
コマンドを忘れても、ややこしいテキストを処理しだして袋小路に追い込まれても、<br />
AWKで力づくで押し切ってしまう腕があれば、<br />
HDDのゴミになるようなプログラムなど書く気にもならなくなるでしょう。</p><br />
<p>　ということで、今回は比較的端末上で扱いづらいテキストを、<br />
AWKで乗り切る方法について扱いたいと思います。</p><br />
<p>　毎回定番の格言ですが、「壁」と言えばこの方ですので、<br />
学習のヒントとして挙げておきます。</p><br />
<ul class="simple"><br />
<li>すでにやってしまった以上は、その結果がよいほうに向かうように、あとの人生を動かすしかない。</li><br />
</ul><br />
<p>&#8212;養老孟司</p><br />
<p>　すでに端末上でやってしまった以上は、その結果がよいほうに向かうように、AWKを動かすしかない。</p><br />
<p>&#8212;　筆者</p><br />
<div class="section" id="id1"><br />
<h2>17.1. 環境<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回も前回に引き続き、Macを使っています。<br />
リスト1に環境を示します。<br />
ただ、今回も環境が違うからと言ってそんなに困る事はないと思います。<br />
むしろ、どの問題もいろんな処理の方法があるので、<br />
うまくいかなかったら別の方法を試してみましょう。</p><br />
<p>↓リスト1: 環境</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201305 ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64<br />
uedamac:201305 ueda<span class="nv">$ </span>awk --version<br />
awk version 20070501<br />
<span class="nv">$ </span>gsed --version<br />
GNU sed version 4.2.1<br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2009 Free Software Foundation, Inc.<br />
（以下略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　問題4で必要なので、Macにデフォルトで入っているsedの他に、<br />
gsedをインストールしました。<br />
Macの人はmacportsやhomebrewを使ってインストールしてみてください。<br />
FreeBSDの場合も、ports等でインストールする必要があります。<br />
Linuxの場合は、そのまま問題なく日本語を処理できるはずです。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>17.2. 問題1<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　リスト2のようなデータがあったとします。<br />
やりたいことは、各行の数字に対して、<br />
その一つ上の数字との差を求めるということです。<br />
出力は、自分で見るためのものなので適当でも構いません。</p><br />
<p>↓リスト2: 問題1の入力ファイル</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT<br />
2<br />
53<br />
165<br />
6<br />
899<br />
9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この問題は、AWKに慣れている人ならすぐにできると思います。<br />
リスト3のように、変数を使って行またぎの処理をします。<br />
AWKのアクションの中は、今のレコードと「 <tt class="docutils literal"><span class="pre">a</span></tt> 」<br />
の差を求めて出力し、その後で今のレコードを <tt class="docutils literal"><span class="pre">a</span></tt><br />
に代入するというものです。<br />
次のレコードに処理が移ったとき、<br />
<tt class="docutils literal"><span class="pre">a</span></tt> には前のレコードの値が入っています。</p><br />
<p>↓リスト3: 解答その1</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;{print $1-a;a=$1}&#39;</span><br />
2<br />
51<br />
112<br />
-159<br />
893<br />
-890<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ところで、この計算では一番最初のレコードの扱いが雑です。<br />
最初のレコードの <tt class="docutils literal"><span class="pre">$1-a</span></tt> は、<br />
<tt class="docutils literal"><span class="pre">a</span></tt> は <tt class="docutils literal"><span class="pre">0</span></tt> で初期化されるので、 <tt class="docutils literal"><span class="pre">2-0</span></tt><br />
で <tt class="docutils literal"><span class="pre">2</span></tt> がそのまま出力されます。<br />
雑なら雑でよいのですが、もし最初のレコードがいらないなら<br />
リスト4のように <tt class="docutils literal"><span class="pre">tail</span></tt> で取り除きます。</p><br />
<p>↓リスト4: 解答その2</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;{print $1-a;a=$1}&#39;</span> | tail -n +2<br />
51<br />
112<br />
-159<br />
893<br />
-890<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　AWKだけでやるとすると、もう少しエレガントな方法もあります。<br />
リスト5に示します。ただまあ、これは考えすぎです。</p><br />
<p>↓リスト5: 解答その3</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;NR!=1{print $1-a}{a=$1}&#39;</span><br />
51<br />
112<br />
-159<br />
893<br />
-890<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id3"><br />
<h2>17.3. 問題2<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次は、つい表計算ソフトでやってしまいそうな足し算の問題です。<br />
リスト6のファイル <tt class="docutils literal"><span class="pre">Q2.INPUT</span></tt> について、<br />
キー（この例では <tt class="docutils literal"><span class="pre">001</span> <span class="pre">AAA</span></tt> や <tt class="docutils literal"><span class="pre">002</span> <span class="pre">BBB</span></tt> のこと）<br />
ごとに数字を足してみましょう。</p><br />
<p>↓リスト6: 問題2の入力ファイル</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT<br />
001 AAA 0.1<br />
001 AAA 0.2<br />
002 BBB 0.2<br />
002 BBB 0.3<br />
002 BBB 0.4<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この問題を一番素直に解くと、<br />
リスト7のように連想配列を使ったものになるでしょう。<br />
一列目と二列目の文字列を空白をはさんで連結してキーにして、<br />
配列 <tt class="docutils literal"><span class="pre">sum</span></tt> の当該のキーに値を足し込みます。<br />
<tt class="docutils literal"><span class="pre">sum</span></tt> の各要素はゼロで初期化されているので、<br />
最初から <tt class="docutils literal"><span class="pre">+=</span></tt> で足して構いません。<br />
そして、前号の画像処理の際も説明しましたが、<br />
AWKの配列は連想配列で、<br />
インデックス（角括弧の中）に初期化せずになんでも指定できます。<br />
ですので、このように文字列を丸ごとインデックスにできます。</p><br />
<p>↓リスト7: 解答その1</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;{sum[$1 &quot; &quot; $2] +=$3}END{for(k in sum){print k,sum[k]}}&#39;</span><br />
001 AAA 0.3<br />
002 BBB 0.9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">for(k</span> <span class="pre">in</span> <span class="pre">sum)</span></tt> は、配列 <tt class="docutils literal"><span class="pre">sum</span></tt><br />
の全要素のインデックスを一つずつ <tt class="docutils literal"><span class="pre">k</span></tt> にセットしてfor文を回す書き方です。</p><br />
<p>　ところでこの方法だと、ソートしていないデータでも足し算してくれる一方、<br />
入力されたデータをAWKが一度全部吸い込んでから出力するので、<br />
パイプの間に挟むとデータが一時的に流れなくなります。<br />
最後に順番に出力してくれるとも限りません。<br />
さらに、連想配列を使っているので、<br />
もう少しデータが大きくなると遅くなります。</p><br />
<p>　ということで、<br />
入力レコードがもうちょっと多くなったときの書き方をリスト8に示します。<br />
データはソートされていることが前提となります。<br />
念のために言っておくと、上記の方法で済むうちは、<br />
わざと難しく書く必要はないので、上記の方法でやってください。</p><br />
<p>↓リスト8: 解答その2</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;NR!=1 &amp;&amp; k1!=$1{print k1,k2,sum;sum=0}\\</span><br />
<span class="s1"> {k1=$1;k2=$2;sum+=$3}END{print k1,k2,sum}&#39;</span><br />
001 AAA 0.3<br />
002 BBB 0.9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　一列目と二列目が一対一対応でないことがある場合は、<br />
リスト9のようにしましょう。</p><br />
<p>↓リスト9: 解答その3</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;NR!=1 &amp;&amp; k!=$1&quot; &quot;$2{print k,sum;sum=0}\\</span><br />
<span class="s1"> {k=$1&quot; &quot;$2;sum+=$3}END{print k,sum}&#39;</span><br />
001 AAA 0.3<br />
002 BBB 0.9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この方法だと、キーの境目で出力がありますし、<br />
配列にデータを溜め込むということもありません。</p><br />
<p>　この手のAWKプログラミングでは、まずパターンがどれだけあるか考え、<br />
その後に各パターンで何をしなければならないのかを考えると、<br />
すんなり問題が解けることがあります。<br />
この例では、</p><br />
<ul class="simple"><br />
<li>キーが変化するレコードで行う処理（キーと和を出力）</li><br />
<li>通常の処理（キーを記憶し、数字を足す）</li><br />
<li>最後の処理（一番最後のキーの和を出力）</li><br />
</ul><br />
<p>と三つのパターンとアクションを考える事で、<br />
if文を使わずに目的の計算を実装しています。</p><br />
<p>　ちょっと脱線しますが、同じ処理をPythonで素直に書くと、<br />
リスト10のようになります。<br />
一概に長い短いを比較することは乱暴ですが、<br />
変数の初期化の方法、行の読み込み方、パターン v.s. if文、<br />
という３つの点において、AWKの方が、<br />
筆者の出している問題に対して近道であることが分かります。</p><br />
<p>↓リスト10: pythonでの解答</p><br />
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ./sum.py<br />
<span class="c">#!/usr/bin/python</span><br />
<br />
import sys<br />
<br />
<span class="nv">key</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span><br />
<span class="nv">n</span> <span class="o">=</span> 1<br />
<span class="nv">s</span> <span class="o">=</span> 0.0<br />
<span class="k">for </span>line in sys.stdin:<br />
 <span class="nv">token</span> <span class="o">=</span> line.rstrip<span class="o">()</span>.split<span class="o">(</span><span class="s2">&quot; &quot;</span><span class="o">)</span><br />
 <span class="nv">k</span> <span class="o">=</span> <span class="s2">&quot; &quot;</span>.join<span class="o">(</span>token<span class="o">[</span>0:2<span class="o">])</span><br />
<br />
 <span class="k">if </span>n !<span class="o">=</span> 1 and key !<span class="o">=</span> k:<br />
 print key, s<br />
 <span class="nv">s</span> <span class="o">=</span> 0.0<br />
<br />
 s +<span class="o">=</span> float<span class="o">(</span>token<span class="o">[</span>2<span class="o">])</span><br />
 <span class="nv">key</span> <span class="o">=</span> k<br />
 n +<span class="o">=</span> 1<br />
<br />
print key, s<br />
<br />
<span class="nv">$ </span>cat Q2.INPUT | ./sum.py<br />
001 AAA 0.3<br />
002 BBB 0.9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もう一つ。Open usp Tukubai の <tt class="docutils literal"><span class="pre">sm2</span></tt> を使えば、<br />
リスト11のようにコマンド一発で終わりです。<br />
詳細については <a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a> をご覧ください。</p><br />
<p>↓リスト11: Open usp Tukubai を使った解答</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sm2 1 2 3 3 Q2.INPUT<br />
001 AAA 0.3<br />
002 BBB 0.9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このAWK、Python、sm2（あとはエクセル）の例を見比べていると、<br />
道具の選び方について考えさせられます。<br />
普段、端末を使わない人がわざわざAWK一行野郎（or perl一行野郎）やsm2<br />
を覚える必要があるかと言われると正直疑問です。<br />
おまけに、問題に特化したツールほど数が多くなるので覚えるのが大変です。<br />
ただし一行野郎もコマンドも知らないと、もしテキストの数字を足せと言われたとき、<br />
遠回りを余儀なくされます。</p><br />
<p>　少なくとも言えることは、<br />
この「汎用的なものを少し覚える v.s. 特化したものを多く覚える」<br />
には優劣がないということと、特に若い人は、思っているより人生は長いので、<br />
どっちもたくさん勉強しておくと後から時間が稼げるということです。</p><br />
<p>　もう一つ言っておくと、「コマンド派」には、「組み合わせ」という強みがあります。<br />
Open usp Tukubai のコマンドは今のところ50足らずですが、<br />
組み合わせる事で無数の仕事をこなせます。<br />
組み合わせることで数が爆発することは、ご存知かと思います。<br />
この点において、言語のライブラリをいちいち調べることよりも、<br />
コマンドを覚える方が学習の密度は高いのかなと考えています。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>17.4. 問題3<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　リスト12のファイルを考えます。<br />
<tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各レコードは日付の範囲で、<br />
<tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> は日付のつもりです。<br />
やりたいことは、 <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各日付の範囲に、<br />
<tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> が何日ずつ含まれているかを調べるということです。</p><br />
<p>↓リスト12: 問題3の入力ファイル</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q3.SPAN<br />
20130101 20130125<br />
20130126 20130212<br />
20130213 20130310<br />
20130311 20130402<br />
<span class="nv">$ </span>cat Q3.DAYS<br />
20130102<br />
20130203<br />
20130209<br />
20130312<br />
20130313<br />
20130429<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　筆者が「AWK1個だけ」という制限のもと、<br />
最初に書いたワンライナーは次のようなものです。</p><br />
<p>↓リスト13: 解答その1</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{f[FNR]=$1;t[FNR]=$2}\\</span><br />
<span class="s1"> FILENAME~/DAYS/{for(k in f){\\</span><br />
<span class="s1"> if($1&gt;=f[k] &amp;&amp; $1&lt;=t[k]){sum[f[k]&quot; &quot;t[k]]++}}}\\</span><br />
<span class="s1"> END{for(k in sum){print k,sum[k]}}&#39;</span> Q3.SPAN Q3.DAYS<br />
20130126 20130212 2<br />
20130311 20130402 2<br />
20130101 20130125 1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>これは完全にライトオンリーのコードなので読む必要はありません。<br />
どんな処理か説明すると、次のようになります。</p><br />
<ul class="simple"><br />
<li>最初のパターンで <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各レコードを配列 <tt class="docutils literal"><span class="pre">f</span></tt> （from）、 <tt class="docutils literal"><span class="pre">t</span></tt> （to）に代入</li><br />
<li>次のパターンで <tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> の日付と <tt class="docutils literal"><span class="pre">f,t</span></tt> の内容を比較して、日付が期間中にあれば、期間に対応するカウンタ（ <tt class="docutils literal"><span class="pre">sum[&lt;期間&gt;]</span></tt> ）に1を足す</li><br />
<li>ENDパターンで、 各期間と <tt class="docutils literal"><span class="pre">sum</span></tt> の内容を出力</li><br />
</ul><br />
<p>変数 <tt class="docutils literal"><span class="pre">FILENAME</span></tt> にはオプションで指定したファイル名、<br />
<tt class="docutils literal"><span class="pre">FNR</span></tt> には、各ファイル内でのレコード番号が予め代入されており、<br />
このコードではそれをパターンや配列のインデックスに使っています。</p><br />
<p>　筆者は答えが出ればそれでOKという立場ですが、<br />
もうちょっときれいに解いてみましょう。<br />
シェルスクリプトでデータ処理を行うときは、<br />
1レコードに計算する対象がすべて収まっていると楽な場合が多くなります。<br />
ということは、予めそのような状態を作りにいけばよいということになります。</p><br />
<p>　ということで、まず、リスト14のように <tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> と <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt><br />
のレコードの組み合わせを全通り作ります。</p><br />
<p>↓リスト14: 解答その2</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{key[FNR]=$1&quot; &quot;$2}FILENAME~/DAYS/{for(k in key){print key[k],$1}}&#39;</span> Q3.SPAN Q3.DAYS<br />
20130126 20130212 20130102<br />
20130213 20130310 20130102<br />
20130311 20130402 20130102<br />
20130101 20130125 20130102<br />
20130126 20130212 20130203<br />
20130213 20130310 20130203<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>こうなると、3列目の日付が1,2列目の日付の範囲に含まれているものを出力し、<br />
数を数えるとよいということになります。<br />
この方が、一個のAWKで頑張るよりすっきりしますね。</p><br />
<p>↓リスト15: 解答その3</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{key[FNR]=$1&quot; &quot;$2}FILENAME~/DAYS/{for(k in key){print key[k],$1}}&#39;</span> Q3.SPAN Q3.DAYS | awk <span class="s1">&#39;$1&lt;=$3&amp;&amp;$3&lt;=$2{print $1,$2}&#39;</span> | uniq <br />
c- 1 20130101 20130125<br />
 2 20130126 20130212<br />
 2 20130311 20130402<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これも、 Open usp Tukubai を使うともっと楽になります。<br />
リスト16に解答を示します。<br />
<tt class="docutils literal"><span class="pre">loopx</span></tt> は、上のリストの最初のAWKと同じ処理をしています。</p><br />
<p>↓リスト16: Open usp Tukubai を使った解答</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>loopx Q3.SPAN Q3.DAYS | awk <span class="s1">&#39;$1&lt;=$3&amp;&amp;$3&lt;=$2{print $1,$2}&#39;</span> | uniq <br />
c- 1 20130101 20130125<br />
 2 20130126 20130212<br />
 2 20130311 20130402<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id5"><br />
<h2>17.5. 問題4<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　最後に、文章の処理を扱ってみましょう。<br />
さばくのはリスト17のファイルです。<br />
文章は、信じないようにしましょう。大嘘です。</p><br />
<p>↓リスト17: 問題4の入力ファイル</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO<br />
「コロラド大ダンゴ虫」は、直径20cmになる世界最大のダンゴ虫。ダンゴ虫を転がし、トゲを抜いた柱状サボテンを倒して遊んだのが、ボーリングの始まり。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このファイルを、何かのフォームに貼付けるために、<br />
20文字で折り返すというのが問題です。<br />
さっそくやってみましょう。</p><br />
<p>↓リスト18: 解答その1</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |<br />
 awk <span class="s1">&#39;{printf $1}NR%20==0{print &quot;&quot;}END{print &quot;&quot;}&#39;</span> &gt; tmp<br />
<span class="nv">$ </span>cat tmp<br />
「コロラド大ダンゴ虫」は、直径20cmに<br />
なる世界最大のダンゴ虫。ダンゴ虫を転がし<br />
、トゲを抜いた柱状サボテンを倒して遊んだ<br />
のが、ボーリングの始まり。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>最初のgsedで一文字一文字、後ろに改行を入れて出力し、<br />
次のAWKで20文字ずつまとめています。<br />
単に文字列を改行しないで出力したい場合は、<br />
この例のように <tt class="docutils literal"><span class="pre">printf</span></tt> を括弧なしで変数を指定して大丈夫です。</p><br />
<p>　この出力、少々問題があります。句点が一個、行頭に来ています。<br />
句読点を21文字目にくっつけてよいなら、<br />
リスト19のようにコードを書けばよいでしょう。</p><br />
<p>↓リスト19: 解答その2（句読点対応）</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;NR!=1{\\</span><br />
<span class="s1"> if($1~/^、/){print a&quot;、&quot;}else{print a}}\\</span><br />
<span class="s1"> {a=$1}END{print a}&#39;</span> | sed <span class="s1">&#39;s/^、//&#39;</span><br />
「コロラド大ダンゴ虫」は、直径20cmに<br />
なる世界最大のダンゴ虫。ダンゴ虫を転がし、<br />
トゲを抜いた柱状サボテンを倒して遊んだ<br />
のが、ボーリングの始まり。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　分かりにくいと思いますが、このAWKは「先読み」<br />
という定石を使っています。実は問題1,2でも使っています。<br />
リスト20のコードのように、<br />
一行読み込んで一行前の行を出力するコードを書いて、<br />
そこから必要なコードを足します。<br />
そうすると、 <tt class="docutils literal"><span class="pre">a</span></tt> の出力をその次の行を見て操作できます。</p><br />
<p>↓リスト20: 先読みの骨組み</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;NR!=1{print a}{a=$1}END{print a}&#39;</span><br />
「コロラド大ダンゴ虫」は、直径20cmに<br />
（以下略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　句読点も含めて20字で収めなければならないなら、<br />
話はもっとややこしくなります。コードだけ示しておきますが、<br />
ここまで来るとバグを取るのが大変でした。こうなったら、<br />
字の折り返しのコマンドをちゃんと作ろうかという気になってきます。<br />
もちろんコマンドにするなら、<br />
句点だけでなく読点等にもちゃんと対応して汎用性を目指すことになります。</p><br />
<p>↓リスト21: 解答その3</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |<br />
awk <span class="s1">&#39;BEGIN{c=0}\\</span><br />
<span class="s1">NR!=1{if(c==19 &amp;&amp; $1==&quot;、&quot;){print &quot;&quot;;printf a;c=1}else{printf a;c++}}\\</span><br />
<span class="s1">c==20{print &quot;&quot;;c=0}{a=$1}END{print a}&#39;</span><br />
「コロラド大ダンゴ虫」は、直径20cmに<br />
なる世界最大のダンゴ虫。ダンゴ虫を転が<br />
し、トゲを抜いた柱状サボテンを倒して遊ん<br />
だのが、ボーリングの始まり。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　最後にどうでもよいことを述べると、<br />
この出力の一字一字にカンマを挟み込んでcsvにすると、<br />
あの悪名高き「エクセル方眼紙」に張り付きます。<br />
やむなくエクセル方眼紙に字を書く羽目になったら、<br />
お試しください。スジのいい人なら、<br />
一字ずつ方眼紙で書く時間より、AWKを覚える時間の方が短いです。<br />
そりゃ言い過ぎですね。失礼しました！</p><br />
</div><br />
<div class="section" id="id6"><br />
<h2>17.6. 最後に<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はシェルスクリプトでテキスト処理する際につまずきやすい問題を、<br />
AWKで解決してみました。このような類いの処理は無数にありますが、<br />
先読みが使えるかどうかなど、パターンはそんなにないので、<br />
慣れてしまうとシェル上でさばくことに抵抗が薄れてきます。<br />
特に先読みは多くの集計処理に登場します。</p><br />
<p>　次回は、twitterでリクエストを受けたので、<br />
netcatなどを使ってbashで通信を行ってみたいと思います。</p><br />
</div><br />
</div><br />
<br />

