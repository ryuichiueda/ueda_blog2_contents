---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年8月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>8. 開眼シェルスクリプト 第8回 パイプで早く仕事をやっつける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>8.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回からしばらく、コマンドに手分けさせて仕事をさせる方法を扱います。
今のノートパソコンはCPUが2個以上あるものが多いので、
これを休ませずに働かせます。</p>
<p>　今回扱うのは、最重要並列化テクニック：</p>
<p>「普通にパイプを使う」</p>
<p>です。え？何がテクニックか、と？
先に答えを言ってしまうと、パイプにつなげたコマンドは並列に動作します。
それを使おうというのが今回のお題です。</p>
<div class="section" id="id3">
<h3>8.1.1. パイプにつながったコマンドの挙動<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　標準入力から字を受けて駆動するタイプ（つまりほとんど）のコマンドは、
パイプやファイルからの入力がないと待ちの状態になります。
ということは、パイプにつながったコマンドたちは、
互いに影響を受けながら待ちの状態とアウトプットしている状態を繰り返します。
たとえCPUが1個であっても、細かい時間間隔で各コマンドが入り乱れて動くので、
パイプにつながったコマンドは同時に動いているように見えます。</p>
<p>　ここでCPUが2個あったらどうなるか考えてみます。
CPUが1個でも細かい時間刻みで各コマンドが動いているということは、
単純に考えてもう1個のCPUで半分受け持てばよいということになります。
問題は、片方のCPUから発生する出力をもう一方のCPUに持っていく手間が必要になることですが、
端末を操作している側の人間は気にしなくてよいほど効率化されています。</p>
</div>
<div class="section" id="id4">
<h3>8.1.2. パイプは基礎<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　ここ数年はCPUのマルチコア化によって様々な並列処理技術が開発されています。
それに対してパイプは有難味を感じないほど取扱いが簡単です。
この違いはいったい何なのかということになりますが、
それは、OSから相対的に見たときに応用技術なのか基礎技術なのかという違いです。</p>
<p>　応用技術はOS側が要件を満たしていないと動きません。
実際、派手な名前がついているフレームワークやソフトウェアでも、
内部はパイプを使ったり、プロセスを操作したりとOSの機能を使っているわけです。
また、どんなプラットフォームでも動くような技術は、
様々な違いを吸収しなければなりません。
そのため、OSの違いを吸収するライブラリなどが増えてしまいがちです。
ですので、セットアップから使用までにどうしても手間がかかります。</p>
<p>　一方OSの各機能は、とにかく単機能でシンプルに使えるように実装されます。
パイプなら「|」、ファイル入出力なら「&lt;、&gt;」など、
ユーザがよく使うものはシェルから記号一つで呼び出せます。
特にUNIX系OSで言えることですが、OSの開発者自身がOSのヘビーユーザなので、
簡単ぶりが徹底されます。
また、OSの評価は各機能のパフォーマンスと使いやすさで決まるので、
開発や改良にかなり力が入る部分でもあります。
パイプに関係する処理も、
OSのメジャーバージョンアップの際にパフォーマンスが向上することがあります。</p>
<p>　あまり、あれがよいこれがよいと比較するつもりはないのですが、
パイプについてはシェルで簡単に使えるよう、
お膳立てされているので積極的に使うべきだと思います。
少なくともOSの機能としては基礎の基礎なので、
これを知らずに他の応用技術をあれこれ議論するのはよろしくありません。</p>
</div>
<div class="section" id="id5">
<h3>8.1.3. 故事<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　「パイプの発明者」は、ダグラス・マキルロイという人です。
UNIXに実装される前後の経緯やマキルロイとトンプソンら同僚の様子について、[Hauben]
（脚注：Hauben, On the Early History and Impact of Unix Tools to Build the Tools for a New Millenium,
<a class="reference external" href="http://people.fas.harvard.edu/~lib113/reference/unix/unix2.html">http://people.fas.harvard.edu/~lib113/reference/unix/unix2.html</a>）
におもしろい記述があります。この文献によると、
パイプの導入はUNIXの開発では少し後回しになっていたものの、
実装されると既存のUNIXコマンドの書き直しやgrepコマンドの誕生を誘発するなど、
黎明期のUNIXに強烈なインパクトを与えたようです。</p>
</div>
</div>
<div class="section" id="cpu">
<h2>8.2. お題：パイプを使ってCPUを使い切る<a class="headerlink" href="#cpu" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前置きが長くなってしまいました。手を動かしましょう。</p>
<div class="section" id="id6">
<h3>8.2.1. 題材・環境<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　コアがいくつもあるサーバでやるとかなり派手な結果になりますが、
今回はカジュアルにさりげなく（？）並列処理ができることを示したいので、
昨年5万円で買ったノートパソコンで計測します。
リスト1にスペック等を示します。</p>
<p>↓リスト1: 実験マシーン（Lenovo ThinkPad SL510）</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#CPUは2個（1個のデュアルコア）</span>
<span class="nv">$ </span>cat /proc/cpuinfo | grep <span class="s2">&quot;model name&quot;</span>
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 @ 1.90GHz
model name : Celeron<span class="o">(</span>R<span class="o">)</span> Dual-Core CPU T3100 @ 1.90GHz
<span class="nv">$ </span>uname -a
Linux uedaubuntu 3.2.0-24-generic <span class="c">#38-Ubuntu SMP Tue May 1 16:18:50 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux</span>
<span class="nv">$ </span>lsb_release -a 2&gt;/dev/null | grep Description
Description: Ubuntu 12.04 LTS
</pre></div>
</td></tr></table></div>
<p>　このノートPCで、原稿を書きつつネットサーフィンしながら計測するので、
その影響も微妙に出ていることはご承知ください
（脚注：あまり感心なことではありませんが、カジュアルさを演出ということで・・・）。
また、工学部で博士号を取った人間としては問題大アリですが、
「実験を十分統計量まで泥臭く繰り返して計測時間の平均とばらつきを出す」という、
実験の基礎中の基礎も割愛します。先生（脚注：指導教官を指す。）ごめんなさい。</p>
<p>　実験に使うデータは、これまでの連載でさんざん使ってきたapacheのアクセスログです。
USP友の会のサイト（<a class="reference external" href="http://www.usptomonokai.jp">http://www.usptomonokai.jp</a>）から、
日ごとにgzip圧縮されているログをSL510にコピーして処理の対象とします。</p>
<div class="highlight-bash"><pre>$ ls
access_log-20120213.gz
...
access_log-20120521.gz
access_log-20120522.gz
#中身（普通のapacheログ）
#gzファイルはzcatを使うと読めます
$ zcat access_log-20120522.gz | head -n 1
219.94.249.xxx - - [21/May/2012:03:31:13 +0900] "GET /TOMONOKAI...（略）
#行数は50万行弱
$ zcat *.gz | wc -l
424787
#圧縮したの容量:3.6MB
$ cat *.gz | wc -m
3570682
#解凍後の容量:97MB
$ zcat *.gz | wc -m
96886530</pre>
</div>
<p>　50万行程度ではあっという間に処理が終わってしまうので、
実験用に、同じログを何回もくっつけて1GBのファイルを作ります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>zcat *.gz &gt; log
<span class="c">#logファイルを11個くっつけて1GBのファイルを作る</span>
<span class="c">#ただcatするだけでは芸がないのでブレース展開を使ってみた</span>
<span class="nv">$ </span>cat log<span class="o">{</span>,,,,,,,,,,<span class="o">}</span> &gt; log1G
<span class="nv">$ </span>ls -lh log1G
-rw-rw-r-- 1 ueda ueda 1017M 5月 22 14:38 log1G
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h3>8.2.2. 処理時間の測り方<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　コマンドの処理時間は、timeコマンドで測ります。
ファイルを全部解凍してファイルに出力する時間を測ってみましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz &gt; hoge

