---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年6月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>18. 開眼シェルスクリプト 第18回サーバを股にかける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　皆様、いい季節いかがお過ごしでしょうか。
この原稿を書いているのが3月頭ですので、筆者は現在、
杉からの花粉ハラスメントを受けている最中です。</p>
<p>　そんな時差を利用した小話はいいとして、
今回のテーマは「サーバを股にかける」です。
時をかける少女じゃなくて、
サーバをかけるオッサンになろうということで、
いろいろネタを準備しました。</p>
<p>　字しか書けない端末のよいところは、一つの端末に字を書くだけで
あっちこっちのコンピュータを気軽に使う事ができることです。
vncやリモートデスクトップではそうはいかず、
あっちこっちの画面を覗いているうちに疲れてきます。
データを移すのにも一苦労です。
やりたいことに対して情報量が多いことは、
決してよいことではありません。</p>
<p>　そういえば、ガンカーズのUNIX哲学には、
主要な9か条の他に、二軍の10か条がありますが、
その中に、</p>
<p>「90パーセントの解決を模索せよ。」</p>
<p>というのがあります。
プログラムを書いたり、仕事をしたりすると、
本筋でない雑事が気になるものですが、
それにはある程度目をつぶれということを言っています。</p>
<p>　これは、時短の発想であるとも解釈できます。
私の仕事の場合は、端末とウェブブラウザがあれば、
仕事の90%は片付いてしまいます。
そのうちの端末を使う数十%の仕事は字だけ見てさっさと終わってしまうので、
メニューをマウスでクリクリしている人よりは、
例え残りの10%で困ったとしても、
トータルでも時間を得しているはずです。</p>
<p>　ちなみに残りの10%のうち、9%がお絵描きで、あと1%が得体の知れない何かで、
これはさすがに端末ではやりません。合った道具を使います。</p>
<p>　これはもう、余談も余談ですが、世の中には10%が気になりすぎて、
脳みそに刷り込まれて、その10%のことを「最重要事項」だ、
と思い込んでバランスの悪い主張をする人々がいます。
また、それに反論ばかりしているうちに脳みそに刷り込まれ、
やはりそれが「最重要事項」になってしまう犠牲者も出現します。</p>
<p>　90%ルールは、その負のループから我々を救ってくださるのです。
あなかしこあなかしこ。</p>
<div class="section" id="id2">
<h2>18.1. 環境等<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="id3">
<h3>18.1.1. 使用する環境<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は多種多様です。リスト1で、簡単に説明します。
なるべく皆様を混乱させないように注意しながら話を進めます。</p>
<ul class="simple">
<li>リスト1: 登場するマシン・サーバ</li>
</ul>
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
18</pre></div></td><td class="code"><div class="highlight"><pre>//1. 筆者のMacBook Air（uedamac）
uedamac:~ ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: （略）
uedamac:~ ueda<span class="nv">$ </span>bash --version
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span>
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.

//2. VPS上のFreeBSD（bsd）
bsd /home/ueda<span class="nv">$ </span>uname -a
FreeBSD bsd.hoge.hoge 9.0-RELEASE FreeBSD 9.0-RELEASE <span class="c">#0: (略)</span>

//3. VPS上のUSP友の会サーバ（tomonokai）
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release
CentOS release 6.3 <span class="o">(</span>Final<span class="o">)</span>

