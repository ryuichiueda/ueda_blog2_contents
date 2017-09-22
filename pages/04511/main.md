---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年6月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>6. 開眼シェルスクリプト 第6回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>6.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回から新しい話題を扱います。シェルやシェルスクリプトを使った関係演算です。
関係演算というのは、リレーショナルデータベース管理システム（RDBMS、以下単にDBと表記）に、
SQLでJOINやSELECTなどと命令を書いて行わせる処理のことをここでは指しています。</p>
<p>　DBを使うと、排他制御やユーザの管理など様々な便利機能も利用できるのですが、
関係演算だけならテキストファイルでもできます。
テキストファイルで関係演算ができると、
端末だけで作業が簡潔することが非常に多くなります。
今回は端末でファイル操作する方法を覚えて、
次回でシェルスクリプトで簡単なシステムを作ります。</p>
<p>　USP研究所ではシェルスクリプトでNoSQLなシステムを作って実績もあげていますので、
これから紹介する方法の延長でデータストアを作ることも可能です。
これについても面白い事例が多いので紹介したいのですが、
これは別の機会に譲ることとします。</p>
<div class="section" id="id3">
<h3>6.1.1. 自由を保つ<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　データをフラットテキストで保存すると話が早いことは、本連載の第一回にも述べました。
わざわざ表計算ソフトやDBがあるのにテキストを使うのは大変そうですが、
実は自由が効く方法です。
おなじみGancarzのUNIX哲学に次の格言があります。</p>
<ul class="simple">
<li>Avoid captive user interfaces （束縛するインタフェースは作るな。）</li>
</ul>
<p>これは、コマンドは対話的に作ってはいけないということを言っています。
例えば、あるDBソフトのCUIクライアントを起動すると、</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>hogesql
SQL&gt;
</pre></div>
</div>
<p>のように、コマンドの入力プロンプトから
SQLの入力プロンプトに変わってしまうのですが、
一旦こうなってしまうとquitするまでgrepもcatもリダイレクトも使えなくなります。
全部SQLで書かなくてはなりません。
GUIを持つアプリケーションでも同じで、
アプリケーションの中で全部操作を行うことになります。
そうなってしまうとソフトウェアの方は全部の操作を引き受ける必要が生じて巨大化します。
巨大化の途中には頻繁にバージョンアップも起こるでしょう。
互換性の問題も発生します。</p>
<p>　逆に、テキストファイルだけでデータを管理する場合、
「公式マニュアル」が存在していないので、
それは欠点までとは言わなくとも不利な点でしょう。
でも、テキストですからいつでも表計算ソフトにコピペできます。</p>
</div>
</div>
<div class="section" id="id4">
<h2>6.2. コマンドの使い方<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はTukubaiコマンドの <tt class="docutils literal"><span class="pre">join0,</span> <span class="pre">join1,</span> <span class="pre">join2</span></tt> を使います。
LinuxやFreeBSDにはjoinという標準のコマンドがあるのですが、
オプションがややこしいのでこれは使いません。
また、今回の端末上でのコードは、
Ubuntu Linux 11.10のbash 4.2上で試しながら書きました。</p>
<div class="section" id="join1">
<h3>6.2.1. join1<a class="headerlink" href="#join1" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず、join0より先にjoin1を説明します。join1はファイル同士をキーでくっつけるコマンドです。
リスト1、2が典型的な使い方です。魚屋の例です。</p>
<p>　リスト1のfile1は、魚卵に二桁のコードをつけて管理しているマスタ台帳です。
同じくリスト2のfile2は、ある日、
何がいくつ売れたかを記録したファイルです（トランザクションと呼ばれます）。
file1とfile2を突き合わせると、マスタ台帳にある項目が、
いつ、どれだけ売れたかを知ることができます。</p>
<p>↓リスト1: マスタファイルとトランザクションファイル</p>
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@sakura 201206<span class="o">]</span><span class="nv">$ </span>cat file1
01 たらこ
02 いくら
03 キャビア
04 カラスミ
<span class="o">[</span>ueda\@sakura 201206<span class="o">]</span><span class="nv">$ </span>cat file2
20120104 01 10
20120104 02 321
20120104 03 13
20120105 02 211
20120105 05 12
</pre></div>
</td></tr></table></div>
<p>　join1は、まさにこのような用途に作られたコマンドで、リスト2のように使います。</p>
<p>↓リスト2: join1の使い方</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join1 <span class="nv">key</span><span class="o">=</span>2 file1 -
20120104 01 たらこ 10
20120104 02 いくら 321
20120105 02 いくら 211
20120104 03 キャビア 13
</pre></div>
</td></tr></table></div>
<p>　まず、 <tt class="docutils literal"><span class="pre">join1</span> <span class="pre">key=2</span> <span class="pre">file1</span> <span class="pre">-</span></tt> について。
<tt class="docutils literal"><span class="pre">key=2</span></tt> は、トランザクションファイルの第2フィールドにキーがあるという意味です。
キーの次にマスタ、その次にトランザクションのファイルを指定します。
<tt class="docutils literal"><span class="pre">-</span></tt> は、ファイルの代わりに標準入力を指定するためのオプションで、
例えばcatなどでも使える一般的な記法です。
マスタファイルは、必ず左側にキーがあってソートされていなければなりません。
トランザクションを <tt class="docutils literal"><span class="pre">key=2</span></tt> で指定すると、トランザクションの第二フィールドと、
マスタの第一フィールドを突き合わせます。</p>
<p>　この例では、join1の前にトランザクションをソートしていますが、join1に入力するデータは、
キーでソートしなければなりません。ソートしていないと、レコードが抜け落ちます。
sortにLANG=Cと打つのは、sortはLANG環境によってソート順が違ってしまい混乱する場合があるので、
それを避けるように書いています。</p>
</div>
<div class="section" id="join2">
<h3>6.2.2. トランザクションのレコードを残すjoin2<a class="headerlink" href="#join2" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　join2は、join1と同じ記法で使えますが、挙動が違います。
リスト3とリスト2を比べると分かるのですが、
join2はマスタに記録のないトランザクションのレコードも残します。
マスタに無いものを急遽売ったときに、
売上の計算でそれを抜いて計算することはないので、
そのようなときにjoin2を使います。</p>
<p>リスト3: join2の使用</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join2 <span class="nv">key</span><span class="o">=</span>2 file1 -
20120104 01 たらこ 10
20120104 02 いくら 321
20120105 02 いくら 211
20120104 03 キャビア 13
20120105 05 ****** 12
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="join0">
<h3>6.2.3. 論理演算するjoin0<a class="headerlink" href="#join0" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　join1,2はマスタファイルの項目をトランザクションにくっつけますが、
join0はマスタにある項目をトランザクションから抽出します。</p>
<p>リスト3: join0の使用</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#トランザクション</span>
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 <span class="nv">key</span><span class="o">=</span>2 file1 -
20120104 01 10
20120104 02 321
20120105 02 211
20120104 03 13
</pre></div>
</td></tr></table></div>
<p>　逆にマスタにない項目を抽出することもできます。
<tt class="docutils literal"><span class="pre">+ng</span></tt> というオプションをつけると、
標準エラー出力からマスタにないトランザクション項目が出力されます。
（標準エラー出力を使うので、下手をするとエラーが出てきますが・・・）</p>
<p>リスト4: join0を使ってマスタにないものを抽出</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#標準出力からはマスタとマッチしたものが出力される。</span>
<span class="c">#この場合は捨てる。</span>
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 +ng <span class="nv">key</span><span class="o">=</span>2 file1 - &gt; /dev/null
20120105 05 12
<span class="c">#標準エラー出力を標準出力に振り向けて、もとの標準出力の結果を捨てる。</span>
<span class="nv">$ LANG</span><span class="o">=</span>C sort -k2,2 file2 | join0 +ng <span class="nv">key</span><span class="o">=</span>2 file1 - 2&gt;&amp;1 &gt; /dev/null
20120105 05 12
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">+ng</span></tt> はjoin1でも使えます。join2の場合はトランザクションが全部残るので、
join2には <tt class="docutils literal"><span class="pre">+ng</span></tt> はありません。</p>
</div>
</div>
<div class="section" id="id5">
<h2>6.3. お題：シェルスクリプトで会員管理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、架空の団体「UPS友の会」の会員管理業務を行います。
UPS友の会には、会を取り仕切る「スタッフ」がいます。
事務局には、次のようなリストがあります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat STAFF
S001 上田 ueda\@hogehoge.com
S002 濱田 hamada\@nullnull.com
S003 鎌田 kamata\@x-japan.com
S004 松浦 matura\@superstrongmachine.com
</pre></div>
</td></tr></table></div>
<p>見れば分かるように、第一フィールドが通し番号（スタッフ番号）、
第二フィールドが名前（例なのでfamily nameだけ）、第三フィールドが電子メールアドレスです。念のため、メールアドレスは架空のものとお断りしておきます。</p>
<p>　会員も、スタッフと同じフォーマットのリストで管理しています。
第一フィールドは会員番号です。
本当はUPS友の会には会員が100万人いるのですが、
人数は10人にして、会員番号は3桁にしておきます。</p>
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat MEMBER
M001 上田 ueda\@hogehoge.com
M002 濱田 hamada\@nullnull.com
M003 武田 takeda\@takenaka.com
M004 竹中 takenaka\@takeda.com
M005 田中 tanaka\@hogehogeho.jp
M006 鎌田 kamata\@x-japan.com
M007 田上 tanoue\@tanoue.co.jp
M008 武山 takeyama\@zzz.com
M009 山本 yamamoto\@bash.co.jp
M010 山口 yamaguchi\@daioujyou.com
</pre></div>
</td></tr></table></div>
<p>会員にもスタッフにも住所は聞いていないので、個人の識別はメールアドレスで行っています。</p>
<p>　UPS友の会の主な活動は、電源に関する勉強会です。
次の勉強会は6月にあり、現在、勉強会への参加者を募集しています。
現在の参加者リストは次のようになってます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat STUDY.201206
takeda\@takenaka.com 武田
yamakura\@hogehogeho.jp 山倉
hamada\@nullnull.com 濱田
tanoue\@tanoue.co.jp 田上
ueda\@hogehoge.com 上田
sinozuka\@zzz.com 篠塚
yamaguchi\@daioujyou.com 山口
yamamoto\@bash.co.jp 山本
</pre></div>
</td></tr></table></div>
<p>　では、この3個のファイルに対して、リレーショナルな演算をしてみましょう。</p>
<div class="section" id="id6">
<h3>6.3.1. スタッフなのに、会員になってない人のあぶり出し<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず最初の例です。この会の会長は、
面白そうな人に声をかけてUPS友の会のスタッフにしているのですが、
こういうスタッフの集め方をしていると
「スタッフなのに会員になっていない人」が出る可能性があります。
会費を取りたいので、しばらく泳がせてから会費を請求して会員にしています。
そのようなスタッフのあぶり出しです。（注意：あくまで架空の話）</p>
<p>　これくらいなら、わざわざシェルスクリプトを書くよりも、
出力を見ながら手作業でやったほうがよさそうです。
端末で、まずキー項目（メールアドレス）をファイルの左側に寄せて、
キーでソートします。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#端末をいじるときは作業ディレクトリを作って、</span>
<span class="c">#必要なファイルをコピーしてくること</span>
<span class="nv">$ </span>self 3 1 2 MEMBER | sort &gt; member
<span class="nv">$ </span>self 3 1 2 STAFF | sort &gt; staff
<span class="nv">$ </span>head -n 3 member <span class="nv">staff</span>
<span class="o">==</span>&gt; member &lt;<span class="o">==</span>
hamada\@nullnull.com M002 濱田
kamata\@x-japan.com M006 鎌田
takeda\@takenaka.com M003 武田