real 0m0.957s
user 0m0.588s
sys 0m0.156s
</pre></div>
</div>
<p>realが実際（我々の世界）でかかった時間、
userとsysはそれぞれ、CPU時間（CPUが働いた時間）のうち、
ユーザモードだった（カーネル以外のプログラムが動いた）時間、
カーネルモードだった時間です。
普通は何らかの原因でプログラムが待たされ、
CPU時間よりもrealの時間が長くなります。</p>
<p>　計測の際、ハードディスクへの出力の遅延を気にしたくない場合は、
次のように <tt class="docutils literal"><span class="pre">/dev/null</span></tt> というところに出力をリダイレクトします。
この例の場合は、ほぼ <tt class="docutils literal"><span class="pre">read</span> <span class="pre">=</span> <span class="pre">user</span> <span class="pre">+</span> <span class="pre">sys</span></tt> になっています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz &gt; /dev/null

real 0m0.563s
user 0m0.560s
sys 0m0.004s
</pre></div>
</div>
<p>　 <tt class="docutils literal"><span class="pre">/dev/null</span></tt> （ビットバケツ）はなんでも吸い込んで消してしまう特殊なファイルです。
コマンドの出力をここにリダイレクトしておくと、
消えてなくなります。
コマンドは接続先が <tt class="docutils literal"><span class="pre">/dev/null</span></tt> でも律儀に出力を行うので、
この時間は計測されます。
ちなみに、筆者は <tt class="docutils literal"><span class="pre">/dev/null</span></tt> を「デブヌル」と呼んでいます。</p>
<p>　もう一つ、パイプでつながっていないコマンドの処理時間を端末で計測したいときには、
以下のようにコマンドをセミコロンで区切って括弧で囲む方法があります。
あるいはシェルスクリプトにして、 <tt class="docutils literal"><span class="pre">$</span> <span class="pre">time</span> <span class="pre">./hoge.sh</span></tt> のように呼び出してもよいでしょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> <span class="o">(</span> sleep 1 ; sleep 2 <span class="o">)</span>

