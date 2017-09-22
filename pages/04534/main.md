---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年11月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>11. 開眼シェルスクリプト 第11回 オンラインストレージもどきを作る（２）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>11.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は豆腐ボックス第二回です。
前回はrsyncを使ったオンラインストレージ
（たまっていく一方なのでモドキ）を作りました。
今回はこれを少しずつ改善していきます。
普段あまり使わない機能のオンパレードなので、
筆者も詳しくはないのですが、
一緒に一つずつ確認していきましょう。</p>
<p>　今回は、前回にも増して力技の嵐です。
また、私は変数にクォートをつけるどうのこうのには無頓着なので、
（脚注：必要な局面では頓着します。）
人によっては「こんなコーディングおかしい」と思うかもしれません。
しかし、秀吉の「墨俣一夜城」の例はちょっと言い過ぎかもしれませんが、
人の想像を超えた早さで何かを作れるということには、
組織や自身の行く末を変えるくらいの力があります。</p>
</div>
<div class="section" id="id3">
<h2>11.2. おさらい<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　豆腐ボックスは、サーバを経由して複数のクライアントPCのファイルを
同期するアプリケーションです。
各PCの <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 内のディレクトリをrsyncで同期します。
クライアントPCは多数台の接続を想定しており、
一つの同時に二台以上のクライアントとサーバが同期処理しないように、
排他制御の仕組みが入っています。</p>
<p>　排他制御は、クライアント側からサーバ側にディレクトリを作りにいき、
その成否を利用して行っています。
<tt class="docutils literal"><span class="pre">mkdir</span></tt> を排他区間の作成に使うという手法です（前回参照）。</p>
<p>　クライアント側は以下の二つのスクリプトで構成されています。
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> が同期を行うスクリプトです。
また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> は、PCがスリープから復帰したら、
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を殺すスクリプトです。
排他制御のために必要なスクリプトです。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>tree .tofubox/
.tofubox/
├── TOFUBOX.SUSSTOP
└── TOFUBOX.SYNC
</pre></div>
</td></tr></table></div>
<p>　サーバ側には、以下のようにシェルスクリプトが一つだけあります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@tofu:~<span class="nv">$ </span>tree .tofubox/
.tofubox/
└── REMOVE.LOCK
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">REMOVE.LOCK</span></tt> は、
クライアント側がロックをかけた後に通信を中断したかどうかを判断し、
適切な時にロックを外します。</p>
<p>　豆腐ボックスのコードの総量は、クライアント側、
サーバ側のものを全部足してもわずか73行です。
せっかくコードが短いんですから、一番長い
<tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をリスト1に全部掲載しておきます。
このコードには、後から手を入れます。</p>
<p>・リスト1: TOFUBOX.SYNC（前回のもの）</p>
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
37
38
39</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.SYNC
<span class="c">#!/bin/bash -xv</span>
<span class="c">#</span>
<span class="c"># TOFUBOX.SYNC</span>
<span class="c">#</span>
<span class="c"># written by R. Ueda (usp-lab.com)</span>
<span class="nb">exec </span>2&gt; /tmp/<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>

<span class="nv">server</span><span class="o">=</span>tofu.usptomonokai.jp
<span class="nv">dir</span><span class="o">=</span>/home/ueda

MESSAGE <span class="o">()</span> <span class="o">{</span>
 <span class="nv">DISPLAY</span><span class="o">=</span>:0 notify-send <span class="s2">&quot;豆腐: $1&quot;</span>
<span class="o">}</span>

