---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年7月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="cgi1">
<h1>19. 開眼シェルスクリプト 第19回 シェルスクリプトでCGIスクリプト1<a class="headerlink" href="#cgi1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　今回から何回かは、連載当初からいつかやるはめになると考えていた
CGIスクリプトを作るというお題を扱います。</p>
<p>　CGIというのは common gateway interface の略で、
単純に言うとブラウザから
ウェブサーバに置いてあるプログラムを起動するための仕様です。
CGIという言葉は interface を指すので、
CGIで動く（動かされる）プログラムのことは、
CGIプログラムと言ったりCGIスクリプトと言ったりする方が丁寧です。
スクリプト言語で書いた場合はCGIスクリプトと言うのがよいでしょう。</p>
<p>　CGIプログラムは、どんな言語で作っても構いません。
C言語で書いても良いわけですが、
この領域ではlightweight language（LL言語）で書かれることがほとんどであり、
伝統的にはperl、php、最近ではruby、pythonもよく使われます。</p>
<p>　そこにシェルスクリプトを加えてやろうというのが今回から数回の内容です。
シェルスクリプトは簡単にOSのコマンドが使えるので大丈夫かいなとよく言われます。
確かにウェブでデータをやりとりするという目的に比べると、
シェルスクリプトでできることはそれを遥かに超越しており、
しかも文字数少なく邪悪なことができてしまいます。
<tt class="docutils literal"><span class="pre">rm</span> <span class="pre">-Rf</span> <span class="pre">/</span></tt> （8文字！）とか。</p>
<p>　しかし、「インジェクションを食らいやすいかどうか」という観点においては、
気をつけていれば言語レベルでは他の言語と大差なく、
むしろ食らいにくいんじゃないかなと筆者は考えています。
世間での書き方のガイドラインが未成熟なだけで、
シェルスクリプトでCGIをやると危ないというのは短絡的で相手を知らなさすぎます。
食わず嫌いはいけません。</p>
<p>　「女をよくいうひとは、女を十分知らないものであり、女をいつも悪くいう人は、
女を全く知らないものである。」
&#8212; モーリス・ルブラン「怪盗アルセーヌ・ルパン」</p>
<p>　 <tt class="docutils literal"><span class="pre">sed</span> <span class="pre">'s/女/シェルスクリプト/g'</span></tt> して音読してから、
先にお進みください。</p>
<div class="section" id="apache">
<h2>19.1. Apacheを準備<a class="headerlink" href="#apache" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回想定する環境はbash、Apache が動くUNIX系の環境です。
筆者は手元で動かしたいので今回もMacを使います。
Linuxで動かす場合については情報が大量にweb上にあるので、
ここで説明しなくても大丈夫でしょう。</p>
<p>　筆者もこれを執筆中に初めて知ったのですが、
OS Xには最初からapache がバンドルされていて、
すぐ使えるようになっています。</p>
<p>　リスト1のようにコマンドを打つと、apacheが起動します。</p>
<ul class="simple">
<li>リスト1: apacheを立ち上げる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:apache2 ueda<span class="nv">$ </span>sudo -s
bash-3.2# apachectl start
org.apache.httpd: Already loaded
bash-3.2# ps cax | grep httpd
16023 ?? Ss 0:00.15 httpd
16024 ?? S 0:00.00 httpd
</pre></div>
</td></tr></table></div>
<p>　本連載の読者ならば、動作確認はブラウザじゃなくて
リスト2のようにcurlでやりましょう。</p>
<ul class="simple">
<li>リスト2: curlで動作確認</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:apache2 ueda<span class="nv">$ </span>curl http://localhost
&lt;html&gt;&lt;body&gt;&lt;h1&gt;It works!&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;
</pre></div>
</td></tr></table></div>
<p>　次に、リスト3のように、cgiを置くディレクトリを確認します。
CGIプログラムは <tt class="docutils literal"><span class="pre">cgi-bin</span></tt> というところに置く事が多いので、
<tt class="docutils literal"><span class="pre">cgi-bin</span></tt> で設定ファイル（ <tt class="docutils literal"><span class="pre">httpd.conf</span></tt> ）を検索します。
検索はエディタを開いて、そのエディタの機能で行っても構いません。
ただ、こういった記事や説明手順を書くときは、
シェルの操作を行ったような体裁の方が分かりやすく書けます。
さっきのcurlも、ブラウザのスクリーンショットを掲載するより楽です。
きっとコミュニケーションのコストに違いがあるのでしょう。
案外大事な余談でした。</p>
<ul class="simple">
<li>リスト3: <tt class="docutils literal"><span class="pre">cgi-bin</span></tt> の場所を調査</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>apachectl -V | grep conf
 -D <span class="nv">SERVER_CONFIG_FILE</span><span class="o">=</span><span class="s2">&quot;/private/etc/apache2/httpd.conf&quot;</span>