real 0m3.003s
user 0m0.000s
sys 0m0.000s
</pre></div>
</div>
</div>
<div class="section" id="id8">
<h3>8.2.3. パイプラインの並列処理<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、まずパイプを使うと何が起こるか見てみましょう。</p>
<p>リスト2：パイプを使う</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G &gt; /dev/null

real 0m12.439s
user 0m10.505s
sys 0m0.876s
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/b/a/g&#39;</span> &gt; /dev/null

real 0m14.938s
user 0m24.338s
sys 0m1.900s
</pre></div>
</td></tr></table></div>
<p>リスト2の上の処理は <tt class="docutils literal"><span class="pre">log1G</span></tt> ファイルをsedコマンドで読み込み、
aをすべてbに置換しています。
下の処理では、さらにパイプの後ろにsedコマンドをつなげ、
bをaに置換しています。
下の処理の方が2.5[s]遅いですが、注目すべきはuserの値がrealの値を上回っていることです。
実際にかかった時間よりもCPU時間が長いということは、
平均してCPUが1個以上使われているということになり、
並列化されているということになります。
リスト3は、処理中にtopコマンドを打ってみたものです。
sedのCPU使用率が92%と82%で、足すとsedだけで1.7個CPUを使用していることになります。</p>
<p>リスト3: sedをパイプでつないだ処理中のtop</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>top -n 1 -b | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 5
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
13108 ueda 20 0 16644 832 704 R 92 0.0 0:04.37 sed
13107 ueda 20 0 16644 828 704 R 82 0.0 0:03.82 sed
 1089 root 20 0 198m 25m 6480 S 2 1.4 5:40.79 Xorg
 2023 ueda 20 0 1261m 64m 10m S 2 3.4 4:06.40 compiz
</pre></div>
</td></tr></table></div>
<p>　ちなみに、この処理をパイプを使わずに行うとこうなります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G &gt; hoge ; sed <span class="s1">&#39;s/b/a/g&#39;</span> &lt; hoge &gt; /dev/null ; rm hoge

