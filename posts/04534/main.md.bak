# 開眼シェルスクリプト2012年11月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>11. 開眼シェルスクリプト 第11回 オンラインストレージもどきを作る（２）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>11.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は豆腐ボックス第二回です。<br />
前回はrsyncを使ったオンラインストレージ<br />
（たまっていく一方なのでモドキ）を作りました。<br />
今回はこれを少しずつ改善していきます。<br />
普段あまり使わない機能のオンパレードなので、<br />
筆者も詳しくはないのですが、<br />
一緒に一つずつ確認していきましょう。</p><br />
<p>　今回は、前回にも増して力技の嵐です。<br />
また、私は変数にクォートをつけるどうのこうのには無頓着なので、<br />
（脚注：必要な局面では頓着します。）<br />
人によっては「こんなコーディングおかしい」と思うかもしれません。<br />
しかし、秀吉の「墨俣一夜城」の例はちょっと言い過ぎかもしれませんが、<br />
人の想像を超えた早さで何かを作れるということには、<br />
組織や自身の行く末を変えるくらいの力があります。</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>11.2. おさらい<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　豆腐ボックスは、サーバを経由して複数のクライアントPCのファイルを<br />
同期するアプリケーションです。<br />
各PCの <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 内のディレクトリをrsyncで同期します。<br />
クライアントPCは多数台の接続を想定しており、<br />
一つの同時に二台以上のクライアントとサーバが同期処理しないように、<br />
排他制御の仕組みが入っています。</p><br />
<p>　排他制御は、クライアント側からサーバ側にディレクトリを作りにいき、<br />
その成否を利用して行っています。<br />
<tt class="docutils literal"><span class="pre">mkdir</span></tt> を排他区間の作成に使うという手法です（前回参照）。</p><br />
<p>　クライアント側は以下の二つのスクリプトで構成されています。<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> が同期を行うスクリプトです。<br />
また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> は、PCがスリープから復帰したら、<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を殺すスクリプトです。<br />
排他制御のために必要なスクリプトです。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>tree .tofubox/<br />
.tofubox/<br />
├── TOFUBOX.SUSSTOP<br />
└── TOFUBOX.SYNC<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　サーバ側には、以下のようにシェルスクリプトが一つだけあります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@tofu:~<span class="nv">$ </span>tree .tofubox/<br />
.tofubox/<br />
└── REMOVE.LOCK<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">REMOVE.LOCK</span></tt> は、<br />
クライアント側がロックをかけた後に通信を中断したかどうかを判断し、<br />
適切な時にロックを外します。</p><br />
<p>　豆腐ボックスのコードの総量は、クライアント側、<br />
サーバ側のものを全部足してもわずか73行です。<br />
せっかくコードが短いんですから、一番長い<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をリスト1に全部掲載しておきます。<br />
このコードには、後から手を入れます。</p><br />
<p>・リスト1: TOFUBOX.SYNC（前回のもの）</p><br />
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
37<br />
38<br />
39</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SYNC<br />
<span class="c">#!/bin/bash -xv</span><br />
<span class="c">#</span><br />
<span class="c"># TOFUBOX.SYNC</span><br />
<span class="c">#</span><br />
<span class="c"># written by R. Ueda (usp-lab.com)</span><br />
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
</div><br />
<div class="section" id="service"><br />
<h2>11.3. serviceコマンドで止めたり動かしたりする<a class="headerlink" href="#service" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まずやりたいのは、<br />
豆腐ボックスを簡単に止めたり動かしたりする機能を作ることです。<br />
例えばapacheなどは以下のようにスマートに止めたり動かしたりできるわけで、<br />
豆腐ボックスもこれくらいスマートにしたいものです。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># service apache start</span><br />
<span class="c"># service apache stop</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　現時点では、<br />
豆腐ボックスの起動には次のようにcrontabを使っています。<br />
しかしこれだと止めるにはわざわざ <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt><br />
などでコメントアウトしに行かなくてはなりません。<br />
下手すると <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> などと打ってえらいことになります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>crontab -l | grep -v <span class="s2">&quot;#&quot;</span><br />
<br />
*/4 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> も、<br />
現状では単に端末からバックグラウンド起動しているだけです。<br />
止めるときはkillしてやらなければなりません。</p><br />
<p>　ということで、 <tt class="docutils literal"><span class="pre">service</span></tt> から豆腐ボックスを制御できるようにしましょう。<br />
ここらへんはOSやディストリビューションによっていろいろ違いますが、<br />
ここでは <tt class="docutils literal"><span class="pre">Ubuntu</span> <span class="pre">Linux</span> <span class="pre">12.04</span></tt> に絞っています。</p><br />
<div class="section" id="id4"><br />
<h3>11.3.1. 起動スクリプトを書く<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず、豆腐ボックスに関わるシェルスクリプトを一斉に起動したり、<br />
止めたりするスクリプトをリスト2のように書きます。<br />
スクリプト中の <tt class="docutils literal"><span class="pre">TOFUBOX.LOOP</span></tt> と <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> は、<br />
まだ書いてないスクリプトです。<br />
特に凝ったことはしていません。<br />
startが引数にあったらシェルスクリプトを立ち上げて、<br />
stopがあったら全部殺すだけです。</p><br />
<p>・リスト2: TOFUBOX.INIT</p><br />
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
32</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.INIT<br />
<span class="c">#!/bin/bash</span><br />
<span class="c">#</span><br />
<span class="c"># TOFUBOX.INIT 豆腐ボックスの起動・終了</span><br />
<span class="c">#</span><br />
<span class="c"># written by R. Ueda (r-ueda\@usp-lab.com)</span><br />
<span class="nb">exec </span>2&gt; /dev/null<br />
<br />
<span class="nv">sys</span><span class="o">=</span>/home/ueda/.tofubox<br />
<br />
<span class="k">case</span> <span class="s2">&quot;$1&quot;</span> in<br />
start<span class="o">)</span><br />
 ps cax | grep -q TOFUBOX.SUSSTOP <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1<br />
 ps cax | grep -q TOFUBOX.LOOP <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1<br />
 ps cax | grep -q TOFUBOX.WATCH <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1<br />
