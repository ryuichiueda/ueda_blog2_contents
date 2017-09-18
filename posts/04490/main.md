---
Copyright: (C) Ryuichi Ueda
---


# 開眼シェルスクリプト2012年2月号
出典: 技術評論社SoftwareDesign<br />
<br />
 <div class="section" id="id1"><br />
<h1>2. 開眼シェルスクリプト 第2回<a class="headerlink" href="#id1" title="このヘッドラインへのパーマリンク">¶</a></h1><br />
<div class="section" id="id2"><br />
<h2>2.1. はじめに<a class="headerlink" href="#id2" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<div class="section" id="awksed"><br />
<h3>2.1.1. 使ってますか？awkとsed<a class="headerlink" href="#awksed" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　皆様、冷え性には辛い季節となりましたが、<br />
寒さに負けず端末を叩いておられますでしょうか。<br />
会社の隅、ドア近くに座っている筆者は、<br />
コードを書いては誰かが開け放したドアを閉めるという毎日を送っております。<br />
ドア用の close コマンドがないものか。</p><br />
<p>　今回、そして次回のお題は冷え性でもドアを閉めようということでもなく、<br />
「ログを捌く」です。今回は、ログやその他テキストを端末で加工する際、<br />
必ずと言っていいほど使う awk と sed の使い方を扱います。</p><br />
<p>　昔からの UNIX 使いの方には愚問になりますが、awk とsed、<br />
ご存知でしょうか？イベントでたくさんの人と話していると、<br />
若い人や UNIX 以外の OS で仕事をしてきた人の認識率はそんなに<br />
高くないという印象を持っています。<br />
自分もそうだったので、まあ、そういう状況です。</p><br />
</div><br />
<div class="section" id="unix"><br />
<h3>2.1.2. UNIX を情報処理装置として使うために<a class="headerlink" href="#unix" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　筆者の場合は大学にいるときから Linux を使う機会は多く、<br />
研究室のためにルータ作りやメールの管理に励んでいました。<br />
が、実験データ等は excel を使うか、<br />
Visual C++ でコードを書いて処理していました。</p><br />
<p>　この原因は間違いなく awk を端末で使う方法を知らなかったからです。<br />
もし知っていたらそんな面倒なことをする必要は無かったのです。<br />
excel はともかくコードを書くことは楽しかったのですが、<br />
同時に現在と同じく多忙だったので、知っていたら楽だったのですが・・・。</p><br />
<p>　もし Linux や BSD などのイメージを問われて、<br />
「無料のサーバ用OS」と真っ先に答える人には今回の内容は非常に有用です。<br />
そのOSは、実は「強力で簡単な情報処理マシン」なので、<br />
ぜひともサーバ用途に加えてそのように使っていただきたい。<br />
awk や sed を覚えるのは、その準備です。<br />
（脚注：perl でも一行野郎ができれば可。）</p><br />
</div><br />
<div class="section" id="id3"><br />
<h3>2.1.3. 今回の気構え<a class="headerlink" href="#id3" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　今回も、お題に入る前に格言めいたものを記し、<br />
読むときに何を意識するかの指針にしたいと思います。<br />
今回は、The Art of UNIX Programming<br />
（脚注: Eric S.Raymond (著), 長尾 高弘 (翻訳): The Art of UNIX Programming, アスキー, 2007.)<br />
から、以下を引用したいと思います。</p><br />
<ul class="simple"><br />
<li>他に方法がないことが実験により明らかである場合に限り、大きいプログラムを書け。</li><br />
<li>プログラマの時間は貴重である。プログラマの時間をコンピュータの時間より優先して節約せよ。</li><br />
</ul><br />
<p>要は、大げさなことをするなということです。<br />
awk を知らなかった時の自分には耳の痛い話です。</p><br />
<p>　ところで、著者の Raymond は同書で awk を否定しているのですが・・・。</p><br />
</div><br />
</div><br />
<div class="section" id="id4"><br />
<h2>2.2. 今回のお題：ログをさばく（前半戦）<a class="headerlink" href="#id4" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　それでは、早速使ってみましょう。<br />
題材は Linux の secure ログ、apache の access_log ログです。<br />
これらのログは、ある程度「人間臭いデータ」なので、<br />
テキスト操作のお題の宝庫です。<br />
次回も secure と access_log を使って、ログの整理シェルスクリプトを書きます。</p><br />
<p>　secure ログは自宅の CentOS6 のサーバから、<br />
access_log は CentOS5.4 のウェブサーバから採取しました。<br />
作業する環境（CentOS6 の入った ThinkPad x41）<br />
のホーム下に「LOG」というディレクトリを作って、<br />
以下のように放り込んであります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#CentOS6 は古いログに日付が入る。</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>ls<br />
httpd/access_log secure<br />
httpd/access_log.1 secure-20111030<br />
httpd/access_log.2 secure-20111106<br />
httpd/access_log.3 secure-20111113<br />
httpd/access_log.4 secure-20111120<br />
</pre></div><br />
</div><br />
<p>小ネタですが、scpを次のように使うとrootにならずにログがコピーでき、<br />
ファイルのユーザも変更できます。<br />
sshd の設定次第ではこの小技は使えませんので、<br />
普通の方法でコピーしてください。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span>scp -r root\@localhost:/var/log ./<br />
</pre></div><br />
</div><br />
<div class="section" id="id5"><br />
<h3>2.2.1. awkとsedを使う取っ掛かりとコツ<a class="headerlink" href="#id5" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　sed、awkは共にスクリプト言語なので長いコードも書けますが、<br />
この連載では処理を細かく切ってパイプでつないで使います。<br />
そうすることで、パイプラインの各ステップで行うことが明確になり、<br />
見通しの良いスクリプト（あるいは端末でのコマンドライン）<br />
を書くことができます。</p><br />
<p>　sed と awk の使い方として、<br />
最初は次の三つのテキスト操作を押さえておきましょう。<br />
空手の型のように身につけてください。</p><br />
<ul class="simple"><br />
<li>レコードの抽出</li><br />
<li>文字列の置換</li><br />
<li>フィールドの抽出と並び替え</li><br />
</ul><br />
<p>sedとawkの性質や誕生の経緯については、wikipediaに詳しいので割愛します。</p><br />
</div><br />
<div class="section" id="grep-awk"><br />
<h3>2.2.2. レコードの抽出（grep の拡張版としての awk ）<a class="headerlink" href="#grep-awk" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　まずはレコードの抽出から。<br />
　サンプルの secure ログには次のように sshd と su のログがあります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#レコードの後半は長いので省略</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 5 secure<br />
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se<br />
Nov 23 16:34:55 cent su: pam_unix<span class="o">(</span>su-l:auth<span class="o">)</span>: auth<br />
Nov 23 16:34:59 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s<br />
Nov 23 16:35:03 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s<br />
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: ses<br />
</pre></div><br />
</div><br />
<p>これを sshd のものだけ、あるいは su のものだけ見たいとします。<br />
grep を使ってもよいのですが、この際いつも問題になるのは、<br />
関係ないところに sshd や su という文字列が混ざっているかもしれず、<br />
きっちり抽出できない懸念があることです。</p><br />
<p>　awk を使えば、そのような心配なく su のレコードだけ抽出できます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$5==&quot;su:&quot;&#39;</span><br />
Nov 23 16:34:55 cent su: pam_unix<span class="o">(</span>su-l:auth<span class="o">)</span>: auth<br />
Nov 23 16:34:59 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s<br />
Nov 23 16:35:03 cent su: pam_unix<span class="o">(</span>su-l:session<span class="o">)</span>: s<br />
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: ses<br />
</pre></div><br />
</div><br />
<p>awk &#8216;$5==&#8221;su:&#8221;&#8217;は、<br />
「第5フィールドの文字列が『su:』の場合」抽出しろということです。<br />
フィールドというのは、スペースで区切られた文字列のことで、<br />
左から第1、第2、・・・と数えます。<br />
このようにawkは、位置指定付きのgrepのように使えます。</p><br />
<p>　正規表現も使えます。sshdのレコードだけ見たければ、<br />
例えば次のように打ちます。<br />
スラッシュで囲まれた部分が正規表現で、第5フィールドに適用しています。<br />
正規表現 <tt class="docutils literal"><span class="pre">sshd\\[[0-9]*\\]:</span></tt> は、</p><br />
<blockquote><br />
<div><tt class="docutils literal"><span class="pre">sshd[</span></tt> の次に数字が0個以上続き、その後 <tt class="docutils literal"><span class="pre">]:</span></tt> が来る文字列</div></blockquote><br />
<p>という意味になります。もう少し補足すると、<br />
<tt class="docutils literal"><span class="pre">[0-9]</span></tt> は0から9のどれか一字という意味になります。<br />
<tt class="docutils literal"><span class="pre">[</span></tt>, <tt class="docutils literal"><span class="pre">]</span></tt> は正規表現で使う記号なので、<br />
<tt class="docutils literal"><span class="pre">[</span></tt>, <tt class="docutils literal"><span class="pre">]</span></tt> という文字そのものを書く時は\\記号でエスケープし、<br />
<tt class="docutils literal"><span class="pre">\\[</span></tt> や <tt class="docutils literal"><span class="pre">\\]</span></tt> と記述します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$5~/sshd\\[[0-9]*\\]:/&#39;</span><br />
Nov 23 08:44:49 cent sshd<span class="o">[</span>32686<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se<br />
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: Accepted publick<br />
Nov 23 08:56:13 cent sshd<span class="o">[</span>32743<span class="o">]</span>: pam_unix<span class="o">(</span>sshd:se<br />
（以下略）<br />
</pre></div><br />
</div><br />
<p>　さらに、文字列や数値の大小比較でレコードを抽出することも可能です。<br />
次の例では、11月23日の8時13分40秒台のレコードを抽出しています。<br />
2つあるうちの後ろのawkで、時刻を文字列として大小比較しています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#いろいろ攻撃されてますが、</span><br />
<span class="c">#鍵認証しか許可していないので大丈夫です。多分。</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat secure | awk <span class="s1">&#39;$1==&quot;Nov&quot; &amp;&amp; $2==&quot;23&quot;&#39;</span> | awk <span class="s1">&#39;$3&gt;=&quot;08:13:40&quot; &amp;&amp; $3&lt;&quot;08:13:50&quot;&#39;</span><br />
Nov 23 08:13:40 cent sshd<span class="o">[</span>32578<span class="o">]</span>: Invalid user cro<br />
Nov 23 08:13:40 cent sshd<span class="o">[</span>32579<span class="o">]</span>: Received disconn<br />
（中略）<br />
Nov 23 08:13:49 cent sshd<span class="o">[</span>32601<span class="o">]</span>: Received disconn<br />
</pre></div><br />
</div><br />
<p>　awkでは文字列を&#8221;&#8220;で囲むと文字列扱い、囲まないと数値扱いになります。<br />
入力されるテキストは比較対象や演算に合わせて扱いが変わります。<br />
したがって、以下のように出力に違いが出ます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#9.9は数字88と比較されるので数字扱い。抽出されない。</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>9.9 | awk <span class="s1">&#39;$1&gt;88&#39;</span><br />
<span class="c">#9.9は文字列88と比較されるので文字列扱い。</span><br />
<span class="c">#辞書順で比較され、抽出される。</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>9.9 | awk <span class="s1">&#39;$1&gt;&quot;88&quot;&#39;</span><br />
9.9<br />
</pre></div><br />
</div><br />
<p>以上がレコード抽出で最初に知っておけばよいことです。<br />
awkをちょっと気の利いたgrepとして使ってみようという気になったら<br />
後は自然に上達すると思います。</p><br />
</div><br />
<div class="section" id="id6"><br />
<h3>2.2.3. 置換<a class="headerlink" href="#id6" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　次に文字列の置換をしてみましょう。<br />
例えばsedを使ってNovを11に置換するには、次のように書きます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#置換前</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure<br />
Nov 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）<br />
<span class="c">#置換後</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | sed <span class="s1">&#39;s/^Nov/11/&#39;</span><br />
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）<br />
</pre></div><br />
</div><br />
<p>sedのオプション「s/^Nov/11/」は呪文めいてますが、左からsが「置換」、<br />
スラッシュの前が置換対象の正規表現、スラッシュの後が置換後の文字列です。<br />
一行に一回、この変換が適用されます。<br />
もし一行で何回も置換したければ、最後のスラッシュの後に文字gを付けます。<br />
正規表現「^Nov」は、行頭にあるNovという意味になります。<br />
区切り文字は必ずしもスラッシュである必要はありません。<br />
正規表現や置換後の文字列にスラッシュが含まれる場合は、<br />
セミコロンなどを使います。あとからそのような例が出てきます。</p><br />
<p>　正規表現でマッチした文字列を再利用することもできます。<br />
次の例のように、正規表現にマッチした文字列を&amp;で呼び出したり、<br />
<tt class="docutils literal"><span class="pre">\\(</span> <span class="pre">\\)</span></tt> で範囲指定して <tt class="docutils literal"><span class="pre">\\1,\\2,\\3,...</span></tt> という記号で呼び出すことができます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1140003 | sed <span class="s1">&#39;s/.../〒&amp;-/&#39;</span><br />
〒114-0003<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>09012345678 | sed <span class="s1">&#39;s/^\\(...\\)\\(....\\)/tel:\\1-\\2-/&#39;</span><br />
tel:090-1234-5678<br />
</pre></div><br />
</div><br />
<p>正規表現中の <tt class="docutils literal"><span class="pre">.</span></tt> は、任意の一字という意味です。<br />
かな漢字も正しく一字と数えてくれますが、<br />
LANGの指定によっては次のように動作が変わります。<br />
この例では、LANG=C としてマルチバイト文字を意識しないようにすると、<br />
「大」の先頭1バイトだけが削れてしまいます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#文字コードがUTF-8</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> <span class="nv">$LANG</span><br />
ja_JP.UTF-8<br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> 大岡山 | sed <span class="s1">&#39;s/^.//g&#39;</span><br />
岡山<br />
<span class="c">#LANGをCとすると動作が変わる。</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo</span> 大岡山 | <span class="nv">LANG</span><span class="o">=</span>C sed <span class="s1">&#39;s/^.//g&#39;</span><br />
��岡山<br />
</pre></div><br />
</div><br />
<p>　awk を使っても置換ができます。<br />
secure ログの Nov を11に置換するには次のように打ちます。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#置換の関数 gsub を使う</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | awk <span class="s1">&#39;{gsub(/Nov/,&quot;11&quot;,$1);print $0}&#39;</span><br />
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）<br />
<span class="c">#条件文を使う</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tail -n 1 secure | awk <span class="s1">&#39;{if($1==&quot;Nov&quot;){$1=&quot;11&quot;};print $0}&#39;</span><br />
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: session （略）<br />
</pre></div><br />
</div><br />
<p>この場合、awkはレコード抽出ツールではなくて文字置換ツールになっています。<br />
抽出以外のawkプログラムは、{}の中に書きます。<br />
この例の上の方は、$1に自動に入った&#8221;Nov&#8221;をgsubという関数で操作しています。<br />
gsubの三つの引数は、それぞれ正規表現、置換後の文字列、変数です。<br />
下の方は、if文を使って$1を&#8221;11&#8221;に置き換えています。</p><br />
<p>　 <tt class="docutils literal"><span class="pre">print</span> <span class="pre">$0</span></tt> の$0は、レコード一行全体を表します。<br />
awk の面白いところは、$1や$2を書き換えると$0も変わるところです。<br />
<tt class="docutils literal"><span class="pre">print</span> <span class="pre">$0</span></tt> は、 <tt class="docutils literal"><span class="pre">print</span></tt> と省略できます。<br />
この規則のおかげで、端末に書く文字が短くなります。<br />
以下は例です。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#入力された全フィールドをそのまま出力する方法</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print $1,$2,$3}&#39;</span><br />
1 2 3<br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print $0}&#39;</span><br />
1 2 3<br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{print}&#39;</span><br />
1 2 3<br />
<span class="c">#フィールドの値の変更</span><br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{$2=&quot;二&quot;;print $0}&#39;</span><br />
1 二 3<br />
<span class="o">[</span>ueda\@cent ~<span class="o">]</span><span class="nv">$ </span><span class="nb">echo </span>1 2 3 | awk <span class="s1">&#39;{$2=&quot;二&quot;;print}&#39;</span><br />
1 二 3<br />
</pre></div><br />
</div><br />
<p>　{}に囲まれた部分は「アクション」と呼ばれます。<br />
囲まれていない、抽出の部分は「パターン」と呼ばれます。<br />
アクション内の各文はセミコロンで区切られ、左から右に処理が流れます。<br />
C言語の影響が強いので、記号類の使い方はC言語に似ています。</p><br />
<p>　ところで先ほどからログの「Nov」を「11」に変換していますが、<br />
他の月も変換するにはどうすればよいでしょうか。<br />
sed や awk を12個つなげばできますが<br />
（脚注：マルチコアの場合、12個つなぐと並列処理になるのでバカにしてはいけません。）、<br />
awk や sed のスクリプトを用意することもできます。<br />
月の変換では、次のMONTHファイルを準備して sed で使えばよいでしょう。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat MONTH<br />
s/^Jan/01/<br />
s/^Feb/02/<br />
s/^Mar/03/<br />
（以下略）<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>sed -f ./MONTH secure | tail -n 1<br />
11 23 16:35:05 cent su: pam_unix<span class="o">(</span>su:session<span class="o">)</span>: sess（略）<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="id7"><br />
<h3>2.2.4. フィールドの抽出と並び替え<a class="headerlink" href="#id7" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　あるフィールド$iの抽出をしたい場合は <tt class="docutils literal"><span class="pre">print</span> <span class="pre">$i</span></tt> と記述します。<br />
次の例では、access_logから第4フィールドを抽出しています。<br />
ただ、access_logの区切り文字は複雑なので、<br />
この場合の第4フィールドは単に空白区切りで見たときの4番目のデータということになります。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>head -n 1 httpd/access_log<br />
114.80.93.71 - - <span class="o">[</span>20/Nov/2011:06:47:54 +0900<span class="o">]</span> <span class="s2">&quot;GET / HTTP/1.1&quot;</span> 200 1429 （略）<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span><br />
<span class="o">[</span>20/Nov/2011:06:47:54<br />
（以下略）<br />
</pre></div><br />
</div><br />
<p>並び替えは、並べたい順にフィールドを指定してprintを適用します。<br />
例えば前の例に続けて、抽出した日付、時刻のデータを8桁の日付、<br />
6桁の時刻で正規化するには次のように操作します。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span> | sed <span class="s1">&#39;s;[:/\\[]; ;g&#39;</span> | awk <span class="s1">&#39;{print $2,$1,$3,$4$5$6}&#39;</span> | sed -f ./MONTH | awk <span class="s1">&#39;{print $3$1$2,$4}&#39;</span><br />
20111120 064754<br />
20111120 064805<br />
（略）<br />
</pre></div><br />
</div><br />
<p>長いので各段階でパイプを切って出力を観察しましょう。<br />
file1 から file2 への変換では、sed で <tt class="docutils literal"><span class="pre">[,</span> <span class="pre">:,</span> <span class="pre">/</span></tt> を空白に変換しています。<br />
正規表現にスラッシュが含まれるので、区切り文字にセミコロンを使っています。<br />
file2 から file3 への変換では、<br />
<tt class="docutils literal"><span class="pre">print</span></tt> を使って日付の年月日の並び替えと時分秒の間のスペースを除去しています。<br />
この例では、 <tt class="docutils literal"><span class="pre">print</span></tt> する変数の間にカンマがあったりなかったりしますが、<br />
カンマを入れると空白区切りで出力、カンマを入れないと連結して出力という意味になります。<br />
カンマを入れずに連結する場合は、 <tt class="docutils literal"><span class="pre">$4</span> <span class="pre">$5</span> <span class="pre">$6</span></tt> と間に空白を入れても連結されます。<br />
あとは月を数字表記に変えて、年月日を連結して目標の出力を得ています。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat httpd/access_log | awk <span class="s1">&#39;{print $4}&#39;</span> | head -n 1 &gt; file1<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file1<br />
<span class="o">[</span>20/Nov/2011:06:47:54<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file1 | sed <span class="s1">&#39;s;[:/\\[]; ;g&#39;</span> &gt; file2<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file2<br />
 20 Nov 2011 06 47 54<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file2 | awk <span class="s1">&#39;{print $2,$1,$3,$4$5$6}&#39;</span> &gt; file3<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file3<br />
Nov 20 2011 064754<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file3 | sed -f ./MONTH &gt; file4<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file4<br />
11 20 2011 064754<br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat file4 | awk <span class="s1">&#39;{print $3$1$2,$4}&#39;</span><br />
20111120 064754<br />
</pre></div><br />
</div><br />
</div><br />
<div class="section" id="id8"><br />
<h3>2.2.5. おまけ<a class="headerlink" href="#id8" title="このヘッドラインへのパーマリンク">¶</a></h3><br />
<p>　awk については、他にも改行を取ったり、行をまたいで数値を集計したりと、<br />
まだちょっと覚えなければならないことがありますが、<br />
次回のログ処理で使うにはこの程度で十分です。<br />
もうちょっと勉強したい人のために、文法的に凝ったコードを示します。<br />
このコードは、西暦年の情報が入っていない secure に、<br />
無理やり年を付加することを想定したものです。</p><br />
<div class="highlight-bash"><div class="highlight"><pre><span class="c">#MMDDの4桁で月日を表現</span><br />
<span class="c">#3行目で年明け</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>cat hoge<br />
1230<br />
1231<br />
0101<br />
0102<br />
<span class="c">#データをひっくり返し、年をまたいだら年を一つ減らす。</span><br />
<span class="c">#年を入れて8桁にしたら再びデータをひっくり返す。</span><br />
<span class="o">[</span>ueda\@cent LOG<span class="o">]</span><span class="nv">$ </span>tac hoge | awk <span class="s1">&#39;BEGIN{y=&#39;</span><span class="k">$(</span>date +%Y<span class="k">)</span><span class="s1">&#39;;md=&#39;</span><span class="k">$(</span>date +%m%d<span class="k">)</span><span class="s1">&#39;}{if(md&lt;$1){y--};md=$1;print y md}&#39;</span> | tac<br />
20111230<br />
20111231<br />
20120101<br />
20120102<br />
</pre></div><br />
</div><br />
</div><br />
</div><br />
<div class="section" id="id9"><br />
<h2>2.3. おわりに<a class="headerlink" href="#id9" title="このヘッドラインへのパーマリンク">¶</a></h2><br />
<p>　今回は、ログの加工を題材に awk と sed の使い方を説明しました。<br />
今回は端末で awk, sed を使う話で、シェルスクリプトは書きませんでした。<br />
sed で月の英語表記を数字表記に変換する sed スクリプトが一つ出てきました。</p><br />
<p>　今回行った端末での awk, sed の使い方は、空手の「型」のようなものです。<br />
自在にテキストを加工するためには、<br />
このような型を組み合わせて端末で使いこなすことが必要で、<br />
少し慣れる必要があります。<br />
また、端末という限られたスペースで必要な処理を行うことで、<br />
きれいなシェルスクリプトを書くことができるようになります。<br />
そこまで苦労して身につけるべきかというところですが、<br />
あまり深く考えず、<br />
grep の代わりに awk を使ってみてから考えてもらえれば幸いです。</p><br />
</div><br />
</div><br />
<br />

