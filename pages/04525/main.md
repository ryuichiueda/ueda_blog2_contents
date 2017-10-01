---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年9月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>9. 開眼シェルスクリプト 第9回 バックグラウンド処理を使った並列化で早く仕事をやっつける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>9.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は格言を書く代わりに脱線した話から始めますが、
工場で製品を組み立てるときの人や生産機械の配置の代表的な方法に、
「ライン生産方式」と「セル生産方式」というものがあります。</p>
<p>　ライン生産方式というのはいわゆる流れ作業のことで、
ベルトコンベアがあり、流れてくる部品を作業者がひたすら捌く方法です。
作業は役割分担されており、一人の作業者は一つの作業しかしません。
T型フォードの生産以来、100年の歴史がある方法です。</p>
<p>　セル生産方式の方は馴染みがないかもしれませんが、
これはデジタルカメラなどの精密機械を作るときにたまに使われる方法で、
一人に一つ屋台のようなものが与えられて、
作業者がそこで1種類～数種類の製品を最初から最後まで組み立てる方法です。
屋台は職人の仕事場を超効率的に
（そしてノルマを電光掲示板で表示するなど恐ろしく）したもので、
手の届く範囲の棚という棚に部品が置かれています。作業者は、
移動せずに組み立て作業に没入できる（せざるを得ない）ようになっています。
また、仕様が少し違う製品を同じ屋台で組むことができるため変化に柔軟です。</p>
<p>　この二つの方式は両極端な方法ですが、
簡単で多く採用される方はライン生産方式です。
作業者が覚えることが少ない、品質にばらつきが出にくい、
あまり考えないで速く手を動かせる（=機械に置き換えやすい）などの理由から、
本当の意味での大量生産に向いています。
セル生産は難しいので、それに見合うメリットがないと採用されません。</p>
<div class="section" id="id3">
<h3>9.1.1. なにが言いたいか「今回は邪道」<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　UNIX哲学にある「単機能コマンドをパイプでつなげ」という文言は、
「データをライン生産方式で処理しろ」と言っているのと非常に良く似ています。
UNIXでも生産工学でも、まずはパイプラインやベルトコンベアをどのように敷設するかということが、
どうやって効率よくデータや製品を産出するかを考える第一歩になるわけです。
従来はCPUが一つしかない（＝作業者が一人しかいない）のが普通だったので、
パイプの効果というのはあまり重視されなかったようです。
しかし今はCPUが複数あるので、生産工学の「常識」がUNIXでも実現しています。</p>
<p>　そういう前置きを書いておいてなんですが、
今回扱うのは、どちらかというと生産工学では難しい方のセル生産です。
同じ処理を並列に実行してCPUを使い切る方法です。
リスト1に典型例を示します。</p>
<p>↓リスト1: gzipの並列実行</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>gzip data1 &amp;
<span class="nv">$ </span>gzip data2 &amp;
</pre></div>
</td></tr></table></div>
<p>実行中にtopで見てみると、CPUが二つ使われていることが分かります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>ueda@uedaubuntu:~<span class="nv">$ </span>top -n 1 -c | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 5
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
28700 ueda 20 0 8800 668 400 R 97 0.0 0:11.06 gzip data1
28701 ueda 20 0 8800 668 400 R 97 0.0 0:09.37 gzip data2
 1089 root 20 0 203m 30m 8612 S 2 0.5 6:55.93 /usr/b...
