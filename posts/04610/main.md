---
Copyright: (C) Ryuichi Ueda
---

# 開眼シェルスクリプト2013年8月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="cgi2"><br />
<h1>20. 開眼シェルスクリプト 第20回 シェルスクリプトでCGIスクリプト2<a class="headerlink" href="#cgi2" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　毎度おなじみ流浪の連載、開眼シェルスクリプトですが、<br />
前回からCGIスクリプトをbashで記述するというお題を扱っています。<br />
実はこの禁断の技は、かつては特別珍しいものではなかったようです。<br />
UNIXの古い方（脚注：言い方がよくないか。）<br />
に話をするとああ懐かしいという言葉が返ってきます。</p><br />
<p>　しかし、懐かしいと言われて喜んでもいられません。<br />
別に古い事を懐古するために連載があるのではありません。<br />
bashでCGIスクリプトを書く技を身につけると、<br />
端末の操作の延長線上でCGIスクリプトを書けるのですから、<br />
実はなかなか便利です。<br />
この伝統芸能が消えないように、<br />
コソコソここに方法を書いておくことにします。</p><br />
<p>　今回は、GETを使ってブラウザからCGIスクリプトに文字を送り込み、<br />
CGIスクリプト側でそれに応じて動的に表示を変えるというお題を扱います。</p><br />
<p>ゲッツ！ &#8212;ダンディー坂野</p><br />
<div class="section" id="id1"><br />
<h2>20.1. 環境等<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回に引き続き、筆者の手元のMacでapacheを起動し、<br />
そこでCGIスクリプトを動かします。<br />
Macでのapacheの設定方法は前回を参照ください。<br />
Linux、BSD等の場合はウェブ等に説明をゆずります。</p><br />
<p>　筆者のMacでは<br />
<tt class="docutils literal"><span class="pre">/Library/WebServer/CGI-Executables/</span></tt><br />
にCGIスクリプトを置くと、<br />
<tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/hoge.cgi</span></tt><br />
などとURLを指定することでCGIスクリプトを起動できます。<br />
前回設定しましたが、<br />
<tt class="docutils literal"><span class="pre">/Library/WebServer/CGI-Executables/</span></tt><br />
にいちいち移動するのは面倒なので、<br />
リスト1のように筆者のアカウントのホーム下に<br />
<tt class="docutils literal"><span class="pre">cgi-bin</span></tt> という名前でシンボリックリンクを張って、<br />
そこにスクリプトを置くようにしました。</p><br />
<ul class="simple"><br />
<li>リスト1: ホームから簡単にアクセスできるようにする（前回からの再掲）</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ln -s /Library/WebServer/CGI-Executables/ ./cgi-bin<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">cd </span>cgi-bin<br />
uedamac:cgi-bin ueda<span class="nv">$ </span>sudo chown ueda:wheel ./<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　今回もバージョンが気になるような特別なことはしませんが、<br />
念のためMacのソフトウェア環境をリスト2に示します。</p><br />
<ul class="simple"><br />
<li>リスト2: 環境</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>bash --version<br />
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span><br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.<br />
uedamac:~ ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.3.0 Darwin Kernel Version 12.3.0: Sun Jan 6 22:37:10 PST 2013; root:xnu-2050.22.13~1/RELEASE_X86_64 x86_64<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>apachectl -v<br />
Server version: Apache/2.2.22 <span class="o">(</span>Unix<span class="o">)</span><br />
Server built: Dec 9 2012 18:57:18<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="get"><br />
<h2>20.2. GETの方法<a class="headerlink" href="#get" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まず最初に、一番簡単なGETから説明します。<br />
GET（GETメソッド）というのは、<br />
HTTPでCGIスクリプトに文字列を渡すための方法の一つです。<br />
ブラウザなどでURLを指定するときに、<br />
後ろに文字列をくっつけてCGIスクリプトにその文字列を送り込む方法です。</p><br />
<p>　リスト3に、シェルスクリプトで実例を示します。</p><br />
<ul class="simple"><br />
<li>リスト3: GETで文字列を受け取り表示するCGIスクリプト</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat echo.cgi<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これを <tt class="docutils literal"><span class="pre">~/cgi-bin/</span></tt> に置いて、<br />
ブラウザから次のように実行します。</p><br />
<ul class="simple"><br />
<li>図1: GETで送った文字列を表示</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="GET.png"><img alt="" src="GET.png" style="width: 40%;" /></a><br />
</div><br />
<p>　これを解説すると、まず、ブラウザに打った文字列</p><br />
<p><tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/echo.cgi?gets!!</span></tt></p><br />
<p>ですが、これは <tt class="docutils literal"><span class="pre">echo.cgi</span></tt> に <tt class="docutils literal"><span class="pre">gets!!</span></tt><br />
という文字列をGETで渡すという意味になります。</p><br />
<p>　文字列を送りつけられたCGIスクリプトの方は、<br />
なんらかの方法でその文字列を受け取らなければなりません。<br />
が、案外簡単で、<br />
<tt class="docutils literal"><span class="pre">QUERY_STRING</span></tt> という変数に入っているのでそれを使うだけです。<br />
ですから、リスト2のようにHTTPヘッダをつけてただ<br />
<tt class="docutils literal"><span class="pre">echo</span></tt> するだけで、<br />
ブラウザにむけてGETで受け取った文字列を出力できます。</p><br />
<p>　変数 <tt class="docutils literal"><span class="pre">QUERY_STRING</span></tt> を使うときは、<br />
よほど特殊な事情がない限り、<br />
6行目のようにダブルクォートで囲みます。<br />
囲まないと、次のようになってしまいます。</p><br />
<ul class="simple"><br />
<li>図2: <tt class="docutils literal"><span class="pre">$QUERY_STRING</span></tt> のダブルクォートを除いて <tt class="docutils literal"><span class="pre">*</span></tt> を送り込む</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="WILD.png"><img alt="" src="WILD.png" style="width: 40%;" /></a><br />
</div><br />
<p>これは、端末上でのルールと同じです。<br />
リスト4のように端末で実験すると理解できるはずです。</p><br />
<ul class="simple"><br />
<li>リスト4: 端末上でのクォート有無の実験</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>//「*」を変数Aにセット<br />
uedamac:cgi-bin ueda<span class="nv">$ A</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><br />
//クォートしない<br />
uedamac:cgi-bin ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$A</span><br />
dame.cgi download_xlsx.cgi ...<span class="o">(</span>略<span class="o">)</span><br />
//クォート<br />
uedamac:cgi-bin ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;$A&quot;</span><br />
*<br />
</pre></div><br />
</td></tr></table></div><br />
<p>シェルスクリプトでCGIスクリプトを書くときは、<br />
良くも悪くもシステムと密着していることを忘れてはいけません。</p><br />
<p>　ただ、コマンドをインジェクションされるということに、<br />
あまりビビってもいけません。<br />
たとえ <tt class="docutils literal"><span class="pre">$QUERY_STRING</span></tt> のクォートが無くても、<br />
<tt class="docutils literal"><span class="pre">echo</span></tt> の後ろの変数はただ文字列に変換されるだけで実行はされません。</p><br />
<ul class="simple"><br />
<li>図3: セミコロンの後ろにコマンドをインジェクション</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="RM.png"><img alt="" src="RM.png" style="width: 40%;" /></a><br />
</div><br />
<p>　逆にまずいパターンをリスト5に挙げておきます。<br />
まずいというより、問題外ですが・・・。<br />
この例のように、<br />
クォートしたからと言って安全というわけではありません。</p><br />
<ul class="simple"><br />
<li>リスト5: GETで受けた文字列を実行してしまうパターン</li><br />
</ul><br />
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
28</pre></div></td><td class="code"><div class="highlight"><pre>//その1:変数が行頭に来ている<br />
uedamac:cgi-bin ueda<span class="nv">$ </span>cat yabai1.cgi<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
<span class="s2">&quot;$QUERY_STRING&quot;</span><br />
<br />
//コマンドが実行できる<br />
uedamac:~ ueda<span class="nv">$ </span>curl http://localhost/cgi-bin/yabai1.cgi?ls<br />
dame.cgi<br />
download_xlsx.cgi<br />
echo.cgi<br />
...<br />
<br />
//evalを使う<br />
uedamac:cgi-bin ueda<span class="nv">$ </span>cat yabai2.cgi<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
<span class="nb">eval</span> <span class="s2">&quot;$QUERY_STRING&quot;</span><br />
//コマンドが実行できる<br />
uedamac:cgi-bin ueda<span class="nv">$ </span>curl http://localhost/cgi-bin/yabai2.cgi?ls<br />
dame.cgi<br />
download_xlsx.cgi<br />
echo.cgi<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>他にもいろいろまずい書き方はありますが、<br />
今回の内容はこれくらい知っておいて予防しておけば大丈夫です。<br />
もちろん閉じた環境で実験するには何も気にする必要はありません。<br />
筆者は、セキュリティーレベルはウェブサイトの<br />
用途次第で変えるべきだという立場ですので、<br />
これくらいにして次に行きます。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>20.3. コマンドを選んで結果を表示<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、ここからはGETを使って作り物をしてみましょう。<br />
ここで作るのはサーバ監理用のウェブページです。<br />
ページからコマンドを呼び出すことができるCGIスクリプトを作ります。<br />
以前も（第4回、第5回）、<br />
HTMLを出力するシェルスクリプトを作ったことはありました。<br />
しかし、今回はHTMLを作り置きするのではなく、<br />
CGIシェルスクリプトに動的にHTMLを生成させる点が違います。</p><br />
<p>　まず、リスト6のhtmlファイルを作ります。<br />
これをCGIスクリプトで読み込み、<br />
<tt class="docutils literal"><span class="pre">sed</span></tt> 等で加工することで動的にHTMLを出力します。</p><br />
<ul class="simple"><br />
<li>リスト6: <tt class="docutils literal"><span class="pre">com.html</span></tt></li><br />
</ul><br />
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
21</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.html<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
 &lt;head&gt;<br />
 &lt;meta <span class="nv">charset</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span> /&gt;<br />
 &lt;title&gt;オレオレマシーン情報&lt;/title&gt;<br />
 &lt;/head&gt;<br />
 &lt;body&gt;<br />
 &lt;form <span class="nv">name</span><span class="o">=</span><span class="s2">&quot;FORM&quot;</span> <span class="nv">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span> <span class="nv">action</span><span class="o">=</span><span class="s2">&quot;./com.cgi&quot;</span>&gt;<br />
 コマンド：<br />
 &lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;0&quot;</span>&gt;cat /etc/hosts&lt;/option&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;1&quot;</span>&gt;top -l 1&lt;/option&gt;<br />
 &lt;/select&gt;<br />
 &lt;input <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;submit&quot;</span> <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;ポチ&quot;</span> /&gt;<br />
 &lt;/form&gt;<br />
 &lt;pre&gt;<br />