uedamac:~ ueda<span class="nv">$ </span>cat /private/etc/apache2/httpd.conf | grep cgi-bin
 ScriptAliasMatch ^/cgi-bin/<span class="o">((</span>?!<span class="o">(</span>?i:webobjects<span class="o">))</span>.*<span class="nv">$)</span> <span class="s2">&quot;/Library/WebServer/CGI-Executables/$1&quot;</span>
<span class="c">#ErrorDocument 404 &quot;/cgi-bin/missing_handler.pl&quot;</span>
</pre></div>
</td></tr></table></div>
<p>　確認の結果、 <tt class="docutils literal"><span class="pre">/Library/WebServer/CGI-Executables/</span></tt> という、
きったねえ名前のディレクトリで動くことが分かりました。
今回は大変遺憾ですが、ここにCGIスクリプトを置く事にします。
いちいちこのディレクトリを覚えておくのは面倒なので、
リスト4のように自分のホームの下にシンボリックリンクを張りましょう。
どうせ自分しか使わないので、所有者も変えておきます。</p>
<ul class="simple">
<li>リスト4: ホームから簡単にアクセスできるようにする</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ln -s /Library/WebServer/CGI-Executables/ ./cgi-bin
uedamac:~ ueda<span class="nv">$ </span><span class="nb">cd </span>cgi-bin
uedamac:cgi-bin ueda<span class="nv">$ </span>sudo chown ueda:wheel ./
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="cgi">
<h2>19.2. CGIプログラムとはなんぞや？=&gt;ただのプログラム<a class="headerlink" href="#cgi" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さあ作業開始です。最初にやるのはCGIプログラムを動かすことです。
CGIプログラムと聞くと何か特別なものだと考えている人が多いので、
その誤解を解いておきましょう。ちょっとした実験をします。</p>
<p>　まず、 <tt class="docutils literal"><span class="pre">/tmp/</span></tt> の下に <tt class="docutils literal"><span class="pre">hoge</span></tt> というファイルを作り、
所有者をapacheの実行ユーザに変えておきます。
apacheの実行ユーザ、そしてグループはリスト5のように調査できます。</p>
<ul class="simple">
<li>リスト5: apacheの動作するユーザ、グループを調査</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>grep ^User /private/etc/apache2/httpd.conf
User _www
uedamac:~ ueda<span class="nv">$ </span>grep ^Group /private/etc/apache2/httpd.conf
Group _www
</pre></div>
</td></tr></table></div>
<p>リスト6のように <tt class="docutils literal"><span class="pre">hoge</span></tt> を置きましょう。</p>
<ul class="simple">
<li>リスト6: ファイルを置いてapacheから操作できるように所有者変更</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>touch /tmp/hoge
uedamac:cgi-bin ueda<span class="nv">$ </span>sudo chown _www:_www /tmp/hoge
</pre></div>
</td></tr></table></div>
<p>次に、リスト7のように <tt class="docutils literal"><span class="pre">rm</span></tt> コマンドを <tt class="docutils literal"><span class="pre">cgi-bin</span></tt> の下に置きます。
拡張子は <tt class="docutils literal"><span class="pre">.cgi</span></tt> にしておきます。</p>
<ul class="simple">
<li>リスト7: <tt class="docutils literal"><span class="pre">rm</span></tt> コマンドに拡張子をつけて <tt class="docutils literal"><span class="pre">cgi-bin</span></tt> に置く</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>cp /bin/rm ~/cgi-bin/rm.cgi
</pre></div>
</td></tr></table></div>
<p>では、この <tt class="docutils literal"><span class="pre">rm.cgi</span></tt> を、ブラウザで呼び出してみます。
これは <tt class="docutils literal"><span class="pre">curl</span></tt> を使うと雰囲気が出ないので、ブラウザで。
アドレスの欄には、
<tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/rm.cgi?/tmp/hoge</span></tt> と書きます。</p>
<p>　ブラウザに表示されるのは、残念ながら図1のような
Internal Server Error です。</p>
<ul class="simple">
<li>図1: <tt class="docutils literal"><span class="pre">rm.cgi</span></tt> を実行した結果</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="RM_CGI.png"><img alt="" src="RM_CGI.png" style="width: 30%;" /></a>
</div>
<p>しかし、 <tt class="docutils literal"><span class="pre">/tmp/hoge</span></tt> は、リスト8のように消えています。</p>
<ul class="simple">
<li>リスト8: <tt class="docutils literal"><span class="pre">/tmp/hoge</span></tt> が消える</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>ls /tmp/hoge
ls: /tmp/hoge: No such file or directory
</pre></div>
</td></tr></table></div>
<p>びっくりしましたでしょうか？</p>
<p>　結局、何をやったかというと、
ブラウザに <tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/rm.cgi?/tmp/hoge</span></tt>
を指定することで、サーバ（この例では自分のMac）の
<tt class="docutils literal"><span class="pre">cgi-bin</span></tt> の下の <tt class="docutils literal"><span class="pre">rm.cgi</span></tt> のオプションに、
<tt class="docutils literal"><span class="pre">/tmp/hoge</span></tt> を渡して <tt class="docutils literal"><span class="pre">/tmp/hoge</span></tt> を消したということになります。
<tt class="docutils literal"><span class="pre">ssh</span></tt> でリモートのサーバに対し、</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>ssh &lt;ホスト&gt; <span class="s1">&#39;~/cgi-bin/rm.cgi /tmp/hoge&#39;</span>
</pre></div>
</div>
<p>とやることと何ら変わりがありません。
違うのは、22番ポートでなく、80番ポートを使用したくらいです。</p>
<p>　ただし、 <tt class="docutils literal"><span class="pre">rm</span></tt> コマンドをインターネット上から
不特定多数の人にやられたらたまったものではないので、
apacheでは、</p>
<ul class="simple">
<li>UserやGroupで実行するユーザを限定</li>
<li>実行できるプログラムを特定のディレクトリの下のものに制限</li>
<li>拡張子を登録した物だけに制限</li>
</ul>
<p>するなど、一定の制約を設けてなるべく安全にしてあります。</p>
<p>　逆に、 <tt class="docutils literal"><span class="pre">~/cgi-bin/</span></tt> の下に置いて実行可能なようにパーミッションを設定すれば、
プログラムはなんでもCGIで起動できるようになります。
<tt class="docutils literal"><span class="pre">rm.cgi</span></tt> のようにC言語で書いてあっても、
伝統的に perl で書いても動きます。</p>
<p>　・・・ということは、シェルスクリプトでも動くということになります。</p>
</div>
<div class="section" id="id1">
<h2>19.3. CGIシェルスクリプトを書く<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、シェルスクリプトでCGIスクリプトを書いてみましょう。
まず、ブラウザに字を表示するための最小限のCGIスクリプトをリスト9に示します。</p>
<ul class="simple">
<li>リスト9: 最小限のCGIスクリプト</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat smallest.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/html&quot;</span>
<span class="nb">echo</span> <span class="s2">&quot;&quot;</span>
<span class="nb">echo</span> 魚眼perlスクリプト
//書いたら実行できるようにしておきましょう。
uedamac:cgi-bin ueda<span class="nv">$ </span>chmod +x smallest.cgi
</pre></div>
</td></tr></table></div>
<p>　このシェルスクリプトは何の変哲もないものなので、
リスト10のように普通に端末から実行できます。</p>
<ul class="simple">
<li>リスト10: 端末からCGIスクリプトを実行してみる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>./smallest.cgi 2&gt; /dev/null
Content-Type: text/html

