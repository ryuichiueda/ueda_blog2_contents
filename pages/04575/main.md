---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年4月号
出典: 技術評論社SoftwareDesign
 
 <div class="section" id="id1">
<h1>16. 開眼シェルスクリプト 第16回画像処理で遊ぶ（２）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　今回は前回に引き続き、シェルスクリプトで画像処理をして遊んでみましょう。
前回はコマンドで扱いやすくするために、
カラー画像を1ピクセル1レコードにしてから処理しました。
ただこの方法だけだとできることが限られるので、
今回は、awkをフルに使って画像処理をやってみます。
配列を操作するので、本連載史上、最も「普通の」プログラミングをやります。
そうは言っても、普通ではありませんが・・・。
しかし、この人もこんなことを言っているのでよいということにしましょう。
（注：完全に言い訳に使っています。）</p>
<p>『人生を楽しむ秘訣は普通にこだわらないこと。
普通と言われる人生を送る人間なんて、
一人としていやしない。いたらお目にかかりたいものだ』
&#8212; アルバート・アインシュタイン</p>
<div class="section" id="id2">
<h2>16.1. 環境<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、12年間親しんだThinkPadからMacBookAirに乗り換えたことを記念して、
Mac上のbashでコーディングします。なぜ乗り換えたかというと、
2月号の特集で「Macにはbashが入っているからターミナル使って欲しい」と書いた時に、
自分が率先しないといかん、と使命感に駆られたからです。
シャレ乙野郎になろうという気は毛頭ありません。
が、もともとカフェ中毒者なので「ドヤ顔mac」とか言われても仕方ありません。
言う側（言ってたのか）から言われる側になって辛いですが、
今月号からしばらくはMacでいきます。</p>
<ul class="simple">
<li>リスト1: 環境等</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>uname -a
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1:
Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64
<span class="nv">$ </span>bash --version
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span>
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.
<span class="nv">$ </span>awk --version
awk version 20070501
</pre></div>
</td></tr></table></div>
<p>　リスト1に、今回の環境を示します。
多くのLinuxディストリビューションと違って、
<tt class="docutils literal"><span class="pre">awk</span></tt> は <tt class="docutils literal"><span class="pre">gawk</span></tt> ではないので注意が必要ですが、
今回の内容では出力の違いはありません。</p>
</div>
<div class="section" id="awk">
<h2>16.2. AWKのおさらい<a class="headerlink" href="#awk" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="id3">
<h3>16.2.1. パターン<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　「パターン」は、これまで何度も使っていたとおり、
入力されたファイルから条件に合う行を抽出するためのものです。
パターンは <tt class="docutils literal"><span class="pre">grep</span></tt> の機能を担っていると考えてよいでしょう。
<tt class="docutils literal"><span class="pre">grep</span></tt> は抽出だけですが、AWKは抽出した行に対して
「アクション」で演算ができます。</p>
<p>　リスト2の例は、パターンで偶数を抽出して、
アクションで10で割るというものです。
<tt class="docutils literal"><span class="pre">jot</span> <span class="pre">10</span></tt> の出力は、 <tt class="docutils literal"><span class="pre">seq</span> <span class="pre">1</span> <span class="pre">10</span></tt> のものと同じです。</p>
<ul class="simple">
<li>リスト2: パターンとアクションの例</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>jot 10 | awk <span class="s1">&#39;$1%2==0{print $1/10}&#39;</span>
0.2
0.4
0.6
0.8
1
</pre></div>
</td></tr></table></div>
<p>　パターンとアクションの組みは、いくつも書くことができます。
リスト3のコードはAWKのプログラムで、偶数と奇数を数えるものです。
パターンは、「START」、「END」も含めて4個ですね。
紙面の関係と一行野郎中毒が祟って1行1パターンにしましたが、
Cのように改行・インデントをする方がAWKのスクリプトとしてはまともでしょう。</p>
<ul class="simple">
<li>リスト3: パターンを並べたAWKのコードの例</li>
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
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat oddeven.awk
<span class="c">#!/usr/bin/awk -f</span>

