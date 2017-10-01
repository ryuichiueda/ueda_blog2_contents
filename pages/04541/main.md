---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年1月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>13. 開眼シェルスクリプト 第13回メールを操る(2)<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>13.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は前回に引き続きメールをシェルスクリプトでさばいていきます。
今回の内容は、CUI端末やシェルスクリプトで
たくさんのファイルを操作するための小技、
大技が入り乱れてますので、メールなんぞ興味無いという方も注目です。
おさえておかないと、
マウスで数千のファイルをプチプチマウスで操作するハメになりますよ!!</p>
<blockquote>
<div>一重積んでは父の為　二重積んでは母の為...
（脚注：賽の河原地蔵和讃より。眠れなくなるので知らない人は調べない方がよいです。）</div></blockquote>
</div>
<div class="section" id="id3">
<h2>13.2. おさらい<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回は、 <tt class="docutils literal"><span class="pre">Maildir</span></tt>
にたまったメールを日別にディレクトリに整理するという課題を扱いました。
リスト1のように、ホーム（ <tt class="docutils literal"><span class="pre">/home/ueda</span></tt> ）下の <tt class="docutils literal"><span class="pre">MAIL</span></tt>
というディレクトリに日別にディレクトリを作り、
各ディレクトリの下にメールを置きました。
また、メールをUTF-8に変換したものも作り、
ディレクトリ <tt class="docutils literal"><span class="pre">&lt;日付&gt;.utf8</span></tt> に置きました。</p>
<p>↓リスト1: <tt class="docutils literal"><span class="pre">~/MAIL/</span></tt> 下</p>
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#MAIL/の下には日付のディレクトリ</span>
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>ls
20120610
20120610.utf8
20120611
20120611.utf8
...
<span class="c">#日付のディレクトリには、それぞれのメールが置かれる</span>
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>ls 20120610/ | head -n 3
1339304183.Vfc03I46017dM943925.abc
1339305265.Vfc03I46062cM458553.abc
1339306807.Vfc03I4607c6M993984.abc
<span class="c">#&lt;日付&gt;.utf8 には、UTF-8化した同名のファイルがある</span>
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>ls 20120610.utf8/ | head -n 3
1339304183.Vfc03I46017dM943925.abc
1339305265.Vfc03I46062cM458553.abc
1339306807.Vfc03I4607c6M993984.abc
</pre></div>
</td></tr></table></div>
<p>　今回はこの状態から、条件抽出してメールを振り分ける方法、
添付ファイルを抜き出す方法を扱います。</p>
</div>
<div class="section" id="id4">
<h2>13.3. メールの振り分け<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　このメールアドレスには世界中から雑多な情報が送られていますが、
ここから条件を満たすメールを集めてみましょう。</p>
<p>　例として、サーバ管理者ならお馴染みのLogwatchからのメールを抽出し、
特定のディレクトリに置くという操作をしてみましょう。
Logwatchは、CentOSなどをインストールすると、
特に設定をしなくてもroot宛にサーバ監視結果のメールを毎日送ってくるツールです。
Logwatchから送られてくるメールは、リスト2のような書き出しで始まります。
見たことある人も多いでしょう。</p>
<p>↓リスト2: Logwatchからのメール</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre> <span class="c">################### Logwatch 7.3 (03/24/06) ####################</span>
 Processing Initiated: Sun Oct 14 04:00:02 2012
...
</pre></div>
</td></tr></table></div>
<p>　このメールの送信メールアドレスは「 <tt class="docutils literal"><span class="pre">From:</span> <span class="pre">logwatch&#64;&lt;サーバ名&gt;</span></tt> 」
となっており、各メールのヘッダに書いてあります。
蛇足ですが、メーラーはメールのヘッダを読み込んで、 <tt class="docutils literal"><span class="pre">Subject:</span></tt>
や <tt class="docutils literal"><span class="pre">From:</span></tt> などの行を読んで件名や送信者をGUI出力しているだけで、
メールはあくまで単なるテキストです。</p>
<p>　メールを振り分けるには <tt class="docutils literal"><span class="pre">From:</span> <span class="pre">logwatch&#64;...</span></tt> の行をgrepで抽出して、
grepの出力するファイル名を使ってファイルをどこかにコピーすればよいでしょう。
例として、ホスト名をオプションに指定したら、
<tt class="docutils literal"><span class="pre">LOGWATCH_&lt;ホスト名&gt;</span></tt>
というディレクトリに当該ファイルをコピーするシェルスクリプトを次に示します。</p>
<p>↓リスト3: 指定したホストのLogwatchからのメールを振り分けるシェルスクリプト</p>
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>
<span class="c">#</span>
<span class="c"># LOGWATCH: 指定したホストのlogwatchメールを収集</span>
<span class="c"># usage: ./LOGWATCH &lt;hostname&gt;</span>
<span class="c">#</span>
<span class="c"># written by R. Ueda (r-ueda@usp-lab.com)</span>