&lt;!--RESULT--&gt;<br />
 &lt;/pre&gt;<br />
 &lt;/body&gt;<br />
&lt;/html&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>次にリスト7のCGIスクリプトを用意し、<br />
このhtmlファイルを表示します。<br />
デバッグ用に、<br />
後ろの方で <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">&quot;$QUERY_STRING&quot;</span></tt> しておきます。<br />
htmlが終わった後の出力になるので邪道ですが、<br />
ブラウザには表示されます。</p><br />
<ul class="simple"><br />
<li>リスト7: <tt class="docutils literal"><span class="pre">com.cgi</span></tt></li><br />
</ul><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.cgi<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html<br />
<br />
<span class="c">###表示</span><br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
cat <span class="nv">$htmlfile</span><br />
<br />
<span class="c">#デバッグ用</span><br />
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これでブラウザから <tt class="docutils literal"><span class="pre">com.cgi</span></tt> を呼び出し、<br />
セレクトボックスから項目を選び、<br />
ボタンを押してみてください。<br />
図4のように左下にGETで送った文字列が表示されるはずです。</p><br />
<ul class="simple"><br />
<li>図4: フォームで送信される文字列</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="COM.png"><img alt="" src="COM.png" style="width: 40%;" /></a><br />
</div><br />
</div><br />
<div class="section" id="html"><br />
<h2>20.4. リストをHTMLにはめ込む<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、図4の <tt class="docutils literal"><span class="pre">COM=1</span></tt> ですが、<br />
<tt class="docutils literal"><span class="pre">COM</span></tt> というのは、セレクトボックスについた名前<br />
（ <tt class="docutils literal"><span class="pre">com.html</span></tt> の <tt class="docutils literal"><span class="pre">name=&quot;COM&quot;</span></tt> の部分）、<br />
<tt class="docutils literal"><span class="pre">=</span></tt> より右側は、選んだ項目の <tt class="docutils literal"><span class="pre">value</span></tt> の値です。<br />
valueの値から、ブラウザでどの項目が選ばれたか分かるので、<br />
セレクトボックスに書かれたコマンドをそのまま実行すればよいということになります。<br />
番号とコマンドの対応表のファイルをどこかに置いておけばよいでしょう。<br />
また、今のところ、 <tt class="docutils literal"><span class="pre">com.html</span></tt> に直接コマンドを書いていますが、<br />
対応表のファイルの内容を動的に反映させた方がよいでしょう。</p><br />
<p>　このとき、open usp Tukubaiの <tt class="docutils literal"><span class="pre">mojihame</span></tt> というコマンドを使います。<br />
まず、 <tt class="docutils literal"><span class="pre">com.html</span></tt> を次のように書き換えます。</p><br />
<ul class="simple"><br />
<li>リスト7: <tt class="docutils literal"><span class="pre">mojihame</span></tt> に対応した <tt class="docutils literal"><span class="pre">com.html</span></tt></li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>&lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;<br />
&lt;!--COMLIST--&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;%1&quot;</span>&gt;%2&lt;/option&gt;<br />
&lt;!--COMLIST--&gt;<br />
&lt;/select&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>次に、 <tt class="docutils literal"><span class="pre">com.cgi</span></tt> をリスト8のように書き換えます。<br />
これで、ブラウザには <tt class="docutils literal"><span class="pre">$tmp-list</span></tt> に書かれたコマンドが<br />
番号（行番号）をつけられてセレクトボックスにセットされます。<br />
コマンドのリストは外部のファイルでもよいのですが、<br />
説明のためにヒアドキュメントで作っています。</p><br />
<p>　先にリスト8について、本題と関係ない細かい部分を説明しておくと、<br />
リスト2行目の <tt class="docutils literal"><span class="pre">-vx</span></tt> はシェルスクリプトの実行ログの<br />
出力を行うためのオプションです。<br />
4行目の <tt class="docutils literal"><span class="pre">exec</span> <span class="pre">2&gt;</span></tt> は、このスクリプトのエラー出力を<br />
ファイルにリダイレクトするためのコマンドです。<br />
11行目から14行目のヒアドキュメントは、<br />
<tt class="docutils literal"><span class="pre">FIN</span></tt> と <tt class="docutils literal"><span class="pre">FIN</span></tt> の間に書いたものを<br />
標準出力に出力するという動きをします。<br />
<tt class="docutils literal"><span class="pre">FIN</span></tt> は、始めと終わりで対になっていれば、<br />
別に <tt class="docutils literal"><span class="pre">EOF</span></tt> とか <tt class="docutils literal"><span class="pre">HOGE</span></tt> とかでも動きます。</p><br />
<ul class="simple"><br />
<li>リスト8: コマンドのリストを <tt class="docutils literal"><span class="pre">com.html</span></tt> にはめ込むための <tt class="docutils literal"><span class="pre">com.cgi</span></tt></li><br />
</ul><br />
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
29</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.cgi<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nb">exec </span>2&gt; /tmp/log<br />
<br />
<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:<span class="nv">$PATH</span><br />
<br />
<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
cat <span class="s">&lt;&lt; FIN &gt; $tmp-list</span><br />
<span class="s">cat /etc/hosts</span><br />
<span class="s">top -l 1</span><br />
<span class="s">echo test_test _</span><br />
<span class="s">FIN</span><br />
<br />
<span class="c">###表示</span><br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> <span class="nv">$tmp</span>-list |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;_&#39;</span> |<br />
awk <span class="s1">&#39;{print NR,$1}&#39;</span> |<br />
mojihame -lCOMLIST <span class="nv">$htmlfile</span> -<br />
<br />
<span class="c">#デバッグ用</span><br />
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span><br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">mojihame</span></tt> の部分だけ抜き出すと、まず、<br />
22行目の <tt class="docutils literal"><span class="pre">awk</span></tt> の後のパイプにはリスト9のようなデータが流れます。<br />
行番号 がついて、スペースは <tt class="docutils literal"><span class="pre">_</span></tt> 、 <tt class="docutils literal"><span class="pre">_</span></tt> は <tt class="docutils literal"><span class="pre">\\_</span></tt><br />
にエスケープされます。<br />
open usp Tukubaiのコマンドは空白区切りのデータを受け付けるので、<br />
それに合わせてデータを変換してやらなくてはいけません。</p><br />
<ul class="simple"><br />
<li>リスト9: エスケープ後のコマンドのリスト</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>1 cat_/etc/hosts<br />
2 top_-l_1<br />
3 echo_test<span class="se">\\_</span>test_<span class="se">\\_</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これで2列のデータになります。<br />
これを <tt class="docutils literal"><span class="pre">mojihame</span></tt> に入力すると、<br />
<tt class="docutils literal"><span class="pre">COMLIST</span></tt> で挟まれた部分がレコードの数だけ複製され、<br />
1列目がリスト&#64;&#64;&#64;の <tt class="docutils literal"><span class="pre">%1</span></tt> 、<br />
2列目がリスト&#64;&#64;&#64;の <tt class="docutils literal"><span class="pre">%2</span></tt> 、にはめ込まれます。<br />
エスケープされた文字は戻ります。<br />
<tt class="docutils literal"><span class="pre">mojihame</span></tt> が出力するHTMLのうち、<br />
セレクトボックスの部分をリスト10に示します。</p><br />
<ul class="simple"><br />
<li>リスト10: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> が出力するHTMLの一部</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>&lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;1&quot;</span>&gt;cat /etc/hosts&lt;/option&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;2&quot;</span>&gt;top -l 1&lt;/option&gt;<br />
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;3&quot;</span>&gt;echo test_test _&lt;/option&gt;<br />
&lt;/select&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">mojihame</span></tt> は慣れると便利です。<br />
が、頑張る人は <tt class="docutils literal"><span class="pre">awk</span></tt> でもHTMLの部品は作れます。</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>20.5. 再度、インジェクションに注意<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　ここでもう一回注意があります。<br />
<tt class="docutils literal"><span class="pre">com.cgi</span></tt> はセレクトボックスから数字を受け取りますが、<br />
数字だけしか受け取れないわけではありません。<br />
リスト11のように <tt class="docutils literal"><span class="pre">curl</span></tt> 等を使っても、<br />
ブラウザでURLの後ろを細工しても邪悪な文字列を送る事ができます。</p><br />
<ul class="simple"><br />
<li>リスト11: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> に直接GETでデータを渡す</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>curl <span class="s2">&quot;http://localhost/cgi-bin/com.cgi?reboot&quot;</span><br />
（略）<br />
&lt;/html&gt;<br />
reboot<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この対策もなかなか面倒なのですが、<br />
今回の例だと単に数字しか受け付けなければよいので、<br />
<tt class="docutils literal"><span class="pre">tr</span></tt> を使って次のようにGETされた文字列を受け取ります。<br />
<tt class="docutils literal"><span class="pre">tmp=/tmp/$$</span></tt> の行の下あたりに、</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span><span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span> | tr -dc <span class="s1">&#39;0-9&#39;</span><span class="k">)</span><br />
</pre></div><br />
</div><br />
<p>と付け足します。 <tt class="docutils literal"><span class="pre">tr</span></tt> のオプション <tt class="docutils literal"><span class="pre">-d</span></tt><br />
は文字（この例では0から9までの数字）を消すという意味ですが、<br />
<tt class="docutils literal"><span class="pre">-c</span></tt> をつけると意味が反転します。<br />
ですので、リスト12のような挙動を示します。<br />
UTF-8なら日本語が混ざっても問題ありません。</p><br />
<ul class="simple"><br />
<li>リスト12: <tt class="docutils literal"><span class="pre">tr</span></tt> で、指定の文字「以外」を削除</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda$ echo &#39;COM=1aewagああ2&#39; | tr -dc &#39;0-9&#39;<br />
12uedamac:~ ueda$<br />
//↑ 1と2だけ残る<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このように12だけ残ります。改行すら消えます。<br />
これで行番号が変数 <tt class="docutils literal"><span class="pre">NUM</span></tt> に入るので、<br />
あとはリストのコマンドを実行するだけです。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>20.6. 完成<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　完成した <tt class="docutils literal"><span class="pre">com.cgi</span></tt> をリスト13に示します。<br />
変数に文字列が入っていなかったり、<br />
中間ファイルができなかったりというところでバグが出るので、<br />
多少慣れが必要です。<br />
例えば、 <tt class="docutils literal"><span class="pre">COM</span></tt> にコマンドが入らないと23行目でエラーが出るので、<br />
21行目で <tt class="docutils literal"><span class="pre">COM</span></tt> に <tt class="docutils literal"><span class="pre">:</span></tt> （なにもしないコマンド）を入れるなど、<br />
細かい芸が必要です。しかし、行数は短くなりますので、<br />
<em>慣れると</em> さっさと何か試作したり、<br />
USP友の会のサイト（<a class="reference external" href="http://www.usptomo.com">http://www.usptomo.com</a>）<br />
のように見栄えのよいものも早く作れるようになります。</p><br />
<ul class="simple"><br />
<li>リスト13: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> 完成品</li><br />
</ul><br />
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -xv</span><br />
<span class="nb">exec </span>2&gt; /tmp/log<br />
<br />
<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:<span class="nv">$PATH</span><br />
<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
<span class="c">######実行可能コマンドリスト######</span><br />
cat <span class="s">&lt;&lt; FIN &gt; $tmp-list</span><br />
<span class="s">cat /etc/hosts</span><br />
<span class="s">top -l 1</span><br />
<span class="s">echo test_test _</span><br />
<span class="s">FIN</span><br />
<br />
<span class="c">######コマンドの実行######</span><br />
<span class="c">#番号受け取り</span><br />
<span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span><span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span> | tr -dc <span class="s1">&#39;0-9&#39;</span><span class="k">)</span><br />
<span class="c">#指定された行を取得</span><br />
<span class="nv">COM</span><span class="o">=</span><span class="k">$(</span>awk -v <span class="nv">n</span><span class="o">=</span><span class="s2">&quot;$NUM&quot;</span> <span class="s1">&#39;NR==n&#39;</span> <span class="nv">$tmp</span>-list<span class="k">)</span><br />
<span class="c">#COMが空なら : を入れておく</span><br />
<span class="o">[</span> -z <span class="s2">&quot;$COM&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nv">COM</span><span class="o">=</span><span class="s2">&quot;:&quot;</span><br />
<span class="c">#実行</span><br />
<span class="nv">$COM</span> &gt; <span class="nv">$tmp</span>-result<br />
<br />
<span class="c">######HTML出力######</span><br />
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span><br />
<span class="nb">echo</span><br />
<span class="c">#エスケープ処理</span><br />
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> <span class="nv">$tmp</span>-list |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;_&#39;</span> |<br />
<span class="c">#行番号をつける</span><br />
awk <span class="s1">&#39;{print NR,$1}&#39;</span> |<br />
<span class="c">#出力 &gt;&gt;&gt; 1:行番号 2:コマンド</span><br />
mojihame -lCOMLIST <span class="nv">$htmlfile</span> - |<br />
<span class="c">#コマンド実行結果をはめ込み</span><br />
filehame -lRESULT - <span class="nv">$tmp</span>-result<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　完成品では、もう一つ <tt class="docutils literal"><span class="pre">filehame</span></tt> というコマンドを使いました。<br />
これは、あるファイルの間に別のファイルの中身を差し込むコマンドで、<br />
次のように使います。</p><br />
<ul class="simple"><br />
<li>リスト14: <tt class="docutils literal"><span class="pre">filehame</span></tt> の使い方</li><br />
</ul><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat <span class="nv">file1</span><br />
<span class="o">===</span>参加者<span class="o">===</span><br />
<span class="nv">ATT</span><br />
<span class="o">===</span>以上<span class="o">===</span><br />
uedamac:cgi-bin ueda<span class="nv">$ </span>cat meibo<br />
山田<br />
里中<br />
殿間<br />
uedamac:cgi-bin ueda<span class="nv">$ </span>filehame -lATT file1 <span class="nv">meibo</span><br />
<span class="o">===</span>参加者<span class="o">===</span><br />
山田<br />
里中<br />
殿間<br />
<span class="o">===</span>以上<span class="o">===</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これも頑張って <tt class="docutils literal"><span class="pre">sed</span></tt> を使えば同様の処理はできます。</p><br />
<p>　最後に実行結果を図5に示します。</p><br />
<ul class="simple"><br />
<li>図5: 実行結果</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="RESULT.png"><img alt="" src="RESULT.png" style="width: 40%;" /></a><br />
</div><br />
<p>　ボタンを押すとセレクトボックスの選択結果が戻ってしまいますが、<br />
これもコマンドで対応できます。<br />
open usp Tukubaiの <tt class="docutils literal"><span class="pre">formhame</span></tt> というコマンドを使いますが、<br />
その説明は、チャンスがあれば次回以降ということで。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>20.7. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はGETを使ってCGIスクリプトに字を送り込む方法を説明し、<br />
ブラウザからコマンドを実行するアプリケーションを作りました。<br />
<tt class="docutils literal"><span class="pre">com.html</span></tt> と <tt class="docutils literal"><span class="pre">com.cgi</span></tt> を合わせても60行程度ですので、<br />
いつも端末を叩いたりシェルスクリプトを書いたりしている人が覚えておくと、<br />
特に何か試作するときに威力を発揮することでしょう。</p><br />
</div><br />
</div>