START<span class="o">{</span><span class="nv">even</span><span class="o">=</span>0;odd<span class="o">=</span>0<span class="o">}</span>
<span class="nv">$1</span>%2<span class="o">==</span>0<span class="o">{</span>even++<span class="o">}</span>
<span class="nv">$1</span>%2<span class="o">==</span>1<span class="o">{</span>odd++<span class="o">}</span>
END<span class="o">{</span>print <span class="s2">&quot;奇数:&quot;</span>,odd;print <span class="s2">&quot;偶数:&quot;</span>,even<span class="o">}</span>
<span class="nv">$ </span>jot 9 | ./oddeven.awk
奇数: 5
偶数: 4
</pre></div>
</td></tr></table></div>
<p>　一つの行が複数のパターンにマッチする時は、リスト4のように、
パターンに書いた順に何回も出力されます。
この辺の挙動は、単なるif文とは違うので注意が必要です。</p>
<ul class="simple">
<li>リスト4: 複数のパターンにマッチする場合</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo </span>1 | awk <span class="s1">&#39;{print $1,&quot;a&quot;}NR==1{print $1,&quot;b&quot;}NR!=2{print $1,&quot;c&quot;}&#39;</span>
1 a
1 b
1 c
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id4">
<h3>16.2.2. 関数<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　関数の書き方はjavascriptに似ています。
<tt class="docutils literal"><span class="pre">function</span> <span class="pre">名前(変数,...){文;文;...}</span></tt>
というように表記します。
リスト5は、関数の名前の書き方と使い方の例です。</p>
<ul class="simple">
<li>リスト5: 関数の書き方</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat func.sh
<span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="nv">$1</span> |
awk <span class="s1">&#39;{print scream($1,10)}</span>
<span class="s1"> function scream(a,n){return n==1?a:(scream(a,n-1) a)}&#39;</span>
<span class="nv">$ </span>./func.sh あ
ああああああああああ
</pre></div>
</td></tr></table></div>
<p>わざと再帰を使ってややこしくしており、
例としてはちょっと不適切かもしれませんが、
<tt class="docutils literal"><span class="pre">function</span></tt> の行が関数になっています。
この例のように、関数は使う場所より後ろに書いても大丈夫です。</p>
</div>
<div class="section" id="id5">
<h3>16.2.3. 配列<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　AWKは言語なのでもちろん配列があります。
AWKの配列は、連想配列として実装されています。
ですので、リスト6のような使い方ができます。</p>
<ul class="simple">
<li>リスト6: 配列の使い方</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{a[&quot;猫&quot;]=&quot;まっしぐら&quot;;print a[&quot;猫&quot;]}&#39;</span>
まっしぐら
</pre></div>
</td></tr></table></div>
<p>　もちろん、普通の配列としても使えます。
配列として使うときは、リスト6のように、
インデックスを0からではなく1から始めます。
自身で使うときは0からでも動きますが、
関数が配列を返すときは1に最初の要素が入っているので、
他に理由がなければ合わせましょう。</p>
<ul class="simple">
<li>リスト6: 配列の使い方その２</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo</span> 南海 ホークス | awk <span class="s1">&#39;{\\</span>
<span class="s1"> a[1]=$1;a[2]=$2;for(i=1;i&lt;=2;i++){print a[i]}}&#39;</span>
南海
ホークス
//split関数で文字列を切って配列aに代入
<span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;OH!MY!GOD!&#39;</span> | awk <span class="s1">&#39;{split($1,a,&quot;!&quot;);print a[2]}&#39;</span>
MY
</pre></div>
</td></tr></table></div>
<p>　表記に区別がないので、リスト7のようなこともできます。
Cでやったら間違いなく怒られますが大丈夫です。</p>
<ul class="simple">
<li>リスト7: インデックスが大きくても大丈夫</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{a[123456789]=10;print a[123456789]}&#39;</span>
10
</pre></div>
</td></tr></table></div>
<p>こういうことができるので、
例えば、$1はいらないけど$2や$3を配列に入れたいという場合、
それぞれ <tt class="docutils literal"><span class="pre">f[2],</span> <span class="pre">f[3]</span></tt> に入れてやればよいということになります。</p>
<p>　他の言語では配列と連想配列は区別されることが多いのですが、
AWKでは実装上も表記上も区別がありません。気軽に使える一方、
連想配列なので、あまり速度は期待できません。</p>
<p>　二次元配列は、次のようにインデックスをカンマで区切って表記します。
もちろん数字も使うことができます。リスト8に使用例を示します。</p>
<ul class="simple">
<li>リスト8: 二次元配列の使用例</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat hoge.sh
<span class="c">#!/bin/bash</span>