22748 ueda 20 0 862m 52m 18m S 2 0.9 0:30.24 /usr/l...
</pre></div>
</td></tr></table></div>
<p>　コマンド（とオプション）の後ろに「&amp;」をつけると、
そのコマンドが終わらないうちに次のコマンドを打つことができることは、
普段からCUIを使っている人には常識だと思います。
もうちょっと説明すると、「&amp;」ありのコマンドは
「バックグラウンドプロセス」で実行されます。
これを使えば、CPUが二つ以上あるコンピュータで、並列処理を行うことができます。</p>
<p>　ただ、やる前に言っておきますが、このような処理で性能を引き出すには、
セル生産方式同様、様々な条件が揃う必要があります。
例えば上のgzipの例では、data1とdata2が同じHDD上にあると、
いくらCPUを2個分使っていてもHDDは1個であり、
二つのデータを同時に読み出すことはできません。
ですから、これが必ず一個のプロセスで実行するより早いかどうかは分かりません。
また、いわゆるmap/reduceのような操作の場合には、
データを最初に二つに分ける処理も同時にはできないので、
そこで性能が頭打ちになる可能性があります。</p>
<p>　そして案外、ネックになるのは人間の頭の方です。
例えば端末上でバックグラウンドプロセスをいろいろ立ち上げたら、
立ち上げた人間の方も何が走っているか把握していないと結果を収集できません。
私のようにビールで頭がふやけている人がやると、
混乱した挙句どうでもよくなってそのまま寝てしまうという事態に陥りかねません。</p>
<p>　一方で、処理するデータ量や計算量が大きいなど諸条件が揃うと時間を短縮できるので、
知っておいて損することはありません。
邪道と言ってはみたものの、
バックグラウンドプロセスをシェルスクリプトで使う方法について、
基礎的なことから書いていこうと思います。</p>
</div>
</div>
<div class="section" id="id4">
<h2>9.2. お題：バックグラウンドプロセスを使いこなす<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="id5">
<h3>9.2.1. おさらい<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まずは端末での操作方法のおさらいをします。
立ち上げるときは、ただ後ろに&amp;をつけるだけですね。</p>
<p>↓リスト2: バックグラウンド起動</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sleep 1000 &amp;
<span class="o">[</span>1<span class="o">]</span> 24474
<span class="nv">$ </span> &lt;- プロンプトが表示される
</pre></div>
</td></tr></table></div>
<p>　では、止めるときはどうしましょう。
普通（フォアグラウンド）の処理ではCtrl+c連打ですが、
バックグラウンドのプロセスにはどんなに悲壮に連打しても伝わりません。
killというコマンドに「ジョブ番号」を指定して殺します。
ジョブ番号は、上のリストの <tt class="docutils literal"><span class="pre">[1]</span> <span class="pre">23374</span></tt> の <tt class="docutils literal"><span class="pre">[1]</span></tt> の方です。
ジョブ番号は、バックグラウンドプロセスを立ち上げたときに表示されますが、
後からでも jobs というコマンドで確認できます。
実際に止めるときには、リスト3のように <tt class="docutils literal"><span class="pre">kill</span> <span class="pre">%番号</span></tt> で止めます。</p>
<p>↓リスト3: バックグラウンドプロセスを止める</p>
<div class="highlight-bash"><pre>ueda@X201:~/GIT/SD_GENKOU$ sleep 1000 &amp;
[1] 31487
ueda@X201:~/GIT/SD_GENKOU$ jobs
[1]+ 実行中 sleep 1000 &amp;
ueda@X201:~/GIT/SD_GENKOU$ kill %1
ueda@X201:~/GIT/SD_GENKOU$ jobs
[1]+ Terminated sleep 1000
ueda@X201:~/GIT/SD_GENKOU$ jobs
ueda@X201:~/GIT/SD_GENKOU$</pre>
</div>
<p>　余談ですが、普段あまり端末を触らない人はプロセスを殺すことに抵抗があるかもしれませんが、
別にどれだけバッシバッシ殺してもOSは不安定になりませんので、
安心して殺していただいて構いません。躊躇せず屠ってください。</p>
</div>
<div class="section" id="id6">
<h3>9.2.2. シェルスクリプトで使う<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　シェルスクリプトでも&amp;をつけるとバックグラウンドプロセスになります。
例えば、下のように書けば、バックアップを並列で行うことができます。
5行目の <tt class="docutils literal"><span class="pre">&amp;&gt;</span> <span class="pre">/dev/null</span></tt> は標準出力もエラー出力も捨ててしまうと言う意味です。</p>
<p>↓リスト4: 並列にtarを立ち上げるシェルスクリプト</p>
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># こんなスクリプト</span>
<span class="nv">$ </span>cat BACKUP
<span class="c">#!/bin/bash</span>

tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null &amp;
tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null &amp;
<span class="c"># 実行！</span>
<span class="nv">$ </span>./BACKUP
<span class="c"># CPUをちゃんと使っているか見る。</span>
<span class="nv">$ </span>top -n 1 -b | head
<span class="nv">$ </span>cat hoge | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 4
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
 4981 ueda 20 0 8800 652 432 R 79 0.0 0:26.23 gzip
 4982 ueda 20 0 8800 632 428 R 77 0.0 0:27.07 gzip
