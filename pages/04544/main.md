---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年2月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>14. 開眼シェルスクリプト 第14回メールを操る(3)<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　前回に引き続き、サーバのMaildirに溜まったメールをいじります。
今回は、メーラー（ただしリードオンリー）を作ってみます。
このなかで、シェルの機能を使い、
届いたメールのフィルタリングやCLIでの
最低限必要なインタラクティブな操作を実現します。</p>
<p>　この企てを考えついたのは、
仕事中にいちいちブラウザやGUIメーラーを開くのが面倒だと思ったからです。
CUIのメーラーは便利なものがいろいろあるのに
リードオンリーのものを作ってどうするんだという話ですが、
筆者としては、既存のものではこれがちょっと気になります。</p>
<ul class="simple">
<li>束縛するインターフェースは作るな。&#8211;ガンカーズのUNIX哲学から</li>
</ul>
<p>メーラーに入り、エディタのような画面が開いてプロンプトの「$」
が消えてしまった瞬間、我々はgrepが使えないことを覚悟させられます。
メールなんてせいぜいお客さんの名前で検索をかけて、
あとは見ないで捨てますので（脚注：本当のような、嘘のような・・・）、
これは困ります。
プロンプトが消えるのはエディタもそうですが、エディタと違って
たかがメールリーダーでプロを目指す気が筆者に微塵もありません。</p>
<p>　ということで、怠け癖が極限に達すると人はこんな
シェルスクリプトを書くという例をお見せしたいと思います。
そういやこんな言葉もあったなということで、以下の名言を。</p>
<p>「私は発明が必要の母だと考えません。私のなかでは発明は暇と直接関係していて、
多分怠惰とも関連しています。面倒を省くという点で。」 &#8211; アガサ・クリスティー</p>
<div class="section" id="id2">
<h2>14.1. 何をどこまで作るか<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="id3">
<h3>14.1.1. 作るもの<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は <tt class="docutils literal"><span class="pre">Maildir</span></tt> の <tt class="docutils literal"><span class="pre">new</span></tt> に届いたメールを取り込んで、</p>
<ul class="simple">
<li>フィルタのルールに応じて振り分けて受信トレイに置き、</li>
<li>vim でメールを読み込み専用で開いて表示し、</li>
<li>見たメールを未読トレイから既読トレイに移す</li>
</ul>
<p>ツールを作ります。Maildir については、
前号、前々号で説明していますが、
要はメールアカウントの <tt class="docutils literal"><span class="pre">~/maildir/new/</span></tt> というディレクトリに
1メール1ファイルでメールが届く方式のことです。</p>
</div>
<div class="section" id="id4">
<h3>14.1.2. 環境<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は、メールの届くサーバにメーラーを作り込みます。
サーバはVPS上で動いています。リスト1に環境を示します。</p>
<p>リスト1: 環境</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@mail ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release
CentOS release 6.3 <span class="o">(</span>Final<span class="o">)</span>
<span class="o">[</span>ueda@mail ~<span class="o">]</span><span class="nv">$ </span>uname -a
Linux mail.usptomonokai.jp 2.6.32-279.5.2.el6.x86_64 <span class="c">#1 SMP</span>
 Fri Aug 24 01:07:11 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
