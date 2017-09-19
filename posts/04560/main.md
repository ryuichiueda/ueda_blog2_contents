---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年3月号
出典: 技術評論社SoftwareDesign


 
 <div class="section" id="id1">
<h1>15. 開眼シェルスクリプト 第15回画像処理で遊ぶ<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　皆様、ラーメンのおいしい季節、いかがお過ごしでしょうか。
筆者は朝うどん、夜ラーメンという、太く短い人生を歩んでおります。</p>
<p>　今回の開眼シェルスクリプトは、
バイナリデータをシェルスクリプトでいじるという宣言をしてあったので、
何を扱おうか考えたのですが、</p>
<div class="section" id="ppm">
<h2>15.1. ppm形式<a class="headerlink" href="#ppm" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　画像は我々が普段書いているようなテキストファイルと比べてサイズが大きいので、
通常はバイナリ形式でファイルにします。
ただ基本的には、ピクセル（画素）ごとに
R（赤）、G（緑）、B（青）の値を記録したファイルならば、
ディスプレイの上に画像として再現できます。</p>
<p>　実はテキストで画像を表現する形式は存在しています。
ここでは、portable pixmap format (PPM) 形式について紹介します。</p>
<p>　ppm形式は、カラー画像の表現形式の一つです。
ppm形式のなかにはテキスト（アスキーコード）
でデータを持つ形式とバイナリで持つ形式がありますが、
ここではテキストの形式について説明します。</p>
<p>　説明のため、次のようなjpgの写真を準備しました。
これをppm形式にしてみましょう。</p>
<p>図1: 今回使う写真（ラーメン）</p>
<div class="figure">
<a class="reference internal image-reference" href="noodle.jpg"><img alt="ラーメン" src="noodle.jpg" style="width: 30%;" /></a>
</div>
<p>　画像の変換には、ImageMagickというツールが便利です。
GUIアプリケーションの裏で使われていることもあるので、
知らないうちに使っている人は多いかもしれません。
環境によっては結構インストールが面倒だったりするのですが、
ウェブ等で調べてなんとかインストールおねがいします。
Ubuntuなら <tt class="docutils literal"><span class="pre">sudo</span> <span class="pre">apt-get</span> <span class="pre">install</span> <span class="pre">imagemagick</span></tt>
で問題なくインストールされます。</p>
<p>　インストールしたら、 <tt class="docutils literal"><span class="pre">convert</span></tt> という、
ちょっとそのネーミングはどうなんだという名前のコマンドで
ImageMagickの機能が使えるようになります。
このように、オプションの最後の方に入力ファイル名と出力ファイル名を書いて変換します。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>convert -compress none noodle.jpg noodle.ppm
//ちょっと大きすぎか・・・
<span class="nv">$ </span>ls -lh noodle.*
-rw-rw-r-- 1 ueda ueda 1.8M 12月 13 11:11 noodle.jpg
-rw-rw-r-- 1 ueda ueda 83M 12月 13 13:06 noodle.ppm
</pre></div>
</td></tr></table></div>
<p>　できたファイルを <tt class="docutils literal"><span class="pre">head</span></tt> してみましょう。
こんなふうに、テキストとして読めたらうまく変換できています。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head noodle.ppm
P3
2448 3264
255
112 14 13 112 14 13 113 15 14 114 16 15 112 14 13 111 13 12 111 13 12
111 13 12 113 15 14 115 17 16 113 15 ...
</pre></div>
</td></tr></table></div>
<p>　ppmは、 <tt class="docutils literal"><span class="pre">head</span></tt> の出力のように、
上数行のヘッダ部と、その下から始まる数字の羅列で構成されます。
ヘッダ部は最初の4個の数字で構成され、
順に画像の種類（P3:テキストのppm）、
幅、高さ、ピクセルの値の最大値を表します。
この画像は2448x3264、256階調で、
テキスト形式で保存されているという意味になります。
また、 <tt class="docutils literal"><span class="pre">#</span></tt> 記号があると、行末までコメント扱いされますので、
なにか処理するときは <tt class="docutils literal"><span class="pre">sed</span> <span class="pre">'s/#.*$//'</span></tt> などで除去します。</p>
<p>　ボディー部には、画像の上の段から順番に、左から右に向かってR, G, Bの順にピクセル値が並びます。
よく見ると数字が3個ごとに似ていることに気づきます。
改行とスペースが区切り文字になり、改行はどこに入れてもよいことになっています。</p>
<p>　ppm形式はテキストファイルですが、立派な画像ファイルでもあるので、
Linuxのデスクトップ環境ならば、GUI上でファイルをクリックするとjpegと同様、
画像が閲覧できると思います。
ppmにすると容量が巨大化しますし、
これからやる処理も速くはありません。
これは人間が手で画像処理するときに、
わかりやすいようにするためのお賽銭ということでご了承を。</p>
</div>
<div class="section" id="id2">
<h2>15.2. シェルスクリプトで画像処理<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、シェルスクリプトでこの画像をいじってみましょう。
ここで扱うことは <tt class="docutils literal"><span class="pre">convert</span></tt> のオプションで実現できることも多いので、
興味がある方はmanを読んでみてください。
本稿では、画像の形式変換のみでImageMagickを使います。</p>
<div class="section" id="id3">
<h3>15.2.1. いつも扱っているようなデータ形式にする<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まずは、ppmのように数字が延々と並んでいるのは後処理が大変なので、
次の形式のように5列のデータに変換しましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>縦の位置 横の位置 Rの値 Gの値 Bの値
...
</pre></div>
</td></tr></table></div>
<p>　コードは次のようなものを書きました。
コメントがあるとヘッダの行がずれてしまうので、
まず、8行目でコメントの行を除去し、ヘッダ行を除いた一時ファイル
<tt class="docutils literal"><span class="pre">$tmp-ppm</span></tt> を作ります。
座標をつけるときに画像の幅が必要なので、
11行目で <tt class="docutils literal"><span class="pre">$tmp-ppm</span></tt> のヘッダから幅を取得しています。</p>
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
25</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat ppm2data
<span class="c">#!/bin/bash</span>
<span class="c"># ppmを座標とピクセル値のレコードに変換</span>
<span class="c"># written by R. Ueda / Dec. 13, 2012</span>
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