<span class="nb">echo</span> <span class="nv">$1</span> <span class="nv">$2</span> |
awk <span class="s1">&#39;BEGIN{</span>
<span class="s1"> a[&quot;グー&quot;,&quot;チョキ&quot;] = &quot;グー&quot;;</span>
<span class="s1"> a[&quot;パー&quot;,&quot;チョキ&quot;] = &quot;チョキ&quot;;</span>
<span class="s1"> （略）</span>
<span class="s1"> }</span>
<span class="s1"> END{print a[$1,$2] &quot;の勝ち&quot;}&#39;</span>
uedamac:201304 ueda<span class="nv">$ </span>./hoge.sh パー チョキ
チョキの勝ち
</pre></div>
</td></tr></table></div>
<p>　察しのよい人にはお分かりかもしれませんが、
この配列は実際にはC言語の二次元配列とは全く異なるものです。
AWKではインデックスを全部連結した文字列をキーにして、
一つの連想配列に記録しているようです。
もちろん、文字列の連結は、 <tt class="docutils literal"><span class="pre">12,3</span></tt> と <tt class="docutils literal"><span class="pre">1,23</span></tt>
が区別できるように行われます。
ここらへんの仕様は、
いかにもLL (lightweight language) の元祖らしい潔さです。</p>
</div>
</div>
<div class="section" id="id6">
<h2>16.3. AWK 多めのシェルスクリプトで画像処理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　では、ここから本題です。
今回もjpeg等の画像をアスキー形式のppm画像に変換し、処理します。
ImageMagickのインストールをお願いします。</p>
<p>前号でも説明しましたが、アスキー形式のppm画像は、
スペースか改行区切りで数字の並んだテキストファイルです。
リスト9に例を示します。
最初のP3が画像の形式、次の二つが画像のサイズ、
次いで画素値の刻み幅（深さ）です。
その後、左から右、上から下の画素に向けて
r（赤）、g（緑）、b（青）の値が並びます。</p>
<ul class="simple">
<li>リスト9: ppm画像をheadした例</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head 1.ppm
P3 &lt;- 画像のタイプ
<span class="c">#* &lt;- コメント</span>
960 640 &lt;- 画像の幅、高さ
255 &lt;- 深さ
125 94 50 126 95 51 127 96 52 128 97 53 128 97 53...
</pre></div>
</td></tr></table></div>
<div class="section" id="id7">
<h3>16.3.1. パターンを使って画素を配列に記録<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず、画像をAWKの配列に記録するまでのコードをリスト10に示します。
6行目で、画像（ <tt class="docutils literal"><span class="pre">$1</span></tt> に指定する）をppm画像に直しています。
12〜15行目でppm画像を読み込み、データを縦一列に並べ、
中間ファイルに落としています。
18〜20行目でヘッダ部分（幅、高さ、深さ）を変数に落とした後、
23行目以降で画像の本体部分の数字をAWKに入力しています。</p>
<ul class="simple">
<li>リスト10: AWKの配列にRGBの値を入れるまで</li>
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
28
29
30</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat donothing.sh
<span class="c">#!/bin/bash -xv</span>

<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

<span class="c">### 画像の変換</span>
convert -compress none <span class="s2">&quot;$1&quot;</span> <span class="nv">$tmp</span>-i.ppm

<span class="c">### データを縦一列に並べる</span>

