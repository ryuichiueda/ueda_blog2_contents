# 開眼シェルスクリプト2013年11月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <br />
 <div class="section" id="id1"><br />
<h1>23. 開眼シェルスクリプト 第23回 表記揺れ・綴りをチェックする<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　前回「文章を扱う」というお題でコマンドの操作をいくつか紹介しました。<br />
今回は「文章を扱う道具」つまりコマンドをシェルスクリプトで作ってみます。</p><br />
<p>　作るコマンドは語尾のチェックコマンドとスペルチェックのコマンドです。<br />
いずれのコマンドも、既存のコマンドをうまく組み合わせて、<br />
短いものを作ります。</p><br />
<p>　今回はコマンド作者となるわけですから、<br />
GancarzのUNIX哲学（脚注：<a class="reference external" href="http://ja.wikipedia.org/wiki">http://ja.wikipedia.org/wiki</a>/UNIX哲学）<br />
を全部頭に叩き込んで、先にお進み下さい。<br />
特に、</p><br />
<ul class="simple"><br />
<li>各プログラムが一つのことをうまくやるようにせよ。</li><br />
<li>全てのプログラムはフィルタとして振る舞うようにせよ。</li><br />
</ul><br />
<p>が大事です。</p><br />
<div class="section" id="id2"><br />
<h2>23.1. 環境等<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、Macに溜まった開眼シェルスクリプトの原稿について、<br />
いろいろチェックするものを作っていきます。<br />
Macには、GNU sed（ <tt class="docutils literal"><span class="pre">gsed</span></tt> ）とGNU awk （ <tt class="docutils literal"><span class="pre">gawk</span></tt> ）<br />
がインストールされているものとします。<br />
リスト1に環境を示します。</p><br />
<ul class="simple"><br />
<li>リスト1: 環境</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.4.0 Darwin Kernel Version 12.4.0: Wed May 1 17:57:12 PDT 2013; root:xnu-2050.24.15~1/RELEASE_X86_64 x86_64<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>gsed --version<br />
gsed <span class="o">(</span>GNU sed<span class="o">)</span> 4.2.2<br />
（略）<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>gawk --version<br />
GNU Awk 4.1.0, API: 1.0<br />
Copyright <span class="o">(</span>C<span class="o">)</span> 1989, 1991-2013 Free Software Foundation.<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　原稿はテキストファイルです。<br />
reStructuredText という形式でマークアップされていますが、<br />
それはあまり気にしなくて大丈夫です。<br />
拡張子はリスト2のように <tt class="docutils literal"><span class="pre">.rst</span></tt> です。</p><br />
<ul class="simple"><br />
<li>リスト2: 原稿のファイル</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>ls *.rst<br />
201201.rst 201210.rst 201306.rst<br />
201202.rst 201211.rst 201306SPECIAL.rst<br />
201203.rst 201212.rst 201307.rst<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<blockquote><br />
<div></div></blockquote><br />
<p>原稿にはリスト3のように、<br />
だいたい30字くらいで改行を入れています。</p><br />
<ul class="simple"><br />
<li>リスト3: 原稿</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>tail -n 5 201302.rst<br />
lsとwcを使えば事足ります。captiveでないので、なんとかなります。<br />
<br />
　今回は正直言いまして、<br />
かなりエクストリームなプログラミングになってしまいましたので、<br />
次回からはもうちょっとマイルドな話題を扱いたいと思います。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　コマンド等、作ったものはディレクトリ <tt class="docutils literal"><span class="pre">SD_GENKOU</span></tt> の下に <tt class="docutils literal"><span class="pre">bin</span></tt><br />
というディレクトリを作ってそこに置く事にします。</p><br />
</div><br />
<div class="section" id="id3"><br />
<h2>23.2. ですます・だであるチェック<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　まず、表記揺れの基本中の基本、<br />
「ですます調」と「だである調」<br />
のチェックを行うシェルスクリプトを作ってみましょう。<br />
「です。」「ます。」等の数を数え、<br />
次に「だ。」「である。」等の数を数え、<br />
どちらも1以上だったら「怪しい」という簡素なものです。</p><br />
<p>　まずはリスト4のように作ってみましょう。<br />
これだと、例えば一行に「です。」が2回出てきても1とカウントされますが、<br />
自分で使うには十分でしょう。<br />
もちろん、たとえばこれを公開しようとすれば、<br />
いろいろ細かく修正が必要です。</p><br />
<ul class="simple"><br />
<li>リスト4: 語尾を数えるコマンド</li><br />
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
23</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201311 ueda<span class="nv">$ </span>cat deathmath1<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
cat &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-text<br />
<br />
<span class="nv">death</span><span class="o">=</span><span class="s2">&quot;(です。|ます。|でした。|ました。|でしょう。|ません。)&quot;</span><br />
<span class="nv">da</span><span class="o">=</span><span class="s2">&quot;(だ。|である。|ない。|か。)&quot;</span><br />
<br />
grep -E <span class="s2">&quot;$death&quot;</span> <span class="nv">$tmp</span>-text |<br />
wc -l |<br />
tr -d <span class="s1">&#39; &#39;</span> &gt; <span class="nv">$tmp</span>-death<br />
<br />
grep -E <span class="s2">&quot;$da&quot;</span> <span class="nv">$tmp</span>-text |<br />
wc -l |<br />
tr -d <span class="s1">&#39; &#39;</span> &gt; <span class="nv">$tmp</span>-da<br />
<br />
<span class="nb">echo</span> <span class="s2">&quot;ですます&quot;</span> <span class="k">$(</span>cat <span class="nv">$tmp</span>-death<span class="k">)</span><br />
<span class="nb">echo</span> <span class="s2">&quot;だである&quot;</span> <span class="k">$(</span>cat <span class="nv">$tmp</span>-da<span class="k">)</span><br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 コードの説明をしておくと、6行目で標準入力を <tt class="docutils literal"><span class="pre">$tmp-text</span></tt><br />
に一度溜めています。<br />
<tt class="docutils literal"><span class="pre">$tmp-text</span></tt> は <tt class="docutils literal"><span class="pre">/tmp/</span></tt> 下のファイルですが、<br />
このコードだと <tt class="docutils literal"><span class="pre">/tmp/</span></tt> 下にファイルが残ってしまう可能性があります。<br />
不特性多数の人々が使うUNIX環境のときは別のところに<br />
一時ファイルを置きましょう。<br />
今はあまりそういうこともないでしょうが、一応お断りを。<br />
6行目の「 <tt class="docutils literal"><span class="pre">&lt;</span> <span class="pre">/dev/stdin</span></tt> 」は、<br />
このシェルスクリプトの標準入力を読み込むリダイレクトですが、<br />
書かなくても <tt class="docutils literal"><span class="pre">cat</span></tt> が標準入力を読んでくれます。<br />
筆者はそれだと分かりにくいので、明記しています。</p><br />
<p>　8,9行目で、正規表現を作ります。<br />
語尾はたくさん種類があるので、ここにずらずら並べておきます。<br />
おそらく全部網羅することは難しいし、<br />
きりがないので自分の困らない範囲で列挙しておけばよいでしょう。<br />
ただ、全く対処できないかというとそうでもなく、<br />
例えばリスト5のようにワンライナーで語尾を抽出して、<br />
後から解析することはできます。<br />
身も蓋もないことを言うと、<br />
形態素解析のコマンドをシェルスクリプトの中で使うと<br />
完璧に近いものができるかもしれません。<br />
それがシェルスクリプトの良いところなので、<br />
使えるものは何でも使いましょう。</p><br />
<ul class="simple"><br />
<li>リスト5: 語尾を抽出</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201311 ueda<span class="nv">$ </span>cat ../*.rst |<br />
gsed <span class="s1">&#39;s/....。/\\n&amp;\\n/g&#39;</span> | grep 。|<br />
sed <span class="s1">&#39;s/。.*/。/&#39;</span> | sort -u<br />
（略）<br />
（縦）軸。<br />
（？）を。<br />
）を作れ。<br />
）を知る。<br />
：私です。<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　使ってみましょう。リスト6は実行例です。<br />
原稿はですます調で書かれていますが、1.5%程度、<br />
したがっていない部分があるように見えます。</p><br />
<ul class="simple"><br />
<li>リスト6: <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を使う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath1<br />
ですます 2252<br />
だである 32<br />
</pre></div><br />
</td></tr></table></div><br />
<blockquote><br />
<div></div></blockquote><br />
</div><br />
<div class="section" id="id4"><br />
<h2>23.3. コマンドを書き直す<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、「だ、である」がちょっと混ざっているようなのですが、<br />
今度はどこを修正しなければならないのか知りたくなってきます。<br />
<tt class="docutils literal"><span class="pre">grep</span></tt> を使えばよいのですが、<br />
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> では8,9行目で複数の語尾を指定しているので、<br />
これをいちいち手打ちするのは面倒くさいし、<br />
いちいち覚えてられません。<br />
コマンドを新たに作るか、 <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を拡張するか、<br />
どちらかをした方がよいでしょう。</p><br />
<p>　ここで、「コマンドの作り手」はとても悩みます。<br />
コマンドは単機能にしておく方が、<br />
後から手を入れるときに楽です。肥大化もしません。<br />
これはGancarzのUNIX哲学にもあります。<br />
例えば、 <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を拡張するとなると、<br />
オプションを新たに設けなければいけませんし、<br />
追加箇所と既存の箇所を分けるために、<br />
関数で分けなければなりません。<br />
つまり、余計な情報を追加しなければなりません。</p><br />
<p>　一方でコマンドを新たに作るとなると、<br />
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> の8,9行目にある変数をうまく共有する仕組みが必要です。<br />
しかし今のところ、わざわざ辞書ファイルを外に出すほどのものでもありません。</p><br />
<p>　筆者の出した答えは次のようなものです。</p><br />
<ul class="simple"><br />
<li><tt class="docutils literal"><span class="pre">deathmath1</span></tt> を、行数でなく、当該箇所を出力するように書き直し</li><br />
<li>行数を数えたかったら、他のコマンドで</li><br />
</ul><br />
<p>　つまるところ、筆者は <tt class="docutils literal"><span class="pre">deathmath1</span></tt> が「作り過ぎ」だったと判断しました。<br />
せっかく作った <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を放棄して、手戻りをします。<br />
普通、雑誌にコードをのっけるときはこういう放棄はしないものですが、<br />
こういう考え方でツールを改善する例ですので容赦ください。</p><br />
<p>　作り直し版では、 <tt class="docutils literal"><span class="pre">grep</span></tt> を使うと中間ファイルを作らざるを得ず面倒なので、<br />
<tt class="docutils literal"><span class="pre">awk</span></tt> で印をつける方式に変更します。<br />
リスト7のようにしました。</p><br />
<ul class="simple"><br />
<li>リスト7: <tt class="docutils literal"><span class="pre">deathmath2</span></tt></li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/deathmath2<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">death</span><span class="o">=</span><span class="s2">&quot;です。|ます。|でしょう。|ません。&quot;</span><br />
<span class="nv">da</span><span class="o">=</span><span class="s2">&quot;だ。|である。|ない。|か。&quot;</span><br />
<br />
gawk <span class="s1">&#39;{print FILENAME &quot;:&quot; FNR &quot;:&quot; ,$0}&#39;</span> <span class="s2">&quot;$\@&quot;</span> |<br />
gawk -v <span class="nv">death</span><span class="o">=</span><span class="nv">$death</span> -v <span class="nv">da</span><span class="o">=</span><span class="nv">$da</span> <span class="se">\\</span><br />
 <span class="s1">&#39;$0~death{print &quot;+&quot;,$0}$0~da{print &quot;-&quot;,$0}&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト7のコードについて補足説明しておきます。<br />
