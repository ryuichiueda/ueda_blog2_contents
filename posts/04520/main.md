---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年8月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>8. 開眼シェルスクリプト 第8回 パイプで早く仕事をやっつける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>8.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回からしばらく、コマンドに手分けさせて仕事をさせる方法を扱います。<br />
今のノートパソコンはCPUが2個以上あるものが多いので、<br />
これを休ませずに働かせます。</p><br />
<p>　今回扱うのは、最重要並列化テクニック：</p><br />
<p>「普通にパイプを使う」</p><br />
<p>です。え？何がテクニックか、と？<br />
先に答えを言ってしまうと、パイプにつなげたコマンドは並列に動作します。<br />
それを使おうというのが今回のお題です。</p><br />
<div class="section" id="id3"><br />
<h3>8.1.1. パイプにつながったコマンドの挙動<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　標準入力から字を受けて駆動するタイプ（つまりほとんど）のコマンドは、<br />
パイプやファイルからの入力がないと待ちの状態になります。<br />
ということは、パイプにつながったコマンドたちは、<br />
互いに影響を受けながら待ちの状態とアウトプットしている状態を繰り返します。<br />
たとえCPUが1個であっても、細かい時間間隔で各コマンドが入り乱れて動くので、<br />
パイプにつながったコマンドは同時に動いているように見えます。</p><br />
<p>　ここでCPUが2個あったらどうなるか考えてみます。<br />
CPUが1個でも細かい時間刻みで各コマンドが動いているということは、<br />
単純に考えてもう1個のCPUで半分受け持てばよいということになります。<br />
問題は、片方のCPUから発生する出力をもう一方のCPUに持っていく手間が必要になることですが、<br />
端末を操作している側の人間は気にしなくてよいほど効率化されています。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>8.1.2. パイプは基礎<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　ここ数年はCPUのマルチコア化によって様々な並列処理技術が開発されています。<br />
それに対してパイプは有難味を感じないほど取扱いが簡単です。<br />
この違いはいったい何なのかということになりますが、<br />
それは、OSから相対的に見たときに応用技術なのか基礎技術なのかという違いです。</p><br />
<p>　応用技術はOS側が要件を満たしていないと動きません。<br />
実際、派手な名前がついているフレームワークやソフトウェアでも、<br />
内部はパイプを使ったり、プロセスを操作したりとOSの機能を使っているわけです。<br />
また、どんなプラットフォームでも動くような技術は、<br />
様々な違いを吸収しなければなりません。<br />
そのため、OSの違いを吸収するライブラリなどが増えてしまいがちです。<br />
ですので、セットアップから使用までにどうしても手間がかかります。</p><br />
<p>　一方OSの各機能は、とにかく単機能でシンプルに使えるように実装されます。<br />
パイプなら「|」、ファイル入出力なら「&lt;、&gt;」など、<br />
ユーザがよく使うものはシェルから記号一つで呼び出せます。<br />
特にUNIX系OSで言えることですが、OSの開発者自身がOSのヘビーユーザなので、<br />
簡単ぶりが徹底されます。<br />
また、OSの評価は各機能のパフォーマンスと使いやすさで決まるので、<br />
開発や改良にかなり力が入る部分でもあります。<br />
パイプに関係する処理も、<br />
OSのメジャーバージョンアップの際にパフォーマンスが向上することがあります。</p><br />
<p>　あまり、あれがよいこれがよいと比較するつもりはないのですが、<br />
パイプについてはシェルで簡単に使えるよう、<br />
お膳立てされているので積極的に使うべきだと思います。<br />
少なくともOSの機能としては基礎の基礎なので、<br />
これを知らずに他の応用技術をあれこれ議論するのはよろしくありません。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h3>8.1.3. 故事<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　「パイプの発明者」は、ダグラス・マキルロイという人です。<br />
UNIXに実装される前後の経緯やマキルロイとトンプソンら同僚の様子について、[Hauben]<br />
（脚注：Hauben, On the Early History and Impact of Unix Tools to Build the Tools for a New Millenium,<br />
<a class="reference external" href="http://people.fas.harvard.edu/~lib113/reference/unix/unix2.html">http://people.fas.harvard.edu/~lib113/reference/unix/unix2.html</a>）<br />
におもしろい記述があります。この文献によると、<br />
パイプの導入はUNIXの開発では少し後回しになっていたものの、<br />
実装されると既存のUNIXコマンドの書き直しやgrepコマンドの誕生を誘発するなど、<br />
黎明期のUNIXに強烈なインパクトを与えたようです。</p><br />
</div><br />
</div><br />
<div class="section" id="cpu"><br />
<h2>8.2. お題：パイプを使ってCPUを使い切る<a class="headerlink" href="#cpu" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前置きが長くなってしまいました。手を動かしましょう。</p><br />
<div class="section" id="id6"><br />
<h3>8.2.1. 題材・環境<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　コアがいくつもあるサーバでやるとかなり派手な結果になりますが、<br />
今回はカジュアルにさりげなく（？）並列処理ができることを示したいので、<br />
昨年5万円で買ったノートパソコンで計測します。<br />
リスト1にスペック等を示します。</p><br />
<p>↓リスト1: 実験マシーン（Lenovo ThinkPad SL510）</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#CPUは2個（1個のデュアルコア）</span><br />
<span class="nv">$ </span>cat /proc/cpuinfo | grep <span class="s2">&quot;model name&quot;</span><br />
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz<br />
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 \@ 1.90GHz<br />
<span class="nv">$ </span>uname -a<br />
Linux uedaubuntu 3.2.0-24-generic <span class="c">#38-Ubuntu SMP Tue May 1 16:18:50 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux</span><br />
<span class="nv">$ </span>lsb_release -a 2&gt;/dev/null | grep Description<br />
Description: Ubuntu 12.04 LTS<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このノートPCで、原稿を書きつつネットサーフィンしながら計測するので、<br />
その影響も微妙に出ていることはご承知ください<br />
（脚注：あまり感心なことではありませんが、カジュアルさを演出ということで・・・）。<br />
また、工学部で博士号を取った人間としては問題大アリですが、<br />
「実験を十分統計量まで泥臭く繰り返して計測時間の平均とばらつきを出す」という、<br />
実験の基礎中の基礎も割愛します。先生（脚注：指導教官を指す。）ごめんなさい。</p><br />
<p>　実験に使うデータは、これまでの連載でさんざん使ってきたapacheのアクセスログです。<br />
USP友の会のサイト（<a class="reference external" href="http://www.usptomonokai.jp">http://www.usptomonokai.jp</a>）から、<br />
日ごとにgzip圧縮されているログをSL510にコピーして処理の対象とします。</p><br />
<div class="highlight-bash"><pre>$ ls<br />
access_log-20120213.gz<br />
...<br />
access_log-20120521.gz<br />
access_log-20120522.gz<br />
#中身（普通のapacheログ）<br />
#gzファイルはzcatを使うと読めます<br />
$ zcat access_log-20120522.gz | head -n 1<br />
219.94.249.xxx - - [21/May/2012:03:31:13 +0900] "GET /TOMONOKAI...（略）<br />
#行数は50万行弱<br />
$ zcat *.gz | wc -l<br />
424787<br />
#圧縮したの容量:3.6MB<br />
$ cat *.gz | wc -m<br />
3570682<br />
#解凍後の容量:97MB<br />
$ zcat *.gz | wc -m<br />
96886530</pre><br />
</div><br />
<p>　50万行程度ではあっという間に処理が終わってしまうので、<br />
実験用に、同じログを何回もくっつけて1GBのファイルを作ります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>zcat *.gz &gt; log<br />
<span class="c">#logファイルを11個くっつけて1GBのファイルを作る</span><br />
<span class="c">#ただcatするだけでは芸がないのでブレース展開を使ってみた</span><br />
<span class="nv">$ </span>cat log<span class="o">{</span>,,,,,,,,,,<span class="o">}</span> &gt; log1G<br />
<span class="nv">$ </span>ls -lh log1G<br />
-rw-rw-r-- 1 ueda ueda 1017M 5月 22 14:38 log1G<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>8.2.2. 処理時間の測り方<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　コマンドの処理時間は、timeコマンドで測ります。<br />
ファイルを全部解凍してファイルに出力する時間を測ってみましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz &gt; hoge<br />
<br />
real 0m0.957s<br />
user 0m0.588s<br />
sys 0m0.156s<br />
</pre></div><br />
</div><br />
<p>realが実際（我々の世界）でかかった時間、<br />
userとsysはそれぞれ、CPU時間（CPUが働いた時間）のうち、<br />
ユーザモードだった（カーネル以外のプログラムが動いた）時間、<br />
カーネルモードだった時間です。<br />
普通は何らかの原因でプログラムが待たされ、<br />
CPU時間よりもrealの時間が長くなります。</p><br />
<p>　計測の際、ハードディスクへの出力の遅延を気にしたくない場合は、<br />
次のように <tt class="docutils literal"><span class="pre">/dev/null</span></tt> というところに出力をリダイレクトします。<br />
この例の場合は、ほぼ <tt class="docutils literal"><span class="pre">read</span> <span class="pre">=</span> <span class="pre">user</span> <span class="pre">+</span> <span class="pre">sys</span></tt> になっています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz &gt; /dev/null<br />
<br />
real 0m0.563s<br />
user 0m0.560s<br />
sys 0m0.004s<br />
</pre></div><br />
</div><br />
<p>　 <tt class="docutils literal"><span class="pre">/dev/null</span></tt> （ビットバケツ）はなんでも吸い込んで消してしまう特殊なファイルです。<br />
コマンドの出力をここにリダイレクトしておくと、<br />
消えてなくなります。<br />
コマンドは接続先が <tt class="docutils literal"><span class="pre">/dev/null</span></tt> でも律儀に出力を行うので、<br />
この時間は計測されます。<br />
ちなみに、筆者は <tt class="docutils literal"><span class="pre">/dev/null</span></tt> を「デブヌル」と呼んでいます。</p><br />
<p>　もう一つ、パイプでつながっていないコマンドの処理時間を端末で計測したいときには、<br />
以下のようにコマンドをセミコロンで区切って括弧で囲む方法があります。<br />
あるいはシェルスクリプトにして、 <tt class="docutils literal"><span class="pre">$</span> <span class="pre">time</span> <span class="pre">./hoge.sh</span></tt> のように呼び出してもよいでしょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> <span class="o">(</span> sleep 1 ; sleep 2 <span class="o">)</span><br />
<br />
real 0m3.003s<br />
user 0m0.000s<br />
sys 0m0.000s<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h3>8.2.3. パイプラインの並列処理<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、まずパイプを使うと何が起こるか見てみましょう。</p><br />
<p>リスト2：パイプを使う</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G &gt; /dev/null<br />
<br />
real 0m12.439s<br />
user 0m10.505s<br />
sys 0m0.876s<br />
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/b/a/g&#39;</span> &gt; /dev/null<br />
<br />
real 0m14.938s<br />
user 0m24.338s<br />
sys 0m1.900s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト2の上の処理は <tt class="docutils literal"><span class="pre">log1G</span></tt> ファイルをsedコマンドで読み込み、<br />
aをすべてbに置換しています。<br />
下の処理では、さらにパイプの後ろにsedコマンドをつなげ、<br />
bをaに置換しています。<br />
下の処理の方が2.5[s]遅いですが、注目すべきはuserの値がrealの値を上回っていることです。<br />
実際にかかった時間よりもCPU時間が長いということは、<br />
平均してCPUが1個以上使われているということになり、<br />
並列化されているということになります。<br />
リスト3は、処理中にtopコマンドを打ってみたものです。<br />
sedのCPU使用率が92%と82%で、足すとsedだけで1.7個CPUを使用していることになります。</p><br />
<p>リスト3: sedをパイプでつないだ処理中のtop</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>top -n 1 -b | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 5<br />
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND<br />
13108 ueda 20 0 16644 832 704 R 92 0.0 0:04.37 sed<br />
13107 ueda 20 0 16644 828 704 R 82 0.0 0:03.82 sed<br />
 1089 root 20 0 198m 25m 6480 S 2 1.4 5:40.79 Xorg<br />
 2023 ueda 20 0 1261m 64m 10m S 2 3.4 4:06.40 compiz<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ちなみに、この処理をパイプを使わずに行うとこうなります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G &gt; hoge ; sed <span class="s1">&#39;s/b/a/g&#39;</span> &lt; hoge &gt; /dev/null ; rm hoge<br />
