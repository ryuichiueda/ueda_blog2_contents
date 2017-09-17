# 開眼シェルスクリプト2012年6月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>6. 開眼シェルスクリプト 第6回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>6.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回から新しい話題を扱います。シェルやシェルスクリプトを使った関係演算です。<br />
関係演算というのは、リレーショナルデータベース管理システム（RDBMS、以下単にDBと表記）に、<br />
SQLでJOINやSELECTなどと命令を書いて行わせる処理のことをここでは指しています。</p><br />
<p>　DBを使うと、排他制御やユーザの管理など様々な便利機能も利用できるのですが、<br />
関係演算だけならテキストファイルでもできます。<br />
テキストファイルで関係演算ができると、<br />
端末だけで作業が簡潔することが非常に多くなります。<br />
今回は端末でファイル操作する方法を覚えて、<br />
次回でシェルスクリプトで簡単なシステムを作ります。</p><br />
<p>　USP研究所ではシェルスクリプトでNoSQLなシステムを作って実績もあげていますので、<br />
これから紹介する方法の延長でデータストアを作ることも可能です。<br />
これについても面白い事例が多いので紹介したいのですが、<br />
これは別の機会に譲ることとします。</p><br />
<div class="section" id="id3"><br />
<h3>6.1.1. 自由を保つ<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　データをフラットテキストで保存すると話が早いことは、本連載の第一回にも述べました。<br />
わざわざ表計算ソフトやDBがあるのにテキストを使うのは大変そうですが、<br />
実は自由が効く方法です。<br />
おなじみGancarzのUNIX哲学に次の格言があります。</p><br />
<ul class="simple"><br />
<li>Avoid captive user interfaces （束縛するインタフェースは作るな。）</li><br />
</ul><br />
<p>これは、コマンドは対話的に作ってはいけないということを言っています。<br />
例えば、あるDBソフトのCUIクライアントを起動すると、</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>hogesql<br />
SQL&gt;<br />
</pre></div><br />
</div><br />
<p>のように、コマンドの入力プロンプトから<br />
SQLの入力プロンプトに変わってしまうのですが、<br />
一旦こうなってしまうとquitするまでgrepもcatもリダイレクトも使えなくなります。<br />
全部SQLで書かなくてはなりません。<br />
GUIを持つアプリケーションでも同じで、<br />
アプリケーションの中で全部操作を行うことになります。<br />
そうなってしまうとソフトウェアの方は全部の操作を引き受ける必要が生じて巨大化します。<br />
巨大化の途中には頻繁にバージョンアップも起こるでしょう。<br />
互換性の問題も発生します。</p><br />
<p>　逆に、テキストファイルだけでデータを管理する場合、<br />
「公式マニュアル」が存在していないので、<br />
それは欠点までとは言わなくとも不利な点でしょう。<br />
でも、テキストですからいつでも表計算ソフトにコピペできます。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>6.2. コマンドの使い方<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はTukubaiコマンドの <tt class="docutils literal"><span class="pre">join0,</span> <span class="pre">join1,</span> <span class="pre">join2</span></tt> を使います。<br />
LinuxやFreeBSDにはjoinという標準のコマンドがあるのですが、<br />
オプションがややこしいのでこれは使いません。<br />
また、今回の端末上でのコードは、<br />
Ubuntu Linux 11.10のbash 4.2上で試しながら書きました。</p><br />
<div class="section" id="join1"><br />
<h3>6.2.1. join1<a class="headerlink" href="#join1" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず、join0より先にjoin1を説明します。join1はファイル同士をキーでくっつけるコマンドです。<br />
リスト1、2が典型的な使い方です。魚屋の例です。</p><br />
<p>　リスト1のfile1は、魚卵に二桁のコードをつけて管理しているマスタ台帳です。<br />
同じくリスト2のfile2は、ある日、<br />
何がいくつ売れたかを記録したファイルです（トランザクションと呼ばれます）。<br />
file1とfile2を突き合わせると、マスタ台帳にある項目が、<br />
いつ、どれだけ売れたかを知ることができます。</p><br />
<p>↓リスト1: マスタファイルとトランザクションファイル</p><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@sakura 201206<span class="o">]</span><span class="nv">$ </span>cat file1<br />
01 たらこ<br />
02 いくら<br />
03 キャビア<br />
04 カラスミ<br />
<span class="o">[</span>ueda\@sakura 201206<span class="o">]</span><span class="nv">$ </span>cat file2<br />
20120104 01 10<br />
20120104 02 321<br />
20120104 03 13<br />
20120105 02 211<br />
20120105 05 12<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　join1は、まさにこのような用途に作られたコマンドで、リスト2のように使います。</p><br />
<p>↓リスト2: join1の使い方</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join1 <span class="nv">key</span><span class="o">=</span>2 file1 -<br />
20120104 01 たらこ 10<br />
20120104 02 いくら 321<br />
20120105 02 いくら 211<br />
20120104 03 キャビア 13<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　まず、 <tt class="docutils literal"><span class="pre">join1</span> <span class="pre">key=2</span> <span class="pre">file1</span> <span class="pre">-</span></tt> について。<br />
<tt class="docutils literal"><span class="pre">key=2</span></tt> は、トランザクションファイルの第2フィールドにキーがあるという意味です。<br />
キーの次にマスタ、その次にトランザクションのファイルを指定します。<br />
<tt class="docutils literal"><span class="pre">-</span></tt> は、ファイルの代わりに標準入力を指定するためのオプションで、<br />
例えばcatなどでも使える一般的な記法です。<br />
マスタファイルは、必ず左側にキーがあってソートされていなければなりません。<br />
トランザクションを <tt class="docutils literal"><span class="pre">key=2</span></tt> で指定すると、トランザクションの第二フィールドと、<br />
マスタの第一フィールドを突き合わせます。</p><br />
<p>　この例では、join1の前にトランザクションをソートしていますが、join1に入力するデータは、<br />
キーでソートしなければなりません。ソートしていないと、レコードが抜け落ちます。<br />
sortにLANG=Cと打つのは、sortはLANG環境によってソート順が違ってしまい混乱する場合があるので、<br />
それを避けるように書いています。</p><br />
</div><br />
<div class="section" id="join2"><br />
<h3>6.2.2. トランザクションのレコードを残すjoin2<a class="headerlink" href="#join2" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　join2は、join1と同じ記法で使えますが、挙動が違います。<br />
リスト3とリスト2を比べると分かるのですが、<br />
join2はマスタに記録のないトランザクションのレコードも残します。<br />
マスタに無いものを急遽売ったときに、<br />
売上の計算でそれを抜いて計算することはないので、<br />
そのようなときにjoin2を使います。</p><br />
<p>リスト3: join2の使用</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join2 <span class="nv">key</span><span class="o">=</span>2 file1 -<br />
20120104 01 たらこ 10<br />
20120104 02 いくら 321<br />
20120105 02 いくら 211<br />
20120104 03 キャビア 13<br />
20120105 05 ****** 12<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="join0"><br />
<h3>6.2.3. 論理演算するjoin0<a class="headerlink" href="#join0" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　join1,2はマスタファイルの項目をトランザクションにくっつけますが、<br />
join0はマスタにある項目をトランザクションから抽出します。</p><br />
<p>リスト3: join0の使用</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#トランザクション</span><br />
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 <span class="nv">key</span><span class="o">=</span>2 file1 -<br />
20120104 01 10<br />
20120104 02 321<br />
20120105 02 211<br />
20120104 03 13<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　逆にマスタにない項目を抽出することもできます。<br />
<tt class="docutils literal"><span class="pre">+ng</span></tt> というオプションをつけると、<br />
標準エラー出力からマスタにないトランザクション項目が出力されます。<br />
（標準エラー出力を使うので、下手をするとエラーが出てきますが・・・）</p><br />
<p>リスト4: join0を使ってマスタにないものを抽出</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#標準出力からはマスタとマッチしたものが出力される。</span><br />
<span class="c">#この場合は捨てる。</span><br />
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 +ng <span class="nv">key</span><span class="o">=</span>2 file1 - &gt; /dev/null<br />
20120105 05 12<br />
<span class="c">#標準エラー出力を標準出力に振り向けて、もとの標準出力の結果を捨てる。</span><br />
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 +ng <span class="nv">key</span><span class="o">=</span>2 file1 - 2&gt;&amp;1 &gt; /dev/null<br />
20120105 05 12<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">+ng</span></tt> はjoin1でも使えます。join2の場合はトランザクションが全部残るので、<br />
join2には <tt class="docutils literal"><span class="pre">+ng</span></tt> はありません。</p><br />
</div><br />
</div><br />
<div class="section" id="id5"><br />
<h2>6.3. お題：シェルスクリプトで会員管理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、架空の団体「UPS友の会」の会員管理業務を行います。<br />
UPS友の会には、会を取り仕切る「スタッフ」がいます。<br />
事務局には、次のようなリストがあります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat STAFF<br />
S001 上田 ueda\@hogehoge.com<br />
S002 濱田 hamada\@nullnull.com<br />
S003 鎌田 kamata\@x-japan.com<br />
S004 松浦 matura\@superstrongmachine.com<br />
</pre></div><br />
</td></tr></table></div><br />
<p>見れば分かるように、第一フィールドが通し番号（スタッフ番号）、<br />
第二フィールドが名前（例なのでfamily nameだけ）、第三フィールドが電子メールアドレスです。念のため、メールアドレスは架空のものとお断りしておきます。</p><br />
<p>　会員も、スタッフと同じフォーマットのリストで管理しています。<br />
第一フィールドは会員番号です。<br />
本当はUPS友の会には会員が100万人いるのですが、<br />
人数は10人にして、会員番号は3桁にしておきます。</p><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat MEMBER<br />
M001 上田 ueda\@hogehoge.com<br />
M002 濱田 hamada\@nullnull.com<br />
M003 武田 takeda\@takenaka.com<br />
M004 竹中 takenaka\@takeda.com<br />
M005 田中 tanaka\@hogehogeho.jp<br />
M006 鎌田 kamata\@x-japan.com<br />
M007 田上 tanoue\@tanoue.co.jp<br />
M008 武山 takeyama\@zzz.com<br />
M009 山本 yamamoto\@bash.co.jp<br />
M010 山口 yamaguchi\@daioujyou.com<br />
</pre></div><br />
</td></tr></table></div><br />
<p>会員にもスタッフにも住所は聞いていないので、個人の識別はメールアドレスで行っています。</p><br />
<p>　UPS友の会の主な活動は、電源に関する勉強会です。<br />
次の勉強会は6月にあり、現在、勉強会への参加者を募集しています。<br />
現在の参加者リストは次のようになってます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat STUDY.201206<br />
takeda\@takenaka.com 武田<br />
yamakura\@hogehogeho.jp 山倉<br />
hamada\@nullnull.com 濱田<br />
tanoue\@tanoue.co.jp 田上<br />
ueda\@hogehoge.com 上田<br />
sinozuka\@zzz.com 篠塚<br />
yamaguchi\@daioujyou.com 山口<br />
yamamoto\@bash.co.jp 山本<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　では、この3個のファイルに対して、リレーショナルな演算をしてみましょう。</p><br />
<div class="section" id="id6"><br />
<h3>6.3.1. スタッフなのに、会員になってない人のあぶり出し<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず最初の例です。この会の会長は、<br />
面白そうな人に声をかけてUPS友の会のスタッフにしているのですが、<br />
こういうスタッフの集め方をしていると<br />
「スタッフなのに会員になっていない人」が出る可能性があります。<br />
会費を取りたいので、しばらく泳がせてから会費を請求して会員にしています。<br />
そのようなスタッフのあぶり出しです。（注意：あくまで架空の話）</p><br />
<p>　これくらいなら、わざわざシェルスクリプトを書くよりも、<br />
出力を見ながら手作業でやったほうがよさそうです。<br />
端末で、まずキー項目（メールアドレス）をファイルの左側に寄せて、<br />
キーでソートします。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#端末をいじるときは作業ディレクトリを作って、</span><br />
<span class="c">#必要なファイルをコピーしてくること</span><br />
<span class="nv">$ </span>self 3 1 2 MEMBER | sort &gt; member<br />
<span class="nv">$ </span>self 3 1 2 STAFF | sort &gt; staff<br />
<span class="nv">$ </span>head -n 3 member <span class="nv">staff</span><br />
<span class="o">==</span>&gt; member &lt;<span class="o">==</span><br />
hamada\@nullnull.com M002 濱田<br />
kamata\@x-japan.com M006 鎌田<br />
takeda\@takenaka.com M003 武田<br />
<br />
<span class="o">==</span>&gt; staff &lt;<span class="o">==</span><br />
hamada\@nullnull.com S002 濱田<br />
kamata\@x-japan.com S003 鎌田<br />
matura\@superstrongmachine.com S004 松浦<br />
</pre></div><br />
</div><br />
<p>　トランザクションにあって、マスタにあるもの／ないものの抽出は、join0で行います。<br />
ここでは会員リストをマスタ扱いにして、会員のスタッフ、非会員のスタッフを分別します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>join0 +ng <span class="nv">key</span><span class="o">=</span>1 member staff &gt; staff_member 2&gt; staff_nonmember<br />
<span class="c"># 会員かつスタッフ</span><br />
<span class="nv">$ </span>cat staff_member<br />
hamada\@nullnull.com S002 濱田<br />
kamata\@x-japan.com S003 鎌田<br />
ueda\@hogehoge.com S001 上田<br />
<span class="c"># 会員でないスタッフ</span><br />
<span class="nv">$ </span>cat staff_nonmember<br />
matura\@superstrongmachine.com S004 松浦<br />
</pre></div><br />
</div><br />
<p>はい。あぶり出しました。松浦さんには、入会案内と請求書が送られることになります。</p><br />
</div><br />
<div class="section" id="id7"><br />
<h3>6.3.2. 勉強会の会費計算<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次に、6月の勉強会の収入を確認します。<br />
UPS友の会の勉強会では、飲み物やお菓子代程度の会費を集めています。<br />
会費は次のように設定しています。</p><br />
<ul class="simple"><br />
<li>スタッフ：無料（当日の労働が参加費）</li><br />
<li>会員：300円</li><br />
<li>非会員：500円</li><br />
</ul><br />
<p>　この計算は、勉強会参加リスト（STUDY.201206）をトランザクションにして、<br />
マスタの情報をくっつけていき、最後に各レコードに金額を付与して計算します。</p><br />
<p>　まず、ソートから。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sort STUDY.201206 &gt; study<br />
<span class="nv">$ </span>head -n 3 study<br />
hamada\@nullnull.com 濱田<br />
sinozuka\@zzz.com 篠塚<br />
takeda\@takenaka.com 武田<br />
</pre></div><br />
</div><br />
<p>次に、順にマスタ情報をくっつけていきます。<br />
レコードが落ちてはいけませんから、join2を使います。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat study | join2 <span class="nv">key</span><span class="o">=</span>1 member - | join2 <span class="nv">key</span><span class="o">=</span>1 staff - | head -n 3<br />
hamada\@nullnull.com S002 濱田 M002 濱田 濱田<br />
sinozuka\@zzz.com **** **** **** **** 篠塚<br />
takeda\@takenaka.com **** **** M003 武田 武田<br />
</pre></div><br />
</div><br />
<p>必要なフィールドだけ取り出して、数を数えます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#必要なフィールド：スタッフ番号、会員番号の頭のアルファベット</span><br />
<span class="nv">$ </span>cat study | join2 <span class="nv">key</span><span class="o">=</span>1 member | join2 <span class="nv">key</span><span class="o">=</span>1 staff | self 2.1.1 4.1.1 | tr <span class="s1">&#39;*&#39;</span> <span class="s1">&#39;\@&#39;</span><br />
<span class="nv">$ </span>cat tmp<br />
S M<br />
\@ \@<br />
\@ M<br />
\@ M<br />
S M<br />
\@ M<br />
\@ \@<br />
\@ M<br />
<span class="c">#どの区分の人が何人いるか？</span><br />
<span class="nv">$ </span>sort tmp | count 1 2<br />
\@ \@ 2<br />
\@ M 4<br />
S M 2<br />
</pre></div><br />
</div><br />
<p>これくらい簡単な話であればあとは手で計算すれば十分ですが、<br />
次のように最後まで計算を進めることができます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#awkで金額を出す。</span><br />
<span class="nv">$ </span>sort tmp | count 1 2 | awk <span class="s1">&#39;/\@ \@/{print $3*500}/\@ M/{print $3*300}&#39;</span><br />
1000<br />
1200<br />
<span class="c">#sm2（Tukubaiコマンド）で合計</span><br />
<span class="nv">$ </span>sort tmp | count 1 2 | awk <span class="s1">&#39;/\@ \@/{print $3*500}/\@ M/{print $3*300}&#39;</span> | sm2 0 0 1 1<br />
2200<br />
</pre></div><br />
</div><br />
<p>　この処理では、少し面白いawkの使い方をしています。<br />
awkは、</p><br />
<div class="highlight-bash"><div class="highlight"><pre>awk <span class="s1">&#39;パターン1{処理1}パターン2{処理2}パターン3{処理3}...&#39;</span><br />
</pre></div><br />
</div><br />
<p>という書き方ができます。<br />
awkはパターンがあると、行を読み込んだときに各パターンと照合して、<br />
合致したら、そのパターンに対応する処理を行います。<br />
二つ以上のパターンに一致するときは、それぞれの処理が同じ行に適用されます。</p><br />
<p>　また、この処理のパターン <tt class="docutils literal"><span class="pre">/&#64;</span> <span class="pre">&#64;/</span></tt> や <tt class="docutils literal"><span class="pre">/&#64;</span> <span class="pre">M/</span></tt> は、<br />
<tt class="docutils literal"><span class="pre">$0~/&#64;</span> <span class="pre">&#64;/</span></tt> や <tt class="docutils literal"><span class="pre">$0~/&#64;</span> <span class="pre">M/</span></tt> と同じ意味で、<br />
行全体に対して正規表現を当てはめる処理です。</p><br />
<p>　もう一点。 <tt class="docutils literal"><span class="pre">sm2</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">1</span> <span class="pre">1</span></tt> は、<br />
入力の第一フィールドを合計するために使われています。<br />
sm2はTukubaiコマンドで、以下のように使います。<br />
4個オプションがありますが、前二つでキーの範囲、後ろ二つで値の範囲を指定します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#こういう情報を処理します。</span><br />
<span class="nv">$ </span>cat BASS<br />
バース SD 1980 3<br />
バース SD 1981 4<br />
バース SD 1982 1<br />
バース TEX 1982 1<br />
バース 阪神 1983 35<br />
バース 阪神 1984 27<br />
バース 阪神 1985 54<br />
バース 阪神 1986 47<br />
バース 阪神 1987 37<br />
バース 阪神 1988 2<br />
<span class="c">#$1（第1フィールド）をキーに$4を合計</span><br />
<span class="nv">$ </span>cat BASS | sm2 1 1 4 4<br />
<span class="c">#キーを無視して$4を合計</span><br />
バース 211<br />
<span class="nv">$ </span>cat BASS | sm2 0 0 4 4<br />
211<br />
<span class="c">#$1、$2をキーに$4を合計</span><br />
<span class="nv">$ </span>cat BASS | sm2 1 2 4 4<br />
バース SD 8<br />
バース TEX 1<br />
バース 阪神 202<br />
<span class="c">#BASSファイルから$2を削除の後、年毎に集計</span><br />
<span class="nv">$ </span>cat BASS | delf 2 | sm2 1 2 3 3<br />
バース 1980 3<br />
バース 1981 4<br />
バース 1982 2<br />
バース 1983 35<br />
バース 1984 27<br />
バース 1985 54<br />
バース 1986 47<br />
バース 1987 37<br />
バース 1988 2<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h3>6.3.3. 会員を追加する<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　勉強会はおおいに盛り上がり、非会員だった人が全員その場で入会を希望しました。<br />
<tt class="docutils literal"><span class="pre">STUDY.201206</span></tt> ファイルから <tt class="docutils literal"><span class="pre">MEMBER</span></tt> ファイルに会員を追加しましょう。<br />
まずは、非会員の勉強会参加者を抽出します。<br />
キーをソートしてからjoin0の+ngオプションで非会員を抽出します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sort STUDY.201206 &gt; study<br />
<span class="nv">$ </span>head -n 3 study<br />
hamada\@nullnull.com 濱田<br />
sinozuka\@zzz.com 篠塚<br />
takeda\@takenaka.com 武田<br />
<span class="nv">$ </span>self 3 MEMBER | sort | join0 +ng <span class="nv">key</span><span class="o">=</span>1 - study &gt; /dev/null 2&gt; tmp<br />
<span class="nv">$ </span>self 2 1 tmp &gt; newmember<br />
<span class="nv">$ </span>cat newmember<br />
篠塚 sinozuka\@zzz.com<br />
山倉 yamakura\@hogehogeho.jp<br />
</pre></div><br />
</div><br />
<p>次のように一気に書くこともできますので一応示しておきますが、<br />
無理に一気に書くことはあまりしないほうがよいと思います。<br />
手作業なので、少しずつファイルにリダイレクトして中身を確認して進めましょう。<br />
<tt class="docutils literal"><span class="pre">&lt;()</span></tt> は、括弧内の処理をファイルのようにコマンドに入力するための記号ですが、<br />
処理の流れが一方通行でなくなるので筆者の場合は滅多に使いません。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>self 3 MEMBER | sort | join0 +ng <span class="nv">key</span><span class="o">=</span>1 - &lt;<span class="o">(</span>sort STUDY.201206<span class="o">)</span> 2&gt;&amp;1 &gt; /dev/null | self 2 1<br />
篠塚 sinozuka\@zzz.com<br />
山倉 yamakura\@hogehogeho.jp<br />
</pre></div><br />
</div><br />
<p>あとはファイルをくっつけて番号を打ち直せば新しいリストができます。<br />
次の方法も一気にやっていますが、いちいち出力を見ながら書いて行ったものです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/^M0*//&#39;</span> MEMBER | cat - newmember | awk <span class="s1">&#39;{if(NF==3){n=$1;print}else{print ++n,$0}}&#39;</span> | awk <span class="s1">&#39;{print sprintf(&quot;M%03d&quot;,$1),$2,$3}&#39;</span> &gt; MEMBER.new<br />
<span class="nv">$ </span>cat MEMBER.new<br />
M001 上田 ueda\@hogehoge.com<br />
M002 濱田 hamada\@nullnull.com<br />
M003 武田 takeda\@takenaka.com<br />
M004 竹中 takenaka\@takeda.com<br />
M005 田中 tanaka\@hogehogeho.jp<br />
M006 鎌田 kamata\@x-japan.com<br />
M007 田上 tanoue\@tanoue.co.jp<br />
M008 武山 takeyama\@zzz.com<br />
M009 山本 yamamoto\@bash.co.jp<br />
M010 山口 yamaguchi\@daioujyou.com<br />
M011 篠塚 sinozuka\@zzz.com<br />
M012 山倉 yamakura\@hogehogeho.jp<br />
</pre></div><br />
</div><br />
<p>　ところで、このような端末操作は常に間違いがつきまといます。<br />
ちゃんとチェックしましょう。<br />
少なくとも、diffには必ず通します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>diff MEMBER MEMBER.new<br />
10a11,12<br />
&gt; M011 篠塚 sinozuka\@zzz.com<br />
&gt; M012 山倉 yamakura\@hogehogeho.jp<br />
</pre></div><br />
</div><br />
<p>もっとレコード数が大きくて目で確認するのが大変なときは、<br />
次のような方法もあります。<br />
gyoは、ファイルの行数を出力するコマンドです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#既存のレコードに変更がないことを確認</span><br />
<span class="nv">$ </span>diff MEMBER MEMBER.new | grep <span class="s1">&#39;^&lt;&#39;</span> | gyo<br />
0<br />
<span class="c">#新規レコード数を確認</span><br />
<span class="nv">$ </span>diff MEMBER MEMBER.new | grep <span class="s1">&#39;^&gt;&#39;</span> | gyo<br />
2<br />
</pre></div><br />
</div><br />
<p>これで納得したらファイルを更新します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>mv MEMBER MEMBER.20120601<br />
<span class="nv">$ </span>mv MEMBER.new MEMBER<br />
</pre></div><br />
</div><br />
</div><br />
</div><br />
<div class="section" id="id9"><br />
<h2>6.4. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はTukubaiコマンドのjoin0,1,2を使ってファイルの関係演算をしました。<br />
コマンドがたった3個増えるだけで、<br />
できることがずいぶん広がったと思っていただければ今回は成功だと思います。<br />
これは、「インタフェースを束縛しない」効果だと言えます。</p><br />
<p>　次回は、UPS友の会の会員情報を、<br />
もうちょっとシステマチックに管理するシェルスクリプトを扱います。<br />
特に最後のファイル更新前のチェックは、<br />
シェルスクリプトにして機械的にした方がよさそうです。<br />
エラーチェックには例外処理などの仕組みが必要なので、<br />
シェルスクリプトでどうそれを実装するかを扱いたいと思います。</p><br />
</div><br />
</div><br />
<br />

