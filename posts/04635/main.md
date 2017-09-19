---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年11月号
出典: 技術評論社SoftwareDesign

 
 <div class="section" id="id1">
<h1>23. 開眼シェルスクリプト 第23回 表記揺れ・綴りをチェックする<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　前回「文章を扱う」というお題でコマンドの操作をいくつか紹介しました。
今回は「文章を扱う道具」つまりコマンドをシェルスクリプトで作ってみます。</p>
<p>　作るコマンドは語尾のチェックコマンドとスペルチェックのコマンドです。
いずれのコマンドも、既存のコマンドをうまく組み合わせて、
短いものを作ります。</p>
<p>　今回はコマンド作者となるわけですから、
GancarzのUNIX哲学（脚注：<a class="reference external" href="http://ja.wikipedia.org/wiki">http://ja.wikipedia.org/wiki</a>/UNIX哲学）
を全部頭に叩き込んで、先にお進み下さい。
特に、</p>
<ul class="simple">
<li>各プログラムが一つのことをうまくやるようにせよ。</li>
<li>全てのプログラムはフィルタとして振る舞うようにせよ。</li>
</ul>
<p>が大事です。</p>
<div class="section" id="id2">
<h2>23.1. 環境等<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、Macに溜まった開眼シェルスクリプトの原稿について、
いろいろチェックするものを作っていきます。
Macには、GNU sed（ <tt class="docutils literal"><span class="pre">gsed</span></tt> ）とGNU awk （ <tt class="docutils literal"><span class="pre">gawk</span></tt> ）
がインストールされているものとします。
リスト1に環境を示します。</p>
<ul class="simple">
<li>リスト1: 環境</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.4.0 Darwin Kernel Version 12.4.0: Wed May 1 17:57:12 PDT 2013; root:xnu-2050.24.15~1/RELEASE_X86_64 x86_64
uedamac:SD_GENKOU ueda<span class="nv">$ </span>gsed --version
gsed <span class="o">(</span>GNU sed<span class="o">)</span> 4.2.2
（略）
uedamac:SD_GENKOU ueda<span class="nv">$ </span>gawk --version
GNU Awk 4.1.0, API: 1.0
Copyright <span class="o">(</span>C<span class="o">)</span> 1989, 1991-2013 Free Software Foundation.
</pre></div>
</td></tr></table></div>
<p>　原稿はテキストファイルです。
reStructuredText という形式でマークアップされていますが、
それはあまり気にしなくて大丈夫です。
拡張子はリスト2のように <tt class="docutils literal"><span class="pre">.rst</span></tt> です。</p>
<ul class="simple">
<li>リスト2: 原稿のファイル</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>ls *.rst
201201.rst 201210.rst 201306.rst
201202.rst 201211.rst 201306SPECIAL.rst
201203.rst 201212.rst 201307.rst
（略）
</pre></div>
</td></tr></table></div>
<blockquote>
<div></div></blockquote>
<p>原稿にはリスト3のように、
だいたい30字くらいで改行を入れています。</p>
<ul class="simple">
<li>リスト3: 原稿</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>tail -n 5 201302.rst
lsとwcを使えば事足ります。captiveでないので、なんとかなります。

　今回は正直言いまして、
かなりエクストリームなプログラミングになってしまいましたので、
次回からはもうちょっとマイルドな話題を扱いたいと思います。
</pre></div>
</td></tr></table></div>
<p>　コマンド等、作ったものはディレクトリ <tt class="docutils literal"><span class="pre">SD_GENKOU</span></tt> の下に <tt class="docutils literal"><span class="pre">bin</span></tt>
というディレクトリを作ってそこに置く事にします。</p>
</div>
<div class="section" id="id3">
<h2>23.2. ですます・だであるチェック<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　まず、表記揺れの基本中の基本、
「ですます調」と「だである調」
のチェックを行うシェルスクリプトを作ってみましょう。
「です。」「ます。」等の数を数え、
次に「だ。」「である。」等の数を数え、
どちらも1以上だったら「怪しい」という簡素なものです。</p>
<p>　まずはリスト4のように作ってみましょう。
これだと、例えば一行に「です。」が2回出てきても1とカウントされますが、
自分で使うには十分でしょう。
もちろん、たとえばこれを公開しようとすれば、
いろいろ細かく修正が必要です。</p>
<ul class="simple">
<li>リスト4: 語尾を数えるコマンド</li>
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
23</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201311 ueda<span class="nv">$ </span>cat deathmath1
<span class="c">#!/bin/bash</span>

