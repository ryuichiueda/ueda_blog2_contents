---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年5月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="awk">
<h1>17. 開眼シェルスクリプト 第17回awkでちょっと面倒な処理をする<a class="headerlink" href="#awk" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　今回の開眼シェルスクリプトは、
作り物を休んでテキスト処理のパズルを扱います。
今回の内容はUSP友の会の
「シェル芸勉強会」で出題しているような問題です。
もしご興味があれば、筆者自らビシビシ鍛えますので、
ぜひ遊びに来てください。参加費500円也。</p>
<p>　そのシェル芸勉強会でも本連載でも再三にわたって訴えていることですが、
シェルでのコマンドの使い方を覚えると、
わざわざプログラム（シェルスクリプトを含む）を書いたりせず、
電卓を叩くようにテキスト処理ができるようになります。</p>
<p>　ただし、端末上でテキストをいじることには一つの「壁」があります。
その壁とは、「本当に自分の欲しい出力が得られるのだろうか？」
という恐怖というか、時間を無駄にするかもしれないことに対する抵抗感です。
UNIXができた当初ならいざ知らず、今はいろんな「逃げ方」があるので、
抵抗感を持つと、筆者が「この方法が一番手っ取り早い」
と言っても、なかなかやってみようという気にはならないでしょう。</p>
<p>　この壁を少しでも低くするために、
筆者は度々AWKを使ってもらうように宣伝します。
AWKの場合、例えば <tt class="docutils literal"><span class="pre">cat</span> <span class="pre">hoge</span> <span class="pre">|</span> <span class="pre">awk</span> <span class="pre">{print</span> <span class="pre">$1}</span></tt>
だけでも役立つ場面が多いので、
シェルスクリプトが云々と言うよりとっかかりが早いのです。</p>
<p>　既に「こちらの世界」に入ってしまった人にとっても、
AWKのスキルはツブしを効かせることに絶大な効果があります。
コマンドを忘れても、ややこしいテキストを処理しだして袋小路に追い込まれても、
AWKで力づくで押し切ってしまう腕があれば、
HDDのゴミになるようなプログラムなど書く気にもならなくなるでしょう。</p>
<p>　ということで、今回は比較的端末上で扱いづらいテキストを、
AWKで乗り切る方法について扱いたいと思います。</p>
<p>　毎回定番の格言ですが、「壁」と言えばこの方ですので、
学習のヒントとして挙げておきます。</p>
<ul class="simple">
<li>すでにやってしまった以上は、その結果がよいほうに向かうように、あとの人生を動かすしかない。</li>
</ul>
<p>&#8212;養老孟司</p>
<p>　すでに端末上でやってしまった以上は、その結果がよいほうに向かうように、AWKを動かすしかない。</p>
<p>&#8212;　筆者</p>
<div class="section" id="id1">
<h2>17.1. 環境<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回も前回に引き続き、Macを使っています。
リスト1に環境を示します。
ただ、今回も環境が違うからと言ってそんなに困る事はないと思います。
むしろ、どの問題もいろんな処理の方法があるので、
うまくいかなかったら別の方法を試してみましょう。</p>
<p>↓リスト1: 環境</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201305 ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64
uedamac:201305 ueda<span class="nv">$ </span>awk --version
awk version 20070501
<span class="nv">$ </span>gsed --version
GNU sed version 4.2.1
Copyright <span class="o">(</span>C<span class="o">)</span> 2009 Free Software Foundation, Inc.
（以下略）
</pre></div>
</td></tr></table></div>
<p>　問題4で必要なので、Macにデフォルトで入っているsedの他に、
gsedをインストールしました。
Macの人はmacportsやhomebrewを使ってインストールしてみてください。
FreeBSDの場合も、ports等でインストールする必要があります。
Linuxの場合は、そのまま問題なく日本語を処理できるはずです。</p>
</div>
<div class="section" id="id2">
<h2>17.2. 問題1<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　リスト2のようなデータがあったとします。
やりたいことは、各行の数字に対して、
その一つ上の数字との差を求めるということです。
出力は、自分で見るためのものなので適当でも構いません。</p>
<p>↓リスト2: 問題1の入力ファイル</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT
2
53
165
6
899
9
</pre></div>
</td></tr></table></div>
<p>　この問題は、AWKに慣れている人ならすぐにできると思います。
リスト3のように、変数を使って行またぎの処理をします。
AWKのアクションの中は、今のレコードと「 <tt class="docutils literal"><span class="pre">a</span></tt> 」
の差を求めて出力し、その後で今のレコードを <tt class="docutils literal"><span class="pre">a</span></tt>
に代入するというものです。
次のレコードに処理が移ったとき、
<tt class="docutils literal"><span class="pre">a</span></tt> には前のレコードの値が入っています。</p>
<p>↓リスト3: 解答その1</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;{print $1-a;a=$1}&#39;</span>
2
51
112
-159
893
-890
</pre></div>
</td></tr></table></div>
<p>　ところで、この計算では一番最初のレコードの扱いが雑です。
最初のレコードの <tt class="docutils literal"><span class="pre">$1-a</span></tt> は、
<tt class="docutils literal"><span class="pre">a</span></tt> は <tt class="docutils literal"><span class="pre">0</span></tt> で初期化されるので、 <tt class="docutils literal"><span class="pre">2-0</span></tt>
で <tt class="docutils literal"><span class="pre">2</span></tt> がそのまま出力されます。
雑なら雑でよいのですが、もし最初のレコードがいらないなら
リスト4のように <tt class="docutils literal"><span class="pre">tail</span></tt> で取り除きます。</p>
<p>↓リスト4: 解答その2</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;{print $1-a;a=$1}&#39;</span> | tail -n +2
51
112
-159
893
-890
</pre></div>
</td></tr></table></div>
<p>　AWKだけでやるとすると、もう少しエレガントな方法もあります。
リスト5に示します。ただまあ、これは考えすぎです。</p>
<p>↓リスト5: 解答その3</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q1.INPUT | awk <span class="s1">&#39;NR!=1{print $1-a}{a=$1}&#39;</span>
51
112
-159
893
-890
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id3">
<h2>17.3. 問題2<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次は、つい表計算ソフトでやってしまいそうな足し算の問題です。
リスト6のファイル <tt class="docutils literal"><span class="pre">Q2.INPUT</span></tt> について、
キー（この例では <tt class="docutils literal"><span class="pre">001</span> <span class="pre">AAA</span></tt> や <tt class="docutils literal"><span class="pre">002</span> <span class="pre">BBB</span></tt> のこと）
ごとに数字を足してみましょう。</p>
<p>↓リスト6: 問題2の入力ファイル</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT
001 AAA 0.1
001 AAA 0.2
002 BBB 0.2
002 BBB 0.3
002 BBB 0.4
</pre></div>
</td></tr></table></div>
<p>　この問題を一番素直に解くと、
リスト7のように連想配列を使ったものになるでしょう。
一列目と二列目の文字列を空白をはさんで連結してキーにして、
配列 <tt class="docutils literal"><span class="pre">sum</span></tt> の当該のキーに値を足し込みます。
<tt class="docutils literal"><span class="pre">sum</span></tt> の各要素はゼロで初期化されているので、
最初から <tt class="docutils literal"><span class="pre">+=</span></tt> で足して構いません。
そして、前号の画像処理の際も説明しましたが、
AWKの配列は連想配列で、
インデックス（角括弧の中）に初期化せずになんでも指定できます。
ですので、このように文字列を丸ごとインデックスにできます。</p>
<p>↓リスト7: 解答その1</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;{sum[$1 &quot; &quot; $2] +=$3}END{for(k in sum){print k,sum[k]}}&#39;</span>
001 AAA 0.3
002 BBB 0.9
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">for(k</span> <span class="pre">in</span> <span class="pre">sum)</span></tt> は、配列 <tt class="docutils literal"><span class="pre">sum</span></tt>
の全要素のインデックスを一つずつ <tt class="docutils literal"><span class="pre">k</span></tt> にセットしてfor文を回す書き方です。</p>
<p>　ところでこの方法だと、ソートしていないデータでも足し算してくれる一方、
入力されたデータをAWKが一度全部吸い込んでから出力するので、
パイプの間に挟むとデータが一時的に流れなくなります。
最後に順番に出力してくれるとも限りません。
さらに、連想配列を使っているので、
もう少しデータが大きくなると遅くなります。</p>
<p>　ということで、
入力レコードがもうちょっと多くなったときの書き方をリスト8に示します。
データはソートされていることが前提となります。
念のために言っておくと、上記の方法で済むうちは、
わざと難しく書く必要はないので、上記の方法でやってください。</p>
<p>↓リスト8: 解答その2</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;NR!=1 &amp;&amp; k1!=$1{print k1,k2,sum;sum=0}\\</span>
<span class="s1"> {k1=$1;k2=$2;sum+=$3}END{print k1,k2,sum}&#39;</span>
001 AAA 0.3
002 BBB 0.9
</pre></div>
</td></tr></table></div>
<p>　一列目と二列目が一対一対応でないことがある場合は、
リスト9のようにしましょう。</p>
<p>↓リスト9: 解答その3</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q2.INPUT | awk <span class="s1">&#39;NR!=1 &amp;&amp; k!=$1&quot; &quot;$2{print k,sum;sum=0}\\</span>
<span class="s1"> {k=$1&quot; &quot;$2;sum+=$3}END{print k,sum}&#39;</span>
001 AAA 0.3
002 BBB 0.9
</pre></div>
</td></tr></table></div>
<p>　この方法だと、キーの境目で出力がありますし、
配列にデータを溜め込むということもありません。</p>
<p>　この手のAWKプログラミングでは、まずパターンがどれだけあるか考え、
その後に各パターンで何をしなければならないのかを考えると、
すんなり問題が解けることがあります。
この例では、</p>
<ul class="simple">
<li>キーが変化するレコードで行う処理（キーと和を出力）</li>
<li>通常の処理（キーを記憶し、数字を足す）</li>
<li>最後の処理（一番最後のキーの和を出力）</li>
</ul>
<p>と三つのパターンとアクションを考える事で、
if文を使わずに目的の計算を実装しています。</p>
<p>　ちょっと脱線しますが、同じ処理をPythonで素直に書くと、
リスト10のようになります。
一概に長い短いを比較することは乱暴ですが、
変数の初期化の方法、行の読み込み方、パターン v.s. if文、
という３つの点において、AWKの方が、
筆者の出している問題に対して近道であることが分かります。</p>
<p>↓リスト10: pythonでの解答</p>
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ./sum.py
<span class="c">#!/usr/bin/python</span>