31938 ueda 20 0 2693m 1.1g 1.1g S 9 19.6 18:57.67 VirtualBox
</pre></div>
</td></tr></table></div>
<p>これも止め方を書いておきます。シェルスクリプトから起動したバックグラウンドプロセスは、
端末からjobsコマンドを叩いても状態を見ることができません。
プロセスIDを指定してkillコマンドで止めるか、
コマンド名を指定してkillallコマンドで止めます。</p>
<p>　リスト5はkillを使う方法で、psを使って確認しながら葬っていきます。
こういうぷちぷち作業が嫌いな人は、
リスト6のようにワンライナーを書いてください。</p>
<p>↓リスト5: killとpsでプロセスを殺す。</p>
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9818 pts/1 00:00:00 tar
 9819 pts/1 00:00:00 tar
 9820 pts/1 00:00:01 gzip
 9821 pts/1 00:00:01 gzip
 9822 pts/1 00:00:00 ps
<span class="nv">$ </span><span class="nb">kill </span>9818
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9819 pts/1 00:00:00 tar
 9821 pts/1 00:00:10 gzip
 9823 pts/1 00:00:00 ps
<span class="nv">$ </span><span class="nb">kill </span>9819
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9824 pts/1 00:00:00 ps
</pre></div>
</td></tr></table></div>
<p>↓リスト6: killとpsとワンライナーでプロセスを殺す。</p>
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9725 pts/1 00:00:00 tar
 9726 pts/1 00:00:00 tar
 9727 pts/1 00:00:01 gzip
 9728 pts/1 00:00:01 gzip
 9729 pts/1 00:00:00 ps
<span class="nv">$ </span>ps | grep tar | awk <span class="s1">&#39;{print $1}&#39;</span> | xargs <span class="nb">kill</span>
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9852 pts/1 00:00:00 ps
</pre></div>
</td></tr></table></div>
<p>　だいたいの場合は、killallを使っても問題ないでしょう。
上のpsを使った方法は慎重な方法で、BACKUPを起動した端末から実行して、
BACKUPが起動したtarだけを捕捉しますが、
リスト7の例では隣の端末のtarも殺しに行きますので注意してください。</p>
<p>↓リスト7: killall</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./BACKUP
<span class="nv">$ </span>killall tar
<span class="nv">$ </span>ps
 PID TTY TIME CMD
 4364 pts/1 00:00:00 bash
 9861 pts/1 00:00:00 ps
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h3>9.2.3. 空ファイルを使って制御する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さてシェルスクリプトBACKUPですが、
tarを二つ立ち上げたらすぐスクリプトが終わってしまいます。
これではいつ終わったか分からないので個人的には不便だと思います。
そこで、二つのtarが終わらないとBACKUPが終わらないように細工をします。</p>
<p>　こういう制御をするときには、
各バックグラウンド処理が終わったときに空ファイルを置き、
それを待つというコードを書きます。リスト8に例を示します。
空ファイルは、セマフォファイルとも言います。</p>
<p>↓リスト8: バックグラウンドプロセスの終了を待つ方法</p>
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
21</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat BACKUP.WAIT
<span class="c">#!/bin/bash</span>

rm -f ./sem.<span class="o">{</span>1,2<span class="o">}</span>

<span class="o">{</span>
 tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null
 touch ./sem.1
<span class="o">}</span> &amp;

<span class="o">{</span>
 tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null
 touch ./sem.2
<span class="o">}</span> &amp;