<span class="o">[</span>ueda@mail ~<span class="o">]</span><span class="nv">$ </span>bash --version
GNU bash, version 4.1.2<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-redhat-linux-gnu<span class="o">)</span>
<span class="o">(</span>割愛<span class="o">)</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id5">
<h3>14.1.3. 制限等<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>このサーバでは SMTP サーバが動いており、
Maildir 方式で各アカウントにメールを配信しています。
今回は、既読のメールを <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> から <tt class="docutils literal"><span class="pre">~/Maildir/cur/</span></tt>
に移すという操作をしますので、他のメーラーとの併用は考えません。</p>
<p>　今回はこのマシンに直接メーラーを作っていきますが、
自分のノートPCなどリモートから使うメーラーを作ることも可能です。
このときは、スクリプトで使うコマンドを <tt class="docutils literal"><span class="pre">ssh</span></tt>
でリモートから動かせるようにします。
今回はそれをやると解説するにはコードが長くなるのでやめておきます。</p>
<p>　また、最近では単なるHTML形式を越えたグラフィカルなメールがありますが、
そういうのを見るのは諦めます。
大抵の場合、その手のメールは筆者にとって重要ではありません。</p>
<p>　最後にお断りですが、今回はやることが多いので、
Tukubaiのコマンドについて説明していません。
<tt class="docutils literal"><span class="pre">plus,</span> <span class="pre">self,</span> <span class="pre">loopj,</span> <span class="pre">gyo,</span> <span class="pre">delf</span></tt> がTukubaiのコマンドです。
<a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a> で機能をお調べ下さい。</p>
</div>
</div>
<div class="section" id="id6">
<h2>14.2. メールの取り込み処理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　最初に、バックエンドで受信したメールをメーラー
に取り込んで整理する部分を作ります。
まず、リスト2のようにディレクトリを準備します。</p>
<p>リスト2: ディレクトリ構成</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@mail ~<span class="o">]</span><span class="nv">$ </span>tree -L 1 ~/MAILER/
/home/ueda/MAILER/
├── DATA
├── FILTERS
└── TRAY
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">DATA</span></tt>: 前処理をしたメールを整理して置く場所</li>
<li><tt class="docutils literal"><span class="pre">FILTERS</span></tt>: メールを振り分ける条件を書いたスクリプトの置き場所</li>
<li><tt class="docutils literal"><span class="pre">TRAY</span></tt>: 受信トレイ</li>
</ul>
<p>　これらのディレクトリに対し、
「 <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> に届いたメールを <tt class="docutils literal"><span class="pre">DATA</span></tt> に取り込んで、
<tt class="docutils literal"><span class="pre">FILTERS</span></tt> 内のフィルタにマッチしたものを <tt class="docutils literal"><span class="pre">TRAY</span></tt> に置く。」
という働きをするスクリプト <tt class="docutils literal"><span class="pre">FETCHER</span></tt> を作りましょう。</p>
<p>　まず、シェルスクリプトのヘッダ部と、
メールを取り込んで <tt class="docutils literal"><span class="pre">DATA</span></tt> にメールを置くところまでをリスト3のように記述します。
<tt class="docutils literal"><span class="pre">$1</span></tt> に <tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> 下のファイル名を指定します。
8～12行目がエラーチェック関数、
13行目がメールがあるかどうかのチェック、
それ以降がメールを扱いやすいように変換する部分です。</p>
<p>　変換部分では、</p>
<ul class="simple">
<li>ヘッダ部分を加工したもの（ <tt class="docutils literal"><span class="pre">$tmp-header</span></tt> ）</li>
<li>検索・表示のためにUTF-8変換したもの（ <tt class="docutils literal"><span class="pre">$tmp-utf</span></tt> ）</li>
</ul>
<p>を作っています。</p>
<p>リスト3: FETCHER の前半部分</p>
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
27</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c"># FETCHER &lt;mailfile&gt;</span>
<span class="c"># written by R. Ueda (USP lab.) Nov. 20, 2012</span>
<span class="nv">dir</span><span class="o">=</span>~/MAILER
<span class="nv">mdir</span><span class="o">=</span>~/Maildir
<span class="nv">tmp</span><span class="o">=</span>~/tmp/<span class="nv">$$</span>

