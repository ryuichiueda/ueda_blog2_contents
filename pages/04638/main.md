---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2013年12月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="cron-crontab">
<h1>24. 開眼シェルスクリプト 第24回 cron/crontabとシェルスクリプトを組み合わせる<a class="headerlink" href="#cron-crontab" title="このヘッドラインへのパーマリンク">¶</a></h1>
<p>　皆様、定時出勤、定時退社してますか？
などと最初から挑発ともとれるような発言で炎上しそうですが、
今回の開眼シェルスクリプトは定時に何かをマシンにさせるcron、
具体的にはcrontabの使い方を扱います。
どうか、右手にお持ちの日本刀を鞘に戻してください。</p>
<p>　cronは、実行したい日時を指定しておけば、
プログラムを自動実行してくれる仕組みです。
Macを含むUNIX系のOSでは、ほとんどの場合、
最初から動いており、
<tt class="docutils literal"><span class="pre">crontab</span></tt> というコマンドを使って、
定期的に動作させたいプログラムを指定するだけで
プログラムが動くようになっています。</p>
<p>　本連載では2012年の10月号で使った例があります。
このときはさらっと説明しましたが、
cronには少し癖みたいなものがあるので、
落とし穴に嵌るとなかなか思うようになりません。
この癖は、シェルスクリプトを間に挟む事で緩和できます。
今回はほんのさわりだけですが、基本的な方法を示します。</p>
<p>　ところで、定期実行というと、昔、
カントというオッサンがいて、あまりに時間に忠実で、
カントが散歩で家の前を通る時刻に
合わせて家の人が時計を合わせたなどという逸話が残ってます。
cronも、それくらいは正確です（当たり前）。
ついでにこのオッサンの言い放ったことを書いておきます。</p>
<blockquote>
<div>我が行いを見習えと、誰にでも言い得るよう行為せよ。
&#8212; イマヌエル・カント</div></blockquote>
<p>先生、無理です。</p>
<p>　ところで、話が逸れたついでに報告しますと、
本連載は今回で終了です。当初、ネタが地味なだけに
6回連載して様子を見るという話でしたが、
シェルスクリプト=UNIXという筆者の勝手な拡大政策によって
気づけば今回で24回目です。
現在の風潮である、
みんなで一生懸命に莫迦でかいブラックボックスの使い方を勉強し、
みんなで愛と情熱を以てブラックボックスの
バージョンアップ地獄をフォローしていくという、
おおよそ工学的アプローチとは思えない騒ぎからのコペルニクス的転回を狙い、
今後も寒風の中裸一貫、地味にシェルスクリプト活動をしていく所存です。
あ、コペルニクス的転回も、カントの言った事です。
うまくまとまりました。</p>
<div class="section" id="croncrondcrontab">
<h2>24.1. cronとcrondとcrontabの関係<a class="headerlink" href="#croncrondcrontab" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、まず用語の整理から。
自分でインストールしなくても、だいたいの環境においては
cronという仕組みが動いています。
cronは仕組みの名前であって、実際には、
<tt class="docutils literal"><span class="pre">crond</span></tt> というサービスが最初から後ろで動いています。
crondというのは、cronのデーモンという意味ですね。
ただ、どの環境でもcrondの名前が <tt class="docutils literal"><span class="pre">crond</span></tt>
であるとは限らず、リスト1のように <tt class="docutils literal"><span class="pre">cron</span></tt>
になっていたりします。ややこしや。</p>
<ul class="simple">
<li>リスト1: 環境によって <tt class="docutils literal"><span class="pre">crond</span></tt> が動いていたり、 <tt class="docutils literal"><span class="pre">cron</span></tt> が動いていたり。</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda@CentOS ~<span class="o">]</span><span class="nv">$ </span>ps aux | grep cron | grep -v grep
root 1397 0.0 0.0 20408 452 ? Ss Feb04 7:25 crond
uedamac:OSX ueda<span class="nv">$ </span>ps aux | grep cron | grep -v grep
root 10058 0.0 0.0 2432784 156 ?? Ss 日03PM 0:00.39 /usr/sbin/cron
ueda@Ubuntu:~<span class="nv">$ </span>ps aux | grep cron | grep -v grep
root 748 0.0 0.0 19112 848 ? Ss Sep18 0:01 cron
</pre></div>
</td></tr></table></div>
<p>　 <tt class="docutils literal"><span class="pre">crontab</span></tt> は、cronで定期実行するプログラムを確認したり、
設定したりするためのコマンドです。
<tt class="docutils literal"><span class="pre">crontab</span></tt> で設定した内容はどこかにファイルで保存されているのですが、
このコマンドを通している限りはどこにあるか気にしなくて構いません。
あるユーザで <tt class="docutils literal"><span class="pre">crontab</span></tt> を呼び出し、
実行内容を書き込むと、その実行内容は、
そのユーザで動作します。
そして <tt class="docutils literal"><span class="pre">crontab</span></tt> に書いた自動実行のリストは、
<tt class="docutils literal"><span class="pre">crond</span></tt> を再起動しなくてもすぐに有効になります。
いつもcronを使っているような人でも、
<tt class="docutils literal"><span class="pre">crond</span></tt> を再起動したという経験は少ないかと思います。
筆者もありません。</p>
</div>
<div class="section" id="crontab">
<h2>24.2. crontabの使い方<a class="headerlink" href="#crontab" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p><tt class="docutils literal"><span class="pre">crontab</span></tt> の使い方ですが、まずは設定内容の編集方法から説明します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>crontab -e
</pre></div>
</div>
<p>と打つと、エディタ（ViかVim）が立ち上がります。
（Macの場合は注意があるので後述します。）</p>
<p>例えばここに次のように打ってみましょう。
（脚注：Viが使えないと苦労しますが、
その場合は <tt class="docutils literal"><span class="pre">vimtutor</span></tt> という練習用コマンドがありますので、
まずはそっちを練習しましょう。）</p>
<div class="highlight-bash"><div class="highlight"><pre>* * * * * touch /tmp/aaaa
</pre></div>
</div>
<p>これで普通のViの操作で保存して終了します。
ちゃんと登録されているかどうかは、
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-l</span></tt> で確認できます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>crontab -l
* * * * * touch /tmp/aaaa
</pre></div>
</div>
<p>1分くらい待って <tt class="docutils literal"><span class="pre">/tmp/aaaa</span></tt>
ができたらうまくcronが働いています。
さらに、1分ごとに <tt class="docutils literal"><span class="pre">ls</span></tt> を打ってみると、
タイムスタンプが変化している様子が分かります。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ls -l /tmp/aaaa
-rw-r--r-- 1 ueda wheel 0 9 22 16:24 /tmp/aaaa
uedamac:~ ueda<span class="nv">$ </span>ls -l /tmp/aaaa
-rw-r--r-- 1 ueda wheel 0 9 22 16:25 /tmp/aaaa
</pre></div>
</div>
<p>なぜそうなるかは後から説明しますが、
cronが1分ごとに <tt class="docutils literal"><span class="pre">touch</span></tt>
を起動して <tt class="docutils literal"><span class="pre">/tmp/aaaa</span></tt> のタイムスタンプを更新しているからです。</p>
<p>　今度は設定を消してみます。
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt> で編集してもよいのですが、
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> とやると、設定が全部消えます。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>crontab -r
uedamac:~ ueda<span class="nv">$ </span>crontab -l
crontab: no crontab <span class="k">for </span>ueda
</pre></div>
</div>
<p>これは「 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> で消しましょう」と言うよりは、
「 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> を押すと大変な事になるぞ！」
という注意の意味で紹介しました。</p>
<div class="section" id="id1">
<h3>24.2.1. ファイルでcrontabの内容を管理<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて、 <tt class="docutils literal"><span class="pre">crontab</span></tt> はMacでも使えますが、
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt> で編集した内容が反映されないという現象が発生します。
どうもVimと相性が悪いようです。
（脚注：<a class="reference external" href="http://d.hatena.ne.jp/yuyarin/20100225/1267084794">http://d.hatena.ne.jp/yuyarin/20100225/1267084794</a> や
<a class="reference external" href="http://d.hatena.ne.jp/shunsuk/20120122/1327239513">http://d.hatena.ne.jp/shunsuk/20120122/1327239513</a>
等で調査しました。）
Vimの設定ファイルをいじると解決するようですが、
ここではもうちょっと確実な方法を示しておきます。</p>
<p>　まず、名前はなんでもよいので、
以下のようなファイルを自分で作ります。
筆者はホームの下に <tt class="docutils literal"><span class="pre">etc</span></tt> を掘ってその下に、
<tt class="docutils literal"><span class="pre">crontab.conf</span></tt> という名前で作りました。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>cat crontab.conf
* * * * * touch /tmp/aaaa
</pre></div>
</div>
<p>　次に、 <tt class="docutils literal"><span class="pre">crontab</span></tt> にこのファイルを読み込ませます。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab crontab.conf
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">-l</span></tt> オプションで確認しましょう。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l
* * * * * touch /tmp/aaaa
</pre></div>
</div>
<p>こうやれば、 <tt class="docutils literal"><span class="pre">crontab</span></tt>
からViを呼び出したときに起こる不具合とは無縁です。
また、設定してやらなくても好きなエディタを使えます。</p>
<p>　また、これを応用すると、リスト2のような事もできます。</p>
<ul class="simple">
<li>リスト2: crontabでリストを出し入れ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># crontabの内容を書き出す</span>
uedamac:etc ueda<span class="nv">$ </span>crontab -l &gt; hoge
<span class="c"># crontabに書き出した内容を戻す</span>
uedamac:etc ueda<span class="nv">$ </span>crontab hoge
</pre></div>
</td></tr></table></div>
<p>この例は同じ物を書き出したり読み出したりしているだけで全く意味がないのですが、
別のサーバや別のユーザに、
cronの設定を簡単に移す事ができます。
そして、 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> をやらかしても、
またファイルを読ませれば復旧できます。</p>
<p>　ただし、この方法には欠点が一つあって、
<tt class="docutils literal"><span class="pre">crontab.conf</span></tt> を書いて満足してしまい、
読み込ませることを忘れがちになります。
ご注意を。</p>
</div>
<div class="section" id="id2">
<h3>24.2.2. コマンドの前の記号の意味<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて、次に時刻の指定の方法を説明します。
書式のマニュアルは <tt class="docutils literal"><span class="pre">man</span> <span class="pre">5</span> <span class="pre">crontab</span></tt> で調べることができますので、
ここでは最小限の説明をします。</p>
<p>　先ほど <tt class="docutils literal"><span class="pre">crontab</span></tt> で指定した</p>
<div class="highlight-bash"><div class="highlight"><pre>* * * * * touch /tmp/aaaa
</pre></div>
</div>
<p>ですが、この <tt class="docutils literal"><span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></tt> の部分が時刻の指定部分です。
順番に、分・時・日・月・曜日の指定で、
<tt class="docutils literal"><span class="pre">*</span></tt> はそれぞれ毎分、毎時、毎日・・・ということになります。
つまりはワイルドカードです。
上の例では、毎分、 <tt class="docutils literal"><span class="pre">touch</span> <span class="pre">/tmp/aaaa</span></tt> を行うという意味になります。
最小単位が分なので、最小の周期は1分ということになります。</p>
<p>　時刻の指定の例を一気に示します。
例えば、(1)毎時5分に実行したい、(2)5分ごとに実行したい、
(3)毎時15分と30分に実行したい、(4)月曜日の14時〜20時まで、
毎時30分に実行したい、というのを上から順に示すと、
リスト3のようになります。曜日の数字は、日曜から土曜まで、
0から6で指定します。日曜は7と書いてもOKです。
結局、次の点を押さえて慣れるということです。</p>
<ul class="simple">
<li>リスト3: crontabの書き方あれこれ</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l
5 * * * * touch /tmp/aaaa
*/5 * * * * touch /tmp/bbbb
15,30 * * * * touch /tmp/cccc
30 14-20 * * 1 touch /tmp/dddd
</pre></div>
</td></tr></table></div>
<ul class="simple">
<li>スラッシュの後ろに数字を書くと、その数字の周期で実行</li>
<li>カンマで数字を並べると、その数字に該当する時に実行</li>
<li>ハイフンで数字をつなぐと、その範囲内で毎回実行</li>
</ul>
<p>ハイフンについては、n-mと書いたら、nとmも含まれます。
また、ハイフンとスラッシュの併用もできます。
あとのことは、使いながら解説します。</p>
</div>
</div>
<div class="section" id="twittercron">
<h2>24.3. Twitterへの自動ツイートにcronを使う<a class="headerlink" href="#twittercron" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　さて、cronを使って何か作ってみましょう。
今回もMacで試します。リスト4に環境を示します。</p>
<ul class="simple">
<li>リスト4: 実験環境</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>uname -a
Darwin uedamac.local 12.5.0 Darwin Kernel Version 12.5.0: Mon Jul 29 16:33:49 PDT 2013; root:xnu-2050.48.11~1/RELEASE_X86_64 x86_64
</pre></div>
</td></tr></table></div>
<p>　それで、cronを使って何をしようかといろいろ考えたのですが、
今回はTwitterで自動ツイートを行うプログラムをしましょう。
と言っても一からシェルスクリプトでbotを作ると大変なので、
出来合いのコマンドを使います。
また、筆者が試した環境は OS X Server ではなく、
MacBook Air なので、
サスペンド状態だったりネットワークに接続されていなかったりすると、
ツイートできません。
ただ、今回の内容を他のUNIX環境に移植するのは簡単です。</p>
<div class="section" id="id3">
<h3>24.3.1. ツイートコマンドの準備<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p><a class="reference external" href="https://github.com/ryuichiueda/TomoTool/blob/master/Twitter/usptomo-tweet">https://github.com/ryuichiueda/TomoTool/blob/master/Twitter/usptomo-tweet</a>
に、筆者が作ったつぶやきコマンド（シェルスクリプト）
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> をダウンロードします。
ダウンロードの方法がわからなかったら、
画面をコピペして <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> ファイルに保存して、</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>chmod +x usptomo-tweet
</pre></div>
</div>
<p>としてください。コマンド名が長いので、
別に <tt class="docutils literal"><span class="pre">tw</span></tt> と変更しても構いません。</p>
<p>　 <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> 内部ではいろいろなコマンドを使っています。
ほとんど標準的なものですが、
<tt class="docutils literal"><span class="pre">nkf,</span> <span class="pre">curl,</span> <span class="pre">openssl</span></tt> コマンドあたりは
インストールされているか確認ください。
所詮書きなぐりのシェルスクリプトなので、
何か動かなかったら自分でログみて直すくらいの気持ちでお願いします。</p>
<p>　次に、鍵やトークンというものの設定を行います。
<a class="reference external" href="https://dev.twitter.com">https://dev.twitter.com</a> に行って、
ツイートしたいアカウントでログインします。
ログインしたら「My applications」の画面、
「Create an application」の画面に進み、
必要事項を入力してください。
アプリケーション名は何でも大丈夫です。
必要事項の入力後、登録のボタンを押すと、
「Consumer key、Consumer secret、
Access token、Access token secret」が取得できます。
普通に取得すると、Consumer keyもAccess tokenも、「Read only」
になっているはずです。画面の指示に従って「Read and write」
というアクセスレベルで再取得してください。
ここら辺、ややこしいのですが、
説明し出すと長くなってしまうので、
うまくWeb上で方法を見つけながらやってみてください。</p>
<p>　取得できたら、リスト5のようなファイルをホームの下に置きます。
これは <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> に読み込ませるシェルスクリプトの一部なので、
シェルスクリプトの文法で書き、ファイル名も間違えないようにします。
もしホーム下に置くのがいやだったら、
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> の中を書き換えます。</p>
<ul class="simple">
<li>リスト5: キーとトークンを書いたファイル</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>cat twitter.key
<span class="nv">CONSUMER_KEY</span><span class="o">=</span><span class="s2">&quot;aaaaaaaaaaaaaaaaaaaaaa&quot;</span>
<span class="nv">CONSUMER_SECRET</span><span class="o">=</span><span class="s2">&quot;bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb&quot;</span>
<span class="nv">ACCESS_TOKEN</span><span class="o">=</span><span class="s2">&quot;000000000-cccccccccccccccccccccccccccccccccccccccc&quot;</span>
<span class="nv">ACCESS_TOKEN_SECRET</span><span class="o">=</span><span class="s2">&quot;ddddddddddddddddddddddddddddddddddddddddddd&quot;</span>
</pre></div>
</td></tr></table></div>
</div>
<div class="section" id="id4">
<h3>24.3.2. ツイートしてみる<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　これで準備OKです。テストしてみましょう。
リスト6のように打ってみます。</p>
<ul class="simple">
<li>リスト6: 端末からテストツイート</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>./bin/usptomo-tweet <span class="s1">&#39;test: 東東東南南南西西西北北北白白&#39;</span>
</pre></div>
</td></tr></table></div>
<p>投稿がうまくいけば、図1のようにネット上にツイートが放出されます。</p>
<ul class="simple">
<li>図1: 投稿される</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="tweet.png"><img alt="" src="tweet.png" style="width: 50%;" /></a>
</div>
</div>
<div class="section" id="cron">
<h3>24.3.3. cronから使う（環境変数に気をつけて）<a class="headerlink" href="#cron" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　さて、cronと <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> を組み合わせて使ってみましょう。
とは言うものの、
cron には慣れていても慣れていなくてもいろいろな落とし穴があって、
なかなか一発でうまくいきません。
粘り強くいきましょう。
ここでは一つだけ、よく起こるミスを、
デバッグしながら紹介します。</p>
<p>　まず、リスト7のように仕掛けてみましょう。
時刻は直近のものに合わせます。
数分余裕を持って仕掛けるようにと書いてあるサイトがありますが、
おそらく余裕を持たせなくても大丈夫な環境がほとんどだと考えます。</p>
<ul class="simple">
<li>リスト7: crontabにコマンドを直接書き込む</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l
21 21 * * * /Users/ueda/bin/usptomo-tweet <span class="s1">&#39;test: びろーん&#39;</span> &gt; /dev/null 2&gt; /tmp/error
</pre></div>
</td></tr></table></div>
<p>時刻がきたら、 <tt class="docutils literal"><span class="pre">/tmp/error</span></tt> を見てみましょう。
環境にもよりますが、筆者のMacではリスト8のように失敗しました。</p>
<ul class="simple">
<li>リスト8: nkfが見つからないエラーが発生</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>less /tmp/error
（略）
/Users/ueda/bin/usptomo-tweet: line 33: nkf: <span class="nb">command </span>not found
（略）
</pre></div>
</td></tr></table></div>
<p>あれ？ <tt class="docutils literal"><span class="pre">nkf</span></tt> がインストールされていないのかな？
というところですが、
先ほど端末から試したときにはうまくいっていたので、
ここはパス（環境変数 <tt class="docutils literal"><span class="pre">PATH</span></tt> ）を疑います。</p>
<p>　 <tt class="docutils literal"><span class="pre">crontab</span></tt> でリスト9のように仕掛けます。
ついでに <tt class="docutils literal"><span class="pre">LANG</span></tt> も調べてみましょう。</p>
<ul class="simple">
<li>リスト9: echoでcronで設定されている環境変数を調べる</li>
</ul>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l
23 10 * * * <span class="nb">echo</span> <span class="s2">&quot;$PATH&quot;</span> &gt; /tmp/path
23 10 * * * <span class="nb">echo</span> <span class="s2">&quot;$LANG&quot;</span> &gt; /tmp/lang
</pre></div>
</div>
<p>時刻が来たら <tt class="docutils literal"><span class="pre">/tmp/path</span></tt> を見てみると、
リスト10のようになっていました。</p>
<ul class="simple">
<li>リスト10: 環境変数の調査結果</li>
</ul>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>cat /tmp/path
/usr/bin:/bin
uedamac:etc ueda<span class="nv">$ </span>cat /tmp/lang

