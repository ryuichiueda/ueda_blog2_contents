---
Copyright: (C) Ryuichi Ueda
---

# 開眼シェルスクリプト2013年1月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>13. 開眼シェルスクリプト 第13回メールを操る(2)<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>13.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は前回に引き続きメールをシェルスクリプトでさばいていきます。<br />
今回の内容は、CUI端末やシェルスクリプトで<br />
たくさんのファイルを操作するための小技、<br />
大技が入り乱れてますので、メールなんぞ興味無いという方も注目です。<br />
おさえておかないと、<br />
マウスで数千のファイルをプチプチマウスで操作するハメになりますよ!!</p><br />
<blockquote><br />
<div>一重積んでは父の為　二重積んでは母の為...<br />
（脚注：賽の河原地蔵和讃より。眠れなくなるので知らない人は調べない方がよいです。）</div></blockquote><br />
</div><br />
<div class="section" id="id3"><br />
<h2>13.2. おさらい<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回は、 <tt class="docutils literal"><span class="pre">Maildir</span></tt><br />
にたまったメールを日別にディレクトリに整理するという課題を扱いました。<br />
リスト1のように、ホーム（ <tt class="docutils literal"><span class="pre">/home/ueda</span></tt> ）下の <tt class="docutils literal"><span class="pre">MAIL</span></tt><br />
というディレクトリに日別にディレクトリを作り、<br />
各ディレクトリの下にメールを置きました。<br />
また、メールをUTF-8に変換したものも作り、<br />
ディレクトリ <tt class="docutils literal"><span class="pre">&lt;日付&gt;.utf8</span></tt> に置きました。</p><br />
<p>↓リスト1: <tt class="docutils literal"><span class="pre">~/MAIL/</span></tt> 下</p><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#MAIL/の下には日付のディレクトリ</span><br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>ls<br />
20120610<br />
20120610.utf8<br />
20120611<br />
20120611.utf8<br />
...<br />
<span class="c">#日付のディレクトリには、それぞれのメールが置かれる</span><br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>ls 20120610/ | head -n 3<br />
1339304183.Vfc03I46017dM943925.abc<br />
1339305265.Vfc03I46062cM458553.abc<br />
1339306807.Vfc03I4607c6M993984.abc<br />
<span class="c">#&lt;日付&gt;.utf8 には、UTF-8化した同名のファイルがある</span><br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>ls 20120610.utf8/ | head -n 3<br />
1339304183.Vfc03I46017dM943925.abc<br />
1339305265.Vfc03I46062cM458553.abc<br />
1339306807.Vfc03I4607c6M993984.abc<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　今回はこの状態から、条件抽出してメールを振り分ける方法、<br />
添付ファイルを抜き出す方法を扱います。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>13.3. メールの振り分け<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　このメールアドレスには世界中から雑多な情報が送られていますが、<br />
ここから条件を満たすメールを集めてみましょう。</p><br />
<p>　例として、サーバ管理者ならお馴染みのLogwatchからのメールを抽出し、<br />
特定のディレクトリに置くという操作をしてみましょう。<br />
Logwatchは、CentOSなどをインストールすると、<br />
特に設定をしなくてもroot宛にサーバ監視結果のメールを毎日送ってくるツールです。<br />
Logwatchから送られてくるメールは、リスト2のような書き出しで始まります。<br />
見たことある人も多いでしょう。</p><br />
<p>↓リスト2: Logwatchからのメール</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre> <span class="c">################### Logwatch 7.3 (03/24/06) ####################</span><br />
 Processing Initiated: Sun Oct 14 04:00:02 2012<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このメールの送信メールアドレスは「 <tt class="docutils literal"><span class="pre">From:</span> <span class="pre">logwatch&#64;&lt;サーバ名&gt;</span></tt> 」<br />