<span class="c">#コメント行の除去</span>
grep -v <span class="s1">&#39;^#&#39;</span> &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-ppm

<span class="c">#幅（ヘッダ二行目の最初の数字）を代入</span>
<span class="nv">W</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;NR==2{print $1}&#39;</span> <span class="nv">$tmp</span>-ppm<span class="k">)</span>

tail -n +4 <span class="nv">$tmp</span>-ppm |
<span class="c">#数字を縦に並べる</span>
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
<span class="c">#空行が入るので除去</span>
grep -v <span class="s1">&#39;^$&#39;</span> |
<span class="c">#3個ごとに数字を1レコードにする</span>
awk <span class="s1">&#39;{printf(&quot;%d &quot;,$1);if(NR%3==0){print &quot;&quot;}}&#39;</span> |
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> <span class="s1">&#39;{n=NR-1;print int(n/w),n%w,$0}&#39;</span> |
<span class="c">#出力: 1.縦の座標 2.横の座標 3-5. R,G,B値</span>
awk <span class="s1">&#39;{print sprintf(&quot;%04d %04d&quot;,$1,$2),$3,$4,$5}&#39;</span>

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　13行目以降が、ピクセルの値を並べ直して座標をレコードに付加するコードです。
先に計算結果を見てから説明します。</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat noodle.ppm | ./ppm2data &gt; noodle.data
<span class="nv">$ </span>head -n 3 noodle.data
0 0 112 14 13
0 1 112 14 13
0 2 113 15 14
<span class="nv">$ </span>tail -n 3 noodle.data
0000 0000 112 14 13
0000 0001 112 14 13
0000 0002 113 15 14
//ppmよりさらに巨大化
<span class="nv">$ </span>ls -lh noodle.data
-rw-rw-r-- 1 ueda ueda 158M 12月 14 10:58 noodle.data
</pre></div>
</td></tr></table></div>
<p>まず、13行目の <tt class="docutils literal"><span class="pre">tail</span> <span class="pre">-n</span> <span class="pre">+4</span></tt> は、「4行目以降を出力」
という意味になります。数字にプラスを付けると、
その行数以降という意味になります。
15行目では、数字を全部縦に並べなおしています。
先に縦に並べて、19行目で3個ずつ横に並べています。
17行目は、余計な空白があると空行ができるので、それを取り除いています。</p>
<p>　19行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、読み込んだ数字を横に並べていって、
3回に一回改行を入れるという処理です。
print は文字列を出力後に改行を入れるので、
19行目のように空文字を出力すると改行の意味になります。</p>
<p>　20行目の <tt class="docutils literal"><span class="pre">awk</span></tt> は、各ピクセルのRGB値に座標を与えています。
AWKでは、物の個数はなんでも1から数えます。
<tt class="docutils literal"><span class="pre">NR</span></tt> は、今扱っているのが何レコード目かという変数ですが、
これも1からスタートします。
これは直感的でよいのですが、数学的には面倒な処理を生む原因になります。
20行目の処理では、0から行数をカウントする <tt class="docutils literal"><span class="pre">n</span></tt> という変数を作り、
そこから、各ピクセルが上から何行目、左から何列目に位置するかを計算しています。</p>
<p>　ところで、この処理は大きな画像で行うと結構時間を食いますので、
小さめの画像で試してから大きな画像を処理してみてください。
まあ、これはシェルスクリプトでやると高速処理は全く期待できません。
ただまあ、スクリプト言語はどの言語もピクセルごとに読み出して処理するのは苦手なようです。</p>
</div>
<div class="section" id="id4">
<h3>15.2.2. 画像を切り出す<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて、ここからは <tt class="docutils literal"><span class="pre">noodle.data</span></tt> を使って画像にいたずらしてみましょう。
まずは、基本として、画像の一部分を切り出してみましょう。
シェルスクリプトでもよいのですが、
あえて雑技団的な雰囲気を出すために端末でやってみました。
画像の上から（約）1000ピクセル、下から300ピクセル分を削る処理です。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;$1&gt;&quot;1000&quot; &amp;&amp; $1&lt;&quot;2764&quot;&#39;</span> noodle.data &gt; tmp
<span class="nv">$ H</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;{print $1}&#39;</span> tmp | uniq | wc -l<span class="k">)</span>
<span class="nv">$ W</span><span class="o">=</span><span class="k">$(</span>awk <span class="s1">&#39;{print $2}&#39;</span> tmp | tail -n 1 | sed <span class="s1">&#39;s/^00*//&#39;</span> | awk <span class="s1">&#39;{print $1+1}&#39;</span><span class="k">)</span>
<span class="nv">$ </span>awk <span class="s1">&#39;{print $3,$4,$5}&#39;</span> tmp &gt; body
<span class="nv">$ </span><span class="nb">echo </span>P3 &gt; header
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$W</span> <span class="nv">$H</span> &gt;&gt; header
<span class="nv">$ </span><span class="nb">echo </span>255 &gt;&gt; header
<span class="nv">$ </span>cat header body &gt; hoge.ppm
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">noodle.data</span></tt> は、第1フィールドが縦の座標なので、
1行目で1001ピクセル目からのピクセルが抽出できます。
2,3行目は、画像の高さと幅を計算してそれぞれファイルに保存しています。
なぜこうなるかは考えてみてください。
4行目で、画像のボディー部を作ります。
座標を取り除けばそのままppmのデータとして使えます。
あとはヘッダを一行ずつ書いていって、拡張子が <tt class="docutils literal"><span class="pre">ppm</span></tt>
のファイルに保存して一丁上がりです。</p>
<p>　私の環境では、ファイルをクリックすると、
次のように画像を見ることができます。
・・・お腹がすいてきました。</p>
<div class="figure">
<a class="reference internal image-reference" href="hogescreen.png"><img alt="ラーメン" src="hogescreen.png" style="width: 30%;" /></a>
</div>
<p>　見られない人は、 <tt class="docutils literal"><span class="pre">convert</span></tt> でjpgかなにかに変換しましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>convert hoge.ppm hoge.jpg
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id5">
<h3>15.2.3. ネガを作る<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次に、色を反転させてみましょう。
これは簡単で、RGB値それぞれを反転させればよいということになります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat noodle.data | awk <span class="s1">&#39;{print 255-$3,255-$4,255-$5}&#39;</span> &gt; body
//もとのヘッダをつける
<span class="nv">$ </span>head -n 3 hoge.ppm | cat - body &gt; nega.ppm
</pre></div>
</td></tr></table></div>
<p>　次のような画像になります。カラーじゃないのが残念ですが、
今度は淡青色スープにウミウシのようなチャーシューと黒髪のような白髪ネギを搭載した、
大変食欲を無くすラーメン画像になります。</p>
<p>図: 食欲を無くす、ネガティブラーメン画像</p>
<div class="figure">
<a class="reference internal image-reference" href="nega.png"><img alt="ネガ" src="nega.png" style="width: 30%;" /></a>
</div>
</div>
<div class="section" id="id6">
<h3>15.2.4. 画像を合成<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次は、ラーメン画像に別の画像を合成してみましょう。
偶然（嘘）、私の画像ディレクトリに、 <tt class="docutils literal"><span class="pre">noodle.ppm</span></tt>
と同じ大きさの次のような画像 <tt class="docutils literal"><span class="pre">curry.ppm</span></tt> がありました。
（脚注：素直に「ラーメン」としないのは性格上の問題です。）</p>
<p>図：合成する画像</p>
<div class="figure">
<a class="reference internal image-reference" href="curry.png"><img alt="" src="curry.png" style="width: 30%;" /></a>
</div>
<p>これを次のように処理します。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat curry.ppm | ./ppm2data &gt; curry.data
<span class="nv">$ </span>loopj <span class="nv">num</span><span class="o">=</span>2 noodle.data curry.data &gt; tmp
<span class="nv">$ </span>cat tmp | awk <span class="s1">&#39;{print $3*$6/255,$4*$7/255,$5*$8/255}&#39;</span> | sed <span class="s1">&#39;s/\\.[0-9]*//g&#39;</span> &gt; body
<span class="nv">$ </span>head -n 3 noodle.ppm | cat - body &gt; curry_noodle.ppm
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">loopj</span></tt> は Open usp Tukubai のコマンドで、
次のような動きをします。
二つ以上のファイルの各レコードについて、
キーが同じレコードを連結します。
<tt class="docutils literal"><span class="pre">num=1</span></tt> は左から1フィールドをキーするという意味です。
キーはソートされている必要があり、
あるファイルにあるキーのレコードがないと、
0でパディングされます。</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>cat file1
001 aaa 123
003 bbb 234
ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>cat file2
001 AAA
002 BBB
004 CCC
ueda\@uedadsk:~/GIT/SD_GENKOU/201303<span class="nv">$ </span>loopj <span class="nv">num</span><span class="o">=</span>1 file1 file2
001 aaa 123 AAA
002 0 0 BBB
003 bbb 234 0
004 0 0 CCC
</pre></div>
</td></tr></table></div>
<p>　ですので、2行目は、画素の位置をキーにして、
<tt class="docutils literal"><span class="pre">noodle.data</span></tt> と <tt class="docutils literal"><span class="pre">curry.data</span></tt> を連結しているという意味になります。
<tt class="docutils literal"><span class="pre">tmp</span></tt> の最初の部分を示します。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head -n 3 tmp
0000 0000 112 14 13 255 255 255
0000 0001 112 14 13 255 255 255
0000 0002 113 15 14 255 255 255
</pre></div>
</td></tr></table></div>
<p>　3行目は、 <tt class="docutils literal"><span class="pre">noodle</span></tt> と <tt class="docutils literal"><span class="pre">curry</span></tt> のピクセルを比較して、
<tt class="docutils literal"><span class="pre">curry</span></tt> の字のない部分（RGBそれぞれ値が255）については、
<tt class="docutils literal"><span class="pre">noodle</span></tt> の値、字のある部分については画素が黒くなる演算をしています。
例えば <tt class="docutils literal"><span class="pre">$3*$6/255</span></tt> は <tt class="docutils literal"><span class="pre">$6=255</span></tt> なら答えは <tt class="docutils literal"><span class="pre">$3</span></tt> の値になるし、
<tt class="docutils literal"><span class="pre">$6=0</span></tt> なら答えは <tt class="docutils literal"><span class="pre">0</span></tt> になります。
3行目の <tt class="docutils literal"><span class="pre">sed</span></tt> は、演算結果の小数点部分を削除する働きをします。
この、計算のような文字列処理が入るのは、
シェルを操作しておもしろいことの一つです。</p>
<p>　最後、4行目でヘッダをつけて次のような画像の完成です。</p>
<p>図：カレーラーメンではありません。</p>
<div class="figure">
<a class="reference internal image-reference" href="curry_noodle.png"><img alt="カレーラーメン" src="curry_noodle.png" style="width: 30%;" /></a>
</div>
</div>
<div class="section" id="id7">
<h3>15.2.5. モザイクをかける<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　最後は、もうちょっと難しいことをしてみましょう。
ブーム（脚注：Nudiferで検索を。）
に乗ってラーメンにモザイクをかけてみます。</p>
<p>　まず、ラーメンの画像を100ピクセルごとに区切ってブロック化します。
次のように、 <tt class="docutils literal"><span class="pre">noodle.data</span></tt> の座標からグループのコードを作ります。
<tt class="docutils literal"><span class="pre">tail</span></tt> の出力のように、例えば <tt class="docutils literal"><span class="pre">(3263,2445)</span></tt>
はグループ <tt class="docutils literal"><span class="pre">(32,24)</span></tt> ということを、各レコードの後ろに付加しておきます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $0,substr($1,1,2),substr($2,1,2)}&#39;</span> noodle.data &gt; tran
<span class="nv">$ </span>tail -n 3 tran
3263 2445 199 132 90 32 24
3263 2446 198 131 89 32 24
3263 2447 199 132 90 32 24
</pre></div>
</td></tr></table></div>
<p>　次に、各グループの画素値を平均します。
このデータがモザイクのレイヤーになります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $6,$7,$3,$4,$5}&#39;</span> tran | sort -k1,2 -s | sm2 +count 1 2 3 5 | awk <span class="s1">&#39;{print $1,$2,$4/$3,$5/$3,$6/$3}&#39;</span> | sed <span class="s1">&#39;s/\\.[0-9]*//g&#39;</span> &gt; mean
</pre></div>
</td></tr></table></div>
<p>上のコードでは、まずグループを左側に持ってきてキーにして、
ソートし、Tukubai コマンドの <tt class="docutils literal"><span class="pre">sm2</span></tt> で足し込んでいます。
<tt class="docutils literal"><span class="pre">sm2</span></tt> の後の出力は次のようになります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{print $6,$7,$3,$4,$5}&#39;</span> tran | sort -k1,2 -s | sm2 +count 1 2 3 5 | head -n 3
00 00 10000 1096186 274854 214869
00 01 10000 1049205 268678 207120
00 02 10000 1048624 266316 212040
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">sm2</span> <span class="pre">+count</span> <span class="pre">1</span> <span class="pre">2</span> <span class="pre">3</span> <span class="pre">5</span></tt> は、1,2列目をキーにして、
キーごとに3～5列目を足し込むという意味になります。
<tt class="docutils literal"><span class="pre">+count</span></tt> をつけると、足し込むときにキーの数を数えておき、
レコードの出力の際にキーの横に数を付加します。
ですので、この出力の6,7,8列目を3列目で割ると、
各グループの平均のRGB値になります。</p>
<p>　 <tt class="docutils literal"><span class="pre">sort</span> <span class="pre">-k1,2</span> <span class="pre">-s</span></tt> の <tt class="docutils literal"><span class="pre">-s</span></tt> ですが、
これは、ソートキーが同じレコードの順番を変えない
「安定ソート」のオプションです。
この処理では安定ソートは不要ですが、 <tt class="docutils literal"><span class="pre">sort</span></tt>
コマンドは安定ソートの方が早く終わるので経験的に付けています。</p>
<p>　 <tt class="docutils literal"><span class="pre">mean</span></tt> のレコードの一部を次に示します。
この部分の処理は、元の画像が大きかったので
open版の <tt class="docutils literal"><span class="pre">sm2</span></tt> だと10分程度かかってしまいました。
AWKでこの計算をすると、もっと速く処理できます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>tail -n 3 mean
32 22 194 132 78
32 23 200 137 86
32 24 200 138 89
</pre></div>
</td></tr></table></div>
<p>　モザイクのレイヤーのRGB値が計算できたら、
さきほど作った <tt class="docutils literal"><span class="pre">tran</span></tt> ファイルに <tt class="docutils literal"><span class="pre">mean</span></tt>
ファイルを連結します。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cjoin1 <span class="nv">key</span><span class="o">=</span>6/7 mean tran | delf 6 7 &gt; tmp
<span class="nv">$ </span>tail -n 3 tmp
3263 2445 199 132 90 200 138 89
3263 2446 198 131 89 200 138 89
3263 2447 199 132 90 200 138 89
//↑座標、もとのRGB値、モザイクのRGB値
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">cjoin1</span></tt> という Tukubai コマンドを使いました。
このコマンドは、 <tt class="docutils literal"><span class="pre">tran</span></tt>
の第6,7列目のデータと <tt class="docutils literal"><span class="pre">mean</span></tt> の左2列を比較して、
<tt class="docutils literal"><span class="pre">mean</span></tt> の内容を <tt class="docutils literal"><span class="pre">tran</span></tt> に連結します。
<tt class="docutils literal"><span class="pre">join1</span></tt> というコマンドもあるのですが、
こちらは <tt class="docutils literal"><span class="pre">tran</span></tt> 側が6,7列目でソートしていないと使えません。
マスタ扱いされる <tt class="docutils literal"><span class="pre">mean</span></tt> の方は、
<tt class="docutils literal"><span class="pre">cjoin1</span></tt> でもキーでソートされている必要があります。</p>
<p>　 <tt class="docutils literal"><span class="pre">delf</span></tt> は指定した列を消すコマンドで、
既に不要なグループのキーを消去しています。</p>
<p>　 <tt class="docutils literal"><span class="pre">tmp</span></tt> が作成できたら、もう少しです。
以下のようにコマンドを打ちます。
読むのが大変ですが、要は画像の範囲指定をして、
範囲内ならモザイクのRGB値、
範囲外なら元の画像のRGB値を出力しているだけです。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;{if($1&gt;=1000&amp;&amp;$1&lt;=2400&amp;&amp;$2&gt;=100&amp;&amp;$2&lt;=2000){print $6,$7,$8}else{print $3,$4,$5}}&#39;</span> tmp &gt; body
<span class="nv">$ </span>head -n 3 noodle.ppm | cat - body &gt; moz.ppm
</pre></div>
</td></tr></table></div>
<div class="figure">
<a class="reference internal image-reference" href="moz.png"><img alt="モザイク" src="moz.png" style="width: 30%;" /></a>
</div>
</div>
</div>
<div class="section" id="id8">
<h2>15.3. 終わりに<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はシェルでバイナリデータを扱うということで、
画像処理をやってみました。</p>
<p>　しかし、よくよく考えてみると、
バイナリデータを最初に
ImageMagick でテキストにしてしまったので、
バイナリだからどうという処理は出てきませんでした。
結局、相互に変換する道具さえあればよいということで、
両者に本質的な違いはなく、
シェルスクリプトで行うようなテキスト処理に落とし込むことができます。</p>
<p>　ただし、jpgのように圧縮効率のよいデータの形式と、
テキストのようにベタなデータでは、
サイズに100倍近い違いがありました。
テキストを圧縮してもjpgにはサイズにはかないません。</p>
<p>　一方で、EXIF情報のように、
人が読めない形式（= <tt class="docutils literal"><span class="pre">cat</span></tt> や <tt class="docutils literal"><span class="pre">grep</span></tt> で読めない形式）
で情報が保存されてしまうと、いろいろ問題が起こりがちです。
もしかしたら、
テキストファイルで画像を持つことが普通になる日が来るかもやしれません。</p>
<p>　次回は、今回のおふざけが編集様の怒りにふれなければ、
もうちょと本格的な画像処理をやってみたいと考えております。</p>
</div>
</div>