<br />
real 0m43.570s<br />
user 0m23.893s<br />
sys 0m4.480s<br />
</pre></div><br />
</div><br />
<p>当然、途中でファイルに書き出す手間がかかるので、時間を食うことになります。<br />
また、中間ファイルは消さないといけません。<br />
書き方もゴテゴテしています。面倒です。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h3>8.2.4. もっとつなぐとどうなるか？<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　パイプで並列処理ができるとなると、<br />
どこまでパイプでつないでよいのかという疑問が生じます。<br />
普通、この手のテクニックは度が過ぎるとパフォーマンスが落ちるものです。</p><br />
<p>　実験をしてみます。<br />
sedで1GBのファイルのアルファベットを一文字ずつ変換してみます。<br />
下のコマンドラインのように、aをb、cをd・・・<br />
と変換するsedコマンドをパイプで数珠つなぎにして処理時間を計測します。<br />
sedの数は1～13まで変化させます。<br />
処理の総量はsedの数に比例して大きくなります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#2個連結</span><br />
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/c/d/g&#39;</span> &gt; /dev/null<br />
<span class="c">#13個連結</span><br />
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/c/d/g&#39;</span> | <span class="o">(</span>略<span class="o">)</span> | sed <span class="s1">&#39;s/w/x/g&#39;</span> | sed <span class="s1">&#39;s/y/z/g&#39;</span> &gt; /dev/null<br />
</pre></div><br />
</div><br />
<p>　計測は、これまで使ってきたノートPCの他に、<br />
CPUを8コア持っているサーバ機でもやってみました。<br />
スペックは書きませんが、CPUを8個全部使えることができれば、<br />
高い並列化の効果を観測できるかもしれません。</p><br />
<p>　図1に、計時結果をグラフを示します。<br />
（脚注：これもシェルスクリプトで描いています。4月号・5月号参考のこと。<br />
細かくデザインしやすいからで、別に意固地になっているわけではありません。）</p><br />
<p>↓図1：処理時間</p><br />
<div class="figure"><br />
<img alt="_images/PIPETIME.PNG" src="PIPETIME.png" /><br />
</div><br />
<p>ほぼ線形で時間が増えており、<br />
処理量に比例して時間が増えているように見えます。<br />
この図ではあまり傾向がつかめないので、<br />
計測時間をsedの数で割ってみたものを図2に示します。<br />
この図は、同じ処理量で計算能力を比較したものになります。<br />
（ただし、ファイルを読み出す時間を考慮するとsedの数が多い方が若干有利な値になります。）</p><br />
<p>↓図2：sed一個あたりの処理時間</p><br />
<div class="figure"><br />
<img alt="_images/PIPEPERTIME.PNG" src="PIPEPERTIME.png" /><br />
</div><br />
<p>こちらの図は並列化の効果がよくわかります。<br />
どちらのマシンでも、sedが1個のときよりも2個のときの方が、<br />
時間あたりにたくさんの処理をこなしています。<br />
8CPUのサーバの場合は、7個あたりまで時間が短くなっています。</p><br />
<p>　また、パイプでつながったsedの数がCPUの数を上回っても、<br />
この範囲のsedの数では性能が落ちないことも分かります。<br />
つまり、思いつく限りずらずらコマンドをパイプで並べていってもパイプが詰まる心配は小さいと言えます。</p><br />
</div><br />
<div class="section" id="id10"><br />
<h3>8.2.5. 負荷にばらつきがある場合<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　sedの実験では、それぞれのsedの負荷にあまり違いがないようにしていましたが、<br />
そうでないときはどうなるでしょうか？</p><br />
<p>　例えば、同じ置換のコマンドであっても、trコマンドはsedに比べてかなり高速です。<br />
そのため、sedとtrをパイプでつなげると、順序はどっちでも、<br />
リスト4の例のようにtrの方が遊んでしまいます。</p><br />
<p>リスト4：sedとtrをつなげるとtrが遊ぶ</p><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> &gt; /dev/null<br />
<span class="c">#別のターミナルでtopを打ったときの出力の抜粋</span><br />
<span class="c">#sedの出力をtrが待ってしまう</span><br />
%CPU %MEM TIME+ COMMAND<br />
 96 0.0 0:07.82 sed<br />
 23 0.0 0:01.89 tr<br />
 10 14.4 12:03.30 chromium-browse<br />
 2 0.0 0:03.36 kswapd0<br />
