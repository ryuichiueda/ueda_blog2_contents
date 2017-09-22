---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年12月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>12. 開眼シェルスクリプト 第12回メールを操る<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>12.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　開眼シェルスクリプトも今回で12回目、つまり1年になります。
ネタが続くのか周囲は心配してましたが、まだまだ大丈夫そうです。</p>
<p>　編集サマの当初の企画意図を引っ張り出してみると、</p>
<p>「さまざまなLight Languageが流行っていますが、ちょっとした処理なら
プログラミングするまでもなくシェルスクリプトだけで実現できるものも
あります。（中略）身近なシェルを使いこなして、
もっと業務に生かそうというのが趣旨。」</p>
<p>とあります。そうです。シェルスクリプトを使うと、
ちょっとした処理を普段のシェル操作の延長線上で
さっさと片付けてしまうことができます。
ちょっとした処理なら身の回りにたくさんありますので、
今後も身の回りのことを次々に取り上げて、
皆様をCUIから離れられないようにしたいと思います。</p>
<p>　今回は電子メールを扱います。
Maildirに溜まったメールを仕分けたり、
中から文章などを切り出したりということをやってみます。</p>
</div>
<div class="section" id="id3">
<h2>12.2. 環境等<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、CentOS 6.3、Ubuntu 12.04 で動作確認しました。
FreeBSD でも動かそうとしたのですが、
dateコマンドにフィルタモードが見当たりませんでした。
while文で逃げるか、
標準入力からUNIX時間を受けて日付に変換するコマンドの自作をお願いします。
pythonで書いた例をリスト1に示しておきます。
（脚注：無理にシェルでやってもいいのですが、
コマンドは1プロセスで動かないとなにかと面倒です。）</p>
<p>・リスト1: UNIX時間を日付に変換するpythonスクリプト</p>
<div class="highlight-python"><pre>$ cat epoc2date
#!/usr/bin/python

import sys
import time

for line in sys.stdin:
 unixtime = line.rstrip()
 t = time.gmtime(int(unixtime))
 print "%d %d %d" % (t.tm_year, t.tm_mon, t.tm_mday)