import sys

<span class="nv">key</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
<span class="nv">n</span> <span class="o">=</span> 1
<span class="nv">s</span> <span class="o">=</span> 0.0
<span class="k">for </span>line in sys.stdin:
 <span class="nv">token</span> <span class="o">=</span> line.rstrip<span class="o">()</span>.split<span class="o">(</span><span class="s2">&quot; &quot;</span><span class="o">)</span>
 <span class="nv">k</span> <span class="o">=</span> <span class="s2">&quot; &quot;</span>.join<span class="o">(</span>token<span class="o">[</span>0:2<span class="o">])</span>

 <span class="k">if </span>n !<span class="o">=</span> 1 and key !<span class="o">=</span> k:
 print key, s
 <span class="nv">s</span> <span class="o">=</span> 0.0

 s +<span class="o">=</span> float<span class="o">(</span>token<span class="o">[</span>2<span class="o">])</span>
 <span class="nv">key</span> <span class="o">=</span> k
 n +<span class="o">=</span> 1

print key, s

<span class="nv">$ </span>cat Q2.INPUT | ./sum.py
001 AAA 0.3
002 BBB 0.9
</pre></div>
</td></tr></table></div>
<p>　もう一つ。Open usp Tukubai の <tt class="docutils literal"><span class="pre">sm2</span></tt> を使えば、
リスト11のようにコマンド一発で終わりです。
詳細については <a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a> をご覧ください。</p>
<p>↓リスト11: Open usp Tukubai を使った解答</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sm2 1 2 3 3 Q2.INPUT
001 AAA 0.3
002 BBB 0.9
</pre></div>
</td></tr></table></div>
<p>　このAWK、Python、sm2（あとはエクセル）の例を見比べていると、
道具の選び方について考えさせられます。
普段、端末を使わない人がわざわざAWK一行野郎（or perl一行野郎）やsm2
を覚える必要があるかと言われると正直疑問です。
おまけに、問題に特化したツールほど数が多くなるので覚えるのが大変です。
ただし一行野郎もコマンドも知らないと、もしテキストの数字を足せと言われたとき、
遠回りを余儀なくされます。</p>
<p>　少なくとも言えることは、
この「汎用的なものを少し覚える v.s. 特化したものを多く覚える」
には優劣がないということと、特に若い人は、思っているより人生は長いので、
どっちもたくさん勉強しておくと後から時間が稼げるということです。</p>
<p>　もう一つ言っておくと、「コマンド派」には、「組み合わせ」という強みがあります。
Open usp Tukubai のコマンドは今のところ50足らずですが、
組み合わせる事で無数の仕事をこなせます。
組み合わせることで数が爆発することは、ご存知かと思います。
この点において、言語のライブラリをいちいち調べることよりも、
コマンドを覚える方が学習の密度は高いのかなと考えています。</p>
</div>
<div class="section" id="id4">
<h2>17.4. 問題3<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　リスト12のファイルを考えます。
<tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各レコードは日付の範囲で、
<tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> は日付のつもりです。
やりたいことは、 <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各日付の範囲に、
<tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> が何日ずつ含まれているかを調べるということです。</p>
<p>↓リスト12: 問題3の入力ファイル</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q3.SPAN
20130101 20130125
20130126 20130212
20130213 20130310
20130311 20130402
<span class="nv">$ </span>cat Q3.DAYS
20130102
20130203
20130209
20130312
20130313
20130429
</pre></div>
</td></tr></table></div>
<p>　筆者が「AWK1個だけ」という制限のもと、
最初に書いたワンライナーは次のようなものです。</p>
<p>↓リスト13: 解答その1</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{f[FNR]=$1;t[FNR]=$2}\\</span>
<span class="s1"> FILENAME~/DAYS/{for(k in f){\\</span>
<span class="s1"> if($1&gt;=f[k] &amp;&amp; $1&lt;=t[k]){sum[f[k]&quot; &quot;t[k]]++}}}\\</span>
<span class="s1"> END{for(k in sum){print k,sum[k]}}&#39;</span> Q3.SPAN Q3.DAYS
20130126 20130212 2
20130311 20130402 2
20130101 20130125 1
</pre></div>
</td></tr></table></div>
<p>これは完全にライトオンリーのコードなので読む必要はありません。
どんな処理か説明すると、次のようになります。</p>
<ul class="simple">
<li>最初のパターンで <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt> の各レコードを配列 <tt class="docutils literal"><span class="pre">f</span></tt> （from）、 <tt class="docutils literal"><span class="pre">t</span></tt> （to）に代入</li>
<li>次のパターンで <tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> の日付と <tt class="docutils literal"><span class="pre">f,t</span></tt> の内容を比較して、日付が期間中にあれば、期間に対応するカウンタ（ <tt class="docutils literal"><span class="pre">sum[&lt;期間&gt;]</span></tt> ）に1を足す</li>
<li>ENDパターンで、 各期間と <tt class="docutils literal"><span class="pre">sum</span></tt> の内容を出力</li>
</ul>
<p>変数 <tt class="docutils literal"><span class="pre">FILENAME</span></tt> にはオプションで指定したファイル名、
<tt class="docutils literal"><span class="pre">FNR</span></tt> には、各ファイル内でのレコード番号が予め代入されており、
このコードではそれをパターンや配列のインデックスに使っています。</p>
<p>　筆者は答えが出ればそれでOKという立場ですが、
もうちょっときれいに解いてみましょう。
シェルスクリプトでデータ処理を行うときは、
1レコードに計算する対象がすべて収まっていると楽な場合が多くなります。
ということは、予めそのような状態を作りにいけばよいということになります。</p>
<p>　ということで、まず、リスト14のように <tt class="docutils literal"><span class="pre">Q3.DAYS</span></tt> と <tt class="docutils literal"><span class="pre">Q3.SPAN</span></tt>
のレコードの組み合わせを全通り作ります。</p>
<p>↓リスト14: 解答その2</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{key[FNR]=$1&quot; &quot;$2}FILENAME~/DAYS/{for(k in key){print key[k],$1}}&#39;</span> Q3.SPAN Q3.DAYS
20130126 20130212 20130102
20130213 20130310 20130102
20130311 20130402 20130102
20130101 20130125 20130102
20130126 20130212 20130203
20130213 20130310 20130203
...
</pre></div>
</td></tr></table></div>
<p>こうなると、3列目の日付が1,2列目の日付の範囲に含まれているものを出力し、
数を数えるとよいということになります。
この方が、一個のAWKで頑張るよりすっきりしますね。</p>
<p>↓リスト15: 解答その3</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;FILENAME~/SPAN/{key[FNR]=$1&quot; &quot;$2}FILENAME~/DAYS/{for(k in key){print key[k],$1}}&#39;</span> Q3.SPAN Q3.DAYS | awk <span class="s1">&#39;$1&lt;=$3&amp;&amp;$3&lt;=$2{print $1,$2}&#39;</span> | uniq 
c- 1 20130101 20130125
 2 20130126 20130212
 2 20130311 20130402