<br />
<span class="c">#trを先にしてみる</span><br />
<span class="nv">$ </span>tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/a/b/g&#39;</span> &gt; /dev/null<br />
<span class="c">#別のターミナルでtopを打ってみる</span><br />
<span class="c">#sedが入力を受け付けるまでtrが待ってしまう</span><br />
%CPU %MEM TIME+ COMMAND<br />
 86 0.0 0:03.25 sed<br />
 29 0.0 0:01.04 tr<br />
 2 0.0 0:04.23 kswapd0<br />
 2 1.1 8:51.42 Xorg<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　また、grepで検索した結果を後続のコマンドで処理するというのはよくあることですが、<br />
このときは後のコマンドで扱うデータ量が少ないので、これも負荷に違いが出ます。<br />
例えば次のワンライナーでは、grepとawkで扱うレコード数が数倍違うので、<br />
負荷もそれくらいの違いが出ます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#「Chrome」という単語のある</span><br />
<span class="c">#レコードからIPと時刻を抜き出す</span><br />
<span class="nv">$ </span>grep Chrome log1G | awk <span class="s1">&#39;{print $1,$4,$5}&#39;</span><br />
114.182.aaa.xxx <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span><br />
114.182.aaa.xxx <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span><br />
・・・<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これら場合は、一番負荷の高いコマンドの処理時間以上に処理が早く終わることはありません。<br />
これはパイプの並列化の限界で、<br />
もしもっと早い処理が必要ならば、別の方法をとる必要があります。</p><br />
<p>　ただし、負荷の高いコマンドを待っている間にCPUを効率的に使うことは可能です。<br />
下の例のように、sedがほぼ1個分のCPUを占領していても、<br />
他のコマンドの負荷が軽ければそちらで勝手に処理が分散されます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> |<br />
tr <span class="s1">&#39;e&#39;</span> <span class="s1">&#39;f&#39;</span> | tr <span class="s1">&#39;g&#39;</span> <span class="s1">&#39;h&#39;</span> | tr <span class="s1">&#39;i&#39;</span> <span class="s1">&#39;j&#39;</span> |<br />
tr <span class="s1">&#39;k&#39;</span> <span class="s1">&#39;l&#39;</span> &gt; /dev/null<br />
<br />
<span class="c">#topの抜粋。sedで82%、あとのtrで91%</span><br />
%CPU %MEM TIME+ COMMAND<br />
 82 0.0 0:04.95 sed<br />
 19 0.0 0:01.28 tr<br />
 16 0.0 0:00.92 tr<br />
 14 0.0 0:00.90 tr<br />
 14 0.0 0:00.86 tr<br />
 14 0.0 0:00.90 tr<br />
 14 0.0 0:00.82 tr<br />