まず、7行目の <tt class="docutils literal"><span class="pre">&quot;$&#64;&quot;</span></tt> は、<br />
<tt class="docutils literal"><span class="pre">deathmath2</span></tt> がもらったオプションをそのまま <tt class="docutils literal"><span class="pre">awk</span></tt><br />
に渡すための方法です。 <tt class="docutils literal"><span class="pre">&quot;$*&quot;</span></tt> だと、<br />
複数のファイル名がオプションに入っている場合、<br />
うまくいきません。<br />
ファイル名がずらずら並んだ文字列を一個のオプションとみなすからです。<br />
リスト8の例では、 <tt class="docutils literal"><span class="pre">&quot;201311.rst</span> <span class="pre">201211.rst&quot;</span></tt><br />
が一つのファイル名だと解釈されるため、<br />
<tt class="docutils literal"><span class="pre">cat</span></tt> がエラーを出します。<br />
ところで、この方法は面白いことに、ファイル名を指定せずに、<br />
標準入力からの文字列を入力しても動作します。<br />
このときは、 <tt class="docutils literal"><span class="pre">&quot;$&#64;&quot;</span></tt> が空になり、<br />
その場合、 <tt class="docutils literal"><span class="pre">gawk</span></tt> はオプション無しと判断して標準入力を読みに行きます。</p><br />
<p>　次に、検索で引っ掛ける文字列は4,5行目で、<br />
bashの変数として定義しています。<br />
これを12行目で <tt class="docutils literal"><span class="pre">gawk</span></tt> に引き渡しています。<br />
正規表現を変数に渡しているわけですが、<br />
<tt class="docutils literal"><span class="pre">/</span></tt> は不要なようです。</p><br />
<p>　7行目の <tt class="docutils literal"><span class="pre">FNR</span></tt> は行番号が格納された変数ですが、<br />
<tt class="docutils literal"><span class="pre">NR</span></tt> と違って、読み込んだファイルごとの行番号が格納されます。<br />
ですので、この例のように「あるファイルの何行目」<br />
を出力するときに便利です。</p><br />
<ul class="simple"><br />
<li>リスト8: <tt class="docutils literal"><span class="pre">$*</span></tt> でうまくいかない場合</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/hoge<br />
<span class="c">#!/bin/bash</span><br />
cat <span class="s2">&quot;$*&quot;</span><br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>chmod +x ./bin/hoge<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/hoge 201311.rst 201211.rst<br />
cat: 201311.rst 201211.rst: No such file or directory<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　使ってみましょう。リスト8のような出力が得られました。<br />
実際に使う場合は、 <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の出力から<br />
<tt class="docutils literal"><span class="pre">grep</span> <span class="pre">&quot;^-&quot;</span></tt> で「だである調」の行を抜き出し、<br />
目で検査することになるでしょう。<br />
もしこれで分からなければ、<br />
ファイル名と行番号が書いてあるので、<br />
当該のファイルを開いて前後の文脈を見ればよいことになります。</p><br />
<p>　ところで細かいですが、リスト8を見ると「でしょうか。」<br />
が「だである調」に分類されています。<br />
ただ、疑わしいものを抽出するという意味では、<br />
これでもいいでしょう（脚注：納得いかない場合は、<br />
「第一種過誤」と「第二種過誤」で検索を。）。</p><br />
<ul class="simple"><br />
<li>リスト8: <tt class="docutils literal"><span class="pre">deathmath2</span></tt> を使う</li><br />
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
15</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath2 | tail -n 3<br />
+ -:13184: //--dont-suggestを指定すると、候補が出てきません。<br />
+ -:13195: エディタを開かなくてもどこに疑わしい単語があるかチェックできます。<br />
+ -:13197: エディタから独立させておくと、思わぬところで助けられることがあります。<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/deathmath2 *.rst | tail -n 3<br />
+ 201311.rst:338: //--dont-suggestを指定すると、候補が出てきません。<br />
+ 201311.rst:349: エディタを開かなくてもどこに疑わしい単語があるかチェックできます。<br />
+ 201311.rst:351: エディタから独立させておくと、思わぬところで助けられることがあります。<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath2 | awk <span class="s1">&#39;{print $1}&#39;</span> | sort | uniq <br />
c-2268 +<br />
 33 -<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/deathmath2 *.rst | grep <span class="s2">&quot;^-&quot;</span> | head -n 3<br />
