---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年8月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="cgi2">
<h1>20. 開眼シェルスクリプト 第20回 シェルスクリプトでCGIスクリプト2<a class="headerlink" href="#cgi2" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　毎度おなじみ流浪の連載、開眼シェルスクリプトですが、
前回からCGIスクリプトをbashで記述するというお題を扱っています。
実はこの禁断の技は、かつては特別珍しいものではなかったようです。
UNIXの古い方（脚注：言い方がよくないか。）
に話をするとああ懐かしいという言葉が返ってきます。</p>
<p>　しかし、懐かしいと言われて喜んでもいられません。
別に古い事を懐古するために連載があるのではありません。
bashでCGIスクリプトを書く技を身につけると、
端末の操作の延長線上でCGIスクリプトを書けるのですから、
実はなかなか便利です。
この伝統芸能が消えないように、
コソコソここに方法を書いておくことにします。</p>
<p>　今回は、GETを使ってブラウザからCGIスクリプトに文字を送り込み、
CGIスクリプト側でそれに応じて動的に表示を変えるというお題を扱います。</p>
<p>ゲッツ！ &#8212;ダンディー坂野</p>
<div class="section" id="id1">
<h2>20.1. 環境等<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回に引き続き、筆者の手元のMacでapacheを起動し、
そこでCGIスクリプトを動かします。
Macでのapacheの設定方法は前回を参照ください。
Linux、BSD等の場合はウェブ等に説明をゆずります。</p>
<p>　筆者のMacでは
<tt class="docutils literal"><span class="pre">/Library/WebServer/CGI-Executables/</span></tt>
にCGIスクリプトを置くと、
<tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/hoge.cgi</span></tt>
などとURLを指定することでCGIスクリプトを起動できます。
前回設定しましたが、
<tt class="docutils literal"><span class="pre">/Library/WebServer/CGI-Executables/</span></tt>
にいちいち移動するのは面倒なので、
リスト1のように筆者のアカウントのホーム下に
<tt class="docutils literal"><span class="pre">cgi-bin</span></tt> という名前でシンボリックリンクを張って、
そこにスクリプトを置くようにしました。</p>
<ul class="simple">
<li>リスト1: ホームから簡単にアクセスできるようにする（前回からの再掲）</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ln -s /Library/WebServer/CGI-Executables/ ./cgi-bin
uedamac:~ ueda<span class="nv">$ </span><span class="nb">cd </span>cgi-bin
uedamac:cgi-bin ueda<span class="nv">$ </span>sudo chown ueda:wheel ./
</pre></div>
</td></tr></table></div>
<p>　今回もバージョンが気になるような特別なことはしませんが、
念のためMacのソフトウェア環境をリスト2に示します。</p>
<ul class="simple">
<li>リスト2: 環境</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>bash --version
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span>
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.
uedamac:~ ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.3.0 Darwin Kernel Version 12.3.0: Sun Jan 6 22:37:10 PST 2013; root:xnu-2050.22.13~1/RELEASE_X86_64 x86_64
uedamac:SD_GENKOU ueda<span class="nv">$ </span>apachectl -v
Server version: Apache/2.2.22 <span class="o">(</span>Unix<span class="o">)</span>
Server built: Dec 9 2012 18:57:18
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="get">
<h2>20.2. GETの方法<a class="headerlink" href="#get" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まず最初に、一番簡単なGETから説明します。
GET（GETメソッド）というのは、
HTTPでCGIスクリプトに文字列を渡すための方法の一つです。
ブラウザなどでURLを指定するときに、
後ろに文字列をくっつけてCGIスクリプトにその文字列を送り込む方法です。</p>
<p>　リスト3に、シェルスクリプトで実例を示します。</p>
<ul class="simple">
<li>リスト3: GETで文字列を受け取り表示するCGIスクリプト</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat echo.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span>
</pre></div>
</td></tr></table></div>
<p>これを <tt class="docutils literal"><span class="pre">~/cgi-bin/</span></tt> に置いて、
ブラウザから次のように実行します。</p>
<ul class="simple">
<li>図1: GETで送った文字列を表示</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="GET.png"><img alt="" src="GET.png" style="width: 40%;" /></a>
</div>
<p>　これを解説すると、まず、ブラウザに打った文字列</p>
<p><tt class="docutils literal"><span class="pre">http://localhost/cgi-bin/echo.cgi?gets!!</span></tt></p>
<p>ですが、これは <tt class="docutils literal"><span class="pre">echo.cgi</span></tt> に <tt class="docutils literal"><span class="pre">gets!!</span></tt>
という文字列をGETで渡すという意味になります。</p>
<p>　文字列を送りつけられたCGIスクリプトの方は、
なんらかの方法でその文字列を受け取らなければなりません。
が、案外簡単で、
<tt class="docutils literal"><span class="pre">QUERY_STRING</span></tt> という変数に入っているのでそれを使うだけです。
ですから、リスト2のようにHTTPヘッダをつけてただ
<tt class="docutils literal"><span class="pre">echo</span></tt> するだけで、
ブラウザにむけてGETで受け取った文字列を出力できます。</p>
<p>　変数 <tt class="docutils literal"><span class="pre">QUERY_STRING</span></tt> を使うときは、
よほど特殊な事情がない限り、
6行目のようにダブルクォートで囲みます。
囲まないと、次のようになってしまいます。</p>
<ul class="simple">
<li>図2: <tt class="docutils literal"><span class="pre">$QUERY_STRING</span></tt> のダブルクォートを除いて <tt class="docutils literal"><span class="pre">*</span></tt> を送り込む</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="WILD.png"><img alt="" src="WILD.png" style="width: 40%;" /></a>
</div>
<p>これは、端末上でのルールと同じです。
リスト4のように端末で実験すると理解できるはずです。</p>
<ul class="simple">
<li>リスト4: 端末上でのクォート有無の実験</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>//「*」を変数Aにセット
uedamac:cgi-bin ueda<span class="nv">$ A</span><span class="o">=</span><span class="s2">&quot;*&quot;</span>
//クォートしない
uedamac:cgi-bin ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$A</span>
dame.cgi download_xlsx.cgi ...<span class="o">(</span>略<span class="o">)</span>
//クォート
uedamac:cgi-bin ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;$A&quot;</span>
*
</pre></div>
</td></tr></table></div>
<p>シェルスクリプトでCGIスクリプトを書くときは、
良くも悪くもシステムと密着していることを忘れてはいけません。</p>
<p>　ただ、コマンドをインジェクションされるということに、
あまりビビってもいけません。
たとえ <tt class="docutils literal"><span class="pre">$QUERY_STRING</span></tt> のクォートが無くても、
<tt class="docutils literal"><span class="pre">echo</span></tt> の後ろの変数はただ文字列に変換されるだけで実行はされません。</p>
<ul class="simple">
<li>図3: セミコロンの後ろにコマンドをインジェクション</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="RM.png"><img alt="" src="RM.png" style="width: 40%;" /></a>
</div>
<p>　逆にまずいパターンをリスト5に挙げておきます。
まずいというより、問題外ですが・・・。
この例のように、
クォートしたからと言って安全というわけではありません。</p>
<ul class="simple">
<li>リスト5: GETで受けた文字列を実行してしまうパターン</li>
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
28</pre></div></td><td class="code"><div class="highlight"><pre>//その1:変数が行頭に来ている
uedamac:cgi-bin ueda<span class="nv">$ </span>cat yabai1.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
<span class="s2">&quot;$QUERY_STRING&quot;</span>

