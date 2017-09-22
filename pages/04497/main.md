---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年3月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>3. 開眼シェルスクリプト 第3回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>3.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　皆様、花粉症対策、万全でしょうか。筆者の場合は毎年対応をサボり、
3月に入ってから医者通いして強い薬を飲み、
半分寝たまま仕事をするのが恒例行事となっております。
早めに原因を叩いておくことが大事だとは分かっていながら、
症状が出るまではつい後回しにしてしまいます。</p>
<p>　今回の開眼シェルスクリプトはログ捌き後半です。
ログを処理しやすい形式に整形して一旦保存し、
保存した整形済みファイルを使い、端末で有用な情報を抽出します。
前回ちらっと見ましたが、Linuxやapacheが吐き出すログは、
必ずしもプログラムで処理するために最適化されていません。
シェルスクリプトで処理しやすいように整形します。</p>
<div class="section" id="id3">
<h3>3.1.1. 花粉症も厄介なデータも早めに叩くのが吉<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　お題に入る前に、例によって格言を。今回は、次の言葉を意識します。</p>
<ul>
<li><dl class="first docutils">
<dt>Data dominates. If you&#8217;ve chosen the right data structures and organized things well, the algorithms will almost always be self­evident. Data structures, not algorithms, are central to programming. (See Brooks p. 102.) [Pike1989]</dt>
<dd><p class="first last">&#8220;データが全てに優先する。もし適切なデータ構造を選んで物事を整理すれば、アルゴリズムはほとんどの場合に自明となる。アルゴリズムではなく、データ構造がプログラミングの中心である。（Brooksの102ページを見よ。）</p>
</dd>
</dl>
</li>
</ul>
<p>（脚注：[Pike1989] Rob Pike, &#8220;Notes on Programming in C&#8221;, <a class="reference external" href="http://www.lysator.liu.se/c/pikestyle.html">http://www.lysator.liu.se/c/pikestyle.html</a>, 1989. 不勉強なため未だ読んでませんが、Brooksの102ページというのは、「人月の神話」の原著の102ページのようです。）</p>
<p>　要は「データがきれいだとコードが短く簡単になる」ということを言っています。
だとしたら、なるべく根元でデータを整形するのが良い習慣と言えるでしょう。
シェルスクリプトの場合は、awkで扱いやすい形式にして、
どこか適切な場所に整形済みデータを置くことが目標となります。
これをサボると、
長いシェルスクリプトを涕泗の如く生産して振り回されることになります。
・・・花粉症のようになります。</p>
<p>　そういう観点を踏まえ、
今回はデータ整形をシェルスクリプトに残し、雑多な集計を端末で済ませます。
集計なぞ、単に何かの数を数えるくらいの処理だったらsort、
uniqと数個のawk・sedで済んでしまうことが大半で、
定期起動したりCGIスクリプトにしない限りはコードに残すと後で面倒です。
一方、データ整形は複雑なだけでなく、
扱いやすいデータを生成するという意味で価値が高いので、残す価値があります。</p>
</div>
</div>
<div class="section" id="id4">
<h2>3.2. 今回のお題：ログをさばく（後半）<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回に引き続き、Linuxのsecureログ、apacheのaccess_logを題材にします。
ホーム下に「LOG」というディレクトリを作って、
以下のように放り込んであります。
ファイルの場所は前回と同じなのですが、
secureログが前回執筆時より増えています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>ls
httpd/access_log secure-20111016
httpd/access_log.1 secure-20111023
httpd/access_log.2 secure-20111030
httpd/access_log.3 secure-20111204
httpd/access_log.4 secure-20111211
secure secure-20111218
secure-20111012 secure-20111225
</pre></div>
</div>
<p>　まず、恐れ多くも「きれいか汚いか」という観点でログにケチを付けます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head -n 1 secure httpd/access_log
<span class="o">==</span>&gt; secure &lt;<span class="o">==</span>
Nov 20 09:23:44 cent sshd<span class="o">[</span>20019<span class="o">]</span>: Did not receive identification string from 123.232.118.231

