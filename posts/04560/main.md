---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年3月号
出典: 技術評論社SoftwareDesign<br />
<br />
<br />
 <br />
 <div class="section" id="id1"><br />
<h1>15. 開眼シェルスクリプト 第15回画像処理で遊ぶ<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　皆様、ラーメンのおいしい季節、いかがお過ごしでしょうか。<br />
筆者は朝うどん、夜ラーメンという、太く短い人生を歩んでおります。</p><br />
<p>　今回の開眼シェルスクリプトは、<br />
バイナリデータをシェルスクリプトでいじるという宣言をしてあったので、<br />
何を扱おうか考えたのですが、</p><br />
<div class="section" id="ppm"><br />
<h2>15.1. ppm形式<a class="headerlink" href="#ppm" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　画像は我々が普段書いているようなテキストファイルと比べてサイズが大きいので、<br />
通常はバイナリ形式でファイルにします。<br />
ただ基本的には、ピクセル（画素）ごとに<br />
R（赤）、G（緑）、B（青）の値を記録したファイルならば、<br />
ディスプレイの上に画像として再現できます。</p><br />
<p>　実はテキストで画像を表現する形式は存在しています。<br />
ここでは、portable pixmap format (PPM) 形式について紹介します。</p><br />
<p>　ppm形式は、カラー画像の表現形式の一つです。<br />
ppm形式のなかにはテキスト（アスキーコード）<br />
でデータを持つ形式とバイナリで持つ形式がありますが、<br />
ここではテキストの形式について説明します。</p><br />
<p>　説明のため、次のようなjpgの写真を準備しました。<br />
これをppm形式にしてみましょう。</p><br />
<p>図1: 今回使う写真（ラーメン）</p><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="noodle.jpg"><img alt="ラーメン" src="noodle.jpg" style="width: 30%;" /></a><br />
</div><br />
<p>　画像の変換には、ImageMagickというツールが便利です。<br />
GUIアプリケーションの裏で使われていることもあるので、<br />
知らないうちに使っている人は多いかもしれません。<br />
環境によっては結構インストールが面倒だったりするのですが、<br />
ウェブ等で調べてなんとかインストールおねがいします。<br />
Ubuntuなら <tt class="docutils literal"><span class="pre">sudo</span> <span class="pre">apt-get</span> <span class="pre">install</span> <span class="pre">imagemagick</span></tt><br />
で問題なくインストールされます。</p><br />
<p>　インストールしたら、 <tt class="docutils literal"><span class="pre">convert</span></tt> という、<br />
ちょっとそのネーミングはどうなんだという名前のコマンドで<br />
ImageMagickの機能が使えるようになります。<br />
このように、オプションの最後の方に入力ファイル名と出力ファイル名を書いて変換します。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>convert -compress none noodle.jpg noodle.ppm<br />
//ちょっと大きすぎか・・・<br />
<span class="nv">$ </span>ls -lh noodle.*<br />
-rw-rw-r-- 1 ueda ueda 1.8M 12月 13 11:11 noodle.jpg<br />
-rw-rw-r-- 1 ueda ueda 83M 12月 13 13:06 noodle.ppm<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　できたファイルを <tt class="docutils literal"><span class="pre">head</span></tt> してみましょう。<br />
こんなふうに、テキストとして読めたらうまく変換できています。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head noodle.ppm<br />
P3<br />
2448 3264<br />
255<br />
112 14 13 112 14 13 113 15 14 114 16 15 112 14 13 111 13 12 111 13 12<br />
111 13 12 113 15 14 115 17 16 113 15 ...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ppmは、 <tt class="docutils literal"><span class="pre">head</span></tt> の出力のように、<br />
上数行のヘッダ部と、その下から始まる数字の羅列で構成されます。<br />
ヘッダ部は最初の4個の数字で構成され、<br />
順に画像の種類（P3:テキストのppm）、<br />
幅、高さ、ピクセルの値の最大値を表します。<br />
この画像は2448x3264、256階調で、<br />
テキスト形式で保存されているという意味になります。<br />
また、 <tt class="docutils literal"><span class="pre">#</span></tt> 記号があると、行末までコメント扱いされますので、<br />
なにか処理するときは <tt class="docutils literal"><span class="pre">sed</span> <span class="pre">'s/#.*$//'</span></tt> などで除去します。</p><br />
<p>　ボディー部には、画像の上の段から順番に、左から右に向かってR, G, Bの順にピクセル値が並びます。<br />
よく見ると数字が3個ごとに似ていることに気づきます。<br />
改行とスペースが区切り文字になり、改行はどこに入れてもよいことになっています。</p><br />
<p>　ppm形式はテキストファイルですが、立派な画像ファイルでもあるので、<br />
Linuxのデスクトップ環境ならば、GUI上でファイルをクリックするとjpegと同様、<br />
画像が閲覧できると思います。<br />
ppmにすると容量が巨大化しますし、<br />
これからやる処理も速くはありません。<br />
これは人間が手で画像処理するときに、<br />
わかりやすいようにするためのお賽銭ということでご了承を。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h2>15.2. シェルスクリプトで画像処理<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、シェルスクリプトでこの画像をいじってみましょう。<br />
ここで扱うことは <tt class="docutils literal"><span class="pre">convert</span></tt> のオプションで実現できることも多いので、<br />
興味がある方はmanを読んでみてください。<br />
本稿では、画像の形式変換のみでImageMagickを使います。</p><br />
<div class="section" id="id3"><br />
<h3>15.2.1. いつも扱っているようなデータ形式にする<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まずは、ppmのように数字が延々と並んでいるのは後処理が大変なので、<br />
次の形式のように5列のデータに変換しましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>縦の位置 横の位置 Rの値 Gの値 Bの値<br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　コードは次のようなものを書きました。<br />
コメントがあるとヘッダの行がずれてしまうので、<br />
まず、8行目でコメントの行を除去し、ヘッダ行を除いた一時ファイル<br />
<tt class="docutils literal"><span class="pre">$tmp-ppm</span></tt> を作ります。<br />
座標をつけるときに画像の幅が必要なので、<br />
11行目で <tt class="docutils literal"><span class="pre">$tmp-ppm</span></tt> のヘッダから幅を取得しています。</p><br />
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ppm2data<br />
<span class="c">#!/bin/bash</span><br />
<span class="c"># ppmを座標とピクセル値のレコードに変換</span><br />
<span class="c"># written by R. Ueda / Dec. 13, 2012</span><br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
<span class="c">#コメント行の除去</span><br />
grep -v <span class="s1">&#39;^#&#39;</span> &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-ppm<br />
<br />
<span class="c">#幅（ヘッダ二行目の最初の数字）を代入</span><br />
<span class="nv">W</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;NR==2{print $1}&#39;</span> <span class="nv">$tmp</span>-ppm<span class="k">)</span><br />
<br />
tail -n +4 <span class="nv">$tmp</span>-ppm |<br />
<span class="c">#数字を縦に並べる</span><br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
<span class="c">#空行が入るので除去</span><br />
grep -v <span class="s1">&#39;^$&#39;</span> |<br />
<span class="c">#3個ごとに数字を1レコードにする</span><br />
awk <span class="s1">&#39;{printf(&quot;%d &quot;,$1);if(NR%3==0){print &quot;&quot;}}&#39;</span> |<br />
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> <span class="s1">&#39;{n=NR-1;print int(n/w),n%w,$0}&#39;</span> |<br />
<span class="c">#出力: 1.縦の座標 2.横の座標 3-5. R,G,B値</span><br />
awk <span class="s1">&#39;{print sprintf(&quot;%04d %04d&quot;,$1,$2),$3,$4,$5}&#39;</span><br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　13行目以降が、ピクセルの値を並べ直して座標をレコードに付加するコードです。<br />
先に計算結果を見てから説明します。</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat noodle.ppm | ./ppm2data &gt; noodle.data<br />
<span class="nv">$ </span>head -n 3 noodle.data<br />
0 0 112 14 13<br />
0 1 112 14 13<br />
0 2 113 15 14<br />
<span class="nv">$ </span>tail -n 3 noodle.data<br />
0000 0000 112 14 13<br />
0000 0001 112 14 13<br />
0000 0002 113 15 14<br />
//ppmよりさらに巨大化<br />
<span class="nv">$ </span>ls -lh noodle.data<br />
-rw-rw-r-- 1 ueda ueda 158M 12月 14 10:58 noodle.data<br />
</pre></div><br />
</td></tr></table></div><br />
<p>まず、13行目の <tt class="docutils literal"><span class="pre">tail</span> <span class="pre">-n</span> <span class="pre">+4</span></tt> は、「4行目以降を出力」<br />
という意味になります。数字にプラスを付けると、<br />
その行数以降という意味になります。<br />
15行目では、数字を全部縦に並べなおしています。<br />
先に縦に並べて、19行目で3個ずつ横に並べています。<br />
17行目は、余計な空白があると空行ができるので、それを取り除いています。</p><br />
<p>　19行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、読み込んだ数字を横に並べていって、<br />
3回に一回改行を入れるという処理です。<br />
print は文字列を出力後に改行を入れるので、<br />
19行目のように空文字を出力すると改行の意味になります。</p><br />
<p>　20行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、各ピクセルのRGB値に座標を与えています。<br />
AWKでは、物の個数はなんでも1から数えます。<br />
<tt class="docutils literal"><span class="pre">NR</span></tt> は、今扱っているのが何レコード目かという変数ですが、<br />
これも1からスタートします。<br />
これは直感的でよいのですが、数学的には面倒な処理を生む原因になります。<br />
20行目の処理では、0から行数をカウントする <tt class="docutils literal"><span class="pre">n</span></tt> という変数を作り、<br />
そこから、各ピクセルが上から何行目、左から何列目に位置するかを計算しています。</p><br />
<p>　ところで、この処理は大きな画像で行うと結構時間を食いますので、<br />
小さめの画像で試してから大きな画像を処理してみてください。<br />
まあ、これはシェルスクリプトでやると高速処理は全く期待できません。<br />
ただまあ、スクリプト言語はどの言語もピクセルごとに読み出して処理するのは苦手なようです。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>15.2.2. 画像を切り出す<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて、ここからは <tt class="docutils literal"><span class="pre">noodle.data</span></tt> を使って画像にいたずらしてみましょう。<br />
まずは、基本として、画像の一部分を切り出してみましょう。<br />
シェルスクリプトでもよいのですが、<br />
あえて雑技団的な雰囲気を出すために端末でやってみました。<br />
画像の上から（約）1000ピクセル、下から300ピクセル分を削る処理です。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;$1&gt;&quot;1000&quot; &amp;&amp; $1&lt;&quot;2764&quot;&#39;</span> noodle.data &gt; tmp<br />
<span class="nv">$ H</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;{print $1}&#39;</span> tmp | uniq | wc -l<span class="k">)</span><br />
<span class="nv">$ W</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;{print $2}&#39;</span> tmp | tail -n 1 | sed <span class="s1">&#39;s/^00*//&#39;</span> | awk <span class="s1">&#39;{print $1+1}&#39;</span><span class="k">)</span><br />
<span class="nv">$ </span>awk <span class="s1">&#39;{print $3,$4,$5}&#39;</span> tmp &gt; body<br />
<span class="nv">$ </span><span class="nb">echo </span>P3 &gt; header<br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$W</span> <span class="nv">$H</span> &gt;&gt; header<br />
<span class="nv">$ </span><span class="nb">echo </span>255 &gt;&gt; header<br />
<span class="nv">$ </span>cat header body &gt; hoge.ppm<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">noodle.data</span></tt> は、第1フィールドが縦の座標なので、<br />
1行目で1001ピクセル目からのピクセルが抽出できます。<br />
2,3行目は、画像の高さと幅を計算してそれぞれファイルに保存しています。<br />
なぜこうなるかは考えてみてください。<br />
4行目で、画像のボディー部を作ります。<br />
座標を取り除けばそのままppmのデータとして使えます。<br />
あとはヘッダを一行ずつ書いていって、拡張子が <tt class="docutils literal"><span class="pre">ppm</span></tt><br />
のファイルに保存して一丁上がりです。</p><br />
<p>　私の環境では、ファイルをクリックすると、<br />
次のように画像を見ることができます。<br />
・・・お腹がすいてきました。</p><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="hogescreen.png"><img alt="ラーメン" src="hogescreen.png" style="width: 30%;" /></a><br />
</div><br />
<p>　見られない人は、 <tt class="docutils literal"><span class="pre">convert</span></tt> でjpgかなにかに変換しましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>convert hoge.ppm hoge.jpg<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id5"><br />
<h3>15.2.3. ネガを作る<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次に、色を反転させてみましょう。<br />
これは簡単で、RGB値それぞれを反転させればよいということになります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat noodle.data | awk <span class="s1">&#39;{print 255-$3,255-$4,255-$5}&#39;</span> &gt; body<br />
//もとのヘッダをつける<br />
<span class="nv">$ </span>head -n 3 hoge.ppm | cat - body &gt; nega.ppm<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次のような画像になります。カラーじゃないのが残念ですが、<br />
今度は淡青色スープにウミウシのようなチャーシューと黒髪のような白髪ネギを搭載した、<br />
大変食欲を無くすラーメン画像になります。</p><br />
<p>図: 食欲を無くす、ネガティブラーメン画像</p><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="nega.png"><img alt="ネガ" src="nega.png" style="width: 30%;" /></a><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h3>15.2.4. 画像を合成<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次は、ラーメン画像に別の画像を合成してみましょう。<br />
偶然（嘘）、私の画像ディレクトリに、 <tt class="docutils literal"><span class="pre">noodle.ppm</span></tt><br />
と同じ大きさの次のような画像 <tt class="docutils literal"><span class="pre">curry.ppm</span></tt> がありました。<br />
（脚注：素直に「ラーメン」としないのは性格上の問題です。）</p><br />
<p>図：合成する画像</p><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="curry.png"><img alt="" src="curry.png" style="width: 30%;" /></a><br />
</div><br />
<p>これを次のように処理します。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat curry.ppm | ./ppm2data &gt; curry.data<br />
<span class="nv">$ </span>loopj <span class="nv">num</span><span class="o">=</span>2 noodle.data curry.data &gt; tmp<br />
<span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;{print $3*$6/255,$4*$7/255,$5*$8/255}&#39;</span> | sed <span class="s1">&#39;s/\\.[0-9]*//g&#39;</span> &gt; body<br />
<span class="nv">$ </span>head -n 3 noodle.ppm | cat - body &gt; curry_noodle.ppm<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">loopj</span></tt> は Open usp Tukubai のコマンドで、<br />
次のような動きをします。<br />
二つ以上のファイルの各レコードについて、<br />
キーが同じレコードを連結します。<br />
<tt class="docutils literal"><span class="pre">num=1</span></tt> は左から1フィールドをキーするという意味です。<br />
キーはソートされている必要があり、<br />
あるファイルにあるキーのレコードがないと、<br />
0でパディングされます。</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>cat file1<br />
001 aaa 123<br />
003 bbb 234<br />
ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>cat file2<br />
001 AAA<br />
002 BBB<br />
004 CCC<br />
ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>loopj <span class="nv">num</span><span class="o">=</span>1 file1 file2<br />
001 aaa 123 AAA<br />
002 0 0 BBB<br />
003 bbb 234 0<br />
004 0 0 CCC<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　ですので、2行目は、画素の位置をキーにして、<br />
<tt class="docutils literal"><span class="pre">noodle.data</span></tt> と <tt class="docutils literal"><span class="pre">curry.data</span></tt> を連結しているという意味になります。<br />
<tt class="docutils literal"><span class="pre">tmp</span></tt> の最初の部分を示します。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head -n 3 tmp<br />
0000 0000 112 14 13 255 255 255<br />
0000 0001 112 14 13 255 255 255<br />
0000 0002 113 15 14 255 255 255<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　3行目は、 <tt class="docutils literal"><span class="pre">noodle</span></tt> と <tt class="docutils literal"><span class="pre">curry</span></tt> のピクセルを比較して、<br />
<tt class="docutils literal"><span class="pre">curry</span></tt> の字のない部分（RGBそれぞれ値が255）については、<br />
<tt class="docutils literal"><span class="pre">noodle</span></tt> の値、字のある部分については画素が黒くなる演算をしています。<br />
例えば <tt class="docutils literal"><span class="pre">$3*$6/255</span></tt> は <tt class="docutils literal"><span class="pre">$6=255</span></tt> なら答えは <tt class="docutils literal"><span class="pre">$3</span></tt> の値になるし、<br />
<tt class="docutils literal"><span class="pre">$6=0</span></tt> なら答えは <tt class="docutils literal"><span class="pre">0</span></tt> になります。<br />
3行目の <tt class="docutils literal"><span class="pre">sed</span></tt> は、演算結果の小数点部分を削除する働きをします。<br />
この、計算のような文字列処理が入るのは、<br />
シェルを操作しておもしろいことの一つです。</p><br />
<p>　最後、4行目でヘッダをつけて次のような画像の完成です。</p><br />
<p>図：カレーラーメンではありません。</p><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="curry_noodle.png"><img alt="カレーラーメン" src="curry_noodle.png" style="width: 30%;" /></a><br />
</div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>15.2.5. モザイクをかける<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　最後は、もうちょっと難しいことをしてみましょう。<br />
ブーム（脚注：Nudiferで検索を。）<br />
に乗ってラーメンにモザイクをかけてみます。</p><br />
<p>　まず、ラーメンの画像を100ピクセルごとに区切ってブロック化します。<br />
次のように、 <tt class="docutils literal"><span class="pre">noodle.data</span></tt> の座標からグループのコードを作ります。<br />
<tt class="docutils literal"><span class="pre">tail</span></tt> の出力のように、例えば <tt class="docutils literal"><span class="pre">(3263,2445)</span></tt><br />
はグループ <tt class="docutils literal"><span class="pre">(32,24)</span></tt> ということを、各レコードの後ろに付加しておきます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $0,substr($1,1,2),substr($2,1,2)}&#39;</span> noodle.data &gt; tran<br />
<span class="nv">$ </span>tail -n 3 tran<br />
3263 2445 199 132 90 32 24<br />
3263 2446 198 131 89 32 24<br />
3263 2447 199 132 90 32 24<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次に、各グループの画素値を平均します。<br />
このデータがモザイクのレイヤーになります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $6,$7,$3,$4,$5}&#39;</span> tran | sort -k1,2 -s | sm2 +count 1 2 3 5 | awk <span class="s1">&#39;{print $1,$2,$4/$3,$5/$3,$6/$3}&#39;</span> | sed <span class="s1">&#39;s/\\.[0-9]*//g&#39;</span> &gt; mean<br />
</pre></div><br />
</td></tr></table></div><br />
<p>上のコードでは、まずグループを左側に持ってきてキーにして、<br />
ソートし、Tukubai コマンドの <tt class="docutils literal"><span class="pre">sm2</span></tt> で足し込んでいます。<br />
<tt class="docutils literal"><span class="pre">sm2</span></tt> の後の出力は次のようになります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $6,$7,$3,$4,$5}&#39;</span> tran | sort -k1,2 -s | sm2 +count 1 2 3 5 | head -n 3<br />
00 00 10000 1096186 274854 214869<br />
00 01 10000 1049205 268678 207120<br />
00 02 10000 1048624 266316 212040<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">sm2</span> <span class="pre">+count</span> <span class="pre">1</span> <span class="pre">2</span> <span class="pre">3</span> <span class="pre">5</span></tt> は、1,2列目をキーにして、<br />
キーごとに3～5列目を足し込むという意味になります。<br />
<tt class="docutils literal"><span class="pre">+count</span></tt> をつけると、足し込むときにキーの数を数えておき、<br />
レコードの出力の際にキーの横に数を付加します。<br />
ですので、この出力の6,7,8列目を3列目で割ると、<br />
各グループの平均のRGB値になります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">sort</span> <span class="pre">-k1,2</span> <span class="pre">-s</span></tt> の <tt class="docutils literal"><span class="pre">-s</span></tt> ですが、<br />
これは、ソートキーが同じレコードの順番を変えない<br />
「安定ソート」のオプションです。<br />
この処理では安定ソートは不要ですが、 <tt class="docutils literal"><span class="pre">sort</span></tt><br />
コマンドは安定ソートの方が早く終わるので経験的に付けています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">mean</span></tt> のレコードの一部を次に示します。<br />
この部分の処理は、元の画像が大きかったので<br />
open版の <tt class="docutils literal"><span class="pre">sm2</span></tt> だと10分程度かかってしまいました。<br />
AWKでこの計算をすると、もっと速く処理できます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>tail -n 3 mean<br />
32 22 194 132 78<br />
32 23 200 137 86<br />
32 24 200 138 89<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　モザイクのレイヤーのRGB値が計算できたら、<br />
さきほど作った <tt class="docutils literal"><span class="pre">tran</span></tt> ファイルに <tt class="docutils literal"><span class="pre">mean</span></tt><br />
ファイルを連結します。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cjoin1 <span class="nv">key</span><span class="o">=</span>6/7 mean tran | delf 6 7 &gt; tmp<br />
<span class="nv">$ </span>tail -n 3 tmp<br />
3263 2445 199 132 90 200 138 89<br />
3263 2446 198 131 89 200 138 89<br />
3263 2447 199 132 90 200 138 89<br />
//↑座標、もとのRGB値、モザイクのRGB値<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">cjoin1</span></tt> という Tukubai コマンドを使いました。<br />
このコマンドは、 <tt class="docutils literal"><span class="pre">tran</span></tt><br />
の第6,7列目のデータと <tt class="docutils literal"><span class="pre">mean</span></tt> の左2列を比較して、<br />
<tt class="docutils literal"><span class="pre">mean</span></tt> の内容を <tt class="docutils literal"><span class="pre">tran</span></tt> に連結します。<br />
<tt class="docutils literal"><span class="pre">join1</span></tt> というコマンドもあるのですが、<br />
こちらは <tt class="docutils literal"><span class="pre">tran</span></tt> 側が6,7列目でソートしていないと使えません。<br />
マスタ扱いされる <tt class="docutils literal"><span class="pre">mean</span></tt> の方は、<br />
<tt class="docutils literal"><span class="pre">cjoin1</span></tt> でもキーでソートされている必要があります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">delf</span></tt> は指定した列を消すコマンドで、<br />
既に不要なグループのキーを消去しています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">tmp</span></tt> が作成できたら、もう少しです。<br />
以下のようにコマンドを打ちます。<br />
読むのが大変ですが、要は画像の範囲指定をして、<br />
範囲内ならモザイクのRGB値、<br />
範囲外なら元の画像のRGB値を出力しているだけです。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{if($1&gt;=1000&amp;&amp;$1&lt;=2400&amp;&amp;$2&gt;=100&amp;&amp;$2&lt;=2000){print $6,$7,$8}else{print $3,$4,$5}}&#39;</span> tmp &gt; body<br />
<span class="nv">$ </span>head -n 3 noodle.ppm | cat - body &gt; moz.ppm<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="moz.png"><img alt="モザイク" src="moz.png" style="width: 30%;" /></a><br />
</div><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h2>15.3. 終わりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はシェルでバイナリデータを扱うということで、<br />
画像処理をやってみました。</p><br />
<p>　しかし、よくよく考えてみると、<br />
バイナリデータを最初に<br />
ImageMagick でテキストにしてしまったので、<br />
バイナリだからどうという処理は出てきませんでした。<br />
結局、相互に変換する道具さえあればよいということで、<br />
両者に本質的な違いはなく、<br />
シェルスクリプトで行うようなテキスト処理に落とし込むことができます。</p><br />
<p>　ただし、jpgのように圧縮効率のよいデータの形式と、<br />
テキストのようにベタなデータでは、<br />
サイズに100倍近い違いがありました。<br />
テキストを圧縮してもjpgにはサイズにはかないません。</p><br />
<p>　一方で、EXIF情報のように、<br />
人が読めない形式（= <tt class="docutils literal"><span class="pre">cat</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> で読めない形式）<br />
で情報が保存されてしまうと、いろいろ問題が起こりがちです。<br />
もしかしたら、<br />
テキストファイルで画像を持つことが普通になる日が来るかもやしれません。</p><br />
<p>　次回は、今回のおふざけが編集様の怒りにふれなければ、<br />
もうちょと本格的な画像処理をやってみたいと考えております。</p><br />
</div><br />
</div>
