---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年9月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>9. 開眼シェルスクリプト 第9回 バックグラウンド処理を使った並列化で早く仕事をやっつける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>9.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は格言を書く代わりに脱線した話から始めますが、<br />
工場で製品を組み立てるときの人や生産機械の配置の代表的な方法に、<br />
「ライン生産方式」と「セル生産方式」というものがあります。</p><br />
<p>　ライン生産方式というのはいわゆる流れ作業のことで、<br />
ベルトコンベアがあり、流れてくる部品を作業者がひたすら捌く方法です。<br />
作業は役割分担されており、一人の作業者は一つの作業しかしません。<br />
T型フォードの生産以来、100年の歴史がある方法です。</p><br />
<p>　セル生産方式の方は馴染みがないかもしれませんが、<br />
これはデジタルカメラなどの精密機械を作るときにたまに使われる方法で、<br />
一人に一つ屋台のようなものが与えられて、<br />
作業者がそこで1種類～数種類の製品を最初から最後まで組み立てる方法です。<br />
屋台は職人の仕事場を超効率的に<br />
（そしてノルマを電光掲示板で表示するなど恐ろしく）したもので、<br />
手の届く範囲の棚という棚に部品が置かれています。作業者は、<br />
移動せずに組み立て作業に没入できる（せざるを得ない）ようになっています。<br />
また、仕様が少し違う製品を同じ屋台で組むことができるため変化に柔軟です。</p><br />
<p>　この二つの方式は両極端な方法ですが、<br />
簡単で多く採用される方はライン生産方式です。<br />
作業者が覚えることが少ない、品質にばらつきが出にくい、<br />
あまり考えないで速く手を動かせる（=機械に置き換えやすい）などの理由から、<br />
本当の意味での大量生産に向いています。<br />
セル生産は難しいので、それに見合うメリットがないと採用されません。</p><br />
<div class="section" id="id3"><br />
<h3>9.1.1. なにが言いたいか「今回は邪道」<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　UNIX哲学にある「単機能コマンドをパイプでつなげ」という文言は、<br />
「データをライン生産方式で処理しろ」と言っているのと非常に良く似ています。<br />
UNIXでも生産工学でも、まずはパイプラインやベルトコンベアをどのように敷設するかということが、<br />
どうやって効率よくデータや製品を産出するかを考える第一歩になるわけです。<br />
従来はCPUが一つしかない（＝作業者が一人しかいない）のが普通だったので、<br />
パイプの効果というのはあまり重視されなかったようです。<br />
しかし今はCPUが複数あるので、生産工学の「常識」がUNIXでも実現しています。</p><br />
<p>　そういう前置きを書いておいてなんですが、<br />
今回扱うのは、どちらかというと生産工学では難しい方のセル生産です。<br />
同じ処理を並列に実行してCPUを使い切る方法です。<br />
リスト1に典型例を示します。</p><br />
<p>↓リスト1: gzipの並列実行</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>gzip data1 &amp;<br />
<span class="nv">$ </span>gzip data2 &amp;<br />
</pre></div><br />
</td></tr></table></div><br />
<p>実行中にtopで見てみると、CPUが二つ使われていることが分かります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>top -n 1 -c | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 5<br />
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND<br />
28700 ueda 20 0 8800 668 400 R 97 0.0 0:11.06 gzip data1<br />
28701 ueda 20 0 8800 668 400 R 97 0.0 0:09.37 gzip data2<br />
 1089 root 20 0 203m 30m 8612 S 2 0.5 6:55.93 /usr/b...<br />