<br />
 <span class="nv">$sys</span>/TOFUBOX.SUSSTOP &amp;<br />
 <span class="nv">$sys</span>/TOFUBOX.LOOP &amp;<br />
 <span class="nv">$sys</span>/TOFUBOX.WATCH &amp;<br />
;;<br />
stop<span class="o">)</span><br />
 killall TOFUBOX.SUSSTOP<br />
 killall TOFUBOX.LOOP<br />
 killall TOFUBOX.WATCH<br />
;;<br />
*<span class="o">)</span><br />
 <span class="nb">echo</span> <span class="s2">&quot;Usage: TOFUBOX {start|stop}&quot;</span> &gt;&amp;2<br />
 <span class="nb">exit </span>1<br />
;;<br />
<span class="k">esac</span><br />
<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">TOFUBOX.LOOP</span></tt> をリスト3に示します。<br />
単に3分ごとに <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を立ち上げるだけの、<br />
crontabの代わりのスクリプトです。</p><br />
<p>・リスト3: TOFUBOX.LOOP</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.LOOP<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="k">while</span> : ; <span class="k">do</span><br />
 /home/ueda/.tofubox/TOFUBOX.SYNC<br />
 sleep 60<br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> を動かしてみましょう。<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> については、<br />
なにもしないスクリプトを置いて、実行できるようにしておきます。<br />
リスト4に動作例を示します。</p><br />
<p>・リスト4：TOFUBOX.INITの動作確認</p><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#起動</span><br />
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT start<br />
<span class="c">#プロセスを確認。</span><br />
ueda\@X201:~/.tofubox<span class="nv">$ </span>ps cax | grep TOFU<br />
26072 pts/5 S 0:00 TOFUBOX.SUSSTOP<br />
26073 pts/5 S 0:00 TOFUBOX.LOOP<br />
26075 pts/5 S 0:00 TOFUBOX.SYNC<br />
<span class="c">#二回目のstartは失敗する。</span><br />
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT start<br />
ueda\@X201:~/.tofubox<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
<span class="c">#止める。</span><br />
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT stop<br />
ueda\@X201:~/.tofubox<span class="nv">$ </span>ps cax | grep TOFU<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次に、これを <tt class="docutils literal"><span class="pre">service</span></tt> で叩けるようにします。<br />
リスト5のように <tt class="docutils literal"><span class="pre">/etc/init.d/</span></tt> 下にリンクを貼ることでできるようになります。</p><br />
<p>・リスト5： <tt class="docutils literal"><span class="pre">/etc/init.d</span></tt> にリンクを張る</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>root\@X201:/etc/init.d# ln -s ~/.tofubox/TOFUBOX.INIT tofubox<br />
root\@X201:/etc/init.d# ls -l tofubox<br />
lrwxrwxrwx 1 root root 32 8月 17 10:08 tofubox -&gt; /home/ueda/.tofubox/TOFUBOX.INIT<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　使ってみましょう。ユーザはrootでなくても大丈夫です。<br />
動作確認した例をリスト6に示します。</p><br />
<p>・リスト6： <tt class="docutils literal"><span class="pre">service</span></tt> を使う</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>service tofubox start<br />
ueda\@X201:~<span class="nv">$ </span>ps cax | grep TOFU<br />
26433 pts/3 S 0:00 TOFUBOX.SUSSTOP<br />
26434 pts/3 S 0:00 TOFUBOX.LOOP<br />
26435 pts/3 S 0:00 TOFUBOX.SYNC<br />
ueda\@X201:~<span class="nv">$ </span>service tofubox start<br />
ueda\@X201:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
ueda\@X201:~<span class="nv">$ </span>service tofubox stop<br />
ueda\@X201:~<span class="nv">$ </span>ps cax | grep TOFU<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ところで、例えばUbuntuなどdebian系のディストリビューションでは<br />
<tt class="docutils literal"><span class="pre">/etc/init.d/skeleton</span></tt> をコピーして起動スクリプトを書くなど、<br />
ディストリビューション、OSによっていろいろ流儀があるようです。<br />
が、個人で使うものを作るうちは、<br />
なにかまずい情報をインターネットにばらまく恐れがない限り、<br />
とにかく拙速にやることをおすすめします。<br />
「許可を取るより謝る方がずっと簡単だ。」<br />
です。考えすぎはいけません。<br />
また、私のようにいちいち変数のクォートをしない人は、<br />
バックアップを欠かさずに・・・。</p><br />
</div><br />
<div class="section" id="pc"><br />
<h3>11.3.2. PCが起動したときに走らせる<a class="headerlink" href="#pc" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次に、PCが起動したときに、<br />
<tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> も起動するようにします。<br />
まあ、あまり難しく考えず、 <tt class="docutils literal"><span class="pre">/etc/rc.local</span></tt><br />
ファイルに <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> を仕掛けることにします。<br />
ただ単に書くだけだと <tt class="docutils literal"><span class="pre">root</span></tt> で起動するので、<br />
<tt class="docutils literal"><span class="pre">ueda</span></tt> で起動させるために <tt class="docutils literal"><span class="pre">su</span></tt> コマンドを使います。<br />
rootで起動すると、例えばsshのための鍵を <tt class="docutils literal"><span class="pre">ueda</span></tt><br />
の鍵でなくてrootのものを読みに行ってしまうなど、<br />
うまく動きません。リスト7のように記述します。</p><br />
<p>・リスト7： <tt class="docutils literal"><span class="pre">/etc/rc.local</span></tt> への追記</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>cat /etc/rc.local<br />
<span class="c">#!/bin/sh -e</span><br />
<span class="c">#</span><br />
<span class="c"># rc.local</span><br />
<span class="c">#</span><br />
（略）<br />
<br />
su - ueda -c <span class="s1">&#39;/home/ueda/.tofubox/TOFUBOX.INIT start&#39;</span><br />
<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これで、再起動のときにこのスクリプト（ <tt class="docutils literal"><span class="pre">rc.local</span></tt> ）が実行され、<br />
その中に書いてある <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> が実行されます。<br />
下のように、 <tt class="docutils literal"><span class="pre">ps</span></tt> に <tt class="docutils literal"><span class="pre">u</span></tt> オプションをつけて、<br />
スクリプトが指定のユーザで実行されていたら成功です。</p><br />
<p>・リスト8：再起動時の動作確認</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~# reboot<br />
...再起動...<br />
ueda\@X201:~<span class="nv">$ </span>ps caxu | grep TOFU<br />
ueda 1364 0.0 0.0 17472 1460 ? S 10:46 0:00 TOFUBOX.SUSSTOP<br />
ueda 1366 0.0 0.0 4392 608 ? S 10:46 0:00 TOFUBOX.LOOP<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
</div><br />
<div class="section" id="id5"><br />
<h2>11.4. もっとタイミングにこだわる<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、今度は同期のタイミングをもっと合理的にします。<br />
とにかく現状では3分ごとに読み書きしており、<br />
右上に「豆腐：～～～」とメッセージが出て非常に煩わしい。<br />
自分で作ってて煩わしいのですから、他人にはもっと煩わしいことでしょう。<br />
（脚注：ここ数ヶ月、画面をのぞきこんだ人に「豆腐って何ですか？」と聞かれます。<br />
「Software Design読め」と答えています。）</p><br />
<div class="section" id="id6"><br />
<h3>11.4.1. ファイルを更新したときだけ同期しにいく<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　クライアントからサーバへの同期は、クライアントの<br />
<tt class="docutils literal"><span class="pre">~/TOFUBOX</span></tt> ディレクトリが変更されたときだけでよいので、<br />
変更されたタイミングでサーバへ同期しにいくのがよいでしょう。<br />
<tt class="docutils literal"><span class="pre">inotifywait</span></tt> というコマンドを使うと、ファイルの変更等の検知ができます。</p><br />
<p>　例えば、 <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 下のディレクトリを監視するにはリスト9のように打ちます。</p><br />
<p>・リスト9： <tt class="docutils literal"><span class="pre">inotifywait</span></tt> の立ち上げ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>inotifywait -mr ~/TOFUBOX/<br />
Setting up watches. Beware: since -r was given, this may take a <span class="k">while</span>!<br />
Watches established.<br />
</pre></div><br />
</td></tr></table></div><br />
<p>立ち上がりっぱなしになるので、<br />
別の端末で <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> の中をリスト10のように操作すると、</p><br />
<p>・リスト10： <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> にちょっかいを出す。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/TOFUBOX<span class="nv">$ </span>touch hoge<br />
ueda\@X201:~/TOFUBOX<span class="nv">$ </span>rm hoge<br />
ueda\@X201:~/TOFUBOX<span class="nv">$ </span>cat ~/TESTDATA | head -n 1000 &gt; hoge<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">inotifywait</span></tt> を立ち上げた画面には、<br />
ファイル操作のログのようなものが出てきます。</p><br />
<p>・リスト11： <tt class="docutils literal"><span class="pre">inotifywait</span></tt> の出力</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/TOFUBOX/ OPEN hoge<br />
/home/ueda/TOFUBOX/ ATTRIB hoge<br />
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge<br />
/home/ueda/TOFUBOX/ DELETE hoge<br />
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge<br />
/home/ueda/TOFUBOX/ MODIFY hoge<br />
/home/ueda/TOFUBOX/ OPEN hoge<br />
/home/ueda/TOFUBOX/ MODIFY hoge<br />
...<br />
/home/ueda/TOFUBOX/ MODIFY hoge<br />
/home/ueda/TOFUBOX/ MODIFY hoge<br />
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ということは、これを立ち上げておいて、<br />
ファイルに変更があったときだけ、<br />
クライアントからサーバへの同期を行えばよいということになります。<br />
また、 <tt class="docutils literal"><span class="pre">inotifywait</span></tt><br />
はリスト11のようにファイルに関する様々なイベントに反応しますが、<br />
<tt class="docutils literal"><span class="pre">-e</span></tt> というオプションで<br />
同期するファイルができるときのイベントだけ引っ掛けることもできます。<br />
（リスト12内で使用しています。）</p><br />
<p>　さっき作った空のスクリプト <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> には、<br />
この役目をさせるつもりでした。<br />
リスト12のように <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> を実装します。</p><br />
<p>・リスト12： <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt></p><br />
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
13</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.WATCH<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">dir</span><span class="o">=</span>/home/usp/TOFUBOX<br />
<span class="nv">sys</span><span class="o">=</span>/home/usp/.tofubox<br />
<br />
touch <span class="nv">$sys</span>/PUSH.REQUEST<br />
<br />
inotifywait -e moved_to -e close_write -mr <span class="nv">$dir</span> |<br />
<span class="k">while </span><span class="nb">read </span>str ; <span class="k">do</span><br />
 <span class="o">[</span> -e <span class="nv">$sys</span>/PUSH.REQUEST <span class="o">]</span> <span class="o">&amp;&amp;</span> touch <span class="nv">$sys</span>/PUSH.WAIT<br />
 touch <span class="nv">$sys</span>/PUSH.REQUEST<br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> は、</p><br />
