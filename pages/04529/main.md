---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年10月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>10. 開眼シェルスクリプト 第10回 オンラインストレージもどきを作る（１）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>10.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回、前々回は並列処理のテクニックを扱いましたが、
今回からは具体的なアプリケーションの作成に戻り、
VPS経由で、複数のマシンのデータを自動で同期する仕組みを作ります。
要はDropboxのようなものですが、さすがにあの完成度で作り切るのは大変ですので、
簡易的なものをシェルスクリプトで作ってみましょう。</p>
<p>　作るのは数台のローカルPCの所定のディレクトリを、
リモートのサーバ経由で同期をとるというアプリケーションです。</p>
<p>　名前は、Dropboxのアイコンを眺めていたら豆腐のように見えたので、
豆腐ボックスとします。敢えてふにゃふにゃな名前にしましたが、
だからといってかっこいい名前は思いついていません。</p>
<p>　豆腐ボックスは、ファイルを消さずにとにかく集積していくように作ります。
削除がからむと途端にコードが面倒になるので、少なくとも今回は扱いません。
その代わり、今回もソースは全部掲載できるほど短くなっています。</p>
<p>「政事は豆腐の箱のごとし、箱ゆがめば豆腐ゆがむなり。」 &#8212;- 二宮尊徳</p>
</div>
<div class="section" id="id3">
<h2>10.2. 環境<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、筆者の手持ちのマシンを総動員します。
クライアントPCには、次の二台を準備しました。</p>
<ul class="simple">
<li>Ubuntu 12.04 x64 on ThinkPad SL510</li>
<li>Ubuntu 12.04 x64 on ThinkPad X201</li>
</ul>
<p>私の自宅のThinkPadと仕事用のThinkPadです。
この連載にも何回か登場していますが、
現在は64ビット版のUbuntuが搭載されています。</p>
<p>　今回はPCのサスペンド機能やデスクトップへの通知機能など、
きわどい機能が登場しますので、一応、Ubuntu Linux上での動作を前提としておきます。
しかし、UNIX系OSならちょっと修正すれば動くはずです。</p>
<p>　今回はサーバ側もUbuntuですが、こちらはsshとrsyncが動けば何でもいいでしょう。</p>
<ul class="simple">
<li>Ubuntu 12.04 x64 on さくらのVPS （ホスト名：tofu.usptomonokai.jp）</li>
</ul>
<p>　サーバとクライアント間は、鍵認証でssh接続できることとします。
rsyncのポート指定をいちいち書いていると面倒なので、
tofu.usptomonokai.jpのsshのポート番号は22番とします。</p>
</div>
<div class="section" id="id4">
<h2>10.3. 作業開始<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、作っていきましょう。まず、クライアントマシンとサーバに、
リスト1のようにディレクトリを作ります。
クライアント側は、一台でプログラミングして他のマシンにscpすればよいでしょう。</p>
<p>・リスト1: ディレクトリ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>/hoge/ueda
├── .tofubox
└── TOFUBOX
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> は同期するディレクトリで、
<tt class="docutils literal"><span class="pre">~/.tofubox/</span></tt> はプログラム等のファイル置き場です。</p>
<div class="section" id="rsyncmkdir">
<h3>10.3.1. 豆腐ボックスのコアテクノロジー（単なるrsyncとmkdir）<a class="headerlink" href="#rsyncmkdir" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　rsyncは、各クライアントから起動します。
豆腐ボックスでは、リスト2のコマンドと共に使います。</p>
<p>・リスト2: rsyncコマンドの使い方</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#A. リモートからローカルマシンへ同期</span>
ueda@X201:~<span class="nv">$ </span>rsync -auz --timeout<span class="o">=</span>30 tofu.usptomonokai.jp:/home/ueda/TOFUBOX/ /home/ueda/TOFUBOX/
<span class="c">#B. ローカルマシンからリモートへ同期</span>
ueda@X201:~<span class="nv">$ </span>rsync -auz --timeout<span class="o">=</span>30 /home/ueda/TOFUBOX/ tofu.usptomonokai.jp:/home/ueda/TOFUBOX/
</pre></div>
</td></tr></table></div>
<p>rsyncは（特に <tt class="docutils literal"><span class="pre">--delete</span></tt> オプションをつけると）
失敗すると怖いコマンドの一つですが、
基本的にcpやscpと同じで、左側に同期元、右側に同期先を書きます。
ディレクトリの後ろにスラッシュを入れる癖をつけておけば、
あとは直感的に動くはずです。</p>
<p>　今回使うオプション <tt class="docutils literal"><span class="pre">-auz</span> <span class="pre">--timeout=30</span></tt> には、次の意味があります。
度々悲劇を起こす <tt class="docutils literal"><span class="pre">--delete</span></tt> も書いておきます。</p>
<table border="1" class="docutils">
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">オプション</th>
<th class="head">意味</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">-a</span></tt></td>
<td>ファイルの属性をなるべく残す。</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">-u</span></tt></td>
<td>同期先に新しいファイルがあればそちらを残す。</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">-z</span></tt></td>
<td>データを圧縮して送受信</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">--timeout=30</span></tt></td>
<td>30秒通信が途絶えるとあきらめて終了</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">--delete</span></tt></td>
<td>送信元にないファイルやディレクトリを送信先で消去</td>
</tr>
</tbody>
</table>
<p>　ちなみに、rsyncは同期をとるマシンのどちらか一方で起動されると、
もう一方のマシンでも起動されます。
どっちのマシンでもrsyncが動いて、連携して同期を取ります。
rsyncは、通信が途絶えてもしばらく立ち上がりっぱなしでリトライを繰り返します。
今回はこの挙動は邪魔なのでクライアント側でtimeoutを指定しておきます。
こうすると、通信が指定した秒数以上に途絶えた場合、
クライアント側、サーバ側のrsync共にすぐ止まります。</p>
<p>　ちょっと u と delete の実験をしてみましょう。</p>
<p>・リスト3: rsyncの実験</p>
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#ローカルマシンにfile1を作る</span>
ueda@X201:~/hoge<span class="nv">$ </span><span class="nb">echo</span> これはファイル１ &gt; file1
<span class="c">#リモートマシンにfile2を作る</span>
ueda@tofu:~/hoge<span class="nv">$ </span><span class="nb">echo</span> これはファイル2 &gt; file2
<span class="c">#ローカルからリモートへコピー</span>
ueda@X201:~/hoge<span class="nv">$ </span>rsync -auz ./ tofu.usptomonokai.jp:~/hoge/
<span class="c">#リモートにローカルのファイルが転送される</span>
ueda@tofu:~/hoge<span class="nv">$ </span>ls
file1 file2
<span class="c">#今度はdeleteオプション付きでもう一度ローカルからリモートへ</span>
ueda@X201:~/hoge<span class="nv">$ </span>rsync -auz --delete ./ tofu.usptomonokai.jp:~/hoge/
<span class="c">#ローカルにないfile2が消える</span>
ueda@tofu:~/hoge<span class="nv">$ </span>ls
file1
<span class="c">#リモートでファイルを更新</span>
ueda@tofu:~/hoge<span class="nv">$ </span><span class="nb">echo</span> リモートでfile1を作ったよ &gt; file1
<span class="c">#ローカルからリモートへ同期</span>
ueda@X201:~/hoge<span class="nv">$ </span>rsync -auz ./ tofu.usptomonokai.jp:~/hoge/
<span class="c">#リモートのfile1の方が新しいので同期しない</span>
ueda@tofu:~/hoge<span class="nv">$ </span>cat file1
リモートでfile1を作ったよ
</pre></div>
</td></tr></table></div>
<p>　また、sshコマンドを使うとリモート側でコマンドが実行できます。
例えば、リスト4のように書きます。</p>
<p>・リスト4: sshのタイムアウト設定</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 tofu.usptomonokai.jp <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span>
</pre></div>
</td></tr></table></div>
<p>これは、リモート側で <tt class="docutils literal"><span class="pre">mkdir</span> <span class="pre">$dir/.tofubox/LOCK</span></tt>
をやってくれとクライアント側から依頼を出すコマンドです。
sshでもrsync同様、タイムアウトを設定します。
ここでは5秒としました。</p>
</div>
<div class="section" id="id5">
<h3>10.3.2. 排他区間を作る<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　ここから本番コードを書いていきます。最初に、
サーバと通信するクライアントが同時に一つになるように、
排他制御を実現しましょう。
rsyncはいくつ同時に行っても多少のことではおかしなことにはならないので、
もしかしたら不要かもしれませんが、今回は排他処理を行います。
次回11月号の内容で、排他制御が生きてきます。</p>
<p>　シェルスクリプトで排他を行うときには、
「OS側が同時に二つ以上実行できないコマンドの終了ステータスを使う」
という定石があります。
例えば、 <tt class="docutils literal"><span class="pre">mkdir</span></tt> コマンドでディレクトリを作ることを考えてみましょう。
あるディレクトリは、一つのマシンに一つしか存在しません。
もし二つのプログラムが <tt class="docutils literal"><span class="pre">mkdir</span></tt> を使って同じディレクトリを作ろうとしても、
うまくいくのはどちらか一方で、
もう一方の <tt class="docutils literal"><span class="pre">mkdir</span></tt> は失敗してゼロでない終了ステータスを返します。
<tt class="docutils literal"><span class="pre">mkdir</span></tt> が同時に二つ成功したら、同じディレクトリが二つできてしまいます。
当然、OS側はそういうことは認めない作りになっています。</p>
<p>　リスト5のスクリプトで試してみましょう。</p>
<p>・リスト5: 排他の実験スクリプト</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~<span class="nv">$ </span>cat locktest.sh
<span class="c">#!/bin/bash</span>