<span class="k">while </span>sleep 3 ; <span class="k">do</span>
<span class="k"> if</span> <span class="o">[</span> -e ./sem.1 -a -e ./sem.2 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>rm ./sem.<span class="o">{</span>1,2<span class="o">}</span>
 <span class="nb">exit </span>0
 <span class="k">fi</span>
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>このコードでまず大事なのは、コマンドを <tt class="docutils literal"><span class="pre">{</span> <span class="pre">}</span></tt> で囲んでグループ化し、
<tt class="docutils literal"><span class="pre">}</span></tt> の後ろに&amp;をつける書き方です。
こうすると、囲んだ部分がバックグラウンドプロセスで順番に実行されます。
6-9行目、11-14行目はそれぞれ、tarの後、空のファイルを作っています。
空ファイルができるときはその前のtarがすでに終わっていることが保証されるので、
二つの空ファイルがあれば、処理が終わったと判断できるわけです。</p>
<p>　ちなみにtouchコマンドは、ファイルのアクセス時刻と修正時刻を変更するコマンドです。
指定したファイルがないと、空のファイルができます。
もう一つ空のファイルを作る方法に、 <tt class="docutils literal"><span class="pre">:</span> <span class="pre">&gt;</span> <span class="pre">./sem.1</span></tt> という書き方もあります。
「:」は、何もしません。何もしないコマンドの出力をファイルにすると、
空のファイルができます。
また、4行目のrmは、残った <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> で誤動作しないように書いたものです。
オプションなしでrmだけ書くと <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> が無い場合にエラーメッセージが出るので、
fオプションでそれを抑制しています。</p>
<p>　16行目以降は空ファイルを待つコードです。
3秒ごとにファイルの有無を確認して、あったらスクリプトを終了します。
リスト9に、この仕組みの動作を確かめるスクリプトと実行結果を示します。
実行例のように、書いた順序と出力が逆になっており、
非同期で処理が進んでいることが分かります。</p>
<p>↓リスト9: バックグラウンドプロセスを待つ</p>
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
15</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat WAIT
<span class="c">#!/bin/bash</span>

rm -f ./sem.<span class="o">{</span>a,b<span class="o">}</span>

<span class="o">{</span> sleep 1; <span class="nb">echo </span>hogeA; :&gt; ./sem.a; <span class="o">}</span> &amp;
<span class="o">{</span> <span class="nb">echo </span>hogeB; :&gt; ./sem.b; <span class="o">}</span> &amp;