（LANGには何も入っていない）
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">nkf</span></tt> の場所は次のように <tt class="docutils literal"><span class="pre">/usr/local/bin/</span></tt>
なので、 <tt class="docutils literal"><span class="pre">nkf</span></tt> が見つからずエラーが起きたようです。</p>
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>which nkf
/usr/local/bin/nkf
</pre></div>
</div>
<p>　cronで何かを動かそうとしてうまくいかない場合、
大抵はパスが間違っているか、
今の例のように環境変数が端末で使っている
ものと違うという問題に突き当たります。</p>
<p>　さて、原因が分かったので対策を。
まず、リスト11のようにcrontabに環境変数を設定する方法があります。</p>
<ul class="simple">
<li>リスト11: 環境変数をcrontabで指定する方法</li>
</ul>
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l
<span class="nv">PATH</span><span class="o">=</span>/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
<span class="nv">MAILTO</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
35 10 * * * /Users/ueda/bin/usptomo-tweet <span class="s1">&#39;test: びろーんぐ&#39;</span> &gt; /dev/null 2&gt; /tmp/error
</pre></div>
</td></tr></table></div>
<p>　結果は掲載しませんが、これはうまくいきます。
ただ、こうやって全体を見渡すとごちゃごちゃしていますし、
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> のために通したパスが他の設定にも影響します。
筆者はあまり良い方向に行っているとは思えません。</p>
<p>　ついでに書いた <tt class="docutils literal"><span class="pre">MAILTO=&quot;&quot;</span></tt> は、
cronがログのメールを送ってくるのを防ぐための記述です。</p>
</div>
<div class="section" id="id5">
<h3>24.3.4. ラッパーのシェルスクリプトを使う<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　ここでシェルスクリプトの出番です。
環境変数やその他を全てシェルスクリプトの中に押し込んでしまいます。
ラッパーのシェルスクリプトは、
ホーム下に <tt class="docutils literal"><span class="pre">batch</span></tt> というディレクトリを掘って、
そこに置く事にします。
リスト12に、例をお見せします。
これは、Macを閉じてしまうとツイートできないのを逆手にとって、
夜にMacを開いていたら自虐ツイートする仕組みです。</p>
<ul class="simple">
<li>リスト12: cronから呼び出すシェルスクリプトと設定</li>
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:batch ueda<span class="nv">$ </span>cat nightwork
<span class="c">#!/bin/bash -xv</span>