22748 ueda 20 0 862m 52m 18m S 2 0.9 0:30.24 /usr/l...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　コマンド（とオプション）の後ろに「&amp;」をつけると、<br />
そのコマンドが終わらないうちに次のコマンドを打つことができることは、<br />
普段からCUIを使っている人には常識だと思います。<br />
もうちょっと説明すると、「&amp;」ありのコマンドは<br />
「バックグラウンドプロセス」で実行されます。<br />
これを使えば、CPUが二つ以上あるコンピュータで、並列処理を行うことができます。</p><br />
<p>　ただ、やる前に言っておきますが、このような処理で性能を引き出すには、<br />
セル生産方式同様、様々な条件が揃う必要があります。<br />
例えば上のgzipの例では、data1とdata2が同じHDD上にあると、<br />
いくらCPUを2個分使っていてもHDDは1個であり、<br />
二つのデータを同時に読み出すことはできません。<br />
ですから、これが必ず一個のプロセスで実行するより早いかどうかは分かりません。<br />
また、いわゆるmap/reduceのような操作の場合には、<br />
データを最初に二つに分ける処理も同時にはできないので、<br />
そこで性能が頭打ちになる可能性があります。</p><br />
<p>　そして案外、ネックになるのは人間の頭の方です。<br />
例えば端末上でバックグラウンドプロセスをいろいろ立ち上げたら、<br />
立ち上げた人間の方も何が走っているか把握していないと結果を収集できません。<br />
私のようにビールで頭がふやけている人がやると、<br />
混乱した挙句どうでもよくなってそのまま寝てしまうという事態に陥りかねません。</p><br />
<p>　一方で、処理するデータ量や計算量が大きいなど諸条件が揃うと時間を短縮できるので、<br />
知っておいて損することはありません。<br />
邪道と言ってはみたものの、<br />
バックグラウンドプロセスをシェルスクリプトで使う方法について、<br />
基礎的なことから書いていこうと思います。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>9.2. お題：バックグラウンドプロセスを使いこなす<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="id5"><br />
<h3>9.2.1. おさらい<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まずは端末での操作方法のおさらいをします。<br />
立ち上げるときは、ただ後ろに&amp;をつけるだけですね。</p><br />
<p>↓リスト2: バックグラウンド起動</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sleep 1000 &amp;<br />
<span class="o">[</span>1<span class="o">]</span> 24474<br />
<span class="nv">$ </span> &lt;- プロンプトが表示される<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　では、止めるときはどうしましょう。<br />
普通（フォアグラウンド）の処理ではCtrl+c連打ですが、<br />
バックグラウンドのプロセスにはどんなに悲壮に連打しても伝わりません。<br />
killというコマンドに「ジョブ番号」を指定して殺します。<br />
ジョブ番号は、上のリストの <tt class="docutils literal"><span class="pre">[1]</span> <span class="pre">23374</span></tt> の <tt class="docutils literal"><span class="pre">[1]</span></tt> の方です。<br />
ジョブ番号は、バックグラウンドプロセスを立ち上げたときに表示されますが、<br />
後からでも jobs というコマンドで確認できます。<br />
実際に止めるときには、リスト3のように <tt class="docutils literal"><span class="pre">kill</span> <span class="pre">%番号</span></tt> で止めます。</p><br />
<p>↓リスト3: バックグラウンドプロセスを止める</p><br />
<div class="highlight-bash"><pre>ueda\@X201:~/GIT/SD_GENKOU$ sleep 1000 &amp;<br />
[1] 31487<br />
ueda\@X201:~/GIT/SD_GENKOU$ jobs<br />
[1]+ 実行中 sleep 1000 &amp;<br />
ueda\@X201:~/GIT/SD_GENKOU$ kill %1<br />
ueda\@X201:~/GIT/SD_GENKOU$ jobs<br />
[1]+ Terminated sleep 1000<br />
ueda\@X201:~/GIT/SD_GENKOU$ jobs<br />
ueda\@X201:~/GIT/SD_GENKOU$</pre><br />
</div><br />
<p>　余談ですが、普段あまり端末を触らない人はプロセスを殺すことに抵抗があるかもしれませんが、<br />
別にどれだけバッシバッシ殺してもOSは不安定になりませんので、<br />
安心して殺していただいて構いません。躊躇せず屠ってください。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>9.2.2. シェルスクリプトで使う<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　シェルスクリプトでも&amp;をつけるとバックグラウンドプロセスになります。<br />
例えば、下のように書けば、バックアップを並列で行うことができます。<br />
5行目の <tt class="docutils literal"><span class="pre">&amp;&gt;</span> <span class="pre">/dev/null</span></tt> は標準出力もエラー出力も捨ててしまうと言う意味です。</p><br />
<p>↓リスト4: 並列にtarを立ち上げるシェルスクリプト</p><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># こんなスクリプト</span><br />
<span class="nv">$ </span>cat BACKUP<br />
<span class="c">#!/bin/bash</span><br />
<br />
tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null &amp;<br />
tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null &amp;<br />
<span class="c"># 実行！</span><br />
<span class="nv">$ </span>./BACKUP<br />
<span class="c"># CPUをちゃんと使っているか見る。</span><br />
<span class="nv">$ </span>top -n 1 -b | head<br />
<span class="nv">$ </span>cat hoge | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 4<br />
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND<br />
 4981 ueda 20 0 8800 652 432 R 79 0.0 0:26.23 gzip<br />
 4982 ueda 20 0 8800 632 428 R 77 0.0 0:27.07 gzip<br />