<span class="nb">exec </span>2&gt; /dev/null

<span class="k">for </span>n in <span class="o">{</span>1..1000<span class="o">}</span> ; <span class="k">do</span>
<span class="k"> </span>mkdir ./LOCK <span class="o">&amp;&amp;</span> touch ./LOCK/<span class="nv">$n</span> &amp;
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　このスクリプトは、「 <tt class="docutils literal"><span class="pre">./LOCK</span></tt> ディレクトリを作ってうまくいったら
<tt class="docutils literal"><span class="pre">./LOCK</span></tt> の中に番号を名前にしてファイルを作る」というプロセスを1000個、
バックグラウンド処理で立ち上げるというものです。</p>
<p>　実行すると、 <tt class="docutils literal"><span class="pre">LOCK</span></tt> の下には必ず一つだけファイルがあり、
たまに、一番最初に立ち上がるプロセスよりも後の <tt class="docutils literal"><span class="pre">mkdir</span></tt> が成功して、
「1」以外のファイルができているはずです。
リスト6に実行例を示します。</p>
<p>・リスト6: 排他の実験</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~<span class="nv">$ </span>./locktest.sh
ueda@SL510:~<span class="nv">$ </span>ls ./LOCK <span class="o">&amp;&amp;</span> rm -Rf ./LOCK
1
ueda@SL510:~<span class="nv">$ </span>./locktest.sh
ueda@SL510:~<span class="nv">$ </span>ls ./LOCK <span class="o">&amp;&amp;</span> rm -Rf ./LOCK
8
</pre></div>
</td></tr></table></div>
<p>　豆腐ボックスではリモートのサーバで、
かつ複数のクライアントがいる状況でこのような排他区間を作らなくてはなりませんが、
sshコマンドを使ってリモート側にディレクトリを作るようにすればよいということになります。
ということで、豆腐ボックスのための排他区間を作り出すコードをリスト7のように書きます。</p>
<p>・リスト7: 排他区間の作り方</p>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SYNC
<span class="c">#!/bin/bash -xv</span>
<span class="c"># TOFUBOX.SYNC</span>
<span class="nb">exec </span>2&gt; /tmp/<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>