ERROR_CHECK<span class="o">(){</span>
 <span class="o">[</span> <span class="s2">&quot;$(plus ${PIPESTATUS[@]})&quot;</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span>
<span class="k"> </span>rm -f <span class="nv">$tmp</span>-*
 <span class="nb">exit </span>1
<span class="o">}</span>
<span class="o">[</span> -f <span class="s2">&quot;$mdir/new/$1&quot;</span> <span class="o">]</span> ; ERROR_CHECK

<span class="c"># データのUTF8変換、整形済みヘッダ作成#############</span>
nkf -wLux <span class="s2">&quot;$mdir/new/$1&quot;</span> |
tee <span class="nv">$tmp</span>-work |
<span class="c"># ヘッダを作る</span>
sed -n <span class="s1">&#39;1,/^$/p&#39;</span> |
awk <span class="s1">&#39;{if(/^[^ \\t]/){print &quot;&quot;};printf(&quot;%s&quot;,$0)}&#39;</span> |
<span class="c">#最初の空行の除去と最後に改行を付加</span>
tail -n +2 | awk <span class="s1">&#39;{print}&#39;</span> &gt; <span class="nv">$tmp</span>-header
ERROR_CHECK
<span class="c">#ヘッダと本文をくっつける。</span>
sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="nv">$tmp</span>-work |
cat <span class="nv">$tmp</span>-header - &gt; <span class="nv">$tmp</span>-utf
ERROR_CHECK
</pre></div>
</td></tr></table></div>
<p>　ヘッダの加工では、19行目の <tt class="docutils literal"><span class="pre">sed</span></tt> で取り出し、
20行目の <tt class="docutils literal"><span class="pre">awk</span></tt> で、ヘッダに入っている余計な改行を取る処理をしています。
リスト4は、To: に複数のアドレスが指定されているヘッダの例ですが、
こうやって改行をとっておけば To: をgrepするだけで全部のアドレスが取得できます。
22行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、最終行に改行が抜けたテキストに改行を付ける常套手段です。</p>
<p>リスト4: ヘッダの改行を戻す</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#before</span>
To: ueda@xxx.jp, r-ueda &lt;r-ueda@yyy.com&gt;,
 Ryuichi UEDA &lt;ryuichiueda@zzz.com&gt;

<span class="c">#after</span>
To: ueda@xxx.jp, r-ueda &lt;r-ueda@yyy.com&gt;, Ryuichi UEDA &lt;ryuichiueda@zzz.com&gt;
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> はコマンドやパイプラインの終了ステータスを監視し、
エラーがあったら処理を止める関数です。
13行目の、「指定したファイルが <tt class="docutils literal"><span class="pre">Maildir</span></tt> にあるか」のチェックは、
<tt class="docutils literal"><span class="pre">DATA</span></tt> ディレクトリ内を汚さないために必須です。</p>
<div class="section" id="id7">
<h3>14.2.1. フィルタを準備<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　後半部分を示す前に、このメーラーで作る「フィルタ」をお見せします。
まず、「all」という名前でリスト5の極小スクリプトを用意しました。
allは必ずこのメーラーに準備しておきます。</p>
<p>リスト5: 全部受理する all フィルタ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@mail MAILER<span class="o">]</span><span class="nv">$ </span>cat ./FILTERS/all
<span class="c">#!/bin/bash</span>
<span class="nb">true</span>
</pre></div>
</td></tr></table></div>
<p>他にも、リスト6のようなものを用意しました。
これは、とあるFreeBSDのサーバから届くシステム管理用メールに反応するフィルタです。</p>
<p>リスト6: rootからのメールかどうか調べるフィルタ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@mail MAILER<span class="o">]</span><span class="nv">$ </span>cat ./FILTERS/bsd.usptomo.com
<span class="c">#!/bin/bash</span>
grep -i <span class="s1">&#39;^from:&#39;</span> &lt; /dev/stdin |
grep -q -F <span class="s1">&#39;root@bsd.usptomo.com&#39;</span>
</pre></div>
</td></tr></table></div>
<p>　このように、標準入力からメールを読み込んで、
条件にマッチしたら終了ステータス <tt class="docutils literal"><span class="pre">0</span></tt>
を返すスクリプトを準備しておきます。
もちろん、他の言語を使ってもいいですし、
もっと長いフィルタを作っても構いません。</p>
<p>　この方法をとっておくと、例えば優秀なスパムフィルタがあったときに、
それをラッパーするシェルスクリプトを書けばそれを利用できるので、
メーラーの方法に束縛されることがなくなります。
執筆にあたってスパムフィルタについては何も調査してませんが、
何も心配してません。まさにUNIX哲学。</p>
</div>
<div class="section" id="id8">
<h3>14.2.2. フィルタリング<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、 <tt class="docutils literal"><span class="pre">FETCHER</span></tt> の後半部分をリスト7に示します。
12行目まででメールのヘッダをフィルタごとの新着トレイに置いて、
万事うまくいったら残りのファイル処理を確定しています。</p>
<p>　トレイにはヘッダのファイルを置いて
「そのトレイにメールがある」という目印代わりにします。
新着のメールは、例えばフィルタ <tt class="docutils literal"><span class="pre">all</span></tt> に適合したものは
<tt class="docutils literal"><span class="pre">./TRAY/all/new/</span></tt> 下に置きます。
既読のメールは <tt class="docutils literal"><span class="pre">./TRAY/all/20121125/</span></tt>
というように日付のディレクトリを作って整理します。</p>
<p>リスト7: FETCHER の後半部分</p>
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
20</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># フィルタ #################################</span>
<span class="nb">cd</span> <span class="s2">&quot;$dir/FILTERS&quot;</span> <span class="o">&amp;&amp;</span> <span class="o">[</span> -e <span class="s2">&quot;all&quot;</span> <span class="o">]</span> ; ERROR_CHECK
<span class="c"># ファイル名のUNIX時間から年月日、時分秒を計算</span>
<span class="nv">D</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d -d <span class="s2">&quot;@&quot;</span><span class="k">${</span><span class="nv">1</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">10</span><span class="k">})</span> ; ERROR_CHECK
<span class="nv">T</span><span class="o">=</span><span class="k">$(</span>date +%H%M%S -d <span class="s2">&quot;@&quot;</span><span class="k">${</span><span class="nv">1</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">10</span><span class="k">})</span> ; ERROR_CHECK

<span class="k">for </span>f in * ; <span class="k">do</span>
 ./<span class="nv">$f</span> &lt; <span class="nv">$tmp</span>-utf <span class="o">||</span> <span class="k">continue</span>
<span class="k"> </span>mkdir -p <span class="nv">$dir</span>/TRAY/<span class="nv">$f</span>/new
 cat <span class="nv">$tmp</span>-header &gt; <span class="nv">$dir</span>/TRAY/<span class="nv">$f</span>/new/<span class="nv">$D</span>.<span class="nv">$T</span>.<span class="nv">$1</span>
 ERROR_CHECK
<span class="k">done</span>
<span class="c"># ファイルを移して終わり ##############</span>
mkdir -p <span class="s2">&quot;$dir/DATA/$D&quot;</span> <span class="o">&amp;&amp;</span>
cat <span class="nv">$tmp</span>-utf &gt; <span class="s2">&quot;$dir/DATA/$D/$D.$T.$1&quot;</span> <span class="o">&amp;&amp;</span>
mv <span class="s2">&quot;$mdir/new/$1&quot;</span> <span class="s2">&quot;$mdir/cur/$1&quot;</span>
ERROR_CHECK

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　取り込んだメールやヘッダのファイル名には、整理のため、
もとのメールファイル名の頭に年月日と時分秒をつけておきます。
その処理のために、4,5行目でファイル名のUNIX時間から年月日、
時分秒を求めています。前々号で説明したように、
メールのファイル名の先頭には10桁で1970年1月1日からの秒数がついており、</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>date -d @1234567890
2009年 2月 14日 土曜日 08:31:30 JST
</pre></div>
</td></tr></table></div>
<p>のように、 <tt class="docutils literal"><span class="pre">date</span></tt> コマンドで変換できます。
<tt class="docutils literal"><span class="pre">${1:0:10}</span></tt> は、 <tt class="docutils literal"><span class="pre">$1</span></tt> の先頭から10文字という意味です。
次のように、任意の変数に対して使えます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ A</span><span class="o">=</span>12345
<span class="c">#2文字目（0から数えて1文字目、から3文字）</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">A</span><span class="p">:</span><span class="nv">1</span><span class="p">:</span><span class="nv">3</span><span class="k">}</span>
234
</pre></div>
</td></tr></table></div>
<p>　7～12行目のfor文で、フィルタに一つずつ、
UTF8変換したメールを入力していきます。
<tt class="docutils literal"><span class="pre">continue</span></tt> は、for文のそれ以降の文をスキップするコマンドです。
フィルタにマッチしたときだけ、13行以降の処理が行われ、
フィルタの新着トレイにヘッダのファイルが置かれます。</p>
<p>　14～16行目はかなり変な書き方をしていますが、
これは <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> をいちいち書くのを避ける小技です。
コマンドを全部 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> でつないで、
どれか一つが失敗したらそこで終わって <tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt>
に処理が飛び、 <tt class="docutils literal"><span class="pre">exit</span> <span class="pre">1</span></tt> します。</p>
<p>　 <tt class="docutils literal"><span class="pre">FETCHER</span></tt> ができたので、リスト8のように
<tt class="docutils literal"><span class="pre">~/Maildir/new/</span></tt> 下のメールを指定して実行してみます。</p>
<p>リスト8: FETCHER の実行</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@mail MAILER<span class="o">]</span><span class="nv">$ </span>./FETCHER 1352657044.Vfc03I468a21M42631.hoge1
<span class="o">[</span>ueda@mail MAILER<span class="o">]</span><span class="nv">$ </span>ls ./TRAY/*/new/*.1352657044.Vfc03I468a21M42631.hoge1
./TRAY/all/new/20121112.030404.1352657044.Vfc03I468a21M42631.hoge1
./TRAY/bsd.usptomo.com/new/20121112.030404.1352657044.Vfc03I468a21M42631.hoge1
</pre></div>
</td></tr></table></div>
<p>このように、各フィルタの新着トレイにメールがあることが確認できます。</p>
</div>
</div>
<div class="section" id="id9">
<h2>14.3. リーダーを作る<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、リーダー（スクリプト名： <tt class="docutils literal"><span class="pre">READER</span></tt> ）を作っていきましょう。
まずは冒頭部分をリスト9に示します。
<tt class="docutils literal"><span class="pre">READER</span></tt> にはオプションでトレイのパス、
メールをリスト表示するときに何件表示するかを指定します。</p>
<p>　14～19行目は、さっき作った <tt class="docutils literal"><span class="pre">FETCHER</span></tt>
を使ってトレイを更新する処理です。
最初の4行でディレクトリ名を除去したファイルのリストを作り、
<tt class="docutils literal"><span class="pre">xargs</span></tt> で <tt class="docutils literal"><span class="pre">FETCHER</span></tt> に一つずつ処理させています。</p>
<p>リスト9: READER のヘッダ部分</p>
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c">#</span>
<span class="c"># READER &lt;dir&gt; &lt;num&gt;</span>
<span class="c"># written by R. Ueda (USP lab.) Nov. 20, 2012</span>
<span class="nv">tmp</span><span class="o">=</span>~/tmp/<span class="nv">$$</span>
<span class="nv">dir</span><span class="o">=</span>~/MAILER

ERROR_CHECK<span class="o">(){</span>
 <span class="o">[</span> <span class="s2">&quot;$(plus ${PIPESTATUS[@]})&quot;</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span>
<span class="k"> </span>rm -f <span class="nv">$tmp</span>-*
 <span class="nb">exit </span>1
<span class="o">}</span>
<span class="c">#先にメールを取得 ###############</span>
<span class="nb">echo</span> ~/Maildir/new/* |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
awk <span class="s1">&#39;!/\\*$/&#39;</span> |
sed <span class="s1">&#39;s;^..*/;;&#39;</span> |
xargs -r -n 1 -P 1 <span class="nv">$dir</span>/FETCHER
ERROR_CHECK
</pre></div>
</td></tr></table></div>
<p>　ここでは、新着メールがなくてもエラーが発生しないように、
細工がしてあります。
まず、新着メールがないと <tt class="docutils literal"><span class="pre">*</span></tt> がそのままパイプに通っていきますが、
これを16行目の <tt class="docutils literal"><span class="pre">awk</span></tt> で除去しています。
<tt class="docutils literal"><span class="pre">grep</span></tt> を使うと検索結果の有無で終了ステータスが変わり、
<tt class="docutils literal"><span class="pre">ERROR_CHECK</span></tt> に引っかかるので、代わりに
<tt class="docutils literal"><span class="pre">awk</span></tt> を使っています。また、 <tt class="docutils literal"><span class="pre">xargs</span></tt> は通常、
入力が空でもコマンドを一回実行してしまいますが、
これを <tt class="docutils literal"><span class="pre">-r</span></tt> オプションで抑制しています。</p>
<p>　 <tt class="docutils literal"><span class="pre">Maildir/new/</span></tt> に何百もメールがあると、
この部分は当然時間がかかります。しかし、
こういう場合は別の端末から <tt class="docutils literal"><span class="pre">FETCHER</span></tt> を起動しておけばよいので、
気を効かせることはやめましょう。
これは、CUI信奉者が自分で使うものですので・・・。</p>
<p>　次にリスト10のように、
メールのリストを表示してメールを選択してもらう部分を記述します。</p>
<p>リスト10: READER のインタラクション部分</p>
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
30
31
32
33
34
35
36
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#メールのリストを作る #######################</span>
<span class="nb">cd</span> <span class="s2">&quot;${1:-$dir/TRAY/all/new}&quot;</span> ; ERROR_CHECK

<span class="c">#表示対象ファイルの抽出</span>
<span class="nb">echo</span> * |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
grep -v <span class="s1">&#39;\\*&#39;</span> |
sort |
tail -n <span class="s2">&quot;${2:-10}&quot;</span> &gt; <span class="nv">$tmp</span>-files
<span class="o">[</span> <span class="k">$(</span>gyo <span class="nv">$tmp</span>-files<span class="k">)</span> -eq 0 <span class="o">]</span> <span class="o">&amp;&amp;</span> rm -f <span class="nv">$tmp</span>-* <span class="o">&amp;&amp;</span> <span class="nb">exit </span>0

<span class="c">#subjectのリストを作成</span>
cat <span class="nv">$tmp</span>-files |
xargs grep -H -i <span class="s1">&#39;^subject:&#39;</span> |
sed <span class="s1">&#39;s/:[Ss]ubject:/ /&#39;</span> &gt; <span class="nv">$tmp</span>-subject
<span class="c">#1:ファイル 2:subject</span>
ERROR_CHECK

<span class="c">#日付のリストを取得し、subjectのリストと連結</span>
cat <span class="nv">$tmp</span>-files |
xargs grep -H -i <span class="s1">&#39;^date:&#39;</span> |
sed <span class="s1">&#39;s/:[Dd]ate:/ /&#39;</span> |
<span class="c">#1:ファイル 2～:date</span>
self 1 2 3 4 6 |
sed <span class="s1">&#39;s/:[0-9][0-9]$//&#39;</span> |
loopj <span class="nv">num</span><span class="o">=</span>1 - <span class="nv">$tmp</span>-subject |
<span class="c">#1:ファイル名 2~日時、subject</span>
tac |
awk <span class="s1">&#39;{print NR,$0}&#39;</span> |
<span class="c">#1:リスト番号 2:ファイル名 3～:日時, subject</span>
tee <span class="nv">$tmp</span>-list |
<span class="c">#リストの表示</span>
delf 2

<span class="nb">cd</span> - &gt; /dev/null
<span class="nb">echo</span> -n <span class="s2">&quot;どのメールを見ますか？（番号）: &quot;</span>
<span class="nb">read </span>n
</pre></div>
</td></tr></table></div>
<p>　ここまでの部分を実行すると、リスト11のような出力が出ます。</p>
<p>リスト11: READER のインタラクション出力</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@www5276ue MAILER<span class="o">]</span><span class="nv">$ </span>./VIEWER
1 Sun, 25 Nov 07:10 処理エラー
2 Sun, 25 Nov 06:00 【先着3名】怪しいアレが5000円！【怪しい.com】
3 Sun, 25 Nov 04:00 Logwatch <span class="k">for </span>mail.usptomonokai.jp <span class="o">(</span>Linux<span class="o">)</span>
4 Sun, 25 Nov 03:04 bsd.usptomo.com security run output
...
10 Sun, 25 Nov 01:00 【再送】本当に致命的なエラー
どのメールを見ますか？（番号）:
</pre></div>
</td></tr></table></div>
<p>番号と着信日時、メールのSubjectが表示され、
どの番号のメールを見るか入力をうながします。</p>
<p>　では、リスト10のスクリプトを見ていきましょう。
まず2行目で、 <tt class="docutils literal"><span class="pre">$1</span></tt> で指定されたトレイに移動しています。
<tt class="docutils literal"><span class="pre">cd</span> <span class="pre">&quot;${1:-$dir/TRAY/all/new}&quot;</span></tt> とありますが、
これは、「 <tt class="docutils literal"><span class="pre">$1</span></tt> が空ならば <tt class="docutils literal"><span class="pre">$dir/TRAY/all/new</span></tt> 」
という意味になります。
9行目の <tt class="docutils literal"><span class="pre">tail</span></tt> のオプション指定でもこの方法を使っています。</p>
<p>　4～10行目は、トレイのファイルのリストを作って、
リストが空ならそのまま処理を終えるという処理が書いてあります。
その後のコードは、各メールの受信時刻とSubjectを抽出し、
画面に出力するための細かい文字列処理です。</p>
<ul class="simple">
<li>12～17行目: ファイル名と Subject の対応表</li>
<li>19～25行目: ファイル名と時刻の対応表</li>
</ul>
<p>を作っています。26行目の <tt class="docutils literal"><span class="pre">loopj</span></tt> で、これらの対応表をくっつけます。
あとは、新着順に並び替え、番号をつけて <tt class="docutils literal"><span class="pre">$tmp-list</span></tt>
に表示します。33行目で画面に出力しますが、
このときはファイル名を <tt class="docutils literal"><span class="pre">delf</span></tt> で削ります。</p>
<p>　35行目の <tt class="docutils literal"><span class="pre">cd</span> <span class="pre">-</span></tt> は、前回の <tt class="docutils literal"><span class="pre">cd</span></tt>
をする前のディレクトリに戻るためのコマンドで、
手で端末を操作するときにもよく使うものです。</p>
<p>　36,37行目では、番号を入力するようにユーザに促し、
<tt class="docutils literal"><span class="pre">read</span> <span class="pre">n</span></tt> で番号を受け付けています。
端末からユーザが打った数字（正確には任意の文字列）が
変数 <tt class="docutils literal"><span class="pre">n</span></tt> に代入されます。</p>
<p>　最後、リスト12に残りの部分を。まず、
2行目で入力してもらった番号からファイル名を抽出しています。
ここで <tt class="docutils literal"><span class="pre">n</span></tt> に変な文字列が入っていると、
4行目でファイルがないので弾かれます。
あとはメールから必要なヘッダとメールの文を取り出して、
<tt class="docutils literal"><span class="pre">view</span></tt> で開いています。</p>
<p>　 <tt class="docutils literal"><span class="pre">view</span></tt> は単にvimをリードオンリーで開くためだけのコマンドです。
vimでファイルを読むので、私の場合は普段のvimの使い方でメールが読めます。
また、見ているファイルを別のディレクトリにそのまま保存できるなど、
筆者と全国1000万人のvimユーザには異常に便利なメールリーダになります。</p>
<p>リスト12: READER の後半部分</p>
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#メールを表示 ###################################</span>
<span class="nv">f</span><span class="o">=</span><span class="k">$(</span>awk -v <span class="nv">n</span><span class="o">=</span><span class="s2">&quot;$n&quot;</span> <span class="s1">&#39;$1==n{print $2}&#39;</span> <span class="nv">$tmp</span>-list<span class="k">)</span>
<span class="nv">m</span><span class="o">=</span><span class="s2">&quot;$dir/DATA/${f:0:8}/$f&quot;</span>
<span class="o">[</span> -f <span class="s2">&quot;$m&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span>
grep -E -i <span class="s1">&#39;^(from|to|cc|date|subject):&#39;</span> <span class="nv">$m</span> &gt; <span class="nv">$tmp</span>-work <span class="o">&amp;&amp;</span>
sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="nv">$m</span> &gt;&gt; <span class="nv">$tmp</span>-work <span class="o">&amp;&amp;</span>
view <span class="nv">$tmp</span>-work
ERROR_CHECK
<span class="c">#既読トレイに移す（newの中だけ） #################</span>
<span class="k">for </span>t in <span class="nv">$dir</span>/TRAY/* ; <span class="k">do</span>
 <span class="o">[</span> -e <span class="s2">&quot;$t/new/$f&quot;</span> <span class="o">]</span> <span class="o">||</span> <span class="k">continue</span>
<span class="k"> </span>mkdir -p <span class="nv">$t</span>/<span class="k">${</span><span class="nv">f</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">8</span><span class="k">}</span>
 mv -f <span class="nv">$t</span>/new/<span class="nv">$f</span> <span class="nv">$t</span>/<span class="k">${</span><span class="nv">f</span><span class="p">:</span><span class="nv">0</span><span class="p">:</span><span class="nv">8</span><span class="k">}</span>/<span class="nv">$f</span>
 ERROR_CHECK
<span class="k">done</span>

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　viewを正常に閉じると10行目以降で各フィルタの新着トレイから、
読んだメールを日付別の既読トレイに移動します。
既読のトレイを開いた場合は、特に何も起こりません。
この処理は、各フィルタのトレイ全部に対して行います。</p>
</div>
<div class="section" id="id10">
<h2>14.4. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、シェルスクリプトでメールリーダーを作ってみました。
今後真面目に作り込むと便利になるかもしれません。</p>
<p>　返信機能を付けるとすると、おそらく <tt class="docutils literal"><span class="pre">view</span></tt> で保存したメールを処理し、
返信用のメールの雛形を作るスクリプトを作ることになります。
メールは <tt class="docutils literal"><span class="pre">mail</span></tt> コマンドか何かで送ればよいですし、
メールアドレスの入力が面倒なら <tt class="docutils literal"><span class="pre">vim</span></tt> の補完ツールの利用や、
メールアドレスを提示するコマンドを作ればなんとかなるでしょう。</p>
<p>　また、「何件メールがトレイにあるか」などは、それこそ
lsとwcを使えば事足ります。captiveでないので、なんとかなります。</p>
<p>　今回は正直言いまして、
かなりエクストリームなプログラミングになってしまいましたので、
次回からはもうちょっとマイルドな話題を扱いたいと思います。</p>
</div>
</div>