real 0m43.570s
user 0m23.893s
sys 0m4.480s
</pre></div>
</div>
<p>当然、途中でファイルに書き出す手間がかかるので、時間を食うことになります。
また、中間ファイルは消さないといけません。
書き方もゴテゴテしています。面倒です。</p>
</div>
<div class="section" id="id9">
<h3>8.2.4. もっとつなぐとどうなるか？<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　パイプで並列処理ができるとなると、
どこまでパイプでつないでよいのかという疑問が生じます。
普通、この手のテクニックは度が過ぎるとパフォーマンスが落ちるものです。</p>
<p>　実験をしてみます。
sedで1GBのファイルのアルファベットを一文字ずつ変換してみます。
下のコマンドラインのように、aをb、cをd・・・
と変換するsedコマンドをパイプで数珠つなぎにして処理時間を計測します。
sedの数は1～13まで変化させます。
処理の総量はsedの数に比例して大きくなります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#2個連結</span>
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/c/d/g&#39;</span> &gt; /dev/null
<span class="c">#13個連結</span>
<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/c/d/g&#39;</span> | <span class="o">(</span>略<span class="o">)</span> | sed <span class="s1">&#39;s/w/x/g&#39;</span> | sed <span class="s1">&#39;s/y/z/g&#39;</span> &gt; /dev/null
</pre></div>
</div>
<p>　計測は、これまで使ってきたノートPCの他に、
CPUを8コア持っているサーバ機でもやってみました。
スペックは書きませんが、CPUを8個全部使えることができれば、
高い並列化の効果を観測できるかもしれません。</p>
<p>　図1に、計時結果をグラフを示します。
（脚注：これもシェルスクリプトで描いています。4月号・5月号参考のこと。
細かくデザインしやすいからで、別に意固地になっているわけではありません。）</p>
<p>↓図1：処理時間</p>
<div class="figure">
<img alt="_images/PIPETIME.PNG" src="PIPETIME.png" />
</div>
<p>ほぼ線形で時間が増えており、
処理量に比例して時間が増えているように見えます。
この図ではあまり傾向がつかめないので、
計測時間をsedの数で割ってみたものを図2に示します。
この図は、同じ処理量で計算能力を比較したものになります。
（ただし、ファイルを読み出す時間を考慮するとsedの数が多い方が若干有利な値になります。）</p>
<p>↓図2：sed一個あたりの処理時間</p>
<div class="figure">
<img alt="_images/PIPEPERTIME.PNG" src="PIPEPERTIME.png" />
</div>
<p>こちらの図は並列化の効果がよくわかります。
どちらのマシンでも、sedが1個のときよりも2個のときの方が、
時間あたりにたくさんの処理をこなしています。
8CPUのサーバの場合は、7個あたりまで時間が短くなっています。</p>
<p>　また、パイプでつながったsedの数がCPUの数を上回っても、
この範囲のsedの数では性能が落ちないことも分かります。
つまり、思いつく限りずらずらコマンドをパイプで並べていってもパイプが詰まる心配は小さいと言えます。</p>
</div>
<div class="section" id="id10">
<h3>8.2.5. 負荷にばらつきがある場合<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　sedの実験では、それぞれのsedの負荷にあまり違いがないようにしていましたが、
そうでないときはどうなるでしょうか？</p>
<p>　例えば、同じ置換のコマンドであっても、trコマンドはsedに比べてかなり高速です。
そのため、sedとtrをパイプでつなげると、順序はどっちでも、
リスト4の例のようにtrの方が遊んでしまいます。</p>
<p>リスト4：sedとtrをつなげるとtrが遊ぶ</p>
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> &gt; /dev/null
<span class="c">#別のターミナルでtopを打ったときの出力の抜粋</span>
<span class="c">#sedの出力をtrが待ってしまう</span>
%CPU %MEM TIME+ COMMAND
 96 0.0 0:07.82 sed
 23 0.0 0:01.89 tr
 10 14.4 12:03.30 chromium-browse
 2 0.0 0:03.36 kswapd0

<span class="c">#trを先にしてみる</span>
<span class="nv">$ </span>tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> &lt; log1G | sed <span class="s1">&#39;s/a/b/g&#39;</span> &gt; /dev/null
<span class="c">#別のターミナルでtopを打ってみる</span>
<span class="c">#sedが入力を受け付けるまでtrが待ってしまう</span>
%CPU %MEM TIME+ COMMAND
 86 0.0 0:03.25 sed
 29 0.0 0:01.04 tr
 2 0.0 0:04.23 kswapd0
 2 1.1 8:51.42 Xorg