- 201202.rst:562: 寒さに負けず端末を叩いておられますでしょうか。<br />
- 201202.rst:565: ドア用の close コマンドがないものか。<br />
- 201202.rst:607: * プログラマの時間は貴重である。（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト8のように、 <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の出力を <tt class="docutils literal"><span class="pre">awk,</span> <span class="pre">sort,</span> <span class="pre">uniq</span></tt> で加工すると、<br />
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> のような答えが得られます。<br />
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> の方が、<br />
コマンド一発で数を数えてくれるので一見よさそうですが、</p><br />
<ul class="simple"><br />
<li>コマンドが二つに分かれると使う側として覚えるのが面倒</li><br />
<li>コマンドのコードが汚くなるのは作る側が面倒</li><br />
<li>そもそも数は最初に述べたように不正確</li><br />
</ul><br />
<p>ということで、筆者は <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の方がよいかなと考えます。<br />
UNIXのコマンドを作ったときの善し悪しは、<br />
他の主要なコマンドとの連携の上で決定されます。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h2>23.4. 英単語をチェックする<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　次に、英単語のスペルチェックを行うスクリプトを作ってみましょう。<br />
スペルチェッカーは通常、エディタから読み出して使いますが、<br />
ここではコマンド仕立てにします。<br />
作ると言っても、単にラッパーを作るだけですからご安心を。</p><br />
<p>　まず、スペルチェッカーをインストールします。<br />
一昔前、筆者の周辺の人はIspell<br />
というスペルチェッカーを使っていましたが、<br />
今はGNU Aspellというツールを用いるようです。<br />
MacだとHomebrewでリスト9のようにインストールできました。</p><br />
<ul class="simple"><br />
<li>リスト9: Aspell のインストール</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>brew install aspell<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　シェルスクリプトからAspellを使いたいので、<br />
対話形式ではなく、フィルタとして（= 標準入出力だけで）使えるかどうか調べます。<br />
<tt class="docutils literal"><span class="pre">man</span></tt> で調べると、リスト10のような記述と、他にパイプについての記述が見つかりました。<br />
どうやら <tt class="docutils literal"><span class="pre">-a</span></tt> を指定するとフィルタとして使えるようです。</p><br />
<ul class="simple"><br />
<li>リスト10: <tt class="docutils literal"><span class="pre">man</span></tt> でオプションを調査</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>man aspell<br />
（略）<br />
pipe, -a<br />
 Run Aspell in ispell -a compatibility mode.<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　試しに使ってみましょう。リスト11のように、環境変数 <tt class="docutils literal"><span class="pre">LANG</span></tt> を、<br />
