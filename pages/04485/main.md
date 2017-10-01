---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年1月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>1. 開眼　シェルスクリプト　第1回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>1.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="gancarzunix">
<h3>1.1.1. GancarzのUNIX哲学<a class="headerlink" href="#gancarzunix" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>突然ですが、これがなんだかご存知でしょうか？</p>
<ul class="simple">
<li>小さいものは美しい。</li>
<li>各プログラムが一つのことをうまくやるようにせよ。</li>
<li>できる限り原型（プロトタイプ）を作れ。</li>
<li>効率よりも移植しやすさを選べ。</li>
<li>単純なテキストファイルにデータを格納せよ。</li>
<li>ソフトウェアの効率をきみの優位さとして利用せよ。</li>
<li>効率と移植性を高めるためにシェルスクリプトを利用せよ。</li>
<li>束縛するインターフェースは作るな。</li>
<li>全てのプログラムはフィルタとして振る舞うようにせよ。</li>
</ul>
<p>これはGancarzのUNIX哲学 [Gancarz2001]というものです。
UNIX（系OS）の使い方、さらには世界観をまとめたもので、
極めて乱暴にまとめると、</p>
<p>「端末やシェルスクリプトでコマンドを使い倒して早く仕事しようぜ」</p>
<p>ということを言っています。（繰り返しますが乱暴です。）</p>
<p>ここで言っている仕事というのは、
エンジニアがコンピュータのために仕事をすることよりも、
顧客データ管理、表計算、原稿書きなど利用することだと考えてください。
UNIXの使い方がCLI（コマンドラインユーザインタフェース）中心だった時代は、
テキストファイルに字を書いて保存したり、検索したり、
表計算したりすることが普通のことだったのです。
（私自身はそんな時代を知らない一人ですが。）</p>
</div>
<div class="section" id="id3">
<h3>1.1.2. テキストファイルは自由だ<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>現在は、便利なGUIソフトがいろいろできたおかげで、
何でもCLIという窮屈なことは無くなりましたが、
テキストファイルが必要なくなることはありません。
どんなワープロソフトでもテキストのペーストは受け付けますし、
インターネットのプロトコルの多くはテキストベースです。
文字しかないということは、ソフトウェア同士、
あるいはコンピュータと人間の間で余計な決めごとが無いという利点があるのです。</p>
<p>また、テキストでデータを持っておくと、何にでも化けるという利点があります。
上記のUNIX哲学で「単純なテキストファイルにデータを格納せよ」
と言っているのはまさにこのことです。
筆者の例で恐縮ですが、今、
この原稿をreST（restructuredText）という形式のテキストで書いています。
reSTはそのまま編集の方に渡しても読んでもらえるほど分かりやすい形式です。
そして、Sphinxというツールに通すとhtmlに変換できるので、
体裁をブラウザで確認しながら書いています。
次回の執筆はもっと便利なように、</p>
<ul class="simple">
<li>さらに編集者フレンドリーなテキストに変換するスクリプト</li>
<li>掲載時とそっくりな体裁になるLaTeX形式への変換スクリプト</li>
</ul>
<p>を書いてから開始しようと考えています。
自分の書くreSTだけ相手にすればよいので、そんなに難しくはないでしょう。</p>
<p>このようにテキストで済ませていると、特定のソフトの仕様に束縛されることがありません。
我々の場合なら、ちょっとプログラムでも書いてみようかという気持ちになるでしょう。
[Raymond2007]にも、UNIXはテキスト文化なので、
気軽にプログラムに入門できる効用があると述べられています。</p>
</div>
<div class="section" id="id4">
<h3>1.1.3. 短いシェルスクリプトで様々な処理を<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>UNIX系OSのコマンドの多くは、テキスト処理のためにあります。
ただ、一つ一つのコマンドを端末で使う機会は多くの人にあるようですが、
組み合わせてシェルスクリプトにすると複雑な処理ができることは、
あまり知られていません。知られていないと言うより、
忘れ去られていると言った方が適切かもしれません。</p>
<p>この連載の目的は、UNIX系OSでコマンドを触ったことのある人に、
シェルスクリプトの便利な利用例を紹介し、
もっとコマンドの用途を広げてもらうことにあります。
コマンドをシェルスクリプトで組み合わせると、
役に立つプログラムが短く書けてしまう例を紹介していきます。
コマンドが多くの仕事をするので、シェルスクリプトを上手く書けば、
とてもあっさりとしたものが出来上がります。</p>
<p>ただし、「短いシェルスクリプト」に開眼するには、
ほとんどの人の場合、ある一定の時間がかかります。
特になにかしらの言語を知っている人が書くと、インデントとfor文だらけになりがちです。
そのようなシェルスクリプトはもっと短くできるのですが、
重要な割にニッチすぎて話題になりません・・・。</p>
<p>そこで本連載では、「シェルスクリプトの便利な利用例」と同じくらいの重要度で、
「短いシェルスクリプトを書く手練手管」も紹介していきます。
シェルスクリプトを使うことにピンと来ない人でも、
「深いインデント回避のためのロジック」を楽しんでいただけたらと考えています。</p>
</div>
<div class="section" id="id5">
<h3>1.1.4. 筆者について<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>これを書いているのは、USP研究所という、
シェルスクリプトで業務システムを構築する会社に勤務し、
毎日シェルスクリプトばかり書いている男です。
短く書いて早く仕事を終わらせることにのみ、心血を注いでいます。</p>
<ul>
<li><dl class="first docutils">
<dt>USP研究所</dt>
<dd><ul class="first last simple">
<li><a class="reference external" href="http://www.usp-lab.com/">http://www.usp-lab.com/</a></li>
</ul>
</dd>
</dl>
</li>
</ul>
<p>夜は（？）USP友の会というシェルスクリプトの会の会長として、
主に技術以外のところで微妙な働きをしています。</p>
<ul>
<li><dl class="first docutils">
<dt>USP友の会</dt>
<dd><ul class="first last simple">
<li>web: <a class="reference external" href="http://www.usptomonokai.jp/">http://www.usptomonokai.jp/</a></li>
<li>twitter: &#64;usptomo</li>
<li>facebook: <a class="reference external" href="http://www.facebook.com/usptomo">http://www.facebook.com/usptomo</a></li>
</ul>
</dd>
</dl>
</li>
</ul>
<p>前職では某大学でロボットのプログラムばかり書き、
学生にもそれを強要していました。この時代は映像処理、カメラの制御、
その他人工知能的なものをひたすらプログラムしており、主にC++を使っていました。
現在もロボカップ（ロボットサッカーの大会）の日本大会で手伝いをしています。</p>
<ul>
<li><dl class="first docutils">
<dt>RoboCup Japan Open</dt>
<dd><ul class="first last simple">
<li><a class="reference external" href="http://www.robocup-japanopen.org/">http://www.robocup-japanopen.org/</a></li>
</ul>
</dd>
</dl>
</li>
</ul>
<p>もしシェルスクリプトに興味をそそられるようでしたら、
USP友の会が出没するイベントを訪ねていただければと存じます。</p>
</div>
</div>
<div class="section" id="id6">
<h2>1.2. 今回のお題: ディレクトリのバックアップ処理＋α<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>第一回はベタで、かつあまりテキスト処理とは縁がなさそうな、バックアップ処理を扱います。
お題はベタですが、連載で目指すコマンドの使い方を見せることができると考え、
取り上げました。また、処理の途中でちょっとしたテキスト処理が出てきます。</p>
<p>下のような状況を想定します。</p>
<ul class="simple">
<li>/var/wwwの下が、毎日少しずつ書き換わる。</li>
<li>/var/wwwの下にはそんなにファイルがないので、毎日丸ごとバックアップを取る。</li>
<li>しかし、バックアップファイルが増えすぎるのはいやなので、昔のものは適切に間引きたい。</li>
</ul>
<p>バックアップファイルには日付を入れて管理することになります。
間引く際には日付の計算をすることになるので、バックアップ自体よりも、
日付の計算をどのようにシェルスクリプトで書くかということが鍵になりそうです。</p>
<div class="section" id="id7">
<h3>1.2.1. 環境等<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>筆者が本連載のために使っているシェル、OS（ディストリビューション）、
マシンは以下の通りです。</p>
<ul class="simple">
<li>シェル：bash 4.1.2</li>
<li>OS：Linux (CentOS 6)</li>
<li>マシン：ThinkPad x41</li>
</ul>
<p>テキストの文字コードは、UTF-8です。</p>
<p>スクリプトは平易な文法で書きますので、
bashのバージョンが違って困ることはないと考えています。
OSやディストリビューションの違いについては、
Macも含めてUNIX系ならば、bashが動けばなんとかなります。
文中のコードがそのままで動くという保証はありませんが、
コマンドのオプションを変えたり、
コマンドをインストールすることでご自身で試すことはできます。
どこにソースが転がっているか分からないコマンドは使いませんので、
適宜インストールするか、オプションを調整して乗り切っていただけたらと考えております。</p>
</div>
<div class="section" id="id8">
<h3>1.2.2. 肩慣らし<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>まずは/var/wwwをバックアップするシェルスクリプトを書いてみましょう。
tarコマンドで/var/wwwディレクトリのファイルを固め、
ホームディレクトリ下の./WWW.BACKUPというディレクトリに置くことにします。
シェルスクリプトを動かすアカウントで、
/var/wwwが読めるようにパーミッション設定されていることが前提です。</p>
<p>シェルスクリプトを書いてみたのがリスト1のコードです。
シェルスクリプト名は~/SYS/WWW.BACKUPとしました。
バックアップファイルの置き場所は上記のように~/WWW.BACKUP、
ファイル名は、www.&lt;日付&gt;.tar.gzとしました。
ディレクトリ名やファイル名の命名規則は、
ある「お作法」にしたがっていますが、ここではあまり気にしないでください。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>