//コマンドが実行できる
uedamac:~ ueda<span class="nv">$ </span>curl http://localhost/cgi-bin/yabai1.cgi?ls
dame.cgi
download_xlsx.cgi
echo.cgi
...

//evalを使う
uedamac:cgi-bin ueda<span class="nv">$ </span>cat yabai2.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
<span class="nb">eval</span> <span class="s2">&quot;$QUERY_STRING&quot;</span>
//コマンドが実行できる
uedamac:cgi-bin ueda<span class="nv">$ </span>curl http://localhost/cgi-bin/yabai2.cgi?ls
dame.cgi
download_xlsx.cgi
echo.cgi
...
</pre></div>
</td></tr></table></div>
<p>他にもいろいろまずい書き方はありますが、
今回の内容はこれくらい知っておいて予防しておけば大丈夫です。
もちろん閉じた環境で実験するには何も気にする必要はありません。
筆者は、セキュリティーレベルはウェブサイトの
用途次第で変えるべきだという立場ですので、
これくらいにして次に行きます。</p>
</div>
<div class="section" id="id2">
<h2>20.3. コマンドを選んで結果を表示<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、ここからはGETを使って作り物をしてみましょう。
ここで作るのはサーバ監理用のウェブページです。
ページからコマンドを呼び出すことができるCGIスクリプトを作ります。
以前も（第4回、第5回）、
HTMLを出力するシェルスクリプトを作ったことはありました。
しかし、今回はHTMLを作り置きするのではなく、
CGIシェルスクリプトに動的にHTMLを生成させる点が違います。</p>
<p>　まず、リスト6のhtmlファイルを作ります。
これをCGIスクリプトで読み込み、
<tt class="docutils literal"><span class="pre">sed</span></tt> 等で加工することで動的にHTMLを出力します。</p>
<ul class="simple">
<li>リスト6: <tt class="docutils literal"><span class="pre">com.html</span></tt></li>
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
21</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
 &lt;head&gt;
 &lt;meta <span class="nv">charset</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span> /&gt;
 &lt;title&gt;オレオレマシーン情報&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;form <span class="nv">name</span><span class="o">=</span><span class="s2">&quot;FORM&quot;</span> <span class="nv">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span> <span class="nv">action</span><span class="o">=</span><span class="s2">&quot;./com.cgi&quot;</span>&gt;
 コマンド：
 &lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;0&quot;</span>&gt;cat /etc/hosts&lt;/option&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;1&quot;</span>&gt;top -l 1&lt;/option&gt;
 &lt;/select&gt;
 &lt;input <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;submit&quot;</span> <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;ポチ&quot;</span> /&gt;
 &lt;/form&gt;
 &lt;pre&gt;
