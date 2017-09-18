---
Copyright: (C) Ryuichi Ueda
---

# USP Magazine 2014年5月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典：<a href="http://www.usp-lab.com/pub.magazine.html" target="_blank">USPマガジン2014年5月号</a><br />
<br />
2014年5月号:<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4904807073" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a><br />
<br />
<h1>2. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1><br />
<p>産業技術大学院・USP研究所・USP友の会　上田隆一<br />
（脚注：順に助教、アドバイザリーフェロー、会長）</p><br />
<blockquote><br />
<div>USP友の会のシェル芸勉強会（脚注：シェルのワンライナー勉強会）は、日々、他の言語からの他流試合に晒されているのである（脚注：Ruby, Perl, PowerShell等々。）。そこで上田は、Haskellで自ら他流試合を行い、さらにシェル芸勉強会をいじめる自傷行為に手を染めるのであった。</div></blockquote><br />
<div class="section" id="id1"><br />
<br />
<h2>2.1. はじめに</h2><br />
<p>皆さん、やさぐれてますか？ブラックエンジェル上田ちゃんです。最近、超ネガティブです。なぜ、ネガティブか。それは喋らずに本題に行きます（脚注：生きていればいろんなことがあるじゃないですか。）。</p><br />
</div><br />
<div class="section" id="id2"><br />
<br />
<h2>2.2. 前回の続き</h2><br />
<p>さて、前回はまだ第1回の1問目について、解答を作ったところでした。ちょっと重複して申し訳ないんですが、問題と解答を書いてから話を始めます。</p><br />
<br />
<ul class="simple"><br />
<li>問題（第1回第1問）:（Linuxの） <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> から、</li><br />
</ul><br />
<p>ユーザ名を抽出したリストを作ってください。</p><br />
<blockquote><br />
<div>シェルのワンライナーだと以下のとおり。</div></blockquote><br />
<br />
<div class="highlight-none"><div class="highlight"><pre>ueda\@ubuntu:~$ cat /etc/passwd | awk &quot;-F:&quot; &#39;{print $1}&#39;<br />
...<br />
sshd<br />
ueda<br />
mysql<br />
postfix<br />
</pre></div><br />
</div><br />
<ul class="simple"><br />
<li>解答例</li><br />
</ul><br />
<div class="highlight-none"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>ueda\@remote:~$ cat q1_1.hs<br />
main = getContents &gt;&gt;= putStr . main&#39;<br />
<br />
main&#39; :: String -&gt; String<br />
main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) ( lines cs )<br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>実行</li><br />
</ul><br />
<div class="highlight-none"><div class="highlight"><pre>ueda\@remote:~$ ghc q1_1.hs<br />
[1 of 1] Compiling Main ( q1_1.hs, q1_1.o )<br />
Linking q1_1 ...<br />
ueda\@remote:~$ cat /etc/passwd | ./q1_1<br />
...<br />
ueda<br />
mysql<br />
postfix<br />
</pre></div><br />
</div><br />
<p>んで、前回は <tt class="docutils literal"><span class="pre">map</span></tt> とか <tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt><br />
を説明しようとして終わっていたのでした。</p><br />
</div><br />
<div class="section" id="map"><br />
<h2>2.3. mapがないと困る</h2><br />
<p>まず <tt class="docutils literal"><span class="pre">map</span></tt> から。<br />
Haskellの対話的インタプリタGHCiで調べると、<br />
型はこんなもんだと分かります。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>ghci<br />
Prelude&gt; :t map<br />
map :: <span class="o">(</span>a -&gt; b<span class="o">)</span> -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>b<span class="o">]</span><br />
<span class="c">###GHCiを抜けるときはCtrl+d###</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">map</span></tt> は、第一引数に型 <tt class="docutils literal"><span class="pre">a</span> <span class="pre">-&gt;</span> <span class="pre">b</span></tt> の <em>関数</em> 、<br />
第二引数に型 <tt class="docutils literal"><span class="pre">a</span></tt> のリストを渡すと、型 <tt class="docutils literal"><span class="pre">b</span></tt> のリストを返すという意味になります。つまり、関数 <tt class="docutils literal"><span class="pre">map</span></tt> には別の関数とリストをひとつずつ指定して使います。<br />
<tt class="docutils literal"><span class="pre">a</span></tt> とか <tt class="docutils literal"><span class="pre">b</span></tt> とかは、どんな型にもなれるもの（脚注：一定の条件あり）で、例えば <tt class="docutils literal"><span class="pre">a,b</span></tt> 共に <tt class="docutils literal"><span class="pre">String</span></tt> という型だとすると、</p><br />
<div class="highlight-bash"><div class="highlight"><pre>map :: <span class="o">(</span>String -&gt; String<span class="o">)</span> -&gt; <span class="o">[</span>String<span class="o">]</span> -&gt; <span class="o">[</span>String<span class="o">]</span><br />
</pre></div><br />
</div><br />
<p>となります。解答のコードで使われる <tt class="docutils literal"><span class="pre">map</span></tt><br />
はこのような型を持ちます。</p><br />
<p>こういう、普通の言語ではあまり見ないものを説明するには、なんでこんなもの必要なのかという切り口でいったほうがいいかなー（脚注：語尾に自信が感じられない。）。</p><br />
<p>GHCiを使って説明します。<br />
GHCiでは、次のように変数を手で打って作ります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">str</span> <span class="o">=</span> <span class="s2">&quot;abcde&quot;</span><br />
</pre></div><br />
</div><br />
<p>文字列を操作する関数に<tt class="docutils literal"><span class="pre">reverse</span></tt>というものがあります。こいつに <tt class="docutils literal"><span class="pre">str</span></tt>をぶち込んでみます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; reverse str<br />
<span class="s2">&quot;edcba&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>では、今度は次のようなリストを考えてみましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">strlst</span> <span class="o">=</span> <span class="o">[</span> <span class="s2">&quot;abcde&quot;</span>, <span class="s2">&quot;fghij&quot;</span> <span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>このリストの中の文字列両方に <tt class="docutils literal"><span class="pre">reverse</span></tt>をぶちかましたいときにどうするか？普通の言語ならfor文とかで一つずつ処理すればよいのですが、Haskellにはそんなもんありません。forなんか使っている言語は時代遅れの×▲□※♨︎です（脚注：言い過ぎ。）。</p><br />
<p>そこで、 <tt class="docutils literal"><span class="pre">map</span></tt> です。 <tt class="docutils literal"><span class="pre">map</span></tt>は、リストの中の要素一つ一つに指定した関数をぶちかましてくれます（脚注：「ぶちかます」→「適用する」）。やってみまっしょい。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; map reverse strlst<br />
<span class="o">[</span><span class="s2">&quot;edcba&quot;</span>,<span class="s2">&quot;jihgf&quot;</span><span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>でけた。<br />
Haskellにはforがありませんが、こんなふうに使わなくてもスマートにリストをさばく仕掛けがいろいろ用意されています。</p><br />
<p>ちなみに、あまり難しい用語を使いたくはないのですが、このような関数を「高階関数」と呼びます。考え方自体はあまり難しいものでもなくて、シェル芸人ならいつもやるような（脚注：国内で2,3人と思われる。）次のようなワンライナーと一緒です。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedambp:USPMAG ueda<span class="nv">$ </span>find . | xargs -I\@ cp \@ \@.org<br />
</pre></div><br />
</td></tr></table></div><br />
<p><tt class="docutils literal"><span class="pre">find(1)</span></tt>から流れてきたファイル名一つ一つに <tt class="docutils literal"><span class="pre">cp(1)</span></tt>を適用して <tt class="docutils literal"><span class="pre">.org</span></tt> という拡張子でバックアップファイルを作るという処理ですが、Haskellのコードとよく見比べてみると、<tt class="docutils literal"><span class="pre">xargs</span></tt> が <tt class="docutils literal"><span class="pre">map</span></tt> の役割を果たしていることが分かります。</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>2.4. また高階関数かよ</h2><br />
<p>さて、次に、 <tt class="docutils literal"><span class="pre">map</span></tt> 関数に放り込まれている<br />
<tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt> について。<br />
まずは <tt class="docutils literal"><span class="pre">takeWhile</span></tt> の型を調べてみましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t takeWhile<br />
takeWhile :: <span class="o">(</span>a -&gt; Bool<span class="o">)</span> -&gt; <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>これも、第一引数に関数をとります。もうわけがわかりません。連載を続ける自信を無くしてきましたが、先に進みます。第二引数はなんらかのリストですね。細かい説明は放棄してとりあえずつこうてみましょーか。</p><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="nb">let </span><span class="nv">str</span> <span class="o">=</span> <span class="s2">&quot;aaabbcaabb&quot;</span><br />
Prelude&gt; :t str<br />
str :: <span class="o">[</span>Char<span class="o">]</span> &lt;- 文字列はCharのリスト<br />
Prelude&gt; takeWhile <span class="o">(</span> <span class="o">==</span> <span class="s1">&#39;a&#39;</span> <span class="o">)</span> str<br />
<span class="s2">&quot;aaa&quot;</span><br />
Prelude&gt; takeWhile <span class="o">(</span> /<span class="o">=</span> <span class="s1">&#39;c&#39;</span> <span class="o">)</span> str<br />
<span class="s2">&quot;aaabb&quot;</span><br />
<span class="c">### == &#39;a&#39;や/= &#39;b&#39;も関数 ###</span><br />
Prelude&gt; :t <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span><br />
<span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span> :: Char -&gt; Bool<br />
Prelude&gt; :t <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;c&#39;</span><span class="o">)</span><br />
<span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;c&#39;</span><span class="o">)</span> :: Char -&gt; Bool<br />
<span class="c">### 「takeWhile (== &#39;a&#39;)」 は、文字列をとり文字列を返す</span><br />
Prelude&gt; :t takeWhile <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span><br />
takeWhile <span class="o">(==</span> <span class="s1">&#39;a&#39;</span><span class="o">)</span> :: <span class="o">[</span>Char<span class="o">]</span> -&gt; <span class="o">[</span>Char<span class="o">]</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>つまり、条件を表す関数 <tt class="docutils literal"><span class="pre">==</span> <span class="pre">'a'</span></tt> や <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">'b'</span></tt><br />
が <tt class="docutils literal"><span class="pre">Bool</span></tt> 型の真を返すところまでのリストを返す<br />
関数ということになります。したがって、解答のコードの<tt class="docutils literal"><span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span></tt>は、「文字列を受け取ってコロンの前までの文字列を返す関数」ということになります。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h2>2.5. んで <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> って何だよ。</h2><br />
<p>「 <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> 」は、関数です。<br />
上の例にもありましたがGHCiで型を調べてみましょう。<br />
まず、 <tt class="docutils literal"><span class="pre">/=</span></tt> の型を調査。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t <span class="o">(</span>/<span class="o">=)</span><br />
<span class="o">(</span>/<span class="o">=)</span> :: Eq <span class="nv">a</span> <span class="o">=</span>&gt; a -&gt; a -&gt; Bool<br />
</pre></div><br />
</td></tr></table></div><br />
<p>とりあえず <tt class="docutils literal"><span class="pre">Eq</span> <span class="pre">a</span> <span class="pre">=&gt;</span></tt> という部分は無視すると、第1引数に型 <tt class="docutils literal"><span class="pre">a</span></tt> 、第2引数に <tt class="docutils literal"><span class="pre">a</span></tt> をとって、<tt class="docutils literal"><span class="pre">Bool</span></tt> を返すことになってます。第1引数と第2引数を比較して同じなら<tt class="docutils literal"><span class="pre">True</span></tt> 、違ったら <tt class="docutils literal"><span class="pre">死ね</span></tt> と返します。間違えた。 <tt class="docutils literal"><span class="pre">False</span></tt> を返します。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; <span class="s2">&quot;祝&quot;</span> <span class="o">==</span> <span class="s2">&quot;祝&quot;</span><br />
True<br />
Prelude&gt; <span class="s2">&quot;祝&quot;</span> <span class="o">==</span> <span class="s2">&quot;呪&quot;</span><br />
False<br />
</pre></div><br />
</td></tr></table></div><br />
<p>「 <tt class="docutils literal"><span class="pre">/=</span> <span class="pre">':'</span></tt> 」というのは、第1引数に <tt class="docutils literal"><span class="pre">':'</span></tt><br />
を指定しただけの関数です。</p><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###まずは型を調査###</span><br />
Prelude&gt; :t <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span><br />
<span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span> :: Char -&gt; Bool<br />
<span class="c">###よく分からんので「f」という名前をつけてみる###</span><br />
Prelude&gt; <span class="nb">let </span><span class="nv">f</span> <span class="o">=</span> <span class="o">(</span>/<span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">)</span><br />
Prelude&gt; :t f<br />
f :: Char -&gt; Bool<br />
<span class="c">###確かに関数として振る舞う###</span><br />
Prelude&gt; f <span class="s1">&#39;:&#39;</span><br />
False<br />
Prelude&gt; f <span class="s1">&#39;;&#39;</span><br />
True<br />
</pre></div><br />
</td></tr></table></div><br />
<p>このようにHaskellの関数は、関数に中途半端に引数を与えて別の関数を作ることができます。これで、たくさん引数をとるような関数も、<tt class="docutils literal"><span class="pre">map</span></tt> や <tt class="docutils literal"><span class="pre">takeWhile</span></tt> で使えるようになるわけです（脚注：型が合えば。）。便利便利。</p><br />
<p>ここまで説明して、<tt class="docutils literal"><span class="pre">map</span> <span class="pre">(</span> <span class="pre">takeWhile</span> <span class="pre">(/=</span> <span class="pre">':')</span> <span class="pre">)</span></tt><br />
というのが、<br />
「文字列のリストを引数にとり、リストの各要素のコロンより前の文字列だけを再度リストにまとめて返す関数」であることが分かります。やれやれ。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>2.6. <tt class="docutils literal"><span class="pre">$</span></tt> のパワーを利用した緩和政策について</h2><br />
<p>さて、では次に <tt class="docutils literal"><span class="pre">map</span></tt> の左にある <tt class="docutils literal"><span class="pre">$</span></tt><br />
について。 <tt class="docutils literal"><span class="pre">$</span></tt> というのは、<br />
<tt class="docutils literal"><span class="pre">$</span></tt> の右側を括弧で囲んでいるつもりになる記号です。<br />
私のアホな説明ではよく分からんと思いますので、<br />
例をお見せします。下の三つのコードは、<br />
互いに全く同じ意味になります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) ( lines cs )<br />
main&#39; cs = unlines ( map ( takeWhile (/= &#39;:&#39;) ) ( lines cs ) )<br />
main&#39; cs = unlines $ map ( takeWhile (/= &#39;:&#39;) ) $ lines cs<br />
</pre></div><br />
</div><br />
<p>Haskellのコードは <tt class="docutils literal"><span class="pre">$</span></tt> なしで書こうと思ったら書けるのですが、上記2番目のコードのように括弧が増えると読みにくくなるので、適度に <tt class="docutils literal"><span class="pre">$</span></tt> を使います。3番目のコードはちょっとやり過ぎのように個人的には思いますので、解答では1番目のコードを使いました。要はですね、これはLispをdisっているわけです。違いますか。違いますね。</p><br />
<p>最後、 <tt class="docutils literal"><span class="pre">unline</span></tt> は、文字列のリストを改行をはさんで連結する関数です。<br />
<tt class="docutils literal"><span class="pre">$</span></tt> の右側の関数は <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> に書いてあるユーザ名をリストで返してくるので、 <tt class="docutils literal"><span class="pre">unline</span></tt><br />
で1行1ユーザ名でシュチュ力（脚注：出力。タイポが面白かったのでこのままで（おい）。）されてめでたしめでたしということになります。</p></div><br />
<div class="section" id="id6"><br />
<h2>2.7. 若干量が余ったので解答2行目も説明しておく</h2><br />
<p>さて、どの問題でも共通の書き方になるので<br />
触れるつもりがなかった解答の2行目ですが、<br />
ちょっと余白ができそうなので解説しておきます<br />
（脚注：どうも手を抜いているように見えるかもしれませんが、<br />
USP Magazineならではのフリーダムを味わっているだけです。）。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>main = getContents &gt;&gt;= putStr . main&#39;<br />
</pre></div><br />
</div><br />
<p><tt class="docutils literal"><span class="pre">main'</span></tt> からは <tt class="docutils literal"><span class="pre">String</span></tt> （厳密には <tt class="docutils literal"><span class="pre">[Char]</span></tt> ）<br />
が返ってきます。他の関数、記号の型を見てみましょう。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t getContents<br />
getContents :: IO String<br />
Prelude&gt; :t putStr<br />
putStr :: String -&gt; IO <span class="o">()</span><br />
<span class="c">### 演算子っぽいものにも型がある徹底っぷり ###</span><br />
Prelude&gt; :t <span class="o">(</span>&gt;&gt;<span class="o">=)</span><br />
<span class="o">(</span>&gt;&gt;<span class="o">=)</span> :: Monad <span class="nv">m</span> <span class="o">=</span>&gt; m a -&gt; <span class="o">(</span>a -&gt; m b<span class="o">)</span> -&gt; m b<br />
Prelude&gt; :t <span class="o">(</span>.<span class="o">)</span><br />
<span class="o">(</span>.<span class="o">)</span> :: <span class="o">(</span>b -&gt; c<span class="o">)</span> -&gt; <span class="o">(</span>a -&gt; b<span class="o">)</span> -&gt; a -&gt; c<br />
</pre></div><br />
</td></tr></table></div><br />
<p>・・・説明する気が失せました。<br />
しかし、本当に「型」というものが徹底されていますね、<br />
Haskellは。</p><br />
<p>機能面からちゃんと説明しておくことにします。<tt class="docutils literal"><span class="pre">getContents</span></tt> は標準入力からデータを読む関数です。んで、よくよく考えると「標準入力からの入力」と、「関数に引数を入力」というのは同じ入力でも全く違うものです。このような違うものは関数をイコールでつないで扱えないので、このコードでは <tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> という記号で右側の関数に標準入力から読んだものを投げています。</p><br />
<p><tt class="docutils literal"><span class="pre">&gt;&gt;=</span></tt> の右側にある <tt class="docutils literal"><span class="pre">putStr</span> <span class="pre">.</span> <span class="pre">main'</span></tt><br />
は、二つの関数がつながったもので、機能としては <tt class="docutils literal"><span class="pre">main'</span></tt>の返す文字列を標準出力に放出するという関数です。<tt class="docutils literal"><span class="pre">main'</span></tt> の型はGHCiで調べられないので、別の例を。<tt class="docutils literal"><span class="pre">reverse</span></tt> と <tt class="docutils literal"><span class="pre">unwords</span></tt> という別々の関数をつなげて、「リストの文字列をひっくり返して空白区切りで連結する関数」を作り出します。</p><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre>Prelude&gt; :t reverse<br />
reverse :: <span class="o">[</span>a<span class="o">]</span> -&gt; <span class="o">[</span>a<span class="o">]</span><br />
Prelude&gt; :t unwords<br />
unwords :: <span class="o">[</span>String<span class="o">]</span> -&gt; String<br />
<span class="c">### unwords と reverse をくっつける ###</span><br />
Prelude&gt; :t unwords . reverse<br />
unwords . reverse :: <span class="o">[</span>String<span class="o">]</span> -&gt; String<br />
<span class="c">### 使う ###</span><br />
Prelude&gt; <span class="o">(</span>unwords . reverse<span class="o">)</span> <span class="o">[</span><span class="s2">&quot;abc&quot;</span>,<span class="s2">&quot;def&quot;</span><span class="o">]</span><br />
<span class="s2">&quot;def abc&quot;</span><br />
<span class="c">### 使う（その2） ###</span><br />
Prelude&gt; <span class="nb">let </span><span class="nv">f</span> <span class="o">=</span> unwords .reverse<br />
Prelude&gt; f <span class="o">[</span><span class="s2">&quot;abc&quot;</span>,<span class="s2">&quot;def&quot;</span><span class="o">]</span><br />
<span class="s2">&quot;def abc&quot;</span><br />
Prelude&gt; :t f<br />
f :: <span class="o">[</span>String<span class="o">]</span> -&gt; String<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h2>2.8. おわりに</h2><br />
<p>では、本稿を締めたいと思います。諦めではありません。締めです。</p><br />
<ul class="simple"><br />
<li>Haskellでは関数を引数にとる関数がある（たくさん）。</li><br />
<li>このような関数がfor文がないHaskellでは重要な役割を担う。</li><br />
<li><tt class="docutils literal"><span class="pre">map</span></tt> 関数はHaskellにおける <tt class="docutils literal"><span class="pre">xargs(1)</span></tt> である。</li><br />
<li><tt class="docutils literal"><span class="pre">xargs(1)</span></tt> はシェル芸におけるmapである。</li><br />
<li>高階関数とか難しいこと考えずにさらっと書けるようになりたいなあ（小並感）。</li><br />
<li>シェル芸って、ここまで説明する側に負担がないから楽だね。</li><br />
</ul><br />
<p>次回、第1回の2問目に入ります！遅っ！</p><br />
</div><br />
<br />
<br />
<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a><br />

