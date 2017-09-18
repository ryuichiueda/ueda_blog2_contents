---
Copyright: (C) Ryuichi Ueda
---

# 開眼シェルスクリプト2013年6月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>18. 開眼シェルスクリプト 第18回サーバを股にかける<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　皆様、いい季節いかがお過ごしでしょうか。<br />
この原稿を書いているのが3月頭ですので、筆者は現在、<br />
杉からの花粉ハラスメントを受けている最中です。</p><br />
<p>　そんな時差を利用した小話はいいとして、<br />
今回のテーマは「サーバを股にかける」です。<br />
時をかける少女じゃなくて、<br />
サーバをかけるオッサンになろうということで、<br />
いろいろネタを準備しました。</p><br />
<p>　字しか書けない端末のよいところは、一つの端末に字を書くだけで<br />
あっちこっちのコンピュータを気軽に使う事ができることです。<br />
vncやリモートデスクトップではそうはいかず、<br />
あっちこっちの画面を覗いているうちに疲れてきます。<br />
データを移すのにも一苦労です。<br />
やりたいことに対して情報量が多いことは、<br />
決してよいことではありません。</p><br />
<p>　そういえば、ガンカーズのUNIX哲学には、<br />
主要な9か条の他に、二軍の10か条がありますが、<br />
その中に、</p><br />
<p>「90パーセントの解決を模索せよ。」</p><br />
<p>というのがあります。<br />
プログラムを書いたり、仕事をしたりすると、<br />
本筋でない雑事が気になるものですが、<br />
それにはある程度目をつぶれということを言っています。</p><br />
<p>　これは、時短の発想であるとも解釈できます。<br />
私の仕事の場合は、端末とウェブブラウザがあれば、<br />
仕事の90%は片付いてしまいます。<br />
そのうちの端末を使う数十%の仕事は字だけ見てさっさと終わってしまうので、<br />
メニューをマウスでクリクリしている人よりは、<br />
例え残りの10%で困ったとしても、<br />
トータルでも時間を得しているはずです。</p><br />
<p>　ちなみに残りの10%のうち、9%がお絵描きで、あと1%が得体の知れない何かで、<br />
これはさすがに端末ではやりません。合った道具を使います。</p><br />
<p>　これはもう、余談も余談ですが、世の中には10%が気になりすぎて、<br />
脳みそに刷り込まれて、その10%のことを「最重要事項」だ、<br />
と思い込んでバランスの悪い主張をする人々がいます。<br />
また、それに反論ばかりしているうちに脳みそに刷り込まれ、<br />
やはりそれが「最重要事項」になってしまう犠牲者も出現します。</p><br />
<p>　90%ルールは、その負のループから我々を救ってくださるのです。<br />
あなかしこあなかしこ。</p><br />
<div class="section" id="id2"><br />
<h2>18.1. 環境等<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="id3"><br />
<h3>18.1.1. 使用する環境<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は多種多様です。リスト1で、簡単に説明します。<br />
なるべく皆様を混乱させないように注意しながら話を進めます。</p><br />
<ul class="simple"><br />
<li>リスト1: 登場するマシン・サーバ</li><br />
</ul><br />
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
18</pre></div></td><td class="code"><div class="highlight"><pre>//1. 筆者のMacBook Air（uedamac）<br />
uedamac:~ ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1: （略）<br />
uedamac:~ ueda<span class="nv">$ </span>bash --version<br />
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span><br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.<br />
<br />
//2. VPS上のFreeBSD（bsd）<br />
bsd /home/ueda<span class="nv">$ </span>uname -a<br />
FreeBSD bsd.hoge.hoge 9.0-RELEASE FreeBSD 9.0-RELEASE <span class="c">#0: (略)</span><br />
<br />
//3. VPS上のUSP友の会サーバ（tomonokai）<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release<br />
CentOS release 6.3 <span class="o">(</span>Final<span class="o">)</span><br />
<br />
//4. ビジネス版Tukubaiが使えるサーバ（usp）<br />
<span class="o">[</span>ueda\@usp ~<span class="o">]</span><span class="nv">$ </span>cat /etc/redhat-release<br />
CentOS release 5.9 <span class="o">(</span>Final<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>友の会のサーバは、 <tt class="docutils literal"><span class="pre">www.usptomo.com</span></tt> というホスト名でDNSに登録されています。<br />
<tt class="docutils literal"><span class="pre">bsd</span></tt> は秘密のサーバですが、<br />
<tt class="docutils literal"><span class="pre">bsd.hoge.hoge</span></tt> で登録されているとしておきます。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>18.1.2. 鍵認証の設定についてちょっと<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　シェルスクリプトという範囲の話ではありませんが、<br />
今回は <tt class="docutils literal"><span class="pre">scp</span></tt> コマンドや <tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドを多用しますので、<br />
ssh接続の鍵認証の方法について触れておきます。<br />
（脚注：パスワードを入れなくてもログインできるアレのことです。念のため。）<br />
いや、手順については「ssh 鍵認証」<br />
などと検索すれば方法が書いてあるのでここでは説明しません。<br />
が、鍵認証はクライアントとサーバ、公開鍵と秘密鍵が登場して、<br />
どっちで何をするのか慣れるまで非常に混乱するので、<br />
そんな人のために、次の一文を書いておきます。</p><br />
<p>「ssh接続される方（サーバ）は危険に晒されるので、<br />
接続してくる奴をリスト化して管理しなければならない。」</p><br />
<p>このリストに登録されるのは、「接続してくる奴」の公開鍵です。</p><br />
<p>　ですから、クライアント側では秘密鍵と公開鍵を準備し、<br />
公開鍵をサーバに登録してもらうという手続きを行うことになります。</p><br />
<p>　これを頭に入れて、設定をお願い致します。</p><br />
</div><br />
</div><br />
<div class="section" id="id5"><br />
<h2>18.2. 通信あれこれ<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="bash-dev-tcp"><br />
<h3>18.2.1. bashの <tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt><a class="headerlink" href="#bash-dev-tcp" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて本題に入っていきましょう。まずは bash の機能を使ってみます。<br />
どのバージョンからかは調べていませんが、少なくとも3以降のbashには、<br />
リスト2の方法で、<br />
特定のホストの特定のポートに <tt class="docutils literal"><span class="pre">file</span></tt> の内容を送信する機能があります。<br />
リダイレクトの左側は、 <tt class="docutils literal"><span class="pre">echo</span></tt> でも <tt class="docutils literal"><span class="pre">grep</span></tt> でもなんでもかまいません。</p><br />
<ul class="simple"><br />
<li>リスト2: bashで通信するときの書式</li><br />
</ul><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>cat file &gt; /dev/tcp/&lt;ホスト名&gt;/&lt;ポート番号&gt;<br />
</pre></div><br />
</div><br />
<p>　早速使ってみましょう。と言ってもこの機能単独だと、<br />
いたずら程度くらいしか思いつきませんので、<br />
リスト3のようにUSP友の会のサーバを餌食にしてみました。<br />
皆さんもなにかメッセージを残してもらって構いませんが、<br />
あまり連発しないでください。</p><br />
<ul class="simple"><br />
<li>リスト3: apacheにいたずらする</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#macからUSP友の会のサーバにちょっかいを出す</span><br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo </span>aho &gt; /dev/tcp/www.usptomo.com/80<br />
<span class="c">#USP友の会のサーバのログに記録が残る</span><br />
<span class="o">[</span>root\@tomonokai ~<span class="o">]</span><span class="c"># tail -n 1 /var/log/httpd/access_log</span><br />
123.234.aa.bb - - <span class="o">[</span>03/Mar/2013:00:58:21 +0900<span class="o">]</span> <span class="s2">&quot;aho&quot;</span> 301 231 <span class="s2">&quot;-&quot;</span> <span class="s2">&quot;-&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<dl class="docutils"><br />
<dt>　リスト4のように調べると分かるように、</dt><br />
<dd><tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt> はシステム側にあるわけではなく、</dd><br />
</dl><br />
<p>bashが擬似的にファイルに見せかけているようです。</p><br />
<ul class="simple"><br />
<li>リスト4: <tt class="docutils literal"><span class="pre">/dev/tcp</span></tt> は存在しない</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ls /dev/tcp<br />
ls: /dev/tcp: No such file or directory<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">/dev/udp/</span></tt> も準備されていますので、<br />
UDPを使うサービスにもちょっかいが出せます。</p><br />
</div><br />
<div class="section" id="netcat"><br />
<h3>18.2.2. netcatを使う<a class="headerlink" href="#netcat" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　bash の <tt class="docutils literal"><span class="pre">/dev/tcp/</span></tt> を使うと、基本、<br />
データをポートに投げつけることしかできません。<br />
投げつけたデータの受け手として、<br />
Netcat を紹介します。</p><br />
<p>　大抵の環境には、 <tt class="docutils literal"><span class="pre">nc</span></tt> というコマンドで Netcat が使えます。<br />
bashからテキストを投げて、 <tt class="docutils literal"><span class="pre">nc</span></tt> で受けてみましょう。<br />
もちろん文字は暗号化されずにそのまま送られるので、<br />
秘密のものは送らないようにしましょう。<br />
この実験をするには、受信側で使うポートが開いている必要があります。</p><br />
<ul class="simple"><br />
<li>リスト5: 10000番ポートで通信する</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>//先に nc で受信側のポートを開いておく<br />
//ncが立ち上がったままになる<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; hoge<br />
<br />
//データを投げる<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> ひえええええ &gt; /dev/tcp/www.usptomo.com/10000<br />
//ncが終わって、hogeの中に文字列が<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat hoge<br />
ひえええええ<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト6のようにシェルスクリプトにして実行すると、<br />
ちょっとしたサービスのように振る舞います。</p><br />
<ul class="simple"><br />
<li>リスト6: whileループで何回も受信</li><br />
</ul><br />
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
28</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>cat file.sh<br />
<span class="c">#!/bin/bash</span><br />
<br />
mkdir -p ./tmp/<br />
<br />
<span class="nv">n</span><span class="o">=</span>1<br />
<span class="k">while </span>nc -l 10000 &gt; ./tmp/<span class="nv">$n</span>.txt ; <span class="k">do</span><br />
<span class="k"> </span><span class="nv">n</span><span class="o">=</span><span class="k">$((</span> n <span class="o">+</span> <span class="m">1</span> <span class="k">))</span><br />
<span class="k">done</span><br />
<br />
//立ち上げる<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>./file.sh<br />
//送る<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> ひえええええ &gt; /dev/tcp/www.usptomo.com/10000<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo</span> どひぇー &gt; /dev/tcp/www.usptomo.com/10000<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">echo </span>NOOO! &gt; /dev/tcp/www.usptomo.com/10000<br />
//Ctrl+cしてファイルができていることを確認<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>./file.sh<br />
^C<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>head ./tmp/<span class="o">{</span>1,2,3<span class="o">}</span>.txt<br />
<span class="o">==</span>&gt; ./tmp/1.txt &lt;<span class="o">==</span><br />
ひえええええ<br />
<br />
<span class="o">==</span>&gt; ./tmp/2.txt &lt;<span class="o">==</span><br />
どひぇー<br />
<br />
<span class="o">==</span>&gt; ./tmp/3.txt &lt;<span class="o">==</span><br />
NOOO!<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　Netcat は Wikipedia に<br />
「ネットワークを扱う万能ツールとして知られる。」<br />
とあるように、単にポートをリッスンするだけでなく、<br />
データの送信側になったり、<br />
邪悪な組織のポートスキャナになったりします。</p><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>18.3. ファイルを転送する<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、いつも大きなデータを扱っている人は、<br />
サーバ間で何十GBものファイルをコピーしなければいけないことがあります。<br />
このようなときはリスト7のように、普通は <tt class="docutils literal"><span class="pre">scp</span></tt> を使うことでしょう。<br />
リスト中の <tt class="docutils literal"><span class="pre">-P</span> <span class="pre">11111</span></tt> は、USP友の会のサーバが<br />
でフォルトの <tt class="docutils literal"><span class="pre">22</span></tt> 番でなく <tt class="docutils literal"><span class="pre">11111</span></tt> 番でssh接続を受け付けているため、<br />
必要となります（脚注: 実際には別のポートを使っています）。</p><br />
<ul class="simple"><br />
<li>リスト7: 普通に <tt class="docutils literal"><span class="pre">scp</span></tt> でファイルをコピー</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>scp -P 11111 TESTDATA www.usptomo.com:~/<br />
TESTDATA 100% 4047MB 4.0MB/s 16:48<br />
<br />
real 16m49.064s<br />
user 3m2.550s<br />
sys 13m38.727s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　実は、 <tt class="docutils literal"><span class="pre">scp</span></tt> には圧縮してデータを送る <tt class="docutils literal"><span class="pre">-C</span></tt><br />
というオプションがあります。リスト8のように使います。<br />
ただ、圧縮はCPUを酷使するので効果のある場合は限られます。<br />
1回しか試していないのでかかった時間は参考程度にしかなりませんが、<br />
user時間で圧縮にかなり時間を使っていることが分かります。</p><br />
<ul class="simple"><br />
<li>リスト8: 圧縮送信したらかえって遅くなった</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>scp -C -P 11111 TESTDATA www.usptomo.com:~/<br />
TESTDATA 100% 4047MB 2.6MB/s 26:16<br />
<br />
real 26m16.678s<br />
user 20m33.275s<br />
sys 6m55.593s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　実は、暗号化しなくてよいならリスト9のように転送する方が速いことがあります。<br />
user時間はほとんどゼロです。</p><br />
<ul class="simple"><br />
<li>リスト9: ポートをダイレクトに使ってファイル転送</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>//受信側で待ち受け<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; TESTDATA<br />
//送信<br />
bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA &gt; /dev/tcp/www.usptomo.com/10000<br />
<br />
real 12m3.584s<br />
user 0m0.000s<br />
sys 10m22.737s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　CPUが速くて通信速度が遅いときは、<br />
<tt class="docutils literal"><span class="pre">scp</span></tt> の <tt class="docutils literal"><span class="pre">-C</span></tt> オプションが有効になりますが、<br />
上の <tt class="docutils literal"><span class="pre">nc</span></tt> の方法で <tt class="docutils literal"><span class="pre">gzip</span></tt> や <tt class="docutils literal"><span class="pre">bzip2</span></tt> などを挟んで送った方が、<br />
速いこともあります。速いこともある、というより、<br />
本来圧縮は <tt class="docutils literal"><span class="pre">scp</span></tt> の仕事ではないはずですし、<br />
圧縮の方式も自由に選べるべきなので、<br />
面倒ですがこっちの方がUNIX的です。<br />
ただまあ、そういうチューニングは本当に困ったときだけにしておきましょう。</p><br />
<p>　一つの巨大なファイルを複数のサーバにコピーしたい場合は、<br />
リスト10のようなことを試みてもよいでしょう。<br />
頭がこんがらがるかもしれませんが、<br />
ちゃんと書けばちゃんと動きます。</p><br />
<ul class="simple"><br />
<li>リスト10: 一度の転送で二つのサーバにファイルをコピー</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>//友の会サーバで10000番ポートからファイルへリダイレクト<br />
<span class="o">[</span>ueda\@tomonokai ~<span class="o">]</span><span class="nv">$ </span>nc -l 10000 &gt; TESTDATA<br />
//bsdサーバで9999番ポートからの出力をteeでファイルにためながら<br />
//友の会サーバにリダイレクト<br />
bsd /home/ueda<span class="nv">$ </span>nc -l 9999 | tee TESTDATA &gt; /dev/tcp/www.usptomo.com/10000<br />
//手元のMacからbsdサーバにデータを投げる<br />
uedamac:~ ueda<span class="nv">$ </span>cat TESTDATA &gt; /dev/tcp/bsd.hoge.hoge/9999<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　この方法のようにサーバを数珠つなぎにすると、<br />
何台ものサーバに同時にコピーができます。<br />
ただし、サーバが同じハブにぶらさがっていると、<br />
ハブにトラフィックが集中します。</p><br />
<p>　あともう一個だけ紹介します。<br />
sshコマンドを使ってもファイルを転送できます。<br />
この例で、sshコマンドが標準入力を受け付けることが分かります。</p><br />
<ul class="simple"><br />
<li>リスト11: <tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドの標準入力を使う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>bsd /home/ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA | ssh -p 11111 www.usptomo.com <span class="s1">&#39;cat &gt; TESTDATA&#39;</span><br />
<br />
real 16m22.054s<br />
user 2m46.163s<br />
sys 12m44.448s<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h2>18.4. リモートマシンで計算する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、もっと便利に使ってみましょう。<br />
このままではコピーだけで今回が終わってしまいます。<br />
（それはそれで面白いかもしれませんが・・・）</p><br />
<p>　例えば、今使っているマシンが遅い場合や使いたいコマンド等が<br />
インストールされていない状況を考えます。<br />
私の場合は、USP研究所のビジネス用 Tukubai<br />
コマンドを使いたい場合や、<br />
あるマシンのTeXの環境を使いたいという場合がこれに相当します。</p><br />
<p>　一例として、手元にあるファイルをリモートのサーバで<br />
ソートして戻してもらうことを考えましょう。</p><br />
<p>　まずリスト12に、普通のシェルスクリプトを示します。<br />
これは、あるリモートのサーバに <tt class="docutils literal"><span class="pre">scp</span></tt> でファイルを送り込み、<br />
ソートした後にファイルを戻すという処理です。<br />
Macの <tt class="docutils literal"><span class="pre">sort</span></tt><br />
コマンドで1千万行のソートなんかやっちゃったらいつ終わるのか読めないので、<br />
これくらいのことは行う価値はあります。</p><br />
<ul class="simple"><br />
<li>リスト12: 「べたな」リモートサーバの使い方</li><br />
</ul><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre>//このデータ（1千万行）を左端の数字でソートしたい<br />
uedamac:~ ueda<span class="nv">$ </span>head -n 2 TESTDATA10M<br />
2377 高知県 -9,987,759 2001年1月5日<br />
2910 鹿児島県 5,689,492 1992年5月6日<br />
uedamac:~ ueda<span class="nv">$ </span>cat sort.sh<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
scp -P 11111 ./TESTDATA10M usp.usp-lab.com:~/<br />
//msortは、マルチスレッドの高速ソートコマンド<br />
ssh -p 11111 usp.usp-lab.com <span class="s2">&quot;msort -p 8 key=1 ~/TESTDATA10M &gt; ~/ueda.tmp&quot;</span><br />
scp -P 11111 usp.usp-lab.com:~/ueda.tmp ./TESTDATA10M.sort<br />
<br />
//手元のMacで実行<br />
uedamac:~ ueda<span class="nv">$ </span><span class="nb">time</span> ./sort.sh<br />
<br />
real 4m1.717s<br />
user 0m13.969s<br />
sys 0m10.090s<br />
//結果が得られた<br />
uedamac:~ ueda<span class="nv">$ </span>head -n 2 TESTDATA10M.sort<br />
0000 岩手県 5,630,892 2006年5月26日<br />
0000 新潟県 1,367,399 1998年8月22日<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　こういった通信ばっかりのシェルスクリプトを書いた人は<br />
そんなにいないと思いますが、<br />
シェルスクリプトなど所詮、人の操作のメモ書きですので、<br />
いつも <tt class="docutils literal"><span class="pre">scp,</span> <span class="pre">ssh</span></tt> を使っていれば理解できるでしょう。</p><br />
<p>　ところでこのシェルスクリプトでは、<br />
中間ファイルがリモートのサーバにできてしまっていますが、<br />
これを避けるにはどうすればよいでしょうか。<br />
こういう中間ファイルは、計算を <tt class="docutils literal"><span class="pre">Ctrl+c</span></tt><br />
などで中断した場合にリモートのサーバにゴミを残すことになります。<br />
処理によっては、次に計算したときに悪さをすることもあります。</p><br />
<p>　これを解決するには「シェル芸」です。<br />
「開眼シェルスクリプト」という名前で連載をしていますが、</p><br />
<p><em>不要なシェルスクリプトと中間ファイルはゴミ</em></p><br />
<p>です。こんなもん、ワンライナーで十分です。<br />
リスト13に示します。</p><br />
<ul class="simple"><br />
<li>リスト13: リモートサーバを使うワンライナー</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">time </span>cat TESTDATA10M | ssh -p 10022 usp.usp-lab.com <span class="s1">&#39;cat | msort -p 8 key=1&#39;</span> &gt; TESTDATA10M.sort3<br />
<br />
real 5m0.033s<br />
user 0m14.077s<br />
sys 0m9.415s<br />
</pre></div><br />
</td></tr></table></div><br />
<p>これで、sshでソートした出力は、（太字）手元のMacの標準出力から出てきます。<br />
<tt class="docutils literal"><span class="pre">ssh</span></tt> が（リモートでなく）<br />
手元のマシンの標準入出力に字を出し入れしてくれることは、<br />
<tt class="docutils literal"><span class="pre">ssh</span></tt> コマンドが手元のマシンで動いているので当然と言えば当然ですが、<br />
よくよく考えるととても便利なことです。<br />
ワンライナーとしては難解かもしれませんが、<br />
リモートとローカルがシームレスにつながっています。<br />
パイプラインなので、ストレージを使う事もありません。</p><br />
<p>　ちょっとやりすぎですが、<br />
筆者の自宅とサーバの間の通信速度がそんなに速くないので、<br />
<tt class="docutils literal"><span class="pre">gzip,</span> <span class="pre">gunzip</span></tt> を使ってリスト14のようにチューンしたらさらに時短できました。</p><br />
<ul class="simple"><br />
<li>リスト14: 圧縮を挟み込んだワンライナー</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span><span class="nb">time </span>gzip &lt; TESTDATA10M | ssh -p 10022 usp.usp-lab.com <span class="s1">&#39;gunzip | msort -p 8 key=1 | gzip&#39;</span> | gunzip &gt; TESTDATA10M.sort3<br />
<br />
real 1m10.669s<br />
user 0m42.874s<br />
sys 0m2.806s<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>18.5. 終わりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回も前回に引き続き作り物をさぼって、<br />
サーバを股にかけてデータをやりとりし、処理する方法について書きました。<br />
bashの通信機能や、 <tt class="docutils literal"><span class="pre">ssh,</span> <span class="pre">scp,</span> <span class="pre">nc</span></tt><br />
などのコマンドについてちょっとした使い方を紹介しました。</p><br />
<p>　マシンを複数台使うと頭の中が混乱しがちです。<br />
その点、 <tt class="docutils literal"><span class="pre">ssh</span></tt> をパイプにつなぐことを覚えると、<br />
あまり頭を悩ませずに複数のマシンを使いこなすことができます。<br />
パイプラインは一方通行で順番にサーバをつなげていくだけなので、<br />
頭の中でいろんなマシンの絵を同時に思い浮かべる負荷が不要です。<br />
マシン間の通信速度はまだ向上していくでしょうから、<br />
これからは使う人が増えるかもしれません。</p><br />
<p>　次回からは、とうとう禁断のお題をやる覚悟ができました。<br />
「シェルスクリプトでCGI」というお題で作り物をしてみます。</p><br />
</div><br />
</div><br />
<br />