魚眼perlスクリプト
</pre></div>
</td></tr></table></div>
<p>　何の変哲もないのですが、ブラウザから呼び出すと図2のように見えます。</p>
<ul class="simple">
<li>図2: ブラウザから <tt class="docutils literal"><span class="pre">smallest.cgi</span></tt> を実行した結果</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="SMALLEST.png"><img alt="" src="SMALLEST.png" style="width: 50%;" /></a>
</div>
<p>　この例のポイントはいくつかあります。
まず、 <tt class="docutils literal"><span class="pre">Content-Type-type:</span> <span class="pre">text/html</span></tt> ですが、
これはHTTPプロトコルで定められたHTTPヘッダです。
さきほどの <tt class="docutils literal"><span class="pre">rm.cgi</span></tt> でブラウザにエラーが出たのは、
HTTPヘッダを <tt class="docutils literal"><span class="pre">rm.cgi</span></tt> が出さないからです。
ブラウザとapacheはHTTPプロトコルでしゃべっているので、
apache（が動かしているCGIプログラム）
がHTTPヘッダを返さず、ブラウザが怒ったのでした。</p>
<p>　ヘッダの次の <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">&quot;&quot;</span></tt> は、
ヘッダと中身を区切る空白行を出すためにあります。
ヘッダの前には余計なものを出してはいけないので、
例えばリスト11のようなCGIスクリプトをブラウザから呼び出すと、
やはりブラウザにエラーが表示されます。</p>
<ul class="simple">
<li>リスト11: HTTPヘッダの前に何か出力するとエラーになる</li>
</ul>
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
11</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat dame.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">echo </span>huh?
<span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/html&quot;</span>
<span class="nb">echo</span> <span class="s2">&quot;&quot;</span>
<span class="nb">echo</span> 湾岸pythonスクリプト
uedamac:cgi-bin ueda<span class="nv">$ </span>curl http://localhost/cgi-bin/dame.cgi 2&gt; /dev/null | head -n 3
&lt;!DOCTYPE HTML PUBLIC <span class="s2">&quot;-//IETF//DTD HTML 2.0//EN&quot;</span>&gt;
&lt;html&gt;&lt;head&gt;
&lt;title&gt;500 Internal Server Error&lt;/title&gt;
</pre></div>
</td></tr></table></div>
<p>　この例では <tt class="docutils literal"><span class="pre">Content-Type-type:</span> <span class="pre">text/html</span></tt> と、
「テキストのHTML」を送ると言っておいて、
実際には単なる一行のテキストしか送っていませんが、
これは今のところこだわらないでおきましょう。</p>
<p>　次に着目すべきは、シェルスクリプトはただ標準出力に字を出しているだけで、
ブラウザやウェブサーバに何か特別なことをしているわけではないということです。
これはapacheがシェルスクリプトの出力を受け取ってブラウザに投げるからです。
シェルスクリプトの側ですべきことは、
正確なHTTPヘッダの出力だけということになります。
いかにもUNIXらしい動きです。</p>
<p>　最後、シバン（ <tt class="docutils literal"><span class="pre">#!/bin/bash</span></tt> ）の行にログを出力する <tt class="docutils literal"><span class="pre">-vx</span></tt>
というオプションをつけましたが、このログはどこに行くのか。
実はリスト12のように、apacheのエラーログに行きます。</p>
<ul class="simple">
<li>リスト12: <tt class="docutils literal"><span class="pre">error_log</span></tt> にCGIスクリプトの標準エラー出力がたまる</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat /private/var/log/apache2/error_log
<span class="o">(</span>略<span class="o">)</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> <span class="c">#!/bin/bash -xv</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> <span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/html&quot;</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> + <span class="nb">echo</span> <span class="s1">&#39;Content-Type: text/html&#39;</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> <span class="nb">echo</span> <span class="s2">&quot;&quot;</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> + <span class="nb">echo</span> <span class="s1">&#39;&#39;</span>
<span class="o">[</span>Tue Apr 23 21:46:14 2013<span class="o">]</span> <span class="o">[</span>error<span class="o">]</span> <span class="o">[</span>client ::1<span class="o">]</span> <span class="nb">echo</span> <span class="se">\\x</span>e9<span class="se">\\x</span>ad<span class="se">\\x</span>9a...<span class="o">(</span>略<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>　今挙げたポイントは、別のLL言語でも全く同じ事です。
違うのは、LL言語には便利なライブラリが存在していて、
ウェブサーバとのダイレクトなやりとりがちょっとだけ隠蔽されていることです。
でもまあ、何を使おうが普通のCGIの場合、
最終的にはHTTPでHTMLやjavascriptを出力することになります。</p>
</div>
<div class="section" id="id2">
<h2>19.4. とりあえず何か作ってみましょう<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、シェルスクリプトでCGIスクリプトが作れると分かったので、
さっそくなにか作ってみましょう。
実用的なものは次回以降にまわすとして、
何か面白い物を作ってみましょう。</p>
<p>　まずは、端末からブラウザに文字等を送り込むものを作ってみます。
リスト13のようなシェルスクリプトを作ります。</p>
<ul class="simple">
<li>リスト13: <tt class="docutils literal"><span class="pre">notify.cgi</span></tt></li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat notify.cgi
<span class="c">#!/bin/bash</span>

mkfifo /tmp/pipe
chmod a+w /tmp/pipe

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/html&quot;</span>
<span class="nb">echo</span> <span class="s2">&quot;&quot;</span>
cat /tmp/pipe
rm /tmp/pipe
</pre></div>
</td></tr></table></div>
<p>4行目の <tt class="docutils literal"><span class="pre">mkfifo</span></tt> というコマンドは、
「名前つきパイプ」という特別なファイルを作るコマンドです。
「名前つきパイプ」は、その名のとおりパイプでして、
片方から字を突っ込むと、もう片方から字が出てきます。
例えば、</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo </span>hoge | cat
</pre></div>
</div>
<p>という処理を名前付きパイプで書くとリスト14のようになります。</p>
<ul class="simple">
<li>リスト14: 名前付きパイプを使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>//端末1
<span class="nv">$ </span>cat /tmp/pipe
//端末2
<span class="nv">$ </span><span class="nb">echo </span>hoge &gt; /tmp/pipe
</pre></div>
</td></tr></table></div>
<p>こうすると、端末1の <tt class="docutils literal"><span class="pre">cat</span></tt> は <tt class="docutils literal"><span class="pre">/tmp/pipe</span></tt>
に何か字が流れてくるまで止まった状態になり、
端末2で <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">hoge</span></tt> が実行されたら <tt class="docutils literal"><span class="pre">hoge</span></tt> と出力します。
<tt class="docutils literal"><span class="pre">echo</span> <span class="pre">hoge</span></tt> が終わると、 <tt class="docutils literal"><span class="pre">cat</span></tt> も終わります。
よくよく考えると、この動作は普通のパイプのものと同じです。
ただし、 <tt class="docutils literal"><span class="pre">/tmp/pipe</span></tt> は <tt class="docutils literal"><span class="pre">rm</span></tt> で消さない限り、残ります。</p>
<p>　五行目の <tt class="docutils literal"><span class="pre">chmod</span></tt> は、 <tt class="docutils literal"><span class="pre">/tmp/pipe</span></tt>
の所有者以外でも書き込めるようにするためのパーミッション変更です。</p>
<p>　さて、 <tt class="docutils literal"><span class="pre">notify.cgi</span></tt> をブラウザから呼び出してみましょう。
CGIスクリプトは <tt class="docutils literal"><span class="pre">cat</span> <span class="pre">/tmp/pipe</span></tt> で一旦止まるので、
ブラウザでは待ちの状態になります。</p>
<p>　次に、おもむろに端末からリスト15のように打ってみてください。
（脚注: <tt class="docutils literal"><span class="pre">/tmp/pipe</span></tt> のないときにやってしまうと、
<tt class="docutils literal"><span class="pre">/tmp/pipe</span></tt> という普通のファイルができてしまうので注意してください。）</p>
<ul class="simple">
<li>リスト15: 送り込む文字列</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;&lt;script&gt;alert(&quot;no more XSS!!&quot;)&lt;/script&gt;&#39;</span> &gt; /tmp/pipe
</pre></div>
</td></tr></table></div>
<p>図3のようにアラートが出たら成功です。
何の役にも立たないですが、多分、面白いと思っていただけたかと。</p>
<ul class="simple">
<li>図3: ブラウザでアラートが表示される</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="ALERT.png"><img alt="" src="ALERT.png" style="width: 50%;" /></a>
</div>
<p>　ちなみに、HTTPヘッダがちゃんと意味があるということを示すために、
<tt class="docutils literal"><span class="pre">notify.cgi</span></tt> をリスト2のように書き換えてもう一度やってみます。</p>
<ul class="simple">
<li>リスト16: <tt class="docutils literal"><span class="pre">notify2.cgi</span></tt></li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat notify2.cgi
<span class="c">#!/bin/bash</span>

mkfifo /tmp/pipe
chmod a+w /tmp/pipe

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: text/plain&quot;</span>
<span class="nb">echo</span> <span class="s2">&quot;&quot;</span>
cat /tmp/pipe
rm /tmp/pipe
</pre></div>
</td></tr></table></div>
<p>今度は、ブラウザに
「&lt;script&gt;alert(&#8220;no more XSS&#8221;)&lt;/script&gt;』
と文字列が表示されたと思います。
まともなブラウザならば・・・。</p>
<p>　HTTPヘッダの話が出たので、
最後にファイルのダウンロードでもやってみましょう。
例えばみんな大好きエクセルファイルのダウンロードを行うCGIスクリプトでは、
リスト17のように書けます。</p>
<ul class="simple">
<li>リスト17: ファイルをダウンロードさせるCGIスクリプト</li>
</ul>
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
11</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat download_xlsx.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nv">FILE</span><span class="o">=</span>/tmp/book1.xlsx
<span class="nv">LENGTH</span><span class="o">=</span><span class="k">$(</span>wc -c <span class="nv">$FILE</span> | awk <span class="s1">&#39;{print $1}&#39;</span><span class="k">)</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: application/octet-stream&quot;</span>
<span class="nb">echo</span> <span class="s1">&#39;Content-Disposition: attachment; filename=&quot;hoge.xlsx&quot;&#39;</span>
<span class="nb">echo</span> <span class="s2">&quot;Content-Length: $LENGTH&quot;</span>
<span class="nb">echo</span>
cat <span class="nv">$FILE</span>
</pre></div>
</td></tr></table></div>
<p>7行目の <tt class="docutils literal"><span class="pre">application/octet-stream</span></tt> は、
「バイナリを送り込むぞ」という宣言、
8行目は「 <tt class="docutils literal"><span class="pre">hoge.xlsx</span></tt> という名前で保存してくれ」、
9行目は変数 <tt class="docutils literal"><span class="pre">LENGTH</span></tt> に書いてあるサイズのデータを出力するぞ、
という意味になります。</p>
<p>　そして、実際にファイルをブラウザに向けて発射するのには、
11行目のようにおなじみの <tt class="docutils literal"><span class="pre">cat</span></tt> を使います。
<tt class="docutils literal"><span class="pre">cat</span></tt> はテキストもバイナリも区別しません。
区別してしまうと他のコマンドと連携して使えなくなってしまいます。</p>
<p>　ファイルはありとあらゆるものがダウンロードさせることができますが、
ヘッダについては微妙に変化させます。
例えば、mpegファイルをブラウザに直接見せたいのなら図12のように書きます。</p>
<ul class="simple">
<li>図12: mpegファイルを見せるためのCGIスクリプト</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat download_movie.cgi
<span class="c">#!/bin/bash</span>

<span class="nv">FILE</span><span class="o">=</span>/tmp/japanopen2006_keeper.mpeg
<span class="nv">LENGTH</span><span class="o">=</span><span class="k">$(</span>wc -c <span class="nv">$FILE</span> | awk <span class="s1">&#39;{print $1}&#39;</span><span class="k">)</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-Type: video/mpeg&quot;</span>
<span class="nb">echo</span> <span class="s2">&quot;Content-Length: $LENGTH&quot;</span>
<span class="nb">echo</span>
cat <span class="nv">$FILE</span>
</pre></div>
</td></tr></table></div>
<p>　私の普段使っているブラウザ（MacのGoogle ChromeとFirefox）では、
図13のようにブラウザのプラグインが立ち上がり、
画面内でムービーが再生されます。</p>
<ul class="simple">
<li>図13: ヘッダを適切に書くとブラウザでよしなに取りはからってくれる</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="MOVIE.png"><img alt="" src="MOVIE.png" style="width: 30%;" /></a>
</div>
<p>ヘッダに <tt class="docutils literal"><span class="pre">Content-Disposition:</span> <span class="pre">attachment;</span> <span class="pre">filename=&quot;hoge.mpeg&quot;'</span></tt>
を加えると、ファイルを再生するかファイルに保存するか聞いて来たり、
再生されずにファイルに保存されたりします。
筆者のHTTPヘッダについての知識はこの程度ですが、
もし別の言語でHTTPヘッダを間接的にいじったことのある人は、
シェルスクリプトでも細かい制御ができることでしょう。</p>
</div>
<div class="section" id="id3">
<h2>19.5. おわりに<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はシェルスクリプトでCGIスクリプトを書きました。
特に出力について扱いました。
おそらく今回の内容で一番重要なのは、
apacheを経由してブラウザにコンテンツを送るときには、
標準出力を使うということでしょうか。
ここらあたりにも、インターネットがUNIXと共に発展して来た名残があります。
いや、名残というよりも必然かもしれません。
標準入出力は、これ以上ないくらい抽象化されたインタフェースであり、
まず最初に使用を検討すべきものでしょう。</p>
<p>　次回はCGIスクリプトでのPOST、
GETも絡めて何かを作ってみようと考えています。</p>
</div>
</div>