<span class="o">==</span>&gt; httpd/access_log &lt;<span class="o">==</span>
114.80.93.71 - - <span class="o">[</span>20/Nov/2011:06:47:54 +0900<span class="o">]</span> <span class="s2">&quot;GET / HTTP/1.1&quot;</span> 200 1429 <span class="s2">&quot;-&quot;</span> <span class="s2">&quot;Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)&quot;</span>
</pre></div>
</div>
<p>もともと人が読むものなのでこれでもよいのですが、
プログラムでログを集計しようとすれば以下の点が問題です。</p>
<ul class="simple">
<li>secureに西暦年がついていない</li>
<li>どちらのログも月の表記が数字でない</li>
<li>access_logのデータの区切り方が統一されていない</li>
</ul>
<p>これらを残しておくと、情報を引き出すときに毎回大変な目に遭います。</p>
<p>　ということで、ログをきれいにします。
実のところ、前回の「他に方法がないことが実験により明らかである場合に限り、
大きいプログラムを書け。」という格言に従えば、
ログの発生元をカスタマイズするのが最良の方法です。
しかし、それでは話が終わってしまうので、
シェルスクリプトで簡潔にします。すんません・・・。</p>
<div class="section" id="secure">
<h3>3.2.1. secureログ整形シェルスクリプト<a class="headerlink" href="#secure" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まずsecureログから。このログの最大の問題は、
ログ発生の月日は書いてあっても年が書いてないことです。
長期にわたるログの解析や、年をまたいだログのソートができなくなってしまいます。
前回は、tacを使って年を付加するトリッキーな処理を書きましたが、
今回はもう少し簡単な方法を使います。
幸い私のCentOS6の環境ではデフォルトの状態で過去のログのファイル名に
年月日が付いているので、これを使って</p>
<ul class="simple">
<li>ある日のログファイルに、その日以降のログがあったらそれは前の年のログ</li>
</ul>
<p>と決めつけて日付に年をつけます。</p>
<p>　さっそく格言どおり、データ側の都合でアルゴリズムを考える必要が出てきました。
最初からログに年情報があればこんなことはしなくてよいのです。
そういう意味では、過去のログに年月日が付いているので、少し負担は減りました。
その代わりに、ポータビリティーは犠牲になります。</p>
<p>　ログファイルの日付をログに付加する処理をリスト1に示します。
8行目で最新のsecureファイルに今日の日付をつけて/tmpにコピーします。
理由は後で説明します。下手な排他ではありません。
10行目のawk中の「FILENAME」は、ファイル名が入った変数です。
10行目の処理で、各ログの先頭にファイル名が入ります。
13行目のsedで、ファイル名から日付以外の文字を除去します。
正規表現 <tt class="docutils literal"><span class="pre">^[^-]*-</span></tt> は、
「行頭からハイフンでない文字が続いた後にハイフン」という意味です。</p>
<p>　結局、8行目のコピーはsecureファイルのファイル名に日付を入れて、
過去のログ（secure-日付）と同じ処理ができるようにするだけのために行ったものでした。
ファイル名もデータの一部なので、
やはり正規化しておいた方がアルゴリズムが簡単になります。
速度にこだわる人はシンボリックリンクを使う手もあります。</p>
<p>▼リスト1: ログにログファイルの日付をつける</p>
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
17</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="nb">cd</span> <span class="nv">$dir</span>/LOG
cat secure &gt; <span class="nv">$tmp</span>-<span class="nv">$today</span>