31938 ueda 20 0 2693m 1.1g 1.1g S 9 19.6 18:57.67 VirtualBox<br />
</pre></div><br />
</td></tr></table></div><br />
<p>これも止め方を書いておきます。シェルスクリプトから起動したバックグラウンドプロセスは、<br />
端末からjobsコマンドを叩いても状態を見ることができません。<br />
プロセスIDを指定してkillコマンドで止めるか、<br />
コマンド名を指定してkillallコマンドで止めます。</p><br />
<p>　リスト5はkillを使う方法で、psを使って確認しながら葬っていきます。<br />
こういうぷちぷち作業が嫌いな人は、<br />
リスト6のようにワンライナーを書いてください。</p><br />
<p>↓リスト5: killとpsでプロセスを殺す。</p><br />
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP<br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9818 pts/1 00:00:00 tar<br />
 9819 pts/1 00:00:00 tar<br />
 9820 pts/1 00:00:01 gzip<br />
 9821 pts/1 00:00:01 gzip<br />
 9822 pts/1 00:00:00 ps<br />
<span class="nv">$ </span><span class="nb">kill </span>9818<br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9819 pts/1 00:00:00 tar<br />
 9821 pts/1 00:00:10 gzip<br />
 9823 pts/1 00:00:00 ps<br />
<span class="nv">$ </span><span class="nb">kill </span>9819<br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9824 pts/1 00:00:00 ps<br />
</pre></div><br />
</td></tr></table></div><br />
<p>↓リスト6: killとpsとワンライナーでプロセスを殺す。</p><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP<br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9725 pts/1 00:00:00 tar<br />
 9726 pts/1 00:00:00 tar<br />
 9727 pts/1 00:00:01 gzip<br />
 9728 pts/1 00:00:01 gzip<br />
 9729 pts/1 00:00:00 ps<br />
<span class="nv">$ </span>ps | grep tar | awk <span class="s1">&#39;{print $1}&#39;</span> | xargs <span class="nb">kill</span><br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9852 pts/1 00:00:00 ps<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　だいたいの場合は、killallを使っても問題ないでしょう。<br />
上のpsを使った方法は慎重な方法で、BACKUPを起動した端末から実行して、<br />
BACKUPが起動したtarだけを捕捉しますが、<br />
リスト7の例では隣の端末のtarも殺しに行きますので注意してください。</p><br />
<p>↓リスト7: killall</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP<br />
<span class="nv">$ </span>killall tar<br />
<span class="nv">$ </span>ps<br />
 PID TTY TIME CMD<br />
 4364 pts/1 00:00:00 bash<br />
 9861 pts/1 00:00:00 ps<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>9.2.3. 空ファイルを使って制御する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さてシェルスクリプトBACKUPですが、<br />
