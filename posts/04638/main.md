# 開眼シェルスクリプト2013年12月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="cron-crontab"><br />
<h1>24. 開眼シェルスクリプト 第24回 cron/crontabとシェルスクリプトを組み合わせる<a class="headerlink" href="#cron-crontab" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<p>　皆様、定時出勤、定時退社してますか？<br />
などと最初から挑発ともとれるような発言で炎上しそうですが、<br />
今回の開眼シェルスクリプトは定時に何かをマシンにさせるcron、<br />
具体的にはcrontabの使い方を扱います。<br />
どうか、右手にお持ちの日本刀を鞘に戻してください。</p><br />
<p>　cronは、実行したい日時を指定しておけば、<br />
プログラムを自動実行してくれる仕組みです。<br />
Macを含むUNIX系のOSでは、ほとんどの場合、<br />
最初から動いており、<br />
<tt class="docutils literal"><span class="pre">crontab</span></tt> というコマンドを使って、<br />
定期的に動作させたいプログラムを指定するだけで<br />
プログラムが動くようになっています。</p><br />
<p>　本連載では2012年の10月号で使った例があります。<br />
このときはさらっと説明しましたが、<br />
cronには少し癖みたいなものがあるので、<br />
落とし穴に嵌るとなかなか思うようになりません。<br />
この癖は、シェルスクリプトを間に挟む事で緩和できます。<br />
今回はほんのさわりだけですが、基本的な方法を示します。</p><br />
<p>　ところで、定期実行というと、昔、<br />
カントというオッサンがいて、あまりに時間に忠実で、<br />
カントが散歩で家の前を通る時刻に<br />
合わせて家の人が時計を合わせたなどという逸話が残ってます。<br />
cronも、それくらいは正確です（当たり前）。<br />
ついでにこのオッサンの言い放ったことを書いておきます。</p><br />
<blockquote><br />
<div>我が行いを見習えと、誰にでも言い得るよう行為せよ。<br />
&#8212; イマヌエル・カント</div></blockquote><br />
<p>先生、無理です。</p><br />
<p>　ところで、話が逸れたついでに報告しますと、<br />
本連載は今回で終了です。当初、ネタが地味なだけに<br />
6回連載して様子を見るという話でしたが、<br />
シェルスクリプト=UNIXという筆者の勝手な拡大政策によって<br />
気づけば今回で24回目です。<br />
現在の風潮である、<br />
みんなで一生懸命に莫迦でかいブラックボックスの使い方を勉強し、<br />
みんなで愛と情熱を以てブラックボックスの<br />
バージョンアップ地獄をフォローしていくという、<br />
おおよそ工学的アプローチとは思えない騒ぎからのコペルニクス的転回を狙い、<br />
今後も寒風の中裸一貫、地味にシェルスクリプト活動をしていく所存です。<br />
あ、コペルニクス的転回も、カントの言った事です。<br />
うまくまとまりました。</p><br />
<div class="section" id="croncrondcrontab"><br />
<h2>24.1. cronとcrondとcrontabの関係<a class="headerlink" href="#croncrondcrontab" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、まず用語の整理から。<br />
自分でインストールしなくても、だいたいの環境においては<br />
cronという仕組みが動いています。<br />
cronは仕組みの名前であって、実際には、<br />
<tt class="docutils literal"><span class="pre">crond</span></tt> というサービスが最初から後ろで動いています。<br />
crondというのは、cronのデーモンという意味ですね。<br />
ただ、どの環境でもcrondの名前が <tt class="docutils literal"><span class="pre">crond</span></tt><br />
であるとは限らず、リスト1のように <tt class="docutils literal"><span class="pre">cron</span></tt><br />
になっていたりします。ややこしや。</p><br />
<ul class="simple"><br />
<li>リスト1: 環境によって <tt class="docutils literal"><span class="pre">crond</span></tt> が動いていたり、 <tt class="docutils literal"><span class="pre">cron</span></tt> が動いていたり。</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5<br />
6</pre></div></td><td class="code"><div class="highlight"><pre><span class="o">[</span>ueda\@CentOS ~<span class="o">]</span><span class="nv">$ </span>ps aux | grep cron | grep -v grep<br />
root 1397 0.0 0.0 20408 452 ? Ss Feb04 7:25 crond<br />
uedamac:OSX ueda<span class="nv">$ </span>ps aux | grep cron | grep -v grep<br />
root 10058 0.0 0.0 2432784 156 ?? Ss 日03PM 0:00.39 /usr/sbin/cron<br />
ueda\@Ubuntu:~<span class="nv">$ </span>ps aux | grep cron | grep -v grep<br />
root 748 0.0 0.0 19112 848 ? Ss Sep18 0:01 cron<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　 <tt class="docutils literal"><span class="pre">crontab</span></tt> は、cronで定期実行するプログラムを確認したり、<br />
設定したりするためのコマンドです。<br />
<tt class="docutils literal"><span class="pre">crontab</span></tt> で設定した内容はどこかにファイルで保存されているのですが、<br />
このコマンドを通している限りはどこにあるか気にしなくて構いません。<br />
あるユーザで <tt class="docutils literal"><span class="pre">crontab</span></tt> を呼び出し、<br />
実行内容を書き込むと、その実行内容は、<br />
そのユーザで動作します。<br />
そして <tt class="docutils literal"><span class="pre">crontab</span></tt> に書いた自動実行のリストは、<br />
<tt class="docutils literal"><span class="pre">crond</span></tt> を再起動しなくてもすぐに有効になります。<br />
いつもcronを使っているような人でも、<br />
<tt class="docutils literal"><span class="pre">crond</span></tt> を再起動したという経験は少ないかと思います。<br />
筆者もありません。</p><br />
</div><br />
<div class="section" id="crontab"><br />
<h2>24.2. crontabの使い方<a class="headerlink" href="#crontab" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p><tt class="docutils literal"><span class="pre">crontab</span></tt> の使い方ですが、まずは設定内容の編集方法から説明します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>crontab -e<br />
</pre></div><br />
</div><br />
<p>と打つと、エディタ（ViかVim）が立ち上がります。<br />
（Macの場合は注意があるので後述します。）</p><br />
<p>例えばここに次のように打ってみましょう。<br />
（脚注：Viが使えないと苦労しますが、<br />
その場合は <tt class="docutils literal"><span class="pre">vimtutor</span></tt> という練習用コマンドがありますので、<br />
まずはそっちを練習しましょう。）</p><br />
<div class="highlight-bash"><div class="highlight"><pre>* * * * * touch /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>これで普通のViの操作で保存して終了します。<br />
ちゃんと登録されているかどうかは、<br />
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-l</span></tt> で確認できます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>crontab -l<br />
* * * * * touch /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>1分くらい待って <tt class="docutils literal"><span class="pre">/tmp/aaaa</span></tt><br />
ができたらうまくcronが働いています。<br />
さらに、1分ごとに <tt class="docutils literal"><span class="pre">ls</span></tt> を打ってみると、<br />
タイムスタンプが変化している様子が分かります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>ls -l /tmp/aaaa<br />
-rw-r--r-- 1 ueda wheel 0 9 22 16:24 /tmp/aaaa<br />
uedamac:~ ueda<span class="nv">$ </span>ls -l /tmp/aaaa<br />
-rw-r--r-- 1 ueda wheel 0 9 22 16:25 /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>なぜそうなるかは後から説明しますが、<br />
cronが1分ごとに <tt class="docutils literal"><span class="pre">touch</span></tt><br />
を起動して <tt class="docutils literal"><span class="pre">/tmp/aaaa</span></tt> のタイムスタンプを更新しているからです。</p><br />
<p>　今度は設定を消してみます。<br />
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt> で編集してもよいのですが、<br />
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> とやると、設定が全部消えます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>crontab -r<br />
uedamac:~ ueda<span class="nv">$ </span>crontab -l<br />
crontab: no crontab <span class="k">for </span>ueda<br />
</pre></div><br />
</div><br />
<p>これは「 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> で消しましょう」と言うよりは、<br />
「 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> を押すと大変な事になるぞ！」<br />
という注意の意味で紹介しました。</p><br />
<div class="section" id="id1"><br />
<h3>24.2.1. ファイルでcrontabの内容を管理<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて、 <tt class="docutils literal"><span class="pre">crontab</span></tt> はMacでも使えますが、<br />
<tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-e</span></tt> で編集した内容が反映されないという現象が発生します。<br />
どうもVimと相性が悪いようです。<br />
（脚注：<a class="reference external" href="http://d.hatena.ne.jp/yuyarin/20100225/1267084794">http://d.hatena.ne.jp/yuyarin/20100225/1267084794</a> や<br />
<a class="reference external" href="http://d.hatena.ne.jp/shunsuk/20120122/1327239513">http://d.hatena.ne.jp/shunsuk/20120122/1327239513</a><br />
等で調査しました。）<br />
Vimの設定ファイルをいじると解決するようですが、<br />
ここではもうちょっと確実な方法を示しておきます。</p><br />
<p>　まず、名前はなんでもよいので、<br />
以下のようなファイルを自分で作ります。<br />
筆者はホームの下に <tt class="docutils literal"><span class="pre">etc</span></tt> を掘ってその下に、<br />
<tt class="docutils literal"><span class="pre">crontab.conf</span></tt> という名前で作りました。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>cat crontab.conf<br />
* * * * * touch /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>　次に、 <tt class="docutils literal"><span class="pre">crontab</span></tt> にこのファイルを読み込ませます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab crontab.conf<br />
</pre></div><br />
</div><br />
<p><tt class="docutils literal"><span class="pre">-l</span></tt> オプションで確認しましょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l<br />
* * * * * touch /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>こうやれば、 <tt class="docutils literal"><span class="pre">crontab</span></tt><br />
からViを呼び出したときに起こる不具合とは無縁です。<br />
また、設定してやらなくても好きなエディタを使えます。</p><br />
<p>　また、これを応用すると、リスト2のような事もできます。</p><br />
<ul class="simple"><br />
<li>リスト2: crontabでリストを出し入れ</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre><span class="c"># crontabの内容を書き出す</span><br />
uedamac:etc ueda<span class="nv">$ </span>crontab -l &gt; hoge<br />
<span class="c"># crontabに書き出した内容を戻す</span><br />
uedamac:etc ueda<span class="nv">$ </span>crontab hoge<br />
</pre></div><br />
</td></tr></table></div><br />
<p>この例は同じ物を書き出したり読み出したりしているだけで全く意味がないのですが、<br />
別のサーバや別のユーザに、<br />
cronの設定を簡単に移す事ができます。<br />
そして、 <tt class="docutils literal"><span class="pre">crontab</span> <span class="pre">-r</span></tt> をやらかしても、<br />
またファイルを読ませれば復旧できます。</p><br />
<p>　ただし、この方法には欠点が一つあって、<br />
<tt class="docutils literal"><span class="pre">crontab.conf</span></tt> を書いて満足してしまい、<br />
読み込ませることを忘れがちになります。<br />
ご注意を。</p><br />
</div><br />
<div class="section" id="id2"><br />
<h3>24.2.2. コマンドの前の記号の意味<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて、次に時刻の指定の方法を説明します。<br />
書式のマニュアルは <tt class="docutils literal"><span class="pre">man</span> <span class="pre">5</span> <span class="pre">crontab</span></tt> で調べることができますので、<br />
ここでは最小限の説明をします。</p><br />
<p>　先ほど <tt class="docutils literal"><span class="pre">crontab</span></tt> で指定した</p><br />
<div class="highlight-bash"><div class="highlight"><pre>* * * * * touch /tmp/aaaa<br />
</pre></div><br />
</div><br />
<p>ですが、この <tt class="docutils literal"><span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></tt> の部分が時刻の指定部分です。<br />
順番に、分・時・日・月・曜日の指定で、<br />
<tt class="docutils literal"><span class="pre">*</span></tt> はそれぞれ毎分、毎時、毎日・・・ということになります。<br />
つまりはワイルドカードです。<br />
上の例では、毎分、 <tt class="docutils literal"><span class="pre">touch</span> <span class="pre">/tmp/aaaa</span></tt> を行うという意味になります。<br />
最小単位が分なので、最小の周期は1分ということになります。</p><br />
<p>　時刻の指定の例を一気に示します。<br />
例えば、(1)毎時5分に実行したい、(2)5分ごとに実行したい、<br />
(3)毎時15分と30分に実行したい、(4)月曜日の14時〜20時まで、<br />
毎時30分に実行したい、というのを上から順に示すと、<br />
リスト3のようになります。曜日の数字は、日曜から土曜まで、<br />
0から6で指定します。日曜は7と書いてもOKです。<br />
結局、次の点を押さえて慣れるということです。</p><br />
<ul class="simple"><br />
<li>リスト3: crontabの書き方あれこれ</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l<br />
5 * * * * touch /tmp/aaaa<br />
*/5 * * * * touch /tmp/bbbb<br />
15,30 * * * * touch /tmp/cccc<br />
30 14-20 * * 1 touch /tmp/dddd<br />
</pre></div><br />
</td></tr></table></div><br />
<ul class="simple"><br />
<li>スラッシュの後ろに数字を書くと、その数字の周期で実行</li><br />
<li>カンマで数字を並べると、その数字に該当する時に実行</li><br />
<li>ハイフンで数字をつなぐと、その範囲内で毎回実行</li><br />
</ul><br />
<p>ハイフンについては、n-mと書いたら、nとmも含まれます。<br />
また、ハイフンとスラッシュの併用もできます。<br />
あとのことは、使いながら解説します。</p><br />
</div><br />
</div><br />
<div class="section" id="twittercron"><br />
<h2>24.3. Twitterへの自動ツイートにcronを使う<a class="headerlink" href="#twittercron" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　さて、cronを使って何か作ってみましょう。<br />
今回もMacで試します。リスト4に環境を示します。</p><br />
<ul class="simple"><br />
<li>リスト4: 実験環境</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>uname -a<br />
Darwin uedamac.local 12.5.0 Darwin Kernel Version 12.5.0: Mon Jul 29 16:33:49 PDT 2013; root:xnu-2050.48.11~1/RELEASE_X86_64 x86_64<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　それで、cronを使って何をしようかといろいろ考えたのですが、<br />
今回はTwitterで自動ツイートを行うプログラムをしましょう。<br />
と言っても一からシェルスクリプトでbotを作ると大変なので、<br />
出来合いのコマンドを使います。<br />
また、筆者が試した環境は OS X Server ではなく、<br />
MacBook Air なので、<br />
サスペンド状態だったりネットワークに接続されていなかったりすると、<br />
ツイートできません。<br />
ただ、今回の内容を他のUNIX環境に移植するのは簡単です。</p><br />
<div class="section" id="id3"><br />
<h3>24.3.1. ツイートコマンドの準備<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p><a class="reference external" href="https://github.com/ryuichiueda/TomoTool/blob/master/Twitter/usptomo-tweet">https://github.com/ryuichiueda/TomoTool/blob/master/Twitter/usptomo-tweet</a><br />
に、筆者が作ったつぶやきコマンド（シェルスクリプト）<br />
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> をダウンロードします。<br />
ダウンロードの方法がわからなかったら、<br />
画面をコピペして <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> ファイルに保存して、</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="nv">$ </span>chmod +x usptomo-tweet<br />
</pre></div><br />
</div><br />
<p>としてください。コマンド名が長いので、<br />
別に <tt class="docutils literal"><span class="pre">tw</span></tt> と変更しても構いません。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> 内部ではいろいろなコマンドを使っています。<br />
ほとんど標準的なものですが、<br />
<tt class="docutils literal"><span class="pre">nkf,</span> <span class="pre">curl,</span> <span class="pre">openssl</span></tt> コマンドあたりは<br />
インストールされているか確認ください。<br />
所詮書きなぐりのシェルスクリプトなので、<br />
何か動かなかったら自分でログみて直すくらいの気持ちでお願いします。</p><br />
<p>　次に、鍵やトークンというものの設定を行います。<br />
<a class="reference external" href="https://dev.twitter.com">https://dev.twitter.com</a> に行って、<br />
ツイートしたいアカウントでログインします。<br />
ログインしたら「My applications」の画面、<br />
「Create an application」の画面に進み、<br />
必要事項を入力してください。<br />
アプリケーション名は何でも大丈夫です。<br />
必要事項の入力後、登録のボタンを押すと、<br />
「Consumer key、Consumer secret、<br />
Access token、Access token secret」が取得できます。<br />
普通に取得すると、Consumer keyもAccess tokenも、「Read only」<br />
になっているはずです。画面の指示に従って「Read and write」<br />
というアクセスレベルで再取得してください。<br />
ここら辺、ややこしいのですが、<br />
説明し出すと長くなってしまうので、<br />
うまくWeb上で方法を見つけながらやってみてください。</p><br />
<p>　取得できたら、リスト5のようなファイルをホームの下に置きます。<br />
これは <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> に読み込ませるシェルスクリプトの一部なので、<br />
シェルスクリプトの文法で書き、ファイル名も間違えないようにします。<br />
もしホーム下に置くのがいやだったら、<br />
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> の中を書き換えます。</p><br />
<ul class="simple"><br />
<li>リスト5: キーとトークンを書いたファイル</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4<br />
5</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>cat twitter.key<br />
<span class="nv">CONSUMER_KEY</span><span class="o">=</span><span class="s2">&quot;aaaaaaaaaaaaaaaaaaaaaa&quot;</span><br />
<span class="nv">CONSUMER_SECRET</span><span class="o">=</span><span class="s2">&quot;bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb&quot;</span><br />
<span class="nv">ACCESS_TOKEN</span><span class="o">=</span><span class="s2">&quot;000000000-cccccccccccccccccccccccccccccccccccccccc&quot;</span><br />
<span class="nv">ACCESS_TOKEN_SECRET</span><span class="o">=</span><span class="s2">&quot;ddddddddddddddddddddddddddddddddddddddddddd&quot;</span><br />
</pre></div><br />
</td></tr></table></div><br />
</div><br />
<div class="section" id="id4"><br />
<h3>24.3.2. ツイートしてみる<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　これで準備OKです。テストしてみましょう。<br />
リスト6のように打ってみます。</p><br />
<ul class="simple"><br />
<li>リスト6: 端末からテストツイート</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:~ ueda<span class="nv">$ </span>./bin/usptomo-tweet <span class="s1">&#39;test: 東東東南南南西西西北北北白白&#39;</span><br />
</pre></div><br />
</td></tr></table></div><br />
<p>投稿がうまくいけば、図1のようにネット上にツイートが放出されます。</p><br />
<ul class="simple"><br />
<li>図1: 投稿される</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="tweet.png"><img alt="" src="tweet.png" style="width: 50%;" /></a><br />
</div><br />
</div><br />
<div class="section" id="cron"><br />
<h3>24.3.3. cronから使う（環境変数に気をつけて）<a class="headerlink" href="#cron" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　さて、cronと <tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> を組み合わせて使ってみましょう。<br />
とは言うものの、<br />
cron には慣れていても慣れていなくてもいろいろな落とし穴があって、<br />
なかなか一発でうまくいきません。<br />
粘り強くいきましょう。<br />
ここでは一つだけ、よく起こるミスを、<br />
デバッグしながら紹介します。</p><br />
<p>　まず、リスト7のように仕掛けてみましょう。<br />
時刻は直近のものに合わせます。<br />
数分余裕を持って仕掛けるようにと書いてあるサイトがありますが、<br />
おそらく余裕を持たせなくても大丈夫な環境がほとんどだと考えます。</p><br />
<ul class="simple"><br />
<li>リスト7: crontabにコマンドを直接書き込む</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l<br />
21 21 * * * /Users/ueda/bin/usptomo-tweet <span class="s1">&#39;test: びろーん&#39;</span> &gt; /dev/null 2&gt; /tmp/error<br />
</pre></div><br />
</td></tr></table></div><br />
<p>時刻がきたら、 <tt class="docutils literal"><span class="pre">/tmp/error</span></tt> を見てみましょう。<br />
環境にもよりますが、筆者のMacではリスト8のように失敗しました。</p><br />
<ul class="simple"><br />
<li>リスト8: nkfが見つからないエラーが発生</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>less /tmp/error<br />
（略）<br />
/Users/ueda/bin/usptomo-tweet: line 33: nkf: <span class="nb">command </span>not found<br />
（略）<br />
</pre></div><br />
</td></tr></table></div><br />
<p>あれ？ <tt class="docutils literal"><span class="pre">nkf</span></tt> がインストールされていないのかな？<br />
というところですが、<br />
先ほど端末から試したときにはうまくいっていたので、<br />
ここはパス（環境変数 <tt class="docutils literal"><span class="pre">PATH</span></tt> ）を疑います。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">crontab</span></tt> でリスト9のように仕掛けます。<br />
ついでに <tt class="docutils literal"><span class="pre">LANG</span></tt> も調べてみましょう。</p><br />
<ul class="simple"><br />
<li>リスト9: echoでcronで設定されている環境変数を調べる</li><br />
</ul><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l<br />
23 10 * * * <span class="nb">echo</span> <span class="s2">&quot;$PATH&quot;</span> &gt; /tmp/path<br />
23 10 * * * <span class="nb">echo</span> <span class="s2">&quot;$LANG&quot;</span> &gt; /tmp/lang<br />
</pre></div><br />
</div><br />
<p>時刻が来たら <tt class="docutils literal"><span class="pre">/tmp/path</span></tt> を見てみると、<br />
リスト10のようになっていました。</p><br />
<ul class="simple"><br />
<li>リスト10: 環境変数の調査結果</li><br />
</ul><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>cat /tmp/path<br />
/usr/bin:/bin<br />
uedamac:etc ueda<span class="nv">$ </span>cat /tmp/lang<br />
<br />
（LANGには何も入っていない）<br />
</pre></div><br />
</div><br />
<p><tt class="docutils literal"><span class="pre">nkf</span></tt> の場所は次のように <tt class="docutils literal"><span class="pre">/usr/local/bin/</span></tt><br />
なので、 <tt class="docutils literal"><span class="pre">nkf</span></tt> が見つからずエラーが起きたようです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>which nkf<br />
/usr/local/bin/nkf<br />
</pre></div><br />
</div><br />
<p>　cronで何かを動かそうとしてうまくいかない場合、<br />
大抵はパスが間違っているか、<br />
今の例のように環境変数が端末で使っている<br />
ものと違うという問題に突き当たります。</p><br />
<p>　さて、原因が分かったので対策を。<br />
まず、リスト11のようにcrontabに環境変数を設定する方法があります。</p><br />
<ul class="simple"><br />
<li>リスト11: 環境変数をcrontabで指定する方法</li><br />
</ul><br />
<div class="highlight-bash"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1<br />
2<br />
3<br />
4</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:etc ueda<span class="nv">$ </span>crontab -l<br />
<span class="nv">PATH</span><span class="o">=</span>/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin<br />
<span class="nv">MAILTO</span><span class="o">=</span><span class="s2">&quot;&quot;</span><br />
35 10 * * * /Users/ueda/bin/usptomo-tweet <span class="s1">&#39;test: びろーんぐ&#39;</span> &gt; /dev/null 2&gt; /tmp/error<br />
</pre></div><br />
</td></tr></table></div><br />
<p>　結果は掲載しませんが、これはうまくいきます。<br />
ただ、こうやって全体を見渡すとごちゃごちゃしていますし、<br />
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> のために通したパスが他の設定にも影響します。<br />
筆者はあまり良い方向に行っているとは思えません。</p><br />
<p>　ついでに書いた <tt class="docutils literal"><span class="pre">MAILTO=&quot;&quot;</span></tt> は、<br />
cronがログのメールを送ってくるのを防ぐための記述です。</p><br />
</div><br />
<div class="section" id="id5"><br />
<h3>24.3.4. ラッパーのシェルスクリプトを使う<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　ここでシェルスクリプトの出番です。<br />
環境変数やその他を全てシェルスクリプトの中に押し込んでしまいます。<br />
ラッパーのシェルスクリプトは、<br />
ホーム下に <tt class="docutils literal"><span class="pre">batch</span></tt> というディレクトリを掘って、<br />
そこに置く事にします。<br />
リスト12に、例をお見せします。<br />
これは、Macを閉じてしまうとツイートできないのを逆手にとって、<br />
夜にMacを開いていたら自虐ツイートする仕組みです。</p><br />
<ul class="simple"><br />
<li>リスト12: cronから呼び出すシェルスクリプトと設定</li><br />
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
17</pre></div></td><td class="code"><div class="highlight"><pre>uedamac:batch ueda<span class="nv">$ </span>cat nightwork<br />
<span class="c">#!/bin/bash -xv</span><br />
<br />
<span class="nv">PATH</span><span class="o">=</span>/usr/local/bin:/Users/ueda/bin:<span class="nv">$PATH</span><br />
<span class="nv">LANG</span><span class="o">=</span>ja_JP.UTF-8<br />
<br />
<span class="nb">exec </span>2&gt; /tmp/stderr.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span><br />
<span class="nb">exec</span> &gt; /tmp/stdout.<span class="k">$(</span>basename <span class="nv">$0</span><span class="k">)</span><br />
<br />
usptomo-tweet <span class="s1">&#39;[自動ツイート]上田さん、こんな時間になってもまだPC開いて仕事をしてるんだって〜。キャハハダッサイ！&#39;</span><br />
<br />
// 実行できるようにしましょう<br />
uedamac:batch ueda<span class="nv">$ </span>chmod +x nightwork<br />
// crontabは次のようにセット<br />
uedamac:batch ueda<span class="nv">$ </span>crontab -l<br />
<span class="nv">MAILTO</span><span class="o">=</span><span class="s2">&quot;&quot;</span><br />
30 23 * * * /Users/ueda/batch/nightwork<br />
</pre></div><br />
</td></tr></table></div><br />
<p>PATHには、 <tt class="docutils literal"><span class="pre">nkf</span></tt> のある <tt class="docutils literal"><span class="pre">/usr/local/bin</span></tt> と、<br />
<tt class="docutils literal"><span class="pre">usptomo-tweet</span></tt> のある <tt class="docutils literal"><span class="pre">/Users/ueda/bin</span></tt> を指定します。<br />
また、 <tt class="docutils literal"><span class="pre">exec</span> <span class="pre">2&gt;</span></tt> でこのシェルスクリプトの標準エラー出力、<br />
<tt class="docutils literal"><span class="pre">exec</span> <span class="pre">&gt;</span></tt> で標準出力をリダイレクトしてファイルに残しておきます。<br />
<tt class="docutils literal"><span class="pre">basename</span> <span class="pre">$0</span></tt> は、このシェルスクリプトの名前（ <tt class="docutils literal"><span class="pre">nightwork</span></tt> ）<br />
になります。</p><br />
<p>　図2のようにちゃんと送信されました・・・。</p><br />
<ul class="simple"><br />
<li>図2: 送信の確認</li><br />
</ul><br />
<div class="figure"><br />
<a class="reference internal image-reference" href="tweet2.png"><img alt="" src="tweet2.png" style="width: 50%;" /></a><br />
</div><br />
<p>　悲しいですね。もう寝ることにします。</p><br />
</div><br />
</div><br />
<div class="section" id="id6"><br />
<h2>24.4. おわりに<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回はcronとシェルスクリプトと組み合わせて、<br />
自動自虐ツイートを行う自動送信機能を MacBook Air<br />
に組み込みました。<br />
シェルスクリプトという点では、<br />
最後の最後にちょっと出てきただけでしたが、<br />
PATHの明示的な指定など、<br />
これまでの連載で説明できなかったことを扱えました。<br />
最後に作った <tt class="docutils literal"><span class="pre">nightwork</span></tt><br />
を拡張していくと、例えばブログの記事を紹介したり、<br />
リストからmongonをランダムに選んでつぶやく<br />
ボットを作ったりすることができます。<br />
ぜひ試していただければ。</p><br />
<p>　冒頭でお伝えした通り、<br />
開眼シェルスクリプトは今回で最終回です。<br />
ご愛読、ありがとうございました。</p><br />
</div><br />
</div>
