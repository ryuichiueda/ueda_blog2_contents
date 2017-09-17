# 開眼シェルスクリプト2012年10月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>10. 開眼シェルスクリプト 第10回 オンラインストレージもどきを作る（１）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>10.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回、前々回は並列処理のテクニックを扱いましたが、<br />
今回からは具体的なアプリケーションの作成に戻り、<br />
VPS経由で、複数のマシンのデータを自動で同期する仕組みを作ります。<br />
要はDropboxのようなものですが、さすがにあの完成度で作り切るのは大変ですので、<br />
簡易的なものをシェルスクリプトで作ってみましょう。</p><br />
<p>　作るのは数台のローカルPCの所定のディレクトリを、<br />
リモートのサーバ経由で同期をとるというアプリケーションです。</p><br />
<p>　名前は、Dropboxのアイコンを眺めていたら豆腐のように見えたので、<br />
豆腐ボックスとします。敢えてふにゃふにゃな名前にしましたが、<br />
だからといってかっこいい名前は思いついていません。</p><br />
<p>　豆腐ボックスは、ファイルを消さずにとにかく集積していくように作ります。<br />
削除がからむと途端にコードが面倒になるので、少なくとも今回は扱いません。<br />
その代わり、今回もソースは全部掲載できるほど短くなっています。</p><br />
<p>「政事は豆腐の箱のごとし、箱ゆがめば豆腐ゆがむなり。」 &#8212;- 二宮尊徳</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>10.2. 環境<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、筆者の手持ちのマシンを総動員します。<br />
クライアントPCには、次の二台を準備しました。</p><br />
<ul class="simple"><br />
<li>Ubuntu 12.04 x64 on ThinkPad SL510</li><br />
<li>Ubuntu 12.04 x64 on ThinkPad X201</li><br />
</ul><br />
<p>私の自宅のThinkPadと仕事用のThinkPadです。<br />
この連載にも何回か登場していますが、<br />
現在は64ビット版のUbuntuが搭載されています。</p><br />
<p>　今回はPCのサスペンド機能やデスクトップへの通知機能など、<br />
きわどい機能が登場しますので、一応、Ubuntu Linux上での動作を前提としておきます。<br />
しかし、UNIX系OSならちょっと修正すれば動くはずです。</p><br />
<p>　今回はサーバ側もUbuntuですが、こちらはsshとrsyncが動けば何でもいいでしょう。</p><br />
<ul class="simple"><br />
<li>Ubuntu 12.04 x64 on さくらのVPS （ホスト名：tofu.usptomonokai.jp）</li><br />
</ul><br />
<p>　サーバとクライアント間は、鍵認証でssh接続できることとします。<br />
rsyncのポート指定をいちいち書いていると面倒なので、<br />
tofu.usptomonokai.jpのsshのポート番号は22番とします。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>10.3. 作業開始<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、作っていきましょう。まず、クライアントマシンとサーバに、<br />
リスト1のようにディレクトリを作ります。<br />
クライアント側は、一台でプログラミングして他のマシンにscpすればよいでしょう。</p><br />
<p>・リスト1: ディレクトリ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>/hoge/ueda<br />
├── .tofubox<br />
└── TOFUBOX<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> は同期するディレクトリで、<br />
<tt class="docutils literal"><span class="pre">~/.tofubox/</span></tt> はプログラム等のファイル置き場です。</p><br />
<div class="section" id="rsyncmkdir"><br />
<h3>10.3.1. 豆腐ボックスのコアテクノロジー（単なるrsyncとmkdir）<a class="headerlink" href="#rsyncmkdir" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　rsyncは、各クライアントから起動します。<br />
豆腐ボックスでは、リスト2のコマンドと共に使います。</p><br />
<p>・リスト2: rsyncコマンドの使い方</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#A. リモートからローカルマシンへ同期</span><br />
ueda\@X201:~<span class="nv">$ </span>rsync -auz --timeout<span class="o">=</span>30 tofu.usptomonokai.jp:/home/ueda/TOFUBOX/ /home/ueda/TOFUBOX/<br />
<span class="c">#B. ローカルマシンからリモートへ同期</span><br />
ueda\@X201:~<span class="nv">$ </span>rsync -auz --timeout<span class="o">=</span>30 /home/ueda/TOFUBOX/ tofu.usptomonokai.jp:/home/ueda/TOFUBOX/<br />
</pre></div><br />
</td></tr></table></div><br />
<p>rsyncは（特に <tt class="docutils literal"><span class="pre">--delete</span></tt> オプションをつけると）<br />
失敗すると怖いコマンドの一つですが、<br />
基本的にcpやscpと同じで、左側に同期元、右側に同期先を書きます。<br />
ディレクトリの後ろにスラッシュを入れる癖をつけておけば、<br />
あとは直感的に動くはずです。</p><br />
<p>　今回使うオプション <tt class="docutils literal"><span class="pre">-auz</span> <span class="pre">--timeout=30</span></tt> には、次の意味があります。<br />
度々悲劇を起こす <tt class="docutils literal"><span class="pre">--delete</span></tt> も書いておきます。</p><br />
<table border="1" class="docutils"><br />
<colgroup><br />
<col width="30%" /><br />
<col width="70%" /><br />
</colgroup><br />
<thead valign="bottom"><br />
<tr class="row-odd"><th class="head">オプション</th><br />
<th class="head">意味</th><br />
</tr><br />
</thead><br />
<tbody valign="top"><br />
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">-a</span></tt></td><br />
<td>ファイルの属性をなるべく残す。</td><br />
</tr><br />
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">-u</span></tt></td><br />
<td>同期先に新しいファイルがあればそちらを残す。</td><br />
</tr><br />
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">-z</span></tt></td><br />
<td>データを圧縮して送受信</td><br />
</tr><br />
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">--timeout=30</span></tt></td><br />
<td>30秒通信が途絶えるとあきらめて終了</td><br />
</tr><br />
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">--delete</span></tt></td><br />
<td>送信元にないファイルやディレクトリを送信先で消去</td><br />
</tr><br />
</tbody><br />
</table><br />
<p>　ちなみに、rsyncは同期をとるマシンのどちらか一方で起動されると、<br />
もう一方のマシンでも起動されます。<br />
どっちのマシンでもrsyncが動いて、連携して同期を取ります。<br />
rsyncは、通信が途絶えてもしばらく立ち上がりっぱなしでリトライを繰り返します。<br />
今回はこの挙動は邪魔なのでクライアント側でtimeoutを指定しておきます。<br />
こうすると、通信が指定した秒数以上に途絶えた場合、<br />
クライアント側、サーバ側のrsync共にすぐ止まります。</p><br />
<p>　ちょっと u と delete の実験をしてみましょう。</p><br />
<p>・リスト3: rsyncの実験</p><br />
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#ローカルマシンにfile1を作る</span><br />
ueda\@X201:~/hoge<span class="nv">$ </span><span class="nb">echo</span> これはファイル１ &gt; file1<br />
<span class="c">#リモートマシンにfile2を作る</span><br />
ueda\@tofu:~/hoge<span class="nv">$ </span><span class="nb">echo</span> これはファイル2 &gt; file2<br />
<span class="c">#ローカルからリモートへコピー</span><br />
ueda\@X201:~/hoge<span class="nv">$ </span>rsync -auz ./ tofu.usptomonokai.jp:~/hoge/<br />
<span class="c">#リモートにローカルのファイルが転送される</span><br />
ueda\@tofu:~/hoge<span class="nv">$ </span>ls<br />
file1 file2<br />
<span class="c">#今度はdeleteオプション付きでもう一度ローカルからリモートへ</span><br />
ueda\@X201:~/hoge<span class="nv">$ </span>rsync -auz --delete ./ tofu.usptomonokai.jp:~/hoge/<br />
<span class="c">#ローカルにないfile2が消える</span><br />
ueda\@tofu:~/hoge<span class="nv">$ </span>ls<br />
file1<br />
<span class="c">#リモートでファイルを更新</span><br />
ueda\@tofu:~/hoge<span class="nv">$ </span><span class="nb">echo</span> リモートでfile1を作ったよ &gt; file1<br />
<span class="c">#ローカルからリモートへ同期</span><br />
ueda\@X201:~/hoge<span class="nv">$ </span>rsync -auz ./ tofu.usptomonokai.jp:~/hoge/<br />
<span class="c">#リモートのfile1の方が新しいので同期しない</span><br />
ueda\@tofu:~/hoge<span class="nv">$ </span>cat file1<br />
リモートでfile1を作ったよ<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　また、sshコマンドを使うとリモート側でコマンドが実行できます。<br />
例えば、リスト4のように書きます。</p><br />
<p>・リスト4: sshのタイムアウト設定</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 tofu.usptomonokai.jp <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これは、リモート側で <tt class="docutils literal"><span class="pre">mkdir</span> <span class="pre">$dir/.tofubox/LOCK</span></tt><br />
をやってくれとクライアント側から依頼を出すコマンドです。<br />
sshでもrsync同様、タイムアウトを設定します。<br />
ここでは5秒としました。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h3>10.3.2. 排他区間を作る<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　ここから本番コードを書いていきます。最初に、<br />
サーバと通信するクライアントが同時に一つになるように、<br />
排他制御を実現しましょう。<br />
rsyncはいくつ同時に行っても多少のことではおかしなことにはならないので、<br />
もしかしたら不要かもしれませんが、今回は排他処理を行います。<br />
次回11月号の内容で、排他制御が生きてきます。</p><br />
<p>　シェルスクリプトで排他を行うときには、<br />
「OS側が同時に二つ以上実行できないコマンドの終了ステータスを使う」<br />
という定石があります。<br />
例えば、 <tt class="docutils literal"><span class="pre">mkdir</span></tt> コマンドでディレクトリを作ることを考えてみましょう。<br />
あるディレクトリは、一つのマシンに一つしか存在しません。<br />
もし二つのプログラムが <tt class="docutils literal"><span class="pre">mkdir</span></tt> を使って同じディレクトリを作ろうとしても、<br />
うまくいくのはどちらか一方で、<br />
もう一方の <tt class="docutils literal"><span class="pre">mkdir</span></tt> は失敗してゼロでない終了ステータスを返します。<br />
<tt class="docutils literal"><span class="pre">mkdir</span></tt> が同時に二つ成功したら、同じディレクトリが二つできてしまいます。<br />
当然、OS側はそういうことは認めない作りになっています。</p><br />
<p>　リスト5のスクリプトで試してみましょう。</p><br />
<p>・リスト5: 排他の実験スクリプト</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~<span class="nv">$ </span>cat locktest.sh<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">exec </span>2&gt; /dev/null<br />
<br />
<span class="k">for </span>n in <span class="o">{</span>1..1000<span class="o">}</span> ; <span class="k">do</span><br />
<span class="k"> </span>mkdir ./LOCK <span class="o">&amp;&amp;</span> touch ./LOCK/<span class="nv">$n</span> &amp;<br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このスクリプトは、「 <tt class="docutils literal"><span class="pre">./LOCK</span></tt> ディレクトリを作ってうまくいったら<br />
<tt class="docutils literal"><span class="pre">./LOCK</span></tt> の中に番号を名前にしてファイルを作る」というプロセスを1000個、<br />
バックグラウンド処理で立ち上げるというものです。</p><br />
<p>　実行すると、 <tt class="docutils literal"><span class="pre">LOCK</span></tt> の下には必ず一つだけファイルがあり、<br />
たまに、一番最初に立ち上がるプロセスよりも後の <tt class="docutils literal"><span class="pre">mkdir</span></tt> が成功して、<br />
「1」以外のファイルができているはずです。<br />
リスト6に実行例を示します。</p><br />
<p>・リスト6: 排他の実験</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~<span class="nv">$ </span>./locktest.sh<br />
ueda\@SL510:~<span class="nv">$ </span>ls ./LOCK <span class="o">&amp;&amp;</span> rm -Rf ./LOCK<br />
1<br />
ueda\@SL510:~<span class="nv">$ </span>./locktest.sh<br />
ueda\@SL510:~<span class="nv">$ </span>ls ./LOCK <span class="o">&amp;&amp;</span> rm -Rf ./LOCK<br />
8<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　豆腐ボックスではリモートのサーバで、<br />
かつ複数のクライアントがいる状況でこのような排他区間を作らなくてはなりませんが、<br />
sshコマンドを使ってリモート側にディレクトリを作るようにすればよいということになります。<br />
ということで、豆腐ボックスのための排他区間を作り出すコードをリスト7のように書きます。</p><br />
<p>・リスト7: 排他区間の作り方</p><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SYNC<br />
<span class="c">#!/bin/bash -xv</span><br />
<span class="c"># TOFUBOX.SYNC</span><br />
<span class="nb">exec </span>2&gt; /tmp/<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span><br />
<br />
<span class="nv">server</span><span class="o">=</span>tofu.usptomonokai.jp<br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda<br />
<br />
<span class="c">#ロックを取る</span><br />
ssh <span class="nv">$server</span> <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span> <span class="o">||</span> <span class="nb">exit </span>0<br />
<br />
<span class="c">#!!!!排他区間!!!!</span><br />
<br />
<span class="c">#ロックを手放す</span><br />
ssh <span class="nv">$server</span> <span class="s2">&quot;rmdir $dir/.tofubox/LOCK&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>ちなみにsshコマンドは、ロックが取れなくても通信できなくても1を返します。</p><br />
<p>　このロックには一つ課題があります。<br />
通信をするのがすべて堅牢なサーバ機ならともかく、<br />
今回は個人用PCがクライアントにいますので、<br />
通信がブチッと切れて <tt class="docutils literal"><span class="pre">LOCK</span></tt><br />
ディレクトリが残ってしまう可能性があります。<br />
この課題については、後から対応します。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>10.3.3. 同期処理を実装<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では作った排他区間内に同期処理を実装しましょう。<br />
サーバからデータを引っ張って反映し、<br />
その後クライアントの変更をサーバに反映します。<br />
この一連の処理を排他区間内に書くと、リスト8のようになります。</p><br />
<p>　この例では、 <tt class="docutils literal"><span class="pre">notify-send</span></tt> というコマンドを使って、<br />
デスクトップ上にアラートを出すようにしています。<br />
この処理はディストリビューションに依存しますが、<br />
Ubuntu 12.04 の場合、 <tt class="docutils literal"><span class="pre">notify-send</span></tt> が実行されると、<br />
下の図のような箱が画面の右上に表示されます。<br />
<tt class="docutils literal"><span class="pre">DISPLAY=:0</span></tt> というのは、 <tt class="docutils literal"><span class="pre">notify-send</span></tt><br />
に、自分のデスクトップを教えるために書いています。</p><br />
<p>・リスト8: TOFUBOX.SYNC</p><br />
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
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -xv</span><br />
<span class="c"># TOFUBOX.SYNC</span><br />
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span><br />
<br />
<span class="nb">exec </span>2&gt; /tmp/<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span><br />
<br />
<span class="nv">server</span><span class="o">=</span>tofu.usptomonokai.jp<br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda<br />
<br />
MESSAGE <span class="o">()</span> <span class="o">{</span><br />
 <span class="nv">DISPLAY</span><span class="o">=</span>:0 notify-send <span class="s2">&quot;豆腐: $1&quot;</span><br />
<span class="o">}</span><br />
<br />
ERROR_CHECK<span class="o">(){</span><br />
 <span class="o">[</span> <span class="s2">&quot;$(echo ${PIPESTATUS[\@]} | tr -d &#39; 0&#39;)&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span><br />
<span class="k"> </span><span class="nv">DISPLAY</span><span class="o">=</span>:0 notify-send <span class="s2">&quot;豆腐: $1&quot;</span><br />
 <span class="nb">exit </span>1<br />
<span class="o">}</span><br />
<br />
<span class="c">#ロックがとれなかったらすぐ終了</span><br />
ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span> <span class="o">||</span> <span class="nb">exit </span>0<br />
<br />
<span class="c">#pull############################</span><br />
MESSAGE <span class="s2">&quot;受信開始&quot;</span><br />
rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$dir</span>/TOFUBOX/<br />
ERROR_CHECK <span class="s2">&quot;受信中断&quot;</span><br />
MESSAGE <span class="s2">&quot;受信完了&quot;</span><br />
<br />
<span class="c">#push############################</span><br />
MESSAGE <span class="s2">&quot;送信開始&quot;</span><br />
rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/<br />
ERROR_CHECK <span class="s2">&quot;送信中断&quot;</span><br />
MESSAGE <span class="s2">&quot;送信完了&quot;</span><br />
<br />
ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;rmdir $dir/.tofubox/LOCK&quot;</span><br />
<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="figure"><br />
<img alt="_images/notify.png" src="notify.png" /><br />
<p class="caption">図：notify-sendで表示されるダイアログ</p><br />
</div><br />
<p>　ロックは、通信が途絶えたりその他エラーが起こったりすると外れないのですが、<br />
このスクリプトではそれを前提としています。残ったロックは、サーバ側で外します。</p><br />
<p>　このスクリプトは排他区間でサスペンドがかかると、<br />
ssh や rsyncの途中であればゼロ以外の終了ステータスを返して終わります。<br />
しかし、<br />
他のコマンドを実行している間やコマンドとコマンドの間でサスペンドがかかると、<br />
そのままrsyncが走ってしまいます。<br />
残念ながらOSのサスペンドは trap コマンドで検知できないようですので、<br />
date コマンドを使って、リスト9のようなスクリプトを作ります。</p><br />
<p>・リスト9: TOFUBOX.SUSSTOP</p><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SUSSTOP<br />
<span class="c">#!/bin/bash</span><br />
<span class="c"># TOFUBOX.SUSSTOP</span><br />
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span><br />
<br />
<span class="nv">FROM</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span><br />
<br />
<span class="k">while </span>sleep 1 ; <span class="k">do</span><br />
<span class="k"> </span><span class="nv">TO</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span><br />
 <span class="nv">DIFF</span><span class="o">=</span><span class="k">$((</span> TO <span class="o">-</span> FROM <span class="k">))</span><br />
 <span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$DIFF&quot;</span> -gt 2 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>killall TOFUBOX.SYNC<br />
 <span class="nv">FROM</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span><br />
 <span class="k">fi</span><br />
<span class="k"> </span><span class="nv">FROM</span><span class="o">=</span><span class="nv">$TO</span><br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このスクリプト（ <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> ）は、<br />
1秒ごとにdateコマンドを呼んで、3秒以上間があいたら<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をコロすものです。<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> を実行しておけば、<br />
サスペンドすると数秒で <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> が止まります。<br />
数秒間なら rsync が走っても事故にはならないでしょう。</p><br />
<p>　実験してみましょう。リスト10が実験の例です。</p><br />
<p>・リスト10: サスペンドからの復帰時にTOFUBOX.SYNCを止める</p><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#あるターミナルで SUSSTOP を実行</span><br />
ueda\@SL510:~/.tofubox<span class="nv">$ </span>./TOFUBOX.SUSSTOP 2&gt; hoge<br />
<span class="c">#別のターミナルで SYNC を実行</span><br />
ueda\@SL510:~/TOFUBOX<span class="nv">$ </span>~/.tofubox/TOFUBOX.SYNC<br />
<span class="c">######################################</span><br />
<span class="c"># TOFUBOX.SYNCが終わる前にサスペンド -&gt; 復帰</span><br />
<span class="c">######################################</span><br />
<br />
<span class="c">#hogeファイルを見ると TOFUBOX.SYNC が止まっている。</span><br />
ueda\@SL510:~/.tofubox<span class="nv">$ </span>less hoge<br />
...<br />
+ <span class="nv">TO</span><span class="o">=</span>1342317384<br />
+ <span class="nv">DIFF</span><span class="o">=</span>10<br />
+ <span class="s1">&#39;[&#39;</span> 10 -gt 2 <span class="s1">&#39;]&#39;</span><br />
+ killall TOFUBOX.SYNC<br />
date +%s<span class="o">)</span><br />
date +%s<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>10.3.4. サーバ側でロックをはずす処理<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　ロックを強制的に外すという処理は、<br />
排他制御に完備性があればやってはいけません。<br />
しかし、今回はそうも言ってられないので実装します。<br />
ロックを外した瞬間に何が起こるかということを考え、<br />
慎重に実装しなければなりません。</p><br />
<p>　ここで効いてくるのは rsync と ssh のタイムアウトです。<br />
もし、サーバ側でロックができてからrsyncが始まらなかったり、<br />
rsyncが終わってからしばらくロックが外れなかったりした場合は、<br />
クライアント側では rsync も ssh も終わって通信していない状態になっています。</p><br />
<p>　sshでは5秒、rsyncでは30秒でタイムアウトするので、<br />
サーバ側では、LOCKがあるのに60秒以上rsyncが走っていないときには、<br />
クライアント側はすでにスクリプトが終わっているか、<br />
サスペンドしていて後でkillされると判断できます。<br />
厳密にはクライアント側でsshとrsync以外の処理で25秒くらい<br />
かかってしまうとこの判断は間違いになってしまいますが、<br />
このようなことはよほどPCが不安定にならない限り起こりません。<br />
万が一そうなってしまったら降参ということにしましょう。</p><br />
<p>　リスト11のシェルスクリプトをサーバ側で実行します。</p><br />
<p>・リスト11: TOFUBOX.RMLOCK</p><br />
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
21</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@tofu:~<span class="nv">$ </span>cat .tofubox/TOFUBOX.RMLOCK<br />
<span class="c">#!/bin/bash</span><br />
<span class="c"># TOFUBOX.RMLOCK</span><br />
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span><br />
<br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda/.tofubox<br />
<br />
<span class="nb">exec </span>2&gt; <span class="nv">$dir</span>/LOG<br />
<br />
<span class="nv">n</span><span class="o">=</span>0<br />
<span class="k">while </span>sleep 3 ; <span class="k">do</span><br />
<span class="k"> </span><span class="nv">n</span><span class="o">=</span><span class="k">$((</span> <span class="nv">$n</span> <span class="o">+</span> <span class="m">1</span> <span class="k">))</span><br />
<br />
 ls -d <span class="nv">$dir</span>/LOCK &amp;&gt; /dev/null <span class="o">||</span> <span class="nv">n</span><span class="o">=</span>0<br />
 ps cax | grep -q rsync <span class="o">&amp;&amp;</span> <span class="nv">n</span><span class="o">=</span>0<br />
<br />
 <span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$n&quot;</span> -eq 20 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>rmdir <span class="nv">$dir</span>/LOCK<br />
 <span class="nv">n</span><span class="o">=</span>0<br />
 <span class="k">fi</span><br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このスクリプトは、とりあえずリスト12のようにバックグラウンドで走らせておきましょう。<br />
（脚注：余談ですが、この終わらないスクリプトを間違えてcronにしかけたら、<br />
ロードアベレージが500を越えました。）</p><br />
<p>・リスト12: TOFUBOX.RMLOCKの実行</p><br />
<div class="highlight-bash"><div class="highlight"><pre>ueda\@tofu:~<span class="nv">$ </span>~/.tofubox/TOFUBOX.RMLOCK &amp;<br />
</pre></div><br />
</div><br />
<p>　 <tt class="docutils literal"><span class="pre">ps</span> <span class="pre">cax</span></tt> のオプションcは、実行中のプロセスをコマンドで表示するときに使います。<br />
よくpsしたらgrepのプロセスも引っかかるということがありますが、<br />
それを避けることができます。リスト13のようにgrepと組み合わせると便利です。</p><br />
<p>・リスト13: TOFUBOX.RMLOCKの実行</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~/.tofubox<span class="nv">$ </span>ps cax | grep <span class="s2">&quot;vi$&quot;</span><br />
 6032 pts/0 S+ 0:00 vi<br />
 6273 pts/2 S+ 0:00 vi<br />
<span class="c">#viのプロセスがあると、grepが0を返し、$?に入る。</span><br />
ueda\@SL510:~<span class="nv">$ </span>ps cax | grep -q vi<span class="nv">$ </span>; <span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
<span class="c">#ないプロセスをgrepすると、grepが1を返す。</span><br />
ueda\@SL510:~<span class="nv">$ </span>ps cax | grep -q hoge<span class="nv">$ </span>; <span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト12の13行目は、grepの終了ステータスを見て、<br />
0ならnを0にしています。</p><br />
</div><br />
<div class="section" id="id8"><br />
<h3>10.3.5. 実行<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> をバックグラウンド実行、<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をcrontabを使って定期的に起動させることにします。<br />
次回、もう少し気の利いたタイミングで <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を起動させることを試みます。</p><br />
<p>・リスト14: crontabへの記述</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@SL510:~<span class="nv">$ </span>~/.tofubox/TOFUBOX.SUSSTOP &amp;<br />
ueda\@SL510:~<span class="nv">$ </span>crontab -e<br />
<span class="c">#これを加筆</span><br />
*/3 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC<br />
ueda\@X201:~<span class="nv">$ </span>crontab -e<br />
<span class="c">#もう一方のマシンではこれを加筆</span><br />
*/4 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">*/3</span></tt> というのは、3分おきという意味です。<br />
これで、SL510側では3分おき、X201側では4分おきに同期処理が起動します。<br />
3分と4分でずらしたのは、両方3分にすると必ずロックの取り合いになるからです。<br />
これでも12分に一回、ロックの取り合いになりますが、<br />
ロックのテストにはちょうどよいでしょう。<br />
また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> は、マシンを再起動したら再度立ち上げなければなりません。<br />
このあたりの改善は次号で扱います。</p><br />
<p>　実行した結果は特に載せませんが、<br />
こっちのノートPCで作ったメモが、あっちのノートPCにひょっこり現れるという具合で、<br />
なかなか便利です。<br />
・・・まあ、Dropboxも使ってるんで、どっちを使おうかというところですが。</p><br />
</div><br />
</div><br />
<div class="section" id="id9"><br />
<h2>10.4. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、オンラインストレージもどきを作ってみました。<br />
サスペンドや通信エラーがからむのでややこしくなりました。<br />
もしかしたらもう少し洗練した書き方もできたかもしれませんが、<br />
それでも今回書いたスクリプトの行数：</p><br />
<ul class="simple"><br />
<li>TOFUBOX.SYNC: 37行</li><br />
<li>TOFUBOX.SUSSTOP: 15行</li><br />
<li>TOFUBOX.RMLOCK: 20行</li><br />
</ul><br />
<p>は、驚異的に短いと言えます。</p><br />
<p>　ただ、今回作ったものは、</p><br />
<ul class="simple"><br />
<li>3分あるいは4分ごとに意味なくrsyncが起動（ <tt class="docutils literal"><span class="pre">notify-send</span></tt> がうるさい。）</li><br />
<li>大きいファイルをTOFUBOXディレクトリにコピーしている間にrsyncが走ると中途半端なアップロードが発生</li><br />
<li>マシンを起動したときに手動で起動</li><br />
</ul><br />
<p>など、いろいろ細かい不便さがあるので、<br />
次回はもう少し凝ってみたいと考えています。</p><br />
</div><br />
</div>