<ul class="simple"><br />
<li>ファイルが <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> に移動してきた</li><br />
<li><tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 内でなにかファイルの書き込みが終わってファイルが閉じられた</li><br />
</ul><br />
<p>の二つの事象を監視し、これらが起こったら、<br />
<tt class="docutils literal"><span class="pre">~/.tofubox/</span></tt> の下に <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt><br />
と <tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> いうファイルを置きます。<br />
<tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> は、 <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> がすでにあるときに置きます。</p><br />
<p>　そして、 <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> 内の、<br />
クライアントのディレクトリをサーバに同期しにいく部分<br />
（リスト1の31～35行目）<br />
を次のように書き換えます。</p><br />
<p>・リスト13：クライアント-&gt;サーバ同期のコード変更</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#push############################</span><br />
<span class="k">while</span> <span class="o">[</span> -e <span class="s2">&quot;$sys/PUSH.REQUEST&quot;</span> <span class="o">]</span> ; <span class="k">do</span><br />
<span class="k"> </span>MESSAGE <span class="s2">&quot;送信開始&quot;</span><br />
<br />
 rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/<br />
 ERROR_CHECK <span class="s2">&quot;送信中断&quot;</span><br />
<br />
 rm <span class="nv">$sys</span>/PUSH.REQUEST<br />
 <span class="o">[</span> -e <span class="nv">$sys</span>/PUSH.WAIT <span class="o">]</span> <span class="o">&amp;&amp;</span> mv <span class="nv">$sys</span>/PUSH.WAIT <span class="nv">$sys</span>/PUSH.REQUEST<br />