$ date +%s | ./epoc2date
2012 9 21</pre>
</div>
</div>
<div class="section" id="mairdir">
<h2>12.3. Mairdir<a class="headerlink" href="#mairdir" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　筆者は、とあるサーバの自分のアカウントに、
自分が管理しているサーバからの自動送信メールを貯めています。
メールをホームに置いているのはこのサーバのpostfixです。</p>
<p>　このpostfixの設定ファイルで、
ホームにメールを置くときの形式をMaildirにしています。
ヘビーにUNIXを使っている人はご存知だと思いますが、
Maildirは、メールを置いておくときの方法の一つです。
Maildir形式では、電子メール一通が一つのファイルになります。</p>
<p>　念のため、postfixの設定ファイルの一部をリスト2に示しておきます。
<tt class="docutils literal"><span class="pre">main.cf</span></tt> の <tt class="docutils literal"><span class="pre">home_mailbox</span></tt> の値を <tt class="docutils literal"><span class="pre">Maildir/</span></tt>
にしておくと、Maildirになります。
デフォルトでは、 <tt class="docutils literal"><span class="pre">Mailbox</span></tt> になっているのですが、
これだと複数のメールが一つの <tt class="docutils literal"><span class="pre">mbox</span></tt>
というファイルに固まって置かれてしまっていろいろとたちの悪いことになります。</p>
<p>・リスト2: main.cfの設定</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>vi /etc/postfix/main.cf
...
<span class="c"># DELIVERY TO MAILBOX</span>
<span class="c">#</span>
<span class="c"># The home_mailbox parameter specifies the optional pathname of a</span>
<span class="c"># mailbox file relative to a user&#39;s home directory. The default</span>
<span class="c"># mailbox file is /var/spool/mail/user or /var/mail/user. Specify</span>
<span class="c"># &quot;Maildir/&quot; for qmail-style delivery (the / is required).</span>
<span class="c">#</span>
<span class="c">#home_mailbox = Mailbox &lt;- mboxを使う</span>
<span class="nv">home_mailbox</span> <span class="o">=</span> Maildir/ &lt;- Maildirを使う
...
</pre></div>
</td></tr></table></div>
<p>　Maildir形式を選ぶと、ホーム下には <tt class="docutils literal"><span class="pre">Maildir</span></tt>
というディレクトリができます。
今までのpostfixの話がちんぷんかんぷんでも、
ホームの下に <tt class="docutils literal"><span class="pre">Maildir</span></tt> がいたら、
今回の方法はいろいろ試すことができることでしょう。
深いことを知らなくても目の前にテキストが
あったらやっちまえというスタンスでいきましょう。
そうでないと、
理屈ばっかりで肝心のコンピューティングがつまらなくなります。
道具は使ってナンボのモンです。</p>
<p>　 <tt class="docutils literal"><span class="pre">~/Maildir</span></tt> の下には、リスト3のように
<tt class="docutils literal"><span class="pre">cur,</span> <span class="pre">new,</span> <span class="pre">tmp</span></tt> という三つのディレクトリがあります。</p>
<p>・リスト3: Maildirディレクトリの下</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls ~/Maildir
cur new tmp
</pre></div>
</td></tr></table></div>
<p>　メーラーで見たファイルはcur、新しいメールはnewに入るようですが、
私はメーラーなどというナンパなものを使ってないので、
全部newに入ったままです（脚注：実際はgmailのヘビーユーザーですごめんなさい。）。
リスト4に、 <tt class="docutils literal"><span class="pre">new</span></tt> の下の様子を示します。</p>
<p>・リスト4: メールファイル</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls new/ | head -n 3
1339304183.Vfc03I46017dM943925.sakura1
1339305265.Vfc03I46062cM458553.sakura1
1339306807.Vfc03I4607c6M993984.sakura1
<span class="c">#2万5千件程度入ってます。</span>
<span class="nv">$ </span>ls ~/Maildir/new/ | wc -l
25094
</pre></div>
</td></tr></table></div>
<p>　実際問題、このメールアカウントに溜まっているのはログばっかりなので、
これを全部メーラーに入れてしまって一つずつ見るのは疲れます。
また、メーラーでいろいろ設定して振り分けるのも、
メーラーの癖や制限があって大変です。
結局見なくなるので、なにか有用な統計と取ったほうがよいでしょう。
こんなときにシェルスクリプトです。奥さん。</p>
</div>
<div class="section" id="id4">
<h2>12.4. ファイル名を眺める<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　もう少し観察してみましょう。
ファイル名は、重複しないように一意になるように工夫されているようです。
リスト5のファイル名をまじまじと見ると、
postfixの置くファイルには、先頭に時刻が入っているようです。</p>
<p>・リスト5: メールのファイル名</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>1339304183.Vfc03I46017dM943925.sakura1
</pre></div>
</td></tr></table></div>
<p>この「1339304183」は、「UNIX時間」というやつで、
1970年1月1日0時0分0秒からの積算秒数を表しています。
Linuxのdateコマンドなら、こんなふうに変換できます。</p>
<p>・リスト6: UNIX時間の変換</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>date -d \@1339304183
2012年 6月 10日 日曜日 13:56:23 JST
</pre></div>
</td></tr></table></div>
<p>　ちなみに、dateコマンドには-fというオプションがあって、
以下のような使い方ができます。これは便利です。</p>
<p>・リスト7: dateのフィルタモード</p>
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#使ったバージョンはこれ。</span>
<span class="nv">$ </span>date --version
date <span class="o">(</span>GNU coreutils<span class="o">)</span> 8.13
（略）
<span class="nv">$ </span>head -n 3 datefile
\@1339304183
\@1339305265
\@1339306807
<span class="nv">$ </span>head -n 3 datefile | date -f -
2012年 6月 10日 日曜日 13:56:23 JST
2012年 6月 10日 日曜日 14:14:25 JST
2012年 6月 10日 日曜日 14:40:07 JST
<span class="nv">$ </span>head -n 3 datefile | date -f - <span class="s2">&quot;+%Y%m%d %H%M%S&quot;</span>
20120610 135623
20120610 141425
20120610 144007
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="while">
<h2>12.5. まずは振り分けてみる（whileを使わずに）<a class="headerlink" href="#while" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まず肩慣らし程度にメールを日付で振り分けてみます。
こうしておけば、例えばある日からある日までのメールを処理したいときに、
いちいちUNIX時間を変換しなくてもよくなります。</p>
<p>　ホーム下に <tt class="docutils literal"><span class="pre">MAIL</span></tt> というディレクトリを作って、
その下に日別のディレクトリを自動で作り、その下にメールをコピーします。</p>
<p>　ただ、肩慣らしと言っても一筋縄ではいかないのがこの連載。
最近、while使うなとあまり言ってませんが、
忘れたわけではありません。whileは避けるべきです。
ここでもwhileを抜く効用を示してみます。</p>
<p>　まずはベタにリスト8のように書いてみます。
ファイルを一個ずつ日付のディレクトリに放り込んでいきます。</p>
<p>・リスト8: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE.betabeta</span></tt> （ベタベタな例）</p>
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#ベタベタバージョン</span>
<span class="nv">$ </span>cat DISTRIBUTE_BY_DATE.betabeta
<span class="c">#!/bin/bash</span>