</pre></div>
</td></tr></table></div>
<p>　これも、 Open usp Tukubai を使うともっと楽になります。
リスト16に解答を示します。
<tt class="docutils literal"><span class="pre">loopx</span></tt> は、上のリストの最初のAWKと同じ処理をしています。</p>
<p>↓リスト16: Open usp Tukubai を使った解答</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>loopx Q3.SPAN Q3.DAYS | awk <span class="s1">&#39;$1&lt;=$3&amp;&amp;$3&lt;=$2{print $1,$2}&#39;</span> | uniq 
c- 1 20130101 20130125
 2 20130126 20130212
 2 20130311 20130402
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id5">
<h2>17.5. 問題4<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　最後に、文章の処理を扱ってみましょう。
さばくのはリスト17のファイルです。
文章は、信じないようにしましょう。大嘘です。</p>
<p>↓リスト17: 問題4の入力ファイル</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO
「コロラド大ダンゴ虫」は、直径20cmになる世界最大のダンゴ虫。ダンゴ虫を転がし、トゲを抜いた柱状サボテンを倒して遊んだのが、ボーリングの始まり。
</pre></div>
</td></tr></table></div>
<p>　このファイルを、何かのフォームに貼付けるために、
20文字で折り返すというのが問題です。
さっそくやってみましょう。</p>
<p>↓リスト18: 解答その1</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |
 awk <span class="s1">&#39;{printf $1}NR%20==0{print &quot;&quot;}END{print &quot;&quot;}&#39;</span> &gt; tmp