//4. ビジネス版Tukubaiが使えるサーバ（usp）
<span class="o">[</span>ueda@usp ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release
CentOS release 5.9 <span class="o">(</span>Final<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>友の会のサーバは、 <tt class="docutils literal"><span class="pre">www.usptomo.com</span></tt> というホスト名でDNSに登録されています。
<tt class="docutils literal"><span class="pre">bsd</span></tt> は秘密のサーバですが、
<tt class="docutils literal"><span class="pre">bsd.hoge.hoge</span></tt> で登録されているとしておきます。</p>
</div>
<div class="section" id="id4">
<h3>18.1.2. 鍵認証の設定についてちょっと<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　シェルスクリプトという範囲の話ではありませんが、
今回は <tt class="docutils literal"><span class="pre">scp</span></tt> コマンドや <tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドを多用しますので、
ssh接続の鍵認証の方法について触れておきます。
（脚注：パスワードを入れなくてもログインできるアレのことです。念のため。）
いや、手順については「ssh 鍵認証」
などと検索すれば方法が書いてあるのでここでは説明しません。
が、鍵認証はクライアントとサーバ、公開鍵と秘密鍵が登場して、
どっちで何をするのか慣れるまで非常に混乱するので、
そんな人のために、次の一文を書いておきます。</p>
<p>「ssh接続される方（サーバ）は危険に晒されるので、
接続してくる奴をリスト化して管理しなければならない。」</p>
<p>このリストに登録されるのは、「接続してくる奴」の公開鍵です。</p>
<p>　ですから、クライアント側では秘密鍵と公開鍵を準備し、
公開鍵をサーバに登録してもらうという手続きを行うことになります。</p>
<p>　これを頭に入れて、設定をお願い致します。</p>
</div>
</div>
<div class="section" id="id5">
<h2>18.2. 通信あれこれ<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="bash-dev-tcp">
<h3>18.2.1. bashの <tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt><a class="headerlink" href="#bash-dev-tcp" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて本題に入っていきましょう。まずは bash の機能を使ってみます。
どのバージョンからかは調べていませんが、少なくとも3以降のbashには、
リスト2の方法で、
特定のホストの特定のポートに <tt class="docutils literal"><span class="pre">file</span></tt> の内容を送信する機能があります。
リダイレクトの左側は、 <tt class="docutils literal"><span class="pre">echo</span></tt> でも <tt class="docutils literal"><span class="pre">grep</span></tt> でもなんでもかまいません。</p>
<ul class="simple">
<li>リスト2: bashで通信するときの書式</li>
</ul>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat file &gt; /dev/tcp/&lt;ホスト名&gt;/&lt;ポート番号&gt;
</pre></div>
</div>
<p>　早速使ってみましょう。と言ってもこの機能単独だと、
いたずら程度くらいしか思いつきませんので、
リスト3のようにUSP友の会のサーバを餌食にしてみました。
皆さんもなにかメッセージを残してもらって構いませんが、
あまり連発しないでください。</p>
<ul class="simple">
<li>リスト3: apacheにいたずらする</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#macからUSP友の会のサーバにちょっかいを出す</span>
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo </span>aho &gt; /dev/tcp/www.usptomo.com/80
<span class="c">#USP友の会のサーバのログに記録が残る</span>
<span class="o">[</span>root@tomonokai ~<span class="o">]</span><span class="c"># tail -n 1 /var/log/httpd/access_log</span>
123.234.aa.bb - - <span class="o">[</span>03/Mar/2013:00:58:21 +0900<span class="o">]</span> <span class="s2">&quot;aho&quot;</span> 301 231 <span class="s2">&quot;-&quot;</span> <span class="s2">&quot;-&quot;</span>
</pre></div>
</td></tr></table></div>
<dl class="docutils">
<dt>　リスト4のように調べると分かるように、</dt>
<dd><tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt> はシステム側にあるわけではなく、</dd>
</dl>
<p>bashが擬似的にファイルに見せかけているようです。</p>
<ul class="simple">
<li>リスト4: <tt class="docutils literal"><span class="pre">/dev/tcp</span></tt> は存在しない</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ls /dev/tcp
ls: /dev/tcp: No such file or directory
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">/dev/udp/</span></tt> も準備されていますので、
UDPを使うサービスにもちょっかいが出せます。</p>
</div>
<div class="section" id="netcat">
<h3>18.2.2. netcatを使う<a class="headerlink" href="#netcat" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　bash の <tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt> を使うと、基本、
データをポートに投げつけることしかできません。
投げつけたデータの受け手として、
Netcat を紹介します。</p>
<p>　大抵の環境には、 <tt class="docutils literal"><span class="pre">nc</span></tt> というコマンドで Netcat が使えます。
bashからテキストを投げて、 <tt class="docutils literal"><span class="pre">nc</span></tt> で受けてみましょう。
もちろん文字は暗号化されずにそのまま送られるので、
秘密のものは送らないようにしましょう。
この実験をするには、受信側で使うポートが開いている必要があります。</p>
<ul class="simple">
<li>リスト5: 10000番ポートで通信する</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>//先に nc で受信側のポートを開いておく
//ncが立ち上がったままになる
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; hoge

//データを投げる
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> ひえええええ &gt; /dev/tcp/www.usptomo.com/10000
//ncが終わって、hogeの中に文字列が
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat hoge
ひえええええ
</pre></div>
</td></tr></table></div>
<p>　リスト6のようにシェルスクリプトにして実行すると、
ちょっとしたサービスのように振る舞います。</p>
<ul class="simple">
<li>リスト6: whileループで何回も受信</li>
</ul>
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
28</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat file.sh
<span class="c">#!/bin/bash</span>

mkdir -p ./tmp/

<span class="nv">n</span><span class="o">=</span>1
<span class="k">while </span>nc -l 10000 &gt; ./tmp/<span class="nv">$n</span>.txt ; <span class="k">do</span>
<span class="k"> </span><span class="nv">n</span><span class="o">=</span><span class="k">$((</span> n <span class="o">+</span> <span class="m">1</span> <span class="k">))</span>
<span class="k">done</span>

//立ち上げる
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>./file.sh
//送る
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> ひえええええ &gt; /dev/tcp/www.usptomo.com/10000
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> どひぇー &gt; /dev/tcp/www.usptomo.com/10000
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo </span>NOOO! &gt; /dev/tcp/www.usptomo.com/10000
//Ctrl+cしてファイルができていることを確認
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>./file.sh
^C
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>head ./tmp/<span class="o">{</span>1,2,3<span class="o">}</span>.txt
<span class="o">==</span>&gt; ./tmp/1.txt &lt;<span class="o">==</span>
ひえええええ

<span class="o">==</span>&gt; ./tmp/2.txt &lt;<span class="o">==</span>
どひぇー

<span class="o">==</span>&gt; ./tmp/3.txt &lt;<span class="o">==</span>
NOOO!
</pre></div>
</td></tr></table></div>
<p>　Netcat は Wikipedia に
「ネットワークを扱う万能ツールとして知られる。」
とあるように、単にポートをリッスンするだけでなく、
データの送信側になったり、
邪悪な組織のポートスキャナになったりします。</p>
</div>
</div>
<div class="section" id="id6">
<h2>18.3. ファイルを転送する<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、いつも大きなデータを扱っている人は、
サーバ間で何十GBものファイルをコピーしなければいけないことがあります。
このようなときはリスト7のように、普通は <tt class="docutils literal"><span class="pre">scp</span></tt> を使うことでしょう。
リスト中の <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">11111</span></tt> は、USP友の会のサーバが
でフォルトの <tt class="docutils literal"><span class="pre">22</span></tt> 番でなく <tt class="docutils literal"><span class="pre">11111</span></tt> 番でssh接続を受け付けているため、
必要となります（脚注: 実際には別のポートを使っています）。</p>
<ul class="simple">
<li>リスト7: 普通に <tt class="docutils literal"><span class="pre">scp</span></tt> でファイルをコピー</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>scp -P 11111 TESTDATA www.usptomo.com:~/
TESTDATA 100% 4047MB 4.0MB/s 16:48

real 16m49.064s
user 3m2.550s
sys 13m38.727s
</pre></div>
</td></tr></table></div>
<p>　実は、 <tt class="docutils literal"><span class="pre">scp</span></tt> には圧縮してデータを送る <tt class="docutils literal"><span class="pre">-C</span></tt>
というオプションがあります。リスト8のように使います。
ただ、圧縮はCPUを酷使するので効果のある場合は限られます。
1回しか試していないのでかかった時間は参考程度にしかなりませんが、
user時間で圧縮にかなり時間を使っていることが分かります。</p>
<ul class="simple">
<li>リスト8: 圧縮送信したらかえって遅くなった</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>scp -C -P 11111 TESTDATA www.usptomo.com:~/
TESTDATA 100% 4047MB 2.6MB/s 26:16

real 26m16.678s
user 20m33.275s
sys 6m55.593s
</pre></div>
</td></tr></table></div>
<p>　実は、暗号化しなくてよいならリスト9のように転送する方が速いことがあります。
user時間はほとんどゼロです。</p>
<ul class="simple">
<li>リスト9: ポートをダイレクトに使ってファイル転送</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>//受信側で待ち受け
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; TESTDATA
//送信
bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA &gt; /dev/tcp/www.usptomo.com/10000

real 12m3.584s
user 0m0.000s
sys 10m22.737s
</pre></div>
</td></tr></table></div>
<p>　CPUが速くて通信速度が遅いときは、
<tt class="docutils literal"><span class="pre">scp</span></tt> の <tt class="docutils literal"><span class="pre">-C</span></tt> オプションが有効になりますが、
上の <tt class="docutils literal"><span class="pre">nc</span></tt> の方法で <tt class="docutils literal"><span class="pre">gzip</span></tt> や <tt class="docutils literal"><span class="pre">bzip2</span></tt> などを挟んで送った方が、
速いこともあります。速いこともある、というより、
本来圧縮は <tt class="docutils literal"><span class="pre">scp</span></tt> の仕事ではないはずですし、
圧縮の方式も自由に選べるべきなので、
面倒ですがこっちの方がUNIX的です。
ただまあ、そういうチューニングは本当に困ったときだけにしておきましょう。</p>
<p>　一つの巨大なファイルを複数のサーバにコピーしたい場合は、
リスト10のようなことを試みてもよいでしょう。
頭がこんがらがるかもしれませんが、
ちゃんと書けばちゃんと動きます。</p>
<ul class="simple">
<li>リスト10: 一度の転送で二つのサーバにファイルをコピー</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>//友の会サーバで10000番ポートからファイルへリダイレクト
<span class="o">[</span>ueda@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; TESTDATA
//bsdサーバで9999番ポートからの出力をteeでファイルにためながら
//友の会サーバにリダイレクト
bsd /home/ueda<span class="nv">$ </span>nc -l 9999 | tee TESTDATA &gt; /dev/tcp/www.usptomo.com/10000
//手元のMacからbsdサーバにデータを投げる
uedamac:~ ueda<span class="nv">$ </span>cat TESTDATA &gt; /dev/tcp/bsd.hoge.hoge/9999
</pre></div>
</td></tr></table></div>
<p>　この方法のようにサーバを数珠つなぎにすると、
何台ものサーバに同時にコピーができます。
ただし、サーバが同じハブにぶらさがっていると、
ハブにトラフィックが集中します。</p>
<p>　あともう一個だけ紹介します。
sshコマンドを使ってもファイルを転送できます。
この例で、sshコマンドが標準入力を受け付けることが分かります。</p>
<ul class="simple">
<li>リスト11: <tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドの標準入力を使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA | ssh -p 11111 www.usptomo.com <span class="s1">&#39;cat &gt; TESTDATA&#39;</span>

real 16m22.054s
user 2m46.163s
sys 12m44.448s
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h2>18.4. リモートマシンで計算する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、もっと便利に使ってみましょう。
このままではコピーだけで今回が終わってしまいます。
（それはそれで面白いかもしれませんが・・・）</p>
<p>　例えば、今使っているマシンが遅い場合や使いたいコマンド等が
インストールされていない状況を考えます。
私の場合は、USP研究所のビジネス用 Tukubai
コマンドを使いたい場合や、
あるマシンのTeXの環境を使いたいという場合がこれに相当します。</p>
<p>　一例として、手元にあるファイルをリモートのサーバで
ソートして戻してもらうことを考えましょう。</p>
<p>　まずリスト12に、普通のシェルスクリプトを示します。
これは、あるリモートのサーバに <tt class="docutils literal"><span class="pre">scp</span></tt> でファイルを送り込み、
ソートした後にファイルを戻すという処理です。
Macの <tt class="docutils literal"><span class="pre">sort</span></tt>
コマンドで1千万行のソートなんかやっちゃったらいつ終わるのか読めないので、
これくらいのことは行う価値はあります。</p>
<ul class="simple">
<li>リスト12: 「べたな」リモートサーバの使い方</li>
</ul>
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
22</pre></div></td><td class="code"><div class="highlight"><pre>//このデータ（1千万行）を左端の数字でソートしたい
uedamac:~ ueda<span class="nv">$ </span>head -n 2 TESTDATA10M
2377 高知県 -9,987,759 2001年1月5日
2910 鹿児島県 5,689,492 1992年5月6日
uedamac:~ ueda<span class="nv">$ </span>cat sort.sh
<span class="c">#!/bin/bash -xv</span>

scp -P 11111 ./TESTDATA10M usp.usp-lab.com:~/
//msortは、マルチスレッドの高速ソートコマンド
ssh -p 11111 usp.usp-lab.com <span class="s2">&quot;msort -p 8 key=1 ~/TESTDATA10M &gt; ~/ueda.tmp&quot;</span>
scp -P 11111 usp.usp-lab.com:~/ueda.tmp ./TESTDATA10M.sort

//手元のMacで実行
uedamac:~ ueda<span class="nv">$ </span><span class="nb">time</span> ./sort.sh

real 4m1.717s
user 0m13.969s
sys 0m10.090s
//結果が得られた
uedamac:~ ueda<span class="nv">$ </span>head -n 2 TESTDATA10M.sort
0000 岩手県 5,630,892 2006年5月26日
0000 新潟県 1,367,399 1998年8月22日
</pre></div>
</td></tr></table></div>
<p>　こういった通信ばっかりのシェルスクリプトを書いた人は
そんなにいないと思いますが、
シェルスクリプトなど所詮、人の操作のメモ書きですので、
いつも <tt class="docutils literal"><span class="pre">scp,</span> <span class="pre">ssh</span></tt> を使っていれば理解できるでしょう。</p>
<p>　ところでこのシェルスクリプトでは、
中間ファイルがリモートのサーバにできてしまっていますが、
これを避けるにはどうすればよいでしょうか。
こういう中間ファイルは、計算を <tt class="docutils literal"><span class="pre">Ctrl+c</span></tt>
などで中断した場合にリモートのサーバにゴミを残すことになります。
処理によっては、次に計算したときに悪さをすることもあります。</p>
<p>　これを解決するには「シェル芸」です。
「開眼シェルスクリプト」という名前で連載をしていますが、</p>
<p><em>不要なシェルスクリプトと中間ファイルはゴミ</em></p>
<p>です。こんなもん、ワンライナーで十分です。
リスト13に示します。</p>
<ul class="simple">
<li>リスト13: リモートサーバを使うワンライナー</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA10M | ssh -p 10022 usp.usp-lab.com <span class="s1">&#39;cat | msort -p 8 key=1&#39;</span> &gt; TESTDATA10M.sort3

real 5m0.033s
user 0m14.077s
sys 0m9.415s
</pre></div>
</td></tr></table></div>
<p>これで、sshでソートした出力は、（太字）手元のMacの標準出力から出てきます。
<tt class="docutils literal"><span class="pre">ssh</span></tt> が（リモートでなく）
手元のマシンの標準入出力に字を出し入れしてくれることは、
<tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドが手元のマシンで動いているので当然と言えば当然ですが、
よくよく考えるととても便利なことです。
ワンライナーとしては難解かもしれませんが、
リモートとローカルがシームレスにつながっています。
パイプラインなので、ストレージを使う事もありません。</p>
<p>　ちょっとやりすぎですが、
筆者の自宅とサーバの間の通信速度がそんなに速くないので、
<tt class="docutils literal"><span class="pre">gzip,</span> <span class="pre">gunzip</span></tt> を使ってリスト14のようにチューンしたらさらに時短できました。</p>
<ul class="simple">
<li>リスト14: 圧縮を挟み込んだワンライナー</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">time </span>gzip &lt; TESTDATA10M | ssh -p 10022 usp.usp-lab.com <span class="s1">&#39;gunzip | msort -p 8 key=1 | gzip&#39;</span> | gunzip &gt; TESTDATA10M.sort3

real 1m10.669s
user 0m42.874s
sys 0m2.806s
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h2>18.5. 終わりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回も前回に引き続き作り物をさぼって、
サーバを股にかけてデータをやりとりし、処理する方法について書きました。
bashの通信機能や、 <tt class="docutils literal"><span class="pre">ssh,</span> <span class="pre">scp,</span> <span class="pre">nc</span></tt>
などのコマンドについてちょっとした使い方を紹介しました。</p>
<p>　マシンを複数台使うと頭の中が混乱しがちです。
その点、 <tt class="docutils literal"><span class="pre">ssh</span></tt> をパイプにつなぐことを覚えると、
あまり頭を悩ませずに複数のマシンを使いこなすことができます。
パイプラインは一方通行で順番にサーバをつなげていくだけなので、
頭の中でいろんなマシンの絵を同時に思い浮かべる負荷が不要です。
マシン間の通信速度はまだ向上していくでしょうから、
これからは使う人が増えるかもしれません。</p>
<p>　次回からは、とうとう禁断のお題をやる覚悟ができました。
「シェルスクリプトでCGI」というお題で作り物をしてみます。</p>
</div>
</div>