&lt;!--RESULT--&gt;
 &lt;/pre&gt;
 &lt;/body&gt;
&lt;/html&gt;
</pre></div>
</td></tr></table></div>
<p>次にリスト7のCGIスクリプトを用意し、
このhtmlファイルを表示します。
デバッグ用に、
後ろの方で <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">&quot;$QUERY_STRING&quot;</span></tt> しておきます。
htmlが終わった後の出力になるので邪道ですが、
ブラウザには表示されます。</p>
<ul class="simple">
<li>リスト7: <tt class="docutils literal"><span class="pre">com.cgi</span></tt></li>
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
11
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html

<span class="c">###表示</span>
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
cat <span class="nv">$htmlfile</span>

<span class="c">#デバッグ用</span>
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span>
</pre></div>
</td></tr></table></div>
<p>これでブラウザから <tt class="docutils literal"><span class="pre">com.cgi</span></tt> を呼び出し、
セレクトボックスから項目を選び、
ボタンを押してみてください。
図4のように左下にGETで送った文字列が表示されるはずです。</p>
<ul class="simple">
<li>図4: フォームで送信される文字列</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="COM.png"><img alt="" src="COM.png" style="width: 40%;" /></a>
</div>
</div>
<div class="section" id="html">
<h2>20.4. リストをHTMLにはめ込む<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、図4の <tt class="docutils literal"><span class="pre">COM=1</span></tt> ですが、
<tt class="docutils literal"><span class="pre">COM</span></tt> というのは、セレクトボックスについた名前
（ <tt class="docutils literal"><span class="pre">com.html</span></tt> の <tt class="docutils literal"><span class="pre">name=&quot;COM&quot;</span></tt> の部分）、
<tt class="docutils literal"><span class="pre">=</span></tt> より右側は、選んだ項目の <tt class="docutils literal"><span class="pre">value</span></tt> の値です。
valueの値から、ブラウザでどの項目が選ばれたか分かるので、
セレクトボックスに書かれたコマンドをそのまま実行すればよいということになります。
番号とコマンドの対応表のファイルをどこかに置いておけばよいでしょう。
また、今のところ、 <tt class="docutils literal"><span class="pre">com.html</span></tt> に直接コマンドを書いていますが、
対応表のファイルの内容を動的に反映させた方がよいでしょう。</p>
<p>　このとき、open usp Tukubaiの <tt class="docutils literal"><span class="pre">mojihame</span></tt> というコマンドを使います。
まず、 <tt class="docutils literal"><span class="pre">com.html</span></tt> を次のように書き換えます。</p>
<ul class="simple">
<li>リスト7: <tt class="docutils literal"><span class="pre">mojihame</span></tt> に対応した <tt class="docutils literal"><span class="pre">com.html</span></tt></li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>&lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;
&lt;!--COMLIST--&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;%1&quot;</span>&gt;%2&lt;/option&gt;
&lt;!--COMLIST--&gt;
&lt;/select&gt;
</pre></div>
</td></tr></table></div>
<p>次に、 <tt class="docutils literal"><span class="pre">com.cgi</span></tt> をリスト8のように書き換えます。
これで、ブラウザには <tt class="docutils literal"><span class="pre">$tmp-list</span></tt> に書かれたコマンドが
番号（行番号）をつけられてセレクトボックスにセットされます。
コマンドのリストは外部のファイルでもよいのですが、
説明のためにヒアドキュメントで作っています。</p>
<p>　先にリスト8について、本題と関係ない細かい部分を説明しておくと、
リスト2行目の <tt class="docutils literal"><span class="pre">-vx</span></tt> はシェルスクリプトの実行ログの
出力を行うためのオプションです。
4行目の <tt class="docutils literal"><span class="pre">exec</span> <span class="pre">2&gt;</span></tt> は、このスクリプトのエラー出力を
ファイルにリダイレクトするためのコマンドです。
11行目から14行目のヒアドキュメントは、
<tt class="docutils literal"><span class="pre">FIN</span></tt> と <tt class="docutils literal"><span class="pre">FIN</span></tt> の間に書いたものを
標準出力に出力するという動きをします。
<tt class="docutils literal"><span class="pre">FIN</span></tt> は、始めと終わりで対になっていれば、
別に <tt class="docutils literal"><span class="pre">EOF</span></tt> とか <tt class="docutils literal"><span class="pre">HOGE</span></tt> とかでも動きます。</p>
<ul class="simple">
<li>リスト8: コマンドのリストを <tt class="docutils literal"><span class="pre">com.html</span></tt> にはめ込むための <tt class="docutils literal"><span class="pre">com.cgi</span></tt></li>
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
29</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat com.cgi
<span class="c">#!/bin/bash -xv</span>

