# 開眼シェルスクリプト2013年4月号
出典: 技術評論社SoftwareDesign<br />
 <br />
 <div class="section" id="id1"><br />
<h1>16. 開眼シェルスクリプト 第16回画像処理で遊ぶ（２）<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　今回は前回に引き続き、シェルスクリプトで画像処理をして遊んでみましょう。<br />
前回はコマンドで扱いやすくするために、<br />
カラー画像を1ピクセル1レコードにしてから処理しました。<br />
ただこの方法だけだとできることが限られるので、<br />
今回は、awkをフルに使って画像処理をやってみます。<br />
配列を操作するので、本連載史上、最も「普通の」プログラミングをやります。<br />
そうは言っても、普通ではありませんが・・・。<br />
しかし、この人もこんなことを言っているのでよいということにしましょう。<br />
（注：完全に言い訳に使っています。）</p><br />
<p>『人生を楽しむ秘訣は普通にこだわらないこと。<br />
普通と言われる人生を送る人間なんて、<br />
一人としていやしない。いたらお目にかかりたいものだ』<br />
&#8212; アルバート・アインシュタイン</p><br />
<div class="section" id="id2"><br />
<h2>16.1. 環境<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、12年間親しんだThinkPadからMacBookAirに乗り換えたことを記念して、<br />
Mac上のbashでコーディングします。なぜ乗り換えたかというと、<br />
2月号の特集で「Macにはbashが入っているからターミナル使って欲しい」と書いた時に、<br />
自分が率先しないといかん、と使命感に駆られたからです。<br />
シャレ乙野郎になろうという気は毛頭ありません。<br />
が、もともとカフェ中毒者なので「ドヤ顔mac」とか言われても仕方ありません。<br />
言う側（言ってたのか）から言われる側になって辛いですが、<br />
今月号からしばらくはMacでいきます。</p><br />
<ul class="simple"><br />
<li>リスト1: 環境等</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.2.1 Darwin Kernel Version 12.2.1:<br />
Thu Oct 18 16:32:48 PDT 2012; root:xnu-2050.20.9~2/RELEASE_X86_64 x86_64<br />
<span class="nv">$ </span>bash --version<br />
GNU bash, version 3.2.48<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>x86_64-apple-darwin12<span class="o">)</span><br />
Copyright <span class="o">(</span>C<span class="o">)</span> 2007 Free Software Foundation, Inc.<br />
<span class="nv">$ </span>awk --version<br />
awk version 20070501<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト1に、今回の環境を示します。<br />
多くのLinuxディストリビューションと違って、<br />
<tt class="docutils literal"><span class="pre">awk</span></tt> は <tt class="docutils literal"><span class="pre">gawk</span></tt> ではないので注意が必要ですが、<br />
今回の内容では出力の違いはありません。</p><br />
</div><br />
<div class="section" id="awk"><br />
<h2>16.2. AWKのおさらい<a class="headerlink" href="#awk" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="id3"><br />
<h3>16.2.1. パターン<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　「パターン」は、これまで何度も使っていたとおり、<br />
入力されたファイルから条件に合う行を抽出するためのものです。<br />
パターンは <tt class="docutils literal"><span class="pre">grep</span></tt> の機能を担っていると考えてよいでしょう。<br />
<tt class="docutils literal"><span class="pre">grep</span></tt> は抽出だけですが、AWKは抽出した行に対して<br />
「アクション」で演算ができます。</p><br />
<p>　リスト2の例は、パターンで偶数を抽出して、<br />
アクションで10で割るというものです。<br />
<tt class="docutils literal"><span class="pre">jot</span> <span class="pre">10</span></tt> の出力は、 <tt class="docutils literal"><span class="pre">seq</span> <span class="pre">1</span> <span class="pre">10</span></tt> のものと同じです。</p><br />
<ul class="simple"><br />
<li>リスト2: パターンとアクションの例</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>jot 10 | awk <span class="s1">&#39;$1%2==0{print $1/10}&#39;</span><br />
0.2<br />
0.4<br />
0.6<br />
0.8<br />
1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　パターンとアクションの組みは、いくつも書くことができます。<br />
リスト3のコードはAWKのプログラムで、偶数と奇数を数えるものです。<br />
パターンは、「START」、「END」も含めて4個ですね。<br />
紙面の関係と一行野郎中毒が祟って1行1パターンにしましたが、<br />
Cのように改行・インデントをする方がAWKのスクリプトとしてはまともでしょう。</p><br />
<ul class="simple"><br />
<li>リスト3: パターンを並べたAWKのコードの例</li><br />
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
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat oddeven.awk<br />
<span class="c">#!/usr/bin/awk -f</span><br />
<br />
START<span class="o">{</span><span class="nv">even</span><span class="o">=</span>0;odd<span class="o">=</span>0<span class="o">}</span><br />
<span class="nv">$1</span>%2<span class="o">==</span>0<span class="o">{</span>even++<span class="o">}</span><br />
<span class="nv">$1</span>%2<span class="o">==</span>1<span class="o">{</span>odd++<span class="o">}</span><br />
END<span class="o">{</span>print <span class="s2">&quot;奇数:&quot;</span>,odd;print <span class="s2">&quot;偶数:&quot;</span>,even<span class="o">}</span><br />
<span class="nv">$ </span>jot 9 | ./oddeven.awk<br />
奇数: 5<br />
偶数: 4<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　一つの行が複数のパターンにマッチする時は、リスト4のように、<br />
パターンに書いた順に何回も出力されます。<br />
この辺の挙動は、単なるif文とは違うので注意が必要です。</p><br />
<ul class="simple"><br />
<li>リスト4: 複数のパターンにマッチする場合</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo </span>1 | awk <span class="s1">&#39;{print $1,&quot;a&quot;}NR==1{print $1,&quot;b&quot;}NR!=2{print $1,&quot;c&quot;}&#39;</span><br />
1 a<br />
1 b<br />
1 c<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id4"><br />
<h3>16.2.2. 関数<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　関数の書き方はjavascriptに似ています。<br />
<tt class="docutils literal"><span class="pre">function</span> <span class="pre">名前(変数,...){文;文;...}</span></tt><br />
というように表記します。<br />
リスト5は、関数の名前の書き方と使い方の例です。</p><br />
<ul class="simple"><br />
<li>リスト5: 関数の書き方</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat func.sh<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">echo</span> <span class="nv">$1</span> |<br />
awk <span class="s1">&#39;{print scream($1,10)}</span><br />
<span class="s1"> function scream(a,n){return n==1?a:(scream(a,n-1) a)}&#39;</span><br />
<span class="nv">$ </span>./func.sh あ<br />
ああああああああああ<br />
</pre></div><br />
</td></tr></table></div><br />
<p>わざと再帰を使ってややこしくしており、<br />
例としてはちょっと不適切かもしれませんが、<br />
<tt class="docutils literal"><span class="pre">function</span></tt> の行が関数になっています。<br />
この例のように、関数は使う場所より後ろに書いても大丈夫です。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h3>16.2.3. 配列<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　AWKは言語なのでもちろん配列があります。<br />
AWKの配列は、連想配列として実装されています。<br />
ですので、リスト6のような使い方ができます。</p><br />
<ul class="simple"><br />
<li>リスト6: 配列の使い方</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{a[&quot;猫&quot;]=&quot;まっしぐら&quot;;print a[&quot;猫&quot;]}&#39;</span><br />
まっしぐら<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　もちろん、普通の配列としても使えます。<br />
配列として使うときは、リスト6のように、<br />
インデックスを0からではなく1から始めます。<br />
自身で使うときは0からでも動きますが、<br />
関数が配列を返すときは1に最初の要素が入っているので、<br />
他に理由がなければ合わせましょう。</p><br />
<ul class="simple"><br />
<li>リスト6: 配列の使い方その２</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">echo</span> 南海 ホークス | awk <span class="s1">&#39;{\\</span><br />
<span class="s1"> a[1]=$1;a[2]=$2;for(i=1;i&lt;=2;i++){print a[i]}}&#39;</span><br />
南海<br />
ホークス<br />
//split関数で文字列を切って配列aに代入<br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="s1">&#39;OH!MY!GOD!&#39;</span> | awk <span class="s1">&#39;{split($1,a,&quot;!&quot;);print a[2]}&#39;</span><br />
MY<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　表記に区別がないので、リスト7のようなこともできます。<br />
Cでやったら間違いなく怒られますが大丈夫です。</p><br />
<ul class="simple"><br />
<li>リスト7: インデックスが大きくても大丈夫</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{a[123456789]=10;print a[123456789]}&#39;</span><br />
10<br />
</pre></div><br />
</td></tr></table></div><br />
<p>こういうことができるので、<br />
例えば、$1はいらないけど$2や$3を配列に入れたいという場合、<br />
それぞれ <tt class="docutils literal"><span class="pre">f[2],</span> <span class="pre">f[3]</span></tt> に入れてやればよいということになります。</p><br />
<p>　他の言語では配列と連想配列は区別されることが多いのですが、<br />
AWKでは実装上も表記上も区別がありません。気軽に使える一方、<br />
連想配列なので、あまり速度は期待できません。</p><br />
<p>　二次元配列は、次のようにインデックスをカンマで区切って表記します。<br />
もちろん数字も使うことができます。リスト8に使用例を示します。</p><br />
<ul class="simple"><br />
<li>リスト8: 二次元配列の使用例</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat hoge.sh<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nb">echo</span> <span class="nv">$1</span> <span class="nv">$2</span> |<br />
awk <span class="s1">&#39;BEGIN{</span><br />
<span class="s1"> a[&quot;グー&quot;,&quot;チョキ&quot;] = &quot;グー&quot;;</span><br />
<span class="s1"> a[&quot;パー&quot;,&quot;チョキ&quot;] = &quot;チョキ&quot;;</span><br />
<span class="s1"> （略）</span><br />
<span class="s1"> }</span><br />
<span class="s1"> END{print a[$1,$2] &quot;の勝ち&quot;}&#39;</span><br />
uedamac:201304 ueda<span class="nv">$ </span>./hoge.sh パー チョキ<br />
チョキの勝ち<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　察しのよい人にはお分かりかもしれませんが、<br />
この配列は実際にはC言語の二次元配列とは全く異なるものです。<br />
AWKではインデックスを全部連結した文字列をキーにして、<br />
一つの連想配列に記録しているようです。<br />
もちろん、文字列の連結は、 <tt class="docutils literal"><span class="pre">12,3</span></tt> と <tt class="docutils literal"><span class="pre">1,23</span></tt><br />
が区別できるように行われます。<br />
ここらへんの仕様は、<br />
いかにもLL (lightweight language) の元祖らしい潔さです。</p><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>16.3. AWK 多めのシェルスクリプトで画像処理<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　では、ここから本題です。<br />
今回もjpeg等の画像をアスキー形式のppm画像に変換し、処理します。<br />
ImageMagickのインストールをお願いします。</p><br />
<p>前号でも説明しましたが、アスキー形式のppm画像は、<br />
スペースか改行区切りで数字の並んだテキストファイルです。<br />
リスト9に例を示します。<br />
最初のP3が画像の形式、次の二つが画像のサイズ、<br />
次いで画素値の刻み幅（深さ）です。<br />
その後、左から右、上から下の画素に向けて<br />
r（赤）、g（緑）、b（青）の値が並びます。</p><br />
<ul class="simple"><br />
<li>リスト9: ppm画像をheadした例</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>head 1.ppm<br />
P3 &lt;- 画像のタイプ<br />
<span class="c">#* &lt;- コメント</span><br />
960 640 &lt;- 画像の幅、高さ<br />
255 &lt;- 深さ<br />
125 94 50 126 95 51 127 96 52 128 97 53 128 97 53...<br />
</pre></div><br />
</td></tr></table></div><br />
<div class="section" id="id7"><br />
<h3>16.3.1. パターンを使って画素を配列に記録<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず、画像をAWKの配列に記録するまでのコードをリスト10に示します。<br />
6行目で、画像（ <tt class="docutils literal"><span class="pre">$1</span></tt> に指定する）をppm画像に直しています。<br />
12〜15行目でppm画像を読み込み、データを縦一列に並べ、<br />
中間ファイルに落としています。<br />
18〜20行目でヘッダ部分（幅、高さ、深さ）を変数に落とした後、<br />
23行目以降で画像の本体部分の数字をAWKに入力しています。</p><br />
<ul class="simple"><br />
<li>リスト10: AWKの配列にRGBの値を入れるまで</li><br />
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
28<br />
29<br />
30</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat donothing.sh<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
<span class="c">### 画像の変換</span><br />
convert -compress none <span class="s2">&quot;$1&quot;</span> <span class="nv">$tmp</span>-i.ppm<br />
<br />
<span class="c">### データを縦一列に並べる</span><br />
<br />
<span class="c">#コメント除去</span><br />
sed <span class="s1">&#39;s/#.*$//&#39;</span> <span class="nv">$tmp</span>-i.ppm |<br />
tr <span class="s1">&#39; &#39;</span> <span class="s1">&#39;\\n&#39;</span> |<br />
<span class="c">#空行を除去</span><br />
awk <span class="s1">&#39;NF==1&#39;</span> &gt; <span class="nv">$tmp</span>-ppm<br />
<br />
<span class="c">### ヘッダ情報取り出し</span><br />
<span class="nv">W</span><span class="o">=</span><span class="k">$(</span>head -n 2 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span><br />
<span class="nv">H</span><span class="o">=</span><span class="k">$(</span>head -n 3 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span><br />
<span class="nv">D</span><span class="o">=</span><span class="k">$(</span>head -n 4 <span class="nv">$tmp</span>-ppm | tail -n 1<span class="k">)</span><br />
<br />
<span class="c">### 画素の値を配列に</span><br />
tail -n +5 <span class="nv">$tmp</span>-ppm |<br />
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span><br />
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}&#39;</span><br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　AWKに書いてあるパターンは三つで、<br />
上から順にそれぞれr, g, bの値を二次元配列に代入しています。<br />
パイプから流れてくる数字は、1行目にr、2行目にg、3行目にb、<br />
というように3個毎に値が並んでいるので、<br />
rgbそれぞれをフィルタしたければリスト10のように、<br />
<tt class="docutils literal"><span class="pre">NR</span></tt> （行番号）を3で割った余りで判定すればよいことになります。</p><br />
<p>　各フィルタに対応するアクションでは、<br />
行番号から画像での横位置、縦位置を求めて配列に値を代入しています。<br />
横位置は左側から <tt class="docutils literal"><span class="pre">0,1,2,...</span></tt> 、<br />
縦位置は上側から <tt class="docutils literal"><span class="pre">0,1,2,...</span></tt> と数えることとしました。<br />
AWKの掟に反してゼロから数えていますが、<br />
<tt class="docutils literal"><span class="pre">n%w</span></tt> と <tt class="docutils literal"><span class="pre">int(n/w)</span></tt><br />
に1を足すのは面倒なのでこのようにしています。</p><br />
</div><br />
<div class="section" id="id8"><br />
<h3>16.3.2. 光を発射<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　後は、これに自分のやりたい処理を実装するだけです。<br />
・・・と言ってもこれは画像処理の本を買ってくるか<br />
ウェブで調べるかしないとチンプンカンプンな人もいるかと思います。<br />
ここでは二つほど例を見せます。</p><br />
<p>　まず、画像の位置を使った処理の例です。<br />
図1のサンプル画像はUSP友の会の勇壮なLL写真です。<br />
見えないかと思いますが、後ろの男（注：私です。）<br />
は手にビール瓶を持っています。<br />
ビール瓶からフラッシュを出してみましょう。</p><br />
<ul class="simple"><br />
<li>図1: 加工する画像（1.jpg）</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="1.jpg"><img alt="_images/1.jpg" src="1.jpg" style="width: 40%;" /></a><br />
</div><br />
<p>　図2に仕上がり、リスト11に、<br />
この処理を行うAWKの部分を示します。<br />
配列に値を読み込む部分まではリスト10と一緒で、<br />
新たにENDパターンに対する処理と、<br />
関数を一つ追加しています。<br />
このシェルスクリプトの名前は <tt class="docutils literal"><span class="pre">flash.sh</span></tt><br />
で、リスト12のように使ってjpg画像を得ました。</p><br />
<ul class="simple"><br />
<li>図2: ビール瓶の先から光線を出す</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="flash.jpg"><img alt="flash.jpg" src="flash.jpg" style="width: 40%;" /></a><br />
</div><br />
<ul class="simple"><br />
<li>リスト11: ビール瓶の先から光を出すためのAWK</li><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">### ビール瓶の先から国民に光を与える</span><br />
tail -n +5 <span class="nv">$tmp</span>-ppm |<br />
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span><br />
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> END{</span><br />
<span class="s1"> print &quot;P3&quot;,w,h,d;</span><br />
<span class="s1"> for(y=0;y&lt;h;y++){</span><br />
<span class="s1"> for(x=0;x&lt;w;x++){</span><br />
<span class="s1"> ex = x - w*0.87;</span><br />
<span class="s1"> ey = y - h*0.32;</span><br />
<span class="s1"> deg = atan2(ey,ex)*360/3.141592 + 360;</span><br />
<span class="s1"> weight = (int(deg/15)%2) ? 1 : 4;</span><br />
<br />
<span class="s1"> p(r[x,y]*weight);</span><br />
<span class="s1"> p(g[x,y]*weight);</span><br />
<span class="s1"> p(b[x,y]);</span><br />
<span class="s1"> }</span><br />
<span class="s1"> }</span><br />
<span class="s1"> }</span><br />
<span class="s1"> function p(n){ print (n&gt;d)?d:n }&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>リスト12: 画像を加工するシェル操作</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./flash.sh 1.jpg &gt; flash.ppm<br />
<span class="nv">$ </span>convert flash.ppm flash.jpg<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト11のENDパターンでは、<br />
まず8行目でppm画像のヘッダ部分を出力しています。<br />
その後の二重の <tt class="docutils literal"><span class="pre">for</span></tt> 文で、<br />
1画素ずつ、r, g, bの順番に値を加工して出力しています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">for</span></tt> のループ内では、まず11, 12行目で、<br />
その画素が光を出す中心の画素に対してどの位置にあるかを求めています。<br />
中心の画素は、私が手で調べてハードコーディングしました。<br />
変数にしてもよいですね。</p><br />
<p>　その後、13行目で、「その画素が光を出す中心に対してどの方角にあるか」<br />
を求めています。 <tt class="docutils literal"><span class="pre">atan2</span></tt> はC言語にもある関数ですが、<br />
見たことが無い人もいるかもしれません。<br />
図3のように角度を返す関数です。<br />
<tt class="docutils literal"><span class="pre">atan2</span></tt> の返した値を <tt class="docutils literal"><span class="pre">π</span></tt> で割って360をかけると、<br />
いわゆる普通の角度（degree）になります。</p><br />
<ul class="simple"><br />
<li>図3: atan2(y,x)の返す角度</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="atan2.png"><img alt="_images/atan2.png" src="atan2.png" style="width: 40%;" /></a><br />
</div><br />
<p>　ところで、 <tt class="docutils literal"><span class="pre">(x,y)</span> <span class="pre">=</span> <span class="pre">(0,0)</span></tt> だと <tt class="docutils literal"><span class="pre">atan2</span></tt><br />
が何を返すか不安ですが、AWKですので、</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>awk <span class="s1">&#39;BEGIN{print atan2(0,0)}&#39;</span><br />
0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>のように実用的な値を返してくれます。<br />
（注：全部のバージョンのAWKに当てはまるかは未調査です。）</p><br />
<p>　14行目では、角度15度刻みで <tt class="docutils literal"><span class="pre">weight</span></tt> という変数の値を<br />
1にしたり4にしたりしています。<br />
完成した画像をよく見ると15度刻みで光っていますが、<br />
この準備です。<br />
細かい話ですが、 <tt class="docutils literal"><span class="pre">atan2</span></tt> が返す値がプラスの場合と<br />
マイナスの場合がある影響で360度きれいに15度刻みにならないので、<br />
13行目で360を足して、 <tt class="docutils literal"><span class="pre">deg</span></tt> の値がプラスになるようにしています。</p><br />
<p>　これでいよいよ標準出力に値を出していきます（16〜18行目）。<br />
白黒で分かりにくいですが、金色（黄色）に光らせたいので、<br />
rとgの値に <tt class="docutils literal"><span class="pre">weight</span></tt> をかけて強調します。<br />
<tt class="docutils literal"><span class="pre">p</span></tt> という関数は22行目で実装しており、<br />
値が最大値 <tt class="docutils literal"><span class="pre">d</span></tt> を超えると <tt class="docutils literal"><span class="pre">d</span></tt> で打ち切って出力するというものです。<br />
ところで、AWKの変数は基本的にすべてグローバル変数なので、<br />
オプションで定義された <tt class="docutils literal"><span class="pre">d</span></tt> は、関数の中でも使えます。<br />
長いプログラミングをするとちょっと辛いかなと、個人的には思います。</p><br />
</div><br />
<div class="section" id="id9"><br />
<h3>16.3.3. エンボス加工する<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　もう一つ例をリスト13に示します。<br />
これは、エンボス加工風に画像を変換する処理です。<br />
図4に、処理前後の画像を示します。<br />
このようなアイコンの処理だけでなく、<br />
写真を処理すると絵画のような風合いになります。<br />
<cite>http://www.usptomo.com/PAGE=20130113IMAGE</cite><br />
で公開していますので、遊んでみてください。</p><br />
<ul class="simple"><br />
<li>リスト13: エンボス加工処理</li><br />
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
13</pre></div></td><td class="code"><div class="highlight"><pre>tail -n +5 <span class="nv">$tmp</span>-ppm |<br />
awk -v <span class="nv">w</span><span class="o">=</span><span class="nv">$W</span> -v <span class="nv">h</span><span class="o">=</span><span class="nv">$H</span> -v <span class="nv">d</span><span class="o">=</span><span class="nv">$D</span> <span class="se">\\</span><br />
 <span class="s1">&#39;NR%3==1{n=(NR-1)/3;r[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==2{n=(NR-2)/3;g[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> NR%3==0{n=(NR-3)/3;b[n%w,int(n/w)] = $1}</span><br />
<span class="s1"> END{print &quot;P3&quot;,w-2,h-2,d;</span><br />
<span class="s1"> for(y=1;y&lt;h-1;y++){</span><br />
<span class="s1"> for(x=1;x&lt;w-1;x++){</span><br />
<span class="s1"> a = 2*g[x-1,y-1] + g[x-1,y] + g[x,y-1] - g[x,y+1] - g[x+1,y] - 2*g[x+1,y+1];</span><br />
<span class="s1"> p(r[x,y] - a); p(g[x,y] - a); p(b[x,y] - a);</span><br />
<span class="s1"> }</span><br />
<span class="s1"> }}</span><br />
<span class="s1"> function p(v){print (v &lt; 0) ? 0 : (v &gt; d ? d : v)}&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>図4: エンボス加工前後の画像</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="CHINJYU.jpg"><img alt="_images/CHINJYU.JPG" src="CHINJYU.jpg" style="width: 40%;" /></a><br />
</div><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="enbos.chinjyu.jpg"><img alt="_images/enbos.chinjyu.jpg" src="enbos.chinjyu.jpg" style="width: 40%;" /></a><br />
</div><br />
<p>　リスト13の処理では、まず変数 <tt class="docutils literal"><span class="pre">a</span></tt> に、<br />
ある画素とその周囲の画素のg値を比較した値を代入しています。<br />
この処理は「sobelフィルタ」と言われるもので、<br />
この演算だと、画像の斜め方向で緑色が急激に変わっている画素の<br />
<tt class="docutils literal"><span class="pre">a</span></tt> の値が正、あるいは負の方向に大きくなります。<br />
図5に、 <tt class="docutils literal"><span class="pre">a</span></tt> の値でグレースケール画像を作ったものを示します。<br />
本当はgだけでなく、r,g,bの値で平均値をとって <tt class="docutils literal"><span class="pre">a</span></tt><br />
の値を求めるべきですが、コードがややこしくなるので緑だけにしています。</p><br />
<ul class="simple"><br />
<li>図5: <tt class="docutils literal"><span class="pre">a</span></tt> の値で画像を作ったもの</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="chinjyu.edge_.jpg"><img alt="_images/chinjyu.edge.jpg" src="chinjyu.edge_.jpg" style="width: 40%;" /></a><br />
</div><br />
<p>　この <tt class="docutils literal"><span class="pre">a</span></tt> の値を、10行目のように各rgb値から引くと、<br />
色の変化の急激なところが強調されて、<br />
人間の目には画像に凹凸があるように見えます。</p><br />
</div><br />
</div><br />
<div class="section" id="id10"><br />
<h2>16.4. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、シェルスクリプト（ただしAWK多め）で画像処理をしてみました。<br />
筆者は遊びのつもりで始めましたが、<br />
テキストにすると処理の流れが分かりやすいので、<br />
これは画像処理の教育用によいかもしれません。</p><br />
<p>　今回はAWKの説明を充実させました。<br />
パターンや配列、関数の書き方などを説明しました。<br />
特徴的なのはパターンの存在そのものと、あとは配列の実装でしょう。<br />
パターンをたくさん並べてプログラミングをすると、<br />
「一行ずつ読み込み、パターンで振り分けて何かする」<br />
という、他の言語との違いが際立ちます。<br />
この動作はシェルスクリプトで使う他のコマンドと似ており、<br />
やはり相性という点でAWKとシェルスクリプトは切っても切れない縁があります。<br />
逆に言えば、AWKが使いこなせることが、<br />
シェルスクリプトでなんでもやろうという発想にもつながります。</p><br />
<p>　次回は作り物を一旦お休みして、<br />
「コマンドでどうしてもできないややこしい処理」<br />
を1行AWKで処理する方法を扱いたいと思います。</p><br />
</div><br />
</div>