<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

cat &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-text

<span class="nv">death</span><span class="o">=</span><span class="s2">&quot;(です。|ます。|でした。|ました。|でしょう。|ません。)&quot;</span>
<span class="nv">da</span><span class="o">=</span><span class="s2">&quot;(だ。|である。|ない。|か。)&quot;</span>

grep -E <span class="s2">&quot;$death&quot;</span> <span class="nv">$tmp</span>-text |
wc -l |
tr -d <span class="s1">&#39; &#39;</span> &gt; <span class="nv">$tmp</span>-death

grep -E <span class="s2">&quot;$da&quot;</span> <span class="nv">$tmp</span>-text |
wc -l |
tr -d <span class="s1">&#39; &#39;</span> &gt; <span class="nv">$tmp</span>-da

<span class="nb">echo</span> <span class="s2">&quot;ですます&quot;</span> <span class="k">$(</span>cat <span class="nv">$tmp</span>-death<span class="k">)</span>
<span class="nb">echo</span> <span class="s2">&quot;だである&quot;</span> <span class="k">$(</span>cat <span class="nv">$tmp</span>-da<span class="k">)</span>

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　 コードの説明をしておくと、6行目で標準入力を <tt class="docutils literal"><span class="pre">$tmp-text</span></tt>
に一度溜めています。
<tt class="docutils literal"><span class="pre">$tmp-text</span></tt> は <tt class="docutils literal"><span class="pre">/tmp/</span></tt> 下のファイルですが、
このコードだと <tt class="docutils literal"><span class="pre">/tmp/</span></tt> 下にファイルが残ってしまう可能性があります。
不特性多数の人々が使うUNIX環境のときは別のところに
一時ファイルを置きましょう。
今はあまりそういうこともないでしょうが、一応お断りを。
6行目の「 <tt class="docutils literal"><span class="pre">&lt;</span> <span class="pre">/dev/stdin</span></tt> 」は、
このシェルスクリプトの標準入力を読み込むリダイレクトですが、
書かなくても <tt class="docutils literal"><span class="pre">cat</span></tt> が標準入力を読んでくれます。
筆者はそれだと分かりにくいので、明記しています。</p>
<p>　8,9行目で、正規表現を作ります。
語尾はたくさん種類があるので、ここにずらずら並べておきます。
おそらく全部網羅することは難しいし、
きりがないので自分の困らない範囲で列挙しておけばよいでしょう。
ただ、全く対処できないかというとそうでもなく、
例えばリスト5のようにワンライナーで語尾を抽出して、
後から解析することはできます。
身も蓋もないことを言うと、
形態素解析のコマンドをシェルスクリプトの中で使うと
完璧に近いものができるかもしれません。
それがシェルスクリプトの良いところなので、
使えるものは何でも使いましょう。</p>
<ul class="simple">
<li>リスト5: 語尾を抽出</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:201311 ueda<span class="nv">$ </span>cat ../*.rst |
gsed <span class="s1">&#39;s/....。/\\n&amp;\\n/g&#39;</span> | grep 。|
sed <span class="s1">&#39;s/。.*/。/&#39;</span> | sort -u
（略）
（縦）軸。
（？）を。
）を作れ。
）を知る。
：私です。
</pre></div>
</td></tr></table></div>
<p>　使ってみましょう。リスト6は実行例です。
原稿はですます調で書かれていますが、1.5%程度、
したがっていない部分があるように見えます。</p>
<ul class="simple">
<li>リスト6: <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath1
ですます 2252
だである 32
</pre></div>
</td></tr></table></div>
<blockquote>
<div></div></blockquote>
</div>
<div class="section" id="id4">
<h2>23.3. コマンドを書き直す<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、「だ、である」がちょっと混ざっているようなのですが、
今度はどこを修正しなければならないのか知りたくなってきます。
<tt class="docutils literal"><span class="pre">grep</span></tt> を使えばよいのですが、
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> では8,9行目で複数の語尾を指定しているので、
これをいちいち手打ちするのは面倒くさいし、
いちいち覚えてられません。
コマンドを新たに作るか、 <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を拡張するか、
どちらかをした方がよいでしょう。</p>
<p>　ここで、「コマンドの作り手」はとても悩みます。
コマンドは単機能にしておく方が、
後から手を入れるときに楽です。肥大化もしません。
これはGancarzのUNIX哲学にもあります。
例えば、 <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を拡張するとなると、
オプションを新たに設けなければいけませんし、
追加箇所と既存の箇所を分けるために、
関数で分けなければなりません。
つまり、余計な情報を追加しなければなりません。</p>
<p>　一方でコマンドを新たに作るとなると、
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> の8,9行目にある変数をうまく共有する仕組みが必要です。
しかし今のところ、わざわざ辞書ファイルを外に出すほどのものでもありません。</p>
<p>　筆者の出した答えは次のようなものです。</p>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">deathmath1</span></tt> を、行数でなく、当該箇所を出力するように書き直し</li>
<li>行数を数えたかったら、他のコマンドで</li>
</ul>
<p>　つまるところ、筆者は <tt class="docutils literal"><span class="pre">deathmath1</span></tt> が「作り過ぎ」だったと判断しました。
せっかく作った <tt class="docutils literal"><span class="pre">deathmath1</span></tt> を放棄して、手戻りをします。
普通、雑誌にコードをのっけるときはこういう放棄はしないものですが、
こういう考え方でツールを改善する例ですので容赦ください。</p>
<p>　作り直し版では、 <tt class="docutils literal"><span class="pre">grep</span></tt> を使うと中間ファイルを作らざるを得ず面倒なので、
<tt class="docutils literal"><span class="pre">awk</span></tt> で印をつける方式に変更します。
リスト7のようにしました。</p>
<ul class="simple">
<li>リスト7: <tt class="docutils literal"><span class="pre">deathmath2</span></tt></li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8
9</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/deathmath2
<span class="c">#!/bin/bash</span>

