---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年5月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典：<a href="http://www.usp-lab.com/pub.magazine.html" target="_blank">USPマガジン2014年5月号</a>

2014年5月号:

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4904807073" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

<a href="/?page=02944">各号の一覧へ</a>

<h1>2. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1>
<p>産業技術大学院・USP研究所・USP友の会　上田隆一
（脚注：順に助教、アドバイザリーフェロー、会長）</p>
<blockquote>
<div>USP友の会のシェル芸勉強会（脚注：シェルのワンライナー勉強会）は、日々、他の言語からの他流試合に晒されているのである（脚注：Ruby, Perl, PowerShell等々。）。そこで上田は、Haskellで自ら他流試合を行い、さらにシェル芸勉強会をいじめる自傷行為に手を染めるのであった。</div></blockquote>
<div class="section" id="id1">

<h2>2.1. はじめに</h2>
<p>皆さん、やさぐれてますか？ブラックエンジェル上田ちゃんです。最近、超ネガティブです。なぜ、ネガティブか。それは喋らずに本題に行きます（脚注：生きていればいろんなことがあるじゃないですか。）。</p>
</div>
<div class="section" id="id2">

<h2>2.2. 前回の続き</h2>
<p>さて、前回はまだ第1回の1問目について、解答を作ったところでした。ちょっと重複して申し訳ないんですが、問題と解答を書いてから話を始めます。</p>

<ul class="simple">
<li>問題（第1回第1問）:（Linuxの） <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> から、</li>
</ul>
<p>ユーザ名を抽出したリストを作ってください。</p>
<blockquote>
<div>シェルのワンライナーだと以下のとおり。</div></blockquote>

<div class="highlight-none"><div class="highlight"><pre>ueda\@ubuntu:~$ cat /etc/passwd | awk &quot;-F:&quot; &#39;{print $1}&#39;
...
sshd
ueda
mysql
postfix
</pre></div>
</div>
<ul class="simple">
<li>解答例</li>
</ul>
<div class="highlight-none"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~$ cat q1_1.hs
main = getContents &gt;&gt;= putStr . main&#39;