awk <span class="s1">&#39;{print FILENAME,$0}&#39;</span> secure-* <span class="nv">$tmp</span>-<span class="nv">$today</span> |
<span class="c">#1:ファイル名 2:ログの内容</span>
<span class="c">#過去のログファイル名から年月日だけ取り出す</span>
sed -e <span class="s1">&#39;s/^[^-]*-//&#39;</span> |
<span class="c">#1:ファイル年月日 2:ログの内容</span>
<span class="c">#年と月日を分ける</span>
sed -e <span class="s1">&#39;s/^..../&amp; /&#39;</span>
<span class="c">#1:ファイル年 2:ファイル月日 3:ログの内容</span>
</pre></div>
</td></tr></table></div>
<p>リスト1のスクリプトを実行すると、出力は次のようになります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./SECURE_NORMALIZE | head -n 2
2011 1012 Sep 11 19:15:23 localhost runuser: pam_un
2011 1012 Sep 11 19:15:23 localhost runuser: pam_un
<span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./SECURE_NORMALIZE | tail -n 2
2011 1230 Dec 30 13:40:03 cent sshd<span class="o">[</span>31763<span class="o">]</span>: Connect
2011 1230 Dec 30 13:40:06 cent su: pam_unix<span class="o">(</span>su-l:se
</pre></div>
</div>
<p>　次にログ自体の日付を正規化していきます。
リスト2のスクリプトで、日付を数字にして正規化できます。
コメントが多いので一見すると雑然としていますが、
パイプの部分はawk5個、sed4個で済んでいます。</p>
<p>▼リスト2: secureログの整形スクリプト</p>
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>
<span class="c">#</span>
<span class="c"># SECURE_NORMALIZE secureログの正規化</span>
<span class="c">#</span>
<span class="c"># usage: ./SECURE_NORMALIZE</span>
<span class="c"># written by R. Ueda (USP研究所) Dec. 30, 2011</span>

<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="nb">cd</span> <span class="nv">$dir</span>/LOG
cat secure &gt; <span class="nv">$tmp</span>-<span class="nv">$today</span>

<span class="c">#前半のコメントは省略</span>
awk <span class="s1">&#39;{print FILENAME,$0}&#39;</span> secure-* <span class="nv">$tmp</span>-<span class="nv">$today</span> |
sed -e <span class="s1">&#39;s/^[^-]*-//&#39;</span> |
sed -e <span class="s1">&#39;s/^..../&amp; /&#39;</span> |
<span class="c">#1:ファイル年 2:ファイル月日 3:ログの内容</span>
<span class="c">#出力例：2011 1230 Dec 30 13:40:06 cent su: pam_u</span>
<span class="c">#月だけ頭に出して英語表記を数字表記に変える</span>
awk <span class="s1">&#39;{print $3,$0}&#39;</span> |
<span class="c">#1:ログ月 2:ファイル年 3:ファイル月日 4:ログの内容</span>
<span class="c">#前回登場した月の英語表記を数字に変換するsedスクリプト</span>
sed -f <span class="nv">$dir</span>/SYS/MONTH - |
<span class="c">#ログから日付を持ってきてログ月にくっつける</span>
<span class="c">#一桁の日付を二桁に（既出のgsubを使うが普通はsprintf）</span>
awk <span class="s1">&#39;{gsub(/^.$/,&quot;0&amp;&quot;,$5);$1=$1$5;print}&#39;</span> |
<span class="c">#1:ログ月日 2:ファイル年 3:ファイル月日 4:ログの内容</span>
<span class="c">#ログの月日がファイルの月日より後なら昨年のデータ</span>
awk <span class="s1">&#39;{if($1&gt;$3){$2--};print}&#39;</span> |
<span class="c">#1:ログ月日 2:ログ年 3:ファイル月日 4:ログの内容</span>
<span class="c">#出力例：0911 2011 1012 Sep 11 19:17:44 localhost</span>
awk <span class="s1">&#39;{$1=$2$1;$2=&quot;&quot;;$3=&quot;&quot;;$4=&quot;&quot;;$5=&quot;&quot;;print}&#39;</span> |
<span class="c">#日付の後に無駄なスペースがたくさん入るので消す</span>
sed -e <span class="s1">&#39;s/ */ /&#39;</span> &gt; <span class="nv">$dir</span>/LOG/SECURE

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>これで、次の出力のように日付が数字で表現できます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>tail -n 3 ../LOG/SECURE
20111230 13:39:16 cent su: pam_unix<span class="o">(</span>su-l:sessio
20111230 13:40:03 cent sshd<span class="o">[</span>31763<span class="o">]</span>: Connection
20111230 13:40:06 cent su: pam_unix<span class="o">(</span>su-l:sessio
</pre></div>
</div>
</div>
<div class="section" id="access-log">
<h3>3.2.2. access_logログ整形シェルスクリプト<a class="headerlink" href="#access-log" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次にaccess_logを整形します。これも大変です。
access_logには、左から順に9項目の情報が記述されています。
私は全項目を人に解説できるほどの知識は無いので詳しくは
<a class="reference external" href="http://httpd.apache.org/docs/2.2/ja/logs.html">http://httpd.apache.org/docs/2.2/ja/logs.html</a>
等を参照願いたいのですが、大雑把に説明すると、</p>
<blockquote>
<div>1.クライアントのIP、2.ユーザ名A、3.ユーザ名B、
4.アクセス日時、5.クライアントからの要求、6.ステータスコード、
7.転送バイト数、8.参照元サイト、9.クライアントの情報</div></blockquote>
<p>です。</p>
<p>　整形の方法は一種類だけではありませんが、
ここではawkにあわせて空白区切りのデータにします。
その後、日時を8桁6桁に整形します。
整形の際、もともとデータ内にある空白が邪魔なので、</p>
<ul class="simple">
<li>空白はアンダースコア「_」に変換</li>
<li>アンダースコアは「 <tt class="docutils literal"><span class="pre">\\_</span></tt> 」に変換</li>
</ul>
<p>します。また、区切りに使われている&#8221; &#8220;や[ ]など、
余計な文字は取り去ります。</p>
<p>　まず、空白区切りにするところまでの処理をリスト2に示します。
sedを使うと以下のようになります。
6行目のsedがお化けみたいになっていますが、
前半の正規表現はレコード全体に一致するように書いてあります。
これで、1から9までに各項目が入ります。
「でりみた」という文字は、暫定的に区切りにする文字列です。
ファイル中に存在する可能性がほぼゼロの文字列ならば何でもかまいません。</p>
<p>▼リスト3: access_logを空白区切りにするまでのスクリプト</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c"># HTTPD_ACCESS_NORMALIZEスクリプト</span>

cat <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> |
<span class="c">#「でりみた」という文字を区切り文字にデータを分ける。</span>
sed -e <span class="s1">&#39;s/^\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$/\\1でりみた\\2でりみた\\3でりみた\\4でりみた\\5でりみた\\6でりみ&gt;た\\7でりみた\\8でりみた\\9/&#39;</span> |
<span class="c">#_を\\_に</span>
sed -e <span class="s1">&#39;s/_/\\\\_/g&#39;</span> |
<span class="c">#空白を_に</span>
sed -e <span class="s1">&#39;s/ /_/g&#39;</span> |
<span class="c">#デリミタを空白に</span>
sed -e <span class="s1">&#39;s/でりみた/ /g&#39;</span>
</pre></div>
</td></tr></table></div>
<p>出力は例えば次のようになります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE 2&gt; /dev/null | head -n 1
180.76.5.49 - - 13/Nov/2011:05:55:20_+0900 GET_/ueda/profile.htm_HTTP/1.1 200 1841 - Mozilla/5.0_<span class="o">(</span>compatible;_Baiduspider/2.0;_+http://www.baidu.com/search/spider.html<span class="o">)</span>
</pre></div>
</div>
<p>　ちゃんと9フィールドになっているか調べるには、awkを使います。
NFは、読み込んだレコードのフィールド数が入る変数です。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE 2&gt; /dev/null | awk <span class="s1">&#39;{print NF}&#39;</span> | uniq
9
</pre></div>
</div>
<p>　6行目のsedはお化けみたいでちょっとという方には、
リスト4のようにawkを使って分割する方法があります。
この方法は、日本 gnu awk ユーザー会の斉藤さんから教えていただいたものです。
awkの-Fは、入力の区切り文字を指定するオプションです。
この例では「&#8221;」を区切り文字に指定しています。
（エスケープするために <tt class="docutils literal"><span class="pre">\\&quot;</span></tt> と指定しています。）</p>
<p>▼リスト4: awkを使ったaccess_logの整形</p>
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
cat <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> &gt; <span class="nv">$tmp</span>-data

awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $1}&#39;</span> <span class="nv">$tmp</span>-data |
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),$0}&#39;</span> |
awk <span class="s1">&#39;{print $1,1,$2;print $1,2,$3;\\</span>
<span class="s1"> print $1,3,$4;print $1,4,$5,$6}&#39;</span> &gt; <span class="nv">$tmp</span>-1-4

awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $2}&#39;</span> <span class="nv">$tmp</span>-data |
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),5,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-5

awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $3}&#39;</span> <span class="nv">$tmp</span>-data |
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),$0}&#39;</span> |
awk <span class="s1">&#39;{print $1,6,$2;print $1,7,$3}&#39;</span> &gt; <span class="nv">$tmp</span>-6-7

awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $4}&#39;</span> <span class="nv">$tmp</span>-data |
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),8,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-8

awk -F<span class="se">\\&quot;</span> <span class="s1">&#39;{print $6}&#39;</span> <span class="nv">$tmp</span>-data |
awk <span class="s1">&#39;{print sprintf(&quot;%010s&quot;,NR),9,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-9

sort -m -k1,2 -s <span class="nv">$tmp</span>-<span class="o">{</span>1-4,5,6-7,8,9<span class="o">}</span>
</pre></div>
</td></tr></table></div>
<p>　リスト4のコードで、次の出力のように縦にデータが整理されます。
一番左のコードはレコード番号です。
こちらの方が空白も残っていて、自分で区切り文字を作る必要もありません。
ただ、整形したデータをさらにawkで捌こうとするなら、
データは縦でなく横並びになっていた方が楽ちんです。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>./HTTPD_ACCESS_NORMALIZE.awk | head -n 9
0000000001 1 180.76.5.49
0000000001 2 -
0000000001 3 -
0000000001 4 <span class="o">[</span>13/Nov/2011:05:55:20 +0900<span class="o">]</span>
0000000001 5 GET /ueda/profile.htm HTTP/1.1
0000000001 6 200
0000000001 7 1841
0000000001 8 -
0000000001 9 Mozilla/5.0 <span class="o">(</span>compatible; Baiduspider/2.0（略）
</pre></div>
</div>
<p>　sed版の続きを作成しましょう。日時を加工する部分を記述します。
完成したものをリスト5に示します。コードの部分はたった14行です。
このコードは、紙面で見やすくするために変数を使ったり、
エスケープの&#8221;や&#8217;を使い分けたりしてコンパクトに書いていますが、
ベタに書いて動けば十分です。</p>
<p>▼リスト5: access_logの整形スクリプト</p>
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
34</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>
<span class="c">#</span>
<span class="c"># HTTP_ACCRESS_NORMALIZE accrss_logの正規化</span>
<span class="c"># usage: ./HTTP_ACCESS_NORMALIZE</span>
<span class="c">#</span>
<span class="c"># written by R. Ueda (USP研究所) Nov. 29, 2011</span>
<span class="nv">dir</span><span class="o">=</span>/home/ueda/GIHYO

<span class="nv">dlmt</span><span class="o">=</span>ﾃﾞﾞﾃﾘﾞﾃﾞﾘﾃﾞﾞﾞﾘﾞﾃﾞﾘﾞ
<span class="nv">reg</span><span class="o">=</span><span class="s1">&#39;^\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$&#39;</span>
<span class="nv">str</span><span class="o">=</span><span class="s2">&quot;\\\\1$dlmt\\\\2$dlmt\\\\3$dlmt\\\\4$dlmt\\\\5$dlmt\\\\6$dlmt\\\\7$dlmt\\\\8$dlmt\\\\9&quot;</span>

<span class="c">#&quot;や[ ]、空白を目印にレコードを9分割する。</span>
sed <span class="s2">&quot;s;$reg;$str;&quot;</span> <span class="nv">$dir</span>/LOG/httpd/access_<span class="o">{</span>log.*,log<span class="o">}</span> |
<span class="c">#_を\\_に</span>
sed <span class="s1">&#39;s/_/\\\\_/g&#39;</span> |
<span class="c">#空白を_に</span>
sed <span class="s1">&#39;s/ /_/g&#39;</span> |
<span class="c">#デリミタを空白に戻す</span>
sed <span class="s2">&quot;s/$dlmt/ /g&quot;</span> |
<span class="c">#出力例：119.147.75.140 - - 23/Nov/2011:15:14:13_+0900 ...</span>
<span class="c">#日時を先頭に</span>
awk <span class="s1">&#39;{a=$4;$4=&quot;&quot;;print a,$0}&#39;</span> |
<span class="c">#出力例：23/Nov/2011:15:14:13_+0900 119.147.75.140 - - ...</span>
sed <span class="s1">&#39;s;^\\(..\\)/\\(...\\)/\\(....\\):\\(..\\):\\(..\\):\\(..\\)_[^ ]*;\\2 \\1 \\3 \\4\\5\\6;&#39;</span> |
<span class="c">#出力例：Nov 23 2011 151413 119.147.75.140 - - ...</span>
sed -f <span class="nv">$dir</span>/SYS/MONTH |
<span class="c">#出力例：11 23 2011 151413 119.147.75.140 - - ...</span>
awk <span class="s1">&#39;{d=$3$1$2;$1=&quot;&quot;;$2=&quot;&quot;;$3=&quot;&quot;;print d,$0}&#39;</span> |
<span class="c">#1:日付 2:時刻 3-10:あとの項目</span>
<span class="c">#間延びした区切りの空白を戻す。</span>
sed <span class="s1">&#39;s/ */ /g&#39;</span> &gt; <span class="nv">$dir</span>/LOG/ACCESS_LOG

<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent SYS<span class="o">]</span><span class="nv">$ </span>head -n 3 ../LOG/ACCESS_LOG
20111030 062140 66.249.67.163 - - GET_/robots.txt_HTTP/1.1 4
20111030 062140 209.85.238.184 - - GET_/paper/ARAIBO<span class="se">\\_</span>Techni
20111030 072937 123.125.71.72 - - HEAD_/paper/ARAIBO<span class="se">\\_</span>Techni
</pre></div>
</div>
</div>
<div class="section" id="id5">
<h3>3.2.3. あとは端末でさっと処理<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、整形したものから情報を取り出してみましょう。</p>
<p>　まず、secureログから、不正なユーザでアクセスしてきたIPでも抽出しましょう。
まず、sshdのログの「Invalid user」のレコードを抽出します。
下の例のように、headを使って出力を確認しながら書いていきます。
一度入力したコマンド列は、bashの場合、上ボタンを押すと再利用できます。
筆者の場合、一つコマンドを書いたら出力して確認することを繰り返しながら、
泥縄式にコマンドを並べていく場合が多いです。
多少コマンドが多くなっても、ファイルにプログラムを書いて動作確認して・・・
という方法よりは、さっさと終わります。
慣れないうちは、リダイレクトを使ってファイルにデータを貯めて確認しながら練習しましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;&#39;</span> | head -n 3
20110912 00:57:32 cent sshd<span class="o">[</span>2942<span class="o">]</span>: Invalid user http from 211.233.62.118
20110912 04:05:35 cent sshd<span class="o">[</span>3386<span class="o">]</span>: Invalid user oracle from 203.236.203.2
20110912 04:05:37 cent sshd<span class="o">[</span>3388<span class="o">]</span>: Invalid user oracle from 203.236.203.2
</pre></div>
</div>
<p>あとは最後のフィールドのIPアドレスを表示するだけです。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;&#39;</span> | awk <span class="s1">&#39;{print $NF}&#39;</span> | sort | uniq &gt; tmp
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head tmp
110.234.96.196
111.92.236.251
112.65.165.131
（略）
</pre></div>
</div>
<p>　今度は、secureログから不正なユーザ名と、使われた回数を表示します。
以下は完成したコマンドラインです。2回出てくるuniqは、</p>
<ul class="simple">
<li>前のuniq: 連続して使われたユーザ名の回数を1と数えるために重複を除去</li>
<li>後のuniq: ソートされたユーザ名の個数をカウント</li>
</ul>
<p>しています。最後に使用数の多いものから上に並べて上位5個を表示しています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$4~/^sshd/&#39;</span> SECURE | awk <span class="s1">&#39;$5==&quot;Invalid&quot;&#39;</span> | awk <span class="s1">&#39;$6==&quot;user&quot;{print $7}&#39;</span> | uniq | sort | uniq -c | sort -k1,1nr | head -n 3
 362 <span class="nb">test</span>