</pre></div>
</td></tr></table></div>
<p>　また、grepで検索した結果を後続のコマンドで処理するというのはよくあることですが、
このときは後のコマンドで扱うデータ量が少ないので、これも負荷に違いが出ます。
例えば次のワンライナーでは、grepとawkで扱うレコード数が数倍違うので、
負荷もそれくらいの違いが出ます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#「Chrome」という単語のある</span>
<span class="c">#レコードからIPと時刻を抜き出す</span>
<span class="nv">$ </span>grep Chrome log1G | awk <span class="s1">&#39;{print $1,$4,$5}&#39;</span>
114.182.aaa.xxx <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span>
114.182.aaa.xxx <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span>
・・・
</pre></div>
</td></tr></table></div>
<p>　これら場合は、一番負荷の高いコマンドの処理時間以上に処理が早く終わることはありません。
これはパイプの並列化の限界で、
もしもっと早い処理が必要ならば、別の方法をとる必要があります。</p>
<p>　ただし、負荷の高いコマンドを待っている間にCPUを効率的に使うことは可能です。
下の例のように、sedがほぼ1個分のCPUを占領していても、
他のコマンドの負荷が軽ければそちらで勝手に処理が分散されます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/a/b/g&#39;</span> &lt; log1G | tr <span class="s1">&#39;c&#39;</span> <span class="s1">&#39;d&#39;</span> |
tr <span class="s1">&#39;e&#39;</span> <span class="s1">&#39;f&#39;</span> | tr <span class="s1">&#39;g&#39;</span> <span class="s1">&#39;h&#39;</span> | tr <span class="s1">&#39;i&#39;</span> <span class="s1">&#39;j&#39;</span> |
tr <span class="s1">&#39;k&#39;</span> <span class="s1">&#39;l&#39;</span> &gt; /dev/null

<span class="c">#topの抜粋。sedで82%、あとのtrで91%</span>
%CPU %MEM TIME+ COMMAND
 82 0.0 0:04.95 sed
 19 0.0 0:01.28 tr
 16 0.0 0:00.92 tr
 14 0.0 0:00.90 tr
 14 0.0 0:00.86 tr
 14 0.0 0:00.90 tr
 14 0.0 0:00.82 tr
</pre></div>
</div>
<p>　冒頭で、
「たとえCPUが1個であっても、細かい時間間隔で各コマンドが入り乱れて動く」
と言ったように、コマンドを二つつなげたらそれぞれがCPUを一個ずつ占領するわけではありません。
パイプにコマンドが3個以上あっても、
CPUが遊ばないように負荷分散されます。
パイプが何段必要かは処理によって違うので、
無理にパイプをつなげて処理することはありませんが、
ちょっと頭の隅に置いておくとよいでしょう。</p>
<p>　もう一つ、特にawkやsedを使って重たい処理をする場合に実践的な方法ですが、
処理を分割すると早くなるという例を下に示します。</p>
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#このような、日付と時刻を加工する処理</span>
<span class="c">#入力</span>
114.182.aaa.xxx - - <span class="o">[</span>05/Feb/2012:16:24:46 +0900<span class="o">]</span> <span class="s2">&quot;GET （略）</span>
<span class="s2">#出力</span>
<span class="s2">114.182.aaa.xxx - - [ 05 Feb 2012 162446 +0900] &quot;</span>GET （略）

<span class="c">#一個のsedで処理</span>
<span class="c">#sedで置換ルールを二つ以上指定するときは-eというオプションを使う</span>
<span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s@\\(..\\)/\\(...\\)/\\(....\\)@ \\1 \\2 \\3@&#39;</span> -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &lt; log1G &gt; /dev/null

real 0m29.488s
user 0m28.994s
sys 0m0.492s
<span class="c">#日付の処理と時刻の処理を分割</span>
<span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s@\\(..\\)/\\(...\\)/\\(....\\)@ \\1 \\2 \\3@&#39;</span> &lt; log1G | sed -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &gt; /dev/null