main&#39; :: String -&gt; String
main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) ( lines cs )
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>実行</li>
</ul>
<div class="highlight-none"><div class="highlight"><pre>ueda\@remote:~$ ghc q1_1.hs
[1 of 1] Compiling Main ( q1_1.hs, q1_1.o )
Linking q1_1 ...
ueda\@remote:~$ cat /etc/passwd | ./q1_1
...
ueda
mysql
postfix
</pre></div>
</div>
<p>んで、前回は <tt class="docutils literal"><span class="pre">map</span></tt> とか <tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt>
を説明しようとして終わっていたのでした。</p>
</div>
<div class="section" id="map">
<h2>2.3. mapがないと困る</h2>
<p>まず <tt class="docutils literal"><span class="pre">map</span></tt> から。
Haskellの対話的インタプリタGHCiで調べると、
型はこんなもんだと分かります。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghci
Prelude&gt; :t map
map :: <span class="o">(</span>a -&gt; b<span class="o">)</span> -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>b<span class="o">]</span>
<span class="c">###GHCiを抜けるときはCtrl+d###</span>
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">map</span></tt> は、第一引数に型 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">b</span></tt> の <em>関数</em> 、
第二引数に型 <tt class="docutils literal"><span class="pre">a</span></tt> のリストを渡すと、型 <tt class="docutils literal"><span class="pre">b</span></tt> のリストを返すという意味になります。つまり、関数 <tt class="docutils literal"><span class="pre">map</span></tt> には別の関数とリストをひとつずつ指定して使います。
<tt class="docutils literal"><span class="pre">a</span></tt> とか <tt class="docutils literal"><span class="pre">b</span></tt> とかは、どんな型にもなれるもの（脚注：一定の条件あり）で、例えば <tt class="docutils literal"><span class="pre">a,b</span></tt> 共に <tt class="docutils literal"><span class="pre">String</span></tt> という型だとすると、</p>
<div class="highlight-bash"><div class="highlight"><pre>map :: <span class="o">(</span>String -&gt; String<span class="o">)</span> -&gt; <span class="o">[</span>String<span class="o">]</span> -&gt; <span class="o">[</span>String<span class="o">]</span>
</pre></div>
</div>
<p>となります。解答のコードで使われる <tt class="docutils literal"><span class="pre">map</span></tt>
はこのような型を持ちます。</p>
<p>こういう、普通の言語ではあまり見ないものを説明するには、なんでこんなもの必要なのかという切り口でいったほうがいいかなー（脚注：語尾に自信が感じられない。）。</p>
<p>GHCiを使って説明します。
GHCiでは、次のように変数を手で打って作ります。</p>
<div class="highlight-bash"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">str</span> <span class="o">=</span> <span class="s2">&quot;abcde&quot;</span>
</pre></div>
</div>
<p>文字列を操作する関数に<tt class="docutils literal"><span class="pre">reverse</span></tt>というものがあります。こいつに <tt class="docutils literal"><span class="pre">str</span></tt>をぶち込んでみます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; reverse str
<span class="s2">&quot;edcba&quot;</span>
</pre></div>
</td></tr></table></div>
<p>では、今度は次のようなリストを考えてみましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">strlst</span> <span class="o">=</span> <span class="o">[</span> <span class="s2">&quot;abcde&quot;</span>, <span class="s2">&quot;fghij&quot;</span> <span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>このリストの中の文字列両方に <tt class="docutils literal"><span class="pre">reverse</span></tt>をぶちかましたいときにどうするか？普通の言語ならfor文とかで一つずつ処理すればよいのですが、Haskellにはそんなもんありません。forなんか使っている言語は時代遅れの×▲□※♨︎です（脚注：言い過ぎ。）。</p>
<p>そこで、 <tt class="docutils literal"><span class="pre">map</span></tt> です。 <tt class="docutils literal"><span class="pre">map</span></tt>は、リストの中の要素一つ一つに指定した関数をぶちかましてくれます（脚注：「ぶちかます」→「適用する」）。やってみまっしょい。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; map reverse strlst
<span class="o">[</span><span class="s2">&quot;edcba&quot;</span>,<span class="s2">&quot;jihgf&quot;</span><span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>でけた。
Haskellにはforがありませんが、こんなふうに使わなくてもスマートにリストをさばく仕掛けがいろいろ用意されています。</p>
<p>ちなみに、あまり難しい用語を使いたくはないのですが、このような関数を「高階関数」と呼びます。考え方自体はあまり難しいものでもなくて、シェル芸人ならいつもやるような（脚注：国内で2,3人と思われる。）次のようなワンライナーと一緒です。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:USPMAG ueda<span class="nv">$ </span>find . | xargs -I\@ cp \@ \@.org
</pre></div>
</td></tr></table></div>
<p><tt class="docutils literal"><span class="pre">find(1)</span></tt>から流れてきたファイル名一つ一つに <tt class="docutils literal"><span class="pre">cp(1)</span></tt>を適用して <tt class="docutils literal"><span class="pre">.org</span></tt> という拡張子でバックアップファイルを作るという処理ですが、Haskellのコードとよく見比べてみると、<tt class="docutils literal"><span class="pre">xargs</span></tt> が <tt class="docutils literal"><span class="pre">map</span></tt> の役割を果たしていることが分かります。</p>
</div>
<div class="section" id="id3">
<h2>2.4. また高階関数かよ</h2>
<p>さて、次に、 <tt class="docutils literal"><span class="pre">map</span></tt> 関数に放り込まれている
<tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt> について。
まずは <tt class="docutils literal"><span class="pre">takeWhile</span></tt> の型を調べてみましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t takeWhile
takeWhile :: <span class="o">(</span>a -&gt; Bool<span class="o">)</span> -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>これも、第一引数に関数をとります。もうわけがわかりません。連載を続ける自信を無くしてきましたが、先に進みます。第二引数はなんらかのリストですね。細かい説明は放棄してとりあえずつこうてみましょーか。</p>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">str</span> <span class="o">=</span> <span class="s2">&quot;aaabbcaabb&quot;</span>
Prelude&gt; :t str
str :: <span class="o">[</span>Char<span class="o">]</span> &lt;- 文字列はCharのリスト
Prelude&gt; takeWhile <span class="o">(</span> <span class="o">==</span> <span class="s1">&#39;a&#39;</span> <span class="o">)</span> str
<span class="s2">&quot;aaa&quot;</span>
Prelude&gt; takeWhile <span class="o">(</span> /<span class="o">=</span> <span class="s1">&#39;c&#39;</span> <span class="o">)</span> str
<span class="s2">&quot;aaabb&quot;</span>
<span class="c">### == &#39;a&#39;や/= &#39;b&#39;も関数 ###</span>
Prelude&gt; :t <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span>
<span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span> :: Char -&gt; Bool
Prelude&gt; :t <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;c&#39;</span><span class="o">)</span>
<span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;c&#39;</span><span class="o">)</span> :: Char -&gt; Bool
<span class="c">### 「takeWhile (== &#39;a&#39;)」 は、文字列をとり文字列を返す</span>
Prelude&gt; :t takeWhile <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span>
takeWhile <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span> :: <span class="o">[</span>Char<span class="o">]</span> -&gt; <span class="o">[</span>Char<span class="o">]</span>
</pre></div>
</td></tr></table></div>
<p>つまり、条件を表す関数 <tt class="docutils literal"><span class="pre">==</span> <span class="pre">'a'</span></tt> や <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">'b'</span></tt>
が <tt class="docutils literal"><span class="pre">Bool</span></tt> 型の真を返すところまでのリストを返す
関数ということになります。したがって、解答のコードの<tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt>は、「文字列を受け取ってコロンの前までの文字列を返す関数」ということになります。</p>
</div>
<div class="section" id="id4">
<h2>2.5. んで <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> って何だよ。</h2>
<p>「 <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> 」は、関数です。
上の例にもありましたがGHCiで型を調べてみましょう。
まず、 <tt class="docutils literal"><span class="pre">/=</span></tt> の型を調査。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span>/<span class="o">=)</span>
<span class="o">(</span>/<span class="o">=)</span> :: Eq <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; Bool
</pre></div>
</td></tr></table></div>
<p>とりあえず <tt class="docutils literal"><span class="pre">Eq</span> <span class="pre">a</span> <span class="pre">=&gt;</span></tt> という部分は無視すると、第1引数に型 <tt class="docutils literal"><span class="pre">a</span></tt> 、第2引数に <tt class="docutils literal"><span class="pre">a</span></tt> をとって、<tt class="docutils literal"><span class="pre">Bool</span></tt> を返すことになってます。第1引数と第2引数を比較して同じなら<tt class="docutils literal"><span class="pre">True</span></tt> 、違ったら <tt class="docutils literal"><span class="pre">死ね</span></tt> と返します。間違えた。 <tt class="docutils literal"><span class="pre">False</span></tt> を返します。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="s2">&quot;祝&quot;</span> <span class="o">==</span> <span class="s2">&quot;祝&quot;</span>
True
Prelude&gt; <span class="s2">&quot;祝&quot;</span> <span class="o">==</span> <span class="s2">&quot;呪&quot;</span>
False
</pre></div>
</td></tr></table></div>
<p>「 <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> 」というのは、第1引数に <tt class="docutils literal"><span class="pre">':'</span></tt>
を指定しただけの関数です。</p>
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###まずは型を調査###</span>
Prelude&gt; :t <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span>
<span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span> :: Char -&gt; Bool
<span class="c">###よく分からんので「f」という名前をつけてみる###</span>
Prelude&gt; <span class="nb">let </span><span class="nv">f</span> <span class="o">=</span> <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span>
Prelude&gt; :t f
f :: Char -&gt; Bool
<span class="c">###確かに関数として振る舞う###</span>
Prelude&gt; f <span class="s1">&#39;:&#39;</span>
False
Prelude&gt; f <span class="s1">&#39;;&#39;</span>
True
</pre></div>
</td></tr></table></div>
<p>このようにHaskellの関数は、関数に中途半端に引数を与えて別の関数を作ることができます。これで、たくさん引数をとるような関数も、<tt class="docutils literal"><span class="pre">map</span></tt> や <tt class="docutils literal"><span class="pre">takeWhile</span></tt> で使えるようになるわけです（脚注：型が合えば。）。便利便利。</p>
<p>ここまで説明して、<tt class="docutils literal"><span class="pre">map</span> <span class="pre">(</span> <span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span> <span class="pre">)</span></tt>
というのが、
「文字列のリストを引数にとり、リストの各要素のコロンより前の文字列だけを再度リストにまとめて返す関数」であることが分かります。やれやれ。</p>
</div>
<div class="section" id="id5">
<h2>2.6. <tt class="docutils literal"><span class="pre">$</span></tt> のパワーを利用した緩和政策について</h2>
<p>さて、では次に <tt class="docutils literal"><span class="pre">map</span></tt> の左にある <tt class="docutils literal"><span class="pre">$</span></tt>
について。 <tt class="docutils literal"><span class="pre">$</span></tt> というのは、
<tt class="docutils literal"><span class="pre">$</span></tt> の右側を括弧で囲んでいるつもりになる記号です。
私のアホな説明ではよく分からんと思いますので、
例をお見せします。下の三つのコードは、
互いに全く同じ意味になります。</p>
<div class="highlight-bash"><div class="highlight"><pre>main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) ( lines cs )
main&#39; cs = unlines ( map ( takeWhile (/= &#39;:&#39;) ) ( lines cs ) )
main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) $ lines cs
</pre></div>
</div>
<p>Haskellのコードは <tt class="docutils literal"><span class="pre">$</span></tt> なしで書こうと思ったら書けるのですが、上記2番目のコードのように括弧が増えると読みにくくなるので、適度に <tt class="docutils literal"><span class="pre">$</span></tt> を使います。3番目のコードはちょっとやり過ぎのように個人的には思いますので、解答では1番目のコードを使いました。要はですね、これはLispをdisっているわけです。違いますか。違いますね。</p>
<p>最後、 <tt class="docutils literal"><span class="pre">unline</span></tt> は、文字列のリストを改行をはさんで連結する関数です。
<tt class="docutils literal"><span class="pre">$</span></tt> の右側の関数は <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> に書いてあるユーザ名をリストで返してくるので、 <tt class="docutils literal"><span class="pre">unline</span></tt>
で1行1ユーザ名でシュチュ力（脚注：出力。タイポが面白かったのでこのままで（おい）。）されてめでたしめでたしということになります。</p></div>
<div class="section" id="id6">
<h2>2.7. 若干量が余ったので解答2行目も説明しておく</h2>
<p>さて、どの問題でも共通の書き方になるので
触れるつもりがなかった解答の2行目ですが、
ちょっと余白ができそうなので解説しておきます
（脚注：どうも手を抜いているように見えるかもしれませんが、
USP Magazineならではのフリーダムを味わっているだけです。）。</p>
<div class="highlight-bash"><div class="highlight"><pre>main = getContents &gt;&gt;= putStr . main&#39;
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">main'</span></tt> からは <tt class="docutils literal"><span class="pre">String</span></tt> （厳密には <tt class="docutils literal"><span class="pre">[Char]</span></tt> ）
が返ってきます。他の関数、記号の型を見てみましょう。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t getContents
getContents :: IO String
Prelude&gt; :t putStr
putStr :: String -&gt; IO <span class="o">()</span>
<span class="c">### 演算子っぽいものにも型がある徹底っぷり ###</span>
Prelude&gt; :t <span class="o">(</span>&gt;&gt;<span class="o">=)</span>
<span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b
Prelude&gt; :t <span class="o">(</span>.<span class="o">)</span>
<span class="o">(</span>.<span class="o">)</span> :: <span class="o">(</span>b -&gt; c<span class="o">)</span> -&gt; <span class="o">(</span>a -&gt; b<span class="o">)</span> -&gt; a -&gt; c
</pre></div>
</td></tr></table></div>
<p>・・・説明する気が失せました。
しかし、本当に「型」というものが徹底されていますね、
Haskellは。</p>
<p>機能面からちゃんと説明しておくことにします。<tt class="docutils literal"><span class="pre">getContents</span></tt> は標準入力からデータを読む関数です。んで、よくよく考えると「標準入力からの入力」と、「関数に引数を入力」というのは同じ入力でも全く違うものです。このような違うものは関数をイコールでつないで扱えないので、このコードでは <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> という記号で右側の関数に標準入力から読んだものを投げています。</p>
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の右側にある <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">main'</span></tt>
は、二つの関数がつながったもので、機能としては <tt class="docutils literal"><span class="pre">main'</span></tt>の返す文字列を標準出力に放出するという関数です。<tt class="docutils literal"><span class="pre">main'</span></tt> の型はGHCiで調べられないので、別の例を。<tt class="docutils literal"><span class="pre">reverse</span></tt> と <tt class="docutils literal"><span class="pre">unwords</span></tt> という別々の関数をつなげて、「リストの文字列をひっくり返して空白区切りで連結する関数」を作り出します。</p>
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
16</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t reverse
reverse :: <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span>
Prelude&gt; :t unwords
unwords :: <span class="o">[</span>String<span class="o">]</span> -&gt; String
<span class="c">### unwords と reverse をくっつける ###</span>
Prelude&gt; :t unwords . reverse
unwords . reverse :: <span class="o">[</span>String<span class="o">]</span> -&gt; String
<span class="c">### 使う ###</span>
Prelude&gt; <span class="o">(</span>unwords . reverse<span class="o">)</span> <span class="o">[</span><span class="s2">&quot;abc&quot;</span>,<span class="s2">&quot;def&quot;</span><span class="o">]</span>
<span class="s2">&quot;def abc&quot;</span>
<span class="c">### 使う（その2） ###</span>
Prelude&gt; <span class="nb">let </span><span class="nv">f</span> <span class="o">=</span> unwords .reverse
Prelude&gt; f <span class="o">[</span><span class="s2">&quot;abc&quot;</span>,<span class="s2">&quot;def&quot;</span><span class="o">]</span>
<span class="s2">&quot;def abc&quot;</span>
Prelude&gt; :t f
f :: <span class="o">[</span>String<span class="o">]</span> -&gt; String
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h2>2.8. おわりに</h2>
<p>では、本稿を締めたいと思います。諦めではありません。締めです。</p>
<ul class="simple">
<li>Haskellでは関数を引数にとる関数がある（たくさん）。</li>
<li>このような関数がfor文がないHaskellでは重要な役割を担う。</li>
<li><tt class="docutils literal"><span class="pre">map</span></tt> 関数はHaskellにおける <tt class="docutils literal"><span class="pre">xargs(1)</span></tt> である。</li>
<li><tt class="docutils literal"><span class="pre">xargs(1)</span></tt> はシェル芸におけるmapである。</li>
<li>高階関数とか難しいこと考えずにさらっと書けるようになりたいなあ（小並感）。</li>
<li>シェル芸って、ここまで説明する側に負担がないから楽だね。</li>
</ul>
<p>次回、第1回の2問目に入ります！遅っ！</p>
</div>


<a href="/?page=02944">各号の一覧へ</a>