<span class="nb">exec </span>2&gt; /tmp/log

<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:<span class="nv">$PATH</span>

<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

cat <span class="s">&lt;&lt; FIN &gt; $tmp-list</span>
<span class="s">cat /etc/hosts</span>
<span class="s">top -l 1</span>
<span class="s">echo test_test _</span>
<span class="s">FIN</span>

<span class="c">###表示</span>
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> <span class="nv">$tmp</span>-list |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;_&#39;</span> |
awk <span class="s1">&#39;{print NR,$1}&#39;</span> |
mojihame -lCOMLIST <span class="nv">$htmlfile</span> -

<span class="c">#デバッグ用</span>
<span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span>

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">mojihame</span></tt> の部分だけ抜き出すと、まず、
22行目の <tt class="docutils literal"><span class="pre">awk</span></tt> の後のパイプにはリスト9のようなデータが流れます。
行番号 がついて、スペースは <tt class="docutils literal"><span class="pre">_</span></tt> 、 <tt class="docutils literal"><span class="pre">_</span></tt> は <tt class="docutils literal"><span class="pre">\\_</span></tt>
にエスケープされます。
open usp Tukubaiのコマンドは空白区切りのデータを受け付けるので、
それに合わせてデータを変換してやらなくてはいけません。</p>
<ul class="simple">
<li>リスト9: エスケープ後のコマンドのリスト</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>1 cat_/etc/hosts
2 top_-l_1
3 echo_test<span class="se">\\_</span>test_<span class="se">\\_</span>
</pre></div>
</td></tr></table></div>
<p>これで2列のデータになります。
これを <tt class="docutils literal"><span class="pre">mojihame</span></tt> に入力すると、
<tt class="docutils literal"><span class="pre">COMLIST</span></tt> で挟まれた部分がレコードの数だけ複製され、
1列目がリスト&#64;&#64;&#64;の <tt class="docutils literal"><span class="pre">%1</span></tt> 、
2列目がリスト&#64;&#64;&#64;の <tt class="docutils literal"><span class="pre">%2</span></tt> 、にはめ込まれます。
エスケープされた文字は戻ります。
<tt class="docutils literal"><span class="pre">mojihame</span></tt> が出力するHTMLのうち、
セレクトボックスの部分をリスト10に示します。</p>
<ul class="simple">
<li>リスト10: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> が出力するHTMLの一部</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>&lt;<span class="k">select </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;COM&quot;</span>&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;1&quot;</span>&gt;cat /etc/hosts&lt;/option&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;2&quot;</span>&gt;top -l 1&lt;/option&gt;
 &lt;option <span class="nv">value</span><span class="o">=</span><span class="s2">&quot;3&quot;</span>&gt;echo test_test _&lt;/option&gt;