<br />
 MESSAGE <span class="s2">&quot;送信完了&quot;</span><br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　rsync がうまくいったら、 <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> を消します。<br />
この間に <tt class="docutils literal"><span class="pre">inotifywait</span></tt> が反応していたら、<br />
<tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> ができているのでこれを<br />
<tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> に名前を変えてもう一回 <tt class="docutils literal"><span class="pre">rsync</span></tt> します。<br />
通信が途切れなければという条件はつきますが、<br />
クライアント側でファイルを書き換えている時はずっとロックを持ったままで<br />
<tt class="docutils literal"><span class="pre">rsync</span></tt> が続きます。</p><br />
<p>　この実装には一つ問題があって、これだとサーバ側にデータ変更があり、<br />
クライアント側の <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> に変更があったら<br />
<tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> ができるので、<br />
一度無駄な書き込みが起こります。これはご愛嬌ということで。</p><br />
</div><br />
<div class="section" id="id7"><br />
<h3>11.4.2. 本当に受信したときだけ通知する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　読み込みの方は定期的に rsync をかけておいてもよいのですが、<br />
rsync が実際にファイルを読み込んでいないのに通知が出るのはかっこ悪い。<br />
実際に読み込んだら通知を出さないと、有用な情報になりません。<br />
余談ですが、弊社ではこういう通知を出すことは厳重な作法違反とされています。<br />
これもなんとかしましょう。</p><br />
<p>　今度は、 <tt class="docutils literal"><span class="pre">inotifywait</span></tt> とは別のアプローチをとってみましょう。<br />
（実は書き込みでも同じ方法が使えますが。）<br />
ややこしいので、先にコードを見せます。<br />
リスト1の23行目、ロックを取りに行った後のコードにリスト14のコードを加えます。</p><br />
<p>・リスト14：サーバ-&gt;クライアント同期のコード変更</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#同期の必要がなければすぐ終了</span><br />
<span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span>rsync -auzin --timeout<span class="o">=</span>30 <span class="nv">$s</span> <span class="nv">$c</span> | wc -c<span class="k">)</span><br />
<span class="c">#通信に失敗した、あるいは同期済みなら終了</span><br />
<span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$NUM&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> -o <span class="s2">&quot;$NUM&quot;</span> -eq 0 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;rmdir $sys/LOCK&quot;</span><br />
 <span class="nb">exit </span>0<br />