<span class="nv">sdir</span><span class="o">=</span>/home/ueda/Maildir/new
<span class="nv">ddir</span><span class="o">=</span>/home/ueda/MAIL

<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>

<span class="nb">cd</span> <span class="nv">$sdir</span> <span class="o">||</span> <span class="nb">exit </span>1

<span class="c">######################################</span>
<span class="c">#ファイルのリストを作る</span>
<span class="nb">echo</span> *.*.* |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
<span class="k">while </span><span class="nb">read </span>f ; <span class="k">do</span>
<span class="k"> </span><span class="nv">UNIXTIME</span><span class="o">=</span><span class="s2">&quot;\@&quot;</span><span class="k">$(</span><span class="nb">echo</span> <span class="nv">$f</span> | awk -F. <span class="s1">&#39;{print $1}&#39;</span><span class="k">)</span>
 <span class="nv">DATE</span><span class="o">=</span><span class="k">$(</span>date -d <span class="nv">$UNIXTIME</span> <span class="s2">&quot;+%Y%m%d&quot;</span><span class="k">)</span>

 <span class="o">[</span> -e <span class="s2">&quot;$ddir/$DATE&quot;</span> <span class="o">]</span> <span class="o">||</span> mkdir <span class="nv">$ddir</span>/<span class="nv">$DATE</span>
 cp -p <span class="nv">$f</span> <span class="nv">$ddir</span>/<span class="nv">$DATE</span>/
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>13行目のechoは、ファイル名を空白区切りで出力してくれます。
いつもlsを使っている人は、適当なディレクトリで <tt class="docutils literal"><span class="pre">echo</span> <span class="pre">*</span></tt>
と打ってみてください。ファイルの一覧が取得できます。
ファイル名が取得できたら、trで空白を改行に変換し、
一つ一つ <tt class="docutils literal"><span class="pre">while</span></tt> で読んで処理していきます。</p>
<p>　上のスクリプトは何のソツもありません。
まあ、世の99%の人がこのように書くと思います。
しかし、あえて言います。</p>
<blockquote>
<div>失格！！！！</div></blockquote>
<p>です。</p>
<p>　サーバで試してみます。結果はリスト9のようになりました。</p>
<p>・リスト9: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE.betabeta</span></tt> は時間がかかる。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE.betabeta

real 7m21.673s
user 1m24.858s
sys 5m51.464s
</pre></div>
</td></tr></table></div>
<p>筆者が書いた失格でないスクリプトについて、
お見せする前に実行時間を測ってみましょう。
リスト10のようになりました。</p>
<p>・リスト10: これくらいは高速化できる。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE

real 0m43.866s
user 0m16.774s
sys 0m43.599s
</pre></div>
</td></tr></table></div>
<p>というように、10倍以上の差がついてしまいます。
今回みたいに何万もファイルを扱うときは、
この差は大きくなります。</p>
<p>　ではどう書いたかというのを次に見せます。
ちょっと長くなってしまったので良し悪しですが・・・
（じゃあ失格とか言うな）。</p>
<p>・リスト11: <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt></p>
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
42
43
44
45
46
47
48</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat DISTRIBUTE_BY_DATE
<span class="c">#!/bin/bash</span>

<span class="nv">sdir</span><span class="o">=</span>/home/ueda/Maildir/new
<span class="nv">ddir</span><span class="o">=</span>/home/ueda/MAIL
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>

<span class="nb">cd</span> <span class="nv">$sdir</span> <span class="o">||</span> <span class="nb">exit </span>1

<span class="c">######################################</span>
<span class="c">#ファイルのリストを作る</span>
<span class="nb">echo</span> *.*.* |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
<span class="c">#1:ファイル名</span>
awk -F. <span class="s1">&#39;{print &quot;\@&quot; $1,$0}&#39;</span> &gt; <span class="nv">$tmp</span>-files
<span class="c">#1:UNIX時間 2:ファイル名</span>

<span class="c"># $tmp-filesの例：</span>
<span class="c">#\@1348117807 1348117807.Vfc03I4670eaM254446.www5276ue.sakura.ne.jp</span>

<span class="c">######################################</span>
<span class="c">#ファイルのリストに年月日をくっつける</span>
self 1 <span class="nv">$tmp</span>-files |
date -f - <span class="s2">&quot;+%Y%m%d&quot;</span> |
<span class="c">#1:年月日</span>
ycat - <span class="nv">$tmp</span>-files |
<span class="c">#1:年月日 2:UNIX時間 3:ファイル名</span>
delf 2 &gt; <span class="nv">$tmp</span>-ymd-file
<span class="c">#1:年月日 2:ファイル名</span>

<span class="c"># $tmp-ymd-fileの例</span>
<span class="c">#20120920 1348116008.Vfc03I4670ecM186337.www5276ue.sakura.ne.jp</span>

<span class="nb">cd</span> <span class="nv">$ddir</span> <span class="o">||</span> <span class="nb">exit </span>1

<span class="c">######################################</span>
<span class="c">#日別のディレクトリを作る</span>
self 1 <span class="nv">$tmp</span>-ymd-file |
uniq |
xargs -P 0 -i_ mkdir -p _

cat <span class="nv">$tmp</span>-ymd-file |
awk -v <span class="nv">sd</span><span class="o">=</span><span class="s2">&quot;$sdir&quot;</span> <span class="s1">&#39;{print sd &quot;/&quot; $2, &quot;./&quot; $1 &quot;/&quot;}&#39;</span> |
<span class="c">#コピー元、コピー先を読み込んでcpに渡す。</span>
xargs -P 0 -n 2 cp -p

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>このスクリプトでは、一個一個ファイルを処理するのではなく、
作るディレクトリのリストとコピーするファイルのリストを作成し、
xargsで一気に作っています。
速いのはxargsそのものの速さの寄与も大きいのですが、
dateとawkをwhileで何回も呼ぶ必要がなくなっていることも原因です。</p>
<p>　速い方のスクリプトを詳しく見ていきましょう。
まず、15行目の処理が終わって出力される
<tt class="docutils literal"><span class="pre">$tmp-files</span></tt> は、19行目の例のようなレコードが縦に並んだファイルです。
そして、23行目でUNIX時間だけとってきて、24行目のdateコマンドに流し込んでいます。
ここで、ファイルごとにdateを読むのではなく、
全ファイルに対して一回だけしかdateを読まなくてよくなります。</p>
<p>　26行目のycatは、Open usp Tukubai のコマンドです。
「横キャット」と発音します。横にファイルをくっつけます。
例をリスト12のように示します。Open usp Tukubaiの詳細は、
UEC（ <tt class="docutils literal"><span class="pre">https://uec.usp-lab.com</span></tt> ）のサイトでご確認を。</p>
<p>・リスト12: <tt class="docutils literal"><span class="pre">ycat</span></tt> の使い方</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat file1
1
2
3
<span class="nv">$ </span>cat file2
a
b
c
<span class="nv">$ </span>ycat file<span class="o">{</span>1,2<span class="o">}</span>
1 a
2 b
3 c
</pre></div>
</td></tr></table></div>
<p>これで、dateで作った日付が、もとの <tt class="docutils literal"><span class="pre">$tmp-files</span></tt> のレコードにくっつきます。
32行目に、 <tt class="docutils literal"><span class="pre">$tmp-ymd-file</span></tt> のレコードを抜き取った例がありますが、
この時点で、日付とファイル名という、処理に必要なデータが揃います。</p>
<p>　後は、日付のディレクトリを作り、
その中にファイルをコピーしていきます。
xargsについては、1,5,9月号に出てきました。
まず、40行目の</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>xargs -P 0 mkdir -p
</pre></div>
</td></tr></table></div>
<p>は、入力から日付を次々に受け取って、
mkdirコマンドを実行していきます。
mkdirの-pオプションは、
すでにディレクトリがあってもエラーにならないように指定しています。
xargsの <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">0</span></tt> ですが、
これは、xargsで指定したコマンドを、
できるだけ多くのプロセスで実行するという意味になります。
manには「できるだけ」としか書いていないのが気になりますが、
並列化してくれるようです。
ここでは「できるだけ」にツッコミは入れず、
<tt class="docutils literal"><span class="pre">-P</span> <span class="pre">0</span></tt> の有無で結果だけリスト13に示します。
筆者の環境では、有意な差が出ています。</p>
<p>　後日談：何回も実験しているうちに、
一回だけものすごい数のcpが立ち上がって自分のノートPCが暴走しました・・・。
めったに起こらないのですが、せいぜい <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">100</span></tt> くらいにしておいてください。
今のマシンやカーネルは頑丈なので、100プロセスぐらいなら何の問題もありません。</p>
<p>・リスト13: -P オプション有無での時間比較</p>
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
11</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE.nop

real 2m58.583s
user 0m27.764s
sys 2m2.736s
<span class="nv">$ </span>rm -Rf 2*
<span class="nv">$ </span><span class="nb">time</span> ./DISTRIBUTE_BY_DATE

real 0m41.221s
user 0m16.201s
sys 0m40.139s
</pre></div>
</td></tr></table></div>
<p>　45行目のxargsは、さらに複雑なことをしています。
このxargsには、次のようなテキストが流れ込みます。</p>
<p>・リスト14: xargsに入力するテキスト</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>/home/ueda/Maildir/new/1339308608.Vfc03I4609ebM178619.sakura1 ./20120610/
/home/ueda/Maildir/new/1339308909.Vfc03I4609ecM601364.sakura1 ./20120610/
/home/ueda/Maildir/new/1339309208.Vfc03I4609edM55303.sakura1 ./20120610/
...
</pre></div>
</td></tr></table></div>
<p>つまり、コピー元のファイルとコピー先のディレクトリがxargsに流れ込みます。
xargsには、 <tt class="docutils literal"><span class="pre">-n</span> <span class="pre">2</span></tt> というオプションがついていますが、
これは、「二個ずつ文字列を読み込む」という意味になります。
つまり、空白・改行で区切られた文字列を二つ取ってきては、
<tt class="docutils literal"><span class="pre">cp</span> <span class="pre">-p</span></tt> の後ろのオプションとして <tt class="docutils literal"><span class="pre">cp</span></tt> を実行します。</p>
<p>　ちなみに、 <tt class="docutils literal"><span class="pre">cp</span> <span class="pre">-p</span></tt> の <tt class="docutils literal"><span class="pre">-p</span></tt> は、
ファイルの時刻や持ち主などをなるべく変えずにコピーしたいときに使います。</p>
<p>　このスクリプトの説明はこの辺にしておきます。
大事なことは、このようなファイルやシステムの操作を繰り返すときは、
大きなwhileループを書かず、
リスト14のように、もうすでにやりたいことが書いてある状態のテキストを作っておいて、
後から一気に処理すると速度の点やデバッグの点で有利になることが多いということです。
特に今回のようにコピーなどの具体的なファイル移動が絡むと、
スクリプトを書いて動作確認して・・・という作業が面倒になります。</p>
<p>　 <tt class="docutils literal"><span class="pre">./DISTRIBUTE_BY_DATE</span></tt> を実行して、リスト15のように、
<tt class="docutils literal"><span class="pre">MAIL</span></tt> ディレクトリの下に日付のディレクトリができ、
各日付のディレクトリ下にメールのファイルが配られていることを確認しましょう。</p>
<p>・リスト15: 実行結果</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls
20120610 20120624 20120708 20120722 20120805 20120819 20120902 20120916
20120611 20120625 20120709 20120723 20120806 20120820 20120903 20120917
<span class="nv">$ </span>ls 20120920 | head -n 3
1348066810.Vfc03I467066M309422.www5276ue.sakura.ne.jp
1348067409.Vfc03I467067M503001.www5276ue.sakura.ne.jp
1348068009.Vfc03I467068M641721.www5276ue.sakura.ne.jp
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="utf-8">
<h2>12.6. UTF-8にする<a class="headerlink" href="#utf-8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　振り分けたら今度はエンコードの問題に取り組みましょう。
メールのヘッダは、ISO-2022-JPやらBエンコードやらQエンコードやら、
普通に暮らしていれば一生触れることもないものであふれています。
リスト16のhogeファイルは、あるメールのヘッダを抜粋したものです。
「To:」のところがわけがわからなくなっています。
さらに困ったことに、「To:」のところとメールアドレスが違う行に渡っていて、
grepしてもメールアドレスが取れません。</p>
<p>・リスト16: 難しいエンコーディングが施されたメール</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat hoge
From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;
To: <span class="o">=</span>?ISO-2022-JP?B?GyRCJCokKiQqJCokKiQqJCokKiEqMjYkTyEmISYhJkMvJEAhQSFBIUEbKEI<span class="o">=</span>?<span class="o">=</span>
 <span class="o">=</span>?ISO-2022-JP?B?GyRCIUEhKSEpISkbKEI<span class="o">=</span>?<span class="o">=</span> &lt;watashiha\@dare.com&gt;
Content-Type: text/plain; <span class="nv">charset</span><span class="o">=</span>ISO-2022-JP
</pre></div>
</td></tr></table></div>
<p>　しかし我々にはnkfという味方がいます。我々は何も知らなくても、
リスト17のようにnkfに突っ込んでUTF-8にすればよいのです。</p>
<p>・リスト17: nkfで変換</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>nkf -w hoge
From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;
To: おおおおおおおお！俺は・・・誰だ〜〜〜〜？？？ &lt;watashiha\@dare.com&gt;
Content-Type: text/plain; <span class="nv">charset</span><span class="o">=</span>ISO-2022-JP
</pre></div>
</td></tr></table></div>
<p>ちゃんと日本語になって、余計な改行も取れてます。
（Toに複数のアドレスがあったら、改行されてしまうので、
これは自分で補正しなければなりませんが。）
ということで、とりあえずメールはnkfに突っ込んで変換して置いておけば、
あとの処理が楽になります。</p>
<p>　とは言っても、もしかしたら変換前のメールも必要になるかもしれません。
<tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> にコードを追加し、
日付のディレクトリに、UTF-8化する前のメールと後のメール、
両方置いておくことにしましょう。今回はこれでおしまいです。</p>
<p>　 <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> の <tt class="docutils literal"><span class="pre">rm</span> <span class="pre">-f</span> <span class="pre">$tmp-*</span></tt> の前に、
リスト18のコードを加えます。
もう一回、メールを <tt class="docutils literal"><span class="pre">&lt;日付&gt;.utf8</span></tt>
というディレクトリにコピーして、
その中のメールに xargsで一気にnkfを適用しています。
nkfには、 <tt class="docutils literal"><span class="pre">--overwrite</span></tt> を指定して、
もとのファイルを上書きするようにしました。
xargsを使っているのでリダイレクトができないからです。
（もしかしたらリダイレクトする方法もあるかもしれません。）</p>
<p>・リスト18: UTF-8で変換したメールを保存するスクリプト片</p>
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
18</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">######################################</span>
<span class="c">#UTF-8に変換</span>

<span class="c">#日別のディレクトリを作る</span>
self 1 <span class="nv">$tmp</span>-ymd-file |
uniq |
awk <span class="s1">&#39;{print $1 &quot;.utf8&quot;}&#39;</span> |
xargs -P 100 mkdir -p

<span class="c">#コピー</span>
cat <span class="nv">$tmp</span>-ymd-file |
awk -v <span class="nv">sd</span><span class="o">=</span><span class="s2">&quot;$sdir&quot;</span> <span class="s1">&#39;{print sd &quot;/&quot; $2, &quot;./&quot; $1 &quot;.utf8/&quot;}&#39;</span> |
xargs -P 100 -n 2 cp -p

<span class="c">#変換</span>
<span class="nb">echo</span> ./*.utf8/* |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
xargs -n 1 nkf -w --overwrite
</pre></div>
</td></tr></table></div>
<p>　これでもう一度 <tt class="docutils literal"><span class="pre">DISTRIBUTE_BY_DATE</span></tt> を実行してみると、
<tt class="docutils literal"><span class="pre">MAIL</span></tt> 下にリスト19のようにディレクトリができます。</p>
<p>・リスト19: ディレクトリの確認</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls
20120610 20120623.utf8 20120707 20120720.utf8 ...
20120610.utf8 20120624 20120707.utf8 20120721 ..
...
</pre></div>
</td></tr></table></div>
<p>　grepして、違いをみてみましょう。
リスト20のようになっていれば成功です。</p>
<p>・リスト20: UTF-8への変換を確認</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ????????/* | head -n 2
20120610/1339304183.Vfc03I46017dM943925.sakura1:From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;
20120610/1339305265.Vfc03I46062cM458553.sakura1:From: <span class="o">=</span>?ISO-2022-JP?B?R21haWwgGyRCJUEhPCVgGyhC?<span class="o">=</span> &lt;mail-noreply\@google.com&gt;
<span class="nv">$ </span>grep <span class="s2">&quot;^From:&quot;</span> ????????.utf8/* | head -n 2
20120610.utf8/1339304183.Vfc03I46017dM943925.sakura1:From: Ryuichi UEDA &lt;r-ueda\@usp-lab.com&gt;
20120610.utf8/1339305265.Vfc03I46062cM458553.sakura1:From: Gmail チーム &lt;mail-noreply\@google.com&gt;
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id5">
<h2>12.7. おわりに<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、Maildirにたまったメールの操作を扱いました。
久しぶりに書き方にこだわり、whileなしでシェルスクリプトを仕上げました。
ただ単に見かけの問題からwhileを嫌うだけでなく、</p>
<ul class="simple">
<li>コマンドを呼ぶ回数を減らす</li>
<li>xargsで並列化</li>
</ul>
<p>など、効用も得られることも示しました。</p>
<p>　メールには、エンコードや添付、
不定形文の処理などいろいろテーマがありそうです。
次回以降もいろいろいじくってみたいと思います。</p>
</div>
</div>