デフォルトの <tt class="docutils literal"><span class="pre">C</span></tt> にしないと動きません。</p><br />
<ul class="simple"><br />
<li>リスト11: Aspell をフィルタモードで使う</li><br />
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
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;All your base are berong to us.&quot;</span> | <span class="nv">LANG</span><span class="o">=</span>C aspell -a<br />
\@<span class="o">(</span><span class="c">#) International Ispell Version 3.1.20 (but really Aspell 0.60.6.1)</span><br />
（略）<br />
*<br />
&amp; berong 25 18: Bering, bronc, belong, Behring, bearing, （略）<br />
//--dont-suggestを指定すると、候補が出てきません。<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;All your base are berong to us.&quot;</span> | <span class="nv">LANG</span><span class="o">=</span>C aspell -a --dont-suggest<br />
\@<span class="o">(</span><span class="c">#) International Ispell Version 3.1.20 (but really Aspell 0.60.6.1)</span><br />
（略）<br />
*<br />
<span class="c"># berong 18</span><br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　さて、これを使って、疑わしき単語のある行を行番号付きで<br />
出力するラッパーのシェルスクリプトを書いてみましょう。<br />
これができれば、とりあえず、<br />
エディタを開かなくてもどこに疑わしい単語があるかチェックできます。<br />
結局、エディタで開いて修正しなければならないかもしれませんが、<br />
エディタから独立させておくと、思わぬところで助けられることがあります。</p><br />
<p>　まず、補助的なコマンドとして、<br />
疑わしいスペルのリストを表示するコマンドをリスト12のように作ります。<br />
これはこれで独立で使えます。<br />
aspellはバッククォートなどの記号類にも反応する事があり、<br />
また、日本語が入ると何が起こるか分かったもんじゃないので、<br />
4行目の <tt class="docutils literal"><span class="pre">sed</span></tt> で、単語に使う文字だけ残してあとは空白に変換しています。</p><br />
<ul class="simple"><br />
<li>リスト12: 疑わしいスペル抽出コマンド</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell-list<br />
<span class="c">#!/bin/bash</span><br />
<br />
sed <span class="s2">&quot;s/[^a-zA-Z0-9&#39;]/ /g&quot;</span> <span class="s2">&quot;$\@&quot;</span> |<br />
<span class="nv">LANG</span><span class="o">=</span>C aspell -a --dont-suggest |<br />
awk <span class="s1">&#39;/^#/{print $2}&#39;</span> |<br />
sort -u<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　使ってみましょう。リスト13のようにまともな単語も引っかかりますが、<br />
これはAspellの辞書にこれらの単語を登録することで、<br />
出なくなります。</p><br />
<ul class="simple"><br />
<li>リスト13: <tt class="docutils literal"><span class="pre">henspell-list</span></tt> を使う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell-list 201311.rst<br />
FILENAME<br />
FNR<br />
<span class="o">(</span>略<span class="o">)</span><br />
berong<br />
<span class="o">(</span>略<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>　辞書ファイルいろいろ種類があるようですが、<br />
とりあえずリスト14のように、１行目におまじないを書いて、<br />
あとは引っかかった正しい単語をひたすら書いていくと作れます。</p><br />
<ul class="simple"><br />
<li>リスト14: Aspell の辞書ファイル</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>head -n 5 ./bin/dict<br />
personal_ws-1.1 en 0<br />
FILENAME<br />
FNR<br />
GENKOU<br />
Gancarz<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　これを <tt class="docutils literal"><span class="pre">henspell-list</span></tt> に読み込ませるとよいということになります。<br />
パスの指定が面倒ですが、コマンドのパスと一緒の所に置くなら、<br />
リスト15のように <tt class="docutils literal"><span class="pre">dirname</span></tt> というコマンドを使って指定できます。</p><br />
<ul class="simple"><br />
<li>リスト15: <tt class="docutils literal"><span class="pre">henspell-list</span></tt> を改良して使ってみる。</li><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell-list<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">dict</span><span class="o">=</span><span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/dict<br />
<br />
sed <span class="s2">&quot;s/[^a-zA-Z0-9&#39;]/ /g&quot;</span> <span class="s2">&quot;$\@&quot;</span> |<br />
<span class="nv">LANG</span><span class="o">=</span>C aspell -p <span class="s2">&quot;$dict&quot;</span> -a --dont-suggest |<br />
awk <span class="s1">&#39;/^#/{print $2}&#39;</span> |<br />
sort -u<br />
//使う<br />
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell-list 201311.rst<br />
berong<br />
da<br />
deathmeth<br />
dirname<br />
zA<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　次に、このコードを利用して、<br />
もとの原稿のどこに変なスペルがありそうなのかを表示します。<br />
リスト16に作成したコマンドを示します。<br />
このコードの場合は、標準入力から文字列を入力する場合と、<br />
ファイル名をオプションで指定する場合について、<br />
場合分けをせざるを得ませんでした。<br />
<tt class="docutils literal"><span class="pre">grep</span></tt> のオプションですが、<br />
<tt class="docutils literal"><span class="pre">-w</span></tt> は、単語の検索を行う（脚注：つまり検索語がmarchでも、<br />
部分一致のdeathmarchは引っかからないということです。）、<br />
<tt class="docutils literal"><span class="pre">-n</span></tt> は行番号を入れる、<br />
<tt class="docutils literal"><span class="pre">-f</span> <span class="pre">&lt;FILE&gt;</span></tt> が検索対象の文字列を <tt class="docutils literal"><span class="pre">FILE</span></tt><br />
から読み込む、です。</p><br />
<ul class="simple"><br />
<li>リスト16: <tt class="docutils literal"><span class="pre">henspell</span></tt></li><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell<br />
<span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<br />
<span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$#&quot;</span> -eq 0 <span class="o">]</span> ; <span class="k">then</span><br />
<span class="k"> </span>cat &lt; /dev/stdin |<br />
 tee <span class="nv">$tmp</span>-stdin |<br />
 <span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/henspell-list &gt; <span class="nv">$tmp</span>-list<br />
 grep -w -n -f <span class="nv">$tmp</span>-list &lt; <span class="nv">$tmp</span>-stdin<br />
<span class="k">else</span><br />
 <span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/henspell-list <span class="s2">&quot;$\@&quot;</span> &gt; <span class="nv">$tmp</span>-list<br />
 grep -w -n -f <span class="nv">$tmp</span>-list <span class="s2">&quot;$\@&quot;</span><br />
<span class="k">fi</span><br />
<br />
rm <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　利用するときはリスト17のように <tt class="docutils literal"><span class="pre">less</span></tt> で受けて、<br />
本当にスペルミスがないか探す事になるでしょう。<br />
リスト中のミスは、「仕込み」です。</p><br />
<ul class="simple"><br />
<li>リスト17: <tt class="docutils literal"><span class="pre">henspell</span></tt> を使う</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell 201311.rst | less<br />
14:Macには、GNU sed（ <span class="sb">``</span>gdes<span class="sb">``</span> ）がインストールされているものとします。<br />
87: <span class="nv">da</span><span class="o">=</span><span class="s2">&quot;(だ。|である。|ない。|か。)&quot;</span><br />
...<br />
217:<span class="sb">``</span>deathmarch2<span class="sb">``</span> がもらったオプションをそのまま <span class="sb">``</span>awk<span class="sb">``</span><br />
...<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>23.5. おわりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、シェルスクリプトで文章チェックのためのコマンドを作ってみました。<br />
文章の仕事というのは、そのときそのときで特殊な作業が必要になることが多いので、<br />
今回のようにシェルスクリプトでコマンドを作ることを覚えると、<br />
1日かけていた作業が数秒で終わるという幸運なことに何回か巡り会うことができます。<br />
シェルスクリプトでコマンドを作ると他のコマンドも呼び出せますから、<br />
この方法はオススメです。</p><br />
<p>　一方、今回のようにコマンドを自作しても、<br />
後日使い回すことになることはあまり無いかもしれません。<br />
<tt class="docutils literal"><span class="pre">grep</span></tt> の使い方は忘れることはないでしょうが、<br />
ニッチな自作コマンドなど、すぐに使い方を忘れてしまうものです。</p><br />
<p>　それはそれでいいと思います。<br />
もし100個自作して、1個お気に入りのコマンドになれば、<br />
そのコマンドは何年にもわたって永続的に力になるわけですから、<br />
たとえ生存率1/100であっても、御利益はあるのです。</p><br />
<p>　次回はcrontabの使い方を扱います。</p><br />
</div><br />
</div><br />