<span class="k">while </span>sleep 3 ; <span class="k">do</span>
 <span class="o">[</span> -e ./sem.a -a -e ./sem.b <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="nb">exit </span>0
<span class="k">done</span>
<span class="nv">$ </span>./WAIT
hogeB &lt;- すぐ出る
hogeA &lt;- 1秒後
<span class="nv">$ </span> &lt;- 3秒後
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h3>9.2.4. もっとスマートに止めるには<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　リスト8のスクリプトは処理の終わりまで待っているわけですが、
Ctrl+cしてもtarが止まりません。あとからkillすればよいのですが、
シェルスクリプトに処理を書くこともできるので紹介します。</p>
<p>　リスト10は、Ctrl+cされたらtarを止め、
残る余計なファイルも消すシェルスクリプトです。</p>
<p>↓リスト10: Ctrl+cしたらtarを止めて掃除</p>
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
31</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat BACKUP.TRAP
<span class="c">#!/bin/bash -xv</span>

EXIT<span class="o">(){</span>
 ps | grep tar | self 1 | xargs <span class="nb">kill</span>
<span class="nb"> </span>rm -f ./<span class="o">{</span>vm,old<span class="o">}</span>.tar.gz
 <span class="k">while</span> ! rm ./sem.1 ; <span class="k">do </span>sleep 1 ; <span class="k">done</span>
<span class="k"> while</span> ! rm ./sem.2 ; <span class="k">do </span>sleep 1 ; <span class="k">done</span>
<span class="k"> </span><span class="nb">exit </span>1
<span class="o">}</span>

<span class="nb">trap </span>EXIT 2

rm -f ./sem.<span class="o">{</span>1,2<span class="o">}</span>

<span class="o">{</span>
 tar zcvf vm.tar.gz ~/VM/ &amp;&gt; /dev/null
 touch ./sem.1
<span class="o">}</span> &amp;

<span class="o">{</span>
 tar zcvf old.tar.gz ~/OLD/ &amp;&gt; /dev/null
 touch ./sem.2
<span class="o">}</span> &amp;

<span class="k">while </span>sleep 3 ; <span class="k">do</span>
<span class="k"> if</span> <span class="o">[</span> -e ./sem.1 -a -e ./sem.2 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>rm ./sem.<span class="o">{</span>1,2<span class="o">}</span>
 <span class="nb">exit </span>0
 <span class="k">fi</span>
<span class="k">done</span>
</pre></div>
</td></tr></table></div>
<p>　スクリプトの冒頭で <tt class="docutils literal"><span class="pre">trap</span> <span class="pre">コマンドor関数</span> <span class="pre">2</span></tt> と書くと、
Ctrl+cが押されたときに、指定したコマンドあるいは関数を実行できるように仕掛けることができます。
この例では、EXITという関数を呼び出すようにしてあります。
2というのはシグナルの番号です。シグナルというのは、
プログラムが走っている最中に何か起こった場合にそのプログラムに通知する仕組みです。
ちなみに2番はSIGINTというシグナルで、
「割り込みが起こった」ということを意味します。
つまり、我々がCtrl+cを連打するのは「ちょっと待った！！待て！待て！・・・」
という意味です。OS側は「待った!」の声を聞くと、
当該処理を止めてメモリをきれいに掃除してくれます。</p>
<p>　EXIT関数の中身ですが、最低限必要なのは5行目のtarを止める処理です。
6行目でtar.gzファイルを消して、7, 8行目で <tt class="docutils literal"><span class="pre">sem.1,</span> <span class="pre">sem.2</span></tt> を消しています。
17行目、22行目のtarがkillされるとそれぞれ18行目、23行目のtouchが実行されるので、
それを待ち受けてファイルを消します。
EXIT関数の中身と18, 23行目のtouchは非同期に起こるので、whileで待たないと素通りすることがあります。
<tt class="docutils literal"><span class="pre">while</span> <span class="pre">!</span> <span class="pre">rm</span> <span class="pre">./sem.1</span> <span class="pre">;</span> <span class="pre">do</span> <span class="pre">...</span> <span class="pre">;</span> <span class="pre">done</span></tt> でrmが成功するまでループします。</p>
<p>　実行結果をリスト11に示します。lsすると分かるように、
Ctrl+c後には余計なファイルが残りません。</p>
<p>↓リスト11: trapでゴミファイルを残さない</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ls
BACKUP BACKUP.TRAP BACKUP.WAIT WAIT
<span class="nv">$ </span>./BACKUP.TRAP
^C &lt;- 割り込み！
./BACKUP.TRAP: 18 行: 12065 Terminated tar zcvf vm.tar.gz ~/VM/ &amp;&gt;/dev/null
./BACKUP.TRAP: 23 行: 12067 Terminated tar zcvf old.tar.gz ~/OLD/ &amp;&gt;/dev/null
<span class="nv">$ </span>ls
BACKUP BACKUP.TRAP BACKUP.WAIT WAIT
</pre></div>
</td></tr></table></div>
</div>
</div>
<div class="section" id="id9">
<h2>9.3. 終わりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、バックグラウンドプロセスを使って処理を並列化するシェルスクリプトを扱いました。
今回はif文、while文、trap、sleep、killなど、面倒なものを使いまくりで大変でした。
結局、同じ処理をn個立ち上げると、入力と出力の口が2n個になってしまうので、
なかなか思うようにコントロールするのは大変です。
やっぱりパイプは簡単だと納得し、今回の終わりとしたいと思います。</p>
<p>　次回は、メールのバッチ処理を扱います。</p>
<div class="section" id="id10">
<h3>9.3.1. 終わりの終わりに・・・<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回の並列化は、ソートの際に非常に有効です。ソートというのは、
データの量が2倍になると計算量が3倍になったり4倍になったりする性質があります。
そのため、ファイルを最初に均等分割してソートをかけて、
あとからマージすると、単に負荷分散した以上の効果を得ることができます。</p>
<p>　ではなぜソートを扱わなかったか・・・。
私のノートPCのsortコマンドが並列化していたからです。
次のtopが証拠です。このノートPCのCPUは2コアx2スレッドで、
CPUの使用率が400%近くなっています。
もちろん、こんなことをしてくれるなら、
何も考えずにコマンドの方に任せるべきです。</p>
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
14</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>sort TESTDATA &amp;
<span class="o">[</span>1<span class="o">]</span> 4368
<span class="nv">$ </span>top -n 1 -b | sed -n <span class="s1">&#39;/PID/,$p&#39;</span> | head -n 3
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
 4368 ueda 20 0 2139m 1.1g 916 R 396 19.4 0:37.92 sort
 3956 ueda 20 0 535m 19m 11m S 2 0.3 0:00.95 gnome-terminal
<span class="nv">$ </span>sort --version
sort <span class="o">(</span>GNU coreutils<span class="o">)</span> 8.13
Copyright <span class="o">(</span>C<span class="o">)</span> 2011 Free Software Foundation, Inc.
ライセンス GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

作者 Mike Haertel および Paul Eggert。
</pre></div>
</td></tr></table></div>
<p>楽な時代になりましたね・・・。私の当初の原稿案はボツになりましたが・・・。</p>
</div>
</div>
</div>


