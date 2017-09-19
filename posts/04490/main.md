---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年2月号
出典: 技術評論社SoftwareDesign

 <div class="section" id="id1">
<h1>2. 開眼シェルスクリプト 第2回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1>
<div class="section" id="id2">
<h2>2.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2>
<div class="section" id="awksed">
<h3>2.1.1. 使ってますか？awkとsed<a class="headerlink" href="#awksed" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　皆様、冷え性には辛い季節となりましたが、
寒さに負けず端末を叩いておられますでしょうか。
会社の隅、ドア近くに座っている筆者は、
コードを書いては誰かが開け放したドアを閉めるという毎日を送っております。
ドア用の close コマンドがないものか。</p>
<p>　今回、そして次回のお題は冷え性でもドアを閉めようということでもなく、
「ログを捌く」です。今回は、ログやその他テキストを端末で加工する際、
必ずと言っていいほど使う awk と sed の使い方を扱います。</p>
<p>　昔からの UNIX 使いの方には愚問になりますが、awk とsed、
ご存知でしょうか？イベントでたくさんの人と話していると、
若い人や UNIX 以外の OS で仕事をしてきた人の認識率はそんなに
高くないという印象を持っています。
自分もそうだったので、まあ、そういう状況です。</p>
</div>
<div class="section" id="unix">
<h3>2.1.2. UNIX を情報処理装置として使うために<a class="headerlink" href="#unix" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　筆者の場合は大学にいるときから Linux を使う機会は多く、
研究室のためにルータ作りやメールの管理に励んでいました。
が、実験データ等は excel を使うか、
Visual C++ でコードを書いて処理していました。</p>
<p>　この原因は間違いなく awk を端末で使う方法を知らなかったからです。
もし知っていたらそんな面倒なことをする必要は無かったのです。
excel はともかくコードを書くことは楽しかったのですが、
同時に現在と同じく多忙だったので、知っていたら楽だったのですが・・・。</p>
<p>　もし Linux や BSD などのイメージを問われて、
「無料のサーバ用OS」と真っ先に答える人には今回の内容は非常に有用です。
そのOSは、実は「強力で簡単な情報処理マシン」なので、
ぜひともサーバ用途に加えてそのように使っていただきたい。
awk や sed を覚えるのは、その準備です。
（脚注：perl でも一行野郎ができれば可。）</p>
</div>
<div class="section" id="id3">
<h3>2.1.3. 今回の気構え<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　今回も、お題に入る前に格言めいたものを記し、
読むときに何を意識するかの指針にしたいと思います。
今回は、The Art of UNIX Programming
（脚注: Eric S.Raymond (著), 長尾 高弘 (翻訳): The Art of UNIX Programming, アスキー, 2007.)
から、以下を引用したいと思います。</p>
<ul class="simple">
<li>他に方法がないことが実験により明らかである場合に限り、大きいプログラムを書け。</li>
<li>プログラマの時間は貴重である。プログラマの時間をコンピュータの時間より優先して節約せよ。</li>
</ul>
<p>要は、大げさなことをするなということです。
awk を知らなかった時の自分には耳の痛い話です。</p>
<p>　ところで、著者の Raymond は同書で awk を否定しているのですが・・・。</p>
</div>
</div>
<div class="section" id="id4">
<h2>2.2. 今回のお題：ログをさばく（前半戦）<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　それでは、早速使ってみましょう。
題材は Linux の secure ログ、apache の access_log ログです。
これらのログは、ある程度「人間臭いデータ」なので、
テキスト操作のお題の宝庫です。
次回も secure と access_log を使って、ログの整理シェルスクリプトを書きます。</p>
<p>　secure ログは自宅の CentOS6 のサーバから、
access_log は CentOS5.4 のウェブサーバから採取しました。
作業する環境（CentOS6 の入った ThinkPad x41）
のホーム下に「LOG」というディレクトリを作って、
以下のように放り込んであります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#CentOS6 は古いログに日付が入る。</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>ls
httpd/access_log secure
httpd/access_log.1 secure-20111030
httpd/access_log.2 secure-20111106
httpd/access_log.3 secure-20111113
httpd/access_log.4 secure-20111120
</pre></div>
</div>
<p>小ネタですが、scpを次のように使うとrootにならずにログがコピーでき、
ファイルのユーザも変更できます。
sshd の設定次第ではこの小技は使えませんので、
普通の方法でコピーしてください。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span>scp -r root\@localhost:/var/log ./
</pre></div>
</div>
<div class="section" id="id5">
<h3>2.2.1. awkとsedを使う取っ掛かりとコツ<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　sed、awkは共にスクリプト言語なので長いコードも書けますが、
この連載では処理を細かく切ってパイプでつないで使います。
そうすることで、パイプラインの各ステップで行うことが明確になり、
見通しの良いスクリプト（あるいは端末でのコマンドライン）
を書くことができます。</p>
<p>　sed と awk の使い方として、
最初は次の三つのテキスト操作を押さえておきましょう。
空手の型のように身につけてください。</p>
<ul class="simple">
<li>レコードの抽出</li>
<li>文字列の置換</li>
<li>フィールドの抽出と並び替え</li>
</ul>
<p>sedとawkの性質や誕生の経緯については、wikipediaに詳しいので割愛します。</p>
</div>
<div class="section" id="grep-awk">
<h3>2.2.2. レコードの抽出（grep の拡張版としての awk ）<a class="headerlink" href="#grep-awk" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　まずはレコードの抽出から。
　サンプルの secure ログには次のように sshd と su のログがあります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#レコードの後半は長いので省略</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 5 secure
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se
Nov 23 16:34:55 cent su: pam_unix<span class="o">(</span>su-l:auth<span class="o">)</span>: auth
Nov 23 16:34:59 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s
Nov 23 16:35:03 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: ses
</pre></div>
</div>
<p>これを sshd のものだけ、あるいは su のものだけ見たいとします。
grep を使ってもよいのですが、この際いつも問題になるのは、
関係ないところに sshd や su という文字列が混ざっているかもしれず、
きっちり抽出できない懸念があることです。</p>
<p>　awk を使えば、そのような心配なく su のレコードだけ抽出できます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$5==&quot;su:&quot;&#39;</span>
Nov 23 16:34:55 cent su: pam_unix<span class="o">(</span>su-l:auth<span class="o">)</span>: auth
Nov 23 16:34:59 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s
Nov 23 16:35:03 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: ses
</pre></div>
</div>
<p>awk &#8216;$5==&#8221;su:&#8221;&#8217;は、
「第5フィールドの文字列が『su:』の場合」抽出しろということです。
フィールドというのは、スペースで区切られた文字列のことで、
左から第1、第2、・・・と数えます。
このようにawkは、位置指定付きのgrepのように使えます。</p>
<p>　正規表現も使えます。sshdのレコードだけ見たければ、
例えば次のように打ちます。
スラッシュで囲まれた部分が正規表現で、第5フィールドに適用しています。
正規表現 <tt class="docutils literal"><span class="pre">sshd\\[[0-9]*\\]:</span></tt> は、</p>
<blockquote>
<div><tt class="docutils literal"><span class="pre">sshd[</span></tt> の次に数字が0個以上続き、その後 <tt class="docutils literal"><span class="pre">]:</span></tt> が来る文字列</div></blockquote>
<p>という意味になります。もう少し補足すると、
<tt class="docutils literal"><span class="pre">[0-9]</span></tt> は0から9のどれか一字という意味になります。
<tt class="docutils literal"><span class="pre">[</span></tt>, <tt class="docutils literal"><span class="pre">]</span></tt> は正規表現で使う記号なので、
<tt class="docutils literal"><span class="pre">[</span></tt>, <tt class="docutils literal"><span class="pre">]</span></tt> という文字そのものを書く時は\\記号でエスケープし、
<tt class="docutils literal"><span class="pre">\\[</span></tt> や <tt class="docutils literal"><span class="pre">\\]</span></tt> と記述します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$5~/sshd\\[[0-9]*\\]:/&#39;</span>
Nov 23 08:44:49 cent sshd<span class="o">[</span>32686<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: Accepted publick
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se
（以下略）
</pre></div>
</div>
<p>　さらに、文字列や数値の大小比較でレコードを抽出することも可能です。
次の例では、11月23日の8時13分40秒台のレコードを抽出しています。
2つあるうちの後ろのawkで、時刻を文字列として大小比較しています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#いろいろ攻撃されてますが、</span>
<span class="c">#鍵認証しか許可していないので大丈夫です。多分。</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$1==&quot;Nov&quot; &amp;&amp; $2==&quot;23&quot;&#39;</span> | awk <span class="s1">&#39;$3&gt;=&quot;08:13:40&quot; &amp;&amp; $3&lt;&quot;08:13:50&quot;&#39;</span>
Nov 23 08:13:40 cent sshd<span class="o">[</span>32578<span class="o">]</span>: Invalid user cro
Nov 23 08:13:40 cent sshd<span class="o">[</span>32579<span class="o">]</span>: Received disconn
（中略）
Nov 23 08:13:49 cent sshd<span class="o">[</span>32601<span class="o">]</span>: Received disconn
</pre></div>
</div>
<p>　awkでは文字列を&#8221;&#8220;で囲むと文字列扱い、囲まないと数値扱いになります。
入力されるテキストは比較対象や演算に合わせて扱いが変わります。
したがって、以下のように出力に違いが出ます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#9.9は数字88と比較されるので数字扱い。抽出されない。</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>9.9 | awk <span class="s1">&#39;$1&gt;88&#39;</span>
<span class="c">#9.9は文字列88と比較されるので文字列扱い。</span>
<span class="c">#辞書順で比較され、抽出される。</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>9.9 | awk <span class="s1">&#39;$1&gt;&quot;88&quot;&#39;</span>
9.9
</pre></div>
</div>
<p>以上がレコード抽出で最初に知っておけばよいことです。
awkをちょっと気の利いたgrepとして使ってみようという気になったら
後は自然に上達すると思います。</p>
</div>
<div class="section" id="id6">
<h3>2.2.3. 置換<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　次に文字列の置換をしてみましょう。
例えばsedを使ってNovを11に置換するには、次のように書きます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#置換前</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）
<span class="c">#置換後</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | sed <span class="s1">&#39;s/^Nov/11/&#39;</span>
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）
</pre></div>
</div>
<p>sedのオプション「s/^Nov/11/」は呪文めいてますが、左からsが「置換」、
スラッシュの前が置換対象の正規表現、スラッシュの後が置換後の文字列です。
一行に一回、この変換が適用されます。
もし一行で何回も置換したければ、最後のスラッシュの後に文字gを付けます。
正規表現「^Nov」は、行頭にあるNovという意味になります。
区切り文字は必ずしもスラッシュである必要はありません。
正規表現や置換後の文字列にスラッシュが含まれる場合は、
セミコロンなどを使います。あとからそのような例が出てきます。</p>
<p>　正規表現でマッチした文字列を再利用することもできます。
次の例のように、正規表現にマッチした文字列を&amp;で呼び出したり、
<tt class="docutils literal"><span class="pre">\\(</span> <span class="pre">\\)</span></tt> で範囲指定して <tt class="docutils literal"><span class="pre">\\1,\\2,\\3,...</span></tt> という記号で呼び出すことができます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1140003 | sed <span class="s1">&#39;s/.../〒&amp;-/&#39;</span>
〒114-0003
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>09012345678 | sed <span class="s1">&#39;s/^\\(...\\)\\(....\\)/tel:\\1-\\2-/&#39;</span>
tel:090-1234-5678
</pre></div>
</div>
<p>正規表現中の <tt class="docutils literal"><span class="pre">.</span></tt> は、任意の一字という意味です。
かな漢字も正しく一字と数えてくれますが、
LANGの指定によっては次のように動作が変わります。
この例では、LANG=C としてマルチバイト文字を意識しないようにすると、
「大」の先頭1バイトだけが削れてしまいます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#文字コードがUTF-8</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span>
ja_JP.UTF-8
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> 大岡山 | sed <span class="s1">&#39;s/^.//g&#39;</span>
岡山
<span class="c">#LANGをCとすると動作が変わる。</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> 大岡山 | <span class="nv">LANG</span><span class="o">=</span>C sed <span class="s1">&#39;s/^.//g&#39;</span>
��岡山
</pre></div>
</div>
<p>　awk を使っても置換ができます。
secure ログの Nov を11に置換するには次のように打ちます。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#置換の関数 gsub を使う</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | awk <span class="s1">&#39;{gsub(/Nov/,&quot;11&quot;,$1);print $0}&#39;</span>
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）
<span class="c">#条件文を使う</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | awk <span class="s1">&#39;{if($1==&quot;Nov&quot;){$1=&quot;11&quot;};print $0}&#39;</span>
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）
</pre></div>
</div>
<p>この場合、awkはレコード抽出ツールではなくて文字置換ツールになっています。
抽出以外のawkプログラムは、{}の中に書きます。
この例の上の方は、$1に自動に入った&#8221;Nov&#8221;をgsubという関数で操作しています。
gsubの三つの引数は、それぞれ正規表現、置換後の文字列、変数です。
下の方は、if文を使って$1を&#8221;11&#8221;に置き換えています。</p>
<p>　 <tt class="docutils literal"><span class="pre">print</span> <span class="pre">$0</span></tt> の$0は、レコード一行全体を表します。
awk の面白いところは、$1や$2を書き換えると$0も変わるところです。
<tt class="docutils literal"><span class="pre">print</span> <span class="pre">$0</span></tt> は、 <tt class="docutils literal"><span class="pre">print</span></tt> と省略できます。
この規則のおかげで、端末に書く文字が短くなります。
以下は例です。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#入力された全フィールドをそのまま出力する方法</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print $1,$2,$3}&#39;</span>
1 2 3
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print $0}&#39;</span>
1 2 3
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print}&#39;</span>
1 2 3
<span class="c">#フィールドの値の変更</span>
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{$2=&quot;二&quot;;print $0}&#39;</span>
1 二 3
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{$2=&quot;二&quot;;print}&#39;</span>
1 二 3
</pre></div>
</div>
<p>　{}に囲まれた部分は「アクション」と呼ばれます。
囲まれていない、抽出の部分は「パターン」と呼ばれます。
アクション内の各文はセミコロンで区切られ、左から右に処理が流れます。
C言語の影響が強いので、記号類の使い方はC言語に似ています。</p>
<p>　ところで先ほどからログの「Nov」を「11」に変換していますが、
他の月も変換するにはどうすればよいでしょうか。
sed や awk を12個つなげばできますが
（脚注：マルチコアの場合、12個つなぐと並列処理になるのでバカにしてはいけません。）、
awk や sed のスクリプトを用意することもできます。
月の変換では、次のMONTHファイルを準備して sed で使えばよいでしょう。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat MONTH
s/^Jan/01/
s/^Feb/02/
s/^Mar/03/
（以下略）
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>sed -f ./MONTH secure | tail -n 1
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: sess（略）
</pre></div>
</div>
</div>
<div class="section" id="id7">
<h3>2.2.4. フィールドの抽出と並び替え<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　あるフィールド$iの抽出をしたい場合は <tt class="docutils literal"><span class="pre">print</span> <span class="pre">$i</span></tt> と記述します。
次の例では、access_logから第4フィールドを抽出しています。
ただ、access_logの区切り文字は複雑なので、
この場合の第4フィールドは単に空白区切りで見たときの4番目のデータということになります。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head -n 1 httpd/access_log
114.80.93.71 - - <span class="o">[</span>20/Nov/2011:06:47:54 +0900<span class="o">]</span> <span class="s2">&quot;GET / HTTP/1.1&quot;</span> 200 1429 （略）
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span>
<span class="o">[</span>20/Nov/2011:06:47:54
（以下略）
</pre></div>
</div>
<p>並び替えは、並べたい順にフィールドを指定してprintを適用します。
例えば前の例に続けて、抽出した日付、時刻のデータを8桁の日付、
6桁の時刻で正規化するには次のように操作します。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span> | sed <span class="s1">&#39;s;[:/\\[]; ;g&#39;</span> | awk <span class="s1">&#39;{print $2,$1,$3,$4$5$6}&#39;</span> | sed -f ./MONTH | awk <span class="s1">&#39;{print $3$1$2,$4}&#39;</span>
20111120 064754
20111120 064805
（略）
</pre></div>
</div>
<p>長いので各段階でパイプを切って出力を観察しましょう。
file1 から file2 への変換では、sed で <tt class="docutils literal"><span class="pre">[,</span> <span class="pre">:,</span> <span class="pre">/</span></tt> を空白に変換しています。
正規表現にスラッシュが含まれるので、区切り文字にセミコロンを使っています。
file2 から file3 への変換では、
<tt class="docutils literal"><span class="pre">print</span></tt> を使って日付の年月日の並び替えと時分秒の間のスペースを除去しています。
この例では、 <tt class="docutils literal"><span class="pre">print</span></tt> する変数の間にカンマがあったりなかったりしますが、
カンマを入れると空白区切りで出力、カンマを入れないと連結して出力という意味になります。
カンマを入れずに連結する場合は、 <tt class="docutils literal"><span class="pre">$4</span> <span class="pre">$5</span> <span class="pre">$6</span></tt> と間に空白を入れても連結されます。
あとは月を数字表記に変えて、年月日を連結して目標の出力を得ています。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span> | head -n 1 &gt; file1
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file1
<span class="o">[</span>20/Nov/2011:06:47:54
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file1 | sed <span class="s1">&#39;s;[:/\\[]; ;g&#39;</span> &gt; file2
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file2
 20 Nov 2011 06 47 54
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file2 | awk <span class="s1">&#39;{print $2,$1,$3,$4$5$6}&#39;</span> &gt; file3
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file3
Nov 20 2011 064754
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file3 | sed -f ./MONTH &gt; file4
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file4
11 20 2011 064754
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file4 | awk <span class="s1">&#39;{print $3$1$2,$4}&#39;</span>
20111120 064754
</pre></div>
</div>
</div>
<div class="section" id="id8">
<h3>2.2.5. おまけ<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3>
<p>　awk については、他にも改行を取ったり、行をまたいで数値を集計したりと、
まだちょっと覚えなければならないことがありますが、
次回のログ処理で使うにはこの程度で十分です。
もうちょっと勉強したい人のために、文法的に凝ったコードを示します。
このコードは、西暦年の情報が入っていない secure に、
無理やり年を付加することを想定したものです。</p>
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#MMDDの4桁で月日を表現</span>
<span class="c">#3行目で年明け</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat hoge
1230
1231
0101
0102
<span class="c">#データをひっくり返し、年をまたいだら年を一つ減らす。</span>
<span class="c">#年を入れて8桁にしたら再びデータをひっくり返す。</span>
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tac hoge | awk <span class="s1">&#39;BEGIN{y=&#39;</span><span class="k">$(</span>date +%Y<span class="k">)</span><span class="s1">&#39;;md=&#39;</span><span class="k">$(</span>date +%m%d<span class="k">)</span><span class="s1">&#39;}{if(md&lt;$1){y--};md=$1;print y md}&#39;</span> | tac
20111230
20111231
20120101
20120102
</pre></div>
</div>
</div>
</div>
<div class="section" id="id9">
<h2>2.3. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2>
<p>　今回は、ログの加工を題材に awk と sed の使い方を説明しました。
今回は端末で awk, sed を使う話で、シェルスクリプトは書きませんでした。
sed で月の英語表記を数字表記に変換する sed スクリプトが一つ出てきました。</p>
<p>　今回行った端末での awk, sed の使い方は、空手の「型」のようなものです。
自在にテキストを加工するためには、
このような型を組み合わせて端末で使いこなすことが必要で、
少し慣れる必要があります。
また、端末という限られたスペースで必要な処理を行うことで、
きれいなシェルスクリプトを書くことができるようになります。
そこまで苦労して身につけるべきかというところですが、
あまり深く考えず、
grep の代わりに awk を使ってみてから考えてもらえれば幸いです。</p>
</div>
</div>