real 0m22.807s
user 0m32.382s
sys 0m2.064s
</pre></div>
</td></tr></table></div>
<p>ハードディスクの読み出しよりも処理がボトルネックになる場合は、
このように処理を分割した方が処理が早く終わる場合が多いです。
また、シェルスクリプトの場合は分けて書いた方が読みやすくなります。</p>
<p>　これの処理については、先ほどパイプをたくさんつなげる実験をした8CPUのサーバでもやってみました。
たくさんコマンドをつなげることに抵抗がなければ、CPUが多い環境だとこれだけ速くなるという例です。
ちょっといい加減なコードですが・・・。</p>
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>sed -e <span class="s1">&#39;s@\\(..\\)/\\(...\\)/\\(....\\)@ \\1 \\2 \\3@&#39;</span> -e <span class="s1">&#39;s/:\\(..\\):\\(..\\):\\(..\\)/ \\1\\2\\3/&#39;</span> &lt; log1G &gt; /dev/null

real 0m17.551s
user 0m17.209s
sys 0m0.303s

<span class="nv">$ </span><span class="nb">time </span>sed <span class="s1">&#39;s/\\[/&amp; /&#39;</span> &lt; log1G | sed <span class="s1">&#39;s@/@ @&#39;</span> | sed <span class="s1">&#39;s@/@ @&#39;</span> | sed <span class="s1">&#39;s/:/ /&#39;</span> | sed <span class="s1">&#39;s/://&#39;</span> | sed <span class="s1">&#39;s/://&#39;</span> &gt; /dev/null

real 0m5.773s
user 0m17.252s
sys 0m10.959s
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id11">
<h3>8.2.6. データをブロックするコマンドがある場合<a class="headerlink" href="#id11" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　sortのように全部データを読み込まないと出力をしないコマンドも、
ボトルネックになります。
次の場合、sortが終わるまで、awk以後の処理は開始しません。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz | sort | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq 
c-</pre></div>
</td></tr></table></div>
<p>これも無理に回避する必要はありませんが、
早く処理を終わらせるテクニックはあります。</p>
<p>　上の例の場合は、単純にgrepとawkの順序を変えるだけでかなり処理時間が違ってきます。</p>
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time </span>zcat *.gz | sort | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq -c | head -n 3
 10 1.112.aaa.xxx
 37 1.112.bbb.yyy
 10 1.112.ccc.zzz

real 0m5.561s
user 0m4.544s
sys 0m0.384s
<span class="nv">$ </span><span class="nb">time </span>zcat *.gz | awk <span class="s1">&#39;{print $1}&#39;</span> | sort | uniq -c | head -n 3
 10 1.112.aaa.xxx
 37 1.112.bbb.yyy
 10 1.112.ccc.zzz

real 0m1.991s
user 0m2.452s
sys 0m0.144s
</pre></div>
</td></tr></table></div>
<p>この例では単にsortに入れるデータ量を減らすということが効率の改善になっていますが、
例えば後者の並び次の二つのグループが同時に実行されることが分かっていることも大事です。</p>
<ul class="simple">
<li>zcat、awk、sortのデータ読み込み</li>
<li>sortの出力、uniq、head</li>
</ul>
<p>実際、後者のreal値とuser値が逆転しているように、
並列化の効果はsortが間にあってもちゃんと出ています。</p>
</div>
</div>
<div class="section" id="id12">
<h2>8.3. 終わりに<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、パイプにコマンドをつないで並列化するというお題を扱いました。
今回はシェルスクリプトは出てきませんでしたが、
たくさんデータを処理するシェルスクリプトを書く際には必須の知識です。
実際のところ、CPUが2個程度だとあまり効果を体感することは少ないと思いますが、
コマンドを何個もつないでもパフォーマンスには影響が出ないどころか、
かえって改善するということはお見せできたと思います。
CPUが多いと、実験で出てきたサーバ機のように効果は明確になります。</p>
<p>　また、マキルロイについて触れましたが、
パイプはUNIXの特性に大きな影響を与えています。
私がパイプ教団の信者であろうがパイプエバンジェリストであろうがそんなこととは関係なく、
パイプの発明が我々に大きな恩恵を与えていることは疑いのないことでしょう。
パイプは通信の方式とも言えますが、
これがインターネットに間接的に与えた影響についても考えてみると良いかもしれません。</p>
<p>　ここまでパイプを持ち上げておいてなんですが、
次回はパイプを使わないで並列化する方法について扱ってみたいと思います。</p>
</div>
</div>