<span class="o">[</span> <span class="s2">&quot;$1&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1

<span class="nv">server</span><span class="o">=</span><span class="s2">&quot;$1&quot;</span>
<span class="nv">dir</span><span class="o">=</span>/home/ueda/MAIL
<span class="nv">dest</span><span class="o">=</span><span class="s2">&quot;$dir/LOGWATCH_$server&quot;</span>

<span class="nb">cd</span> <span class="s2">&quot;$dir&quot;</span> <span class="o">||</span> <span class="nb">exit </span>1
mkdir -p <span class="s2">&quot;$dest&quot;</span> <span class="o">||</span> <span class="nb">exit </span>1

<span class="nb">echo</span> ????????.utf8/* |
xargs grep -F <span class="s2">&quot;From: logwatch@$server&quot;</span> |
awk -F: <span class="s1">&#39;{print $1,substr($1,1,8)}&#39;</span> |
<span class="c">#1:ファイル名 2:日付</span>
awk -v <span class="nv">d</span><span class="o">=</span><span class="s2">&quot;$dest&quot;</span> <span class="s1">&#39;{print $1,d &quot;/&quot; $2}&#39;</span> |
<span class="c">#1:コピー元 2:コピー先</span>
xargs -n 2 cp
</pre></div>
</td></tr></table></div>
<p>　8行目から12行目で、
引数をチェックしたり保存先のディレクトリを作ったりしています。
<tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> や <tt class="docutils literal"><span class="pre">||</span></tt> については以前から何回か出てきていますが、
<tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> は左側のコマンドが成功（終了ステータスが0）
だったら右側のコマンドを実行します。
<tt class="docutils literal"><span class="pre">||</span></tt> はこの逆です。</p>
<p>　15行目の <tt class="docutils literal"><span class="pre">mkdir</span></tt> の <tt class="docutils literal"><span class="pre">-p</span></tt> オプションは、
既にディレクトリがあってもエラーにならないように指定しています。
一方で、パーミッション等の理由でディレクトリが作れないときは
しっかりエラーを出してくれます。</p>
<p>　17行目から23行目の処理を一言で言うと、
全メールに対してSubjectを調べて、
<tt class="docutils literal"><span class="pre">$1</span></tt> で指定したホストのLogwatchなら、
ディレクトリ <tt class="docutils literal"><span class="pre">LOGWATCH_&lt;ホスト名&gt;</span></tt>
にファイルをコピーしています。
Logwatchのメールは一日一通来るので、
コピーしたファイル名を日付にしています。</p>
<p>　18行目のgrepのオプション <tt class="docutils literal"><span class="pre">-F</span></tt> ですが、
これは正規表現を使わないときに指定するオプションです。
メールアドレスにドット（ <tt class="docutils literal"><span class="pre">.</span></tt> ）が入っていて、
そのままgrepすると「任意の一字」を示す記号扱いされてしまうので、
<tt class="docutils literal"><span class="pre">-F</span></tt> を指定しました。
<tt class="docutils literal"><span class="pre">grep</span> <span class="pre">-F</span></tt> と同義の <tt class="docutils literal"><span class="pre">fgrep</span></tt> というコマンドもあります。</p>
<p>　21行目のawkを通った後の文字列をリスト4に示します。
これを23行目のxargsに通すことでリストの1列目のファイルが
二列目のファイル名でコピーされます。</p>
<p>↓リスト4: 21行目のパイプを通る文字列</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>20120611.utf8/1339354818.xyz.abc /home/ueda/MAIL/LOGWATCH_abc.usptomonokai.jp/20120611
20120612.utf8/1339441214.xyz.abc /home/ueda/MAIL/LOGWATCH_abc.usptomonokai.jp/20120612
</pre></div>
</td></tr></table></div>
<p>リスト4の「xyz」はもっと長い文字列ですが、
紙面で煩わしいので短縮しています。
以後も「xyz」で置き換えます。</p>
<p>　では、実行して、ちゃんと動いたか確かめてみましょう。
リスト5に実行例と結果を示します。</p>
<p>↓リスト5: <tt class="docutils literal"><span class="pre">LOGWATCH</span></tt> の実行</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>./LOGWATCH abc.usptomonokai.jp 2&gt; /dev/null
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>ls LOGWATCH_abc.usptomonokai.jp | head -n 3
20120611
20120612
20120613
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ./LOGWATCH_abc.usptomonokai.jp/* | head -n 2
./LOGWATCH_abc.usptomonokai.jp/20120611:From: logwatch@abc.usptomonokai.jp
./LOGWATCH_abc.usptomonokai.jp/20120612:From: logwatch@abc.usptomonokai.jp
</pre></div>
</td></tr></table></div>
<p>　もし複数のサーバからLogwatchのメールを受け取っているならば、
ホストのリストを作ってシェルスクリプト <tt class="docutils literal"><span class="pre">LOGWATCH</span></tt>
を繰り返し適用すれば、Logwatchのメールを振り分けることができるでしょう。</p>
</div>
<div class="section" id="id5">
<h2>13.4. 添付ファイルを抽出する<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次は大技です。メールから添付ファイルを抽出します。
図1は、準備したサンプルメールをgmailで見たところです。
サンプルメールのメールには画像ファイル
（イラストと大きなデジカメ写真）
が二つ添付されています。</p>
<div class="figure">
<img alt="_images/MAIL1.png" src="MAIL1.png" />
<p class="caption">図1: サンプルメール（添付ファイル2個付き）</p>
</div>
<p>　毎度のこと大雑把なので詳しくは別の資料を見ていただきたいのですが、
添付ファイルがあるときのメールのフォーマットについて説明します。
まず図1のメールについて、
実物（つまりテキストファイル）を見てみましょう。
lessで見るとリスト6のような構造になっているのが分かります。
と言っても、7万7千行もあるので見るのは大変ですが・・・。</p>
<p>↓リスト6: サンプルメール実物（大幅に省略）</p>
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
14</pre></div></td><td class="code"><div class="highlight"><pre>ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>less ./20121016/1350369599.xyz.abc
（ヘッダ。略）
Content-Type: multipart/mixed; <span class="nv">boundary</span><span class="o">=</span>047d7b621ee6cf83c604cc276bb3

--047d7b621ee6cf83c604cc276bb3
（メール本文。文字化け）
--047d7b621ee6cf83c604cc276bb3
...ひたすら記号が続く...
--047d7b621ee6cf83c604cc276bb3
...ひたすら記号が続く...
--047d7b621ee6cf83c604cc276bb3--
<span class="c">#7万7千行もある。</span>
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>wc -l ./20121016/1350369599.xyz.abc
77342 ./20121016/1350369599.xyz.abc
</pre></div>
</td></tr></table></div>
<p>　このテキストの中に、
<tt class="docutils literal"><span class="pre">--047d7b621ee6cf83c604cc276bb3</span></tt>
という行がいくつかあって、
どうやら区切り文字になっているようです。</p>
<p>　これは、「MIMEマルチパート」と呼ばれる形式です。
MIMEマルチパートにはいくつか種類がありますが、
1個以上の添付ファイルが含まれたテキスト形式のメールは、
何か特殊な状況でなければ <tt class="docutils literal"><span class="pre">multipart/mixed</span></tt> という種類になります。
今回はこいつだけ相手にしましょう。</p>
<p>　添付ファイルをメールから抽出するには、
<tt class="docutils literal"><span class="pre">boundary</span></tt> で指定された文字列（境界文字列）
で挟まれた領域から中身を抽出します。
リスト7は、 <tt class="docutils literal"><span class="pre">CHINJYU.JPG</span></tt> に関係する部分です。</p>
<p>↓リスト7: 境界と境界の間のテキスト</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>--047d7b621ee6cf83c604cc276bb3
Content-Type: image/jpeg; <span class="nv">name</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span>
Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span>
Content-Transfer-Encoding: base64
X-Attachment-Id: f_h8cn3pxc0

/9j/4AAQSkZJRgABAQEASABIAAD//gATQ3JlYXRlZCB3aXRoIEdJTVD/2wBDAAEBAQEBAQEBAQEB
AQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBD
（略）
0000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000001//9k<span class="o">=</span>
--047d7b621ee6cf83c604cc276bb3
</pre></div>
</td></tr></table></div>
<p>この部分は空行をはさんで上側にファイルの情報が書かれたヘッダ、
下側にエンコードされたファイルの中身があります。
<tt class="docutils literal"><span class="pre">Content-Transfer-Encoding:</span> <span class="pre">base64</span></tt> とあるように、
base64という方式でエンコードされています。
データをbase64でエンコードしたりデコードしたりするのは簡単で、
リスト8のように <tt class="docutils literal"><span class="pre">base64</span></tt> というコマンドを使います。</p>
<p>↓リスト8: base64コマンドによるエンコードとデコード</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo</span> あはははは | base64
<span class="nv">44GC44Gv44Gv44Gv44GvCg</span><span class="o">==</span>
<span class="nv">$ </span><span class="nb">echo</span> あはははは | base64 | base64 -d
あはははは
</pre></div>
</td></tr></table></div>
<p>　では、理屈と方法が分かったので、
添付ファイルを抽出します。
リスト9に作ったシェルスクリプトを示します。
このシェルスクリプトで、
<tt class="docutils literal"><span class="pre">/home/ueda/MAIL/FILES</span></tt>
内に、 <tt class="docutils literal"><span class="pre">&lt;メールファイル名&gt;_&lt;添付ファイル名&gt;</span></tt>
で添付ファイルが抽出されます。ディレクトリ
<tt class="docutils literal"><span class="pre">/home/ueda/MAIL/FILES</span></tt> は事前に作っておきます。</p>
<p>↓リスト9: 添付ファイル抽出シェルスクリプト</p>
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
39
40
41
42</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c">#</span>
<span class="c"># EXTFILE: メールから添付ファイルを抽出する。</span>
<span class="c"># usage: EXTFILE &lt;電子メールファイル&gt;</span>
<span class="c"># written by R. Ueda (r-ueda@usp-lab.com) Oct. 16, 2012</span>

<span class="o">[</span> <span class="s2">&quot;$1&quot;</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>1
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>
<span class="nv">dest</span><span class="o">=</span>/home/ueda/MAIL/FILES
<span class="c">##############################################</span>
<span class="c">#境界文字列を抽出</span>
grep -i <span class="s1">&#39;^Content-Type:&#39;</span> <span class="s2">&quot;$1&quot;</span> |
grep <span class="s2">&quot;multipart/mixed&quot;</span> |
<span class="c">#最初にあるもの（=ヘッダにあるもの）だけ処理</span>
head -n 1 |
sed <span class="s1">&#39;s/..*boundary=//&#39;</span> |
<span class="c">#「&quot;」がくっついている場合があるので、取って変数に入れる</span>
tr -d <span class="s1">&#39;&quot;&#39;</span> &gt; <span class="nv">$tmp</span>-boundary

<span class="c">##############################################</span>
<span class="c">#境界でファイルを分割</span>
awk -v <span class="nv">b</span><span class="o">=</span><span class="s2">&quot;^--$(cat $tmp-boundary)&quot;</span> -v <span class="nv">f</span><span class="o">=</span><span class="s2">&quot;$tmp-F&quot;</span> <span class="se">\\</span>
 <span class="s1">&#39;{if($0~b){a++};print &gt; f a}&#39;</span> <span class="s2">&quot;$1&quot;</span>

<span class="c">##############################################</span>
<span class="c">#分割したファイルから添付ファイルを作る</span>
grep -i <span class="s1">&#39;^content-disposition:&#39;</span> <span class="nv">$tmp</span>-F* |
<span class="c">#1:grepの結果から中間ファイル名と添付ファイル名を抜き出す</span>
sed <span class="s1">&#39;s/^\\([^:][^:]*\\):..*filename=\\(..*\\)/\\1 \\2/&#39;</span> |
<span class="c">#1:中間ファイル名 2:添付ファイル名</span>
tr -d <span class="s1">&#39;&quot;&#39;</span> |
<span class="k">while </span><span class="nb">read </span>a b ; <span class="k">do</span>
 <span class="c">#抽出、デコード、出力</span>
 sed -n <span class="s1">&#39;/^$/,$p&#39;</span> <span class="s2">&quot;$a&quot;</span> |
 base64 -d &gt; <span class="s2">&quot;$dest/$(basename $1)_${b}&quot;</span>
<span class="k">done</span>

<span class="c">#作ったファイルを表示</span>
ls <span class="nv">$dest</span>/<span class="k">$(</span>basename <span class="nv">$1</span><span class="k">)</span>_*

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　10行目～18行目は、 <tt class="docutils literal"><span class="pre">Content-Type:</span> <span class="pre">multipart/mixed</span></tt>
の行から境界文字列を取り出しています。
この部分は取り出せればどのように書いてもよいのですが、
このスクリプトでは、本文中に
<tt class="docutils literal"><span class="pre">Content-Type:</span> <span class="pre">multipart/mixed</span> <span class="pre">...</span></tt>
と書いてあっても騙されないように一工夫しています。
また、 <tt class="docutils literal"><span class="pre">Content-Type:</span></tt>
の大文字小文字が間違っていてもよいように <tt class="docutils literal"><span class="pre">grep</span></tt>
に <tt class="docutils literal"><span class="pre">-i</span></tt> オプションをつけています。
解説は割愛しますが、 <tt class="docutils literal"><span class="pre">Content-Type</span></tt>
の大文字小文字入り乱れの様子は、
リスト10のように端末で確かめることができます。
（sm2, countは open usp Tukubaiのコマンドです。）</p>
<p>↓リスト10: Content-Typeの大文字小文字バリエーション</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>grep -i <span class="s2">&quot;^content-type:&quot;</span> ./*.utf8/* |
 awk -F: <span class="s1">&#39;{print $2}&#39;</span> | count 1 1 | sort | sm2 1 1 2 2
Content-Type 41367
Content-type 75
content-type 9
</pre></div>
</td></tr></table></div>
<p>　22,23行目のawkは、メールファイルを境界で切って保存する処理です。
このawkにはいろいろポイントがあります。
正直言って、ややこしいです。</p>
<p>　まず、awkの <tt class="docutils literal"><span class="pre">-v</span></tt> オプションは何回か紹介していますが、
bashの変数をawkの変数に事前に代入するためのものです。
ここでは、境界の文字列と切り出し先のファイル名の一部を、
それぞれ <tt class="docutils literal"><span class="pre">b</span></tt> と <tt class="docutils literal"><span class="pre">f</span></tt> という変数に代入しています。</p>
<p>　if文中の <tt class="docutils literal"><span class="pre">$0~b</span></tt> は、変数 <tt class="docutils literal"><span class="pre">b</span></tt> を正規表現扱いして、
<tt class="docutils literal"><span class="pre">$0</span></tt> （行全体）と比較する式です。
変数を右側に持ってくるときは、 <tt class="docutils literal"><span class="pre">/</span></tt> は不要です。</p>
<p>　そして、知らない人には一番わけがわからない
<tt class="docutils literal"><span class="pre">print</span> <span class="pre">&gt;</span> <span class="pre">f</span> <span class="pre">a</span></tt> ですが、
実は <tt class="docutils literal"><span class="pre">&gt;</span></tt> は不等号ではなくリダイレクトです。
<tt class="docutils literal"><span class="pre">print</span></tt> で行全体を出力し、その出力先を <tt class="docutils literal"><span class="pre">f</span> <span class="pre">a</span></tt>
にしています。 <tt class="docutils literal"><span class="pre">f</span></tt> はファイル名の一部
（ <tt class="docutils literal"><span class="pre">/tmp/&lt;プロセス番号&gt;-F</span></tt> ）
<tt class="docutils literal"><span class="pre">a</span></tt> は境界文字列が見つかると一つずつ増える数字です。
awkでは文字列と数字を並べるとそのまま文字列として連結するので、
リダイレクト先は、
<tt class="docutils literal"><span class="pre">/tmp/&lt;プロセス番号&gt;-F&lt;数字&gt;</span></tt> となります。</p>
<p>　25～36行目は、分割されたファイルから添付ファイルを復元する処理です。
27行目のgrepで <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt> の行
（添付ファイル名が含まれる）を抽出します。
図1のメールを通すと、
27行目のgrepの後ろのパイプにはリスト11の文字列が流れます。</p>
<p>↓リスト11: リスト9、27行目のパイプを通る文字列</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/tmp/3560-F2:Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;CHINJYU.JPG&quot;</span>
/home/ueda/tmp/3560-F3:Content-Disposition: attachment; <span class="nv">filename</span><span class="o">=</span><span class="s2">&quot;IMG_0965.JPG&quot;</span>
</pre></div>
</td></tr></table></div>
<p>これを見ると <tt class="docutils literal"><span class="pre">3560-F0</span></tt> と <tt class="docutils literal"><span class="pre">3560-F1</span></tt> はどこにいったということになりますが、
<tt class="docutils literal"><span class="pre">3560-F0</span></tt> はメールのヘッダ、 <tt class="docutils literal"><span class="pre">3560-F1</span></tt> は本文で <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt>
という文字列がないのでこの時点で弾かれます。
もし <tt class="docutils literal"><span class="pre">Content-Disposition</span></tt> で始まる行があれば添付ファイル扱いされますが、
まあ、ゴミが出るだけなのでよいとしましょう。
もし気になるのであれば、 <tt class="docutils literal"><span class="pre">while</span></tt> 文のなかでチェックします。</p>
<p>　リスト9、29行目のsedは、
grepの出力から分割したファイル名と添付ファイル名を抽出しています。
こうすることで、後ろの <tt class="docutils literal"><span class="pre">while</span></tt> 文に入出力するファイル名を与えています。</p>
<p>　whileの中は、34行目のsedでファイルの中身部分を取り出し、
35行目のbase64で添付ファイルを復元しています。
<tt class="docutils literal"><span class="pre">sed</span> <span class="pre">-n</span> <span class="pre">'/^$/,$p'</span></tt> は、「空行以降をプリントせよ」という意味になります。
<tt class="docutils literal"><span class="pre">sed</span> <span class="pre">-n</span> <span class="pre">'&lt;開始行&gt;,&lt;終了行&gt;p'</span></tt> で、
ファイルからある範囲を行単位で出力する処理ができるので、
これは丸暗記しておくとよいでしょう。34行目のように、
行の指定には正規表現や最終行を表す <tt class="docutils literal"><span class="pre">$</span></tt> などの記号が使えます。</p>
<p>　35行目のbase64で気になるのは、
ちゃんと1ビットも違わずファイルを復元してくれるのかというところですが、
これは大丈夫です。 <tt class="docutils literal"><span class="pre">EXTFILE</span></tt> を実行して、
できたファイルを添付した元のファイルと比較してみましょう。</p>
<p>↓リスト12: <tt class="docutils literal"><span class="pre">EXTFILE</span></tt> の実行と添付ファイルのチェック</p>
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
11</pre></div></td><td class="code"><div class="highlight"><pre>ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>./EXTFILE ./20121016/1350369599.xyz.abc
/home/ueda/MAIL/FILES/1350369599.xyz.abc_CHINJYU.JPG
/home/ueda/MAIL/FILES/1350369599.xyz.abc_IMG_0965.JPG
<span class="c">#元のファイルと比較</span>
<span class="c">#バイナリファイル（テキストも）を比較するときは、diffではなくcmpを使います。</span>
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>cmp ./CHINJYU.JPG ./FILES/1350369599.xyz.abc_CHINJYU.JPG
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span>cmp ./IMG_0965.JPG ./FILES/1350369599.xyz.abc_IMG_0965.JPG
ueda@uedaubuntu:~/MAIL<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
</pre></div>
</td></tr></table></div>
<p>大丈夫ですね。</p>
</div>
<div class="section" id="id6">
<h2>13.5. 終わりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は前回に引き続き、電子メールを扱いました。
気づいた人は少ないと思いますが、
grepを起点としてファイルを操作するためのリストを作るという処理が、
メールの振り分け、添付ファイルの操作の両方で出てきました。
これは覚えておくと便利なテクニックです。
慣れておくと、実際にファイルを操作する直前まではテキスト処理になるので、
whileのなかでcpやmvの前処理をするよりもデバッグが楽になります。
また、立ち上がるコマンドの数も減らすことができます。</p>
<p>　添付ファイルの抽出では、バイナリデータを扱いました。
これは知らない人が意外に多いのですが、
バイナリデータに対してリダイレクトやcatをしても、
データが壊れることはありません。
base64など、テキストとバイナリを橋渡しするコマンドがあれば、
シームレスにバイナリをシェルスクリプトで扱うことができます。
これは次々回あたりに扱ってみたいと考えています。</p>
<p>　次回は、これまでの応用で「CUIおれおれメーラー」
でも作ってみたいと思います。</p>
</div>
</div>
