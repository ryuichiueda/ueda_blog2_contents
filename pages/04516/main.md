---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年7月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>7. 開眼シェルスクリプト 第7回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>7.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回の開眼シェルスクリプトは、なにかしらの重要なファイルを上書き更新するシェルスクリプトを扱います。
ファイルを更新するということは「覆水盆に返らず」ですので、それなりに気を使うべきです。
今回はシェルスクリプトを使って安全に更新する方法を扱います。</p>
<div class="section" id="id3">
<h3>7.1.1. コマンドはファイルを上書きしない<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　たまにtwitterなどで「ファイルを直接更新するコマンドはないのか？」
という発言を捕捉することがあります。
つまり、下のような例で、ファイル <tt class="docutils literal"><span class="pre">file</span></tt> が変更できないのかということでしょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">command </span>file
</pre></div>
</div>
<p>　UNIX系OSにおいては、このようなコマンドは少数派です。
sedやnkfコマンドは上書きができますが、オプションを指定しないと上書きモードになりません。</p>
<p>　ファイル上書きをむやみに許してしまうと、次のようになにかと不都合です。</p>
<ul class="simple">
<li>パイプ接続できるコマンドとできないコマンドの識別する労力が増大</li>
<li>なにか失敗すると後戻り不可能。あるいは面倒</li>
</ul>
<p>　ファイルを上書きしたいときは、面倒でも次のような手続きを踏みます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span><span class="nb">command </span>file &gt; file.new
<span class="nv">$ </span>mv file.new file
</pre></div>
</div>
<p>もし必要なら、mvの前にdiffをとって確認したり、
もとのファイルのバックアップをとったりします。
逆に言えば、そのような機会が必ず用意されるという点で、
一度別のファイルに結果を出力してからmvする方法は合理的と言えます。
シェルスクリプトでも、同様の手続きを踏みます。</p>
<p>　もういい加減ネタ切れですが、今回も格言（？）を。</p>
<ul class="simple">
<li>覆水盆に返らず &#8212;呂尚</li>
<li>いきなり盆をひっくり返すから盆に返らないだけ &#8212;筆者</li>
</ul>
</div>
</div>
<div class="section" id="id4">
<h2>7.2. お題：会員管理を自動化する<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　前回に引き続き、架空の団体「UPS友の会」の会員管理を扱います。
前回は手動で会員リストを操作しましたが、
今回は会員リストへの新会員の追加処理をシェルスクリプト化します。
シェルスクリプトでは、会員リストを上書きするときに会員リストを壊さないように、
様々な仕掛けをします。これまでの連載では、
ほとんど一直線のパイプライン処理ばかり扱っていましたが、
今回は細かい文法をいくつか知っておく必要があります。
細かくなると、文法がシェルごとに違うことがありますが、
今回はbashの文法を使います。</p>
<div class="section" id="id5">
<h3>7.2.1. 準備<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は、リスト1の環境でプログラムを組んで動作させます。</p>
<p>↓リスト1: 環境</p>
<div class="highlight-bash"><div class="highlight"><pre>ueda@uedaubuntu:~<span class="nv">$ </span>bash --version | head -n 1
GNU bash, バージョン 4.2.10<span class="o">(</span>1<span class="o">)</span>-release <span class="o">(</span>i686-pc-linux-gnu<span class="o">)</span>
ueda@uedaubuntu:~<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span>
ja_JP.UTF-8
ueda@uedaubuntu:~<span class="nv">$ </span>lsb_release -a | grep Description
Description: Ubuntu 11.10
</pre></div>
</div>
<p>　まず、ディレクトリを準備をします。
適当な場所に、リスト2のようにディレクトリを掘ります。</p>
<ul class="simple">
<li>SCR: シェルスクリプト（ADDMEMBERファイル）置き場</li>
<li>DATA：会員リスト（MEMBERファイル）の置き場所</li>
</ul>
<p>↓リスト2: ディレクトリ</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre>UPSTOMO/
├── DATA
│ └── MEMBER
├── SCR
│ └── ADDMEMBER
└── newmember
</pre></div>
</td></tr></table></div>
<p>newmemberは、新しく追加する会員のリストで、一時的なのものです（リスト3）。</p>
<p>↓リスト3: 新規会員を書いたファイル</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat newmember
門田 kadota@paa-league.net
香川 kagawa@dokaben.com
</pre></div>
</td></tr></table></div>
<p>MEMBERファイルには、次のような既存会員データが記録されています（リスト4）。
このファイルが原本です。</p>
<p>↓リスト4: 会員リスト</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#1:会員番号 2:氏名（簡略化のため姓のみ） 3:e-mailアドレス</span>
<span class="c">#4:入会処理日 5:退会処理日</span>
<span class="nv">$ </span>head -n 5 ./DATA/MEMBER
10000001 上田 ueda@hogehoge.com 19720103 -
10000002 濱田 hamada@nullnull.com 19831102 -
10000003 武田 takeda@takenaka.com 19930815 20120104
10000004 竹中 takenaka@takeda.com 19980423 -
10000005 田中 tanaka@kakuei.jp 20000111 -
</pre></div>
</td></tr></table></div>
<p>newmemberファイルのデータに会員番号と入会処理日をつけて、
MEMBERファイルに追記するのが、ADDMEMBER の役目です。
MEMBERファイルを壊してはいけませんので、
入力をチェックしてから追記処理をしなくてはなりません。</p>
</div>
<div class="section" id="id6">
<h3>7.2.2. 準備<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まず、シェルスクリプトADDMEMBERに、
リスト5のようにエラーを検知する仕組みを書きます。</p>
<p>↓リスト5: エラー検知処理を書く</p>
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
22</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>