<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="c">#/tmpに/var/www/の内容を固めて圧縮</span>
tar zcvf <span class="nv">$tmp</span>.tar.gz /var/www/
<span class="c">#バックアップファイルの置き場所に移動</span>
mv <span class="nv">$tmp</span>.tar.gz <span class="k">${</span><span class="nv">dest</span><span class="k">}</span>/www.<span class="k">${</span><span class="nv">today</span><span class="k">}</span>.tar.gz
</pre></div>
</td></tr></table></div>
<p>【リスト1: 最初のWWW.BACKUP】</p>
<p>たった10行なので、このコードを使っておさらいをしましょう。
1行目の#から始まる行ですが、
これはスクリプトを読み込むインタプリタを指定するための行です。
#!のことを「シバン」（shebang）と言います。
インタプリタは、ここではbashなので、bashの置いてある/bin/bashを指定します。</p>
<p>もし/bin/bashにbashが無い場合は、以下のようにwhichコマンドを使って調べましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ </span>which bash
/bin/bash
</pre></div>
</div>
<p>#!/bin/bash の後ろの-xvは、
シェルスクリプト実行時にログが表示されるようにするオプションです。
3～5行目は、変数を指定しています。
変数と言っても、bashの変数は単に文字列を格納するためにあります。
書き方は、3行目のように、</p>
<div class="highlight-bash"><div class="highlight"><pre>変数名<span class="o">=</span>値となる文字列
</pre></div>
</div>
<p>です。3行目で、destという変数に「/home/ueda/WWW.BACKUP」という文字列が格納されます。
=の両側に空白を入れてはいけません。空白を入れてしまうと、
bashが、変数のつもりで書いた文字列をコマンドだと解釈します。
変数destは、シェルスクリプト中で$destや${dest}と書くと値に置き換わります。</p>
<p>4, 5行目は、ちょっと難しいことをしています。
4行目は、tmpという変数に、「/tmp/」と「$$という変数の値」をくっつけた文字列を格納しています。
これでよく分からなければ、以下のように実際に打ってみましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$tmp</span>
/tmp/8389
</pre></div>
</div>
<p>「$$」は予約変数で、このシェルスクリプトのプロセス番号が格納されています。
tmpはファイル名に使いますが、プロセス番号を入れることでファイル名の衝突を防ぎます。</p>
<p>変数todayには、dateコマンドから出力される文字列が格納されます。
これは言葉で説明するより、端末を叩いた方がよいでしょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#dateコマンドで8桁日付を出力</span>
<span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ </span>date +%Y%m%d
20111022
<span class="c">#$()でコマンドを囲うと、</span>
<span class="c">#コマンドから出力された文字列を変数に代入できる。</span>
<span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>
<span class="o">[</span>ueda@cent GIHYO<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$today</span>
20111022
</pre></div>
</div>
<p>変数を定義したら、あとは単にバックアップするコマンドを書くだけです。
tarコマンドの使い方についてはご自身で調べていただきたいのですが、
9行目で$tmp.tar.gzというファイルに/var/www/の内容が圧縮保存されます。
このスクリプトでは、
一度/tmpで作ったバックアップが10行目のmvで/home/ueda/WWW.BACKUPに移されています。
これは、途中でスクリプトが止まったとき、
中途半端なバックアップがWWW.BACKUPにできないようにする配慮です。</p>
<p>書いたら早速動かしてみましょう。図1のように、
実行したときのログが画面に吐き出されるはずです。
+印の行に、実行されたコマンドが表示されます。</p>
<div class="highlight-bash"><pre>[ueda@cent SYS]$ ./WWW.BACKUP
#!/bin/bash -vx

dest=/home/ueda/WWW.BACKUP
+ dest=/home/ueda/WWW.BACKUP
tmp=/tmp/$$
+ tmp=/tmp/9174
today=$(date +%Y%m%d)
date +%Y%m%d)
date +%Y%m%d
++ date +%Y%m%d
+ today=20111022

