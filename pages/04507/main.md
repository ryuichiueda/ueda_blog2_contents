---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年5月号
出典: 技術評論社SoftwareDesign

 
 <div class="section" id="id1">
<h1>5. 開眼シェルスクリプト 第5回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>5.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　開眼シェルスクリプトも第5回になりました。
今回は、これまでのテクニックを駆使して、
アプリケーションを作ることに挑戦します。
お題はapacheのログを解析してアクセス数等をHTMLにするソフトです。
「車輪の再発明だ！」と言われてしまいそうですが、今回は
「ソフトをインストールして使いこなすまでの時間よりも早く作ってしまえ」
という立場で押し切ります。</p>
<div class="section" id="id3">
<h3>5.1.1. 車輪を使って車輪を超高速再発明<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　毎度おなじみガンカーズのUNIX哲学には、</p>
<p>「できる限り原型（プロトタイプ）を作れ。」</p>
<p>という項目がありますが、
これはコマンドを組み合わせたシェルスクリプトでさっさと動くものを作って人に見せろということです。
コマンドを使いまわす方法が手っ取り早いことは昔も今もそんなに変わっていません。
テトリスの上手な人はものすごいスピードでブロックを落としていきますが、
良く使うコマンドの組み合わせが一通り頭に入ると同じような感覚を味わうことになります。</p>
<p>　それに、コマンド自体は一つ一つ非常に有能で長い間使われてきた車輪です。
これを組み合わせてアプリケーションを作る行為自体は、
車輪を再発明しない工夫でもあります。
筆者はそれを再び広めたいのです。と言い訳して本題に入ります。</p>
</div>
</div>
<div class="section" id="id4">
<h2>5.2. お題：お手製アクセス解析ソフトを作る<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　アクセス解析ソフトとしては、Webalizerが有名で筆者も使っていますが、
もうちょっと気の利いたことをしたい場合に拡張するのは大変です。
グラフ以外はシェルスクリプトでさっと書けるので、自分で作ってしまいましょう。
グラフも、前回の応用でなんとかなります。</p>
<p>　解析対象は、USP友の会のウェブサイト（脚注:<a class="reference external" href="http://www.usptomonokai.jp">http://www.usptomonokai.jp</a>）です。
このサイト、bash製という珍品ですが、ログはいたって普通です。
余計なことですが、このbashウェブシステムは私が半日で作り、
次の日&#64;nullpopopo氏とネットワーク設定をして公開したものです。
車輪の再発明コストは相当低いと思います。</p>
<p>　ログは~/LOGの下に溜まっていくようになっていて、
root以外でも読み込み可能にしてあります。</p>
<p>↓リスト1: アクセスログ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura LOG<span class="o">]</span><span class="nv">$ </span>ls -ltr access_log* | tail -n 5
-rw-r--r-- 1 root root 82408 2月 22 03:32 access_log-20120222.gz
-rw-r--r-- 1 root root 61438 2月 23 03:32 access_log-20120223.gz
-rw-r--r-- 1 root root 70638 2月 24 03:32 access_log-20120224.gz
-rw-r--r-- 1 root root 60125 2月 25 03:32 access_log-20120225.gz
-rw-r--r-- 1 root root 744255 2月 25 22:02 access_log
</pre></div>
</td></tr></table></div>
<p>このデータを解析して、ブラウザで見やすいHTMLを作ることが、
お手製アクセス解析ソフトの目指すところです。</p>
<div class="section" id="id5">
<h3>5.2.1. 準備<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　作る前に、場所を作りましょう。適当な場所に、
リスト2のようにディレクトリを掘ってください。</p>
<p>↓リスト2: ディレクトリ構造</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WWW<span class="o">]</span><span class="nv">$ </span>tree -L 1 WEB_KAISEKI
WEB_KAISEKI
|-- HTML <span class="c">#HTMLのテンプレート置き場</span>
|-- SCR <span class="c">#シェルスクリプト置き場</span>
<span class="sb">`</span>-- TMP <span class="c">#作成したファイル置き場</span>
</pre></div>
</div>
<p>「WEB_KAISEKI」というのがこのソフトの名前です。
（脚注：英語でなくてローマ字なのは業務上の癖なので突っ込まないでください。）</p>
</div>
<div class="section" id="id6">
<h3>5.2.2. ログの整理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まずSCRの下に、
3月号で作った「apacheのログをきれいにするスクリプト」を置きます。
前回Tukubaiコマンド（参照：<a class="reference external" href="http://uec.usp-lab.com">http://uec.usp-lab.com</a>）を紹介したので、
Tukubaiのコマンドを使って簡略化してリスト3に再掲します。
また、その他の部分も環境と目的に合わせて微調整してあります。</p>
<p>↓リスト3: apacheのログを整理するスクリプト</p>
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>cat SCR/HTTPD_ACCESS_NORMALIZE
<span class="c">#!/bin/bash</span>

<span class="nv">logdir</span><span class="o">=</span>/home/hoge/LOG
<span class="nv">dir</span><span class="o">=</span>/home/hoge/WWW/WEB_KAISEKI

<span class="nb">echo</span> <span class="nv">$logdir</span>/access_log*.gz |
xargs zcat |
cat - <span class="nv">$logdir</span>/access_log |
sed <span class="s1">&#39;s/&quot;&quot;/&quot;-&quot;/g&#39;</span> |
sed <span class="s1">&#39;s/\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$/\\1あ\\2あ\\3あ\\4あ\\5あ\\6あ\\7あ\\8あ\\9/&#39;</span> |
sed -e <span class="s1">&#39;s/_/＿/g&#39;</span> -e <span class="s1">&#39;s/ /_/g&#39;</span> -e <span class="s1">&#39;s/あ/ /g&#39;</span> |
<span class="c">#1:IP 2,3:id 4:日時 5-9:リクエスト以降</span>
self 4.4.3 4.1.2 4.8.4 4.13.8 1/3 5/NF |
<span class="c">#1:月 2:日 3:年 4:時:分:秒 5:IP 6,7:id 8-12:リクエスト以降</span>
sed -f <span class="nv">$dir</span>/SCR/MONTH |
<span class="c">#↑参考：https://github.com/ryuichiueda/SoftwareDesign/blob/master/201202/MONTH.sed</span>
<span class="c">#時分秒のコロンを取る</span>
awk <span class="s1">&#39;{gsub(/:/,&quot;&quot;,$4);print}&#39;</span> |
<span class="c">#年月日の空白を取る</span>
awk <span class="s1">&#39;{print $3$1$2,$4,$5,$6,$7,$8,$9,$10,$11,$12}&#39;</span> |
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト以降</span>
sort -s -k1,2 &gt; <span class="nv">$dir</span>/TMP/ACCESS_LOG
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト 7:ステータス 8以降:今回不使用</span>
</pre></div>
</td></tr></table></div>
<p>　ここで使っているTukubaiコマンドは、 <tt class="docutils literal"><span class="pre">self</span></tt> です。
selfは、awkの文字を切り出す機能を単純化したコマンドです。
リスト4を見れば、awkのsubstrの動作と似ていることが分かると思います。
また、リスト1の15行目の <tt class="docutils literal"><span class="pre">1/3</span></tt> というのは1～3フィールド、
<tt class="docutils literal"><span class="pre">5/NF</span></tt> というのは5～最終フィールドのことです。</p>
<p>↓リスト４：selfの使用例</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#第1Fと、第1Fの3文字目以降、第2Fの1文字目から2文字抽出</span>
<span class="nv">$ </span><span class="nb">echo </span>abcd 1234 | self 1 1.3 2.1.2
abcd <span class="nb">cd </span>12
<span class="c">#次のawkと等価</span>
<span class="nv">$ </span><span class="nb">echo </span>abcd 1234 | awk <span class="s1">&#39;{print $1,substr($1,3),substr($2,1,2)}&#39;</span>
abcd <span class="nb">cd </span>12
</pre></div>
</div>
<p>　その他、リスト3のスクリプトの変更点は次のとおりです。</p>
<p>　まず、7, 8行目は <tt class="docutils literal"><span class="pre">zcat</span> <span class="pre">$logdir/access_log*.gz</span></tt> と書いてもよいのですが、
ファイル数が非常に多くなるとエラーが出るのでそれを回避しています。
（こうしなくても10年は大丈夫なのですが。）
また、10行目で空データ <tt class="docutils literal"><span class="pre">&quot;&quot;</span></tt> を <tt class="docutils literal"><span class="pre">&quot;-&quot;</span></tt> に変換してから
11行目でフィールド分割しています。
12行目のsedでは、 <tt class="docutils literal"><span class="pre">_</span></tt> を全角の <tt class="docutils literal"><span class="pre">＿</span></tt> 、半角空白を <tt class="docutils literal"><span class="pre">_</span></tt> 、
一時的なデリミタである「あ」を半角空白に変換しています。
二つ以上の変換を一回のsedで行う場合は、
12行目のように-eというオプションを付けます。</p>
<p>このスクリプトを実行して、日付・時刻ソートされた以下のようなデータが得られればOKです。
第3フィールドにはIPアドレスやホスト名が記録されることがありますが、
今回は「IPアドレス」あるいは「IP」と表記します。</p>
<p>↓リスト5: ファイル「ACCESS_LOG」のレコード</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#フィールド数は10列</span>
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト 7:ステータス 8以降:今回不使用</span>
<span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;{print NF}&#39;</span> TMP/ACCESS_LOG | uniq
10
<span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>tail -n 2 TMP/ACCESS_LOG
20120225 221853 72.14.199.225 - - GET_/TOMONOKAI＿CMS/CGI/TOMONOKAI＿CMS.CGI_HTTP/1.1 200 16920 - Feedfetcher-Google;_<span class="o">(</span>略<span class="o">)</span>
20120225 221946 210.128.183.1 - - GET_/TOMONOKAI＿CMS/HTML/rss20.xml_HTTP/1.0 200 10233 - Mozilla/4.0_<span class="o">(</span>compatible;<span class="o">)</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h3>5.2.3. 集計データをつくる<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて、「きれいなデータ」ACCESS_LOGを作ったので、
次は自分の解析したい情報をそこから抽出します。
何をしようか考えたのですが、とりあえずWebalizerが出力する基本的な数値である
「Hits, Files, Pages, Visits, Sites」をちゃんと集計したいと思います。</p>
<table border="1" class="docutils">
<colgroup>
<col width="33%" />
<col width="67%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">項目</th>
<th class="head">意味</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>Hits（ヒット数）</td>
<td>access_logに記録されたレコード数</td>
</tr>
<tr class="row-odd"><td>Files（ファイル数）</td>
<td>Hitsのうち、正常にアクセスされた数</td>
</tr>
<tr class="row-even"><td>Pages（ページ数）</td>
<td>正常にアクセスされたページ（画面）数</td>
</tr>
<tr class="row-odd"><td>Sites（サイト数）</td>
<td>ヒット数の集計対象のレコード中にある、IPの種類の数</td>
</tr>
<tr class="row-even"><td>Visits（訪問数）</td>
<td>ページ数の集計対象レコードから、30分以内の同一IPのレコードを重複として取り除いた数</td>
</tr>
</tbody>
</table>
<p>　これらを時間単位で集計するシェルスクリプトをリスト6,7に示します。
これらのスクリプトを実行すると、TMP下にリスト8のようなファイルが出力されます。</p>
<p>↓リスト6: 集計スクリプト（hit,file,site数）</p>
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c"># COUNT.HIT_FILE_SITE.HOUR: hit,file,siteの時間別集計</span>
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com)</span>

<span class="nb">cd</span> /home/hoge/WWW/WEB_KAISEKI/TMP

<span class="c">###ヒット数</span>
self 1 2.1.2 ACCESS_LOG |
<span class="c">#1:年月日 2:時</span>
count 1 2 &gt; HITS.COUNT
<span class="c">#1:年月日 2:時 3:数</span>

<span class="c">###ファイル数</span>
awk <span class="s1">&#39;$7==200&#39;</span> ACCESS_LOG |
self 1 2.1.2 |
<span class="c">#1:IP 2:時</span>
count 1 2 &gt; FILES.COUNT
<span class="c">#1:年月日 2:時 3:数</span>

<span class="c">###サイト数（時間別）</span>
self 1 2.1.2 3 ACCESS_LOG |
<span class="c">#1:日付 2:時 3:IP</span>
sort -su |
count 1 2 &gt; SITES.COUNT
<span class="c">#1:年月日 2:時 3:数</span>
</pre></div>
</td></tr></table></div>
<p>↓リスト7: 集計スクリプト（page,visit数）</p>
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
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>
<span class="c"># COUNT.HOUR: page,visitの時間別集計</span>
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com)</span>

<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nb">cd</span> /home/hoge/WWW/WEB_KAISEKI/TMP

<span class="c">###ページ数</span>
<span class="c">#ステイタス200、メソッドGETのデータだけ</span>
awk <span class="s1">&#39;$7==200 &amp;&amp; $6~/^GET/&#39;</span> ACCESS_LOG |
self 1/3 6 |
<span class="c">#1:年月日 2:時分秒 3:IP 4:リクエスト</span>
<span class="c">#プロトコルや?以降の文字列を削る</span>
sed -e <span class="s1">&#39;s;_HTTP/.*$;;&#39;</span> -e <span class="s1">&#39;s;\\?.*$;;&#39;</span> |
<span class="c">#集計対象を検索</span>
egrep <span class="s1">&#39;GET_//*$|TOMONOKAI＿CMS\\.CGI$&#39;</span> |
tee <span class="nv">$tmp</span>-pages |
self 1 2.1.2 |
count 1 2 &gt; PAGES.HOUR

<span class="c">###訪問数</span>
<span class="c">#1:年月日 2:時分秒 3:IP 4:リクエスト</span>
self 3 1 2 2.1.2 2.3.2 <span class="nv">$tmp</span>-pages |
<span class="c">#1:IP 2:年月日 3:時分秒 4:時 5:分</span>
<span class="c">#$4,$5を分に換算（頭にゼロがあっても大丈夫）</span>
awk <span class="s1">&#39;{print $1,$2,$3,$4*60+$5}&#39;</span> |
<span class="c">#1:IP 2:年月日 3:時分秒 4:分</span>
<span class="c">#IP、年月日、時分秒でソートする</span>
sort -k1,3 -s |
awk <span class="s1">&#39;{if(ip!=$1||day!=$2||$4-tm&gt;=30){</span>
<span class="s1"> print;ip=$1;day=$2;tm=$4}}&#39;</span> |
self 2 3.1.2 1 |
<span class="c">#1:年月日 2:時 3:IP</span>
sort -k1,2 -s |
count 1 2 &gt; VISITS.HOUR

rm -f <span class="nv">$tmp</span>-*
</pre></div>
</td></tr></table></div>
<p>↓リスト8：出力</p>
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura TMP<span class="o">]</span><span class="nv">$ </span>tail -n 1 ./*.HOUR
<span class="o">==</span>&gt; ./FILES.HOUR &lt;<span class="o">==</span>
20120225 21 <span class="nv">125</span>

<span class="o">==</span>&gt; ./HITS.HOUR &lt;<span class="o">==</span>
20120225 21 <span class="nv">189</span>

<span class="o">==</span>&gt; ./PAGES.HOUR &lt;<span class="o">==</span>
20120225 21 <span class="nv">51</span>

<span class="o">==</span>&gt; ./SITES.HOUR &lt;<span class="o">==</span>
20120225 21 <span class="nv">34</span>

<span class="o">==</span>&gt; ./VISITS.HOUR &lt;<span class="o">==</span>
20120225 21 25
</pre></div>
</td></tr></table></div>
<p>　ヒット数はただ単にログから年月日と時（時分秒の「時」）を切り出して数えるだけ、
ファイル数は、その処理の前に「正常」、
つまりステータスが200のレコードを抽出しています。
サイト数については、同時間内の重複を消してから数えています。</p>
<p>　リスト6で使われているcountはTukubaiコマンドです。
countは、文字通り数を数えるためのコマンドです。リスト9に例を示します。
オプションの <tt class="docutils literal"><span class="pre">1</span> <span class="pre">2</span></tt> というのは、
第1フィールドから第2フィールドまでが同じレコードをカウントせよということです。
データは、第1、第2フィールドでソートされている必要があります。
<tt class="docutils literal"><span class="pre">uniq</span> <span class="pre">-c</span></tt> でも同じことができます。
余計な空白が入るのでパイプラインのなかでは扱いにくいですが。</p>
<p>↓リスト9：countの使用例</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat hoge
001 上田
001 上田
001 上田
002 鎌田
002 鎌田
<span class="nv">$ </span>count 1 2 hoge
001 上田 3
002 鎌田 2
</pre></div>
</div>
<p>　リスト6の23行目のsortに <tt class="docutils literal"><span class="pre">u</span></tt> というオプションがついていますが、
これは重複を除去するというオプション指定です。
<tt class="docutils literal"><span class="pre">sort</span> <span class="pre">-u</span></tt> と <tt class="docutils literal"><span class="pre">sort</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> は同じことです。
安定ソートのオプション <tt class="docutils literal"><span class="pre">s</span></tt> は高速化のために付けています。</p>
<p>　ページ数については、記事のページを、
それ以外（画像、rssファイル、ajax用bashスクリプト）
と区別して抽出する必要があります。
このサイトでは、ページが呼び出されるときに必ず
<tt class="docutils literal"><span class="pre">TOMONOKAI_CMS.CGI</span></tt> というCGI（bash）スクリプトが呼ばれます。
urlだけ要求されたときは、
access_logには <tt class="docutils literal"><span class="pre">GET</span> <span class="pre">/</span> <span class="pre">HTTP1.0</span></tt> などという記録が残ります。
（まれに <tt class="docutils literal"><span class="pre">GET</span> <span class="pre">//</span> <span class="pre">HTTP1.0</span></tt> などと変則パターンがあって面倒です。）
リスト7の16行目のegrep（拡張正規表現の使えるgrep）で、
集計対象のページを抽出しています。
<tt class="docutils literal"><span class="pre">egrep</span> <span class="pre">'AAA|BBB'</span></tt> という書式で、
「AAAまたはBBBを含むレコード」という意味になります。
また、14行目でurlから「?」以降の文字列（GETの値）
やその他不要なデータを消して誤抽出を防いでいます。
この部分は、自作するとかなり柔軟にカスタマイズできるが故に難しい部分ではあります。
面倒ならば拡張子だけ見ればよいと思います。</p>
<p>　フィルタされたログは、訪問数の集計でも使うことができるので、
17行目で <tt class="docutils literal"><span class="pre">$tmp-pages</span></tt> というファイルに保存されています。
teeは、標準入力をファイルと標準出力に二股分岐するコマンドです。</p>
<p>　訪問者数の計算は、ひねりがいります。
アルゴリズムを説明するために、
リスト7の26行目の処理が終わったあとのデータをリスト7に示します。</p>
<p>↓リスト7：sort後のデータの一部</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>95.108.246.253 20120212 203105 1231
95.108.246.253 20120212 235718 1437
95.108.246.253 20120213 150603 906
95.108.246.253 20120213 150605 906
95.108.246.253 20120213 151252 912
</pre></div>
</td></tr></table></div>
<p>左から順に、IPアドレス、年月日、時分秒と並び、最後に時分秒を分に直した数字が入っています。
この最後のフィールドをレコードの上から比較していって、
30分以上離れていない同一IPのレコードを取り除く必要があります。
その処理を行っているのが30, 31行目のawkです。
定義していないip, day, tmという変数をいきなり比較していますが、
awkは変数が出てきたときに初期化するので、
このようなさぼったコードを書くことができます。</p>
<p>　念のためこのawkが行っている処理を説明すると次のようになります。</p>
<ol class="arabic simple">
<li>ipと第1フィールドを比較</li>
<li>dayを第2フィールドと比較</li>
<li>第4フィールドとtmの差が30分以上か調査</li>
<li>1～3の結果、残すレコードであれば出力して、そのレコードの情報をip, day, tmに反映</li>
</ol>
<p>この処理のあとは、毎時のレコード数をカウントするだけで訪問数になります。
（脚注：ただしリスト7の方法だと、
日をまたいで30分以内の閲覧が2カウントされます。）</p>
</div>
<div class="section" id="html">
<h3>5.2.4. HTMLを作る<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　あとはデータをHTMLにはめ込みます。グラフを作ってみましょう。
5種類のデータも楽々出力・・・と言いたいところですが、
同じような処理の繰り返しでどうしてもコードの量がかさんでしまうので、
訪問数のグラフを描くところまでにします。</p>
<p>　先に、作るグラフのイメージを図1に示します。
縦に時間軸を置いて、上に新しい時間帯のデータが来るようにしましょう。
横軸の値は固定にしています。可変にもできますが、
訪問数はそんなに変化はしないので、やめておきます。
たくさん増えたら、喜んで作り直します。
また、座標のオフセット等の定数もハードコーディングですがご了承ください。</p>
<p>↓図1：訪問者数グラフ</p>
<div class="figure">
<img alt="_images/201205_1.png" src="201205_1.png" />
</div>
<p>　前回やりましたが、HTMLを作るときは、
HTMLのテンプレートを作りながらTukubaiコマンドの
mojihame等を使ってデータをはめ込んでいきます。
リスト8にテンプレート、リスト9にスクリプトを示します。
（脚注：BSD系の場合は、tacはtail、seqはjotで対応お願いします。）
スクリプトで行っていることは、横軸を作り、縦軸を作り、
棒グラフ用の座標を計算し、最後にそれぞれをmojihameするという処理です。</p>
<p>↓リスト8: HTMLテンプレート</p>
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
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
33</pre></div></td><td class="code"><div class="highlight"><pre>[hoge\@sakura WEB_KAISEKI]$ cat HTML/TEMPLATE.HTML
<span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="nt">&lt;html&gt;</span>
 <span class="nt">&lt;head&gt;&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;UTF-8&quot;</span> <span class="nt">/&gt;&lt;/head&gt;</span>
 <span class="nt">&lt;body&gt;</span>
 <span class="nt">&lt;div&gt;</span>訪問数<span class="nt">&lt;/div&gt;</span>
 <span class="nt">&lt;svg</span> <span class="na">style=</span><span class="s">&quot;height:1000px;width:400px;font-size:12px&quot;</span><span class="nt">&gt;</span>
<span class="c">&lt;!--VALUEAXIS--&gt;</span>
 <span class="c">&lt;!--背景帯・軸目盛・目盛ラベル--&gt;</span>
 <span class="nt">&lt;rect</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x=</span><span class="s">&quot;%2&quot;</span> <span class="na">y=</span><span class="s">&quot;20&quot;</span> <span class="na">width=</span><span class="s">&quot;15&quot;</span> <span class="na">height=</span><span class="s">&quot;1000&quot;</span>
 <span class="na">style=</span><span class="s">&quot;fill:lightgray;stroke:none&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;%2&quot;</span> <span class="na">y1=</span><span class="s">&quot;15&quot;</span> <span class="na">x2=</span><span class="s">&quot;%2&quot;</span> <span class="na">y2=</span><span class="s">&quot;20&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;text</span> <span class="na">x=</span><span class="s">&quot;%3&quot;</span> <span class="na">y=</span><span class="s">&quot;10&quot;</span><span class="nt">&gt;</span>%1<span class="nt">&lt;/text&gt;</span>
<span class="c">&lt;!--VALUEAXIS--&gt;</span>
 <span class="c">&lt;!--横軸--&gt;</span>
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;20&quot;</span> <span class="na">x2=</span><span class="s">&quot;350&quot;</span> <span class="na">y2=</span><span class="s">&quot;20&quot;</span> <span class="nt">/&gt;</span>

<span class="c">&lt;!--TIMEAXIS--&gt;</span>
 <span class="c">&lt;!--目盛・目盛ラベル--&gt;</span>
 <span class="nt">&lt;line</span> <span class="na">x1=</span><span class="s">&quot;45&quot;</span> <span class="na">y1=</span><span class="s">&quot;%1&quot;</span> <span class="na">x2=</span><span class="s">&quot;350&quot;</span> <span class="na">y2=</span><span class="s">&quot;%1&quot;</span>
 <span class="na">style=</span><span class="s">&quot;stroke:white;stroke-width:1px&quot;</span> <span class="nt">/&gt;</span>
 <span class="nt">&lt;text</span> <span class="na">x=</span><span class="s">&quot;0&quot;</span> <span class="na">y=</span><span class="s">&quot;%1&quot;</span><span class="nt">&gt;</span>%2日0時<span class="nt">&lt;/text&gt;</span>
<span class="c">&lt;!--TIMEAXIS--&gt;</span>
 <span class="c">&lt;!--縦軸線--&gt;</span>
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;20&quot;</span> <span class="na">x2=</span><span class="s">&quot;50&quot;</span> <span class="na">y2=</span><span class="s">&quot;1000&quot;</span> <span class="nt">/&gt;</span>
<span class="c">&lt;!-- VISITS --&gt;</span>
 <span class="c">&lt;!--グラフ--&gt;</span>
 <span class="nt">&lt;line</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;%1&quot;</span> <span class="na">x2=</span><span class="s">&quot;%2&quot;</span> <span class="na">y2=</span><span class="s">&quot;%1&quot;</span> <span class="na">stroke-opacity=</span><span class="s">&quot;0.6&quot;</span>
 <span class="na">style=</span><span class="s">&quot;stroke:red;stroke-width:2px&quot;</span> <span class="nt">/&gt;</span>
<span class="c">&lt;!-- VISITS --&gt;</span>
 <span class="nt">&lt;/svg&gt;</span>
 <span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/html&gt;</span>
</pre></div>
</td></tr></table></div>
<p>↓リスト9: HTML生成スクリプト</p>
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
30</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>cat ./SCR/HTMLMAKE
<span class="c">#!/bin/bash</span>
<span class="c"># HTMLMAKE: 訪問数のグラフを表示するHTMLファイルを作る</span>
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com) Feb. 26, 2012</span>
<span class="nv">tmp</span><span class="o">=</span>/home/hoge/tmp/<span class="nv">$$</span>
<span class="nv">dir</span><span class="o">=</span>/home/hoge/WWW/WEB_KAISEKI

<span class="c">###データ採取</span>
tac <span class="nv">$dir</span>/TMP/VISITS.HOUR &gt; <span class="nv">$tmp</span>-data

<span class="c">###数値（縦）軸。原点は20px下</span>
seq 0 9 |
awk <span class="s1">&#39;{print $1*10,$1*30+50,$1*30+45}&#39;</span> &gt; <span class="nv">$tmp</span>-vaxis
<span class="c">#1:ラベル 2:目盛座標 3:文字列座標</span>

<span class="c">###時間軸。原点は50px左</span>
<span class="c">#tmp-data: 1:日付 2:時 3:数</span>
awk <span class="s1">&#39;$2==&quot;00&quot;{print NR*2+20,$1}&#39;</span> <span class="nv">$tmp</span>-data |
self 1 2.7 &gt; <span class="nv">$tmp</span>-taxis
<span class="c">#1:縦座標 2:日</span>

<span class="c">###訪問数をくっつけてHTMLを出力</span>
<span class="c">#1:日付 2:時 3:数</span>
awk <span class="s1">&#39;{print NR*2+20,$3*5+50}&#39;</span> <span class="nv">$tmp</span>-data |
<span class="c">#1:縦座標 2:値</span>
mojihame -lVISITS <span class="nv">$dir</span>/HTML/TEMPLATE.HTML - |
mojihame -lVALUEAXIS - <span class="nv">$tmp</span>-vaxis |
mojihame -lTIMEAXIS - <span class="nv">$tmp</span>-taxis &gt; /home/hoge/visits.html

rm -f <span class="nv">$tmp</span>-*
</pre></div>
</td></tr></table></div>
<p>　28行目のHTMLの出力先ですが、
apacheでHTMLが閲覧可能なディレクトリにリダイレクトしておけば、
ブラウザでの確認が可能になります。
また、cron等を使って、1時間に一度、
それぞれのスクリプトを順番に起動すれば、
自動で訪問数を集計するアプリケーションになります。</p>
<p>　項目を追加したければ、</p>
<ul class="simple">
<li>グラフや表のデータをCGIスクリプトで作成</li>
<li>HTMLのテンプレートを記述</li>
<li>CGIスクリプトのmojihameを増やす</li>
</ul>
<p>という作業をすることになります。日別の集計が必要な場合は、
リスト6,7のようなバッチのスクリプトを新たに作ればよいでしょう。</p>
</div>
</div>
<div class="section" id="id8">
<h2>5.3. おわりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、apacheのログを解析してグラフにするアプリケーションを作りました。
これだけ書いて制御構文がawkのif文1個だけで、
処理がすべて一方通行になっているのはシェルスクリプトの面白い性質だと思います。</p>
<p>　今回出てきたTukubaiコマンドはcountとmojihameでした。
mojihameの反則的威力は前回も紹介しましたが、今回はパイプで3個連結してみました。
countは、集計のための便利なコマンドです。
Tukubaiコマンドには、他にsm2などの足し算コマンドがあって、
集計などに使えますのでおいおい紹介します。</p>
<p>　次回はSQLの代わりにコマンドを使う方法を紹介します。
いわゆるNoSQLというやつですが、
シェルスクリプトを使うと極めて自然に実現できることを示したいと思います。</p>
</div>
</div>