<span class="c">#コメント除去</span>
sed <span class="s1">&#39;s/#.*$//&#39;</span> <span class="nv">$tmp</span>-i.ppm |
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |
<span class="c">#空行を除去</span>
awk <span class="s1">&#39;NF==1&#39;</span> &gt; <span class="nv">$tmp</span>-ppm

<span class="c">### ヘッダ情報取り出し</span>
<span class="nv">W</span><span class="o">=</span><span class="k">$(</span>head -n 2 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span>
<span class="nv">H</span><span class="o">=</span><span class="k">$(</span>head -n 3 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span>
<span class="nv">D</span><span class="o">=</span><span class="k">$(</span>head -n 4 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span>

<span class="c">### 画素の値を配列に</span>
tail -n +5 <span class="nv">$tmp</span>-ppm |
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span>
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}&#39;</span>

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　AWKに書いてあるパターンは三つで、
上から順にそれぞれr, g, bの値を二次元配列に代入しています。
パイプから流れてくる数字は、1行目にr、2行目にg、3行目にb、
というように3個毎に値が並んでいるので、
rgbそれぞれをフィルタしたければリスト10のように、
<tt class="docutils literal"><span class="pre">NR</span></tt> （行番号）を3で割った余りで判定すればよいことになります。</p>
<p>　各フィルタに対応するアクションでは、
行番号から画像での横位置、縦位置を求めて配列に値を代入しています。
横位置は左側から <tt class="docutils literal"><span class="pre">0,1,2,...</span></tt> 、
縦位置は上側から <tt class="docutils literal"><span class="pre">0,1,2,...</span></tt> と数えることとしました。
AWKの掟に反してゼロから数えていますが、
<tt class="docutils literal"><span class="pre">n%w</span></tt> と <tt class="docutils literal"><span class="pre">int(n/w)</span></tt>
に1を足すのは面倒なのでこのようにしています。</p>
</div>
<div class="section" id="id8">
<h3>16.3.2. 光を発射<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　後は、これに自分のやりたい処理を実装するだけです。
・・・と言ってもこれは画像処理の本を買ってくるか
ウェブで調べるかしないとチンプンカンプンな人もいるかと思います。
ここでは二つほど例を見せます。</p>
<p>　まず、画像の位置を使った処理の例です。
図1のサンプル画像はUSP友の会の勇壮なLL写真です。
見えないかと思いますが、後ろの男（注：私です。）
は手にビール瓶を持っています。
ビール瓶からフラッシュを出してみましょう。</p>
<ul class="simple">
<li>図1: 加工する画像（1.jpg）</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="1.jpg"><img alt="_images/1.jpg" src="1.jpg" style="width: 40%;" /></a>
</div>
<p>　図2に仕上がり、リスト11に、
この処理を行うAWKの部分を示します。
配列に値を読み込む部分まではリスト10と一緒で、
新たにENDパターンに対する処理と、
関数を一つ追加しています。
このシェルスクリプトの名前は <tt class="docutils literal"><span class="pre">flash.sh</span></tt>
で、リスト12のように使ってjpg画像を得ました。</p>
<ul class="simple">
<li>図2: ビール瓶の先から光線を出す</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="flash.jpg"><img alt="flash.jpg" src="flash.jpg" style="width: 40%;" /></a>
</div>
<ul class="simple">
<li>リスト11: ビール瓶の先から光を出すためのAWK</li>
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">### ビール瓶の先から国民に光を与える</span>
tail -n +5 <span class="nv">$tmp</span>-ppm |
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span>
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}</span>
<span class="s1"> END{</span>
<span class="s1"> print &quot;P3&quot;,w,h,d;</span>
<span class="s1"> for(y=0;y&lt;h;y++){</span>
<span class="s1"> for(x=0;x&lt;w;x++){</span>
<span class="s1"> ex = x - w*0.87;</span>
<span class="s1"> ey = y - h*0.32;</span>
<span class="s1"> deg = atan2(ey,ex)*360/3.141592 + 360;</span>
<span class="s1"> weight = (int(deg/15)%2) ? 1 : 4;</span>

<span class="s1"> p(r[x,y]*weight);</span>
<span class="s1"> p(g[x,y]*weight);</span>
<span class="s1"> p(b[x,y]);</span>
<span class="s1"> }</span>
<span class="s1"> }</span>
<span class="s1"> }</span>
<span class="s1"> function p(n){ print (n&gt;d)?d:n }&#39;</span>
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>リスト12: 画像を加工するシェル操作</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./flash.sh 1.jpg &gt; flash.ppm
<span class="nv">$ </span>convert flash.ppm flash.jpg
</pre></div>
</td></tr></table></div>
<p>　リスト11のENDパターンでは、
まず8行目でppm画像のヘッダ部分を出力しています。
その後の二重の <tt class="docutils literal"><span class="pre">for</span></tt> 文で、
1画素ずつ、r, g, bの順番に値を加工して出力しています。</p>
<p>　 <tt class="docutils literal"><span class="pre">for</span></tt> のループ内では、まず11, 12行目で、
その画素が光を出す中心の画素に対してどの位置にあるかを求めています。
中心の画素は、私が手で調べてハードコーディングしました。
変数にしてもよいですね。</p>
<p>　その後、13行目で、「その画素が光を出す中心に対してどの方角にあるか」
を求めています。 <tt class="docutils literal"><span class="pre">atan2</span></tt> はC言語にもある関数ですが、
見たことが無い人もいるかもしれません。
図3のように角度を返す関数です。
<tt class="docutils literal"><span class="pre">atan2</span></tt> の返した値を <tt class="docutils literal"><span class="pre">π</span></tt> で割って360をかけると、
いわゆる普通の角度（degree）になります。</p>
<ul class="simple">
<li>図3: atan2(y,x)の返す角度</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="atan2.png"><img alt="_images/atan2.png" src="atan2.png" style="width: 40%;" /></a>
</div>
<p>　ところで、 <tt class="docutils literal"><span class="pre">(x,y)</span> <span class="pre">=</span> <span class="pre">(0,0)</span></tt> だと <tt class="docutils literal"><span class="pre">atan2</span></tt>
が何を返すか不安ですが、AWKですので、</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{print atan2(0,0)}&#39;</span>
0
</pre></div>
</td></tr></table></div>
<p>のように実用的な値を返してくれます。
（注：全部のバージョンのAWKに当てはまるかは未調査です。）</p>
<p>　14行目では、角度15度刻みで <tt class="docutils literal"><span class="pre">weight</span></tt> という変数の値を
1にしたり4にしたりしています。
完成した画像をよく見ると15度刻みで光っていますが、
この準備です。
細かい話ですが、 <tt class="docutils literal"><span class="pre">atan2</span></tt> が返す値がプラスの場合と
マイナスの場合がある影響で360度きれいに15度刻みにならないので、
13行目で360を足して、 <tt class="docutils literal"><span class="pre">deg</span></tt> の値がプラスになるようにしています。</p>
<p>　これでいよいよ標準出力に値を出していきます（16〜18行目）。
白黒で分かりにくいですが、金色（黄色）に光らせたいので、
rとgの値に <tt class="docutils literal"><span class="pre">weight</span></tt> をかけて強調します。
<tt class="docutils literal"><span class="pre">p</span></tt> という関数は22行目で実装しており、
値が最大値 <tt class="docutils literal"><span class="pre">d</span></tt> を超えると <tt class="docutils literal"><span class="pre">d</span></tt> で打ち切って出力するというものです。
ところで、AWKの変数は基本的にすべてグローバル変数なので、
オプションで定義された <tt class="docutils literal"><span class="pre">d</span></tt> は、関数の中でも使えます。
長いプログラミングをするとちょっと辛いかなと、個人的には思います。</p>
</div>
<div class="section" id="id9">
<h3>16.3.3. エンボス加工する<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　もう一つ例をリスト13に示します。
これは、エンボス加工風に画像を変換する処理です。
図4に、処理前後の画像を示します。
このようなアイコンの処理だけでなく、
写真を処理すると絵画のような風合いになります。
<cite>http://www.usptomo.com/PAGE=20130113IMAGE</cite>
で公開していますので、遊んでみてください。</p>
<ul class="simple">
<li>リスト13: エンボス加工処理</li>
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
13</pre></div></td><td class="code"><div class="highlight"><pre>tail -n +5 <span class="nv">$tmp</span>-ppm |
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span>
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span>
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}</span>
<span class="s1"> END{print &quot;P3&quot;,w-2,h-2,d;</span>
<span class="s1"> for(y=1;y&lt;h-1;y++){</span>
<span class="s1"> for(x=1;x&lt;w-1;x++){</span>
<span class="s1"> a = 2*g[x-1,y-1] + g[x-1,y] + g[x,y-1] - g[x,y+1] - g[x+1,y] - 2*g[x+1,y+1];</span>
<span class="s1"> p(r[x,y] - a); p(g[x,y] - a); p(b[x,y] - a);</span>
<span class="s1"> }</span>
<span class="s1"> }}</span>
<span class="s1"> function p(v){print (v &lt; 0) ? 0 : (v &gt; d ? d : v)}&#39;</span>
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>図4: エンボス加工前後の画像</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="CHINJYU.jpg"><img alt="_images/CHINJYU.JPG" src="CHINJYU.jpg" style="width: 40%;" /></a>
</div>
<div class="figure">
<a class="reference internal image-reference" href="enbos.chinjyu.jpg"><img alt="_images/enbos.chinjyu.jpg" src="enbos.chinjyu.jpg" style="width: 40%;" /></a>
</div>
<p>　リスト13の処理では、まず変数 <tt class="docutils literal"><span class="pre">a</span></tt> に、
ある画素とその周囲の画素のg値を比較した値を代入しています。
この処理は「sobelフィルタ」と言われるもので、
この演算だと、画像の斜め方向で緑色が急激に変わっている画素の
<tt class="docutils literal"><span class="pre">a</span></tt> の値が正、あるいは負の方向に大きくなります。
図5に、 <tt class="docutils literal"><span class="pre">a</span></tt> の値でグレースケール画像を作ったものを示します。
本当はgだけでなく、r,g,bの値で平均値をとって <tt class="docutils literal"><span class="pre">a</span></tt>
の値を求めるべきですが、コードがややこしくなるので緑だけにしています。</p>
<ul class="simple">
<li>図5: <tt class="docutils literal"><span class="pre">a</span></tt> の値で画像を作ったもの</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="chinjyu.edge_.jpg"><img alt="_images/chinjyu.edge.jpg" src="chinjyu.edge_.jpg" style="width: 40%;" /></a>
</div>
<p>　この <tt class="docutils literal"><span class="pre">a</span></tt> の値を、10行目のように各rgb値から引くと、
色の変化の急激なところが強調されて、
人間の目には画像に凹凸があるように見えます。</p>
</div>
</div>
<div class="section" id="id10">
<h2>16.4. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、シェルスクリプト（ただしAWK多め）で画像処理をしてみました。
筆者は遊びのつもりで始めましたが、
テキストにすると処理の流れが分かりやすいので、
これは画像処理の教育用によいかもしれません。</p>
<p>　今回はAWKの説明を充実させました。
パターンや配列、関数の書き方などを説明しました。
特徴的なのはパターンの存在そのものと、あとは配列の実装でしょう。
パターンをたくさん並べてプログラミングをすると、
「一行ずつ読み込み、パターンで振り分けて何かする」
という、他の言語との違いが際立ちます。
この動作はシェルスクリプトで使う他のコマンドと似ており、
やはり相性という点でAWKとシェルスクリプトは切っても切れない縁があります。
逆に言えば、AWKが使いこなせることが、
シェルスクリプトでなんでもやろうという発想にもつながります。</p>
<p>　次回は作り物を一旦お休みして、
「コマンドでどうしてもできないややこしい処理」
を1行AWKで処理する方法を扱いたいと思います。</p>
</div>
</div>