<span class="nv">server</span><span class="o">=</span>tofu.usptomonokai.jp
<span class="nv">dir</span><span class="o">=</span>/home/ueda

<span class="c">#ロックを取る</span>
ssh <span class="nv">$server</span> <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span> <span class="o">||</span> <span class="nb">exit </span>0

<span class="c">#!!!!排他区間!!!!</span>

<span class="c">#ロックを手放す</span>
ssh <span class="nv">$server</span> <span class="s2">&quot;rmdir $dir/.tofubox/LOCK&quot;</span>
</pre></div>
</td></tr></table></div>
<p>ちなみにsshコマンドは、ロックが取れなくても通信できなくても1を返します。</p>
<p>　このロックには一つ課題があります。
通信をするのがすべて堅牢なサーバ機ならともかく、
今回は個人用PCがクライアントにいますので、
通信がブチッと切れて <tt class="docutils literal"><span class="pre">LOCK</span></tt>
ディレクトリが残ってしまう可能性があります。
この課題については、後から対応します。</p>
</div>
<div class="section" id="id6">
<h3>10.3.3. 同期処理を実装<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では作った排他区間内に同期処理を実装しましょう。
サーバからデータを引っ張って反映し、
その後クライアントの変更をサーバに反映します。
この一連の処理を排他区間内に書くと、リスト8のようになります。</p>
<p>　この例では、 <tt class="docutils literal"><span class="pre">notify-send</span></tt> というコマンドを使って、
デスクトップ上にアラートを出すようにしています。
この処理はディストリビューションに依存しますが、
Ubuntu 12.04 の場合、 <tt class="docutils literal"><span class="pre">notify-send</span></tt> が実行されると、
下の図のような箱が画面の右上に表示されます。
<tt class="docutils literal"><span class="pre">DISPLAY=:0</span></tt> というのは、 <tt class="docutils literal"><span class="pre">notify-send</span></tt>
に、自分のデスクトップを教えるために書いています。</p>
<p>・リスト8: TOFUBOX.SYNC</p>
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
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -xv</span>
<span class="c"># TOFUBOX.SYNC</span>
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span>

