# 開眼シェルスクリプト2013年2月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>14. 開眼シェルスクリプト 第14回メールを操る(3)<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　前回に引き続き、サーバのMaildirに溜まったメールをいじります。<br />
今回は、メーラー（ただしリードオンリー）を作ってみます。<br />
このなかで、シェルの機能を使い、<br />
届いたメールのフィルタリングやCLIでの<br />
最低限必要なインタラクティブな操作を実現します。</p><br />
<p>　この企てを考えついたのは、<br />
仕事中にいちいちブラウザやGUIメーラーを開くのが面倒だと思ったからです。<br />
CUIのメーラーは便利なものがいろいろあるのに<br />
リードオンリーのものを作ってどうするんだという話ですが、<br />
筆者としては、既存のものではこれがちょっと気になります。</p><br />
<ul class="simple"><br />
<li>束縛するインターフェースは作るな。&#8211;ガンカーズのUNIX哲学から</li><br />
</ul><br />
<p>メーラーに入り、エディタのような画面が開いてプロンプトの「$」<br />
が消えてしまった瞬間、我々はgrepが使えないことを覚悟させられます。<br />
メールなんてせいぜいお客さんの名前で検索をかけて、<br />
あとは見ないで捨てますので（脚注：本当のような、嘘のような・・・）、<br />
これは困ります。<br />
プロンプトが消えるのはエディタもそうですが、エディタと違って<br />
たかがメールリーダーでプロを目指す気が筆者に微塵もありません。</p><br />
<p>　ということで、怠け癖が極限に達すると人はこんな<br />
シェルスクリプトを書くという例をお見せしたいと思います。<br />
そういやこんな言葉もあったなということで、以下の名言を。</p><br />
<p>「私は発明が必要の母だと考えません。私のなかでは発明は暇と直接関係していて、<br />
多分怠惰とも関連しています。面倒を省くという点で。」 &#8211; アガサ・クリスティー</p><br />
<div class="section" id="id2"><br />
<h2>14.1. 何をどこまで作るか<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="id3"><br />
<h3>14.1.1. 作るもの<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は <tt class="docutils literal"><span class="pre">Maildir</span></tt> の <tt class="docutils literal"><span class="pre">new</span></tt> に届いたメールを取り込んで、</p><br />
<ul class="simple"><br />
<li>フィルタのルールに応じて振り分けて受信トレイに置き、</li><br />
<li>vim でメールを読み込み専用で開いて表示し、</li><br />
<li>見たメールを未読トレイから既読トレイに移す</li><br />
</ul><br />
<p>ツールを作ります。Maildir については、<br />
前号、前々号で説明していますが、<br />
要はメールアカウントの <tt class="docutils literal"><span class="pre">~/maildir/new/</span></tt> というディレクトリに<br />
1メール1ファイルでメールが届く方式のことです。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>14.1.2. 環境<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は、メールの届くサーバにメーラーを作り込みます。<br />
サーバはVPS上で動いています。リスト1に環境を示します。</p><br />
<p>リスト1: 環境</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@mail ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release<br />
CentOS release 6.3 <span class="o">(</span>Final<span class="o">)</span><br />
<span class="o">[</span>ueda\@mail ~<span class="o">]</span><span class="nv">$ </span>uname -a<br />
Linux mail.usptomonokai.jp 2.6.32-279.5.2.el6.x86_64 <span class="c">#1 SMP</span><br />
 Fri Aug 24 01:07:11 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux<br />