<span class="nv">death</span><span class="o">=</span><span class="s2">&quot;です。|ます。|でしょう。|ません。&quot;</span>
<span class="nv">da</span><span class="o">=</span><span class="s2">&quot;だ。|である。|ない。|か。&quot;</span>

gawk <span class="s1">&#39;{print FILENAME &quot;:&quot; FNR &quot;:&quot; ,$0}&#39;</span> <span class="s2">&quot;$\@&quot;</span> |
gawk -v <span class="nv">death</span><span class="o">=</span><span class="nv">$death</span> -v <span class="nv">da</span><span class="o">=</span><span class="nv">$da</span> <span class="se">\\</span>
 <span class="s1">&#39;$0~death{print &quot;+&quot;,$0}$0~da{print &quot;-&quot;,$0}&#39;</span>
</pre></div>
</td></tr></table></div>
<p>　リスト7のコードについて補足説明しておきます。
まず、7行目の <tt class="docutils literal"><span class="pre">&quot;$&#64;&quot;</span></tt> は、
<tt class="docutils literal"><span class="pre">deathmath2</span></tt> がもらったオプションをそのまま <tt class="docutils literal"><span class="pre">awk</span></tt>
に渡すための方法です。 <tt class="docutils literal"><span class="pre">&quot;$*&quot;</span></tt> だと、
複数のファイル名がオプションに入っている場合、
うまくいきません。
ファイル名がずらずら並んだ文字列を一個のオプションとみなすからです。
リスト8の例では、 <tt class="docutils literal"><span class="pre">&quot;201311.rst</span> <span class="pre">201211.rst&quot;</span></tt>
が一つのファイル名だと解釈されるため、
<tt class="docutils literal"><span class="pre">cat</span></tt> がエラーを出します。
ところで、この方法は面白いことに、ファイル名を指定せずに、
標準入力からの文字列を入力しても動作します。
このときは、 <tt class="docutils literal"><span class="pre">&quot;$&#64;&quot;</span></tt> が空になり、
その場合、 <tt class="docutils literal"><span class="pre">gawk</span></tt> はオプション無しと判断して標準入力を読みに行きます。</p>
<p>　次に、検索で引っ掛ける文字列は4,5行目で、
bashの変数として定義しています。
これを12行目で <tt class="docutils literal"><span class="pre">gawk</span></tt> に引き渡しています。
正規表現を変数に渡しているわけですが、
<tt class="docutils literal"><span class="pre">/</span></tt> は不要なようです。</p>
<p>　7行目の <tt class="docutils literal"><span class="pre">FNR</span></tt> は行番号が格納された変数ですが、
<tt class="docutils literal"><span class="pre">NR</span></tt> と違って、読み込んだファイルごとの行番号が格納されます。
ですので、この例のように「あるファイルの何行目」
を出力するときに便利です。</p>
<ul class="simple">
<li>リスト8: <tt class="docutils literal"><span class="pre">$*</span></tt> でうまくいかない場合</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/hoge
<span class="c">#!/bin/bash</span>
cat <span class="s2">&quot;$*&quot;</span>
uedamac:SD_GENKOU ueda<span class="nv">$ </span>chmod +x ./bin/hoge
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/hoge 201311.rst 201211.rst
cat: 201311.rst 201211.rst: No such file or directory
</pre></div>
</td></tr></table></div>
<p>　使ってみましょう。リスト8のような出力が得られました。
実際に使う場合は、 <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の出力から
<tt class="docutils literal"><span class="pre">grep</span> <span class="pre">&quot;^-&quot;</span></tt> で「だである調」の行を抜き出し、
目で検査することになるでしょう。
もしこれで分からなければ、
ファイル名と行番号が書いてあるので、
当該のファイルを開いて前後の文脈を見ればよいことになります。</p>
<p>　ところで細かいですが、リスト8を見ると「でしょうか。」
が「だである調」に分類されています。
ただ、疑わしいものを抽出するという意味では、
これでもいいでしょう（脚注：納得いかない場合は、
「第一種過誤」と「第二種過誤」で検索を。）。</p>
<ul class="simple">
<li>リスト8: <tt class="docutils literal"><span class="pre">deathmath2</span></tt> を使う</li>
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
15</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath2 | tail -n 3
+ -:13184: //--dont-suggestを指定すると、候補が出てきません。
+ -:13195: エディタを開かなくてもどこに疑わしい単語があるかチェックできます。
+ -:13197: エディタから独立させておくと、思わぬところで助けられることがあります。
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/deathmath2 *.rst | tail -n 3
+ 201311.rst:338: //--dont-suggestを指定すると、候補が出てきません。
+ 201311.rst:349: エディタを開かなくてもどこに疑わしい単語があるかチェックできます。
+ 201311.rst:351: エディタから独立させておくと、思わぬところで助けられることがあります。
uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat *.rst | ./bin/deathmath2 | awk <span class="s1">&#39;{print $1}&#39;</span> | sort | uniq 
c-2268 +
 33 -
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/deathmath2 *.rst | grep <span class="s2">&quot;^-&quot;</span> | head -n 3
- 201202.rst:562: 寒さに負けず端末を叩いておられますでしょうか。
- 201202.rst:565: ドア用の close コマンドがないものか。
- 201202.rst:607: * プログラマの時間は貴重である。（略）
</pre></div>
</td></tr></table></div>
<p>　リスト8のように、 <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の出力を <tt class="docutils literal"><span class="pre">awk,</span> <span class="pre">sort,</span> <span class="pre">uniq</span></tt> で加工すると、
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> のような答えが得られます。
<tt class="docutils literal"><span class="pre">deathmath1</span></tt> の方が、
コマンド一発で数を数えてくれるので一見よさそうですが、</p>
<ul class="simple">
<li>コマンドが二つに分かれると使う側として覚えるのが面倒</li>
<li>コマンドのコードが汚くなるのは作る側が面倒</li>
<li>そもそも数は最初に述べたように不正確</li>
</ul>
<p>ということで、筆者は <tt class="docutils literal"><span class="pre">deathmath2</span></tt> の方がよいかなと考えます。
UNIXのコマンドを作ったときの善し悪しは、
他の主要なコマンドとの連携の上で決定されます。</p>
</div>
<div class="section" id="id5">
<h2>23.4. 英単語をチェックする<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　次に、英単語のスペルチェックを行うスクリプトを作ってみましょう。
スペルチェッカーは通常、エディタから読み出して使いますが、
ここではコマンド仕立てにします。
作ると言っても、単にラッパーを作るだけですからご安心を。</p>
<p>　まず、スペルチェッカーをインストールします。
一昔前、筆者の周辺の人はIspell
というスペルチェッカーを使っていましたが、
今はGNU Aspellというツールを用いるようです。
MacだとHomebrewでリスト9のようにインストールできました。</p>
<ul class="simple">
<li>リスト9: Aspell のインストール</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>brew install aspell
</pre></div>
</td></tr></table></div>
<p>　シェルスクリプトからAspellを使いたいので、
対話形式ではなく、フィルタとして（= 標準入出力だけで）使えるかどうか調べます。
<tt class="docutils literal"><span class="pre">man</span></tt> で調べると、リスト10のような記述と、他にパイプについての記述が見つかりました。
どうやら <tt class="docutils literal"><span class="pre">-a</span></tt> を指定するとフィルタとして使えるようです。</p>
<ul class="simple">
<li>リスト10: <tt class="docutils literal"><span class="pre">man</span></tt> でオプションを調査</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>man aspell
（略）
pipe, -a
 Run Aspell in ispell -a compatibility mode.
