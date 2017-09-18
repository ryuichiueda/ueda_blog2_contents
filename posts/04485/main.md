---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年1月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>1. 開眼　シェルスクリプト　第1回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>1.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="gancarzunix"><br />
<h3>1.1.1. GancarzのUNIX哲学<a class="headerlink" href="#gancarzunix" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>突然ですが、これがなんだかご存知でしょうか？</p><br />
<ul class="simple"><br />
<li>小さいものは美しい。</li><br />
<li>各プログラムが一つのことをうまくやるようにせよ。</li><br />
<li>できる限り原型（プロトタイプ）を作れ。</li><br />
<li>効率よりも移植しやすさを選べ。</li><br />
<li>単純なテキストファイルにデータを格納せよ。</li><br />
<li>ソフトウェアの効率をきみの優位さとして利用せよ。</li><br />
<li>効率と移植性を高めるためにシェルスクリプトを利用せよ。</li><br />
<li>束縛するインターフェースは作るな。</li><br />
<li>全てのプログラムはフィルタとして振る舞うようにせよ。</li><br />
</ul><br />
<p>これはGancarzのUNIX哲学 [Gancarz2001]というものです。<br />
UNIX（系OS）の使い方、さらには世界観をまとめたもので、<br />
極めて乱暴にまとめると、</p><br />
<p>「端末やシェルスクリプトでコマンドを使い倒して早く仕事しようぜ」</p><br />
<p>ということを言っています。（繰り返しますが乱暴です。）</p><br />
<p>ここで言っている仕事というのは、<br />
エンジニアがコンピュータのために仕事をすることよりも、<br />
顧客データ管理、表計算、原稿書きなど利用することだと考えてください。<br />
UNIXの使い方がCLI（コマンドラインユーザインタフェース）中心だった時代は、<br />
テキストファイルに字を書いて保存したり、検索したり、<br />
表計算したりすることが普通のことだったのです。<br />
（私自身はそんな時代を知らない一人ですが。）</p><br />
</div><br />
<div class="section" id="id3"><br />
<h3>1.1.2. テキストファイルは自由だ<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>現在は、便利なGUIソフトがいろいろできたおかげで、<br />
何でもCLIという窮屈なことは無くなりましたが、<br />
テキストファイルが必要なくなることはありません。<br />
どんなワープロソフトでもテキストのペーストは受け付けますし、<br />
インターネットのプロトコルの多くはテキストベースです。<br />
文字しかないということは、ソフトウェア同士、<br />
あるいはコンピュータと人間の間で余計な決めごとが無いという利点があるのです。</p><br />
<p>また、テキストでデータを持っておくと、何にでも化けるという利点があります。<br />
上記のUNIX哲学で「単純なテキストファイルにデータを格納せよ」<br />
と言っているのはまさにこのことです。<br />
筆者の例で恐縮ですが、今、<br />
この原稿をreST（restructuredText）という形式のテキストで書いています。<br />
reSTはそのまま編集の方に渡しても読んでもらえるほど分かりやすい形式です。<br />
そして、Sphinxというツールに通すとhtmlに変換できるので、<br />
体裁をブラウザで確認しながら書いています。<br />
次回の執筆はもっと便利なように、</p><br />
<ul class="simple"><br />
<li>さらに編集者フレンドリーなテキストに変換するスクリプト</li><br />
<li>掲載時とそっくりな体裁になるLaTeX形式への変換スクリプト</li><br />
</ul><br />
<p>を書いてから開始しようと考えています。<br />
自分の書くreSTだけ相手にすればよいので、そんなに難しくはないでしょう。</p><br />
<p>このようにテキストで済ませていると、特定のソフトの仕様に束縛されることがありません。<br />
我々の場合なら、ちょっとプログラムでも書いてみようかという気持ちになるでしょう。<br />
[Raymond2007]にも、UNIXはテキスト文化なので、<br />
気軽にプログラムに入門できる効用があると述べられています。</p><br />
</div><br />
<div class="section" id="id4"><br />
<h3>1.1.3. 短いシェルスクリプトで様々な処理を<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>UNIX系OSのコマンドの多くは、テキスト処理のためにあります。<br />
ただ、一つ一つのコマンドを端末で使う機会は多くの人にあるようですが、<br />
組み合わせてシェルスクリプトにすると複雑な処理ができることは、<br />
あまり知られていません。知られていないと言うより、<br />
忘れ去られていると言った方が適切かもしれません。</p><br />
<p>この連載の目的は、UNIX系OSでコマンドを触ったことのある人に、<br />
シェルスクリプトの便利な利用例を紹介し、<br />
もっとコマンドの用途を広げてもらうことにあります。<br />
コマンドをシェルスクリプトで組み合わせると、<br />
役に立つプログラムが短く書けてしまう例を紹介していきます。<br />
コマンドが多くの仕事をするので、シェルスクリプトを上手く書けば、<br />
とてもあっさりとしたものが出来上がります。</p><br />
<p>ただし、「短いシェルスクリプト」に開眼するには、<br />
ほとんどの人の場合、ある一定の時間がかかります。<br />
特になにかしらの言語を知っている人が書くと、インデントとfor文だらけになりがちです。<br />
そのようなシェルスクリプトはもっと短くできるのですが、<br />
重要な割にニッチすぎて話題になりません・・・。</p><br />
<p>そこで本連載では、「シェルスクリプトの便利な利用例」と同じくらいの重要度で、<br />
「短いシェルスクリプトを書く手練手管」も紹介していきます。<br />
シェルスクリプトを使うことにピンと来ない人でも、<br />
「深いインデント回避のためのロジック」を楽しんでいただけたらと考えています。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h3>1.1.4. 筆者について<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>これを書いているのは、USP研究所という、<br />
シェルスクリプトで業務システムを構築する会社に勤務し、<br />
毎日シェルスクリプトばかり書いている男です。<br />
短く書いて早く仕事を終わらせることにのみ、心血を注いでいます。</p><br />
<ul><br />
<li><dl class="first docutils"><br />
<dt>USP研究所</dt><br />
<dd><ul class="first last simple"><br />
<li><a class="reference external" href="http://www.usp-lab.com/">http://www.usp-lab.com/</a></li><br />
</ul><br />
</dd><br />
</dl><br />
</li><br />
</ul><br />
<p>夜は（？）USP友の会というシェルスクリプトの会の会長として、<br />
主に技術以外のところで微妙な働きをしています。</p><br />
<ul><br />
<li><dl class="first docutils"><br />
<dt>USP友の会</dt><br />
<dd><ul class="first last simple"><br />
<li>web: <a class="reference external" href="http://www.usptomonokai.jp/">http://www.usptomonokai.jp/</a></li><br />
<li>twitter: &#64;usptomo</li><br />
<li>facebook: <a class="reference external" href="http://www.facebook.com/usptomo">http://www.facebook.com/usptomo</a></li><br />
</ul><br />
</dd><br />
</dl><br />
</li><br />
</ul><br />
<p>前職では某大学でロボットのプログラムばかり書き、<br />
学生にもそれを強要していました。この時代は映像処理、カメラの制御、<br />
その他人工知能的なものをひたすらプログラムしており、主にC++を使っていました。<br />
現在もロボカップ（ロボットサッカーの大会）の日本大会で手伝いをしています。</p><br />
<ul><br />
<li><dl class="first docutils"><br />
<dt>RoboCup Japan Open</dt><br />
<dd><ul class="first last simple"><br />
<li><a class="reference external" href="http://www.robocup-japanopen.org/">http://www.robocup-japanopen.org/</a></li><br />
</ul><br />
</dd><br />
</dl><br />
</li><br />
</ul><br />
<p>もしシェルスクリプトに興味をそそられるようでしたら、<br />
USP友の会が出没するイベントを訪ねていただければと存じます。</p><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>1.2. 今回のお題: ディレクトリのバックアップ処理＋α<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>第一回はベタで、かつあまりテキスト処理とは縁がなさそうな、バックアップ処理を扱います。<br />
お題はベタですが、連載で目指すコマンドの使い方を見せることができると考え、<br />
取り上げました。また、処理の途中でちょっとしたテキスト処理が出てきます。</p><br />
<p>下のような状況を想定します。</p><br />
<ul class="simple"><br />
<li>/var/wwwの下が、毎日少しずつ書き換わる。</li><br />
<li>/var/wwwの下にはそんなにファイルがないので、毎日丸ごとバックアップを取る。</li><br />
<li>しかし、バックアップファイルが増えすぎるのはいやなので、昔のものは適切に間引きたい。</li><br />
</ul><br />
<p>バックアップファイルには日付を入れて管理することになります。<br />
間引く際には日付の計算をすることになるので、バックアップ自体よりも、<br />
日付の計算をどのようにシェルスクリプトで書くかということが鍵になりそうです。</p><br />
<div class="section" id="id7"><br />
<h3>1.2.1. 環境等<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>筆者が本連載のために使っているシェル、OS（ディストリビューション）、<br />
マシンは以下の通りです。</p><br />
<ul class="simple"><br />
<li>シェル：bash 4.1.2</li><br />
<li>OS：Linux (CentOS 6)</li><br />
<li>マシン：ThinkPad x41</li><br />
</ul><br />
<p>テキストの文字コードは、UTF-8です。</p><br />
<p>スクリプトは平易な文法で書きますので、<br />
bashのバージョンが違って困ることはないと考えています。<br />
OSやディストリビューションの違いについては、<br />
Macも含めてUNIX系ならば、bashが動けばなんとかなります。<br />
文中のコードがそのままで動くという保証はありませんが、<br />
コマンドのオプションを変えたり、<br />
コマンドをインストールすることでご自身で試すことはできます。<br />
どこにソースが転がっているか分からないコマンドは使いませんので、<br />
適宜インストールするか、オプションを調整して乗り切っていただけたらと考えております。</p><br />
</div><br />
<div class="section" id="id8"><br />
<h3>1.2.2. 肩慣らし<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>まずは/var/wwwをバックアップするシェルスクリプトを書いてみましょう。<br />
tarコマンドで/var/wwwディレクトリのファイルを固め、<br />
ホームディレクトリ下の./WWW.BACKUPというディレクトリに置くことにします。<br />
シェルスクリプトを動かすアカウントで、<br />
/var/wwwが読めるようにパーミッション設定されていることが前提です。</p><br />
<p>シェルスクリプトを書いてみたのがリスト1のコードです。<br />
シェルスクリプト名は~/SYS/WWW.BACKUPとしました。<br />
バックアップファイルの置き場所は上記のように~/WWW.BACKUP、<br />
ファイル名は、www.&lt;日付&gt;.tar.gzとしました。<br />
ディレクトリ名やファイル名の命名規則は、<br />
ある「お作法」にしたがっていますが、ここではあまり気にしないでください。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1<br />
 2<br />
 3<br />
 4<br />
 5<br />
 6<br />
 7<br />
 8<br />
 9<br />
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<br />
<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="c">#/tmpに/var/www/の内容を固めて圧縮</span><br />
tar zcvf <span class="nv">$tmp</span>.tar.gz /var/www/<br />
<span class="c">#バックアップファイルの置き場所に移動</span><br />
mv <span class="nv">$tmp</span>.tar.gz <span class="k">${</span><span class="nv">dest</span><span class="k">}</span>/www.<span class="k">${</span><span class="nv">today</span><span class="k">}</span>.tar.gz<br />
</pre></div><br />
</td></tr></table></div><br />
<p>【リスト1: 最初のWWW.BACKUP】</p><br />
<p>たった10行なので、このコードを使っておさらいをしましょう。<br />
1行目の#から始まる行ですが、<br />
これはスクリプトを読み込むインタプリタを指定するための行です。<br />
#!のことを「シバン」（shebang）と言います。<br />
インタプリタは、ここではbashなので、bashの置いてある/bin/bashを指定します。</p><br />
<p>もし/bin/bashにbashが無い場合は、以下のようにwhichコマンドを使って調べましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ </span>which bash<br />
/bin/bash<br />
</pre></div><br />
</div><br />
<p>#!/bin/bash の後ろの-xvは、<br />
シェルスクリプト実行時にログが表示されるようにするオプションです。<br />
3～5行目は、変数を指定しています。<br />
変数と言っても、bashの変数は単に文字列を格納するためにあります。<br />
書き方は、3行目のように、</p><br />
<div class="highlight-bash"><div class="highlight"><pre>変数名<span class="o">=</span>値となる文字列<br />
</pre></div><br />
</div><br />
<p>です。3行目で、destという変数に「/home/ueda/WWW.BACKUP」という文字列が格納されます。<br />
=の両側に空白を入れてはいけません。空白を入れてしまうと、<br />
bashが、変数のつもりで書いた文字列をコマンドだと解釈します。<br />
変数destは、シェルスクリプト中で$destや${dest}と書くと値に置き換わります。</p><br />
<p>4, 5行目は、ちょっと難しいことをしています。<br />
4行目は、tmpという変数に、「/tmp/」と「$$という変数の値」をくっつけた文字列を格納しています。<br />
これでよく分からなければ、以下のように実際に打ってみましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$tmp</span><br />
/tmp/8389<br />
</pre></div><br />
</div><br />
<p>「$$」は予約変数で、このシェルスクリプトのプロセス番号が格納されています。<br />
tmpはファイル名に使いますが、プロセス番号を入れることでファイル名の衝突を防ぎます。</p><br />
<p>変数todayには、dateコマンドから出力される文字列が格納されます。<br />
これは言葉で説明するより、端末を叩いた方がよいでしょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#dateコマンドで8桁日付を出力</span><br />
<span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ </span>date +%Y%m%d<br />
20111022<br />
<span class="c">#$()でコマンドを囲うと、</span><br />
<span class="c">#コマンドから出力された文字列を変数に代入できる。</span><br />
<span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<span class="o">[</span>ueda\@cent GIHYO<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$today</span><br />
20111022<br />
</pre></div><br />
</div><br />
<p>変数を定義したら、あとは単にバックアップするコマンドを書くだけです。<br />
tarコマンドの使い方についてはご自身で調べていただきたいのですが、<br />
9行目で$tmp.tar.gzというファイルに/var/www/の内容が圧縮保存されます。<br />
このスクリプトでは、<br />
一度/tmpで作ったバックアップが10行目のmvで/home/ueda/WWW.BACKUPに移されています。<br />
これは、途中でスクリプトが止まったとき、<br />
中途半端なバックアップがWWW.BACKUPにできないようにする配慮です。</p><br />
<p>書いたら早速動かしてみましょう。図1のように、<br />
実行したときのログが画面に吐き出されるはずです。<br />
+印の行に、実行されたコマンドが表示されます。</p><br />
<div class="highlight-bash"><pre>[ueda\@cent SYS]$ ./WWW.BACKUP<br />
#!/bin/bash -vx<br />
<br />
dest=/home/ueda/WWW.BACKUP<br />
+ dest=/home/ueda/WWW.BACKUP<br />
tmp=/tmp/$$<br />
+ tmp=/tmp/9174<br />
today=$(date +%Y%m%d)<br />
date +%Y%m%d)<br />
date +%Y%m%d<br />
++ date +%Y%m%d<br />
+ today=20111022<br />
<br />
#/tmpに/var/www/の内容を固めて圧縮<br />
tar zcvf $tmp.tar.gz /var/www/<br />
+ tar zcvf /tmp/9174.tar.gz /var/www/<br />
tar: Removing leading `/' from member names<br />
/var/www/<br />
/var/www/html/<br />
（中略。だらだらと保存したファイルが表示される。）<br />
#バックアップファイルの置き場所に移動<br />
mv $tmp.tar.gz ${dest}/www.${today}.tar.gz<br />
+ mv /tmp/9227.tar.gz /home/ueda/WWW.BACKUP/www.20111022.tar.gz</pre><br />
</div><br />
<p>【図1: WWW.BACKUPの実行ログ】</p><br />
<p>WWW.BACKUPディレクトリにファイルがあったら成功です。解凍できるか試してください。<br />
（tar zxvf &lt;ファイル名&gt;で解凍できます。）</p><br />
</div><br />
<div class="section" id="id9"><br />
<h3>1.2.3. 日付の演算をコマンドだけで行う<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>さあ今回はここからが本番です。<br />
WWW.BACKUPを（crontabなどを使って）毎日実行すると、日々のファイルができます。<br />
これらのファイルを適切に間引くという処理をWWW.BACKUPに追加します。<br />
具体的には、「直近一週間のバックアップファイルを残し、<br />
あとは毎週日曜のバックアップファイルだけを残す。」という処理を記述します。</p><br />
<p>このような処理は、プログラミングに慣れた人なら、<br />
「for文を作り、for文の中で一つずつバックアップファイルの日付を調べ、<br />
if文で処理を場合分けし・・・」というコードを書いていくことが通常です。<br />
しかしシェルスクリプトでそれをやってしまうと、読みやすいコードになりません。<br />
シェルが得意なのはファイル入出力とパイプライン処理なので、<br />
これらを駆使して入れ子の少ない平坦なコードを書きます。</p><br />
<p>まず、上で書いたシェルスクリプトについて、<br />
tarを使う前の部分をリスト2のように書き加えます。<br />
初めて見た方のために補足すると、<br />
パイプ「|」は、コマンドの出力を次のコマンドに渡すための記号、<br />
リダイレクト「&gt;」は、コマンドの出力をファイルに保存するための記号です。</p><br />
<p>14行目から18行目はデバッグのためのコードで、<br />
「昔のバックアップ」のダミーファイルを作っています。<br />
この部分は最後に消します。もしwhileがうまく動かなければ、<br />
端末で手打ちでダミーファイルを作っても構いません。<br />
17行目のdateコマンドの使い方はあまりなじみが無いかもしれませんが、<br />
-dというオプションを使うと日付の演算ができます。<br />
20行目以降は古いファイルを間引くパートです。<br />
記述はまだ途中で、この段階ではファイルの日付を取得して表示しているだけです。</p><br />
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<br />
<span class="c">#ログをlogというファイルに保存する</span><br />
<span class="nb">exec </span>2&gt; ./log<br />
<br />
<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="c">###############################################################</span><br />
<span class="c">#デバッグのため、ダミーファイルを作る</span><br />
<span class="c">#稼動時には消す。</span><br />
<br />
<span class="nv">d</span><span class="o">=</span>20100101<br />
<span class="k">while</span> <span class="o">[</span> <span class="nv">$d</span> -lt <span class="nv">$today</span> <span class="o">]</span> ; <span class="k">do</span><br />
<span class="k"> </span>touch <span class="nv">$dest</span>/www.<span class="nv">$d</span>.tar.gz<br />
 <span class="nv">d</span><span class="o">=</span><span class="k">$(</span>date -d <span class="s2">&quot;${d} 1 day&quot;</span> +%Y%m%d<span class="k">)</span><br />
<span class="k">done</span><br />
<br />
<span class="c">###############################################################</span><br />
<span class="c">#古いファイルの削除</span><br />
<br />
<span class="c">#移動</span><br />
<span class="nb">cd</span> <span class="nv">$dest</span><br />
<span class="c">#ファイル列挙</span><br />
ls |<br />
<span class="c">#ドットを区切り文字にして第二フィールド（＝日付）を取り出す。</span><br />
cut -d. -f2 |<br />
<span class="c">#日付ではないものを除去</span><br />
egrep <span class="s2">&quot;[0-9]{8}&quot;</span> |<br />
<span class="c">#念のためソート</span><br />
sort &gt; <span class="nv">$tmp</span>-days<br />
<br />
<span class="c">#デバッグのために出力</span><br />
cat <span class="nv">$tmp</span>-days<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
<span class="o">(</span>以下略。tarの処理が書いてある。<span class="o">)</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>【リスト2: 日付の処理を途中まで加えたWWW.BACKUP】</p><br />
<p>$tmp-daysに日付の一覧ができたので、この中からファイルを消すべき日付を抽出します。<br />
シェルスクリプトを書いたことのある人は、<br />
読み進む前にぜひコードを考えてみてください。<br />
コードには、「if」が一個も現れません。</p><br />
<p>筆者の書いたコードをリスト3に示します。$tmp-daysを求めた後の部分です。<br />
2行目から13行目で、直近7日分の日付を書いたファイルと、<br />
日曜日を書いたファイルを作成します。<br />
その後、17, 18行目で「直近7日分でも日曜日でもない日付」を抽出しています。</p><br />
<p>6～9行目のwhileの部分が汚いですが、ここでは日付のデータに曜日を付加しています。<br />
6行目で$tmp-daysの内容がパイプから一行ずつ読み込まれて変数dにセットされています。<br />
7行目のdateで、変数dの日付に曜日が付けられます。<br />
dateコマンドの出力は、doneの後のパイプからgrepに渡っています。</p><br />
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#直近7日分の日付</span><br />
tail -n 7 <span class="nv">$tmp</span>-days &gt; <span class="nv">$tmp</span>-lastdays<br />
<br />
<span class="c">#日曜日</span><br />
cat <span class="nv">$tmp</span>-days |<br />
<span class="k">while </span><span class="nb">read </span>d ; <span class="k">do</span><br />
<span class="k"> </span>date -d <span class="s2">&quot;${d}&quot;</span> +<span class="s2">&quot;%Y%m%d %w&quot;</span><br />
 <span class="c">#1:日付 2:曜日（ゼロが日曜）</span><br />
<span class="k">done</span> |<br />
<span class="c">#第二フィールドが0のものだけ残す</span><br />
grep <span class="s2">&quot;0$&quot;</span> |<br />
<span class="c">#曜日を消す</span><br />
cut -d<span class="s2">&quot; &quot;</span> -f1 &gt; <span class="nv">$tmp</span>-sundays<br />
<br />
<span class="c">#days,lastdays,sundaysをマージして、</span><br />
<span class="c">#一つしかない日付が削除対象</span><br />
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |<br />
uniq -u &gt; <span class="nv">$tmp</span>-remove<br />
<br />
<span class="c">#デバッグのため出力</span><br />
cat <span class="nv">$tmp</span>-remove<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>【リスト3: ファイルを消す日付を求めるためのロジック】</p><br />
<p>18行目のuniq -uは、一個だけしかない日付だけ出力するという動きをします。<br />
これで、$tmp-daysにあって、$tmp-lastdaysや$tmp-sundaysに無い日付だけが出力されるので、<br />
「直近7日でも日曜でもない日付＝ファイルを消す日付」が得られます。<br />
sortとuniqだけでこのような演算ができるということに気づくにはちょっと経験が要りますが、<br />
二行で済んでしまう破壊力は抜群です。</p><br />
</div><br />
<div class="section" id="id10"><br />
<h3>1.2.4. 完成<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>では、肝心の「消去する」を実装しましょう。<br />
これもxargsというコマンドを知っていれば、一行で実装できます。<br />
リスト4のように、uniq -uの後に次のようにパイプでつなぎます。</p><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#days,lastdays,sundaysをマージして、</span><br />
<span class="c">#一つしかない日付が削除対象</span><br />
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |<br />
uniq -u |<br />
<span class="c">#消去対象日付がパイプを通って来る。</span><br />
xargs -i rm www.<span class="s1">&#39;{}&#39;</span>.tar.gz<br />
</pre></div><br />
</td></tr></table></div><br />
<p>【リスト4: xargsとrmで指定日付のファイルを消去】</p><br />
<p>xargsは、パイプから受けた文字をオプションに変換するコマンドです。<br />
この例では、www.と.tar.gzの間に日付を一つずつ入れてrmのオプションにしていきます。<br />
この連載ではあまり難しいコマンドを使うことは避けていきますが、<br />
while文をなくすためなら、このような高度なコマンドも扱っていきます。</p><br />
<p>最後に、体裁を整えたシェルスクリプトをリスト5に示します。<br />
本文で触れていない小細工も盛り込んでいますので、解析してみてください。</p><br />
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
46<br />
47<br />
48<br />
49<br />
50<br />
51<br />
52<br />
53<br />
54<br />
55<br />
56<br />
57</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span><br />
<span class="c">#</span><br />
<span class="c"># /var/wwwのバックアップ</span><br />
<span class="c">#</span><br />
<span class="c"># written by R. UEDA (USP研究所) Oct. 10, 2011</span><br />
<span class="c">#</span><br />
<br />
<span class="nb">exec </span>2&gt; /home/ueda/LOG/LOG.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>.<span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP<br />
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span><br />
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span><br />
<br />
<span class="c">###############################################################</span><br />
<span class="c">#古いファイルの削除</span><br />
<br />
<span class="c">#移動</span><br />
<span class="nb">cd</span> <span class="nv">$dest</span><br />
<span class="c">#ファイル列挙</span><br />
ls |<br />
<span class="c">#ドットを区切り文字にして第二フィールド（＝日付）を取り出す。</span><br />
cut -d. -f2 |<br />
<span class="c">#日付ではないものを除去</span><br />
egrep <span class="s2">&quot;[0-9]{8}&quot;</span> |<br />
<span class="c">#念のためソート</span><br />
sort &gt; <span class="nv">$tmp</span>-days<br />
<br />
<span class="c">#直近7日分の日付のリスト</span><br />
tail -n 7 <span class="nv">$tmp</span>-days &gt; <span class="nv">$tmp</span>-lastdays<br />
<br />
<span class="c">#日曜日のリスト</span><br />
cat <span class="nv">$tmp</span>-days |<br />
<span class="k">while </span><span class="nb">read </span>d ; <span class="k">do</span><br />
<span class="k"> </span>date -d <span class="s2">&quot;${d}&quot;</span> +<span class="s2">&quot;%Y%m%d %w&quot;</span><br />
 <span class="c">#1:日付 2:曜日（ゼロが日曜）</span><br />
<span class="k">done</span> |<br />
<span class="c">#第二フィールドが0のものだけ残す</span><br />
grep <span class="s2">&quot;0$&quot;</span> |<br />
<span class="c">#曜日を消す</span><br />
cut -d<span class="s2">&quot; &quot;</span> -f1 &gt; <span class="nv">$tmp</span>-sundays<br />
<br />
<span class="c">#days,lastdays,sundaysをマージして、</span><br />
<span class="c">#レコードが一つしかない日付が削除対象</span><br />
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |<br />
uniq -u |<br />
xargs --verbose -i rm www.<span class="s1">&#39;{}&#39;</span>.tar.gz<br />
<br />
<span class="c">###############################################################</span><br />
<span class="c">#バックアップ</span><br />
<br />
<span class="c">#/tmpに/var/www/の内容を固めて圧縮</span><br />
tar zcvf <span class="nv">$tmp</span>.tar.gz /var/www/ &gt;&amp;2<br />
<span class="c">#バックアップファイルの置き場所に移動</span><br />
mv <span class="nv">$tmp</span>.tar.gz <span class="k">${</span><span class="nv">dest</span><span class="k">}</span>/www.<span class="k">${</span><span class="nv">today</span><span class="k">}</span>.tar.gz<br />
<br />
rm -f <span class="nv">$tmp</span>-*<br />
<span class="nb">exit </span>0<br />
</pre></div><br />
</td></tr></table></div><br />
<p>【リスト5: 完成したWWW.BACKUP】</p><br />
<p>シェルスクリプトを書いたら、コメントは豊富に書きましょう。<br />
コマンド自体は汎用品なので、使った意図を書いておかないと後から意味不明になります。<br />
逆に言えば、意図と処理がはっきり分かれるということが、シェルスクリプトの特徴とも言えます。</p><br />
<p>今回の例で気づいた人もいると思いますが、短いシェルスクリプトを書けるようになる第一歩は、<br />
ファイルを配列の代わりに使う癖を付けることです。<br />
grepやuniqなどのコマンドの多くも、実はそういうことを前提に作られているのです。</p><br />
</div><br />
</div><br />
<div class="section" id="id11"><br />
<h2>1.3. おわりに<a class="headerlink" href="#id11" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>今回は、シェルスクリプトを書く動機について説明し、<br />
バックアップというお題に対するシェルスクリプトWWW.BACKUPを作りました。<br />
WWW.BACKUPは57行のスクリプトで、そのうちコードが23行、コメントと空白が34行でした。<br />
制御構文は、while文1個で、if文はゼロでした。</p><br />
<p>以下が今回の重要な点です。</p><br />
<ul class="simple"><br />
<li>テキストファイルはソフトに束縛されず、自由</li><br />
<li>ファイルを配列代わりに使うと短いシェルスクリプトを記述可能</li><br />
</ul><br />
<p>次回以降もUNIX哲学の道を邁進しますので、ご贔屓に。</p><br />
</div><br />
<div class="section" id="id12"><br />
<h2>1.4. 出典<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>[Gancarz2011] Mike Gancarz (著), 芳尾 桂 (翻訳):<br />
UNIXという考え方 &#8211;その設計思想と哲学, オーム社, 2001.</p><br />
<p>[Raymond2007] Eric S.Raymond (著), 長尾 高弘 (翻訳):<br />
The Art of UNIX Programming, アスキー, 2007.</p><br />
</div><br />
</div><br />
<br />

