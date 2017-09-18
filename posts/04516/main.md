---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年7月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>7. 開眼シェルスクリプト 第7回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>7.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回の開眼シェルスクリプトは、なにかしらの重要なファイルを上書き更新するシェルスクリプトを扱います。<br />
ファイルを更新するということは「覆水盆に返らず」ですので、それなりに気を使うべきです。<br />
今回はシェルスクリプトを使って安全に更新する方法を扱います。</p><br />
<div class="section" id="id3"><br />
<h3>7.1.1. コマンドはファイルを上書きしない<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　たまにtwitterなどで「ファイルを直接更新するコマンドはないのか？」<br />
という発言を捕捉することがあります。<br />
つまり、下のような例で、ファイル <tt class="docutils literal"><span class="pre">file</span></tt> が変更できないのかということでしょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">command </span>file<br />
</pre></div><br />
</div><br />
<p>　UNIX系OSにおいては、このようなコマンドは少数派です。<br />
sedやnkfコマンドは上書きができますが、オプションを指定しないと上書きモードになりません。</p><br />
<p>　ファイル上書きをむやみに許してしまうと、次のようになにかと不都合です。</p><br />
<ul class="simple"><br />
<li>パイプ接続できるコマンドとできないコマンドの識別する労力が増大</li><br />
<li>なにか失敗すると後戻り不可能。あるいは面倒</li><br />
</ul><br />
<p>　ファイルを上書きしたいときは、面倒でも次のような手続きを踏みます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">command </span>file &gt; file.new<br />
<span class="nv">$ </span>mv file.new file<br />
</pre></div><br />
</div><br />
<p>もし必要なら、mvの前にdiffをとって確認したり、<br />
もとのファイルのバックアップをとったりします。<br />
逆に言えば、そのような機会が必ず用意されるという点で、<br />
一度別のファイルに結果を出力してからmvする方法は合理的と言えます。<br />
シェルスクリプトでも、同様の手続きを踏みます。</p><br />
<p>　もういい加減ネタ切れですが、今回も格言（？）を。</p><br />
<ul class="simple"><br />
<li>覆水盆に返らず &#8212;呂尚</li><br />
<li>いきなり盆をひっくり返すから盆に返らないだけ &#8212;筆者</li><br />
</ul><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>7.2. お題：会員管理を自動化する<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　前回に引き続き、架空の団体「UPS友の会」の会員管理を扱います。<br />
前回は手動で会員リストを操作しましたが、<br />
今回は会員リストへの新会員の追加処理をシェルスクリプト化します。<br />
シェルスクリプトでは、会員リストを上書きするときに会員リストを壊さないように、<br />
様々な仕掛けをします。これまでの連載では、<br />
ほとんど一直線のパイプライン処理ばかり扱っていましたが、<br />
今回は細かい文法をいくつか知っておく必要があります。<br />
細かくなると、文法がシェルごとに違うことがありますが、<br />
今回はbashの文法を使います。</p><br />
<div class="section" id="id5"><br />
<h3>7.2.1. 準備<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は、リスト1の環境でプログラムを組んで動作させます。</p><br />
<p>↓リスト1: 環境</p><br />
<div class="highlight-bash"><div class="highlight"><pre>ueda\@uedaubuntu:~<span class="nv">$ </span>bash --version | head -n 1<br />
GNU bash, バージョン 4.2.10<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>i686-pc-linux-gnu<span class="o">)</span><br />
ueda\@uedaubuntu:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span><br />
ja_JP.UTF-8<br />
ueda\@uedaubuntu:~<span class="nv">$ </span>lsb_release -a | grep Description<br />
Description: Ubuntu 11.10<br />
</pre></div><br />
</div><br />
<p>　まず、ディレクトリを準備をします。<br />
適当な場所に、リスト2のようにディレクトリを掘ります。</p><br />
<ul class="simple"><br />
<li>SCR: シェルスクリプト（ADDMEMBERファイル）置き場</li><br />
<li>DATA：会員リスト（MEMBERファイル）の置き場所</li><br />
</ul><br />
<p>↓リスト2: ディレクトリ</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre>UPSTOMO/<br />
├── DATA<br />
│ └── MEMBER<br />
├── SCR<br />
│ └── ADDMEMBER<br />
└── newmember<br />
</pre></div><br />
</td></tr></table></div><br />
<p>newmemberは、新しく追加する会員のリストで、一時的なのものです（リスト3）。</p><br />
<p>↓リスト3: 新規会員を書いたファイル</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat newmember<br />
門田 kadota\@paa-league.net<br />
香川 kagawa\@dokaben.com<br />
</pre></div><br />
</td></tr></table></div><br />
<p>MEMBERファイルには、次のような既存会員データが記録されています（リスト4）。<br />
このファイルが原本です。</p><br />
<p>↓リスト4: 会員リスト</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#1:会員番号 2:氏名（簡略化のため姓のみ） 3:e-mailアドレス</span><br />
<span class="c">#4:入会処理日 5:退会処理日</span><br />
<span class="nv">$ </span>head -n 5 ./DATA/MEMBER<br />
10000001 上田 ueda\@hogehoge.com 19720103 -<br />
10000002 濱田 hamada\@nullnull.com 19831102 -<br />
10000003 武田 takeda\@takenaka.com 19930815 20120104<br />
10000004 竹中 takenaka\@takeda.com 19980423 -<br />
10000005 田中 tanaka\@kakuei.jp 20000111 -<br />
</pre></div><br />
</td></tr></table></div><br />
<p>newmemberファイルのデータに会員番号と入会処理日をつけて、<br />
MEMBERファイルに追記するのが、ADDMEMBER の役目です。<br />
MEMBERファイルを壊してはいけませんので、<br />
入力をチェックしてから追記処理をしなくてはなりません。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>7.2.2. 準備<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まず、シェルスクリプトADDMEMBERに、<br />
リスト5のようにエラーを検知する仕組みを書きます。</p><br />
<p>↓リスト5: エラー検知処理を書く</p><br />
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<br />
CHECK<span class="o">(){</span><br />
 <span class="o">[</span> -z <span class="s2">&quot;$(echo ${PIPESTATUS[\@]} | tr -d &#39;0 &#39;)&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span><br />
<br />
<span class="k"> </span><span class="nb">echo</span> <span class="s2">&quot;エラー: $1&quot;</span> &gt;&amp;2<br />
 <span class="nb">echo</span> 処理できませんでした。&gt;&amp;2<br />
 rm -f <span class="nv">$tmp</span>-*<br />
 <span class="nb">exit </span>1<br />
<span class="o">}</span><br />
<br />
<span class="c">#テスト</span><br />
<span class="nb">true</span> | <span class="nb">true</span><br />
CHECK これは成功する。<br />
<br />
<span class="nb">true</span> | <span class="nb">false</span><br />
CHECK <span class="nb">false</span>で失敗<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　5～12行目はbashの関数です。<br />
書き方はリスト1のように、 <tt class="docutils literal"><span class="pre">名前(){処理}</span></tt> となります。<br />
呼び出し方はコマンドと一緒で、名前を行頭に書きます。<br />
引数は <tt class="docutils literal"><span class="pre">()</span></tt> 内で定義せず、関数内で <tt class="docutils literal"><span class="pre">$1,</span> <span class="pre">$2,</span> <span class="pre">...</span></tt> と呼び出します。<br />
例えば、19行目で <tt class="docutils literal"><span class="pre">CHECK</span> <span class="pre">falseで失敗</span></tt> と記述されていますが、<br />
「falseで失敗」は、CHECK関数の第一引数で、関数内で$1として呼び出せます。<br />
リスト5では、8行目で$1を使っています。</p><br />
<p>　エラーメッセージは、標準エラー出力に出すのが行儀良いでしょう。<br />
8,9行目のように、 <tt class="docutils literal"><span class="pre">&gt;&amp;2</span></tt> と書くことで、<br />
echoの出力先を標準エラー出力にリダイレクトできます。<br />
基本的に、標準出力はコマンド（コンピュータ）のため、<br />
標準エラー出力は人間が読むために使います。</p><br />
<p>　6行目の呪文を一つずつ紐解いていきましょう。<br />
まず <tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt><br />
は、パイプでつながったコマンドの終了ステータスを記録した文字列に置き換わります。<br />
終了ステータスは、コマンドが成功したかどうかを示す値で、<br />
コマンドが終わると変数 <tt class="docutils literal"><span class="pre">$?</span></tt> にセットされる値です。<br />
ただ、 <tt class="docutils literal"><span class="pre">$?</span></tt> には一つの終了ステータスしか記録できないので、<br />
bashではPIPESTATUSという配列に、<br />
パイプでつながったコマンドの終了ステータスを記録できるようになっています。<br />
リスト6に例を示します。trueコマンドとfalseコマンドは、<br />
ただ単に成功（終了ステータス0）、<br />
失敗（終了ステータス1）を返すコマンドです。</p><br />
<p>↓リスト6: PIPESTATUS</p><br />
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#単独動作</span><br />
<span class="c">#終了ステータスは$?で参照できる</span><br />
<span class="nv">$ </span><span class="nb">true</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
<span class="nv">$ </span><span class="nb">false</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
<span class="c">#PIPESTATUSには終了ステータスが順に入る</span><br />
<span class="nv">$ </span><span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">true</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[\@]</span><span class="k">}</span><br />
0 0 0 0<br />
<span class="nv">$ </span><span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">false</span> | <span class="nb">true</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[\@]</span><span class="k">}</span><br />
0 0 1 0<br />
<span class="c">#コマンドが一個だけでもOK</span><br />
<span class="nv">$ </span><span class="nb">true</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[\@]</span><span class="k">}</span><br />
0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　PIPESTATUSが分かったところで再びリスト5の6行目に戻ります。<br />
<tt class="docutils literal"><span class="pre">&quot;$(echo</span> <span class="pre">${PIPESTATUS[&#64;]}</span> <span class="pre">|</span> <span class="pre">tr</span> <span class="pre">-d</span> <span class="pre">'0</span> <span class="pre">')&quot;</span></tt><br />
は、「文字列 <tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt> をtrに送って、0と半角空白を取り除いた文字列」<br />
となります。 <tt class="docutils literal"><span class="pre">$()</span></tt> は、<br />
括弧中のコマンドの標準出力を文字列として置き換えるための表記方法です。<br />
<tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt> から0と空白を除去すれば、<br />
コマンドの終了ステータスがすべて0ならば空文字列になります。<br />
<tt class="docutils literal"><span class="pre">[</span> <span class="pre">-z</span> <span class="pre">&quot;文字列&quot;</span> <span class="pre">]</span> <span class="pre">&amp;&amp;</span> <span class="pre">return</span></tt> で、<br />
「空文字であったら関数を出る」という意味になるので、<br />
コマンドにエラーがなければCHECK関数をすぐに出て処理に戻ります。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">[</span> <span class="pre">]</span></tt> と <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> についても解説が必要でしょう。<br />
<tt class="docutils literal"><span class="pre">[</span></tt> はコマンドです。 <tt class="docutils literal"><span class="pre">man</span> <span class="pre">[</span></tt> と打ってみると、<br />
マニュアルが表示されるはずです。<br />
このコマンドはテストコマンドと呼ばれ、<br />
コマンド本体 <tt class="docutils literal"><span class="pre">[</span></tt> とオプション <tt class="docutils literal"><span class="pre">]</span></tt> で囲まれた部分に<br />
条件式をオプションで書いて、<br />
条件式が満たされれば終了ステータス0を返すコマンドです。<br />
<tt class="docutils literal"><span class="pre">[</span> <span class="pre">-z</span> <span class="pre">&quot;文字列&quot;</span> <span class="pre">]</span></tt> と書くと、<br />
「文字列が空であること」をテストすることになり、<br />
空文字ならば終了ステータス0を返します。<br />
リスト7で動きを示します。</p><br />
<p>↓リスト7: 空文字かどうかの判定</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="o">[</span> -z <span class="s2">&quot;&quot;</span> <span class="o">]</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
<span class="nv">$ </span><span class="o">[</span> -z <span class="s2">&quot;12&quot;</span> <span class="o">]</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
</pre></div><br />
</td></tr></table></div><br />
<p>そして、 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> をコマンドをはさむと、<br />
左側のコマンドの終了ステータスが0の場合に右側のコマンドが実行されます。<br />
リスト5の7行目の場合、PIPESTATUSに0以外のものがなければ <tt class="docutils literal"><span class="pre">[</span></tt> が0を返すので、<br />
returnが実行されて処理が関数から出ます。<br />
もし0でない数字が含まれていたら、処理は8行目以降に進み、<br />
エラー情報が表示され、中間ファイルが消されて、<br />
終了ステータス1でスクリプトが終わります。</p><br />
<p>　ところで、テストコマンドを使うときは、<br />
必ず変数や文字列に置き換わる部分を&#8221;&#8220;で囲んでください。<br />
リスト8のように、違った結果が返ってきます。<br />
&#8220;&#8221;で囲っていない変数が空だと、<br />
<tt class="docutils literal"><span class="pre">[</span></tt> コマンドがオプションとして認識できないので、<br />
このように挙動が変わってしまいます。</p><br />
<p>↓リスト8: 変数を&#8221;&#8220;で囲まないと挙動が変わる</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#空の変数aをセット</span><br />
<span class="nv">$ a</span><span class="o">=</span><br />
<span class="nv">$ </span><span class="o">[</span> -n <span class="s2">&quot;$a&quot;</span> <span class="o">]</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
<span class="nv">$ </span><span class="o">[</span> -n <span class="nv">$a</span> <span class="o">]</span><br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　最後に、書いたスクリプトを実行してみましょう。<br />
これまでのことが理解できていたら、<br />
リスト9のような出力になることも理解できると思います。</p><br />
<p>↓リスト9: 実行結果</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./ADDMEMBER<br />
エラー: <span class="nb">false</span>で失敗<br />
処理できませんでした。<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>7.2.3. チェックを実装する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　では、ADDMEMBERに次のチェック項目を実装してみましょう。</p><br />
<ul class="simple"><br />
<li>入力のデータがちゃんと二列になっているか</li><br />
<li>メールアドレスについて、文字列と文字列の間に&#64;がついているか</li><br />
</ul><br />
<p>ある文字列がメールアドレスかどうかという判断は大変です。<br />
厳密にチェックしたい場合は、コマンドを準備して、<br />
そこに通して判断させるということを考えないといけません。<br />
ここでは簡素に済ますことにします。</p><br />
<p>　リスト10が上記2点を実装したものです。</p><br />
<p>19,20行目でフィールド数を確認します。<br />
gyoとretuはTukubaiコマンド（<a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a>）で、<br />
gyoはレコードの数、retuはフィールド数を出力するものです。<br />
リスト11に使用例を示します。<br />
あるファイルのフィールド数が揃っていると、<br />
<tt class="docutils literal"><span class="pre">retu</span> <span class="pre">file</span> <span class="pre">|</span> <span class="pre">gyo</span></tt> と書くと1が出力されます。<br />
リスト10のチェックでは、<br />
19行目でそれを利用してフィールドが揃っていることを確認して、<br />
20行目でフィールド数が2であることを調べています。<br />
ちなみに、gyoは <tt class="docutils literal"><span class="pre">awk</span> <span class="pre">'END{print</span> <span class="pre">NR}'</span></tt> 、<br />
retuは <tt class="docutils literal"><span class="pre">awk</span> <span class="pre">'{print</span> <span class="pre">NF}'</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> と等価です。</p><br />
<p>　23,24行目では、入力から電子メールのフィールドをself（Tukubaiコマンド）<br />
で切り出して、grepで条件に合うものを抽出しています。<br />
25行目で、もとのレコード数と抽出された電子メールのレコード数を比較しています。</p><br />
<p>↓リスト10: チェックのコード</p><br />
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
29</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<br />
CHECK<span class="o">(){</span><br />
 （略）<br />
<span class="o">}</span><br />
<br />
<span class="c">####################################</span><br />
<span class="c">#標準入力をファイルに書き出す</span><br />
cat &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-file<br />
<span class="c">#1:名前 2:emailアドレス</span><br />
CHECK 読み込めません<br />
<br />
<span class="c">####################################</span><br />
<span class="c">#入力チェック</span><br />
<br />
<span class="c">###入力ファイルが2列か調べる</span><br />
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-file | gyo)&quot;</span> -eq 1 <span class="o">]</span> ; CHECK 列数<br />
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-file)&quot;</span> -eq 2 <span class="o">]</span> ; CHECK 列数<br />
<br />
<span class="c">###\@が文字列と文字列の間に挟まっていること</span><br />
self 2 <span class="nv">$tmp</span>-file |<br />
grep <span class="s1">&#39;^..*\@..*$&#39;</span> &gt; <span class="nv">$tmp</span>-ok-email<br />
<span class="o">[</span> <span class="s2">&quot;$(gyo $tmp-file)&quot;</span> -eq <span class="s2">&quot;$(gyo $tmp-ok-email)&quot;</span> <span class="o">]</span><br />
CHECK email<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>↓リスト11: retuの使用例</p><br />
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat fuge<br />
1 2 3<br />
1 2 3<br />
1 2 3<br />
1 2 3<br />
<span class="nv">$ </span>gyo fuge<br />
4<br />
<span class="nv">$ </span>cat fuge | retu<br />
3<br />
<span class="nv">$ </span>cat hoge<br />
a<br />
a<br />
a<br />
a a a<br />
a a<br />
<span class="nv">$ </span>cat hoge | retu<br />
1<br />
3<br />
2<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id8"><br />
<h3>7.2.4. 動作の確認<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　スクリプトを書いたら、挙動を確認してみましょう。<br />
リスト12のように、エラーメッセージと終了ステータスが<br />
適切に出力されることを確認してみます。</p><br />
<p>↓リスト12: 挙動の確認</p><br />
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#正しい入力</span><br />
<span class="nv">$ </span><span class="nb">echo</span> 山田 email\@email | ./ADDMEMBER<br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
0<br />
<span class="c">#emailがない</span><br />
<span class="nv">$ </span><span class="nb">echo</span> 山田 | ./ADDMEMBER.CHECK<br />
エラー: 列数<br />
処理できませんでした。<br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
<span class="c">#間違えてtwitterアカウントを入力</span><br />
<span class="nv">$ </span><span class="nb">echo</span> 山田 \@usptomo | ./ADDMEMBER.CHECK<br />
エラー: email<br />
処理できませんでした。<br />
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span><br />
1<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id9"><br />
<h3>7.2.5. メンバー追加処理を書く<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　入力のチェック部分は完成したので、<br />
本来やりたいことである新規会員の追加処理を書きましょう。<br />
こちらにもエラーチェックは必要です。<br />
特に、ファイルを更新するときは神経を使わなければなりません。</p><br />
<p>↓リスト13: MEMBERファイル更新スクリプト</p><br />
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
30<br />
31<br />
32<br />
33<br />
34<br />
35<br />
36<br />
37<br />
38<br />
39<br />
40<br />
41<br />
42<br />
43<br />
44<br />
45<br />
46</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span><br />
<br />
<span class="nv">dir</span><span class="o">=</span><span class="s2">&quot;$(dirname $0)/../DATA&quot;</span><br />
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span><br />
<br />
（リスト10の5～26行目。関数と入力チェック）<br />
<br />
<span class="c">####################################</span><br />
<span class="c">#追記処理</span><br />
<span class="nv">DATE</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="c">#1:名前 2:email</span><br />
cat <span class="nv">$tmp</span>-file |<br />
<span class="c">#MEMBERと形式を合わせる</span><br />
awk -v <span class="nv">d</span><span class="o">=</span><span class="s2">&quot;${DATE}&quot;</span> <span class="s1">&#39;{print 0,$0,d,&quot;-&quot;}&#39;</span> |<br />
<span class="c">#1:会員番号（仮） 2:名前 3:email 4:登録日 5:&quot;-&quot;</span><br />
<span class="c">#MEMBERとマージ</span><br />
cat <span class="nv">$dir</span>/MEMBER - |<br />
<span class="c">#1:会員番号 2:名前 3:email 4:登録日 5:退会日</span><br />
awk <span class="s1">&#39;{if($1==0){$1=n};print;n=$1+1}&#39;</span> &gt; <span class="nv">$tmp</span>-new<br />
CHECK 追加処理失敗<br />
<br />
<span class="c">#新しいリストをチェック</span><br />
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-new | gyo)&quot;</span> -eq 1 <span class="o">]</span><br />
CHECK フィールド数が不正<br />
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-new)&quot;</span> -eq 5 <span class="o">]</span><br />
CHECK フィールド数が不正<br />
<span class="c">#emailの重複チェック</span><br />
<span class="nv">DUP</span><span class="o">=</span><span class="k">$(</span>self 3 <span class="nv">$tmp</span>-new | sort | uniq -d | gyo<span class="k">)</span><br />
<span class="o">[</span> <span class="s2">&quot;${DUP}&quot;</span> -eq 0 <span class="o">]</span><br />
CHECK email重複<br />
<br />
<span class="c">######################################</span><br />
<span class="c">#更新</span><br />
cat <span class="nv">$dir</span>/MEMBER &gt; <span class="nv">$dir</span>/MEMBER.<span class="k">${</span><span class="nv">DATE</span><span class="k">}</span>.<span class="nv">$$</span><br />
CHECK 旧リストのバックアップ<br />
cat <span class="nv">$tmp</span>-new &gt; <span class="nv">$dir</span>/MEMBER<br />
CHECK 新リストの書き出し<br />
<br />
<span class="c">######################################</span><br />
<span class="c">#diffで確認</span><br />
<span class="nb">echo</span> 変更しました &gt;&amp;2<br />
diff <span class="nv">$dir</span>/MEMBER.<span class="k">${</span><span class="nv">DATE</span><span class="k">}</span>.<span class="nv">$$</span> <span class="nv">$dir</span>/MEMBER &gt;&amp;2<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　リスト9にスクリプト全体を示します。<br />
13行目から20行目で、新たなメンバーをMEMBERファイルに追加して、<br />
<tt class="docutils literal"><span class="pre">$tmp-new</span></tt> に新しいリストを作成しています。</p><br />
<p>　目新しいところとしては、3行目のdirnameコマンドの使い方と、<br />
15行目のawkの使い方でしょう。<br />
dirnameコマンドは、このスクリプトのあるディレクトリを出力します。<br />
このスクリプトでは、MEMBERファイルの場所を特定するために使っています。<br />
15行目では、bashの変数をawkに渡すために、<br />
-vというオプションを使用しています<br />
（脚注: <a class="reference external" href="http://d.hatena.ne.jp/Rocco/20071031/p2">http://d.hatena.ne.jp/Rocco/20071031/p2</a>）。</p><br />
<p>　23行目から31行目までで、しつこくチェックをします。<br />
29行目の <tt class="docutils literal"><span class="pre">uniq</span> <span class="pre">-d</span></tt><br />
は第一回でも使いましたが重複するレコードを抽出するために使っています。</p><br />
<p>　35～38行目での更新では、<br />
更新前のファイルのバックアップをとっています。<br />
こうしておけば、何かあっても安心です。<br />
本連載で扱っているシェルスクリプトはファイル操作のためのものが中心なので、<br />
もとのファイルさえ残しておけば多少ルーズに書いても、<br />
致命的なことになりにくいという性質があります。<br />
また、パイプを使うとファイルを直接上書きすることはないので、<br />
スクリプトが途中で止まれば重要なファイルは守られるという性質があります。</p><br />
<p>　一方で <tt class="docutils literal"><span class="pre">rm</span> <span class="pre">-Rf</span> <span class="pre">~/</span></tt> などと書いてしまうとなにもかも消えてしまうので、<br />
ホームのバックアップは必須ですが・・・。</p><br />
<p>　最後に、スクリプトを動作させて、今回は終わりにします。</p><br />
<p>↓リスト14: 会員の追加の実行</p><br />
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###更新前</span><br />
<span class="nv">$ </span>tail -n 2 ./DATA/MEMBER<br />
10000009 山本 yamamoto\@bash.co.jp 20101010 -<br />
10000010 山口 yamaguchi\@daioujyou.com 20120401 -<br />
<span class="c">###更新実行</span><br />
<span class="nv">$ </span>cat newmember | ./SCR/ADDMEMBER<br />
変更しました<br />
10a11,12<br />
&gt; 10000011 門田 kadota\@paa-league.net 20120429 -<br />
&gt; 10000012 香川 kagawa\@dokaben.com 20120429 -<br />
<span class="c">###不正な値を入力してみる</span><br />
<span class="nv">$ </span><span class="nb">echo</span> 上田 ueda\@hogehoge.com | ./SCR/ADDMEMBER<br />
エラー: email重複<br />
処理できませんでした。<br />
<span class="c">###更新後</span><br />
<span class="nv">$ </span>tail -n 4 ./DATA/MEMBER<br />
10000009 山本 yamamoto\@bash.co.jp 20101010 -<br />
10000010 山口 yamaguchi\@daioujyou.com 20120401 -<br />
10000011 門田 kadota\@paa-league.net 20120429 -<br />
10000012 香川 kagawa\@dokaben.com 20120429 -<br />
<span class="c">###バックアップが作成されている</span><br />
<span class="nv">$ </span>ls ./DATA/MEMBER*<br />
./DATA/MEMBER ./DATA/MEMBER.20120429.8648<br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id10"><br />
<h3>7.2.6. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回は、ファイルの追記を自動化するためのスクリプトを書きました。<br />
関数、テストコマンド、 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> 記号など、ややこしいものが出てきました。<br />
これらの記号は一般的なプログラミング言語に比べると洗練されたものとは言えません。<br />
しかしシェルスクリプトの場合、ほとんどファイルと標準出力を相手にプログラムするので、<br />
配列やメモリなど可視化しにくいものを相手するよりは、<br />
かなり楽に処理を書くことができると考えています。</p><br />
</div><br />
</div><br />
</div><br />