<span class="nb"> </span>275 oracle
 234 admin
</pre></div>
</div>
<p>　次はaccess_logをいじります。
まず、一日に何種類のIPアドレスから受信があったかを調べてみましょう。
下のように、日付とIPの対でuniqして、その後日付だけ残してソートし、
日付の数を数えます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&##39;{print $1,$3}&#39;</span> ACCESS_LOG | sort | uniq | awk <span class="s1">&#39;{print $1}&#39;</span> | uniq -c &gt; tmp
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp
 28 20111009
 24 20111010
 28 20111011
 44 20111012
 （略）
</pre></div>
</div>
<p>昔はもっとアクセスあったんですが・・・。</p>
<p>　最後の例です。自分のサイトのページに対して、
アクセスランキングでもつくってみましょう。
まず、ステータスコード（$7）が200（OK）のものからリクエストを取り出し、
パスを抜き出します。
これはちょっとややこしい操作になっていますので、
もしかしたらリクエストの文字列はもう少し分解したほうが良いかもしれません。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;$7==200&amp;&amp;$6~/^GET/{print $6}&#39;</span> ACCESS_LOG | sed <span class="s1">&#39;s/^GET_\\(..*\\)_[^_]*$/\\1/&#39;</span> | sed <span class="s1">&#39;s/?..*//&#39;</span> &gt; tmp
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head tmp
/ueda/profile.htm
/paper/ARAIBO<span class="se">\\_</span>TechnicalReport2005.pdf
/
/araibo.css
/updates.html
/ueda/activity<span class="se">\\_</span>j.cgi
/ueda/award.cgi
/ueda/current.htm
/ueda/dp.php
/ueda/index.htm
</pre></div>
</div>
<p>　次に、ランキング対象の拡張子を引っ張り出したいのですが、
どんな拡張子があるか確認してみましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp | awk -F. <span class="s1">&#39;{print $NF}&#39;</span> | sort | uniq | tr <span class="s1">&#39;\\n&#39;</span> <span class="s1">&#39; &#39;</span>
/ // /haribote/ /ueda/ /usage/ /webalizer/ JPG PNG cgi com/ css gif htm html jar jpg mpeg mpg pdf php png wmv
</pre></div>
</div>
<p>個人サイトにありがちな統一感の無さですが、「/」で終わっているものと、
cgi、htm、html、phpあたりを対象にしましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat tmp | awk -F. <span class="s1">&#39;$NF~/\\/$|^htm|^cgi|^php/&#39;</span> | sort | uniq -c | sort -k1,1nr | sed <span class="s1">&#39;s;\\\\_;_;g&#39;</span> | head
 152 /
 78 /haribote/index.php
 78 /updates.html
 71 /ueda/dp.php
 50 /ueda/prob_robotics_j.cgi
 49 /ueda/publication_j.cgi
 44 /ueda/index_j.htm
 42 /ueda/index_j_right.html
 40 /ueda/index_j_left.htm
 28 /ueda/current_j.html
</pre></div>
</div>
</div>
</div>
<div class="section" id="id6">
<h2>3.3. 終わりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、ログを整形するシェルスクリプトと端末でのログ集計の例を示しました。
今回、forやwhileの使用はゼロでした。if文はawk中で1回だけ使いました。</p>
<p>　端末でのログ集計では当然グラフを描くなどの派手なことはできませんが、
ログに書いてあることは何でも集計できるので、慣れておくと自由が利きます。
また、「集計部分をシェルスクリプトにして、CGIから起動してブラウザで見る」
ということも、他の言語と比べてもそんなに手間にならないので、
機会があったら扱ってみたいと考えています。</p>
</div>
</div>