tarを二つ立ち上げたらすぐスクリプトが終わってしまいます。<br />
これではいつ終わったか分からないので個人的には不便だと思います。<br />
そこで、二つのtarが終わらないとBACKUPが終わらないように細工をします。</p><br />
<p>　こういう制御をするときには、<br />
各バックグラウンド処理が終わったときに空ファイルを置き、<br />
それを待つというコードを書きます。リスト8に例を示します。<br />
空ファイルは、セマフォファイルとも言います。</p><br />
<p>↓リスト8: バックグラウンドプロセスの終了を待つ方法</p><br />
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat BACKUP.WAIT<br />
<span class="c">#!/bin/bash</span><br />
<br />
rm -f ./sem.<span class="o">{</span>1,2<span class="o">}</span><br />
<br />
<span class="o">{</span><br />
 tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null<br />
 touch ./sem.1<br />
<span class="o">}</span> &amp;<br />
<br />
<span class="o">{</span><br />
 tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null<br />
 touch ./sem.2<br />
<span class="o">}</span> &amp;<br />
<br />
<span class="k">while </span>sleep 3 ; <span class="k">do</span><br />
<span class="k"> if</span> <span class="o">[</span> -e ./sem.1 -a -e ./sem.2 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>rm ./sem.<span class="o">{</span>1,2<span class="o">}</span><br />
 <span class="nb">exit </span>0<br />
 <span class="k">fi</span><br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>このコードでまず大事なのは、コマンドを <tt class="docutils literal"><span class="pre">{</span> <span class="pre">}</span></tt> で囲んでグループ化し、<br />
<tt class="docutils literal"><span class="pre">}</span></tt> の後ろに&amp;をつける書き方です。<br />
こうすると、囲んだ部分がバックグラウンドプロセスで順番に実行されます。<br />
6-9行目、11-14行目はそれぞれ、tarの後、空のファイルを作っています。<br />
空ファイルができるときはその前のtarがすでに終わっていることが保証されるので、<br />
二つの空ファイルがあれば、処理が終わったと判断できるわけです。</p><br />
<p>　ちなみにtouchコマンドは、ファイルのアクセス時刻と修正時刻を変更するコマンドです。<br />
指定したファイルがないと、空のファイルができます。<br />
もう一つ空のファイルを作る方法に、 <tt class="docutils literal"><span class="pre">:</span> <span class="pre">&gt;</span> <span class="pre">./sem.1</span></tt> という書き方もあります。<br />
「:」は、何もしません。何もしないコマンドの出力をファイルにすると、<br />
空のファイルができます。<br />
また、4行目のrmは、残った <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> で誤動作しないように書いたものです。<br />
オプションなしでrmだけ書くと <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> が無い場合にエラーメッセージが出るので、<br />
fオプションでそれを抑制しています。</p><br />
<p>　16行目以降は空ファイルを待つコードです。<br />
3秒ごとにファイルの有無を確認して、あったらスクリプトを終了します。<br />
リスト9に、この仕組みの動作を確かめるスクリプトと実行結果を示します。<br />
実行例のように、書いた順序と出力が逆になっており、<br />
非同期で処理が進んでいることが分かります。</p><br />
<p>↓リスト9: バックグラウンドプロセスを待つ</p><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat WAIT<br />
<span class="c">#!/bin/bash</span><br />
<br />
rm -f ./sem.<span class="o">{</span>a,b<span class="o">}</span><br />
<br />
<span class="o">{</span> sleep 1; <span class="nb">echo </span>hogeA; :&gt; ./sem.a; <span class="o">}</span> &amp;<br />
<span class="o">{</span> <span class="nb">echo </span>hogeB; :&gt; ./sem.b; <span class="o">}</span> &amp;<br />
<br />
<span class="k">while </span>sleep 3 ; <span class="k">do</span><br />
 <span class="o">[</span> -e ./sem.a -a -e ./sem.b <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>0<br />
<span class="k">done</span><br />
<span class="nv">$ </span>./WAIT<br />
hogeB &lt;- すぐ出る<br />
hogeA &lt;- 1秒後<br />
<span class="nv">$ </span> &lt;- 3秒後<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h3>9.2.4. もっとスマートに止めるには<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　リスト8のスクリプトは処理の終わりまで待っているわけですが、<br />
Ctrl+cしてもtarが止まりません。あとからkillすればよいのですが、<br />
シェルスクリプトに処理を書くこともできるので紹介します。</p><br />
<p>　リスト10は、Ctrl+cされたらtarを止め、<br />
残る余計なファイルも消すシェルスクリプトです。</p><br />
<p>↓リスト10: Ctrl+cしたらtarを止めて掃除</p><br />
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
31</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat BACKUP.TRAP<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
EXIT<span class="o">(){</span><br />
 ps | grep tar | self 1 | xargs <span class="nb">kill</span><br />
<span class="nb"> </span>rm -f ./<span class="o">{</span>vm,old<span class="o">}</span>.tar.gz<br />
 <span class="k">while</span> ! rm ./sem.1 ; <span class="k">do </span>sleep 1 ; <span class="k">done</span><br />
<span class="k"> while</span> ! rm ./sem.2 ; <span class="k">do </span>sleep 1 ; <span class="k">done</span><br />
<span class="k"> </span><span class="nb">exit </span>1<br />
<span class="o">}</span><br />
<br />
<span class="nb">trap </span>EXIT 2<br />
<br />
rm -f ./sem.<span class="o">{</span>1,2<span class="o">}</span><br />
<br />
<span class="o">{</span><br />
 tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null<br />
 touch ./sem.1<br />
<span class="o">}</span> &amp;<br />
<br />
<span class="o">{</span><br />
 tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null<br />
 touch ./sem.2<br />
<span class="o">}</span> &amp;<br />
<br />
<span class="k">while </span>sleep 3 ; <span class="k">do</span><br />
<span class="k"> if</span> <span class="o">[</span> -e ./sem.1 -a -e ./sem.2 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>rm ./sem.<span class="o">{</span>1,2<span class="o">}</span><br />
 <span class="nb">exit </span>0<br />
 <span class="k">fi</span><br />
<span class="k">done</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　スクリプトの冒頭で <tt class="docutils literal"><span class="pre">trap</span> <span class="pre">コマンドor関数</span> <span class="pre">2</span></tt> と書くと、<br />
Ctrl+cが押されたときに、指定したコマンドあるいは関数を実行できるように仕掛けることができます。<br />
この例では、EXITという関数を呼び出すようにしてあります。<br />
2というのはシグナルの番号です。シグナルというのは、<br />
プログラムが走っている最中に何か起こった場合にそのプログラムに通知する仕組みです。<br />
ちなみに2番はSIGINTというシグナルで、<br />
「割り込みが起こった」ということを意味します。<br />
つまり、我々がCtrl+cを連打するのは「ちょっと待った！！待て！待て！・・・」<br />
という意味です。OS側は「待った!」の声を聞くと、<br />
当該処理を止めてメモリをきれいに掃除してくれます。</p><br />
<p>　EXIT関数の中身ですが、最低限必要なのは5行目のtarを止める処理です。<br />
6行目でtar.gzファイルを消して、7, 8行目で <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> を消しています。<br />
17行目、22行目のtarがkillされるとそれぞれ18行目、23行目のtouchが実行されるので、<br />
それを待ち受けてファイルを消します。<br />
EXIT関数の中身と18, 23行目のtouchは非同期に起こるので、whileで待たないと素通りすることがあります。<br />
<tt class="docutils literal"><span class="pre">while</span> <span class="pre">!</span> <span class="pre">rm</span> <span class="pre">./sem.1</span> <span class="pre">;</span> <span class="pre">do</span> <span class="pre">...</span> <span class="pre">;</span> <span class="pre">done</span></tt> でrmが成功するまでループします。</p><br />
<p>　実行結果をリスト11に示します。lsすると分かるように、<br />
Ctrl+c後には余計なファイルが残りません。</p><br />
<p>↓リスト11: trapでゴミファイルを残さない</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls<br />
BACKUP BACKUP.TRAP BACKUP.WAIT WAIT<br />
<span class="nv">$ </span>./BACKUP.TRAP<br />
^C &lt;- 割り込み！<br />
./BACKUP.TRAP: 18 行: 12065 Terminated tar zcvf vm.tar.gz ~/VM/ &amp;&gt;/dev/null<br />
./BACKUP.TRAP: 23 行: 12067 Terminated tar zcvf old.tar.gz ~/OLD/ &amp;&gt;/dev/null<br />
<span class="nv">$ </span>ls<br />
BACKUP BACKUP.TRAP BACKUP.WAIT WAIT<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
</div><br />
<div class="section" id="id9"><br />
<h2>9.3. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、バックグラウンドプロセスを使って処理を並列化するシェルスクリプトを扱いました。<br />
今回はif文、while文、trap、sleep、killなど、面倒なものを使いまくりで大変でした。<br />
結局、同じ処理をn個立ち上げると、入力と出力の口が2n個になってしまうので、<br />
なかなか思うようにコントロールするのは大変です。<br />
やっぱりパイプは簡単だと納得し、今回の終わりとしたいと思います。</p><br />
<p>　次回は、メールのバッチ処理を扱います。</p><br />
<div class="section" id="id10"><br />
<h3>9.3.1. 終わりの終わりに・・・<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回の並列化は、ソートの際に非常に有効です。ソートというのは、<br />
データの量が2倍になると計算量が3倍になったり4倍になったりする性質があります。<br />
そのため、ファイルを最初に均等分割してソートをかけて、<br />
あとからマージすると、単に負荷分散した以上の効果を得ることができます。</p><br />
<p>　ではなぜソートを扱わなかったか・・・。<br />
私のノートPCのsortコマンドが並列化していたからです。<br />
次のtopが証拠です。このノートPCのCPUは2コアx2スレッドで、<br />
CPUの使用率が400%近くなっています。<br />
もちろん、こんなことをしてくれるなら、<br />
何も考えずにコマンドの方に任せるべきです。</p><br />
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sort TESTDATA &amp;<br />
<span class="o">[</span>1<span class="o">]</span> 4368<br />
<span class="nv">$ </span>top -n 1 -b | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 3<br />
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND<br />
 4368 ueda 20 0 2139m 1.1g 916 R 396 19.4 0:37.92 sort<br />
 3956 ueda 20 0 535m 19m 11m S 2 0.3 0:00.95 gnome-terminal<br />
<span class="nv">$ </span>sort --version<br />
sort <span class="o">(</span>GNU coreutils<span class="o">)</span> 8.13<br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2011 Free Software Foundation, Inc.<br />
ライセンス GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;.<br />
This is free software: you are free to change and redistribute it.<br />
There is NO WARRANTY, to the extent permitted by law.<br />
<br />
作者 Mike Haertel および Paul Eggert。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>楽な時代になりましたね・・・。私の当初の原稿案はボツになりましたが・・・。</p><br />
</div><br />
</div><br />
</div><br />
<br />