ERROR_CHECK<span class="o">(){</span>
 <span class="o">[</span> <span class="s2">&quot;$(echo ${PIPESTATUS[\@]} | tr -d &#39; 0&#39;)&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span>
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
</div>
<div class="section" id="service">
<h2>11.3. serviceコマンドで止めたり動かしたりする<a class="headerlink" href="#service" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まずやりたいのは、
豆腐ボックスを簡単に止めたり動かしたりする機能を作ることです。
例えばapacheなどは以下のようにスマートに止めたり動かしたりできるわけで、
豆腐ボックスもこれくらいスマートにしたいものです。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># service apache start</span>
<span class="c"># service apache stop</span>
</pre></div>
</td></tr></table></div>
<p>　現時点では、
豆腐ボックスの起動には次のようにcrontabを使っています。
しかしこれだと止めるにはわざわざ <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt>
などでコメントアウトしに行かなくてはなりません。
下手すると <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> などと打ってえらいことになります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>crontab -l | grep -v <span class="s2">&quot;#&quot;</span>

*/4 * * * * /home/ueda/.tofubox/TOFUBOX.SYNC
</pre></div>
</td></tr></table></div>
<p>　また、 <tt class="docutils literal"><span class="pre">TOFUBOX.SUSSTOP</span></tt> も、
現状では単に端末からバックグラウンド起動しているだけです。
止めるときはkillしてやらなければなりません。</p>
<p>　ということで、 <tt class="docutils literal"><span class="pre">service</span></tt> から豆腐ボックスを制御できるようにしましょう。
ここらへんはOSやディストリビューションによっていろいろ違いますが、
ここでは <tt class="docutils literal"><span class="pre">Ubuntu</span> <span class="pre">Linux</span> <span class="pre">12.04</span></tt> に絞っています。</p>
<div class="section" id="id4">
<h3>11.3.1. 起動スクリプトを書く<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず、豆腐ボックスに関わるシェルスクリプトを一斉に起動したり、
止めたりするスクリプトをリスト2のように書きます。
スクリプト中の <tt class="docutils literal"><span class="pre">TOFUBOX.LOOP</span></tt> と <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> は、
まだ書いてないスクリプトです。
特に凝ったことはしていません。
startが引数にあったらシェルスクリプトを立ち上げて、
stopがあったら全部殺すだけです。</p>
<p>・リスト2: TOFUBOX.INIT</p>
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
32</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.INIT
<span class="c">#!/bin/bash</span>
<span class="c">#</span>
<span class="c"># TOFUBOX.INIT 豆腐ボックスの起動・終了</span>
<span class="c">#</span>
<span class="c"># written by R. Ueda (r-ueda\@usp-lab.com)</span>
<span class="nb">exec </span>2&gt; /dev/null

<span class="nv">sys</span><span class="o">=</span>/home/ueda/.tofubox

<span class="k">case</span> <span class="s2">&quot;$1&quot;</span> in
start<span class="o">)</span>
 ps cax | grep -q TOFUBOX.SUSSTOP <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1
 ps cax | grep -q TOFUBOX.LOOP <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1
 ps cax | grep -q TOFUBOX.WATCH <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1

 <span class="nv">$sys</span>/TOFUBOX.SUSSTOP &amp;
 <span class="nv">$sys</span>/TOFUBOX.LOOP &amp;
 <span class="nv">$sys</span>/TOFUBOX.WATCH &amp;
;;
stop<span class="o">)</span>
 killall TOFUBOX.SUSSTOP
 killall TOFUBOX.LOOP
 killall TOFUBOX.WATCH
;;
*<span class="o">)</span>
 <span class="nb">echo</span> <span class="s2">&quot;Usage: TOFUBOX {start|stop}&quot;</span> &gt;&amp;2
 <span class="nb">exit </span>1
;;
<span class="k">esac</span>

<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">TOFUBOX.LOOP</span></tt> をリスト3に示します。
単に3分ごとに <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> を立ち上げるだけの、
crontabの代わりのスクリプトです。</p>
<p>・リスト3: TOFUBOX.LOOP</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.LOOP
<span class="c">#!/bin/bash -xv</span>

