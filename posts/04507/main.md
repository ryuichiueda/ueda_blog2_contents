---
Copyright: (C) Ryuichi Ueda
---

# 開眼シェルスクリプト2012年5月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <br />
 <div class="section" id="id1"><br />
<h1>5. 開眼シェルスクリプト 第5回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>5.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　開眼シェルスクリプトも第5回になりました。<br />
今回は、これまでのテクニックを駆使して、<br />
アプリケーションを作ることに挑戦します。<br />
お題はapacheのログを解析してアクセス数等をHTMLにするソフトです。<br />
「車輪の再発明だ！」と言われてしまいそうですが、今回は<br />
「ソフトをインストールして使いこなすまでの時間よりも早く作ってしまえ」<br />
という立場で押し切ります。</p><br />
<div class="section" id="id3"><br />
<h3>5.1.1. 車輪を使って車輪を超高速再発明<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　毎度おなじみガンカーズのUNIX哲学には、</p><br />
<p>「できる限り原型（プロトタイプ）を作れ。」</p><br />
<p>という項目がありますが、<br />
これはコマンドを組み合わせたシェルスクリプトでさっさと動くものを作って人に見せろということです。<br />
コマンドを使いまわす方法が手っ取り早いことは昔も今もそんなに変わっていません。<br />
テトリスの上手な人はものすごいスピードでブロックを落としていきますが、<br />
良く使うコマンドの組み合わせが一通り頭に入ると同じような感覚を味わうことになります。</p><br />
<p>　それに、コマンド自体は一つ一つ非常に有能で長い間使われてきた車輪です。<br />
これを組み合わせてアプリケーションを作る行為自体は、<br />
車輪を再発明しない工夫でもあります。<br />
筆者はそれを再び広めたいのです。と言い訳して本題に入ります。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>5.2. お題：お手製アクセス解析ソフトを作る<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　アクセス解析ソフトとしては、Webalizerが有名で筆者も使っていますが、<br />
もうちょっと気の利いたことをしたい場合に拡張するのは大変です。<br />
グラフ以外はシェルスクリプトでさっと書けるので、自分で作ってしまいましょう。<br />
グラフも、前回の応用でなんとかなります。</p><br />
<p>　解析対象は、USP友の会のウェブサイト（脚注:<a class="reference external" href="http://www.usptomonokai.jp">http://www.usptomonokai.jp</a>）です。<br />
このサイト、bash製という珍品ですが、ログはいたって普通です。<br />
余計なことですが、このbashウェブシステムは私が半日で作り、<br />
次の日&#64;nullpopopo氏とネットワーク設定をして公開したものです。<br />
車輪の再発明コストは相当低いと思います。</p><br />
<p>　ログは~/LOGの下に溜まっていくようになっていて、<br />
root以外でも読み込み可能にしてあります。</p><br />
<p>↓リスト1: アクセスログ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura LOG<span class="o">]</span><span class="nv">$ </span>ls -ltr access_log* | tail -n 5<br />
-rw-r--r-- 1 root root 82408 2月 22 03:32 access_log-20120222.gz<br />
-rw-r--r-- 1 root root 61438 2月 23 03:32 access_log-20120223.gz<br />
-rw-r--r-- 1 root root 70638 2月 24 03:32 access_log-20120224.gz<br />
-rw-r--r-- 1 root root 60125 2月 25 03:32 access_log-20120225.gz<br />
-rw-r--r-- 1 root root 744255 2月 25 22:02 access_log<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このデータを解析して、ブラウザで見やすいHTMLを作ることが、<br />
お手製アクセス解析ソフトの目指すところです。</p><br />
<div class="section" id="id5"><br />
<h3>5.2.1. 準備<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　作る前に、場所を作りましょう。適当な場所に、<br />
リスト2のようにディレクトリを掘ってください。</p><br />
<p>↓リスト2: ディレクトリ構造</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WWW<span class="o">]</span><span class="nv">$ </span>tree -L 1 WEB_KAISEKI<br />
WEB_KAISEKI<br />
|-- HTML <span class="c">#HTMLのテンプレート置き場</span><br />
|-- SCR <span class="c">#シェルスクリプト置き場</span><br />
<span class="sb">`</span>-- TMP <span class="c">#作成したファイル置き場</span><br />
</pre></div><br />
</div><br />
<p>「WEB_KAISEKI」というのがこのソフトの名前です。<br />
（脚注：英語でなくてローマ字なのは業務上の癖なので突っ込まないでください。）</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>5.2.2. ログの整理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まずSCRの下に、<br />
3月号で作った「apacheのログをきれいにするスクリプト」を置きます。<br />
前回Tukubaiコマンド（参照：<a class="reference external" href="http://uec.usp-lab.com">http://uec.usp-lab.com</a>）を紹介したので、<br />
Tukubaiのコマンドを使って簡略化してリスト3に再掲します。<br />
また、その他の部分も環境と目的に合わせて微調整してあります。</p><br />
<p>↓リスト3: apacheのログを整理するスクリプト</p><br />
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>cat SCR/HTTPD_ACCESS_NORMALIZE<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">logdir</span><span class="o">=</span>/home/hoge/LOG<br />
<span class="nv">dir</span><span class="o">=</span>/home/hoge/WWW/WEB_KAISEKI<br />
<br />
<span class="nb">echo</span> <span class="nv">$logdir</span>/access_log*.gz |<br />
xargs zcat |<br />
cat - <span class="nv">$logdir</span>/access_log |<br />
sed <span class="s1">&#39;s/&quot;&quot;/&quot;-&quot;/g&#39;</span> |<br />
sed <span class="s1">&#39;s/\\(..*\\) \\(..*\\) \\(..*\\) \\[\\(..*\\)\\] &quot;\\(..*\\)&quot; \\(..*\\) \\(..*\\) &quot;\\(..*\\)&quot; &quot;\\(..*\\)&quot;$/\\1あ\\2あ\\3あ\\4あ\\5あ\\6あ\\7あ\\8あ\\9/&#39;</span> |<br />
sed -e <span class="s1">&#39;s/_/＿/g&#39;</span> -e <span class="s1">&#39;s/ /_/g&#39;</span> -e <span class="s1">&#39;s/あ/ /g&#39;</span> |<br />
<span class="c">#1:IP 2,3:id 4:日時 5-9:リクエスト以降</span><br />
self 4.4.3 4.1.2 4.8.4 4.13.8 1/3 5/NF |<br />
<span class="c">#1:月 2:日 3:年 4:時:分:秒 5:IP 6,7:id 8-12:リクエスト以降</span><br />
sed -f <span class="nv">$dir</span>/SCR/MONTH |<br />
<span class="c">#↑参考：https://github.com/ryuichiueda/SoftwareDesign/blob/master/201202/MONTH.sed</span><br />
<span class="c">#時分秒のコロンを取る</span><br />
awk <span class="s1">&#39;{gsub(/:/,&quot;&quot;,$4);print}&#39;</span> |<br />
<span class="c">#年月日の空白を取る</span><br />
awk <span class="s1">&#39;{print $3$1$2,$4,$5,$6,$7,$8,$9,$10,$11,$12}&#39;</span> |<br />
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト以降</span><br />
sort -s -k1,2 &gt; <span class="nv">$dir</span>/TMP/ACCESS_LOG<br />
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト 7:ステータス 8以降:今回不使用</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ここで使っているTukubaiコマンドは、 <tt class="docutils literal"><span class="pre">self</span></tt> です。<br />
selfは、awkの文字を切り出す機能を単純化したコマンドです。<br />
リスト4を見れば、awkのsubstrの動作と似ていることが分かると思います。<br />
また、リスト1の15行目の <tt class="docutils literal"><span class="pre">1/3</span></tt> というのは1～3フィールド、<br />
<tt class="docutils literal"><span class="pre">5/NF</span></tt> というのは5～最終フィールドのことです。</p><br />
<p>↓リスト４：selfの使用例</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#第1Fと、第1Fの3文字目以降、第2Fの1文字目から2文字抽出</span><br />
<span class="nv">$ </span><span class="nb">echo </span>abcd 1234 | self 1 1.3 2.1.2<br />
abcd <span class="nb">cd </span>12<br />
<span class="c">#次のawkと等価</span><br />
<span class="nv">$ </span><span class="nb">echo </span>abcd 1234 | awk <span class="s1">&#39;{print $1,substr($1,3),substr($2,1,2)}&#39;</span><br />
abcd <span class="nb">cd </span>12<br />
</pre></div><br />
</div><br />
<p>　その他、リスト3のスクリプトの変更点は次のとおりです。</p><br />
<p>　まず、7, 8行目は <tt class="docutils literal"><span class="pre">zcat</span> <span class="pre">$logdir/access_log*.gz</span></tt> と書いてもよいのですが、<br />
ファイル数が非常に多くなるとエラーが出るのでそれを回避しています。<br />
（こうしなくても10年は大丈夫なのですが。）<br />
また、10行目で空データ <tt class="docutils literal"><span class="pre">&quot;&quot;</span></tt> を <tt class="docutils literal"><span class="pre">&quot;-&quot;</span></tt> に変換してから<br />
11行目でフィールド分割しています。<br />
12行目のsedでは、 <tt class="docutils literal"><span class="pre">_</span></tt> を全角の <tt class="docutils literal"><span class="pre">＿</span></tt> 、半角空白を <tt class="docutils literal"><span class="pre">_</span></tt> 、<br />
一時的なデリミタである「あ」を半角空白に変換しています。<br />
二つ以上の変換を一回のsedで行う場合は、<br />
12行目のように-eというオプションを付けます。</p><br />
<p>このスクリプトを実行して、日付・時刻ソートされた以下のようなデータが得られればOKです。<br />
第3フィールドにはIPアドレスやホスト名が記録されることがありますが、<br />
今回は「IPアドレス」あるいは「IP」と表記します。</p><br />
<p>↓リスト5: ファイル「ACCESS_LOG」のレコード</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#フィールド数は10列</span><br />
<span class="c">#1:年月日 2:時分秒 3:IP 4,5:id 6:リクエスト 7:ステータス 8以降:今回不使用</span><br />
<span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>awk <span class="s1">&#39;{print NF}&#39;</span> TMP/ACCESS_LOG | uniq<br />
10<br />
<span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>tail -n 2 TMP/ACCESS_LOG<br />
20120225 221853 72.14.199.225 - - GET_/TOMONOKAI＿CMS/CGI/TOMONOKAI＿CMS.CGI_HTTP/1.1 200 16920 - Feedfetcher-Google;_<span class="o">(</span>略<span class="o">)</span><br />
20120225 221946 210.128.183.1 - - GET_/TOMONOKAI＿CMS/HTML/rss20.xml_HTTP/1.0 200 10233 - Mozilla/4.0_<span class="o">(</span>compatible;<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>5.2.3. 集計データをつくる<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて、「きれいなデータ」ACCESS_LOGを作ったので、<br />
次は自分の解析したい情報をそこから抽出します。<br />
何をしようか考えたのですが、とりあえずWebalizerが出力する基本的な数値である<br />
「Hits, Files, Pages, Visits, Sites」をちゃんと集計したいと思います。</p><br />
<table border="1" class="docutils"><br />
<colgroup><br />
<col width="33%" /><br />
<col width="67%" /><br />
</colgroup><br />
<thead valign="bottom"><br />
<tr class="row-odd"><th class="head">項目</th><br />
<th class="head">意味</th><br />
</tr><br />
</thead><br />
<tbody valign="top"><br />
<tr class="row-even"><td>Hits（ヒット数）</td><br />
<td>access_logに記録されたレコード数</td><br />
</tr><br />
<tr class="row-odd"><td>Files（ファイル数）</td><br />
<td>Hitsのうち、正常にアクセスされた数</td><br />
</tr><br />
<tr class="row-even"><td>Pages（ページ数）</td><br />
<td>正常にアクセスされたページ（画面）数</td><br />
</tr><br />
<tr class="row-odd"><td>Sites（サイト数）</td><br />
<td>ヒット数の集計対象のレコード中にある、IPの種類の数</td><br />
</tr><br />
<tr class="row-even"><td>Visits（訪問数）</td><br />
<td>ページ数の集計対象レコードから、30分以内の同一IPのレコードを重複として取り除いた数</td><br />
</tr><br />
</tbody><br />
</table><br />
<p>　これらを時間単位で集計するシェルスクリプトをリスト6,7に示します。<br />
これらのスクリプトを実行すると、TMP下にリスト8のようなファイルが出力されます。</p><br />
<p>↓リスト6: 集計スクリプト（hit,file,site数）</p><br />
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c"># COUNT.HIT_FILE_SITE.HOUR: hit,file,siteの時間別集計</span><br />
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com)</span><br />
<br />
<span class="nb">cd</span> /home/hoge/WWW/WEB_KAISEKI/TMP<br />
<br />
<span class="c">###ヒット数</span><br />
self 1 2.1.2 ACCESS_LOG |<br />
<span class="c">#1:年月日 2:時</span><br />
count 1 2 &gt; HITS.COUNT<br />
<span class="c">#1:年月日 2:時 3:数</span><br />
<br />
<span class="c">###ファイル数</span><br />
awk <span class="s1">&#39;$7==200&#39;</span> ACCESS_LOG |<br />
self 1 2.1.2 |<br />
<span class="c">#1:IP 2:時</span><br />
count 1 2 &gt; FILES.COUNT<br />
<span class="c">#1:年月日 2:時 3:数</span><br />
<br />
<span class="c">###サイト数（時間別）</span><br />
self 1 2.1.2 3 ACCESS_LOG |<br />
<span class="c">#1:日付 2:時 3:IP</span><br />
sort -su |<br />
count 1 2 &gt; SITES.COUNT<br />
<span class="c">#1:年月日 2:時 3:数</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>↓リスト7: 集計スクリプト（page,visit数）</p><br />
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
37</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<span class="c"># COUNT.HOUR: page,visitの時間別集計</span><br />
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com)</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nb">cd</span> /home/hoge/WWW/WEB_KAISEKI/TMP<br />
<br />
<span class="c">###ページ数</span><br />
<span class="c">#ステイタス200、メソッドGETのデータだけ</span><br />
awk <span class="s1">&#39;$7==200 &amp;&amp; $6~/^GET/&#39;</span> ACCESS_LOG |<br />
self 1/3 6 |<br />
<span class="c">#1:年月日 2:時分秒 3:IP 4:リクエスト</span><br />
<span class="c">#プロトコルや?以降の文字列を削る</span><br />
sed -e <span class="s1">&#39;s;_HTTP/.*$;;&#39;</span> -e <span class="s1">&#39;s;\\?.*$;;&#39;</span> |<br />
<span class="c">#集計対象を検索</span><br />
egrep <span class="s1">&#39;GET_//*$|TOMONOKAI＿CMS\\.CGI$&#39;</span> |<br />
tee <span class="nv">$tmp</span>-pages |<br />
self 1 2.1.2 |<br />
count 1 2 &gt; PAGES.HOUR<br />
<br />
<span class="c">###訪問数</span><br />
<span class="c">#1:年月日 2:時分秒 3:IP 4:リクエスト</span><br />
self 3 1 2 2.1.2 2.3.2 <span class="nv">$tmp</span>-pages |<br />
<span class="c">#1:IP 2:年月日 3:時分秒 4:時 5:分</span><br />
<span class="c">#$4,$5を分に換算（頭にゼロがあっても大丈夫）</span><br />
awk <span class="s1">&#39;{print $1,$2,$3,$4*60+$5}&#39;</span> |<br />
<span class="c">#1:IP 2:年月日 3:時分秒 4:分</span><br />
<span class="c">#IP、年月日、時分秒でソートする</span><br />
sort -k1,3 -s |<br />
awk <span class="s1">&#39;{if(ip!=$1||day!=$2||$4-tm&gt;=30){</span><br />
<span class="s1"> print;ip=$1;day=$2;tm=$4}}&#39;</span> |<br />
self 2 3.1.2 1 |<br />
<span class="c">#1:年月日 2:時 3:IP</span><br />
sort -k1,2 -s |<br />
count 1 2 &gt; VISITS.HOUR<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
</pre></div><br />
</td></tr></table></div><br />
<p>↓リスト8：出力</p><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura TMP<span class="o">]</span><span class="nv">$ </span>tail -n 1 ./*.HOUR<br />
<span class="o">==</span>&gt; ./FILES.HOUR &lt;<span class="o">==</span><br />
20120225 21 <span class="nv">125</span><br />
<br />
<span class="o">==</span>&gt; ./HITS.HOUR &lt;<span class="o">==</span><br />
20120225 21 <span class="nv">189</span><br />
<br />
<span class="o">==</span>&gt; ./PAGES.HOUR &lt;<span class="o">==</span><br />
20120225 21 <span class="nv">51</span><br />
<br />
<span class="o">==</span>&gt; ./SITES.HOUR &lt;<span class="o">==</span><br />
20120225 21 <span class="nv">34</span><br />
<br />
<span class="o">==</span>&gt; ./VISITS.HOUR &lt;<span class="o">==</span><br />
20120225 21 25<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ヒット数はただ単にログから年月日と時（時分秒の「時」）を切り出して数えるだけ、<br />
ファイル数は、その処理の前に「正常」、<br />
つまりステータスが200のレコードを抽出しています。<br />
サイト数については、同時間内の重複を消してから数えています。</p><br />
<p>　リスト6で使われているcountはTukubaiコマンドです。<br />
countは、文字通り数を数えるためのコマンドです。リスト9に例を示します。<br />
オプションの <tt class="docutils literal"><span class="pre">1</span> <span class="pre">2</span></tt> というのは、<br />
第1フィールドから第2フィールドまでが同じレコードをカウントせよということです。<br />
データは、第1、第2フィールドでソートされている必要があります。<br />
<tt class="docutils literal"><span class="pre">uniq</span> <span class="pre">-c</span></tt> でも同じことができます。<br />
余計な空白が入るのでパイプラインのなかでは扱いにくいですが。</p><br />
<p>↓リスト9：countの使用例</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat hoge<br />
001 上田<br />
001 上田<br />
001 上田<br />
002 鎌田<br />
002 鎌田<br />
<span class="nv">$ </span>count 1 2 hoge<br />
001 上田 3<br />
002 鎌田 2<br />
</pre></div><br />
</div><br />
<p>　リスト6の23行目のsortに <tt class="docutils literal"><span class="pre">u</span></tt> というオプションがついていますが、<br />
これは重複を除去するというオプション指定です。<br />
<tt class="docutils literal"><span class="pre">sort</span> <span class="pre">-u</span></tt> と <tt class="docutils literal"><span class="pre">sort</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> は同じことです。<br />
安定ソートのオプション <tt class="docutils literal"><span class="pre">s</span></tt> は高速化のために付けています。</p><br />
<p>　ページ数については、記事のページを、<br />
それ以外（画像、rssファイル、ajax用bashスクリプト）<br />
と区別して抽出する必要があります。<br />
このサイトでは、ページが呼び出されるときに必ず<br />
<tt class="docutils literal"><span class="pre">TOMONOKAI_CMS.CGI</span></tt> というCGI（bash）スクリプトが呼ばれます。<br />
urlだけ要求されたときは、<br />
access_logには <tt class="docutils literal"><span class="pre">GET</span> <span class="pre">/</span> <span class="pre">HTTP1.0</span></tt> などという記録が残ります。<br />
（まれに <tt class="docutils literal"><span class="pre">GET</span> <span class="pre">//</span> <span class="pre">HTTP1.0</span></tt> などと変則パターンがあって面倒です。）<br />
リスト7の16行目のegrep（拡張正規表現の使えるgrep）で、<br />
集計対象のページを抽出しています。<br />
<tt class="docutils literal"><span class="pre">egrep</span> <span class="pre">'AAA|BBB'</span></tt> という書式で、<br />
「AAAまたはBBBを含むレコード」という意味になります。<br />
また、14行目でurlから「?」以降の文字列（GETの値）<br />
やその他不要なデータを消して誤抽出を防いでいます。<br />
この部分は、自作するとかなり柔軟にカスタマイズできるが故に難しい部分ではあります。<br />
面倒ならば拡張子だけ見ればよいと思います。</p><br />
<p>　フィルタされたログは、訪問数の集計でも使うことができるので、<br />
17行目で <tt class="docutils literal"><span class="pre">$tmp-pages</span></tt> というファイルに保存されています。<br />
teeは、標準入力をファイルと標準出力に二股分岐するコマンドです。</p><br />
<p>　訪問者数の計算は、ひねりがいります。<br />
アルゴリズムを説明するために、<br />
リスト7の26行目の処理が終わったあとのデータをリスト7に示します。</p><br />
<p>↓リスト7：sort後のデータの一部</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>95.108.246.253 20120212 203105 1231<br />
95.108.246.253 20120212 235718 1437<br />
95.108.246.253 20120213 150603 906<br />
95.108.246.253 20120213 150605 906<br />
95.108.246.253 20120213 151252 912<br />
</pre></div><br />
</td></tr></table></div><br />
<p>左から順に、IPアドレス、年月日、時分秒と並び、最後に時分秒を分に直した数字が入っています。<br />
この最後のフィールドをレコードの上から比較していって、<br />
30分以上離れていない同一IPのレコードを取り除く必要があります。<br />
その処理を行っているのが30, 31行目のawkです。<br />
定義していないip, day, tmという変数をいきなり比較していますが、<br />
awkは変数が出てきたときに初期化するので、<br />
このようなさぼったコードを書くことができます。</p><br />
<p>　念のためこのawkが行っている処理を説明すると次のようになります。</p><br />
<ol class="arabic simple"><br />
<li>ipと第1フィールドを比較</li><br />
<li>dayを第2フィールドと比較</li><br />
<li>第4フィールドとtmの差が30分以上か調査</li><br />
<li>1～3の結果、残すレコードであれば出力して、そのレコードの情報をip, day, tmに反映</li><br />
</ol><br />
<p>この処理のあとは、毎時のレコード数をカウントするだけで訪問数になります。<br />
（脚注：ただしリスト7の方法だと、<br />
日をまたいで30分以内の閲覧が2カウントされます。）</p><br />
</div><br />
<div class="section" id="html"><br />
<h3>5.2.4. HTMLを作る<a class="headerlink" href="#html" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　あとはデータをHTMLにはめ込みます。グラフを作ってみましょう。<br />
5種類のデータも楽々出力・・・と言いたいところですが、<br />
同じような処理の繰り返しでどうしてもコードの量がかさんでしまうので、<br />
訪問数のグラフを描くところまでにします。</p><br />
<p>　先に、作るグラフのイメージを図1に示します。<br />
縦に時間軸を置いて、上に新しい時間帯のデータが来るようにしましょう。<br />
横軸の値は固定にしています。可変にもできますが、<br />
訪問数はそんなに変化はしないので、やめておきます。<br />
たくさん増えたら、喜んで作り直します。<br />
また、座標のオフセット等の定数もハードコーディングですがご了承ください。</p><br />
<p>↓図1：訪問者数グラフ</p><br />
<div class="figure"><br />
<img alt="_images/201205_1.png" src="201205_1.png" /><br />
</div><br />
<p>　前回やりましたが、HTMLを作るときは、<br />
HTMLのテンプレートを作りながらTukubaiコマンドの<br />
mojihame等を使ってデータをはめ込んでいきます。<br />
リスト8にテンプレート、リスト9にスクリプトを示します。<br />
（脚注：BSD系の場合は、tacはtail、seqはjotで対応お願いします。）<br />
スクリプトで行っていることは、横軸を作り、縦軸を作り、<br />
棒グラフ用の座標を計算し、最後にそれぞれをmojihameするという処理です。</p><br />
<p>↓リスト8: HTMLテンプレート</p><br />
<div class="highlight-html"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
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
33</pre></div></td><td class="code"><div class="highlight"><pre>[hoge\@sakura WEB_KAISEKI]$ cat HTML/TEMPLATE.HTML<br />
<span class="cp">&lt;!DOCTYPE html&gt;</span><br />
<span class="nt">&lt;html&gt;</span><br />
 <span class="nt">&lt;head&gt;&lt;meta</span> <span class="na">charset=</span><span class="s">&quot;UTF-8&quot;</span> <span class="nt">/&gt;&lt;/head&gt;</span><br />
 <span class="nt">&lt;body&gt;</span><br />
 <span class="nt">&lt;div&gt;</span>訪問数<span class="nt">&lt;/div&gt;</span><br />
 <span class="nt">&lt;svg</span> <span class="na">style=</span><span class="s">&quot;height:1000px;width:400px;font-size:12px&quot;</span><span class="nt">&gt;</span><br />
<span class="c">&lt;!--VALUEAXIS--&gt;</span><br />
 <span class="c">&lt;!--背景帯・軸目盛・目盛ラベル--&gt;</span><br />
 <span class="nt">&lt;rect</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x=</span><span class="s">&quot;%2&quot;</span> <span class="na">y=</span><span class="s">&quot;20&quot;</span> <span class="na">width=</span><span class="s">&quot;15&quot;</span> <span class="na">height=</span><span class="s">&quot;1000&quot;</span><br />
 <span class="na">style=</span><span class="s">&quot;fill:lightgray;stroke:none&quot;</span> <span class="nt">/&gt;</span><br />
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;%2&quot;</span> <span class="na">y1=</span><span class="s">&quot;15&quot;</span> <span class="na">x2=</span><span class="s">&quot;%2&quot;</span> <span class="na">y2=</span><span class="s">&quot;20&quot;</span> <span class="nt">/&gt;</span><br />
 <span class="nt">&lt;text</span> <span class="na">x=</span><span class="s">&quot;%3&quot;</span> <span class="na">y=</span><span class="s">&quot;10&quot;</span><span class="nt">&gt;</span>%1<span class="nt">&lt;/text&gt;</span><br />
<span class="c">&lt;!--VALUEAXIS--&gt;</span><br />
 <span class="c">&lt;!--横軸--&gt;</span><br />
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;20&quot;</span> <span class="na">x2=</span><span class="s">&quot;350&quot;</span> <span class="na">y2=</span><span class="s">&quot;20&quot;</span> <span class="nt">/&gt;</span><br />
<br />
<span class="c">&lt;!--TIMEAXIS--&gt;</span><br />
 <span class="c">&lt;!--目盛・目盛ラベル--&gt;</span><br />
 <span class="nt">&lt;line</span> <span class="na">x1=</span><span class="s">&quot;45&quot;</span> <span class="na">y1=</span><span class="s">&quot;%1&quot;</span> <span class="na">x2=</span><span class="s">&quot;350&quot;</span> <span class="na">y2=</span><span class="s">&quot;%1&quot;</span><br />
 <span class="na">style=</span><span class="s">&quot;stroke:white;stroke-width:1px&quot;</span> <span class="nt">/&gt;</span><br />
 <span class="nt">&lt;text</span> <span class="na">x=</span><span class="s">&quot;0&quot;</span> <span class="na">y=</span><span class="s">&quot;%1&quot;</span><span class="nt">&gt;</span>%2日0時<span class="nt">&lt;/text&gt;</span><br />
<span class="c">&lt;!--TIMEAXIS--&gt;</span><br />
 <span class="c">&lt;!--縦軸線--&gt;</span><br />
 <span class="nt">&lt;line</span> <span class="na">stroke=</span><span class="s">&quot;black&quot;</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;20&quot;</span> <span class="na">x2=</span><span class="s">&quot;50&quot;</span> <span class="na">y2=</span><span class="s">&quot;1000&quot;</span> <span class="nt">/&gt;</span><br />
<span class="c">&lt;!-- VISITS --&gt;</span><br />
 <span class="c">&lt;!--グラフ--&gt;</span><br />
 <span class="nt">&lt;line</span> <span class="na">x1=</span><span class="s">&quot;50&quot;</span> <span class="na">y1=</span><span class="s">&quot;%1&quot;</span> <span class="na">x2=</span><span class="s">&quot;%2&quot;</span> <span class="na">y2=</span><span class="s">&quot;%1&quot;</span> <span class="na">stroke-opacity=</span><span class="s">&quot;0.6&quot;</span><br />
 <span class="na">style=</span><span class="s">&quot;stroke:red;stroke-width:2px&quot;</span> <span class="nt">/&gt;</span><br />
<span class="c">&lt;!-- VISITS --&gt;</span><br />
 <span class="nt">&lt;/svg&gt;</span><br />
 <span class="nt">&lt;/body&gt;</span><br />
<span class="nt">&lt;/html&gt;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>↓リスト9: HTML生成スクリプト</p><br />
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
30</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>hoge\@sakura WEB_KAISEKI<span class="o">]</span><span class="nv">$ </span>cat ./SCR/HTMLMAKE<br />
<span class="c">#!/bin/bash</span><br />
<span class="c"># HTMLMAKE: 訪問数のグラフを表示するHTMLファイルを作る</span><br />
<span class="c"># written by R.Ueda (r-ueda\@usp-lab.com) Feb. 26, 2012</span><br />
<span class="nv">tmp</span><span class="o">=</span>/home/hoge/tmp/<span class="nv">$$</span><br />
<span class="nv">dir</span><span class="o">=</span>/home/hoge/WWW/WEB_KAISEKI<br />
<br />
<span class="c">###データ採取</span><br />
tac <span class="nv">$dir</span>/TMP/VISITS.HOUR &gt; <span class="nv">$tmp</span>-data<br />
<br />
<span class="c">###数値（縦）軸。原点は20px下</span><br />
seq 0 9 |<br />
awk <span class="s1">&#39;{print $1*10,$1*30+50,$1*30+45}&#39;</span> &gt; <span class="nv">$tmp</span>-vaxis<br />
<span class="c">#1:ラベル 2:目盛座標 3:文字列座標</span><br />
<br />
<span class="c">###時間軸。原点は50px左</span><br />
<span class="c">#tmp-data: 1:日付 2:時 3:数</span><br />
awk <span class="s1">&#39;$2==&quot;00&quot;{print NR*2+20,$1}&#39;</span> <span class="nv">$tmp</span>-data |<br />
self 1 2.7 &gt; <span class="nv">$tmp</span>-taxis<br />
<span class="c">#1:縦座標 2:日</span><br />
<br />
<span class="c">###訪問数をくっつけてHTMLを出力</span><br />
<span class="c">#1:日付 2:時 3:数</span><br />
awk <span class="s1">&#39;{print NR*2+20,$3*5+50}&#39;</span> <span class="nv">$tmp</span>-data |<br />
<span class="c">#1:縦座標 2:値</span><br />
mojihame -lVISITS <span class="nv">$dir</span>/HTML/TEMPLATE.HTML - |<br />
mojihame -lVALUEAXIS - <span class="nv">$tmp</span>-vaxis |<br />
mojihame -lTIMEAXIS - <span class="nv">$tmp</span>-taxis &gt; /home/hoge/visits.html<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　28行目のHTMLの出力先ですが、<br />
apacheでHTMLが閲覧可能なディレクトリにリダイレクトしておけば、<br />
ブラウザでの確認が可能になります。<br />
また、cron等を使って、1時間に一度、<br />
それぞれのスクリプトを順番に起動すれば、<br />
自動で訪問数を集計するアプリケーションになります。</p><br />
<p>　項目を追加したければ、</p><br />
<ul class="simple"><br />
<li>グラフや表のデータをCGIスクリプトで作成</li><br />
<li>HTMLのテンプレートを記述</li><br />
<li>CGIスクリプトのmojihameを増やす</li><br />
</ul><br />
<p>という作業をすることになります。日別の集計が必要な場合は、<br />
リスト6,7のようなバッチのスクリプトを新たに作ればよいでしょう。</p><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>5.3. おわりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、apacheのログを解析してグラフにするアプリケーションを作りました。<br />
これだけ書いて制御構文がawkのif文1個だけで、<br />
処理がすべて一方通行になっているのはシェルスクリプトの面白い性質だと思います。</p><br />
<p>　今回出てきたTukubaiコマンドはcountとmojihameでした。<br />
mojihameの反則的威力は前回も紹介しましたが、今回はパイプで3個連結してみました。<br />
countは、集計のための便利なコマンドです。<br />
Tukubaiコマンドには、他にsm2などの足し算コマンドがあって、<br />
集計などに使えますのでおいおい紹介します。</p><br />
<p>　次回はSQLの代わりにコマンドを使う方法を紹介します。<br />
いわゆるNoSQLというやつですが、<br />
シェルスクリプトを使うと極めて自然に実現できることを示したいと思います。</p><br />
</div><br />
</div><br />