<span class="k">fi</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　何をやっているのかというと、二行目で <tt class="docutils literal"><span class="pre">rsync</span></tt> を空実行して同期の必要を探り、<br />
同期の必要があれば、そのまま下に書いてある読み込み処理（と書き込み処理）を実行します。<br />
必要がなければif文内の処理でロックを返上します。</p><br />
<p>　二行目の <tt class="docutils literal"><span class="pre">rsync</span></tt> には、 <tt class="docutils literal"><span class="pre">i</span></tt> と <tt class="docutils literal"><span class="pre">n</span></tt> というオプションがついています。<br />
<tt class="docutils literal"><span class="pre">rsync</span></tt> に <tt class="docutils literal"><span class="pre">i</span></tt> を指定すると、以下のように更新のリストが表示されます。</p><br />
<div class="highlight-bash"><pre>#iで更新のリストを表示<br />
ueda\@uedaubuntu:~$ rsync -auzi tofu.usptomonokai.jp:~/hoge ./<br />
cd+++++++++ hoge/<br />
&gt;f+++++++++ hoge/file1<br />
&gt;f+++++++++ hoge/file2<br />
&gt;f+++++++++ hoge/file3<br />
#もう一度実行すると、すでに同期済みなのでなにも表示されない<br />
ueda\@uedaubuntu:~$ rsync -auzi tofu.usptomonokai.jp:~/hoge ./<br />
ueda\@uedaubuntu:~$</pre><br />
</div><br />
<p>また、 <tt class="docutils literal"><span class="pre">n</span></tt> を指定すると、 <tt class="docutils literal"><span class="pre">rsync</span></tt> は同期処理をしません。<br />
ドライランというやつです。</p><br />
<p>　したがって、二行目の <tt class="docutils literal"><span class="pre">rsync</span></tt> では、実際に同期は行わず、<br />
同期に必要なファイルのリストがあれば、そのリストを出力します。<br />
その出力を <tt class="docutils literal"><span class="pre">wc</span> <span class="pre">-c</span></tt> に通して、 <tt class="docutils literal"><span class="pre">$NUM</span></tt> という変数に代入しています。<br />
同期の必要がなければなにもリストが出ないので、<br />
<tt class="docutils literal"><span class="pre">$NUM</span></tt> はゼロになり、あれば非ゼロになります。</p><br />
<p>　これで不必要な通知は画面に出なくなります。</p><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>11.5. 完成！<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　余計な通知が出なくなったところで、完成としましょう。<br />
整理した <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をGitHub<br />
（ryuichiueda/SoftwareDesign/201211の下,<br />
<a class="reference external" href="https://github.com/ryuichiueda/SoftwareDesign/blob/master/201211/client/TOFUBOX.SYNC">https://github.com/ryuichiueda/SoftwareDesign/blob/master/201211/client/TOFUBOX.SYNC</a>）<br />
に掲載しておきました。<br />
整理と言っても、記号類がごちゃっとして綺麗ではありませんが・・・。<br />
これはコードの短さに免じて許してやってください。<br />
結局、クライアント側のコードは118行、サーバ側のコードは20行となりました。<br />
たった138行です。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h2>11.6. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回と今回で、オンラインストレージもどき「豆腐ボックス」<br />
を作りました。出てきたテクニックをまとめると次のようになります。</p><br />
<ul class="simple"><br />
<li>sshとrsyncのタイムアウト</li><br />
<li>rsyncの使い方あれこれ</li><br />
<li>notify-send</li><br />
<li>inotify（inotifywait）</li><br />
<li>mkdir を使った排他制御</li><br />
<li>service</li><br />
<li>sshを使ったリモートからのコマンド実行</li><br />
</ul><br />
<p>　筆者はこれらの何一つエキスパートということはないのですが、<br />
manを読んで、webで調べて、シェルスクリプトで組み合わせるだけで、<br />
なんとか豆腐ボックスを作りました。<br />
ユーザが使えるOSの機能はほとんどコマンドで準備されます。<br />
ですから、シェルスクリプトを書けると機能を総動員することができます。<br />
これが、シェルスクリプトでアプリケーション<br />
（あるいはアプリケーションのプロトタイプ）<br />
を書く一番の利点でしょう。</p><br />
<p>　もしかしたら、他にもっと便利な機能があって、<br />
もっとコードを短くすることができるかもしれません。<br />
また、今回はやらなかったファイル消去の同期も可能かもしれません。</p><br />
<p>　次回からは、Maildirに蓄えたメールをさばくというお題に取り組みます。</p><br />
</div><br />
</div><br />