<span class="k">while</span> : ; <span class="k">do</span>
 /home/ueda/.tofubox/TOFUBOX.SYNC
 sleep 60
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> を動かしてみましょう。
<tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> については、
なにもしないスクリプトを置いて、実行できるようにしておきます。
リスト4に動作例を示します。</p>
<p>・リスト4：TOFUBOX.INITの動作確認</p>
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#起動</span>
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT start
<span class="c">#プロセスを確認。</span>
ueda\@X201:~/.tofubox<span class="nv">$ </span>ps cax | grep TOFU
26072 pts/5 S 0:00 TOFUBOX.SUSSTOP
26073 pts/5 S 0:00 TOFUBOX.LOOP
26075 pts/5 S 0:00 TOFUBOX.SYNC
<span class="c">#二回目のstartは失敗する。</span>
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT start
ueda\@X201:~/.tofubox<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
<span class="c">#止める。</span>
ueda\@X201:~/.tofubox<span class="nv">$ </span>./TOFUBOX.INIT stop
ueda\@X201:~/.tofubox<span class="nv">$ </span>ps cax | grep TOFU
</pre></div>
</td></tr></table></div>
<p>　次に、これを <tt class="docutils literal"><span class="pre">service</span></tt> で叩けるようにします。
リスト5のように <tt class="docutils literal"><span class="pre">/etc/init.d/</span></tt> 下にリンクを貼ることでできるようになります。</p>
<p>・リスト5： <tt class="docutils literal"><span class="pre">/etc/init.d</span></tt> にリンクを張る</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>root\@X201:/etc/init.d# ln -s ~/.tofubox/TOFUBOX.INIT tofubox
root\@X201:/etc/init.d# ls -l tofubox
lrwxrwxrwx 1 root root 32 8月 17 10:08 tofubox -&gt; /home/ueda/.tofubox/TOFUBOX.INIT
</pre></div>
</td></tr></table></div>
<p>　使ってみましょう。ユーザはrootでなくても大丈夫です。
動作確認した例をリスト6に示します。</p>
<p>・リスト6： <tt class="docutils literal"><span class="pre">service</span></tt> を使う</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>service tofubox start
ueda\@X201:~<span class="nv">$ </span>ps cax | grep TOFU
26433 pts/3 S 0:00 TOFUBOX.SUSSTOP
26434 pts/3 S 0:00 TOFUBOX.LOOP
26435 pts/3 S 0:00 TOFUBOX.SYNC
ueda\@X201:~<span class="nv">$ </span>service tofubox start
ueda\@X201:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
ueda\@X201:~<span class="nv">$ </span>service tofubox stop
ueda\@X201:~<span class="nv">$ </span>ps cax | grep TOFU
</pre></div>
</td></tr></table></div>
<p>　ところで、例えばUbuntuなどdebian系のディストリビューションでは
<tt class="docutils literal"><span class="pre">/etc/init.d/skeleton</span></tt> をコピーして起動スクリプトを書くなど、
ディストリビューション、OSによっていろいろ流儀があるようです。
が、個人で使うものを作るうちは、
なにかまずい情報をインターネットにばらまく恐れがない限り、
とにかく拙速にやることをおすすめします。
「許可を取るより謝る方がずっと簡単だ。」
です。考えすぎはいけません。
また、私のようにいちいち変数のクォートをしない人は、
バックアップを欠かさずに・・・。</p>
</div>
<div class="section" id="pc">
<h3>11.3.2. PCが起動したときに走らせる<a class="headerlink" href="#pc" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次に、PCが起動したときに、
<tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> も起動するようにします。
まあ、あまり難しく考えず、 <tt class="docutils literal"><span class="pre">/etc/rc.local</span></tt>
ファイルに <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> を仕掛けることにします。
ただ単に書くだけだと <tt class="docutils literal"><span class="pre">root</span></tt> で起動するので、
<tt class="docutils literal"><span class="pre">ueda</span></tt> で起動させるために <tt class="docutils literal"><span class="pre">su</span></tt> コマンドを使います。
rootで起動すると、例えばsshのための鍵を <tt class="docutils literal"><span class="pre">ueda</span></tt>
の鍵でなくてrootのものを読みに行ってしまうなど、
うまく動きません。リスト7のように記述します。</p>
<p>・リスト7： <tt class="docutils literal"><span class="pre">/etc/rc.local</span></tt> への追記</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>cat /etc/rc.local
<span class="c">#!/bin/sh -e</span>
<span class="c">#</span>
<span class="c"># rc.local</span>
<span class="c">#</span>
（略）

su - ueda -c <span class="s1">&#39;/home/ueda/.tofubox/TOFUBOX.INIT start&#39;</span>