&lt;/select&gt;
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">mojihame</span></tt> は慣れると便利です。
が、頑張る人は <tt class="docutils literal"><span class="pre">awk</span></tt> でもHTMLの部品は作れます。</p>
</div>
<div class="section" id="id3">
<h2>20.5. 再度、インジェクションに注意<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　ここでもう一回注意があります。
<tt class="docutils literal"><span class="pre">com.cgi</span></tt> はセレクトボックスから数字を受け取りますが、
数字だけしか受け取れないわけではありません。
リスト11のように <tt class="docutils literal"><span class="pre">curl</span></tt> 等を使っても、
ブラウザでURLの後ろを細工しても邪悪な文字列を送る事ができます。</p>
<ul class="simple">
<li>リスト11: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> に直接GETでデータを渡す</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>curl <span class="s2">&quot;http://localhost/cgi-bin/com.cgi?reboot&quot;</span>
（略）
&lt;/html&gt;
reboot
</pre></div>
</td></tr></table></div>
<p>この対策もなかなか面倒なのですが、
今回の例だと単に数字しか受け付けなければよいので、
<tt class="docutils literal"><span class="pre">tr</span></tt> を使って次のようにGETされた文字列を受け取ります。
<tt class="docutils literal"><span class="pre">tmp=/tmp/$$</span></tt> の行の下あたりに、</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span><span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span> | tr -dc <span class="s1">&#39;0-9&#39;</span><span class="k">)</span>
</pre></div>
</div>
<p>と付け足します。 <tt class="docutils literal"><span class="pre">tr</span></tt> のオプション <tt class="docutils literal"><span class="pre">-d</span></tt>
は文字（この例では0から9までの数字）を消すという意味ですが、
<tt class="docutils literal"><span class="pre">-c</span></tt> をつけると意味が反転します。
ですので、リスト12のような挙動を示します。
UTF-8なら日本語が混ざっても問題ありません。</p>
<ul class="simple">
<li>リスト12: <tt class="docutils literal"><span class="pre">tr</span></tt> で、指定の文字「以外」を削除</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda$ echo &#39;COM=1aewagああ2&#39; | tr -dc &#39;0-9&#39;
12uedamac:~ ueda$
//↑ 1と2だけ残る
</pre></div>
</td></tr></table></div>
<p>このように12だけ残ります。改行すら消えます。
これで行番号が変数 <tt class="docutils literal"><span class="pre">NUM</span></tt> に入るので、
あとはリストのコマンドを実行するだけです。</p>
</div>
<div class="section" id="id4">
<h2>20.6. 完成<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　完成した <tt class="docutils literal"><span class="pre">com.cgi</span></tt> をリスト13に示します。
変数に文字列が入っていなかったり、
中間ファイルができなかったりというところでバグが出るので、
多少慣れが必要です。
例えば、 <tt class="docutils literal"><span class="pre">COM</span></tt> にコマンドが入らないと23行目でエラーが出るので、
21行目で <tt class="docutils literal"><span class="pre">COM</span></tt> に <tt class="docutils literal"><span class="pre">:</span></tt> （なにもしないコマンド）を入れるなど、
細かい芸が必要です。しかし、行数は短くなりますので、
<em>慣れると</em> さっさと何か試作したり、
USP友の会のサイト（<a class="reference external" href="http://www.usptomo.com">http://www.usptomo.com</a>）
のように見栄えのよいものも早く作れるようになります。</p>
<ul class="simple">
<li>リスト13: <tt class="docutils literal"><span class="pre">com.cgi</span></tt> 完成品</li>
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -xv</span>
<span class="nb">exec </span>2&gt; /tmp/log

<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:<span class="nv">$PATH</span>
<span class="nv">htmlfile</span><span class="o">=</span>/Users/ueda/cgi-bin/com.html
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

