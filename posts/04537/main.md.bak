# 開眼シェルスクリプト2012年12月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>12. 開眼シェルスクリプト 第12回メールを操る<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>12.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　開眼シェルスクリプトも今回で12回目、つまり1年になります。<br />
ネタが続くのか周囲は心配してましたが、まだまだ大丈夫そうです。</p><br />
<p>　編集サマの当初の企画意図を引っ張り出してみると、</p><br />
<p>「さまざまなLight Languageが流行っていますが、ちょっとした処理なら<br />
プログラミングするまでもなくシェルスクリプトだけで実現できるものも<br />
あります。（中略）身近なシェルを使いこなして、<br />
もっと業務に生かそうというのが趣旨。」</p><br />
<p>とあります。そうです。シェルスクリプトを使うと、<br />
ちょっとした処理を普段のシェル操作の延長線上で<br />
さっさと片付けてしまうことができます。<br />
ちょっとした処理なら身の回りにたくさんありますので、<br />
今後も身の回りのことを次々に取り上げて、<br />
皆様をCUIから離れられないようにしたいと思います。</p><br />
<p>　今回は電子メールを扱います。<br />
Maildirに溜まったメールを仕分けたり、<br />
中から文章などを切り出したりということをやってみます。</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>12.2. 環境等<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、CentOS 6.3、Ubuntu 12.04 で動作確認しました。<br />
FreeBSD でも動かそうとしたのですが、<br />
dateコマンドにフィルタモードが見当たりませんでした。<br />
while文で逃げるか、<br />
標準入力からUNIX時間を受けて日付に変換するコマンドの自作をお願いします。<br />
pythonで書いた例をリスト1に示しておきます。<br />
（脚注：無理にシェルでやってもいいのですが、<br />
コマンドは1プロセスで動かないとなにかと面倒です。）</p><br />
<p>・リスト1: UNIX時間を日付に変換するpythonスクリプト</p><br />
<div class="highlight-python"><pre>$ cat epoc2date<br />
#!/usr/bin/python<br />
<br />
import sys<br />
import time<br />
<br />
for line in sys.stdin:<br />
 unixtime = line.rstrip()<br />
 t = time.gmtime(int(unixtime))<br />
 print "%d %d %d" % (t.tm_year, t.tm_mon, t.tm_mday)<br />