<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　これで、再起動のときにこのスクリプト（ <tt class="docutils literal"><span class="pre">rc.local</span></tt> ）が実行され、
その中に書いてある <tt class="docutils literal"><span class="pre">TOFUBOX.INIT</span></tt> が実行されます。
下のように、 <tt class="docutils literal"><span class="pre">ps</span></tt> に <tt class="docutils literal"><span class="pre">u</span></tt> オプションをつけて、
スクリプトが指定のユーザで実行されていたら成功です。</p>
<p>・リスト8：再起動時の動作確認</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~# reboot
...再起動...
ueda\@X201:~<span class="nv">$ </span>ps caxu | grep TOFU
ueda 1364 0.0 0.0 17472 1460 ? S 10:46 0:00 TOFUBOX.SUSSTOP
ueda 1366 0.0 0.0 4392 608 ? S 10:46 0:00 TOFUBOX.LOOP
</pre></div>
</td></tr></table></div>
</div>
</div>
<div class="section" id="id5">
<h2>11.4. もっとタイミングにこだわる<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、今度は同期のタイミングをもっと合理的にします。
とにかく現状では3分ごとに読み書きしており、
右上に「豆腐：～～～」とメッセージが出て非常に煩わしい。
自分で作ってて煩わしいのですから、他人にはもっと煩わしいことでしょう。
（脚注：ここ数ヶ月、画面をのぞきこんだ人に「豆腐って何ですか？」と聞かれます。
「Software Design読め」と答えています。）</p>
<div class="section" id="id6">
<h3>11.4.1. ファイルを更新したときだけ同期しにいく<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　クライアントからサーバへの同期は、クライアントの
<tt class="docutils literal"><span class="pre">~/TOFUBOX</span></tt> ディレクトリが変更されたときだけでよいので、
変更されたタイミングでサーバへ同期しにいくのがよいでしょう。
<tt class="docutils literal"><span class="pre">inotifywait</span></tt> というコマンドを使うと、ファイルの変更等の検知ができます。</p>
<p>　例えば、 <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 下のディレクトリを監視するにはリスト9のように打ちます。</p>
<p>・リスト9： <tt class="docutils literal"><span class="pre">inotifywait</span></tt> の立ち上げ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~<span class="nv">$ </span>inotifywait -mr ~/TOFUBOX/
Setting up watches. Beware: since -r was given, this may take a <span class="k">while</span>!
Watches established.
</pre></div>
</td></tr></table></div>
<p>立ち上がりっぱなしになるので、
別の端末で <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> の中をリスト10のように操作すると、</p>
<p>・リスト10： <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> にちょっかいを出す。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/TOFUBOX<span class="nv">$ </span>touch hoge
ueda\@X201:~/TOFUBOX<span class="nv">$ </span>rm hoge
ueda\@X201:~/TOFUBOX<span class="nv">$ </span>cat ~/TESTDATA | head -n 1000 &gt; hoge
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">inotifywait</span></tt> を立ち上げた画面には、
ファイル操作のログのようなものが出てきます。</p>
<p>・リスト11： <tt class="docutils literal"><span class="pre">inotifywait</span></tt> の出力</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/TOFUBOX/ OPEN hoge
/home/ueda/TOFUBOX/ ATTRIB hoge
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge
/home/ueda/TOFUBOX/ DELETE hoge
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge
/home/ueda/TOFUBOX/ MODIFY hoge
/home/ueda/TOFUBOX/ OPEN hoge
/home/ueda/TOFUBOX/ MODIFY hoge
...
/home/ueda/TOFUBOX/ MODIFY hoge
/home/ueda/TOFUBOX/ MODIFY hoge
/home/ueda/TOFUBOX/ CLOSE_WRITE,CLOSE hoge
</pre></div>
</td></tr></table></div>
<p>　ということは、これを立ち上げておいて、
ファイルに変更があったときだけ、
クライアントからサーバへの同期を行えばよいということになります。
また、 <tt class="docutils literal"><span class="pre">inotifywait</span></tt>
はリスト11のようにファイルに関する様々なイベントに反応しますが、
<tt class="docutils literal"><span class="pre">-e</span></tt> というオプションで
同期するファイルができるときのイベントだけ引っ掛けることもできます。
（リスト12内で使用しています。）</p>
<p>　さっき作った空のスクリプト <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> には、
この役目をさせるつもりでした。
リスト12のように <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> を実装します。</p>
<p>・リスト12： <tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt></p>
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
13</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@X201:~/.tofubox<span class="nv">$ </span>cat TOFUBOX.WATCH
<span class="c">#!/bin/bash</span>

<span class="nv">dir</span><span class="o">=</span>/home/usp/TOFUBOX
<span class="nv">sys</span><span class="o">=</span>/home/usp/.tofubox

touch <span class="nv">$sys</span>/PUSH.REQUEST