<span class="o">==</span>&gt; staff &lt;<span class="o">==</span>
hamada\@nullnull.com S002 濱田
kamata\@x-japan.com S003 鎌田
matura\@superstrongmachine.com S004 松浦
</pre></div>
</div>
<p>　トランザクションにあって、マスタにあるもの／ないものの抽出は、join0で行います。
ここでは会員リストをマスタ扱いにして、会員のスタッフ、非会員のスタッフを分別します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>join0 +ng <span class="nv">key</span><span class="o">=</span>1 member staff &gt; staff_member 2&gt; staff_nonmember
<span class="c"># 会員かつスタッフ</span>
<span class="nv">$ </span>cat staff_member
hamada\@nullnull.com S002 濱田
kamata\@x-japan.com S003 鎌田
ueda\@hogehoge.com S001 上田
<span class="c"># 会員でないスタッフ</span>
<span class="nv">$ </span>cat staff_nonmember
matura\@superstrongmachine.com S004 松浦
</pre></div>
</div>
<p>はい。あぶり出しました。松浦さんには、入会案内と請求書が送られることになります。</p>
</div>
<div class="section" id="id7">
<h3>6.3.2. 勉強会の会費計算<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次に、6月の勉強会の収入を確認します。
UPS友の会の勉強会では、飲み物やお菓子代程度の会費を集めています。
会費は次のように設定しています。</p>
<ul class="simple">
<li>スタッフ：無料（当日の労働が参加費）</li>
<li>会員：300円</li>
<li>非会員：500円</li>
</ul>
<p>　この計算は、勉強会参加リスト（STUDY.201206）をトランザクションにして、
マスタの情報をくっつけていき、最後に各レコードに金額を付与して計算します。</p>
<p>　まず、ソートから。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sort STUDY.201206 &gt; study
<span class="nv">$ </span>head -n 3 study
hamada\@nullnull.com 濱田
sinozuka\@zzz.com 篠塚
takeda\@takenaka.com 武田
</pre></div>
</div>
<p>次に、順にマスタ情報をくっつけていきます。
レコードが落ちてはいけませんから、join2を使います。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat study | join2 <span class="nv">key</span><span class="o">=</span>1 member - | join2 <span class="nv">key</span><span class="o">=</span>1 staff - | head -n 3
hamada\@nullnull.com S002 濱田 M002 濱田 濱田
sinozuka\@zzz.com **** **** **** **** 篠塚
takeda\@takenaka.com **** **** M003 武田 武田
</pre></div>
</div>
<p>必要なフィールドだけ取り出して、数を数えます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#必要なフィールド：スタッフ番号、会員番号の頭のアルファベット</span>
<span class="nv">$ </span>cat study | join2 <span class="nv">key</span><span class="o">=</span>1 member | join2 <span class="nv">key</span><span class="o">=</span>1 staff | self 2.1.1 4.1.1 | tr <span class="s1">&#39;*&#39;</span> <span class="s1">&#39;\@&#39;</span>
<span class="nv">$ </span>cat tmp
S M
\@ \@
\@ M
\@ M
S M
\@ M
\@ \@
\@ M
<span class="c">#どの区分の人が何人いるか？</span>
<span class="nv">$ </span>sort tmp | count 1 2
\@ \@ 2
\@ M 4
S M 2
</pre></div>
</div>
<p>これくらい簡単な話であればあとは手で計算すれば十分ですが、
次のように最後まで計算を進めることができます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#awkで金額を出す。</span>
<span class="nv">$ </span>sort tmp | count 1 2 | awk <span class="s1">&#39;/\@ \@/{print $3*500}/\@ M/{print $3*300}&#39;</span>
1000
1200
<span class="c">#sm2（Tukubaiコマンド）で合計</span>
<span class="nv">$ </span>sort tmp | count 1 2 | awk <span class="s1">&#39;/\@ \@/{print $3*500}/\@ M/{print $3*300}&#39;</span> | sm2 0 0 1 1
2200
</pre></div>
</div>
<p>　この処理では、少し面白いawkの使い方をしています。
awkは、</p>
<div class="highlight-bash"><div class="highlight"><pre>awk <span class="s1">&#39;パターン1{処理1}パターン2{処理2}パターン3{処理3}...&#39;</span>
</pre></div>
</div>
<p>という書き方ができます。
awkはパターンがあると、行を読み込んだときに各パターンと照合して、
合致したら、そのパターンに対応する処理を行います。
二つ以上のパターンに一致するときは、それぞれの処理が同じ行に適用されます。</p>
<p>　また、この処理のパターン <tt class="docutils literal"><span class="pre">/&#64;</span> <span class="pre">&#64;/</span></tt> や <tt class="docutils literal"><span class="pre">/&#64;</span> <span class="pre">M/</span></tt> は、
<tt class="docutils literal"><span class="pre">$0~/&#64;</span> <span class="pre">&#64;/</span></tt> や <tt class="docutils literal"><span class="pre">$0~/&#64;</span> <span class="pre">M/</span></tt> と同じ意味で、
行全体に対して正規表現を当てはめる処理です。</p>
<p>　もう一点。 <tt class="docutils literal"><span class="pre">sm2</span> <span class="pre">0</span> <span class="pre">0</span> <span class="pre">1</span> <span class="pre">1</span></tt> は、
入力の第一フィールドを合計するために使われています。
sm2はTukubaiコマンドで、以下のように使います。
4個オプションがありますが、前二つでキーの範囲、後ろ二つで値の範囲を指定します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#こういう情報を処理します。</span>
<span class="nv">$ </span>cat BASS
バース SD 1980 3
バース SD 1981 4
バース SD 1982 1
バース TEX 1982 1
バース 阪神 1983 35
バース 阪神 1984 27
バース 阪神 1985 54
バース 阪神 1986 47
バース 阪神 1987 37
バース 阪神 1988 2
<span class="c">#$1（第1フィールド）をキーに$4を合計</span>
<span class="nv">$ </span>cat BASS | sm2 1 1 4 4
<span class="c">#キーを無視して$4を合計</span>
バース 211
<span class="nv">$ </span>cat BASS | sm2 0 0 4 4
211
<span class="c">#$1、$2をキーに$4を合計</span>
<span class="nv">$ </span>cat BASS | sm2 1 2 4 4
バース SD 8
バース TEX 1
バース 阪神 202
<span class="c">#BASSファイルから$2を削除の後、年毎に集計</span>
<span class="nv">$ </span>cat BASS | delf 2 | sm2 1 2 3 3
バース 1980 3
バース 1981 4
バース 1982 2
バース 1983 35
バース 1984 27
バース 1985 54
バース 1986 47
バース 1987 37
バース 1988 2
</pre></div>
</div>
</div>
<div class="section" id="id8">
<h3>6.3.3. 会員を追加する<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　勉強会はおおいに盛り上がり、非会員だった人が全員その場で入会を希望しました。
<tt class="docutils literal"><span class="pre">STUDY.201206</span></tt> ファイルから <tt class="docutils literal"><span class="pre">MEMBER</span></tt> ファイルに会員を追加しましょう。
まずは、非会員の勉強会参加者を抽出します。
キーをソートしてからjoin0の+ngオプションで非会員を抽出します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sort STUDY.201206 &gt; study
<span class="nv">$ </span>head -n 3 study
hamada\@nullnull.com 濱田
sinozuka\@zzz.com 篠塚
takeda\@takenaka.com 武田
<span class="nv">$ </span>self 3 MEMBER | sort | join0 +ng <span class="nv">key</span><span class="o">=</span>1 - study &gt; /dev/null 2&gt; tmp
<span class="nv">$ </span>self 2 1 tmp &gt; newmember
<span class="nv">$ </span>cat newmember
篠塚 sinozuka\@zzz.com
山倉 yamakura\@hogehogeho.jp
</pre></div>
</div>
<p>次のように一気に書くこともできますので一応示しておきますが、
無理に一気に書くことはあまりしないほうがよいと思います。
手作業なので、少しずつファイルにリダイレクトして中身を確認して進めましょう。
<tt class="docutils literal"><span class="pre">&lt;()</span></tt> は、括弧内の処理をファイルのようにコマンドに入力するための記号ですが、
処理の流れが一方通行でなくなるので筆者の場合は滅多に使いません。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>self 3 MEMBER | sort | join0 +ng <span class="nv">key</span><span class="o">=</span>1 - &lt;<span class="o">(</span>sort STUDY.201206<span class="o">)</span> 2&gt;&amp;1 &gt; /dev/null | self 2 1
篠塚 sinozuka\@zzz.com
山倉 yamakura\@hogehogeho.jp
</pre></div>
</div>
<p>あとはファイルをくっつけて番号を打ち直せば新しいリストができます。
次の方法も一気にやっていますが、いちいち出力を見ながら書いて行ったものです。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>sed <span class="s1">&#39;s/^M0*//&#39;</span> MEMBER | cat - newmember | awk <span class="s1">&#39;{if(NF==3){n=$1;print}else{print ++n,$0}}&#39;</span> | awk <span class="s1">&#39;{print sprintf(&quot;M%03d&quot;,$1),$2,$3}&#39;</span> &gt; MEMBER.new
<span class="nv">$ </span>cat MEMBER.new
M001 上田 ueda\@hogehoge.com
M002 濱田 hamada\@nullnull.com
M003 武田 takeda\@takenaka.com
M004 竹中 takenaka\@takeda.com
M005 田中 tanaka\@hogehogeho.jp
M006 鎌田 kamata\@x-japan.com
M007 田上 tanoue\@tanoue.co.jp
M008 武山 takeyama\@zzz.com
M009 山本 yamamoto\@bash.co.jp
M010 山口 yamaguchi\@daioujyou.com
M011 篠塚 sinozuka\@zzz.com
M012 山倉 yamakura\@hogehogeho.jp
</pre></div>
</div>
<p>　ところで、このような端末操作は常に間違いがつきまといます。
ちゃんとチェックしましょう。
少なくとも、diffには必ず通します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>diff MEMBER MEMBER.new
10a11,12
&gt; M011 篠塚 sinozuka\@zzz.com
&gt; M012 山倉 yamakura\@hogehogeho.jp
</pre></div>
</div>
<p>もっとレコード数が大きくて目で確認するのが大変なときは、
次のような方法もあります。
gyoは、ファイルの行数を出力するコマンドです。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#既存のレコードに変更がないことを確認</span>
<span class="nv">$ </span>diff MEMBER MEMBER.new | grep <span class="s1">&#39;^&lt;&#39;</span> | gyo
0
<span class="c">#新規レコード数を確認</span>
<span class="nv">$ </span>diff MEMBER MEMBER.new | grep <span class="s1">&#39;^&gt;&#39;</span> | gyo
2
</pre></div>
</div>
<p>これで納得したらファイルを更新します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>mv MEMBER MEMBER.20120601
<span class="nv">$ </span>mv MEMBER.new MEMBER
</pre></div>
</div>
</div>
</div>
<div class="section" id="id9">
<h2>6.4. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はTukubaiコマンドのjoin0,1,2を使ってファイルの関係演算をしました。
コマンドがたった3個増えるだけで、
できることがずいぶん広がったと思っていただければ今回は成功だと思います。
これは、「インタフェースを束縛しない」効果だと言えます。</p>
<p>　次回は、UPS友の会の会員情報を、
もうちょっとシステマチックに管理するシェルスクリプトを扱います。
特に最後のファイル更新前のチェックは、
シェルスクリプトにして機械的にした方がよさそうです。
エラーチェックには例外処理などの仕組みが必要なので、
シェルスクリプトでどうそれを実装するかを扱いたいと思います。</p>
</div>
</div>