</pre></div><br />
</div><br />
<p>　冒頭で、<br />
「たとえCPUが1個であっても、細かい時間間隔で各コマンドが入り乱れて動く」<br />
と言ったように、コマンドを二つつなげたらそれぞれがCPUを一個ずつ占領するわけではありません。<br />
パイプにコマンドが3個以上あっても、<br />
CPUが遊ばないように負荷分散されます。<br />
パイプが何段必要かは処理によって違うので、<br />
無理にパイプをつなげて処理することはありませんが、<br />
ちょっと頭の隅に置いておくとよいでしょう。</p><br />
<p>　もう一つ、特にawkやsedを使って重たい処理をする場合に実践的な方法ですが、<br />
処理を分割すると早くなるという例を下に示します。</p><br />
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#このような、日付と時刻を加工する処理</span><br />
<span class="c">#入力</span><br />
114.182.aaa.xxx - - <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span> <span class="s2">&quot;GET （略）</span><br />
<span class="s2">#出力</span><br />
<span class="s2">114.182.aaa.xxx - - [ 05 Feb 2012 162446 +0900] &quot;</span>GET （略）<br />
<br />
<span class="c">#一個のsedで処理</span><br />
<span class="c">#sedで置換ルールを二つ以上指定するときは-eというオプションを使う</span><br />
<span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s\@\\(..\\)/\\(...\\)/\\(....\\)\@ \\1 \\2 \\3\@&#39;</span> -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &lt; log1G &gt; /dev/null<br />
<br />
real 0m29.488s<br />
user 0m28.994s<br />
sys 0m0.492s<br />
<span class="c">#日付の処理と時刻の処理を分割</span><br />
<span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s\@\\(..\\)/\\(...\\)/\\(....\\)\@ \\1 \\2 \\3\@&#39;</span> &lt; log1G | sed -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &gt; /dev/null<br />
<br />
real 0m22.807s<br />
user 0m32.382s<br />
sys 0m2.064s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>ハードディスクの読み出しよりも処理がボトルネックになる場合は、<br />
このように処理を分割した方が処理が早く終わる場合が多いです。<br />
また、シェルスクリプトの場合は分けて書いた方が読みやすくなります。</p><br />
<p>　これの処理については、先ほどパイプをたくさんつなげる実験をした8CPUのサーバでもやってみました。<br />
たくさんコマンドをつなげることに抵抗がなければ、CPUが多い環境だとこれだけ速くなるという例です。<br />
ちょっといい加減なコードですが・・・。</p><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s\@\\(..\\)/\\(...\\)/\\(....\\)\@ \\1 \\2 \\3\@&#39;</span> -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &lt; log1G &gt; /dev/null<br />
<br />
real 0m17.551s<br />
user 0m17.209s<br />
sys 0m0.303s<br />
<br />
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/\\[/&amp; /&#39;</span> &lt; log1G | sed <span class="s1">&#39;s\@/\@ \@&#39;</span> | sed <span class="s1">&#39;s\@/\@ \@&#39;</span> | sed <span class="s1">&#39;s/:/ /&#39;</span> | sed <span class="s1">&#39;s/://&#39;</span> | sed <span class="s1">&#39;s/://&#39;</span> &gt; /dev/null<br />
<br />
real 0m5.773s<br />
user 0m17.252s<br />
sys 0m10.959s<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id11"><br />
<h3>8.2.6. データをブロックするコマンドがある場合<a class="headerlink" href="#id11" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　sortのように全部データを読み込まないと出力をしないコマンドも、<br />
ボトルネックになります。<br />
次の場合、sortが終わるまで、awk以後の処理は開始しません。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz | sort | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq <br />
c-</pre></div><br />
</td></tr></table></div><br />
<p>これも無理に回避する必要はありませんが、<br />
早く処理を終わらせるテクニックはあります。</p><br />
<p>　上の例の場合は、単純にgrepとawkの順序を変えるだけでかなり処理時間が違ってきます。</p><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz | sort | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq -c | head -n 3<br />
 10 1.112.aaa.xxx<br />
 37 1.112.bbb.yyy<br />
 10 1.112.ccc.zzz<br />
<br />
real 0m5.561s<br />
user 0m4.544s<br />
sys 0m0.384s<br />
<span class="nv">$ </span><span class="nb">time </span>zcat *.gz | awk <span class="s1">&#39;{print $1}&#39;</span> | sort | uniq -c | head -n 3<br />
 10 1.112.aaa.xxx<br />
 37 1.112.bbb.yyy<br />
 10 1.112.ccc.zzz<br />
<br />
real 0m1.991s<br />
user 0m2.452s<br />
sys 0m0.144s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この例では単にsortに入れるデータ量を減らすということが効率の改善になっていますが、<br />
例えば後者の並び次の二つのグループが同時に実行されることが分かっていることも大事です。</p><br />
<ul class="simple"><br />
<li>zcat、awk、sortのデータ読み込み</li><br />
<li>sortの出力、uniq、head</li><br />
</ul><br />
<p>実際、後者のreal値とuser値が逆転しているように、<br />
並列化の効果はsortが間にあってもちゃんと出ています。</p><br />
</div><br />
</div><br />
<div class="section" id="id12"><br />
<h2>8.3. 終わりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、パイプにコマンドをつないで並列化するというお題を扱いました。<br />
今回はシェルスクリプトは出てきませんでしたが、<br />
たくさんデータを処理するシェルスクリプトを書く際には必須の知識です。<br />
実際のところ、CPUが2個程度だとあまり効果を体感することは少ないと思いますが、<br />
コマンドを何個もつないでもパフォーマンスには影響が出ないどころか、<br />
かえって改善するということはお見せできたと思います。<br />
CPUが多いと、実験で出てきたサーバ機のように効果は明確になります。</p><br />
<p>　また、マキルロイについて触れましたが、<br />
パイプはUNIXの特性に大きな影響を与えています。<br />
私がパイプ教団の信者であろうがパイプエバンジェリストであろうがそんなこととは関係なく、<br />
パイプの発明が我々に大きな恩恵を与えていることは疑いのないことでしょう。<br />
パイプは通信の方式とも言えますが、<br />
これがインターネットに間接的に与えた影響についても考えてみると良いかもしれません。</p><br />
<p>　ここまでパイプを持ち上げておいてなんですが、<br />
次回はパイプを使わないで並列化する方法について扱ってみたいと思います。</p><br />
</div><br />
</div><br />