inotifywait -e moved_to -e close_write -mr <span class="nv">$dir</span> |
<span class="k">while </span><span class="nb">read </span>str ; <span class="k">do</span>
 <span class="o">[</span> -e <span class="nv">$sys</span>/PUSH.REQUEST <span class="o">]</span> <span class="o">&amp;&amp;</span> touch <span class="nv">$sys</span>/PUSH.WAIT
 touch <span class="nv">$sys</span>/PUSH.REQUEST
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">TOFUBOX.WATCH</span></tt> は、</p>
<ul class="simple">
<li>ファイルが <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> に移動してきた</li>
<li><tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> 内でなにかファイルの書き込みが終わってファイルが閉じられた</li>
</ul>
<p>の二つの事象を監視し、これらが起こったら、
<tt class="docutils literal"><span class="pre">~/.tofubox/</span></tt> の下に <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt>
と <tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> いうファイルを置きます。
<tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> は、 <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> がすでにあるときに置きます。</p>
<p>　そして、 <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> 内の、
クライアントのディレクトリをサーバに同期しにいく部分
（リスト1の31～35行目）
を次のように書き換えます。</p>
<p>・リスト13：クライアント-&gt;サーバ同期のコード変更</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#push############################</span>
<span class="k">while</span> <span class="o">[</span> -e <span class="s2">&quot;$sys/PUSH.REQUEST&quot;</span> <span class="o">]</span> ; <span class="k">do</span>
<span class="k"> </span>MESSAGE <span class="s2">&quot;送信開始&quot;</span>

 rsync -auz --timeout<span class="o">=</span>30 <span class="nv">$dir</span>/TOFUBOX/ <span class="nv">$server</span>:<span class="nv">$dir</span>/TOFUBOX/
 ERROR_CHECK <span class="s2">&quot;送信中断&quot;</span>

 rm <span class="nv">$sys</span>/PUSH.REQUEST
 <span class="o">[</span> -e <span class="nv">$sys</span>/PUSH.WAIT <span class="o">]</span> <span class="o">&amp;&amp;</span> mv <span class="nv">$sys</span>/PUSH.WAIT <span class="nv">$sys</span>/PUSH.REQUEST

 MESSAGE <span class="s2">&quot;送信完了&quot;</span>
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　rsync がうまくいったら、 <tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> を消します。
この間に <tt class="docutils literal"><span class="pre">inotifywait</span></tt> が反応していたら、
<tt class="docutils literal"><span class="pre">PUSH.WAIT</span></tt> ができているのでこれを
<tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> に名前を変えてもう一回 <tt class="docutils literal"><span class="pre">rsync</span></tt> します。
通信が途切れなければという条件はつきますが、
クライアント側でファイルを書き換えている時はずっとロックを持ったままで
<tt class="docutils literal"><span class="pre">rsync</span></tt> が続きます。</p>
<p>　この実装には一つ問題があって、これだとサーバ側にデータ変更があり、
クライアント側の <tt class="docutils literal"><span class="pre">~/TOFUBOX/</span></tt> に変更があったら
<tt class="docutils literal"><span class="pre">PUSH.REQUEST</span></tt> ができるので、
一度無駄な書き込みが起こります。これはご愛嬌ということで。</p>
</div>
<div class="section" id="id7">
<h3>11.4.2. 本当に受信したときだけ通知する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　読み込みの方は定期的に rsync をかけておいてもよいのですが、
rsync が実際にファイルを読み込んでいないのに通知が出るのはかっこ悪い。
実際に読み込んだら通知を出さないと、有用な情報になりません。
余談ですが、弊社ではこういう通知を出すことは厳重な作法違反とされています。
これもなんとかしましょう。</p>
<p>　今度は、 <tt class="docutils literal"><span class="pre">inotifywait</span></tt> とは別のアプローチをとってみましょう。
（実は書き込みでも同じ方法が使えますが。）
ややこしいので、先にコードを見せます。
リスト1の23行目、ロックを取りに行った後のコードにリスト14のコードを加えます。</p>
<p>・リスト14：サーバ-&gt;クライアント同期のコード変更</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#同期の必要がなければすぐ終了</span>
<span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span>rsync -auzin --timeout<span class="o">=</span>30 <span class="nv">$s</span> <span class="nv">$c</span> | wc -c<span class="k">)</span>
<span class="c">#通信に失敗した、あるいは同期済みなら終了</span>
<span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$NUM&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> -o <span class="s2">&quot;$NUM&quot;</span> -eq 0 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>ssh -o <span class="nv">ConnectTimeout</span><span class="o">=</span>5 <span class="nv">$server</span> <span class="s2">&quot;rmdir $sys/LOCK&quot;</span>
 <span class="nb">exit </span>0