<span class="c">######実行可能コマンドリスト######</span>
cat <span class="s">&lt;&lt; FIN &gt; $tmp-list</span>
<span class="s">cat /etc/hosts</span>
<span class="s">top -l 1</span>
<span class="s">echo test_test _</span>
<span class="s">FIN</span>

<span class="c">######コマンドの実行######</span>
<span class="c">#番号受け取り</span>
<span class="nv">NUM</span><span class="o">=</span><span class="k">$(</span><span class="nb">echo</span> <span class="s2">&quot;$QUERY_STRING&quot;</span> | tr -dc <span class="s1">&#39;0-9&#39;</span><span class="k">)</span>
<span class="c">#指定された行を取得</span>
<span class="nv">COM</span><span class="o">=</span><span class="k">$(</span>awk -v <span class="nv">n</span><span class="o">=</span><span class="s2">&quot;$NUM&quot;</span> <span class="s1">&#39;NR==n&#39;</span> <span class="nv">$tmp</span>-list<span class="k">)</span>
<span class="c">#COMが空なら : を入れておく</span>
<span class="o">[</span> -z <span class="s2">&quot;$COM&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nv">COM</span><span class="o">=</span><span class="s2">&quot;:&quot;</span>
<span class="c">#実行</span>
<span class="nv">$COM</span> &gt; <span class="nv">$tmp</span>-result

<span class="c">######HTML出力######</span>
<span class="nb">echo</span> <span class="s2">&quot;Content-type: text/html&quot;</span>
<span class="nb">echo</span>
<span class="c">#エスケープ処理</span>
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> <span class="nv">$tmp</span>-list |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;_&#39;</span> |
<span class="c">#行番号をつける</span>
awk <span class="s1">&#39;{print NR,$1}&#39;</span> |
<span class="c">#出力 &gt;&gt;&gt; 1:行番号 2:コマンド</span>
mojihame -lCOMLIST <span class="nv">$htmlfile</span> - |
<span class="c">#コマンド実行結果をはめ込み</span>
filehame -lRESULT - <span class="nv">$tmp</span>-result

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　完成品では、もう一つ <tt class="docutils literal"><span class="pre">filehame</span></tt> というコマンドを使いました。
これは、あるファイルの間に別のファイルの中身を差し込むコマンドで、
次のように使います。</p>
<ul class="simple">
<li>リスト14: <tt class="docutils literal"><span class="pre">filehame</span></tt> の使い方</li>
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
11
12
13
14</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:cgi-bin ueda<span class="nv">$ </span>cat <span class="nv">file1</span>
<span class="o">===</span>参加者<span class="o">===</span>
<span class="nv">ATT</span>
<span class="o">===</span>以上<span class="o">===</span>
uedamac:cgi-bin ueda<span class="nv">$ </span>cat meibo
山田
里中
殿間
uedamac:cgi-bin ueda<span class="nv">$ </span>filehame -lATT file1 <span class="nv">meibo</span>
<span class="o">===</span>参加者<span class="o">===</span>
山田
里中
殿間
<span class="o">===</span>以上<span class="o">===</span>
</pre></div>
</td></tr></table></div>
<p>これも頑張って <tt class="docutils literal"><span class="pre">sed</span></tt> を使えば同様の処理はできます。</p>
<p>　最後に実行結果を図5に示します。</p>
<ul class="simple">
<li>図5: 実行結果</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="RESULT.png"><img alt="" src="RESULT.png" style="width: 40%;" /></a>
</div>
<p>　ボタンを押すとセレクトボックスの選択結果が戻ってしまいますが、
これもコマンドで対応できます。
open usp Tukubaiの <tt class="docutils literal"><span class="pre">formhame</span></tt> というコマンドを使いますが、
その説明は、チャンスがあれば次回以降ということで。</p>
</div>
<div class="section" id="id5">
<h2>20.7. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はGETを使ってCGIスクリプトに字を送り込む方法を説明し、
ブラウザからコマンドを実行するアプリケーションを作りました。
<tt class="docutils literal"><span class="pre">com.html</span></tt> と <tt class="docutils literal"><span class="pre">com.cgi</span></tt> を合わせても60行程度ですので、
いつも端末を叩いたりシェルスクリプトを書いたりしている人が覚えておくと、
特に何か試作するときに威力を発揮することでしょう。</p>
</div>
</div>