<span class="o">[</span>ueda\@mail ~<span class="o">]</span><span class="nv">$ </span>bash --version<br />
GNU bash, version 4.1.2<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-redhat-linux-gnu<span class="o">)</span><br />
<span class="o">(</span>割愛<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id5"><br />
<h3>14.1.3. 制限等<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>このサーバでは SMTP サーバが動いており、<br />
Maildir 方式で各アカウントにメールを配信しています。<br />
今回は、既読のメールを <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> から <tt class="docutils literal"><span class="pre">~/Maildir/cur/</span></tt><br />
に移すという操作をしますので、他のメーラーとの併用は考えません。</p><br />
<p>　今回はこのマシンに直接メーラーを作っていきますが、<br />
自分のノートPCなどリモートから使うメーラーを作ることも可能です。<br />
このときは、スクリプトで使うコマンドを <tt class="docutils literal"><span class="pre">ssh</span></tt><br />
でリモートから動かせるようにします。<br />
今回はそれをやると解説するにはコードが長くなるのでやめておきます。</p><br />
<p>　また、最近では単なるHTML形式を越えたグラフィカルなメールがありますが、<br />
そういうのを見るのは諦めます。<br />
大抵の場合、その手のメールは筆者にとって重要ではありません。</p><br />
<p>　最後にお断りですが、今回はやることが多いので、<br />
Tukubaiのコマンドについて説明していません。<br />
<tt class="docutils literal"><span class="pre">plus,</span> <span class="pre">self,</span> <span class="pre">loopj,</span> <span class="pre">gyo,</span> <span class="pre">delf</span></tt> がTukubaiのコマンドです。<br />
<a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a> で機能をお調べ下さい。</p><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>14.2. メールの取り込み処理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　最初に、バックエンドで受信したメールをメーラー<br />
に取り込んで整理する部分を作ります。<br />
まず、リスト2のようにディレクトリを準備します。</p><br />
<p>リスト2: ディレクトリ構成</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@mail ~<span class="o">]</span><span class="nv">$ </span>tree -L 1 ~/MAILER/<br />
/home/ueda/MAILER/<br />
├── DATA<br />
├── FILTERS<br />
└── TRAY<br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">DATA</span></tt>: 前処理をしたメールを整理して置く場所</li><br />
<li><tt class="docutils literal"><span class="pre">FILTERS</span></tt>: メールを振り分ける条件を書いたスクリプトの置き場所</li><br />
<li><tt class="docutils literal"><span class="pre">TRAY</span></tt>: 受信トレイ</li><br />
</ul><br />
<p>　これらのディレクトリに対し、<br />
「 <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> に届いたメールを <tt class="docutils literal"><span class="pre">DATA</span></tt> に取り込んで、<br />
<tt class="docutils literal"><span class="pre">FILTERS</span></tt> 内のフィルタにマッチしたものを <tt class="docutils literal"><span class="pre">TRAY</span></tt> に置く。」<br />
という働きをするスクリプト <tt class="docutils literal"><span class="pre">FETCHER</span></tt> を作りましょう。</p><br />
<p>　まず、シェルスクリプトのヘッダ部と、<br />
メールを取り込んで <tt class="docutils literal"><span class="pre">DATA</span></tt> にメールを置くところまでをリスト3のように記述します。<br />
<tt class="docutils literal"><span class="pre">$1</span></tt> に <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> 下のファイル名を指定します。<br />
8～12行目がエラーチェック関数、<br />
13行目がメールがあるかどうかのチェック、<br />
それ以降がメールを扱いやすいように変換する部分です。</p><br />
<p>　変換部分では、</p><br />
<ul class="simple"><br />
<li>ヘッダ部分を加工したもの（ <tt class="docutils literal"><span class="pre">$tmp-header</span></tt> ）</li><br />
<li>検索・表示のためにUTF-8変換したもの（ <tt class="docutils literal"><span class="pre">$tmp-utf</span></tt> ）</li><br />
</ul><br />
<p>を作っています。</p><br />
<p>リスト3: FETCHER の前半部分</p><br />
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
27</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c"># FETCHER &lt;mailfile&gt;</span><br />
<span class="c"># written by R. Ueda (USP lab.) Nov. 20, 2012</span><br />
<span class="nv">dir</span><span class="o">=</span>~/MAILER<br />
<span class="nv">mdir</span><span class="o">=</span>~/Maildir<br />
<span class="nv">tmp</span><span class="o">=</span>~/tmp/<span class="nv">$$</span><br />
<br />
ERROR_CHECK<span class="o">(){</span><br />
 <span class="o">[</span> <span class="s2">&quot;$(plus ${PIPESTATUS[\@]})&quot;</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span><br />
<span class="k"> </span>rm -f <span class="nv">$tmp</span>-*<br />
 <span class="nb">exit </span>1<br />
<span class="o">}</span><br />
<span class="o">[</span> -f <span class="s2">&quot;$mdir/new/$1&quot;</span> <span class="o">]</span> ; ERROR_CHECK<br />
<br />
<span class="c"># データのUTF8変換、整形済みヘッダ作成#############</span><br />
nkf -wLux <span class="s2">&quot;$mdir/new/$1&quot;</span> |<br />
tee <span class="nv">$tmp</span>-work |<br />
<span class="c"># ヘッダを作る</span><br />
sed -n <span class="s1">&#39;1,/^$/p&#39;</span> |<br />
awk <span class="s1">&#39;{if(/^[^ \\t]/){print &quot;&quot;};printf(&quot;%s&quot;,$0)}&#39;</span> |<br />
<span class="c">#最初の空行の除去と最後に改行を付加</span><br />
tail -n +2 | awk <span class="s1">&#39;{print}&#39;</span> &gt; <span class="nv">$tmp</span>-header<br />
ERROR_CHECK<br />
<span class="c">#ヘッダと本文をくっつける。</span><br />
sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="nv">$tmp</span>-work |<br />
cat <span class="nv">$tmp</span>-header - &gt; <span class="nv">$tmp</span>-utf<br />
ERROR_CHECK<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ヘッダの加工では、19行目の <tt class="docutils literal"><span class="pre">sed</span></tt> で取り出し、<br />
20行目の <tt class="docutils literal"><span class="pre">awk</span></tt> で、ヘッダに入っている余計な改行を取る処理をしています。<br />
リスト4は、To: に複数のアドレスが指定されているヘッダの例ですが、<br />
こうやって改行をとっておけば To: をgrepするだけで全部のアドレスが取得できます。<br />
22行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、最終行に改行が抜けたテキストに改行を付ける常套手段です。</p><br />
<p>リスト4: ヘッダの改行を戻す</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#before</span><br />
To: ueda\@xxx.jp, r-ueda &lt;r-ueda\@yyy.com&gt;,<br />
 Ryuichi UEDA &lt;ryuichiueda\@zzz.com&gt;<br />
<br />
<span class="c">#after</span><br />
To: ueda\@xxx.jp, r-ueda &lt;r-ueda\@yyy.com&gt;, Ryuichi UEDA &lt;ryuichiueda\@zzz.com&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> はコマンドやパイプラインの終了ステータスを監視し、<br />
エラーがあったら処理を止める関数です。<br />
13行目の、「指定したファイルが <tt class="docutils literal"><span class="pre">Maildir</span></tt> にあるか」のチェックは、<br />
<tt class="docutils literal"><span class="pre">DATA</span></tt> ディレクトリ内を汚さないために必須です。</p><br />
<div class="section" id="id7"><br />
<h3>14.2.1. フィルタを準備<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　後半部分を示す前に、このメーラーで作る「フィルタ」をお見せします。<br />
まず、「all」という名前でリスト5の極小スクリプトを用意しました。<br />
allは必ずこのメーラーに準備しておきます。</p><br />
<p>リスト5: 全部受理する all フィルタ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@mail MAILER<span class="o">]</span><span class="nv">$ </span>cat ./FILTERS/all<br />
<span class="c">#!/bin/bash</span><br />
<span class="nb">true</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>他にも、リスト6のようなものを用意しました。<br />
これは、とあるFreeBSDのサーバから届くシステム管理用メールに反応するフィルタです。</p><br />
<p>リスト6: rootからのメールかどうか調べるフィルタ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@mail MAILER<span class="o">]</span><span class="nv">$ </span>cat ./FILTERS/bsd.usptomo.com<br />
<span class="c">#!/bin/bash</span><br />
grep -i <span class="s1">&#39;^from:&#39;</span> &lt; /dev/stdin |<br />
grep -q -F <span class="s1">&#39;root\@bsd.usptomo.com&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このように、標準入力からメールを読み込んで、<br />
条件にマッチしたら終了ステータス <tt class="docutils literal"><span class="pre">0</span></tt><br />
を返すスクリプトを準備しておきます。<br />
もちろん、他の言語を使ってもいいですし、<br />
もっと長いフィルタを作っても構いません。</p><br />
<p>　この方法をとっておくと、例えば優秀なスパムフィルタがあったときに、<br />
それをラッパーするシェルスクリプトを書けばそれを利用できるので、<br />
メーラーの方法に束縛されることがなくなります。<br />
執筆にあたってスパムフィルタについては何も調査してませんが、<br />
何も心配してません。まさにUNIX哲学。</p><br />
</div><br />
<div class="section" id="id8"><br />
<h3>14.2.2. フィルタリング<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、 <tt class="docutils literal"><span class="pre">FETCHER</span></tt> の後半部分をリスト7に示します。<br />
12行目まででメールのヘッダをフィルタごとの新着トレイに置いて、<br />
万事うまくいったら残りのファイル処理を確定しています。</p><br />
<p>　トレイにはヘッダのファイルを置いて<br />
「そのトレイにメールがある」という目印代わりにします。<br />
新着のメールは、例えばフィルタ <tt class="docutils literal"><span class="pre">all</span></tt> に適合したものは<br />
<tt class="docutils literal"><span class="pre">./TRAY/all/new/</span></tt> 下に置きます。<br />
既読のメールは <tt class="docutils literal"><span class="pre">./TRAY/all/20121125/</span></tt><br />
というように日付のディレクトリを作って整理します。</p><br />
<p>リスト7: FETCHER の後半部分</p><br />
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
20</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># フィルタ #################################</span><br />
<span class="nb">cd</span> <span class="s2">&quot;$dir/FILTERS&quot;</span> <span class="o">&amp;&amp;</span> <span class="o">[</span> -e <span class="s2">&quot;all&quot;</span> <span class="o">]</span> ; ERROR_CHECK<br />
<span class="c"># ファイル名のUNIX時間から年月日、時分秒を計算</span><br />
<span class="nv">D</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d -d <span class="s2">&quot;\@&quot;</span><span class="k">${</span><span class="nv">1</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">10</span><span class="k">})</span> ; ERROR_CHECK<br />
<span class="nv">T</span><span class="o">=</span><span class="k">$(</span>date +%H%M%S -d <span class="s2">&quot;\@&quot;</span><span class="k">${</span><span class="nv">1</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">10</span><span class="k">})</span> ; ERROR_CHECK<br />
<br />
<span class="k">for </span>f in * ; <span class="k">do</span><br />
 ./<span class="nv">$f</span> &lt; <span class="nv">$tmp</span>-utf <span class="o">||</span> <span class="k">continue</span><br />
<span class="k"> </span>mkdir -p <span class="nv">$dir</span>/TRAY/<span class="nv">$f</span>/new<br />
 cat <span class="nv">$tmp</span>-header &gt; <span class="nv">$dir</span>/TRAY/<span class="nv">$f</span>/new/<span class="nv">$D</span>.<span class="nv">$T</span>.<span class="nv">$1</span><br />
 ERROR_CHECK<br />
<span class="k">done</span><br />
<span class="c"># ファイルを移して終わり ##############</span><br />
mkdir -p <span class="s2">&quot;$dir/DATA/$D&quot;</span> <span class="o">&amp;&amp;</span><br />
cat <span class="nv">$tmp</span>-utf &gt; <span class="s2">&quot;$dir/DATA/$D/$D.$T.$1&quot;</span> <span class="o">&amp;&amp;</span><br />
mv <span class="s2">&quot;$mdir/new/$1&quot;</span> <span class="s2">&quot;$mdir/cur/$1&quot;</span><br />
ERROR_CHECK<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　取り込んだメールやヘッダのファイル名には、整理のため、<br />
もとのメールファイル名の頭に年月日と時分秒をつけておきます。<br />
その処理のために、4,5行目でファイル名のUNIX時間から年月日、<br />
時分秒を求めています。前々号で説明したように、<br />
メールのファイル名の先頭には10桁で1970年1月1日からの秒数がついており、</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>date -d \@1234567890<br />
2009年 2月 14日 土曜日 08:31:30 JST<br />
</pre></div><br />
</td></tr></table></div><br />
<p>のように、 <tt class="docutils literal"><span class="pre">date</span></tt> コマンドで変換できます。<br />
<tt class="docutils literal"><span class="pre">${1:0:10}</span></tt> は、 <tt class="docutils literal"><span class="pre">$1</span></tt> の先頭から10文字という意味です。<br />
次のように、任意の変数に対して使えます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ A</span><span class="o">=</span>12345<br />
<span class="c">#2文字目（0から数えて1文字目、から3文字）</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">A</span><span class="p">:</span><span class="nv">1</span><span class="p">:</span><span class="nv">3</span><span class="k">}</span><br />
234<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　7～12行目のfor文で、フィルタに一つずつ、<br />
UTF8変換したメールを入力していきます。<br />
<tt class="docutils literal"><span class="pre">continue</span></tt> は、for文のそれ以降の文をスキップするコマンドです。<br />
フィルタにマッチしたときだけ、13行以降の処理が行われ、<br />
フィルタの新着トレイにヘッダのファイルが置かれます。</p><br />
<p>　14～16行目はかなり変な書き方をしていますが、<br />
これは <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> をいちいち書くのを避ける小技です。<br />
コマンドを全部 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> でつないで、<br />
どれか一つが失敗したらそこで終わって <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt><br />
に処理が飛び、 <tt class="docutils literal"><span class="pre">exit</span> <span class="pre">1</span></tt> します。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">FETCHER</span></tt> ができたので、リスト8のように<br />
<tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> 下のメールを指定して実行してみます。</p><br />
<p>リスト8: FETCHER の実行</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@mail MAILER<span class="o">]</span><span class="nv">$ </span>./FETCHER 1352657044.Vfc03I468a21M42631.hoge1<br />
<span class="o">[</span>ueda\@mail MAILER<span class="o">]</span><span class="nv">$ </span>ls ./TRAY/*/new/*.1352657044.Vfc03I468a21M42631.hoge1<br />
./TRAY/all/new/20121112.030404.1352657044.Vfc03I468a21M42631.hoge1<br />
./TRAY/bsd.usptomo.com/new/20121112.030404.1352657044.Vfc03I468a21M42631.hoge1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このように、各フィルタの新着トレイにメールがあることが確認できます。</p><br />
</div><br />
</div><br />
<div class="section" id="id9"><br />
<h2>14.3. リーダーを作る<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、リーダー（スクリプト名： <tt class="docutils literal"><span class="pre">READER</span></tt> ）を作っていきましょう。<br />
まずは冒頭部分をリスト9に示します。<br />
<tt class="docutils literal"><span class="pre">READER</span></tt> にはオプションでトレイのパス、<br />
メールをリスト表示するときに何件表示するかを指定します。</p><br />
<p>　14～19行目は、さっき作った <tt class="docutils literal"><span class="pre">FETCHER</span></tt><br />
を使ってトレイを更新する処理です。<br />
最初の4行でディレクトリ名を除去したファイルのリストを作り、<br />
<tt class="docutils literal"><span class="pre">xargs</span></tt> で <tt class="docutils literal"><span class="pre">FETCHER</span></tt> に一つずつ処理させています。</p><br />
<p>リスト9: READER のヘッダ部分</p><br />
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c">#</span><br />
<span class="c"># READER &lt;dir&gt; &lt;num&gt;</span><br />
<span class="c"># written by R. Ueda (USP lab.) Nov. 20, 2012</span><br />
<span class="nv">tmp</span><span class="o">=</span>~/tmp/<span class="nv">$$</span><br />
<span class="nv">dir</span><span class="o">=</span>~/MAILER<br />
<br />
ERROR_CHECK<span class="o">(){</span><br />
 <span class="o">[</span> <span class="s2">&quot;$(plus ${PIPESTATUS[\@]})&quot;</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span><br />
<span class="k"> </span>rm -f <span class="nv">$tmp</span>-*<br />
 <span class="nb">exit </span>1<br />
<span class="o">}</span><br />
<span class="c">#先にメールを取得 ###############</span><br />
<span class="nb">echo</span> ~/Maildir/new/* |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
awk <span class="s1">&#39;!/\\*$/&#39;</span> |<br />
sed <span class="s1">&#39;s;^..*/;;&#39;</span> |<br />
xargs -r -n 1 -P 1 <span class="nv">$dir</span>/FETCHER<br />
ERROR_CHECK<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ここでは、新着メールがなくてもエラーが発生しないように、<br />
細工がしてあります。<br />
まず、新着メールがないと <tt class="docutils literal"><span class="pre">*</span></tt> がそのままパイプに通っていきますが、<br />
これを16行目の <tt class="docutils literal"><span class="pre">awk</span></tt> で除去しています。<br />
<tt class="docutils literal"><span class="pre">grep</span></tt> を使うと検索結果の有無で終了ステータスが変わり、<br />
<tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> に引っかかるので、代わりに<br />
<tt class="docutils literal"><span class="pre">awk</span></tt> を使っています。また、 <tt class="docutils literal"><span class="pre">xargs</span></tt> は通常、<br />
入力が空でもコマンドを一回実行してしまいますが、<br />
これを <tt class="docutils literal"><span class="pre">-r</span></tt> オプションで抑制しています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">Maildir/new/</span></tt> に何百もメールがあると、<br />
この部分は当然時間がかかります。しかし、<br />
こういう場合は別の端末から <tt class="docutils literal"><span class="pre">FETCHER</span></tt> を起動しておけばよいので、<br />
気を効かせることはやめましょう。<br />
これは、CUI信奉者が自分で使うものですので・・・。</p><br />
<p>　次にリスト10のように、<br />
メールのリストを表示してメールを選択してもらう部分を記述します。</p><br />
<p>リスト10: READER のインタラクション部分</p><br />
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
30<br />
31<br />
32<br />
33<br />
34<br />
35<br />
36<br />
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#メールのリストを作る #######################</span><br />
<span class="nb">cd</span> <span class="s2">&quot;${1:-$dir/TRAY/all/new}&quot;</span> ; ERROR_CHECK<br />
<br />
<span class="c">#表示対象ファイルの抽出</span><br />
<span class="nb">echo</span> * |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
grep -v <span class="s1">&#39;\\*&#39;</span> |<br />
sort |<br />
tail -n <span class="s2">&quot;${2:-10}&quot;</span> &gt; <span class="nv">$tmp</span>-files<br />
<span class="o">[</span> <span class="k">$(</span>gyo <span class="nv">$tmp</span>-files<span class="k">)</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> rm -f <span class="nv">$tmp</span>-* <span class="o">&amp;&amp;</span> <span class="nb">exit </span>0<br />
<br />
<span class="c">#subjectのリストを作成</span><br />
cat <span class="nv">$tmp</span>-files |<br />
xargs grep -H -i <span class="s1">&#39;^subject:&#39;</span> |<br />
sed <span class="s1">&#39;s/:[Ss]ubject:/ /&#39;</span> &gt; <span class="nv">$tmp</span>-subject<br />
<span class="c">#1:ファイル 2:subject</span><br />
ERROR_CHECK<br />
<br />
<span class="c">#日付のリストを取得し、subjectのリストと連結</span><br />
cat <span class="nv">$tmp</span>-files |<br />
xargs grep -H -i <span class="s1">&#39;^date:&#39;</span> |<br />
sed <span class="s1">&#39;s/:[Dd]ate:/ /&#39;</span> |<br />
<span class="c">#1:ファイル 2～:date</span><br />
self 1 2 3 4 6 |<br />
sed <span class="s1">&#39;s/:[0-9][0-9]$//&#39;</span> |<br />
loopj <span class="nv">num</span><span class="o">=</span>1 - <span class="nv">$tmp</span>-subject |<br />
<span class="c">#1:ファイル名 2~日時、subject</span><br />
tac |<br />
awk <span class="s1">&#39;{print NR,$0}&#39;</span> |<br />
<span class="c">#1:リスト番号 2:ファイル名 3～:日時, subject</span><br />
tee <span class="nv">$tmp</span>-list |<br />
<span class="c">#リストの表示</span><br />
delf 2<br />
<br />
<span class="nb">cd</span> - &gt; /dev/null<br />
<span class="nb">echo</span> -n <span class="s2">&quot;どのメールを見ますか？（番号）: &quot;</span><br />
<span class="nb">read </span>n<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ここまでの部分を実行すると、リスト11のような出力が出ます。</p><br />
<p>リスト11: READER のインタラクション出力</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@www5276ue MAILER<span class="o">]</span><span class="nv">$ </span>./VIEWER<br />
1 Sun, 25 Nov 07:10 処理エラー<br />
2 Sun, 25 Nov 06:00 【先着3名】怪しいアレが5000円！【怪しい.com】<br />
3 Sun, 25 Nov 04:00 Logwatch <span class="k">for </span>mail.usptomonokai.jp <span class="o">(</span>Linux<span class="o">)</span><br />
4 Sun, 25 Nov 03:04 bsd.usptomo.com security run output<br />
...<br />
10 Sun, 25 Nov 01:00 【再送】本当に致命的なエラー<br />
どのメールを見ますか？（番号）:<br />
</pre></div><br />
</td></tr></table></div><br />
<p>番号と着信日時、メールのSubjectが表示され、<br />
どの番号のメールを見るか入力をうながします。</p><br />
<p>　では、リスト10のスクリプトを見ていきましょう。<br />
まず2行目で、 <tt class="docutils literal"><span class="pre">$1</span></tt> で指定されたトレイに移動しています。<br />
<tt class="docutils literal"><span class="pre">cd</span> <span class="pre">&quot;${1:-$dir/TRAY/all/new}&quot;</span></tt> とありますが、<br />
これは、「 <tt class="docutils literal"><span class="pre">$1</span></tt> が空ならば <tt class="docutils literal"><span class="pre">$dir/TRAY/all/new</span></tt> 」<br />
という意味になります。<br />
9行目の <tt class="docutils literal"><span class="pre">tail</span></tt> のオプション指定でもこの方法を使っています。</p><br />
<p>　4～10行目は、トレイのファイルのリストを作って、<br />
リストが空ならそのまま処理を終えるという処理が書いてあります。<br />
その後のコードは、各メールの受信時刻とSubjectを抽出し、<br />
画面に出力するための細かい文字列処理です。</p><br />
<ul class="simple"><br />
<li>12～17行目: ファイル名と Subject の対応表</li><br />
<li>19～25行目: ファイル名と時刻の対応表</li><br />
</ul><br />
<p>を作っています。26行目の <tt class="docutils literal"><span class="pre">loopj</span></tt> で、これらの対応表をくっつけます。<br />
あとは、新着順に並び替え、番号をつけて <tt class="docutils literal"><span class="pre">$tmp-list</span></tt><br />
に表示します。33行目で画面に出力しますが、<br />
このときはファイル名を <tt class="docutils literal"><span class="pre">delf</span></tt> で削ります。</p><br />
<p>　35行目の <tt class="docutils literal"><span class="pre">cd</span> <span class="pre">-</span></tt> は、前回の <tt class="docutils literal"><span class="pre">cd</span></tt><br />
をする前のディレクトリに戻るためのコマンドで、<br />
手で端末を操作するときにもよく使うものです。</p><br />
<p>　36,37行目では、番号を入力するようにユーザに促し、<br />
<tt class="docutils literal"><span class="pre">read</span> <span class="pre">n</span></tt> で番号を受け付けています。<br />
端末からユーザが打った数字（正確には任意の文字列）が<br />
変数 <tt class="docutils literal"><span class="pre">n</span></tt> に代入されます。</p><br />
<p>　最後、リスト12に残りの部分を。まず、<br />
2行目で入力してもらった番号からファイル名を抽出しています。<br />
ここで <tt class="docutils literal"><span class="pre">n</span></tt> に変な文字列が入っていると、<br />
4行目でファイルがないので弾かれます。<br />
あとはメールから必要なヘッダとメールの文を取り出して、<br />
<tt class="docutils literal"><span class="pre">view</span></tt> で開いています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">view</span></tt> は単にvimをリードオンリーで開くためだけのコマンドです。<br />
vimでファイルを読むので、私の場合は普段のvimの使い方でメールが読めます。<br />
また、見ているファイルを別のディレクトリにそのまま保存できるなど、<br />
筆者と全国1000万人のvimユーザには異常に便利なメールリーダになります。</p><br />
<p>リスト12: READER の後半部分</p><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#メールを表示 ###################################</span><br />
<span class="nv">f</span><span class="o">=</span><span class="k">$(</span>awk -v <span class="nv">n</span><span class="o">=</span><span class="s2">&quot;$n&quot;</span> <span class="s1">&#39;$1==n{print $2}&#39;</span> <span class="nv">$tmp</span>-list<span class="k">)</span><br />
<span class="nv">m</span><span class="o">=</span><span class="s2">&quot;$dir/DATA/${f:0:8}/$f&quot;</span><br />
<span class="o">[</span> -f <span class="s2">&quot;$m&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span><br />
grep -E -i <span class="s1">&#39;^(from|to|cc|date|subject):&#39;</span> <span class="nv">$m</span> &gt; <span class="nv">$tmp</span>-work <span class="o">&amp;&amp;</span><br />
sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="nv">$m</span> &gt;&gt; <span class="nv">$tmp</span>-work <span class="o">&amp;&amp;</span><br />
view <span class="nv">$tmp</span>-work<br />
ERROR_CHECK<br />
<span class="c">#既読トレイに移す（newの中だけ） #################</span><br />
<span class="k">for </span>t in <span class="nv">$dir</span>/TRAY/* ; <span class="k">do</span><br />
 <span class="o">[</span> -e <span class="s2">&quot;$t/new/$f&quot;</span> <span class="o">]</span> <span class="o">||</span> <span class="k">continue</span><br />
<span class="k"> </span>mkdir -p <span class="nv">$t</span>/<span class="k">${</span><span class="nv">f</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">8</span><span class="k">}</span><br />
 mv -f <span class="nv">$t</span>/new/<span class="nv">$f</span> <span class="nv">$t</span>/<span class="k">${</span><span class="nv">f</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">8</span><span class="k">}</span>/<span class="nv">$f</span><br />
 ERROR_CHECK<br />
<span class="k">done</span><br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　viewを正常に閉じると10行目以降で各フィルタの新着トレイから、<br />
読んだメールを日付別の既読トレイに移動します。<br />
既読のトレイを開いた場合は、特に何も起こりません。<br />
この処理は、各フィルタのトレイ全部に対して行います。</p><br />
</div><br />
<div class="section" id="id10"><br />
<h2>14.4. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、シェルスクリプトでメールリーダーを作ってみました。<br />
今後真面目に作り込むと便利になるかもしれません。</p><br />
<p>　返信機能を付けるとすると、おそらく <tt class="docutils literal"><span class="pre">view</span></tt> で保存したメールを処理し、<br />
返信用のメールの雛形を作るスクリプトを作ることになります。<br />
メールは <tt class="docutils literal"><span class="pre">mail</span></tt> コマンドか何かで送ればよいですし、<br />
メールアドレスの入力が面倒なら <tt class="docutils literal"><span class="pre">vim</span></tt> の補完ツールの利用や、<br />
メールアドレスを提示するコマンドを作ればなんとかなるでしょう。</p><br />
<p>　また、「何件メールがトレイにあるか」などは、それこそ<br />
lsとwcを使えば事足ります。captiveでないので、なんとかなります。</p><br />
<p>　今回は正直言いまして、<br />
かなりエクストリームなプログラミングになってしまいましたので、<br />
次回からはもうちょっとマイルドな話題を扱いたいと思います。</p><br />
</div><br />
</div><br />
<br />