<span class="k">fi</span>
</pre></div>
</td></tr></table></div>
<p>　何をやっているのかというと、二行目で <tt class="docutils literal"><span class="pre">rsync</span></tt> を空実行して同期の必要を探り、
同期の必要があれば、そのまま下に書いてある読み込み処理（と書き込み処理）を実行します。
必要がなければif文内の処理でロックを返上します。</p>
<p>　二行目の <tt class="docutils literal"><span class="pre">rsync</span></tt> には、 <tt class="docutils literal"><span class="pre">i</span></tt> と <tt class="docutils literal"><span class="pre">n</span></tt> というオプションがついています。
<tt class="docutils literal"><span class="pre">rsync</span></tt> に <tt class="docutils literal"><span class="pre">i</span></tt> を指定すると、以下のように更新のリストが表示されます。</p>
<div class="highlight-bash"><pre>#iで更新のリストを表示
ueda\@uedaubuntu:~$ rsync -auzi tofu.usptomonokai.jp:~/hoge ./
cd+++++++++ hoge/
&gt;f+++++++++ hoge/file1
&gt;f+++++++++ hoge/file2
&gt;f+++++++++ hoge/file3
#もう一度実行すると、すでに同期済みなのでなにも表示されない
ueda\@uedaubuntu:~$ rsync -auzi tofu.usptomonokai.jp:~/hoge ./
ueda\@uedaubuntu:~$</pre>
</div>
<p>また、 <tt class="docutils literal"><span class="pre">n</span></tt> を指定すると、 <tt class="docutils literal"><span class="pre">rsync</span></tt> は同期処理をしません。
ドライランというやつです。</p>
<p>　したがって、二行目の <tt class="docutils literal"><span class="pre">rsync</span></tt> では、実際に同期は行わず、
同期に必要なファイルのリストがあれば、そのリストを出力します。
その出力を <tt class="docutils literal"><span class="pre">wc</span> <span class="pre">-c</span></tt> に通して、 <tt class="docutils literal"><span class="pre">$NUM</span></tt> という変数に代入しています。
同期の必要がなければなにもリストが出ないので、
<tt class="docutils literal"><span class="pre">$NUM</span></tt> はゼロになり、あれば非ゼロになります。</p>
<p>　これで不必要な通知は画面に出なくなります。</p>
</div>
</div>
<div class="section" id="id8">
<h2>11.5. 完成！<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　余計な通知が出なくなったところで、完成としましょう。
整理した <tt class="docutils literal"><span class="pre">TOFUBOX.SYNC</span></tt> をGitHub
（ryuichiueda/SoftwareDesign/201211の下,
<a class="reference external" href="https://github.com/ryuichiueda/SoftwareDesign/blob/master/201211/client/TOFUBOX.SYNC">https://github.com/ryuichiueda/SoftwareDesign/blob/master/201211/client/TOFUBOX.SYNC</a>）
に掲載しておきました。
整理と言っても、記号類がごちゃっとして綺麗ではありませんが・・・。
これはコードの短さに免じて許してやってください。
結局、クライアント側のコードは118行、サーバ側のコードは20行となりました。
たった138行です。</p>
</div>
<div class="section" id="id9">
<h2>11.6. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回と今回で、オンラインストレージもどき「豆腐ボックス」
を作りました。出てきたテクニックをまとめると次のようになります。</p>
<ul class="simple">
<li>sshとrsyncのタイムアウト</li>
<li>rsyncの使い方あれこれ</li>
<li>notify-send</li>
<li>inotify（inotifywait）</li>
<li>mkdir を使った排他制御</li>
<li>service</li>
<li>sshを使ったリモートからのコマンド実行</li>
</ul>
<p>　筆者はこれらの何一つエキスパートということはないのですが、
manを読んで、webで調べて、シェルスクリプトで組み合わせるだけで、
なんとか豆腐ボックスを作りました。
ユーザが使えるOSの機能はほとんどコマンドで準備されます。
ですから、シェルスクリプトを書けると機能を総動員することができます。
これが、シェルスクリプトでアプリケーション
（あるいはアプリケーションのプロトタイプ）
を書く一番の利点でしょう。</p>
<p>　もしかしたら、他にもっと便利な機能があって、
もっとコードを短くすることができるかもしれません。
また、今回はやらなかったファイル消去の同期も可能かもしれません。</p>
<p>　次回からは、Maildirに蓄えたメールをさばくというお題に取り組みます。</p>
</div>
</div>