CHECK<span class="o">(){</span>
 <span class="o">[</span> -z <span class="s2">&quot;$(echo ${PIPESTATUS[@]} | tr -d &#39;0 &#39;)&quot;</span> <span class="o">]</span> <span class="o">&amp;&amp;</span> <span class="k">return</span>

<span class="k"> </span><span class="nb">echo</span> <span class="s2">&quot;エラー: $1&quot;</span> &gt;&amp;2
 <span class="nb">echo</span> 処理できませんでした。&gt;&amp;2
 rm -f <span class="nv">$tmp</span>-*
 <span class="nb">exit </span>1
<span class="o">}</span>

<span class="c">#テスト</span>
<span class="nb">true</span> | <span class="nb">true</span>
CHECK これは成功する。

<span class="nb">true</span> | <span class="nb">false</span>
CHECK <span class="nb">false</span>で失敗

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　5～12行目はbashの関数です。
書き方はリスト1のように、 <tt class="docutils literal"><span class="pre">名前(){処理}</span></tt> となります。
呼び出し方はコマンドと一緒で、名前を行頭に書きます。
引数は <tt class="docutils literal"><span class="pre">()</span></tt> 内で定義せず、関数内で <tt class="docutils literal"><span class="pre">$1,</span> <span class="pre">$2,</span> <span class="pre">...</span></tt> と呼び出します。
例えば、19行目で <tt class="docutils literal"><span class="pre">CHECK</span> <span class="pre">falseで失敗</span></tt> と記述されていますが、
「falseで失敗」は、CHECK関数の第一引数で、関数内で$1として呼び出せます。
リスト5では、8行目で$1を使っています。</p>
<p>　エラーメッセージは、標準エラー出力に出すのが行儀良いでしょう。
8,9行目のように、 <tt class="docutils literal"><span class="pre">&gt;&amp;2</span></tt> と書くことで、
echoの出力先を標準エラー出力にリダイレクトできます。
基本的に、標準出力はコマンド（コンピュータ）のため、
標準エラー出力は人間が読むために使います。</p>
<p>　6行目の呪文を一つずつ紐解いていきましょう。
まず <tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt>
は、パイプでつながったコマンドの終了ステータスを記録した文字列に置き換わります。
終了ステータスは、コマンドが成功したかどうかを示す値で、
コマンドが終わると変数 <tt class="docutils literal"><span class="pre">$?</span></tt> にセットされる値です。
ただ、 <tt class="docutils literal"><span class="pre">$?</span></tt> には一つの終了ステータスしか記録できないので、
bashではPIPESTATUSという配列に、
パイプでつながったコマンドの終了ステータスを記録できるようになっています。
リスト6に例を示します。trueコマンドとfalseコマンドは、
ただ単に成功（終了ステータス0）、
失敗（終了ステータス1）を返すコマンドです。</p>
<p>↓リスト6: PIPESTATUS</p>
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#単独動作</span>
<span class="c">#終了ステータスは$?で参照できる</span>
<span class="nv">$ </span><span class="nb">true</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
<span class="nv">$ </span><span class="nb">false</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
<span class="c">#PIPESTATUSには終了ステータスが順に入る</span>
<span class="nv">$ </span><span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">true</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[@]</span><span class="k">}</span>
0 0 0 0
<span class="nv">$ </span><span class="nb">true</span> | <span class="nb">true</span> | <span class="nb">false</span> | <span class="nb">true</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[@]</span><span class="k">}</span>
0 0 1 0
<span class="c">#コマンドが一個だけでもOK</span>
<span class="nv">$ </span><span class="nb">true</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="k">${</span><span class="nv">PIPESTATUS</span><span class="p">[@]</span><span class="k">}</span>
0
</pre></div>
</td></tr></table></div>
<p>　PIPESTATUSが分かったところで再びリスト5の6行目に戻ります。
<tt class="docutils literal"><span class="pre">&quot;$(echo</span> <span class="pre">${PIPESTATUS[&#64;]}</span> <span class="pre">|</span> <span class="pre">tr</span> <span class="pre">-d</span> <span class="pre">'0</span> <span class="pre">')&quot;</span></tt>
は、「文字列 <tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt> をtrに送って、0と半角空白を取り除いた文字列」
となります。 <tt class="docutils literal"><span class="pre">$()</span></tt> は、
括弧中のコマンドの標準出力を文字列として置き換えるための表記方法です。
<tt class="docutils literal"><span class="pre">${PIPESTATUS[&#64;]}</span></tt> から0と空白を除去すれば、
コマンドの終了ステータスがすべて0ならば空文字列になります。
<tt class="docutils literal"><span class="pre">[</span> <span class="pre">-z</span> <span class="pre">&quot;文字列&quot;</span> <span class="pre">]</span> <span class="pre">&amp;&amp;</span> <span class="pre">return</span></tt> で、
「空文字であったら関数を出る」という意味になるので、
コマンドにエラーがなければCHECK関数をすぐに出て処理に戻ります。</p>
<p>　 <tt class="docutils literal"><span class="pre">[</span> <span class="pre">]</span></tt> と <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> についても解説が必要でしょう。
<tt class="docutils literal"><span class="pre">[</span></tt> はコマンドです。 <tt class="docutils literal"><span class="pre">man</span> <span class="pre">[</span></tt> と打ってみると、
マニュアルが表示されるはずです。
このコマンドはテストコマンドと呼ばれ、
コマンド本体 <tt class="docutils literal"><span class="pre">[</span></tt> とオプション <tt class="docutils literal"><span class="pre">]</span></tt> で囲まれた部分に
条件式をオプションで書いて、
条件式が満たされれば終了ステータス0を返すコマンドです。
<tt class="docutils literal"><span class="pre">[</span> <span class="pre">-z</span> <span class="pre">&quot;文字列&quot;</span> <span class="pre">]</span></tt> と書くと、
「文字列が空であること」をテストすることになり、
空文字ならば終了ステータス0を返します。
リスト7で動きを示します。</p>
<p>↓リスト7: 空文字かどうかの判定</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span><span class="o">[</span> -z <span class="s2">&quot;&quot;</span> <span class="o">]</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
<span class="nv">$ </span><span class="o">[</span> -z <span class="s2">&quot;12&quot;</span> <span class="o">]</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
</pre></div>
</td></tr></table></div>
<p>そして、 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> をコマンドをはさむと、
左側のコマンドの終了ステータスが0の場合に右側のコマンドが実行されます。
リスト5の7行目の場合、PIPESTATUSに0以外のものがなければ <tt class="docutils literal"><span class="pre">[</span></tt> が0を返すので、
returnが実行されて処理が関数から出ます。
もし0でない数字が含まれていたら、処理は8行目以降に進み、
エラー情報が表示され、中間ファイルが消されて、
終了ステータス1でスクリプトが終わります。</p>
<p>　ところで、テストコマンドを使うときは、
必ず変数や文字列に置き換わる部分を&#8221;&#8220;で囲んでください。
リスト8のように、違った結果が返ってきます。
&#8220;&#8221;で囲っていない変数が空だと、
<tt class="docutils literal"><span class="pre">[</span></tt> コマンドがオプションとして認識できないので、
このように挙動が変わってしまいます。</p>
<p>↓リスト8: 変数を&#8221;&#8220;で囲まないと挙動が変わる</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7
8</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#空の変数aをセット</span>
<span class="nv">$ a</span><span class="o">=</span>
<span class="nv">$ </span><span class="o">[</span> -n <span class="s2">&quot;$a&quot;</span> <span class="o">]</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
<span class="nv">$ </span><span class="o">[</span> -n <span class="nv">$a</span> <span class="o">]</span>
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
</pre></div>
</td></tr></table></div>
<p>　最後に、書いたスクリプトを実行してみましょう。
これまでのことが理解できていたら、
リスト9のような出力になることも理解できると思います。</p>
<p>↓リスト9: 実行結果</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>./ADDMEMBER
エラー: <span class="nb">false</span>で失敗
処理できませんでした。
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id7">
<h3>7.2.3. チェックを実装する<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　では、ADDMEMBERに次のチェック項目を実装してみましょう。</p>
<ul class="simple">
<li>入力のデータがちゃんと二列になっているか</li>
<li>メールアドレスについて、文字列と文字列の間に&#64;がついているか</li>
</ul>
<p>ある文字列がメールアドレスかどうかという判断は大変です。
厳密にチェックしたい場合は、コマンドを準備して、
そこに通して判断させるということを考えないといけません。
ここでは簡素に済ますことにします。</p>
<p>　リスト10が上記2点を実装したものです。</p>
<p>19,20行目でフィールド数を確認します。
gyoとretuはTukubaiコマンド（<a class="reference external" href="https://uec.usp-lab.com">https://uec.usp-lab.com</a>）で、
gyoはレコードの数、retuはフィールド数を出力するものです。
リスト11に使用例を示します。
あるファイルのフィールド数が揃っていると、
<tt class="docutils literal"><span class="pre">retu</span> <span class="pre">file</span> <span class="pre">|</span> <span class="pre">gyo</span></tt> と書くと1が出力されます。
リスト10のチェックでは、
19行目でそれを利用してフィールドが揃っていることを確認して、
20行目でフィールド数が2であることを調べています。
ちなみに、gyoは <tt class="docutils literal"><span class="pre">awk</span> <span class="pre">'END{print</span> <span class="pre">NR}'</span></tt> 、
retuは <tt class="docutils literal"><span class="pre">awk</span> <span class="pre">'{print</span> <span class="pre">NF}'</span> <span class="pre">|</span> <span class="pre">uniq</span></tt> と等価です。</p>
<p>　23,24行目では、入力から電子メールのフィールドをself（Tukubaiコマンド）
で切り出して、grepで条件に合うものを抽出しています。
25行目で、もとのレコード数と抽出された電子メールのレコード数を比較しています。</p>
<p>↓リスト10: チェックのコード</p>
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
29</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>

CHECK<span class="o">(){</span>
 （略）
<span class="o">}</span>

<span class="c">####################################</span>
<span class="c">#標準入力をファイルに書き出す</span>
cat &lt; /dev/stdin &gt; <span class="nv">$tmp</span>-file
<span class="c">#1:名前 2:emailアドレス</span>
CHECK 読み込めません

<span class="c">####################################</span>
<span class="c">#入力チェック</span>

<span class="c">###入力ファイルが2列か調べる</span>
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-file | gyo)&quot;</span> -eq 1 <span class="o">]</span> ; CHECK 列数
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-file)&quot;</span> -eq 2 <span class="o">]</span> ; CHECK 列数

<span class="c">###@が文字列と文字列の間に挟まっていること</span>
self 2 <span class="nv">$tmp</span>-file |
grep <span class="s1">&#39;^..*@..*$&#39;</span> &gt; <span class="nv">$tmp</span>-ok-email
<span class="o">[</span> <span class="s2">&quot;$(gyo $tmp-file)&quot;</span> -eq <span class="s2">&quot;$(gyo $tmp-ok-email)&quot;</span> <span class="o">]</span>
CHECK email

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>↓リスト11: retuの使用例</p>
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
19</pre></div></td><td class="code"><div class="highlight"><pre><span class="nv">$ </span>cat fuge
1 2 3
1 2 3
1 2 3
1 2 3
<span class="nv">$ </span>gyo fuge
4
<span class="nv">$ </span>cat fuge | retu
3
<span class="nv">$ </span>cat hoge
a
a
a
a a a
a a
<span class="nv">$ </span>cat hoge | retu
1
3
2
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id8">
<h3>7.2.4. 動作の確認<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　スクリプトを書いたら、挙動を確認してみましょう。
リスト12のように、エラーメッセージと終了ステータスが
適切に出力されることを確認してみます。</p>
<p>↓リスト12: 挙動の確認</p>
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
16</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#正しい入力</span>
<span class="nv">$ </span><span class="nb">echo</span> 山田 email@email | ./ADDMEMBER
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
0
<span class="c">#emailがない</span>
<span class="nv">$ </span><span class="nb">echo</span> 山田 | ./ADDMEMBER.CHECK
エラー: 列数
処理できませんでした。
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
<span class="c">#間違えてtwitterアカウントを入力</span>
<span class="nv">$ </span><span class="nb">echo</span> 山田 @usptomo | ./ADDMEMBER.CHECK
エラー: email
処理できませんでした。
<span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$?</span>
1
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id9">
<h3>7.2.5. メンバー追加処理を書く<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　入力のチェック部分は完成したので、
本来やりたいことである新規会員の追加処理を書きましょう。
こちらにもエラーチェックは必要です。
特に、ファイルを更新するときは神経を使わなければなりません。</p>
<p>↓リスト13: MEMBERファイル更新スクリプト</p>
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
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash</span>

<span class="nv">dir</span><span class="o">=</span><span class="s2">&quot;$(dirname $0)/../DATA&quot;</span>
<span class="nv">tmp</span><span class="o">=</span>/home/ueda/tmp/<span class="nv">$$</span>

（リスト10の5～26行目。関数と入力チェック）

<span class="c">####################################</span>
<span class="c">#追記処理</span>
<span class="nv">DATE</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="c">#1:名前 2:email</span>
cat <span class="nv">$tmp</span>-file |
<span class="c">#MEMBERと形式を合わせる</span>
awk -v <span class="nv">d</span><span class="o">=</span><span class="s2">&quot;${DATE}&quot;</span> <span class="s1">&#39;{print 0,$0,d,&quot;-&quot;}&#39;</span> |
<span class="c">#1:会員番号（仮） 2:名前 3:email 4:登録日 5:&quot;-&quot;</span>
<span class="c">#MEMBERとマージ</span>
cat <span class="nv">$dir</span>/MEMBER - |
<span class="c">#1:会員番号 2:名前 3:email 4:登録日 5:退会日</span>
awk <span class="s1">&#39;{if($1==0){$1=n};print;n=$1+1}&#39;</span> &gt; <span class="nv">$tmp</span>-new
CHECK 追加処理失敗

<span class="c">#新しいリストをチェック</span>
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-new | gyo)&quot;</span> -eq 1 <span class="o">]</span>
CHECK フィールド数が不正
<span class="o">[</span> <span class="s2">&quot;$(retu $tmp-new)&quot;</span> -eq 5 <span class="o">]</span>
CHECK フィールド数が不正
<span class="c">#emailの重複チェック</span>
<span class="nv">DUP</span><span class="o">=</span><span class="k">$(</span>self 3 <span class="nv">$tmp</span>-new | sort | uniq -d | gyo<span class="k">)</span>
<span class="o">[</span> <span class="s2">&quot;${DUP}&quot;</span> -eq 0 <span class="o">]</span>
CHECK email重複

<span class="c">######################################</span>
<span class="c">#更新</span>
cat <span class="nv">$dir</span>/MEMBER &gt; <span class="nv">$dir</span>/MEMBER.<span class="k">${</span><span class="nv">DATE</span><span class="k">}</span>.<span class="nv">$$</span>
CHECK 旧リストのバックアップ
cat <span class="nv">$tmp</span>-new &gt; <span class="nv">$dir</span>/MEMBER
CHECK 新リストの書き出し

<span class="c">######################################</span>
<span class="c">#diffで確認</span>
<span class="nb">echo</span> 変更しました &gt;&amp;2
diff <span class="nv">$dir</span>/MEMBER.<span class="k">${</span><span class="nv">DATE</span><span class="k">}</span>.<span class="nv">$$</span> <span class="nv">$dir</span>/MEMBER &gt;&amp;2

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>　リスト9にスクリプト全体を示します。
13行目から20行目で、新たなメンバーをMEMBERファイルに追加して、
<tt class="docutils literal"><span class="pre">$tmp-new</span></tt> に新しいリストを作成しています。</p>
<p>　目新しいところとしては、3行目のdirnameコマンドの使い方と、
15行目のawkの使い方でしょう。
dirnameコマンドは、このスクリプトのあるディレクトリを出力します。
このスクリプトでは、MEMBERファイルの場所を特定するために使っています。
15行目では、bashの変数をawkに渡すために、
-vというオプションを使用しています
（脚注: <a class="reference external" href="http://d.hatena.ne.jp/Rocco/20071031/p2">http://d.hatena.ne.jp/Rocco/20071031/p2</a>）。</p>
<p>　23行目から31行目までで、しつこくチェックをします。
29行目の <tt class="docutils literal"><span class="pre">uniq</span> <span class="pre">-d</span></tt>
は第一回でも使いましたが重複するレコードを抽出するために使っています。</p>
<p>　35～38行目での更新では、
更新前のファイルのバックアップをとっています。
こうしておけば、何かあっても安心です。
本連載で扱っているシェルスクリプトはファイル操作のためのものが中心なので、
もとのファイルさえ残しておけば多少ルーズに書いても、
致命的なことになりにくいという性質があります。
また、パイプを使うとファイルを直接上書きすることはないので、
スクリプトが途中で止まれば重要なファイルは守られるという性質があります。</p>
<p>　一方で <tt class="docutils literal"><span class="pre">rm</span> <span class="pre">-Rf</span> <span class="pre">~/</span></tt> などと書いてしまうとなにもかも消えてしまうので、
ホームのバックアップは必須ですが・・・。</p>
<p>　最後に、スクリプトを動作させて、今回は終わりにします。</p>
<p>↓リスト14: 会員の追加の実行</p>
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
23</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">###更新前</span>
<span class="nv">$ </span>tail -n 2 ./DATA/MEMBER
10000009 山本 yamamoto@bash.co.jp 20101010 -
10000010 山口 yamaguchi@daioujyou.com 20120401 -
<span class="c">###更新実行</span>
<span class="nv">$ </span>cat newmember | ./SCR/ADDMEMBER
変更しました
10a11,12
&gt; 10000011 門田 kadota@paa-league.net 20120429 -
&gt; 10000012 香川 kagawa@dokaben.com 20120429 -
<span class="c">###不正な値を入力してみる</span>
<span class="nv">$ </span><span class="nb">echo</span> 上田 ueda@hogehoge.com | ./SCR/ADDMEMBER
エラー: email重複
処理できませんでした。
<span class="c">###更新後</span>
<span class="nv">$ </span>tail -n 4 ./DATA/MEMBER
10000009 山本 yamamoto@bash.co.jp 20101010 -
10000010 山口 yamaguchi@daioujyou.com 20120401 -
10000011 門田 kadota@paa-league.net 20120429 -
10000012 香川 kagawa@dokaben.com 20120429 -
<span class="c">###バックアップが作成されている</span>
<span class="nv">$ </span>ls ./DATA/MEMBER*
./DATA/MEMBER ./DATA/MEMBER.20120429.8648
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id10">
<h3>7.2.6. おわりに<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回は、ファイルの追記を自動化するためのスクリプトを書きました。
関数、テストコマンド、 <tt class="docutils literal"><span class="pre">&amp;&amp;</span></tt> 記号など、ややこしいものが出てきました。
これらの記号は一般的なプログラミング言語に比べると洗練されたものとは言えません。
しかしシェルスクリプトの場合、ほとんどファイルと標準出力を相手にプログラムするので、
配列やメモリなど可視化しにくいものを相手するよりは、
かなり楽に処理を書くことができると考えています。</p>
</div>
</div>
</div>