<span class="nb">exec </span>2&gt; /tmp/<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>

<span class="nv">server</span><span class="o">=</span>tofu.usptomonokai.jp
<span class="nv">dir</span><span class="o">=</span>/home/ueda

MESSAGE <span class="o">()</span> <span class="o">{</span>
 <span class="nv">DISPLAY</span><span class="o">=</span>:0 notify-send <span class="s2">&quot;豆腐: $1&quot;</span>
<span class="o">}</span>

ERROR_CHECK<span class="o">(){</span>
 <span class="o">[</span> <span class="s2">&quot;$(echo ${PIPESTATUS[@]} | tr -d &#39; 0&#39;)&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span>
<span class="k"> </span><span class="nv">DISPLAY</span><span class="o">=</span>:0 notify-send <span class="s2">&quot;豆腐: $1&quot;</span>
 <span class="nb">exit </span>1
<span class="o">}</span>

<span class="c">#ロックがとれなかったらすぐ終了</span>
ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;mkdir $dir/.tofubox/LOCK&quot;</span> <span class="o">||</span> <span class="nb">exit </span>0

<span class="c">#pull############################</span>
MESSAGE <span class="s2">&quot;受信開始&quot;</span>
rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$dir</span>/TOFUBOX/
ERROR_CHECK <span class="s2">&quot;受信中断&quot;</span>
MESSAGE <span class="s2">&quot;受信完了&quot;</span>

<span class="c">#push############################</span>
MESSAGE <span class="s2">&quot;送信開始&quot;</span>
rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/
ERROR_CHECK <span class="s2">&quot;送信中断&quot;</span>
MESSAGE <span class="s2">&quot;送信完了&quot;</span>

ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;rmdir $dir/.tofubox/LOCK&quot;</span>

<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<div class="figure">
<img alt="_images/notify.png" src="notify.png" />
<p class="caption">図：notify-sendで表示されるダイアログ</p>
</div>
<p>　ロックは、通信が途絶えたりその他エラーが起こったりすると外れないのですが、
このスクリプトではそれを前提としています。残ったロックは、サーバ側で外します。</p>
<p>　このスクリプトは排他区間でサスペンドがかかると、
ssh や rsyncの途中であればゼロ以外の終了ステータスを返して終わります。
しかし、
他のコマンドを実行している間やコマンドとコマンドの間でサスペンドがかかると、
そのままrsyncが走ってしまいます。
残念ながらOSのサスペンドは trap コマンドで検知できないようですので、
date コマンドを使って、リスト9のようなスクリプトを作ります。</p>
<p>・リスト9: TOFUBOX.SUSSTOP</p>
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
16</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SUSSTOP
<span class="c">#!/bin/bash</span>
<span class="c"># TOFUBOX.SUSSTOP</span>
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span>

<span class="nv">FROM</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span>

<span class="k">while </span>sleep 1 ; <span class="k">do</span>
<span class="k"> </span><span class="nv">TO</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span>
 <span class="nv">DIFF</span><span class="o">=</span><span class="k">$((</span> TO <span class="o">-</span> FROM <span class="k">))</span>
 <span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$DIFF&quot;</span> -gt 2 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>killall TOFUBOX.SYNC
 <span class="nv">FROM</span><span class="o">=</span><span class="k">$(</span>date +%s<span class="k">)</span>
 <span class="k">fi</span>
<span class="k"> </span><span class="nv">FROM</span><span class="o">=</span><span class="nv">$TO</span>
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　このスクリプト（ <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> ）は、
1秒ごとにdateコマンドを呼んで、3秒以上間があいたら
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をコロすものです。
<tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> を実行しておけば、
サスペンドすると数秒で <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> が止まります。
数秒間なら rsync が走っても事故にはならないでしょう。</p>
<p>　実験してみましょう。リスト10が実験の例です。</p>
<p>・リスト10: サスペンドからの復帰時にTOFUBOX.SYNCを止める</p>
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#あるターミナルで SUSSTOP を実行</span>
ueda@SL510:~/.tofubox<span class="nv">$ </span>./TOFUBOX.SUSSTOP 2&gt; hoge
<span class="c">#別のターミナルで SYNC を実行</span>
ueda@SL510:~/TOFUBOX<span class="nv">$ </span>~/.tofubox/TOFUBOX.SYNC
<span class="c">######################################</span>
<span class="c"># TOFUBOX.SYNCが終わる前にサスペンド -&gt; 復帰</span>
<span class="c">######################################</span>

<span class="c">#hogeファイルを見ると TOFUBOX.SYNC が止まっている。</span>
ueda@SL510:~/.tofubox<span class="nv">$ </span>less hoge
...
+ <span class="nv">TO</span><span class="o">=</span>1342317384
+ <span class="nv">DIFF</span><span class="o">=</span>10
+ <span class="s1">&#39;[&#39;</span> 10 -gt 2 <span class="s1">&#39;]&#39;</span>
+ killall TOFUBOX.SYNC
date +%s<span class="o">)</span>
date +%s
...
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h3>10.3.4. サーバ側でロックをはずす処理<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　ロックを強制的に外すという処理は、
排他制御に完備性があればやってはいけません。
しかし、今回はそうも言ってられないので実装します。
ロックを外した瞬間に何が起こるかということを考え、
慎重に実装しなければなりません。</p>
<p>　ここで効いてくるのは rsync と ssh のタイムアウトです。
もし、サーバ側でロックができてからrsyncが始まらなかったり、
rsyncが終わってからしばらくロックが外れなかったりした場合は、
クライアント側では rsync も ssh も終わって通信していない状態になっています。</p>
<p>　sshでは5秒、rsyncでは30秒でタイムアウトするので、
サーバ側では、LOCKがあるのに60秒以上rsyncが走っていないときには、
クライアント側はすでにスクリプトが終わっているか、
サスペンドしていて後でkillされると判断できます。
厳密にはクライアント側でsshとrsync以外の処理で25秒くらい
かかってしまうとこの判断は間違いになってしまいますが、
このようなことはよほどPCが不安定にならない限り起こりません。
万が一そうなってしまったら降参ということにしましょう。</p>
<p>　リスト11のシェルスクリプトをサーバ側で実行します。</p>
<p>・リスト11: TOFUBOX.RMLOCK</p>
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
21</pre></div></td><td class="code"><div class="highlight"><pre>ueda@tofu:~<span class="nv">$ </span>cat .tofubox/TOFUBOX.RMLOCK
<span class="c">#!/bin/bash</span>
<span class="c"># TOFUBOX.RMLOCK</span>
<span class="c"># written by R. Ueda (USP研究所) Jul. 21, 2012</span>

<span class="nv">dir</span><span class="o">=</span>/home/ueda/.tofubox

<span class="nb">exec </span>2&gt; <span class="nv">$dir</span>/LOG

<span class="nv">n</span><span class="o">=</span>0
<span class="k">while </span>sleep 3 ; <span class="k">do</span>
<span class="k"> </span><span class="nv">n</span><span class="o">=</span><span class="k">$((</span> <span class="nv">$n</span> <span class="o">+</span> <span class="m">1</span> <span class="k">))</span>

 ls -d <span class="nv">$dir</span>/LOCK &amp;&gt; /dev/null <span class="o">||</span> <span class="nv">n</span><span class="o">=</span>0
 ps cax | grep -q rsync <span class="o">&amp;&amp;</span> <span class="nv">n</span><span class="o">=</span>0

 <span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$n&quot;</span> -eq 20 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>rmdir <span class="nv">$dir</span>/LOCK
 <span class="nv">n</span><span class="o">=</span>0
 <span class="k">fi</span>
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　このスクリプトは、とりあえずリスト12のようにバックグラウンドで走らせておきましょう。
（脚注：余談ですが、この終わらないスクリプトを間違えてcronにしかけたら、
ロードアベレージが500を越えました。）</p>
<p>・リスト12: TOFUBOX.RMLOCKの実行</p>
<div class="highlight-bash"><div class="highlight"><pre>ueda@tofu:~<span class="nv">$ </span>~/.tofubox/TOFUBOX.RMLOCK &amp;
</pre></div>
</div>
<p>　 <tt class="docutils literal"><span class="pre">ps</span> <span class="pre">cax</span></tt> のオプションcは、実行中のプロセスをコマンドで表示するときに使います。
よくpsしたらgrepのプロセスも引っかかるということがありますが、
それを避けることができます。リスト13のようにgrepと組み合わせると便利です。</p>
<p>・リスト13: TOFUBOX.RMLOCKの実行</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~/.tofubox<span class="nv">$ </span>ps cax | grep <span class="s2">&quot;vi$&quot;</span>
 6032 pts/0 S+ 0:00 vi
 6273 pts/2 S+ 0:00 vi
<span class="c">#viのプロセスがあると、grepが0を返し、$?に入る。</span>
ueda@SL510:~<span class="nv">$ </span>ps cax | grep -q vi<span class="nv">$ </span>; <span class="nb">echo</span> <span class="nv">$?</span>
0
<span class="c">#ないプロセスをgrepすると、grepが1を返す。</span>
ueda@SL510:~<span class="nv">$ </span>ps cax | grep -q hoge<span class="nv">$ </span>; <span class="nb">echo</span> <span class="nv">$?</span>
1
</pre></div>
</td></tr></table></div>
<p>リスト12の13行目は、grepの終了ステータスを見て、
0ならnを0にしています。</p>
</div>
<div class="section" id="id8">
<h3>10.3.5. 実行<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> をバックグラウンド実行、
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をcrontabを使って定期的に起動させることにします。
次回、もう少し気の利いたタイミングで <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を起動させることを試みます。</p>
<p>・リスト14: crontabへの記述</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda@SL510:~<span class="nv">$ </span>~/.tofubox/TOFUBOX.SUSSTOP &amp;
ueda@SL510:~<span class="nv">$ </span>crontab -e
<span class="c">#これを加筆</span>
*/3 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC
ueda@X201:~<span class="nv">$ </span>crontab -e
<span class="c">#もう一方のマシンではこれを加筆</span>
*/4 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">*/3</span></tt> というのは、3分おきという意味です。
これで、SL510側では3分おき、X201側では4分おきに同期処理が起動します。
3分と4分でずらしたのは、両方3分にすると必ずロックの取り合いになるからです。
これでも12分に一回、ロックの取り合いになりますが、
ロックのテストにはちょうどよいでしょう。
また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> は、マシンを再起動したら再度立ち上げなければなりません。
このあたりの改善は次号で扱います。</p>
<p>　実行した結果は特に載せませんが、
こっちのノートPCで作ったメモが、あっちのノートPCにひょっこり現れるという具合で、
なかなか便利です。
・・・まあ、Dropboxも使ってるんで、どっちを使おうかというところですが。</p>
</div>
</div>
<div class="section" id="id9">
<h2>10.4. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、オンラインストレージもどきを作ってみました。
サスペンドや通信エラーがからむのでややこしくなりました。
もしかしたらもう少し洗練した書き方もできたかもしれませんが、
それでも今回書いたスクリプトの行数：</p>
<ul class="simple">
<li>TOFUBOX.SYNC: 37行</li>
<li>TOFUBOX.SUSSTOP: 15行</li>
<li>TOFUBOX.RMLOCK: 20行</li>
</ul>
<p>は、驚異的に短いと言えます。</p>
<p>　ただ、今回作ったものは、</p>
<ul class="simple">
<li>3分あるいは4分ごとに意味なくrsyncが起動（ <tt class="docutils literal"><span class="pre">notify-send</span></tt> がうるさい。）</li>
<li>大きいファイルをTOFUBOXディレクトリにコピーしている間にrsyncが走ると中途半端なアップロードが発生</li>
<li>マシンを起動したときに手動で起動</li>
</ul>
<p>など、いろいろ細かい不便さがあるので、
次回はもう少し凝ってみたいと考えています。</p>
</div>
</div>
