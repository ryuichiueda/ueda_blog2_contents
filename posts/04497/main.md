# 開眼シェルスクリプト2012年3月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>3. 開眼シェルスクリプト 第3回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>3.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　皆様、花粉症対策、万全でしょうか。筆者の場合は毎年対応をサボり、<br />
3月に入ってから医者通いして強い薬を飲み、<br />
半分寝たまま仕事をするのが恒例行事となっております。<br />
早めに原因を叩いておくことが大事だとは分かっていながら、<br />
症状が出るまではつい後回しにしてしまいます。</p><br />
<p>　今回の開眼シェルスクリプトはログ捌き後半です。<br />
ログを処理しやすい形式に整形して一旦保存し、<br />
保存した整形済みファイルを使い、端末で有用な情報を抽出します。<br />
前回ちらっと見ましたが、Linuxやapacheが吐き出すログは、<br />
必ずしもプログラムで処理するために最適化されていません。<br />
シェルスクリプトで処理しやすいように整形します。</p><br />
<div class="section" id="id3"><br />
<h3>3.1.1. 花粉症も厄介なデータも早めに叩くのが吉<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　お題に入る前に、例によって格言を。今回は、次の言葉を意識します。</p><br />
<ul><br />
<li><dl class="first docutils"><br />
<dt>Data dominates. If you&#8217;ve chosen the right data structures and organized things well, the algorithms will almost always be self­evident. Data structures, not algorithms, are central to programming. (See Brooks p. 102.) [Pike1989]</dt><br />
<dd><p class="first last">&#8220;データが全てに優先する。もし適切なデータ構造を選んで物事を整理すれば、アルゴリズムはほとんどの場合に自明となる。アルゴリズムではなく、データ構造がプログラミングの中心である。（Brooksの102ページを見よ。）</p><br />
</dd><br />
</dl><br />
</li><br />
</ul><br />
<p>（脚注：[Pike1989] Rob Pike, &#8220;Notes on Programming in C&#8221;, <a class="reference external" href="http://www.lysator.liu.se/c/pikestyle.html">http://www.lysator.liu.se/c/pikestyle.html</a>, 1989. 不勉強なため未だ読んでませんが、Brooksの102ページというのは、「人月の神話」の原著の102ページのようです。）</p><br />
<p>　要は「データがきれいだとコードが短く簡単になる」ということを言っています。<br />
だとしたら、なるべく根元でデータを整形するのが良い習慣と言えるでしょう。<br />
シェルスクリプトの場合は、awkで扱いやすい形式にして、<br />
どこか適切な場所に整形済みデータを置くことが目標となります。<br />
これをサボると、<br />
長いシェルスクリプトを涕泗の如く生産して振り回されることになります。<br />
・・・花粉症のようになります。</p><br />
<p>　そういう観点を踏まえ、<br />
今回はデータ整形をシェルスクリプトに残し、雑多な集計を端末で済ませます。<br />
集計なぞ、単に何かの数を数えるくらいの処理だったらsort、<br />
uniqと数個のawk・sedで済んでしまうことが大半で、<br />
定期起動したりCGIスクリプトにしない限りはコードに残すと後で面倒です。<br />
一方、データ整形は複雑なだけでなく、<br />
扱いやすいデータを生成するという意味で価値が高いので、残す価値があります。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>3.2. 今回のお題：ログをさばく（後半）<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回に引き続き、Linuxのsecureログ、apacheのaccess_logを題材にします。<br />
ホーム下に「LOG」というディレクトリを作って、<br />
以下のように放り込んであります。<br />
ファイルの場所は前回と同じなのですが、<br />
secureログが前回執筆時より増えています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>ls<br />
httpd/access_log secure-20111016<br />
httpd/access_log.1 secure-20111023<br />
httpd/access_log.2 secure-20111030<br />
httpd/access_log.3 secure-20111204<br />
httpd/access_log.4 secure-20111211<br />
secure secure-20111218<br />
secure-20111012 secure-20111225<br />
</pre></div><br />
</div><br />
<p>　まず、恐れ多くも「きれいか汚いか」という観点でログにケチを付けます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head -n 1 secure httpd/access_log<br />
<span class="o">==</span>&gt; secure &lt;<span class="o">==</span><br />
Nov 20 09:23:44 cent sshd<span class="o">[</span>20019<span class="o">]</span>: Did not receive identification string from 123.232.118.231<br />
<br />
<span class="o">==</span>&gt; httpd/access_log &lt;<span class="o">==</span><br />
114.80.93.71 - - <span class="o">[</span>20/Nov/2011:06:47:54 +0900<span class="o">]</span> <span class="s2">&quot;GET / HTTP/1.1&quot;</span> 200 1429 <span class="s2">&quot;-&quot;</span> <span class="s2">&quot;Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)&quot;</span><br />
</pre></div><br />
</div><br />
<p>もともと人が読むものなのでこれでもよいのですが、<br />
プログラムでログを集計しようとすれば以下の点が問題です。</p><br />
<ul class="simple"><br />
<li>secureに西暦年がついていない</li><br />
<li>どちらのログも月の表記が数字でない</li><br />
<li>access_logのデータの区切り方が統一されていない</li><br />
</ul><br />
<p>これらを残しておくと、情報を引き出すときに毎回大変な目に遭います。</p><br />
<p>　ということで、ログをきれいにします。<br />
実のところ、前回の「他に方法がないことが実験により明らかである場合に限り、<br />
大きいプログラムを書け。」という格言に従えば、<br />
ログの発生元をカスタマイズするのが最良の方法です。<br />
しかし、それでは話が終わってしまうので、<br />
シェルスクリプトで簡潔にします。すんません・・・。</p><br />
<div class="section" id="secure"><br />
<h3>3.2.1. secureログ整形シェルスクリプト<a class="headerlink" href="#secure" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まずsecureログから。このログの最大の問題は、<br />
ログ発生の月日は書いてあっても年が書いてないことです。<br />
長期にわたるログの解析や、年をまたいだログのソートができなくなってしまいます。<br />
前回は、tacを使って年を付加するトリッキーな処理を書きましたが、<br />
今回はもう少し簡単な方法を使います。<br />
幸い私のCentOS6の環境ではデフォルトの状態で過去のログのファイル名に<br />
年月日が付いているので、これを使って</p><br />
<ul class="simple"><br />
<li>ある日のログファイルに、その日以降のログがあったらそれは前の年のログ</li><br />
</ul><br />
<p>と決めつけて日付に年をつけます。</p><br />
<p>　さっそく格言どおり、データ側の都合でアルゴリズムを考える必要が出てきました。<br />
最初からログに年情報があればこんなことはしなくてよいのです。<br />
そういう意味では、過去のログに年月日が付いているので、少し負担は減りました。<br />
その代わりに、ポータビリティーは犠牲になります。</p><br />
<p>　ログファイルの日付をログに付加する処理をリスト1に示します。<br />
8行目で最新のsecureファイルに今日の日付をつけて/tmpにコピーします。<br />
理由は後で説明します。下手な排他ではありません。<br />
10行目のawk中の「FILENAME」は、ファイル名が入った変数です。<br />
10行目の処理で、各ログの先頭にファイル名が入ります。<br />
13行目のsedで、ファイル名から日付以外の文字を除去します。<br />
正規表現 <tt class="docutils literal"><span class="pre">^[^-]*-</span></tt> は、<br />
「行頭からハイフンでない文字が続いた後にハイフン」という意味です。</p><br />
<p>　結局、8行目のコピーはsecureファイルのファイル名に日付を入れて、<br />
過去のログ（secure-日付）と同じ処理ができるようにするだけのために行ったものでした。<br />
ファイル名もデータの一部なので、<br />
やはり正規化しておいた方がアルゴリズムが簡単になります。<br />
速度にこだわる人はシンボリックリンクを使う手もあります。</p><br />
<p>▼リスト1: ログにログファイルの日付をつける</p><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="nb">cd</span> <span class="nv">$dir</span>/LOG<br />
cat secure &gt; <span class="nv">$tmp</span>-<span class="nv">$today</span><br />
<br />
awk <span class="s1">&#39;{print FILENAME,$0}&#39;</span> secure-* <span class="nv">$tmp</span>-<span class="nv">$today</span> |<br />
<span class="c">#1:ファイル名 2:ログの内容</span><br />
<span class="c">#過去のログファイル名から年月日だけ取り出す</span><br />
sed -e <span class="s1">&#39;s/^[^-]*-//&#39;</span> |<br />
<span class="c">#1:ファイル年月日 2:ログの内容</span><br />
<span class="c">#年と月日を分ける</span><br />
sed -e <span class="s1">&#39;s/^..../&amp; /&#39;</span><br />
<span class="c">#1:ファイル年 2:ファイル月日 3:ログの内容</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>リスト1のスクリプトを実行すると、出力は次のようになります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./SECURE_NORMALIZE | head -n 2<br />
2011 1012 Sep 11 19:15:23 localhost runuser: pam_un<br />
2011 1012 Sep 11 19:15:23 localhost runuser: pam_un<br />
<span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./SECURE_NORMALIZE | tail -n 2<br />
2011 1230 Dec 30 13:40:03 cent sshd<span class="o">[</span>31763<span class="o">]</span>: Connect<br />
2011 1230 Dec 30 13:40:06 cent su: pam_unix<span class="o">(</span>su-l:se<br />
</pre></div><br />
</div><br />
<p>　次にログ自体の日付を正規化していきます。<br />
リスト2のスクリプトで、日付を数字にして正規化できます。<br />
コメントが多いので一見すると雑然としていますが、<br />
パイプの部分はawk5個、sed4個で済んでいます。</p><br />
<p>▼リスト2: secureログの整形スクリプト</p><br />
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<span class="c">#</span><br />
<span class="c"># SECURE_NORMALIZE secureログの正規化</span><br />
<span class="c">#</span><br />
<span class="c"># usage: ./SECURE_NORMALIZE</span><br />
<span class="c"># written by R. Ueda (USP研究所) Dec. 30, 2011</span><br />
<br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="nb">cd</span> <span class="nv">$dir</span>/LOG<br />
cat secure &gt; <span class="nv">$tmp</span>-<span class="nv">$today</span><br />
<br />
<span class="c">#前半のコメントは省略</span><br />
awk <span class="s1">&#39;{print FILENAME,$0}&#39;</span> secure-* <span class="nv">$tmp</span>-<span class="nv">$today</span> |<br />
sed -e <span class="s1">&#39;s/^[^-]*-//&#39;</span> |<br />
sed -e <span class="s1">&#39;s/^..../&amp; /&#39;</span> |<br />
<span class="c">#1:ファイル年 2:ファイル月日 3:ログの内容</span><br />
<span class="c">#出力例：2011 1230 Dec 30 13:40:06 cent su: pam_u</span><br />
<span class="c">#月だけ頭に出して英語表記を数字表記に変える</span><br />
awk <span class="s1">&#39;{print $3,$0}&#39;</span> |<br />
<span class="c">#1:ログ月 2:ファイル年 3:ファイル月日 4:ログの内容</span><br />
<span class="c">#前回登場した月の英語表記を数字に変換するsedスクリプト</span><br />
sed -f <span class="nv">$dir</span>/SYS/MONTH - |<br />
<span class="c">#ログから日付を持ってきてログ月にくっつける</span><br />
<span class="c">#一桁の日付を二桁に（既出のgsubを使うが普通はsprintf）</span><br />
awk <span class="s1">&#39;{gsub(/^.$/,&quot;0&amp;&quot;,$5);$1=$1$5;print}&#39;</span> |<br />
<span class="c">#1:ログ月日 2:ファイル年 3:ファイル月日 4:ログの内容</span><br />
<span class="c">#ログの月日がファイルの月日より後なら昨年のデータ</span><br />
awk <span class="s1">&#39;{if($1&gt;$3){$2--};print}&#39;</span> |<br />
<span class="c">#1:ログ月日 2:ログ年 3:ファイル月日 4:ログの内容</span><br />
<span class="c">#出力例：0911 2011 1012 Sep 11 19:17:44 localhost</span><br />
awk <span class="s1">&#39;{$1=$2$1;$2=&quot;&quot;;$3=&quot;&quot;;$4=&quot;&quot;;$5=&quot;&quot;;print}&#39;</span> |<br />
<span class="c">#日付の後に無駄なスペースがたくさん入るので消す</span><br />
sed -e <span class="s1">&#39;s/ */ /&#39;</span> &gt; <span class="nv">$dir</span>/LOG/SECURE<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>これで、次の出力のように日付が数字で表現できます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>tail -n 3 ../LOG/SECURE<br />
20111230 13:39:16 cent su: pam_unix<span class="o">(</span>su-l:sessio<br />
20111230 13:40:03 cent sshd<span class="o">[</span>31763<span class="o">]</span>: Connection<br />
20111230 13:40:06 cent su: pam_unix<span class="o">(</span>su-l:sessio<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="access-log"><br />
<h3>3.2.2. access_logログ整形シェルスクリプト<a class="headerlink" href="#access-log" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次にaccess_logを整形します。これも大変です。<br />
access_logには、左から順に9項目の情報が記述されています。<br />
私は全項目を人に解説できるほどの知識は無いので詳しくは<br />
<a class="reference external" href="http://httpd.apache.org/docs/2.2/ja/logs.html">http://httpd.apache.org/docs/2.2/ja/logs.html</a><br />
等を参照願いたいのですが、大雑把に説明すると、</p><br />
<blockquote><br />
<div>1.クライアントのIP、2.ユーザ名A、3.ユーザ名B、<br />
4.アクセス日時、5.クライアントからの要求、6.ステータスコード、<br />
7.転送バイト数、8.参照元サイト、9.クライアントの情報</div></blockquote><br />
<p>です。</p><br />
<p>　整形の方法は一種類だけではありませんが、<br />
ここではawkにあわせて空白区切りのデータにします。<br />
その後、日時を8桁6桁に整形します。<br />
整形の際、もともとデータ内にある空白が邪魔なので、</p><br />
<ul class="simple"><br />
<li>空白はアンダースコア「_」に変換</li><br />
<li>アンダースコアは「 <tt class="docutils literal"><span class="pre">\\_</span></tt> 」に変換</li><br />
</ul><br />
<p>します。また、区切りに使われている&#8221; &#8220;や[ ]など、<br />
余計な文字は取り去ります。</p><br />
<p>　まず、空白区切りにするところまでの処理をリスト2に示します。<br />
sedを使うと以下のようになります。<br />
6行目のsedがお化けみたいになっていますが、<br />
前半の正規表現はレコード全体に一致するように書いてあります。<br />
これで、1から9までに各項目が入ります。<br />
「でりみた」という文字は、暫定的に区切りにする文字列です。<br />
ファイル中に存在する可能性がほぼゼロの文字列ならば何でもかまいません。</p><br />
<p>▼リスト3: access_logを空白区切りにするまでのスクリプト</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c"># HTTPD_ACCESS_NORMALIZEスクリプト</span><br />
<br />
cat <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> |<br />
<span class="c">#「でりみた」という文字を区切り文字にデータを分ける。</span><br />
sed -e <span class="s1">&#39;s/^\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$/\\1でりみた\\2でりみた\\3でりみた\\4でりみた\\5でりみた\\6でりみ&gt;た\\7でりみた\\8でりみた\\9/&#39;</span> |<br />
<span class="c">#_を\\_に</span><br />
sed -e <span class="s1">&#39;s/_/\\\\_/g&#39;</span> |<br />
<span class="c">#空白を_に</span><br />
sed -e <span class="s1">&#39;s/ /_/g&#39;</span> |<br />
<span class="c">#デリミタを空白に</span><br />
sed -e <span class="s1">&#39;s/でりみた/ /g&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>出力は例えば次のようになります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE 2&gt; /dev/null | head -n 1<br />
180.76.5.49 - - 13/Nov/2011:05:55:20_+0900 GET_/ueda/profile.htm_HTTP/1.1 200 1841 - Mozilla/5.0_<span class="o">(</span>compatible;_Baiduspider/2.0;_+http://www.baidu.com/search/spider.html<span class="o">)</span><br />
</pre></div><br />
</div><br />
<p>　ちゃんと9フィールドになっているか調べるには、awkを使います。<br />
NFは、読み込んだレコードのフィールド数が入る変数です。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE 2&gt; /dev/null | awk <span class="s1">&#39;{print NF}&#39;</span> | uniq<br />
9<br />
</pre></div><br />
</div><br />
<p>　6行目のsedはお化けみたいでちょっとという方には、<br />
リスト4のようにawkを使って分割する方法があります。<br />
この方法は、日本 gnu awk ユーザー会の斉藤さんから教えていただいたものです。<br />
awkの-Fは、入力の区切り文字を指定するオプションです。<br />
この例では「&#8221;」を区切り文字に指定しています。<br />
（エスケープするために <tt class="docutils literal"><span class="pre">\\&quot;</span></tt> と指定しています。）</p><br />
<p>▼リスト4: awkを使ったaccess_logの整形</p><br />
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
cat <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> &gt; <span class="nv">$tmp</span>-data<br />
<br />
awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $1}&#39;</span> <span class="nv">$tmp</span>-data |<br />
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),$0}&#39;</span> |<br />
awk <span class="s1">&#39;{print $1,1,$2;print $1,2,$3;\\</span><br />
<span class="s1"> print $1,3,$4;print $1,4,$5,$6}&#39;</span> &gt; <span class="nv">$tmp</span>-1-4<br />
<br />
awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $2}&#39;</span> <span class="nv">$tmp</span>-data |<br />
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),5,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-5<br />
<br />
awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $3}&#39;</span> <span class="nv">$tmp</span>-data |<br />
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),$0}&#39;</span> |<br />
awk <span class="s1">&#39;{print $1,6,$2;print $1,7,$3}&#39;</span> &gt; <span class="nv">$tmp</span>-6-7<br />
<br />
awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $4}&#39;</span> <span class="nv">$tmp</span>-data |<br />
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),8,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-8<br />
<br />
awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $6}&#39;</span> <span class="nv">$tmp</span>-data |<br />
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),9,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-9<br />
<br />
sort -m -k1,2 -s <span class="nv">$tmp</span>-<span class="o">{</span>1-4,5,6-7,8,9<span class="o">}</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト4のコードで、次の出力のように縦にデータが整理されます。<br />
一番左のコードはレコード番号です。<br />
こちらの方が空白も残っていて、自分で区切り文字を作る必要もありません。<br />
ただ、整形したデータをさらにawkで捌こうとするなら、<br />
データは縦でなく横並びになっていた方が楽ちんです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE.awk | head -n 9<br />
0000000001 1 180.76.5.49<br />
0000000001 2 -<br />
0000000001 3 -<br />
0000000001 4 <span class="o">[</span>13/Nov/2011:05:55:20 +0900<span class="o">]</span><br />
0000000001 5 GET /ueda/profile.htm HTTP/1.1<br />
0000000001 6 200<br />
0000000001 7 1841<br />
0000000001 8 -<br />
0000000001 9 Mozilla/5.0 <span class="o">(</span>compatible; Baiduspider/2.0（略）<br />
</pre></div><br />
</div><br />
<p>　sed版の続きを作成しましょう。日時を加工する部分を記述します。<br />
完成したものをリスト5に示します。コードの部分はたった14行です。<br />
このコードは、紙面で見やすくするために変数を使ったり、<br />
エスケープの&#8221;や&#8217;を使い分けたりしてコンパクトに書いていますが、<br />
ベタに書いて動けば十分です。</p><br />
<p>▼リスト5: access_logの整形スクリプト</p><br />
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
34</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<span class="c">#</span><br />
<span class="c"># HTTP_ACCRESS_NORMALIZE accrss_logの正規化</span><br />
<span class="c"># usage: ./HTTP_ACCESS_NORMALIZE</span><br />
<span class="c">#</span><br />
<span class="c"># written by R. Ueda (USP研究所) Nov. 29, 2011</span><br />
<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO<br />
<br />
<span class="nv">dlmt</span><span class="o">=</span>ﾃﾞﾞﾃﾘﾞﾃﾞﾘﾃﾞﾞﾞﾘﾞﾃﾞﾘﾞ<br />
<span class="nv">reg</span><span class="o">=</span><span class="s1">&#39;^\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$&#39;</span><br />
<span class="nv">str</span><span class="o">=</span><span class="s2">&quot;\\\\1$dlmt\\\\2$dlmt\\\\3$dlmt\\\\4$dlmt\\\\5$dlmt\\\\6$dlmt\\\\7$dlmt\\\\8$dlmt\\\\9&quot;</span><br />
<br />
<span class="c">#&quot;や[ ]、空白を目印にレコードを9分割する。</span><br />
sed <span class="s2">&quot;s;$reg;$str;&quot;</span> <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> |<br />
<span class="c">#_を\\_に</span><br />
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> |<br />
<span class="c">#空白を_に</span><br />
sed <span class="s1">&#39;s/ /_/g&#39;</span> |<br />
<span class="c">#デリミタを空白に戻す</span><br />
sed <span class="s2">&quot;s/$dlmt/ /g&quot;</span> |<br />
<span class="c">#出力例：119.147.75.140 - - 23/Nov/2011:15:14:13_+0900 ...</span><br />
<span class="c">#日時を先頭に</span><br />
awk <span class="s1">&#39;{a=$4;$4=&quot;&quot;;print a,$0}&#39;</span> |<br />
<span class="c">#出力例：23/Nov/2011:15:14:13_+0900 119.147.75.140 - - ...</span><br />
sed <span class="s1">&#39;s;^\\(..\\)/\\(...\\)/\\(....\\):\\(..\\):\\(..\\):\\(..\\)_[^ ]*;\\2 \\1 \\3 \\4\\5\\6;&#39;</span> |<br />
<span class="c">#出力例：Nov 23 2011 151413 119.147.75.140 - - ...</span><br />
sed -f <span class="nv">$dir</span>/SYS/MONTH |<br />
<span class="c">#出力例：11 23 2011 151413 119.147.75.140 - - ...</span><br />
awk <span class="s1">&#39;{d=$3$1$2;$1=&quot;&quot;;$2=&quot;&quot;;$3=&quot;&quot;;print d,$0}&#39;</span> |<br />
<span class="c">#1:日付 2:時刻 3-10:あとの項目</span><br />
<span class="c">#間延びした区切りの空白を戻す。</span><br />
sed <span class="s1">&#39;s/ */ /g&#39;</span> &gt; <span class="nv">$dir</span>/LOG/ACCESS_LOG<br />
<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>head -n 3 ../LOG/ACCESS_LOG<br />
20111030 062140 66.249.67.163 - - GET_/robots.txt_HTTP/1.1 4<br />
20111030 062140 209.85.238.184 - - GET_/paper/ARAIBO<span class="se">\\_</span>Techni<br />
20111030 072937 123.125.71.72 - - HEAD_/paper/ARAIBO<span class="se">\\_</span>Techni<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="id5"><br />
<h3>3.2.3. あとは端末でさっと処理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、整形したものから情報を取り出してみましょう。</p><br />
<p>　まず、secureログから、不正なユーザでアクセスしてきたIPでも抽出しましょう。<br />
まず、sshdのログの「Invalid user」のレコードを抽出します。<br />
下の例のように、headを使って出力を確認しながら書いていきます。<br />
一度入力したコマンド列は、bashの場合、上ボタンを押すと再利用できます。<br />
筆者の場合、一つコマンドを書いたら出力して確認することを繰り返しながら、<br />
泥縄式にコマンドを並べていく場合が多いです。<br />
多少コマンドが多くなっても、ファイルにプログラムを書いて動作確認して・・・<br />
という方法よりは、さっさと終わります。<br />
慣れないうちは、リダイレクトを使ってファイルにデータを貯めて確認しながら練習しましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;&#39;</span> | head -n 3<br />
20110912 00:57:32 cent sshd<span class="o">[</span>2942<span class="o">]</span>: Invalid user http from 211.233.62.118<br />
20110912 04:05:35 cent sshd<span class="o">[</span>3386<span class="o">]</span>: Invalid user oracle from 203.236.203.2<br />
20110912 04:05:37 cent sshd<span class="o">[</span>3388<span class="o">]</span>: Invalid user oracle from 203.236.203.2<br />
</pre></div><br />
</div><br />
<p>あとは最後のフィールドのIPアドレスを表示するだけです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;&#39;</span> | awk <span class="s1">&#39;{print $NF}&#39;</span> | sort | uniq &gt; tmp<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head tmp<br />
110.234.96.196<br />
111.92.236.251<br />
112.65.165.131<br />
（略）<br />
</pre></div><br />
</div><br />
<p>　今度は、secureログから不正なユーザ名と、使われた回数を表示します。<br />
以下は完成したコマンドラインです。2回出てくるuniqは、</p><br />
<ul class="simple"><br />
<li>前のuniq: 連続して使われたユーザ名の回数を1と数えるために重複を除去</li><br />
<li>後のuniq: ソートされたユーザ名の個数をカウント</li><br />
</ul><br />
<p>しています。最後に使用数の多いものから上に並べて上位5個を表示しています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;{print $7}&#39;</span> | uniq | sort | uniq -c | sort -k1,1nr | head -n 3<br />
 362 <span class="nb">test</span><br />
<span class="nb"> </span>275 oracle<br />
 234 admin<br />
</pre></div><br />
</div><br />
<p>　次はaccess_logをいじります。<br />
まず、一日に何種類のIPアドレスから受信があったかを調べてみましょう。<br />
下のように、日付とIPの対でuniqして、その後日付だけ残してソートし、<br />
日付の数を数えます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&##39;{print $1,$3}&#39;</span> ACCESS_LOG | sort | uniq | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq -c &gt; tmp<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp<br />
 28 20111009<br />
 24 20111010<br />
 28 20111011<br />
 44 20111012<br />
 （略）<br />
</pre></div><br />
</div><br />
<p>昔はもっとアクセスあったんですが・・・。</p><br />
<p>　最後の例です。自分のサイトのページに対して、<br />
アクセスランキングでもつくってみましょう。<br />
まず、ステータスコード（$7）が200（OK）のものからリクエストを取り出し、<br />
パスを抜き出します。<br />
これはちょっとややこしい操作になっていますので、<br />
もしかしたらリクエストの文字列はもう少し分解したほうが良いかもしれません。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$7==200&amp;&amp;$6~/^GET/{print $6}&#39;</span> ACCESS_LOG | sed <span class="s1">&#39;s/^GET_\\(..*\\)_[^_]*$/\\1/&#39;</span> | sed <span class="s1">&#39;s/?..*//&#39;</span> &gt; tmp<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head tmp<br />
/ueda/profile.htm<br />
/paper/ARAIBO<span class="se">\\_</span>TechnicalReport2005.pdf<br />
/<br />
/araibo.css<br />
/updates.html<br />
/ueda/activity<span class="se">\\_</span>j.cgi<br />
/ueda/award.cgi<br />
/ueda/current.htm<br />
/ueda/dp.php<br />
/ueda/index.htm<br />
</pre></div><br />
</div><br />
<p>　次に、ランキング対象の拡張子を引っ張り出したいのですが、<br />
どんな拡張子があるか確認してみましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp | awk -F. <span class="s1">&#39;{print $NF}&#39;</span> | sort | uniq | tr <span class="s1">&#39;\\n&#39;</span> <span class="s1">&#39; &#39;</span><br />
/ // /haribote/ /ueda/ /usage/ /webalizer/ JPG PNG cgi com/ css gif htm html jar jpg mpeg mpg pdf php png wmv<br />
</pre></div><br />
</div><br />
<p>個人サイトにありがちな統一感の無さですが、「/」で終わっているものと、<br />
cgi、htm、html、phpあたりを対象にしましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp | awk -F. <span class="s1">&#39;$NF~/\\/$|^htm|^cgi|^php/&#39;</span> | sort | uniq -c | sort -k1,1nr | sed <span class="s1">&#39;s;\\\\_;_;g&#39;</span> | head<br />
 152 /<br />
 78 /haribote/index.php<br />
 78 /updates.html<br />
 71 /ueda/dp.php<br />
 50 /ueda/prob_robotics_j.cgi<br />
 49 /ueda/publication_j.cgi<br />
 44 /ueda/index_j.htm<br />
 42 /ueda/index_j_right.html<br />
 40 /ueda/index_j_left.htm<br />
 28 /ueda/current_j.html<br />
</pre></div><br />
</div><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>3.3. 終わりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、ログを整形するシェルスクリプトと端末でのログ集計の例を示しました。<br />
今回、forやwhileの使用はゼロでした。if文はawk中で1回だけ使いました。</p><br />
<p>　端末でのログ集計では当然グラフを描くなどの派手なことはできませんが、<br />
ログに書いてあることは何でも集計できるので、慣れておくと自由が利きます。<br />
また、「集計部分をシェルスクリプトにして、CGIから起動してブラウザで見る」<br />
ということも、他の言語と比べてもそんなに手間にならないので、<br />
機会があったら扱ってみたいと考えています。</p><br />
</div><br />
</div><br />