<span class="nv">$ </span>cat tmp
「コロラド大ダンゴ虫」は、直径20cmに
なる世界最大のダンゴ虫。ダンゴ虫を転がし
、トゲを抜いた柱状サボテンを倒して遊んだ
のが、ボーリングの始まり。
</pre></div>
</td></tr></table></div>
<p>最初のgsedで一文字一文字、後ろに改行を入れて出力し、
次のAWKで20文字ずつまとめています。
単に文字列を改行しないで出力したい場合は、
この例のように <tt class="docutils literal"><span class="pre">printf</span></tt> を括弧なしで変数を指定して大丈夫です。</p>
<p>　この出力、少々問題があります。句点が一個、行頭に来ています。
句読点を21文字目にくっつけてよいなら、
リスト19のようにコードを書けばよいでしょう。</p>
<p>↓リスト19: 解答その2（句読点対応）</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;NR!=1{\\</span>
<span class="s1"> if($1~/^、/){print a&quot;、&quot;}else{print a}}\\</span>
<span class="s1"> {a=$1}END{print a}&#39;</span> | sed <span class="s1">&#39;s/^、//&#39;</span>
「コロラド大ダンゴ虫」は、直径20cmに
なる世界最大のダンゴ虫。ダンゴ虫を転がし、
トゲを抜いた柱状サボテンを倒して遊んだ
のが、ボーリングの始まり。
</pre></div>
</td></tr></table></div>
<p>　分かりにくいと思いますが、このAWKは「先読み」
という定石を使っています。実は問題1,2でも使っています。
リスト20のコードのように、
一行読み込んで一行前の行を出力するコードを書いて、
そこから必要なコードを足します。
そうすると、 <tt class="docutils literal"><span class="pre">a</span></tt> の出力をその次の行を見て操作できます。</p>
<p>↓リスト20: 先読みの骨組み</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;NR!=1{print a}{a=$1}END{print a}&#39;</span>
「コロラド大ダンゴ虫」は、直径20cmに
（以下略）
</pre></div>
</td></tr></table></div>
<p>　句読点も含めて20字で収めなければならないなら、
話はもっとややこしくなります。コードだけ示しておきますが、
ここまで来るとバグを取るのが大変でした。こうなったら、
字の折り返しのコマンドをちゃんと作ろうかという気になってきます。
もちろんコマンドにするなら、
句点だけでなく読点等にもちゃんと対応して汎用性を目指すことになります。</p>
<p>↓リスト21: 解答その3</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat Q4.MEMO | gsed <span class="s1">&#39;s/./&amp;\\n/g&#39;</span> |
awk <span class="s1">&#39;BEGIN{c=0}\\</span>
<span class="s1">NR!=1{if(c==19 &amp;&amp; $1==&quot;、&quot;){print &quot;&quot;;printf a;c=1}else{printf a;c++}}\\</span>
<span class="s1">c==20{print &quot;&quot;;c=0}{a=$1}END{print a}&#39;</span>
「コロラド大ダンゴ虫」は、直径20cmに
なる世界最大のダンゴ虫。ダンゴ虫を転が
し、トゲを抜いた柱状サボテンを倒して遊ん
だのが、ボーリングの始まり。
</pre></div>
</td></tr></table></div>
<p>　最後にどうでもよいことを述べると、
この出力の一字一字にカンマを挟み込んでcsvにすると、
あの悪名高き「エクセル方眼紙」に張り付きます。
やむなくエクセル方眼紙に字を書く羽目になったら、
お試しください。スジのいい人なら、
一字ずつ方眼紙で書く時間より、AWKを覚える時間の方が短いです。
そりゃ言い過ぎですね。失礼しました！</p>
</div>
<div class="section" id="id6">
<h2>17.6. 最後に<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はシェルスクリプトでテキスト処理する際につまずきやすい問題を、
AWKで解決してみました。このような類いの処理は無数にありますが、
先読みが使えるかどうかなど、パターンはそんなにないので、
慣れてしまうとシェル上でさばくことに抵抗が薄れてきます。
特に先読みは多くの集計処理に登場します。</p>
<p>　次回は、twitterでリクエストを受けたので、
netcatなどを使ってbashで通信を行ってみたいと思います。</p>
</div>
</div>