$ date +%s | ./epoc2date<br />
2012 9 21</pre><br />
</div><br />
</div><br />
<div class="section" id="mairdir"><br />
<h2>12.3. Mairdir<a class="headerlink" href="#mairdir" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　筆者は、とあるサーバの自分のアカウントに、<br />
自分が管理しているサーバからの自動送信メールを貯めています。<br />
メールをホームに置いているのはこのサーバのpostfixです。</p><br />
<p>　このpostfixの設定ファイルで、<br />
ホームにメールを置くときの形式をMaildirにしています。<br />
ヘビーにUNIXを使っている人はご存知だと思いますが、<br />
Maildirは、メールを置いておくときの方法の一つです。<br />
Maildir形式では、電子メール一通が一つのファイルになります。</p><br />
<p>　念のため、postfixの設定ファイルの一部をリスト2に示しておきます。<br />
<tt class="docutils literal"><span class="pre">main.cf</span></tt> の <tt class="docutils literal"><span class="pre">home_mailbox</span></tt> の値を <tt class="docutils literal"><span class="pre">Maildir/</span></tt><br />
にしておくと、Maildirになります。<br />
デフォルトでは、 <tt class="docutils literal"><span class="pre">Mailbox</span></tt> になっているのですが、<br />
これだと複数のメールが一つの <tt class="docutils literal"><span class="pre">mbox</span></tt><br />
というファイルに固まって置かれてしまっていろいろとたちの悪いことになります。</p><br />
<p>・リスト2: main.cfの設定</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>vi /etc/postfix/main.cf<br />
...<br />
<span class="c"># DELIVERY TO MAILBOX</span><br />
<span class="c">#</span><br />
<span class="c"># The home_mailbox parameter specifies the optional pathname of a</span><br />
<span class="c"># mailbox file relative to a user&#39;s home directory. The default</span><br />
<span class="c"># mailbox file is /var/spool/mail/user or /var/mail/user. Specify</span><br />
<span class="c"># &quot;Maildir/&quot; for qmail-style delivery (the / is required).</span><br />
<span class="c">#</span><br />
<span class="c">#home_mailbox = Mailbox &lt;- mboxを使う</span><br />
<span class="nv">home_mailbox</span> <span class="o">=</span> Maildir/ &lt;- Maildirを使う<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　Maildir形式を選ぶと、ホーム下には <tt class="docutils literal"><span class="pre">Maildir</span></tt><br />
というディレクトリができます。<br />
今までのpostfixの話がちんぷんかんぷんでも、<br />
ホームの下に <tt class="docutils literal"><span class="pre">Maildir</span></tt> がいたら、<br />
今回の方法はいろいろ試すことができることでしょう。<br />
深いことを知らなくても目の前にテキストが<br />
あったらやっちまえというスタンスでいきましょう。<br />
そうでないと、<br />
理屈ばっかりで肝心のコンピューティングがつまらなくなります。<br />
道具は使ってナンボのモンです。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">~/Maildir</span></tt> の下には、リスト3のように<br />
<tt class="docutils literal"><span class="pre">cur,</span> <span class="pre">new,</span> <span class="pre">tmp</span></tt> という三つのディレクトリがあります。</p><br />
<p>・リスト3: Maildirディレクトリの下</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls ~/Maildir<br />
cur new tmp<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　メーラーで見たファイルはcur、新しいメールはnewに入るようですが、<br />
私はメーラーなどというナンパなものを使ってないので、<br />
全部newに入ったままです（脚注：実際はgmailのヘビーユーザーですごめんなさい。）。<br />
リスト4に、 <tt class="docutils literal"><span class="pre">new</span></tt> の下の様子を示します。</p><br />
<p>・リスト4: メールファイル</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls new/ | head -n 3<br />
1339304183.Vfc03I46017dM943925.sakura1<br />
1339305265.Vfc03I46062cM458553.sakura1<br />
1339306807.Vfc03I4607c6M993984.sakura1<br />
<span class="c">#2万5千件程度入ってます。</span><br />
<span class="nv">$ </span>ls ~/Maildir/new/ | wc -l<br />
25094<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　実際問題、このメールアカウントに溜まっているのはログばっかりなので、<br />
これを全部メーラーに入れてしまって一つずつ見るのは疲れます。<br />
また、メーラーでいろいろ設定して振り分けるのも、<br />
メーラーの癖や制限があって大変です。<br />
結局見なくなるので、なにか有用な統計と取ったほうがよいでしょう。<br />
こんなときにシェルスクリプトです。奥さん。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>12.4. ファイル名を眺める<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　もう少し観察してみましょう。<br />
ファイル名は、重複しないように一意になるように工夫されているようです。<br />
リスト5のファイル名をまじまじと見ると、<br />
postfixの置くファイルには、先頭に時刻が入っているようです。</p><br />
<p>・リスト5: メールのファイル名</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>1339304183.Vfc03I46017dM943925.sakura1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この「1339304183」は、「UNIX時間」というやつで、<br />
1970年1月1日0時0分0秒からの積算秒数を表しています。<br />
Linuxのdateコマンドなら、こんなふうに変換できます。</p><br />
<p>・リスト6: UNIX時間の変換</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>date -d \@1339304183<br />
2012年 6月 10日 日曜日 13:56:23 JST<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ちなみに、dateコマンドには-fというオプションがあって、<br />
以下のような使い方ができます。これは便利です。</p><br />
<p>・リスト7: dateのフィルタモード</p><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#使ったバージョンはこれ。</span><br />
<span class="nv">$ </span>date --version<br />
date <span class="o">(</span>GNU coreutils<span class="o">)</span> 8.13<br />
（略）<br />
<span class="nv">$ </span>head -n 3 datefile<br />
\@1339304183<br />
\@1339305265<br />
\@1339306807<br />
<span class="nv">$ </span>head -n 3 datefile | date -f -<br />
2012年 6月 10日 日曜日 13:56:23 JST<br />
2012年 6月 10日 日曜日 14:14:25 JST<br />
2012年 6月 10日 日曜日 14:40:07 JST<br />
<span class="nv">$ </span>head -n 3 datefile | date -f - <span class="s2">&quot;+%Y%m%d %H%M%S&quot;</span><br />
20120610 135623<br />
20120610 141425<br />
20120610 144007<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="while"><br />
<h2>12.5. まずは振り分けてみる（whileを使わずに）<a class="headerlink" href="#while" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まず肩慣らし程度にメールを日付で振り分けてみます。<br />
こうしておけば、例えばある日からある日までのメールを処理したいときに、<br />
いちいちUNIX時間を変換しなくてもよくなります。</p><br />
<p>　ホーム下に <tt class="docutils literal"><span class="pre">MAIL</span></tt> というディレクトリを作って、<br />
その下に日別のディレクトリを自動で作り、その下にメールをコピーします。</p><br />
<p>　ただ、肩慣らしと言っても一筋縄ではいかないのがこの連載。<br />
最近、while使うなとあまり言ってませんが、<br />
忘れたわけではありません。whileは避けるべきです。<br />
ここでもwhileを抜く効用を示してみます。</p><br />
<p>　まずはベタにリスト8のように書いてみます。<br />
ファイルを一個ずつ日付のディレクトリに放り込んでいきます。</p><br />
<p>・リスト8: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE.betabeta</span></tt> （ベタベタな例）</p><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#ベタベタバージョン</span><br />
<span class="nv">$ </span>cat DISTRIBUTE_BY_DATE.betabeta<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">sdir</span><span class="o">=</span>/home/ueda/Maildir/new<br />
<span class="nv">ddir</span><span class="o">=</span>/home/ueda/MAIL<br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<br />
<span class="nb">cd</span> <span class="nv">$sdir</span> <span class="o">||</span> <span class="nb">exit </span>1<br />
<br />
<span class="c">######################################</span><br />
<span class="c">#ファイルのリストを作る</span><br />
<span class="nb">echo</span> *.*.* |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
<span class="k">while </span><span class="nb">read </span>f ; <span class="k">do</span><br />
<span class="k"> </span><span class="nv">UNIXTIME</span><span class="o">=</span><span class="s2">&quot;\@&quot;</span><span class="k">$(</span><span class="nb">echo</span> <span class="nv">$f</span> | awk -F. <span class="s1">&#39;{print $1}&#39;</span><span class="k">)</span><br />
 <span class="nv">DATE</span><span class="o">=</span><span class="k">$(</span>date -d <span class="nv">$UNIXTIME</span> <span class="s2">&quot;+%Y%m%d&quot;</span><span class="k">)</span><br />
<br />
 <span class="o">[</span> -e <span class="s2">&quot;$ddir/$DATE&quot;</span> <span class="o">]</span> <span class="o">||</span> mkdir <span class="nv">$ddir</span>/<span class="nv">$DATE</span><br />
 cp -p <span class="nv">$f</span> <span class="nv">$ddir</span>/<span class="nv">$DATE</span>/<br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>13行目のechoは、ファイル名を空白区切りで出力してくれます。<br />
いつもlsを使っている人は、適当なディレクトリで <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">*</span></tt><br />
と打ってみてください。ファイルの一覧が取得できます。<br />
ファイル名が取得できたら、trで空白を改行に変換し、<br />
一つ一つ <tt class="docutils literal"><span class="pre">while</span></tt> で読んで処理していきます。</p><br />
<p>　上のスクリプトは何のソツもありません。<br />
まあ、世の99%の人がこのように書くと思います。<br />
しかし、あえて言います。</p><br />
<blockquote><br />
<div>失格！！！！</div></blockquote><br />
<p>です。</p><br />
<p>　サーバで試してみます。結果はリスト9のようになりました。</p><br />
<p>・リスト9: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE.betabeta</span></tt> は時間がかかる。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE.betabeta<br />
<br />
real 7m21.673s<br />
user 1m24.858s<br />
sys 5m51.464s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>筆者が書いた失格でないスクリプトについて、<br />
お見せする前に実行時間を測ってみましょう。<br />
リスト10のようになりました。</p><br />
<p>・リスト10: これくらいは高速化できる。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE<br />
<br />
real 0m43.866s<br />
user 0m16.774s<br />
sys 0m43.599s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>というように、10倍以上の差がついてしまいます。<br />
今回みたいに何万もファイルを扱うときは、<br />
この差は大きくなります。</p><br />
<p>　ではどう書いたかというのを次に見せます。<br />
ちょっと長くなってしまったので良し悪しですが・・・<br />
（じゃあ失格とか言うな）。</p><br />
<p>・リスト11: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt></p><br />
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
42<br />
43<br />
44<br />
45<br />
46<br />
47<br />
48</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat DISTRIBUTE_BY_DATE<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">sdir</span><span class="o">=</span>/home/ueda/Maildir/new<br />
<span class="nv">ddir</span><span class="o">=</span>/home/ueda/MAIL<br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<br />
<span class="nb">cd</span> <span class="nv">$sdir</span> <span class="o">||</span> <span class="nb">exit </span>1<br />
<br />
<span class="c">######################################</span><br />
<span class="c">#ファイルのリストを作る</span><br />
<span class="nb">echo</span> *.*.* |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
<span class="c">#1:ファイル名</span><br />
awk -F. <span class="s1">&#39;{print &quot;\@&quot; $1,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-files<br />
<span class="c">#1:UNIX時間 2:ファイル名</span><br />
<br />
<span class="c"># $tmp-filesの例：</span><br />
<span class="c">#\@1348117807 1348117807.Vfc03I4670eaM254446.www5276ue.sakura.ne.jp</span><br />
<br />
<span class="c">######################################</span><br />
<span class="c">#ファイルのリストに年月日をくっつける</span><br />
self 1 <span class="nv">$tmp</span>-files |<br />
date -f - <span class="s2">&quot;+%Y%m%d&quot;</span> |<br />
<span class="c">#1:年月日</span><br />
ycat - <span class="nv">$tmp</span>-files |<br />
<span class="c">#1:年月日 2:UNIX時間 3:ファイル名</span><br />
delf 2 &gt; <span class="nv">$tmp</span>-ymd-file<br />
<span class="c">#1:年月日 2:ファイル名</span><br />
<br />
<span class="c"># $tmp-ymd-fileの例</span><br />
<span class="c">#20120920 1348116008.Vfc03I4670ecM186337.www5276ue.sakura.ne.jp</span><br />
<br />
<span class="nb">cd</span> <span class="nv">$ddir</span> <span class="o">||</span> <span class="nb">exit </span>1<br />
<br />
<span class="c">######################################</span><br />
<span class="c">#日別のディレクトリを作る</span><br />
self 1 <span class="nv">$tmp</span>-ymd-file |<br />
uniq |<br />
xargs -P 0 -i_ mkdir -p _<br />
<br />
cat <span class="nv">$tmp</span>-ymd-file |<br />
awk -v <span class="nv">sd</span><span class="o">=</span><span class="s2">&quot;$sdir&quot;</span> <span class="s1">&#39;{print sd &quot;/&quot; $2, &quot;./&quot; $1 &quot;/&quot;}&#39;</span> |<br />
<span class="c">#コピー元、コピー先を読み込んでcpに渡す。</span><br />
xargs -P 0 -n 2 cp -p<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このスクリプトでは、一個一個ファイルを処理するのではなく、<br />
作るディレクトリのリストとコピーするファイルのリストを作成し、<br />
xargsで一気に作っています。<br />
速いのはxargsそのものの速さの寄与も大きいのですが、<br />
dateとawkをwhileで何回も呼ぶ必要がなくなっていることも原因です。</p><br />
<p>　速い方のスクリプトを詳しく見ていきましょう。<br />
まず、15行目の処理が終わって出力される<br />
<tt class="docutils literal"><span class="pre">$tmp-files</span></tt> は、19行目の例のようなレコードが縦に並んだファイルです。<br />
そして、23行目でUNIX時間だけとってきて、24行目のdateコマンドに流し込んでいます。<br />
ここで、ファイルごとにdateを読むのではなく、<br />
全ファイルに対して一回だけしかdateを読まなくてよくなります。</p><br />
<p>　26行目のycatは、Open usp Tukubai のコマンドです。<br />
「横キャット」と発音します。横にファイルをくっつけます。<br />
例をリスト12のように示します。Open usp Tukubaiの詳細は、<br />
UEC（ <tt class="docutils literal"><span class="pre">https://uec.usp-lab.com</span></tt> ）のサイトでご確認を。</p><br />
<p>・リスト12: <tt class="docutils literal"><span class="pre">ycat</span></tt> の使い方</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat file1<br />
1<br />
2<br />
3<br />
<span class="nv">$ </span>cat file2<br />
a<br />
b<br />
c<br />
<span class="nv">$ </span>ycat file<span class="o">{</span>1,2<span class="o">}</span><br />
1 a<br />
2 b<br />
3 c<br />
</pre></div><br />
</td></tr></table></div><br />
<p>これで、dateで作った日付が、もとの <tt class="docutils literal"><span class="pre">$tmp-files</span></tt> のレコードにくっつきます。<br />
32行目に、 <tt class="docutils literal"><span class="pre">$tmp-ymd-file</span></tt> のレコードを抜き取った例がありますが、<br />
この時点で、日付とファイル名という、処理に必要なデータが揃います。</p><br />
<p>　後は、日付のディレクトリを作り、<br />
その中にファイルをコピーしていきます。<br />
xargsについては、1,5,9月号に出てきました。<br />
まず、40行目の</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>xargs -P 0 mkdir -p<br />
</pre></div><br />
</td></tr></table></div><br />
<p>は、入力から日付を次々に受け取って、<br />
mkdirコマンドを実行していきます。<br />
mkdirの-pオプションは、<br />
すでにディレクトリがあってもエラーにならないように指定しています。<br />
xargsの <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">0</span></tt> ですが、<br />
これは、xargsで指定したコマンドを、<br />
できるだけ多くのプロセスで実行するという意味になります。<br />
manには「できるだけ」としか書いていないのが気になりますが、<br />
並列化してくれるようです。<br />
ここでは「できるだけ」にツッコミは入れず、<br />
<tt class="docutils literal"><span class="pre">-P</span> <span class="pre">0</span></tt> の有無で結果だけリスト13に示します。<br />
筆者の環境では、有意な差が出ています。</p><br />
<p>　後日談：何回も実験しているうちに、<br />
一回だけものすごい数のcpが立ち上がって自分のノートPCが暴走しました・・・。<br />
めったに起こらないのですが、せいぜい <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">100</span></tt> くらいにしておいてください。<br />
今のマシンやカーネルは頑丈なので、100プロセスぐらいなら何の問題もありません。</p><br />
<p>・リスト13: -P オプション有無での時間比較</p><br />
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE.nop<br />
<br />
real 2m58.583s<br />
user 0m27.764s<br />
sys 2m2.736s<br />
<span class="nv">$ </span>rm -Rf 2*<br />
<span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE<br />
<br />
real 0m41.221s<br />
user 0m16.201s<br />
sys 0m40.139s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　45行目のxargsは、さらに複雑なことをしています。<br />
このxargsには、次のようなテキストが流れ込みます。</p><br />
<p>・リスト14: xargsに入力するテキスト</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/Maildir/new/1339308608.Vfc03I4609ebM178619.sakura1 ./20120610/<br />
/home/ueda/Maildir/new/1339308909.Vfc03I4609ecM601364.sakura1 ./20120610/<br />
/home/ueda/Maildir/new/1339309208.Vfc03I4609edM55303.sakura1 ./20120610/<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>つまり、コピー元のファイルとコピー先のディレクトリがxargsに流れ込みます。<br />
xargsには、 <tt class="docutils literal"><span class="pre">-n</span> <span class="pre">2</span></tt> というオプションがついていますが、<br />
これは、「二個ずつ文字列を読み込む」という意味になります。<br />
つまり、空白・改行で区切られた文字列を二つ取ってきては、<br />
<tt class="docutils literal"><span class="pre">cp</span> <span class="pre">-p</span></tt> の後ろのオプションとして <tt class="docutils literal"><span class="pre">cp</span></tt> を実行します。</p><br />
<p>　ちなみに、 <tt class="docutils literal"><span class="pre">cp</span> <span class="pre">-p</span></tt> の <tt class="docutils literal"><span class="pre">-p</span></tt> は、<br />
ファイルの時刻や持ち主などをなるべく変えずにコピーしたいときに使います。</p><br />
<p>　このスクリプトの説明はこの辺にしておきます。<br />
大事なことは、このようなファイルやシステムの操作を繰り返すときは、<br />
大きなwhileループを書かず、<br />
リスト14のように、もうすでにやりたいことが書いてある状態のテキストを作っておいて、<br />
後から一気に処理すると速度の点やデバッグの点で有利になることが多いということです。<br />
特に今回のようにコピーなどの具体的なファイル移動が絡むと、<br />
スクリプトを書いて動作確認して・・・という作業が面倒になります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">./DISTRIBUTE_BY_DATE</span></tt> を実行して、リスト15のように、<br />
<tt class="docutils literal"><span class="pre">MAIL</span></tt> ディレクトリの下に日付のディレクトリができ、<br />
各日付のディレクトリ下にメールのファイルが配られていることを確認しましょう。</p><br />
<p>・リスト15: 実行結果</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls<br />
20120610 20120624 20120708 20120722 20120805 20120819 20120902 20120916<br />
20120611 20120625 20120709 20120723 20120806 20120820 20120903 20120917<br />
<span class="nv">$ </span>ls 20120920 | head -n 3<br />
1348066810.Vfc03I467066M309422.www5276ue.sakura.ne.jp<br />
1348067409.Vfc03I467067M503001.www5276ue.sakura.ne.jp<br />
1348068009.Vfc03I467068M641721.www5276ue.sakura.ne.jp<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="utf-8"><br />
<h2>12.6. UTF-8にする<a class="headerlink" href="#utf-8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　振り分けたら今度はエンコードの問題に取り組みましょう。<br />
メールのヘッダは、ISO-2022-JPやらBエンコードやらQエンコードやら、<br />
普通に暮らしていれば一生触れることもないものであふれています。<br />
リスト16のhogeファイルは、あるメールのヘッダを抜粋したものです。<br />
「To:」のところがわけがわからなくなっています。<br />
さらに困ったことに、「To:」のところとメールアドレスが違う行に渡っていて、<br />
grepしてもメールアドレスが取れません。</p><br />
<p>・リスト16: 難しいエンコーディングが施されたメール</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat hoge<br />
From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;<br />
To: <span class="o">=</span>?ISO-2022-JP?B?GyRCJCokKiQqJCokKiQqJCokKiEqMjYkTyEmISYhJkMvJEAhQSFBIUEbKEI<span class="o">=</span>?<span class="o">=</span><br />
 <span class="o">=</span>?ISO-2022-JP?B?GyRCIUEhKSEpISkbKEI<span class="o">=</span>?<span class="o">=</span> &lt;watashiha\@dare.com&gt;<br />
Content-Type: text/plain; <span class="nv">charset</span><span class="o">=</span>ISO-2022-JP<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　しかし我々にはnkfという味方がいます。我々は何も知らなくても、<br />
リスト17のようにnkfに突っ込んでUTF-8にすればよいのです。</p><br />
<p>・リスト17: nkfで変換</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>nkf -w hoge<br />
From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;<br />
To: おおおおおおおお！俺は・・・誰だ〜〜〜〜？？？ &lt;watashiha\@dare.com&gt;<br />
Content-Type: text/plain; <span class="nv">charset</span><span class="o">=</span>ISO-2022-JP<br />
</pre></div><br />
</td></tr></table></div><br />
<p>ちゃんと日本語になって、余計な改行も取れてます。<br />
（Toに複数のアドレスがあったら、改行されてしまうので、<br />
これは自分で補正しなければなりませんが。）<br />
ということで、とりあえずメールはnkfに突っ込んで変換して置いておけば、<br />
あとの処理が楽になります。</p><br />
<p>　とは言っても、もしかしたら変換前のメールも必要になるかもしれません。<br />
<tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> にコードを追加し、<br />
日付のディレクトリに、UTF-8化する前のメールと後のメール、<br />
両方置いておくことにしましょう。今回はこれでおしまいです。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> の <tt class="docutils literal"><span class="pre">rm</span> <span class="pre">-f</span> <span class="pre">$tmp-*</span></tt> の前に、<br />
リスト18のコードを加えます。<br />
もう一回、メールを <tt class="docutils literal"><span class="pre">&lt;日付&gt;.utf8</span></tt><br />
というディレクトリにコピーして、<br />
その中のメールに xargsで一気にnkfを適用しています。<br />
nkfには、 <tt class="docutils literal"><span class="pre">--overwrite</span></tt> を指定して、<br />
もとのファイルを上書きするようにしました。<br />
xargsを使っているのでリダイレクトができないからです。<br />
（もしかしたらリダイレクトする方法もあるかもしれません。）</p><br />
<p>・リスト18: UTF-8で変換したメールを保存するスクリプト片</p><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">######################################</span><br />
<span class="c">#UTF-8に変換</span><br />
<br />
<span class="c">#日別のディレクトリを作る</span><br />
self 1 <span class="nv">$tmp</span>-ymd-file |<br />
uniq |<br />
awk <span class="s1">&#39;{print $1 &quot;.utf8&quot;}&#39;</span> |<br />
xargs -P 100 mkdir -p<br />
<br />
<span class="c">#コピー</span><br />
cat <span class="nv">$tmp</span>-ymd-file |<br />
awk -v <span class="nv">sd</span><span class="o">=</span><span class="s2">&quot;$sdir&quot;</span> <span class="s1">&#39;{print sd &quot;/&quot; $2, &quot;./&quot; $1 &quot;.utf8/&quot;}&#39;</span> |<br />
xargs -P 100 -n 2 cp -p<br />
<br />
<span class="c">#変換</span><br />
<span class="nb">echo</span> ./*.utf8/* |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
xargs -n 1 nkf -w --overwrite<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これでもう一度 <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> を実行してみると、<br />
<tt class="docutils literal"><span class="pre">MAIL</span></tt> 下にリスト19のようにディレクトリができます。</p><br />
<p>・リスト19: ディレクトリの確認</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls<br />
20120610 20120623.utf8 20120707 20120720.utf8 ...<br />
20120610.utf8 20120624 20120707.utf8 20120721 ..<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　grepして、違いをみてみましょう。<br />
リスト20のようになっていれば成功です。</p><br />
<p>・リスト20: UTF-8への変換を確認</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ????????/* | head -n 2<br />
20120610/1339304183.Vfc03I46017dM943925.sakura1:From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;<br />
20120610/1339305265.Vfc03I46062cM458553.sakura1:From: <span class="o">=</span>?ISO-2022-JP?B?R21haWwgGyRCJUEhPCVgGyhC?<span class="o">=</span> &lt;mail-noreply\@google.com&gt;<br />
<span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ????????.utf8/* | head -n 2<br />
20120610.utf8/1339304183.Vfc03I46017dM943925.sakura1:From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;<br />
20120610.utf8/1339305265.Vfc03I46062cM458553.sakura1:From: Gmail チーム &lt;mail-noreply\@google.com&gt;<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id5"><br />
<h2>12.7. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、Maildirにたまったメールの操作を扱いました。<br />
久しぶりに書き方にこだわり、whileなしでシェルスクリプトを仕上げました。<br />
ただ単に見かけの問題からwhileを嫌うだけでなく、</p><br />
<ul class="simple"><br />
<li>コマンドを呼ぶ回数を減らす</li><br />
<li>xargsで並列化</li><br />
</ul><br />
<p>など、効用も得られることも示しました。</p><br />
<p>　メールには、エンコードや添付、<br />
不定形文の処理などいろいろテーマがありそうです。<br />
次回以降もいろいろいじくってみたいと思います。</p><br />
</div><br />
</div><br />
<br />