</pre></div>
</td></tr></table></div>
<p>　試しに使ってみましょう。リスト11のように、環境変数 <tt class="docutils literal"><span class="pre">LANG</span></tt> を、
デフォルトの <tt class="docutils literal"><span class="pre">C</span></tt> にしないと動きません。</p>
<ul class="simple">
<li>リスト11: Aspell をフィルタモードで使う</li>
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
12</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;All your base are berong to us.&quot;</span> | <span class="nv">LANG</span><span class="o">=</span>C aspell -a
\@<span class="o">(</span><span class="c">#) International Ispell Version 3.1.20 (but really Aspell 0.60.6.1)</span>
（略）
*
&amp; berong 25 18: Bering, bronc, belong, Behring, bearing, （略）
//--dont-suggestを指定すると、候補が出てきません。
uedamac:SD_GENKOU ueda<span class="nv">$ </span><span class="nb">echo</span> <span class="s2">&quot;All your base are berong to us.&quot;</span> | <span class="nv">LANG</span><span class="o">=</span>C aspell -a --dont-suggest
\@<span class="o">(</span><span class="c">#) International Ispell Version 3.1.20 (but really Aspell 0.60.6.1)</span>
（略）
*
<span class="c"># berong 18</span>
（略）
</pre></div>
</td></tr></table></div>
<p>　さて、これを使って、疑わしき単語のある行を行番号付きで
出力するラッパーのシェルスクリプトを書いてみましょう。
これができれば、とりあえず、
エディタを開かなくてもどこに疑わしい単語があるかチェックできます。
結局、エディタで開いて修正しなければならないかもしれませんが、
エディタから独立させておくと、思わぬところで助けられることがあります。</p>
<p>　まず、補助的なコマンドとして、
疑わしいスペルのリストを表示するコマンドをリスト12のように作ります。
これはこれで独立で使えます。
aspellはバッククォートなどの記号類にも反応する事があり、
また、日本語が入ると何が起こるか分かったもんじゃないので、
4行目の <tt class="docutils literal"><span class="pre">sed</span></tt> で、単語に使う文字だけ残してあとは空白に変換しています。</p>
<ul class="simple">
<li>リスト12: 疑わしいスペル抽出コマンド</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell-list
<span class="c">#!/bin/bash</span>

sed <span class="s2">&quot;s/[^a-zA-Z0-9&#39;]/ /g&quot;</span> <span class="s2">&quot;$\@&quot;</span> |
<span class="nv">LANG</span><span class="o">=</span>C aspell -a --dont-suggest |
awk <span class="s1">&#39;/^#/{print $2}&#39;</span> |
sort -u
</pre></div>
</td></tr></table></div>
<p>　使ってみましょう。リスト13のようにまともな単語も引っかかりますが、
これはAspellの辞書にこれらの単語を登録することで、
出なくなります。</p>
<ul class="simple">
<li>リスト13: <tt class="docutils literal"><span class="pre">henspell-list</span></tt> を使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell-list 201311.rst
FILENAME
FNR
<span class="o">(</span>略<span class="o">)</span>
berong
<span class="o">(</span>略<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>　辞書ファイルいろいろ種類があるようですが、
とりあえずリスト14のように、１行目におまじないを書いて、
あとは引っかかった正しい単語をひたすら書いていくと作れます。</p>
<ul class="simple">
<li>リスト14: Aspell の辞書ファイル</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>head -n 5 ./bin/dict
personal_ws-1.1 en 0
FILENAME
FNR
GENKOU
Gancarz
（略）
</pre></div>
</td></tr></table></div>
<p>　これを <tt class="docutils literal"><span class="pre">henspell-list</span></tt> に読み込ませるとよいということになります。
パスの指定が面倒ですが、コマンドのパスと一緒の所に置くなら、
リスト15のように <tt class="docutils literal"><span class="pre">dirname</span></tt> というコマンドを使って指定できます。</p>
<ul class="simple">
<li>リスト15: <tt class="docutils literal"><span class="pre">henspell-list</span></tt> を改良して使ってみる。</li>
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
16</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell-list
<span class="c">#!/bin/bash</span>

<span class="nv">dict</span><span class="o">=</span><span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/dict

sed <span class="s2">&quot;s/[^a-zA-Z0-9&#39;]/ /g&quot;</span> <span class="s2">&quot;$\@&quot;</span> |
<span class="nv">LANG</span><span class="o">=</span>C aspell -p <span class="s2">&quot;$dict&quot;</span> -a --dont-suggest |
awk <span class="s1">&#39;/^#/{print $2}&#39;</span> |
sort -u
//使う
uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell-list 201311.rst
berong
da
deathmeth
dirname
zA
</pre></div>
</td></tr></table></div>
<p>　次に、このコードを利用して、
もとの原稿のどこに変なスペルがありそうなのかを表示します。
リスト16に作成したコマンドを示します。
このコードの場合は、標準入力から文字列を入力する場合と、
ファイル名をオプションで指定する場合について、
場合分けをせざるを得ませんでした。
<tt class="docutils literal"><span class="pre">grep</span></tt> のオプションですが、
<tt class="docutils literal"><span class="pre">-w</span></tt> は、単語の検索を行う（脚注：つまり検索語がmarchでも、
部分一致のdeathmarchは引っかからないということです。）、
<tt class="docutils literal"><span class="pre">-n</span></tt> は行番号を入れる、
<tt class="docutils literal"><span class="pre">-f</span> <span class="pre">&lt;FILE&gt;</span></tt> が検索対象の文字列を <tt class="docutils literal"><span class="pre">FILE</span></tt>
から読み込む、です。</p>
<ul class="simple">
<li>リスト16: <tt class="docutils literal"><span class="pre">henspell</span></tt></li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>cat ./bin/henspell
<span class="c">#!/bin/bash</span>

<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>

<span class="k">if</span> <span class="o">[</span> <span class="s2">&quot;$#&quot;</span> -eq 0 <span class="o">]</span> ; <span class="k">then</span>
<span class="k"> </span>cat &lt; /dev/stdin |
 tee <span class="nv">$tmp</span>-stdin |
 <span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/henspell-list &gt; <span class="nv">$tmp</span>-list
 grep -w -n -f <span class="nv">$tmp</span>-list &lt; <span class="nv">$tmp</span>-stdin
<span class="k">else</span>
 <span class="k">$(</span>dirname <span class="nv">$0</span><span class="k">)</span>/henspell-list <span class="s2">&quot;$\@&quot;</span> &gt; <span class="nv">$tmp</span>-list
 grep -w -n -f <span class="nv">$tmp</span>-list <span class="s2">&quot;$\@&quot;</span>
<span class="k">fi</span>

rm <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　利用するときはリスト17のように <tt class="docutils literal"><span class="pre">less</span></tt> で受けて、
本当にスペルミスがないか探す事になるでしょう。
リスト中のミスは、「仕込み」です。</p>
<ul class="simple">
<li>リスト17: <tt class="docutils literal"><span class="pre">henspell</span></tt> を使う</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:SD_GENKOU ueda<span class="nv">$ </span>./bin/henspell 201311.rst | less
14:Macには、GNU sed（ <span class="sb">``</span>gdes<span class="sb">``</span> ）がインストールされているものとします。
87: <span class="nv">da</span><span class="o">=</span><span class="s2">&quot;(だ。|である。|ない。|か。)&quot;</span>
...
217:<span class="sb">``</span>deathmarch2<span class="sb">``</span> がもらったオプションをそのまま <span class="sb">``</span>awk<span class="sb">``</span>
...
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id6">
<h2>23.5. おわりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、シェルスクリプトで文章チェックのためのコマンドを作ってみました。
文章の仕事というのは、そのときそのときで特殊な作業が必要になることが多いので、
今回のようにシェルスクリプトでコマンドを作ることを覚えると、
1日かけていた作業が数秒で終わるという幸運なことに何回か巡り会うことができます。
シェルスクリプトでコマンドを作ると他のコマンドも呼び出せますから、
この方法はオススメです。</p>
<p>　一方、今回のようにコマンドを自作しても、
後日使い回すことになることはあまり無いかもしれません。
<tt class="docutils literal"><span class="pre">grep</span></tt> の使い方は忘れることはないでしょうが、
ニッチな自作コマンドなど、すぐに使い方を忘れてしまうものです。</p>
<p>　それはそれでいいと思います。
もし100個自作して、1個お気に入りのコマンドになれば、
そのコマンドは何年にもわたって永続的に力になるわけですから、
たとえ生存率1/100であっても、御利益はあるのです。</p>
<p>　次回はcrontabの使い方を扱います。</p>
</div>
</div>