#/tmpに/var/www/の内容を固めて圧縮
tar zcvf $tmp.tar.gz /var/www/
+ tar zcvf /tmp/9174.tar.gz /var/www/
tar: Removing leading `/' from member names
/var/www/
/var/www/html/
（中略。だらだらと保存したファイルが表示される。）
#バックアップファイルの置き場所に移動
mv $tmp.tar.gz ${dest}/www.${today}.tar.gz
+ mv /tmp/9227.tar.gz /home/ueda/WWW.BACKUP/www.20111022.tar.gz</pre>
</div>
<p>【図1: WWW.BACKUPの実行ログ】</p>
<p>WWW.BACKUPディレクトリにファイルがあったら成功です。解凍できるか試してください。
（tar zxvf &lt;ファイル名&gt;で解凍できます。）</p>
</div>
<div class="section" id="id9">
<h3>1.2.3. 日付の演算をコマンドだけで行う<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>さあ今回はここからが本番です。
WWW.BACKUPを（crontabなどを使って）毎日実行すると、日々のファイルができます。
これらのファイルを適切に間引くという処理をWWW.BACKUPに追加します。
具体的には、「直近一週間のバックアップファイルを残し、
あとは毎週日曜のバックアップファイルだけを残す。」という処理を記述します。</p>
<p>このような処理は、プログラミングに慣れた人なら、
「for文を作り、for文の中で一つずつバックアップファイルの日付を調べ、
if文で処理を場合分けし・・・」というコードを書いていくことが通常です。
しかしシェルスクリプトでそれをやってしまうと、読みやすいコードになりません。
シェルが得意なのはファイル入出力とパイプライン処理なので、
これらを駆使して入れ子の少ない平坦なコードを書きます。</p>
<p>まず、上で書いたシェルスクリプトについて、
tarを使う前の部分をリスト2のように書き加えます。
初めて見た方のために補足すると、
パイプ「|」は、コマンドの出力を次のコマンドに渡すための記号、
リダイレクト「&gt;」は、コマンドの出力をファイルに保存するための記号です。</p>
<p>14行目から18行目はデバッグのためのコードで、
「昔のバックアップ」のダミーファイルを作っています。
この部分は最後に消します。もしwhileがうまく動かなければ、
端末で手打ちでダミーファイルを作っても構いません。
17行目のdateコマンドの使い方はあまりなじみが無いかもしれませんが、
-dというオプションを使うと日付の演算ができます。
20行目以降は古いファイルを間引くパートです。
記述はまだ途中で、この段階ではファイルの日付を取得して表示しているだけです。</p>
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
39</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>

<span class="c">#ログをlogというファイルに保存する</span>
<span class="nb">exec </span>2&gt; ./log

<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="c">###############################################################</span>
<span class="c">#デバッグのため、ダミーファイルを作る</span>
<span class="c">#稼動時には消す。</span>

<span class="nv">d</span><span class="o">=</span>20100101
<span class="k">while</span> <span class="o">[</span> <span class="nv">$d</span> -lt <span class="nv">$today</span> <span class="o">]</span> ; <span class="k">do</span>
<span class="k"> </span>touch <span class="nv">$dest</span>/www.<span class="nv">$d</span>.tar.gz
 <span class="nv">d</span><span class="o">=</span><span class="k">$(</span>date -d <span class="s2">&quot;${d} 1 day&quot;</span> +%Y%m%d<span class="k">)</span>
<span class="k">done</span>

<span class="c">###############################################################</span>
<span class="c">#古いファイルの削除</span>

<span class="c">#移動</span>
<span class="nb">cd</span> <span class="nv">$dest</span>
<span class="c">#ファイル列挙</span>
ls |
<span class="c">#ドットを区切り文字にして第二フィールド（＝日付）を取り出す。</span>
cut -d. -f2 |
<span class="c">#日付ではないものを除去</span>
egrep <span class="s2">&quot;[0-9]{8}&quot;</span> |
<span class="c">#念のためソート</span>
sort &gt; <span class="nv">$tmp</span>-days

<span class="c">#デバッグのために出力</span>
cat <span class="nv">$tmp</span>-days

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
<span class="o">(</span>以下略。tarの処理が書いてある。<span class="o">)</span>
</pre></div>
</td></tr></table></div>
<p>【リスト2: 日付の処理を途中まで加えたWWW.BACKUP】</p>
<p>$tmp-daysに日付の一覧ができたので、この中からファイルを消すべき日付を抽出します。
シェルスクリプトを書いたことのある人は、
読み進む前にぜひコードを考えてみてください。
コードには、「if」が一個も現れません。</p>
<p>筆者の書いたコードをリスト3に示します。$tmp-daysを求めた後の部分です。
2行目から13行目で、直近7日分の日付を書いたファイルと、
日曜日を書いたファイルを作成します。
その後、17, 18行目で「直近7日分でも日曜日でもない日付」を抽出しています。</p>
<p>6～9行目のwhileの部分が汚いですが、ここでは日付のデータに曜日を付加しています。
6行目で$tmp-daysの内容がパイプから一行ずつ読み込まれて変数dにセットされています。
7行目のdateで、変数dの日付に曜日が付けられます。
dateコマンドの出力は、doneの後のパイプからgrepに渡っています。</p>
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
24</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#直近7日分の日付</span>
tail -n 7 <span class="nv">$tmp</span>-days &gt; <span class="nv">$tmp</span>-lastdays

<span class="c">#日曜日</span>
cat <span class="nv">$tmp</span>-days |
<span class="k">while </span><span class="nb">read </span>d ; <span class="k">do</span>
<span class="k"> </span>date -d <span class="s2">&quot;${d}&quot;</span> +<span class="s2">&quot;%Y%m%d %w&quot;</span>
 <span class="c">#1:日付 2:曜日（ゼロが日曜）</span>
<span class="k">done</span> |
<span class="c">#第二フィールドが0のものだけ残す</span>
grep <span class="s2">&quot;0$&quot;</span> |
<span class="c">#曜日を消す</span>
cut -d<span class="s2">&quot; &quot;</span> -f1 &gt; <span class="nv">$tmp</span>-sundays

<span class="c">#days,lastdays,sundaysをマージして、</span>
<span class="c">#一つしかない日付が削除対象</span>
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |
uniq -u &gt; <span class="nv">$tmp</span>-remove

<span class="c">#デバッグのため出力</span>
cat <span class="nv">$tmp</span>-remove

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>【リスト3: ファイルを消す日付を求めるためのロジック】</p>
<p>18行目のuniq -uは、一個だけしかない日付だけ出力するという動きをします。
これで、$tmp-daysにあって、$tmp-lastdaysや$tmp-sundaysに無い日付だけが出力されるので、
「直近7日でも日曜でもない日付＝ファイルを消す日付」が得られます。
sortとuniqだけでこのような演算ができるということに気づくにはちょっと経験が要りますが、
二行で済んでしまう破壊力は抜群です。</p>
</div>
<div class="section" id="id10">
<h3>1.2.4. 完成<a class="headerlink" href="#id10" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>では、肝心の「消去する」を実装しましょう。
これもxargsというコマンドを知っていれば、一行で実装できます。
リスト4のように、uniq -uの後に次のようにパイプでつなぎます。</p>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#days,lastdays,sundaysをマージして、</span>
<span class="c">#一つしかない日付が削除対象</span>
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |
uniq -u |
<span class="c">#消去対象日付がパイプを通って来る。</span>
xargs -i rm www.<span class="s1">&#39;{}&#39;</span>.tar.gz
</pre></div>
</td></tr></table></div>
<p>【リスト4: xargsとrmで指定日付のファイルを消去】</p>
<p>xargsは、パイプから受けた文字をオプションに変換するコマンドです。
この例では、www.と.tar.gzの間に日付を一つずつ入れてrmのオプションにしていきます。
この連載ではあまり難しいコマンドを使うことは避けていきますが、
while文をなくすためなら、このような高度なコマンドも扱っていきます。</p>
<p>最後に、体裁を整えたシェルスクリプトをリスト5に示します。
本文で触れていない小細工も盛り込んでいますので、解析してみてください。</p>
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
46
47
48
49
50
51
52
53
54
55
56
57</pre></div></td><td class="code"><div class="highlight"><pre><span class="c">#!/bin/bash -vx</span>
<span class="c">#</span>
<span class="c"># /var/wwwのバックアップ</span>
<span class="c">#</span>
<span class="c"># written by R. UEDA (USP研究所) Oct. 10, 2011</span>
<span class="c">#</span>

<span class="nb">exec </span>2&gt; /home/ueda/LOG/LOG.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>.<span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="nv">dest</span><span class="o">=</span>/home/ueda/WWW.BACKUP
<span class="nv">tmp</span><span class="o">=</span>/tmp/<span class="nv">$$</span>
<span class="nv">today</span><span class="o">=</span><span class="k">$(</span>date +%Y%m%d<span class="k">)</span>

<span class="c">###############################################################</span>
<span class="c">#古いファイルの削除</span>

<span class="c">#移動</span>
<span class="nb">cd</span> <span class="nv">$dest</span>
<span class="c">#ファイル列挙</span>
ls |
<span class="c">#ドットを区切り文字にして第二フィールド（＝日付）を取り出す。</span>
cut -d. -f2 |
<span class="c">#日付ではないものを除去</span>
egrep <span class="s2">&quot;[0-9]{8}&quot;</span> |
<span class="c">#念のためソート</span>
sort &gt; <span class="nv">$tmp</span>-days

<span class="c">#直近7日分の日付のリスト</span>
tail -n 7 <span class="nv">$tmp</span>-days &gt; <span class="nv">$tmp</span>-lastdays

<span class="c">#日曜日のリスト</span>
cat <span class="nv">$tmp</span>-days |
<span class="k">while </span><span class="nb">read </span>d ; <span class="k">do</span>
<span class="k"> </span>date -d <span class="s2">&quot;${d}&quot;</span> +<span class="s2">&quot;%Y%m%d %w&quot;</span>
 <span class="c">#1:日付 2:曜日（ゼロが日曜）</span>
<span class="k">done</span> |
<span class="c">#第二フィールドが0のものだけ残す</span>
grep <span class="s2">&quot;0$&quot;</span> |
<span class="c">#曜日を消す</span>
cut -d<span class="s2">&quot; &quot;</span> -f1 &gt; <span class="nv">$tmp</span>-sundays

<span class="c">#days,lastdays,sundaysをマージして、</span>
<span class="c">#レコードが一つしかない日付が削除対象</span>
sort -m <span class="nv">$tmp</span>-<span class="o">{</span>days,lastdays,sundays<span class="o">}</span> |
uniq -u |
xargs --verbose -i rm www.<span class="s1">&#39;{}&#39;</span>.tar.gz

<span class="c">###############################################################</span>
<span class="c">#バックアップ</span>

<span class="c">#/tmpに/var/www/の内容を固めて圧縮</span>
tar zcvf <span class="nv">$tmp</span>.tar.gz /var/www/ &gt;&amp;2
<span class="c">#バックアップファイルの置き場所に移動</span>
mv <span class="nv">$tmp</span>.tar.gz <span class="k">${</span><span class="nv">dest</span><span class="k">}</span>/www.<span class="k">${</span><span class="nv">today</span><span class="k">}</span>.tar.gz

rm -f <span class="nv">$tmp</span>-*
<span class="nb">exit </span>0
</pre></div>
</td></tr></table></div>
<p>【リスト5: 完成したWWW.BACKUP】</p>
<p>シェルスクリプトを書いたら、コメントは豊富に書きましょう。
コマンド自体は汎用品なので、使った意図を書いておかないと後から意味不明になります。
逆に言えば、意図と処理がはっきり分かれるということが、シェルスクリプトの特徴とも言えます。</p>
<p>今回の例で気づいた人もいると思いますが、短いシェルスクリプトを書けるようになる第一歩は、
ファイルを配列の代わりに使う癖を付けることです。
grepやuniqなどのコマンドの多くも、実はそういうことを前提に作られているのです。</p>
</div>
</div>
<div class="section" id="id11">
<h2>1.3. おわりに<a class="headerlink" href="#id11" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>今回は、シェルスクリプトを書く動機について説明し、
バックアップというお題に対するシェルスクリプトWWW.BACKUPを作りました。
WWW.BACKUPは57行のスクリプトで、そのうちコードが23行、コメントと空白が34行でした。
制御構文は、while文1個で、if文はゼロでした。</p>
<p>以下が今回の重要な点です。</p>
<ul class="simple">
<li>テキストファイルはソフトに束縛されず、自由</li>
<li>ファイルを配列代わりに使うと短いシェルスクリプトを記述可能</li>
</ul>
<p>次回以降もUNIX哲学の道を邁進しますので、ご贔屓に。</p>
</div>
<div class="section" id="id12">
<h2>1.4. 出典<a class="headerlink" href="#id12" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>[Gancarz2011] Mike Gancarz (著), 芳尾 桂 (翻訳):
UNIXという考え方 &#8211;その設計思想と哲学, オーム社, 2001.</p>
<p>[Raymond2007] Eric S.Raymond (著), 長尾 高弘 (翻訳):
The Art of UNIX Programming, アスキー, 2007.</p>
</div>
</div>