<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:/Users/ueda/bin:<span class="nv">$PATH</span>
<span class="nv">LANG</span><span class="o">=</span>ja_JP.UTF-8

<span class="nb">exec </span>2&gt; /tmp/stderr.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>
<span class="nb">exec</span> &gt; /tmp/stdout.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span>

usptomo-tweet <span class="s1">&#39;[自動ツイート]上田さん、こんな時間になってもまだPC開いて仕事をしてるんだって〜。キャハハダッサイ！&#39;</span>

// 実行できるようにしましょう
uedamac:batch ueda<span class="nv">$ </span>chmod +x nightwork
// crontabは次のようにセット
uedamac:batch ueda<span class="nv">$ </span>crontab -l
<span class="nv">MAILTO</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
30 23 * * * /Users/ueda/batch/nightwork
</pre></div>
</td></tr></table></div>
<p>PATHには、 <tt class="docutils literal"><span class="pre">nkf</span></tt> のある <tt class="docutils literal"><span class="pre">/usr/local/bin</span></tt> と、
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> のある <tt class="docutils literal"><span class="pre">/Users/ueda/bin</span></tt> を指定します。
また、 <tt class="docutils literal"><span class="pre">exec</span> <span class="pre">2&gt;</span></tt> でこのシェルスクリプトの標準エラー出力、
<tt class="docutils literal"><span class="pre">exec</span> <span class="pre">&gt;</span></tt> で標準出力をリダイレクトしてファイルに残しておきます。
<tt class="docutils literal"><span class="pre">basename</span> <span class="pre">$0</span></tt> は、このシェルスクリプトの名前（ <tt class="docutils literal"><span class="pre">nightwork</span></tt> ）
になります。</p>
<p>　図2のようにちゃんと送信されました・・・。</p>
<ul class="simple">
<li>図2: 送信の確認</li>
</ul>
<div class="figure">
<a class="reference internal image-reference" href="tweet2.png"><img alt="" src="tweet2.png" style="width: 50%;" /></a>
</div>
<p>　悲しいですね。もう寝ることにします。</p>
</div>
</div>
<div class="section" id="id6">
<h2>24.4. おわりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回はcronとシェルスクリプトと組み合わせて、
自動自虐ツイートを行う自動送信機能を MacBook Air
に組み込みました。
シェルスクリプトという点では、
最後の最後にちょっと出てきただけでしたが、
PATHの明示的な指定など、
これまでの連載で説明できなかったことを扱えました。
最後に作った <tt class="docutils literal"><span class="pre">nightwork</span></tt>
を拡張していくと、例えばブログの記事を紹介したり、
リストからmongonをランダムに選んでつぶやく
ボットを作ったりすることができます。
ぜひ試していただければ。</p>
<p>　冒頭でお伝えした通り、
開眼シェルスクリプトは今回で最終回です。
ご愛読、ありがとうございました。</p>
</div>
</div>