となっており、各メールのヘッダに書いてあります。<br />
蛇足ですが、メーラーはメールのヘッダを読み込んで、 <tt class="docutils literal"><span class="pre">Subject:</span></tt><br />
や <tt class="docutils literal"><span class="pre">From:</span></tt> などの行を読んで件名や送信者をGUI出力しているだけで、<br />
メールはあくまで単なるテキストです。</p><br />
<p>　メールを振り分けるには <tt class="docutils literal"><span class="pre">From:</span> <span class="pre">logwatch&#64;...</span></tt> の行をgrepで抽出して、<br />
grepの出力するファイル名を使ってファイルをどこかにコピーすればよいでしょう。<br />
例として、ホスト名をオプションに指定したら、<br />
<tt class="docutils literal"><span class="pre">LOGWATCH_&lt;ホスト名&gt;</span></tt><br />
というディレクトリに当該ファイルをコピーするシェルスクリプトを次に示します。</p><br />
<p>↓リスト3: 指定したホストのLogwatchからのメールを振り分けるシェルスクリプト</p><br />
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<span class="c">#</span><br />
<span class="c"># LOGWATCH: 指定したホストのlogwatchメールを収集</span><br />
<span class="c"># usage: ./LOGWATCH &lt;hostname&gt;</span><br />
<span class="c">#</span><br />
<span class="c"># written by R. Ueda (r-ueda\@usp-lab.com)</span><br />
<br />
<span class="o">[</span> <span class="s2">&quot;$1&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1<br />
<br />
<span class="nv">server</span><span class="o">=</span><span class="s2">&quot;$1&quot;</span><br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda/MAIL<br />
<span class="nv">dest</span><span class="o">=</span><span class="s2">&quot;$dir/LOGWATCH_$server&quot;</span><br />
<br />
<span class="nb">cd</span> <span class="s2">&quot;$dir&quot;</span> <span class="o">||</span> <span class="nb">exit </span>1<br />
mkdir -p <span class="s2">&quot;$dest&quot;</span> <span class="o">||</span> <span class="nb">exit </span>1<br />
<br />
<span class="nb">echo</span> ????????.utf8/* |<br />
xargs grep -F <span class="s2">&quot;From: logwatch\@$server&quot;</span> |<br />
awk -F: <span class="s1">&#39;{print $1,substr($1,1,8)}&#39;</span> |<br />
<span class="c">#1:ファイル名 2:日付</span><br />
awk -v <span class="nv">d</span><span class="o">=</span><span class="s2">&quot;$dest&quot;</span> <span class="s1">&#39;{print $1,d &quot;/&quot; $2}&#39;</span> |<br />
<span class="c">#1:コピー元 2:コピー先</span><br />
xargs -n 2 cp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　8行目から12行目で、<br />
引数をチェックしたり保存先のディレクトリを作ったりしています。<br />
<tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> や <tt class="docutils literal"><span class="pre">||</span></tt> については以前から何回か出てきていますが、<br />
<tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> は左側のコマンドが成功（終了ステータスが0）<br />
だったら右側のコマンドを実行します。<br />
<tt class="docutils literal"><span class="pre">||</span></tt> はこの逆です。</p><br />
<p>　15行目の <tt class="docutils literal"><span class="pre">mkdir</span></tt> の <tt class="docutils literal"><span class="pre">-p</span></tt> オプションは、<br />
既にディレクトリがあってもエラーにならないように指定しています。<br />
一方で、パーミッション等の理由でディレクトリが作れないときは<br />
しっかりエラーを出してくれます。</p><br />
<p>　17行目から23行目の処理を一言で言うと、<br />
全メールに対してSubjectを調べて、<br />
<tt class="docutils literal"><span class="pre">$1</span></tt> で指定したホストのLogwatchなら、<br />
ディレクトリ <tt class="docutils literal"><span class="pre">LOGWATCH_&lt;ホスト名&gt;</span></tt><br />
にファイルをコピーしています。<br />
Logwatchのメールは一日一通来るので、<br />
コピーしたファイル名を日付にしています。</p><br />
<p>　18行目のgrepのオプション <tt class="docutils literal"><span class="pre">-F</span></tt> ですが、<br />
これは正規表現を使わないときに指定するオプションです。<br />
メールアドレスにドット（ <tt class="docutils literal"><span class="pre">.</span></tt> ）が入っていて、<br />
そのままgrepすると「任意の一字」を示す記号扱いされてしまうので、<br />
<tt class="docutils literal"><span class="pre">-F</span></tt> を指定しました。<br />
<tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-F</span></tt> と同義の <tt class="docutils literal"><span class="pre">fgrep</span></tt> というコマンドもあります。</p><br />
<p>　21行目のawkを通った後の文字列をリスト4に示します。<br />
これを23行目のxargsに通すことでリストの1列目のファイルが<br />
二列目のファイル名でコピーされます。</p><br />
<p>↓リスト4: 21行目のパイプを通る文字列</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>20120611.utf8/1339354818.xyz.abc /home/ueda/MAIL/LOGWATCH_abc.usptomonokai.jp/20120611<br />
20120612.utf8/1339441214.xyz.abc /home/ueda/MAIL/LOGWATCH_abc.usptomonokai.jp/20120612<br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト4の「xyz」はもっと長い文字列ですが、<br />
紙面で煩わしいので短縮しています。<br />
以後も「xyz」で置き換えます。</p><br />
<p>　では、実行して、ちゃんと動いたか確かめてみましょう。<br />
リスト5に実行例と結果を示します。</p><br />
<p>↓リスト5: <tt class="docutils literal"><span class="pre">LOGWATCH</span></tt> の実行</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>./LOGWATCH abc.usptomonokai.jp 2&gt; /dev/null<br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>ls LOGWATCH_abc.usptomonokai.jp | head -n 3<br />
20120611<br />
20120612<br />
20120613<br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ./LOGWATCH_abc.usptomonokai.jp/* | head -n 2<br />
./LOGWATCH_abc.usptomonokai.jp/20120611:From: logwatch\@abc.usptomonokai.jp<br />
./LOGWATCH_abc.usptomonokai.jp/20120612:From: logwatch\@abc.usptomonokai.jp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もし複数のサーバからLogwatchのメールを受け取っているならば、<br />
ホストのリストを作ってシェルスクリプト <tt class="docutils literal"><span class="pre">LOGWATCH</span></tt><br />
を繰り返し適用すれば、Logwatchのメールを振り分けることができるでしょう。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>13.4. 添付ファイルを抽出する<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次は大技です。メールから添付ファイルを抽出します。<br />
図1は、準備したサンプルメールをgmailで見たところです。<br />
サンプルメールのメールには画像ファイル<br />
（イラストと大きなデジカメ写真）<br />
が二つ添付されています。</p><br />
<div class="figure"><br />
<img alt="_images/MAIL1.png" src="MAIL1.png" /><br />
<p class="caption">図1: サンプルメール（添付ファイル2個付き）</p><br />
</div><br />
<p>　毎度のこと大雑把なので詳しくは別の資料を見ていただきたいのですが、<br />
添付ファイルがあるときのメールのフォーマットについて説明します。<br />
まず図1のメールについて、<br />
実物（つまりテキストファイル）を見てみましょう。<br />
lessで見るとリスト6のような構造になっているのが分かります。<br />
と言っても、7万7千行もあるので見るのは大変ですが・・・。</p><br />
<p>↓リスト6: サンプルメール実物（大幅に省略）</p><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>less ./20121016/1350369599.xyz.abc<br />
（ヘッダ。略）<br />
Content-Type: multipart/mixed; <span class="nv">boundary</span><span class="o">=</span>047d7b621ee6cf83c604cc276bb3<br />
<br />
--047d7b621ee6cf83c604cc276bb3<br />
（メール本文。文字化け）<br />
--047d7b621ee6cf83c604cc276bb3<br />
...ひたすら記号が続く...<br />
--047d7b621ee6cf83c604cc276bb3<br />
...ひたすら記号が続く...<br />
--047d7b621ee6cf83c604cc276bb3--<br />
<span class="c">#7万7千行もある。</span><br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>wc -l ./20121016/1350369599.xyz.abc<br />
77342 ./20121016/1350369599.xyz.abc<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　このテキストの中に、<br />
<tt class="docutils literal"><span class="pre">--047d7b621ee6cf83c604cc276bb3</span></tt><br />
という行がいくつかあって、<br />
どうやら区切り文字になっているようです。</p><br />
<p>　これは、「MIMEマルチパート」と呼ばれる形式です。<br />
MIMEマルチパートにはいくつか種類がありますが、<br />
1個以上の添付ファイルが含まれたテキスト形式のメールは、<br />
何か特殊な状況でなければ <tt class="docutils literal"><span class="pre">multipart/mixed</span></tt> という種類になります。<br />
今回はこいつだけ相手にしましょう。</p><br />
<p>　添付ファイルをメールから抽出するには、<br />
<tt class="docutils literal"><span class="pre">boundary</span></tt> で指定された文字列（境界文字列）<br />
で挟まれた領域から中身を抽出します。<br />
リスト7は、 <tt class="docutils literal"><span class="pre">CHINJYU.JPG</span></tt> に関係する部分です。</p><br />
<p>↓リスト7: 境界と境界の間のテキスト</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>--047d7b621ee6cf83c604cc276bb3<br />
Content-Type: image/jpeg; <span class="nv">name</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span><br />
Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span><br />
Content-Transfer-Encoding: base64<br />
X-Attachment-Id: f_h8cn3pxc0<br />
<br />
/9j/4AAQSkZJRgABAQEASABIAAD//gATQ3JlYXRlZCB3aXRoIEdJTVD/2wBDAAEBAQEBAQEBAQEB<br />
AQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBD<br />
（略）<br />
0000000000000000000000000000000000000000000000000000000000000000000000000000<br />
0000000000000000000000000000001//9k<span class="o">=</span><br />
--047d7b621ee6cf83c604cc276bb3<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この部分は空行をはさんで上側にファイルの情報が書かれたヘッダ、<br />
下側にエンコードされたファイルの中身があります。<br />
<tt class="docutils literal"><span class="pre">Content-Transfer-Encoding:</span> <span class="pre">base64</span></tt> とあるように、<br />
base64という方式でエンコードされています。<br />
データをbase64でエンコードしたりデコードしたりするのは簡単で、<br />
リスト8のように <tt class="docutils literal"><span class="pre">base64</span></tt> というコマンドを使います。</p><br />
<p>↓リスト8: base64コマンドによるエンコードとデコード</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo</span> あはははは | base64<br />
<span class="nv">44GC44Gv44Gv44Gv44GvCg</span><span class="o">==</span><br />
<span class="nv">$ </span><span class="nb">echo</span> あはははは | base64 | base64 -d<br />
あはははは<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　では、理屈と方法が分かったので、<br />
添付ファイルを抽出します。<br />
リスト9に作ったシェルスクリプトを示します。<br />
このシェルスクリプトで、<br />
<tt class="docutils literal"><span class="pre">/home/ueda/MAIL/FILES</span></tt><br />
内に、 <tt class="docutils literal"><span class="pre">&lt;メールファイル名&gt;_&lt;添付ファイル名&gt;</span></tt><br />
で添付ファイルが抽出されます。ディレクトリ<br />
<tt class="docutils literal"><span class="pre">/home/ueda/MAIL/FILES</span></tt> は事前に作っておきます。</p><br />
<p>↓リスト9: 添付ファイル抽出シェルスクリプト</p><br />
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
39<br />
40<br />
41<br />
42</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c">#</span><br />
<span class="c"># EXTFILE: メールから添付ファイルを抽出する。</span><br />
<span class="c"># usage: EXTFILE &lt;電子メールファイル&gt;</span><br />
<span class="c"># written by R. Ueda (r-ueda\@usp-lab.com) Oct. 16, 2012</span><br />
<br />
<span class="o">[</span> <span class="s2">&quot;$1&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1<br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<span class="nv">dest</span><span class="o">=</span>/home/ueda/MAIL/FILES<br />
<span class="c">##############################################</span><br />
<span class="c">#境界文字列を抽出</span><br />
grep -i <span class="s1">&#39;^Content-Type:&#39;</span> <span class="s2">&quot;$1&quot;</span> |<br />
grep <span class="s2">&quot;multipart/mixed&quot;</span> |<br />
<span class="c">#最初にあるもの（=ヘッダにあるもの）だけ処理</span><br />
head -n 1 |<br />
sed <span class="s1">&#39;s/..*boundary=//&#39;</span> |<br />
<span class="c">#「&quot;」がくっついている場合があるので、取って変数に入れる</span><br />
tr -d <span class="s1">&#39;&quot;&#39;</span> &gt; <span class="nv">$tmp</span>-boundary<br />
<br />
<span class="c">##############################################</span><br />
<span class="c">#境界でファイルを分割</span><br />
awk -v <span class="nv">b</span><span class="o">=</span><span class="s2">&quot;^--$(cat $tmp-boundary)&quot;</span> -v <span class="nv">f</span><span class="o">=</span><span class="s2">&quot;$tmp-F&quot;</span> <span class="se">\\</span><br />
 <span class="s1">&#39;{if($0~b){a++};print &gt; f a}&#39;</span> <span class="s2">&quot;$1&quot;</span><br />
<br />
<span class="c">##############################################</span><br />
<span class="c">#分割したファイルから添付ファイルを作る</span><br />
grep -i <span class="s1">&#39;^content-disposition:&#39;</span> <span class="nv">$tmp</span>-F* |<br />
<span class="c">#1:grepの結果から中間ファイル名と添付ファイル名を抜き出す</span><br />
sed <span class="s1">&#39;s/^\\([^:][^:]*\\):..*filename=\\(..*\\)/\\1 \\2/&#39;</span> |<br />
<span class="c">#1:中間ファイル名 2:添付ファイル名</span><br />
tr -d <span class="s1">&#39;&quot;&#39;</span> |<br />
<span class="k">while </span><span class="nb">read </span>a b ; <span class="k">do</span><br />
 <span class="c">#抽出、デコード、出力</span><br />
 sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="s2">&quot;$a&quot;</span> |<br />
 base64 -d &gt; <span class="s2">&quot;$dest/$(basename $1)_${b}&quot;</span><br />
<span class="k">done</span><br />
<br />
<span class="c">#作ったファイルを表示</span><br />
ls <span class="nv">$dest</span>/<span class="k">$(</span>basename <span class="nv">$1</span><span class="k">)</span>_*<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　10行目～18行目は、 <tt class="docutils literal"><span class="pre">Content-Type:</span> <span class="pre">multipart/mixed</span></tt><br />
の行から境界文字列を取り出しています。<br />
この部分は取り出せればどのように書いてもよいのですが、<br />
このスクリプトでは、本文中に<br />
<tt class="docutils literal"><span class="pre">Content-Type:</span> <span class="pre">multipart/mixed</span> <span class="pre">...</span></tt><br />
と書いてあっても騙されないように一工夫しています。<br />
また、 <tt class="docutils literal"><span class="pre">Content-Type:</span></tt><br />
の大文字小文字が間違っていてもよいように <tt class="docutils literal"><span class="pre">grep</span></tt><br />
に <tt class="docutils literal"><span class="pre">-i</span></tt> オプションをつけています。<br />
解説は割愛しますが、 <tt class="docutils literal"><span class="pre">Content-Type</span></tt><br />
の大文字小文字入り乱れの様子は、<br />
リスト10のように端末で確かめることができます。<br />
（sm2, countは open usp Tukubaiのコマンドです。）</p><br />
<p>↓リスト10: Content-Typeの大文字小文字バリエーション</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>grep -i <span class="s2">&quot;^content-type:&quot;</span> ./*.utf8/* |<br />
 awk -F: <span class="s1">&#39;{print $2}&#39;</span> | count 1 1 | sort | sm2 1 1 2 2<br />
Content-Type 41367<br />
Content-type 75<br />
content-type 9<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　22,23行目のawkは、メールファイルを境界で切って保存する処理です。<br />
このawkにはいろいろポイントがあります。<br />
正直言って、ややこしいです。</p><br />
<p>　まず、awkの <tt class="docutils literal"><span class="pre">-v</span></tt> オプションは何回か紹介していますが、<br />
bashの変数をawkの変数に事前に代入するためのものです。<br />
ここでは、境界の文字列と切り出し先のファイル名の一部を、<br />
それぞれ <tt class="docutils literal"><span class="pre">b</span></tt> と <tt class="docutils literal"><span class="pre">f</span></tt> という変数に代入しています。</p><br />
<p>　if文中の <tt class="docutils literal"><span class="pre">$0~b</span></tt> は、変数 <tt class="docutils literal"><span class="pre">b</span></tt> を正規表現扱いして、<br />
<tt class="docutils literal"><span class="pre">$0</span></tt> （行全体）と比較する式です。<br />
変数を右側に持ってくるときは、 <tt class="docutils literal"><span class="pre">/</span></tt> は不要です。</p><br />
<p>　そして、知らない人には一番わけがわからない<br />
<tt class="docutils literal"><span class="pre">print</span> <span class="pre">&gt;</span> <span class="pre">f</span> <span class="pre">a</span></tt> ですが、<br />
実は <tt class="docutils literal"><span class="pre">&gt;</span></tt> は不等号ではなくリダイレクトです。<br />
<tt class="docutils literal"><span class="pre">print</span></tt> で行全体を出力し、その出力先を <tt class="docutils literal"><span class="pre">f</span> <span class="pre">a</span></tt><br />
にしています。 <tt class="docutils literal"><span class="pre">f</span></tt> はファイル名の一部<br />
（ <tt class="docutils literal"><span class="pre">/tmp/&lt;プロセス番号&gt;-F</span></tt> ）<br />
<tt class="docutils literal"><span class="pre">a</span></tt> は境界文字列が見つかると一つずつ増える数字です。<br />
awkでは文字列と数字を並べるとそのまま文字列として連結するので、<br />
リダイレクト先は、<br />
<tt class="docutils literal"><span class="pre">/tmp/&lt;プロセス番号&gt;-F&lt;数字&gt;</span></tt> となります。</p><br />
<p>　25～36行目は、分割されたファイルから添付ファイルを復元する処理です。<br />
27行目のgrepで <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt> の行<br />
（添付ファイル名が含まれる）を抽出します。<br />
図1のメールを通すと、<br />
27行目のgrepの後ろのパイプにはリスト11の文字列が流れます。</p><br />
<p>↓リスト11: リスト9、27行目のパイプを通る文字列</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/tmp/3560-F2:Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span><br />
/home/ueda/tmp/3560-F3:Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;IMG_0965.JPG&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これを見ると <tt class="docutils literal"><span class="pre">3560-F0</span></tt> と <tt class="docutils literal"><span class="pre">3560-F1</span></tt> はどこにいったということになりますが、<br />
<tt class="docutils literal"><span class="pre">3560-F0</span></tt> はメールのヘッダ、 <tt class="docutils literal"><span class="pre">3560-F1</span></tt> は本文で <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt><br />
という文字列がないのでこの時点で弾かれます。<br />
もし <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt> で始まる行があれば添付ファイル扱いされますが、<br />
まあ、ゴミが出るだけなのでよいとしましょう。<br />
もし気になるのであれば、 <tt class="docutils literal"><span class="pre">while</span></tt> 文のなかでチェックします。</p><br />
<p>　リスト9、29行目のsedは、<br />
grepの出力から分割したファイル名と添付ファイル名を抽出しています。<br />
こうすることで、後ろの <tt class="docutils literal"><span class="pre">while</span></tt> 文に入出力するファイル名を与えています。</p><br />
<p>　whileの中は、34行目のsedでファイルの中身部分を取り出し、<br />
35行目のbase64で添付ファイルを復元しています。<br />
<tt class="docutils literal"><span class="pre">sed</span> <span class="pre">-n</span> <span class="pre">'/^$/,$p'</span></tt> は、「空行以降をプリントせよ」という意味になります。<br />
<tt class="docutils literal"><span class="pre">sed</span> <span class="pre">-n</span> <span class="pre">'&lt;開始行&gt;,&lt;終了行&gt;p'</span></tt> で、<br />
ファイルからある範囲を行単位で出力する処理ができるので、<br />
これは丸暗記しておくとよいでしょう。34行目のように、<br />
行の指定には正規表現や最終行を表す <tt class="docutils literal"><span class="pre">$</span></tt> などの記号が使えます。</p><br />
<p>　35行目のbase64で気になるのは、<br />
ちゃんと1ビットも違わずファイルを復元してくれるのかというところですが、<br />
これは大丈夫です。 <tt class="docutils literal"><span class="pre">EXTFILE</span></tt> を実行して、<br />
できたファイルを添付した元のファイルと比較してみましょう。</p><br />
<p>↓リスト12: <tt class="docutils literal"><span class="pre">EXTFILE</span></tt> の実行と添付ファイルのチェック</p><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>./EXTFILE ./20121016/1350369599.xyz.abc<br />
/home/ueda/MAIL/FILES/1350369599.xyz.abc_CHINJYU.JPG<br />
/home/ueda/MAIL/FILES/1350369599.xyz.abc_IMG_0965.JPG<br />
<span class="c">#元のファイルと比較</span><br />
<span class="c">#バイナリファイル（テキストも）を比較するときは、diffではなくcmpを使います。</span><br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>cmp ./CHINJYU.JPG ./FILES/1350369599.xyz.abc_CHINJYU.JPG<br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span>cmp ./IMG_0965.JPG ./FILES/1350369599.xyz.abc_IMG_0965.JPG<br />
ueda\@uedaubuntu:~/MAIL<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>大丈夫ですね。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h2>13.5. 終わりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は前回に引き続き、電子メールを扱いました。<br />
気づいた人は少ないと思いますが、<br />
grepを起点としてファイルを操作するためのリストを作るという処理が、<br />
メールの振り分け、添付ファイルの操作の両方で出てきました。<br />
これは覚えておくと便利なテクニックです。<br />
慣れておくと、実際にファイルを操作する直前まではテキスト処理になるので、<br />
whileのなかでcpやmvの前処理をするよりもデバッグが楽になります。<br />
また、立ち上がるコマンドの数も減らすことができます。</p><br />
<p>　添付ファイルの抽出では、バイナリデータを扱いました。<br />
これは知らない人が意外に多いのですが、<br />
バイナリデータに対してリダイレクトやcatをしても、<br />
データが壊れることはありません。<br />
base64など、テキストとバイナリを橋渡しするコマンドがあれば、<br />
シームレスにバイナリをシェルスクリプトで扱うことができます。<br />
これは次々回あたりに扱ってみたいと考えています。</p><br />
<p>　次回は、これまでの応用で「CUIおれおれメーラー」<br />
でも作ってみたいと思います。</p><br />
</div><br />
</div>
