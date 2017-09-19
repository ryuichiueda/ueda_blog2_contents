---
Copyright: (C) Ryuichi Ueda
---


# USP Magazine 2014年4月号「シェル芸勉強会後追い企画 Haskellでやってはいかんのか？
出典：<a href="http://www.usp-lab.com/pub.magazine.html" target="_blank">USPマガジン2014年4月号</a>

最新号:

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4904807081" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a>

<h1>1. シェル芸勉強会後追い企画: Haskellでやってはいかんのか？</h1>
<p>産業技術大学院・USP研究所・USP友の会　上田隆一
（脚注：順に助教、アドバイザリーフェロー、会長）</p>
<p>こんにちは。USP研究所元社員の上田です。USPマガジンに久しぶりに何か書けと言われました。ご存知のように（？）本誌はもともと、USP友の会が世に送り出した日本唯一のシェルスクリプト総合誌です。最近のUSPマガジンは良くも悪くも大人しいので、友の会っぽさ（脚注：一般的にはダメな意味で扱われる。南無阿弥陀仏。）を取り戻すため、黒いエンジェルちゃんとして舞い戻って来た次第です（脚注：意味不明。ところで本連載は脚注まみれにする予定ですので悪しからず。なんとなく。なんとなくクリスタル。滝川ク（以下略）。）。</p>

<p>ところでシェルスクリプトと言っても、USP研究所のシェルスクリプト（つまりユニケージ）は「データの変換こそプログラミングだ」と言わんばかりに入出力にこだわったものです。Tukubaiコマンドを見ると分かる通り、ほとんどのコマンドは文字列の加工のためにあり、しかもほとんどが標準入力から標準出力に字を流すだけのものです。</p>

<p>このようなシェルスクリプトの使い方はまだそんなに普及しているわけではありませんが、プログラミングの世界には、同じ思想のものが存在します。あのこわいこわい（脚注：なぜこわいのか。「なごやこわい 関数型」で検索。）「関数型言語」です。「違う！」と言う人もいますが、一緒です（脚注：私の頭の中では）。プログラミングというのは、究極のことを言えば、材料を自分の欲しい姿に変換することです。その変換は、「入力」と「出力」を考えれば十分OKなはずなのですが、世の中には余計なものがなんと多いことか。</p>

<p>ということで、本連載ではユニケージの親戚とも言える（脚注：言い過ぎ）関数型言語を取り上げます。
具体的にはHaskellをやります。なぜか。自分が好きだからです。問答無用です。</p>

<p>よし、USPマガジンでHaskellやる名目が立った。</p>

<div class="section" id="id1">

<h2>1.1. Haskellで何やりましょう？</h2>
<p>んで、Haskellで何をやるのか。モナドとか高階関数とかややこしい言葉を使って煙に巻くのか。いや、理屈より先に手を動かした方がよいでしょう。ということで、これまでやってきたシェル芸勉強会（脚注：<a class="reference external" href="http://blog.ueda.asia/?page_id=684">http://blog.ueda.asia/?page_id=684</a>）の問題を、順に淡々と解いて行くことにしましょう。（脚注：これなら毎回ネタを考えないで済むという黒い判断。）</p>

</div>
<div class="section" id="id2">


<h2>1.2. 第1回問題1</h2>
<p>第1回シェル芸勉強会（脚注：hbstudy#38でやらせてもらったものです。2012年10月27日のことでした。）の記念すべき最初の問題は、こんなものでした。</p>

<blockquote>
<div><tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> から、ユーザ名を抽出したリストを作ってください。</div></blockquote>

<p>シェルのワンライナーだと簡単ですね。</p>
```bash
ueda\@ubuntu:~$ cat /etc/passwd | awk &amp;quot;-F:&amp;quot; &amp;#39;{print $1}&amp;#39;
...
sshd
ueda
mysql
postfix
```

<p>等、さらっとできます。さあこれをHaskellでやりましょう（脚注：今、とても面倒くさいという気分です。）。</p>

<p>やる前に、Haskellの環境を整えましょう。特にこだわりがないならUbuntu Linuxの新しいものか、
Macがおすすめです。</p>

<p>Ubuntuの場合、次のコマンド一発でHaskellの環境がインストールできます。</p>

```bash
ueda\@ubuntu:~$ sudo apt-get install haskell-platform
```

<p>Macの場合は、</p>
```bash
uedamac:~ ueda$ brew install ghc
```
<p>でコンパイラをインストールできます。</p>
<div class="section" id="id3">

<h3>1.2.1. 最初なのでとりあえず手を動かしてみる</h3>
<p>では、解いて行きます。最初なので、Haskellのコードを書いてコンパイルすることから始めます。</p>

<p>まず、次のようなファイルを準備してください。1行のHaskellのプログラムです。</p>
```hs
ueda\@ubuntu:~$ cat q1_1.hs
main = getContents &amp;gt;&amp;gt;= putStr
```
<p>これを次のように <tt class="docutils literal"><span class="pre">ghc</span></tt> （The Glasgow Haskell Compiler）
（脚注：GCC?、DHC?、いいえGHCです。）
でコンパイルします。</p>
```bash
ueda\@ubuntu:~$ ghc q1_1.hs
[1 of 1] Compiling Main ( q1_1.hs, q1_1.o )
Linking q1_1 ...
```
<p>すると次のように <tt class="docutils literal"><span class="pre">q1_1</span></tt> というファイルができているはずです。</p>
<div class="highlight-none"><div class="highlight"><pre>ueda\@ubuntu:~$ ls q1_1*
q1_1 q1_1.hi q1_1.hs q1_1.o
</pre></div>
</div>
<p>これを実行してみましょう。 <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt>
を <tt class="docutils literal"><span class="pre">cat</span></tt> してパイプに通します。</p>
<div class="highlight-none"><div class="highlight"><pre>ueda\@ubuntu:~$ cat /etc/passwd | ./q1_1
...
ueda:x:1000:1000:Ryuichi Ueda,,,:/home/ueda:/bin/hs
mysql:x:104:111:MySQL Server,,,:/nonexistent:/bin/false
postfix:x:105:112::/var/spool/postfix:/bin/false
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> の中身が表示されたと思います。
<tt class="docutils literal"><span class="pre">q1_1.hs</span></tt> は今のところ、 <tt class="docutils literal"><span class="pre">cat</span></tt> のように入力されたテキストをそのまま出力するコマンドになってます。</p>

<p>文法は少し書いて動かしてみてから詳しく勉強した方がいいと思いますので、先に進みます。今度は <tt class="docutils literal"><span class="pre">q1_1.hs</span></tt> を図1のように加筆します。これはまだ答えではありません。寄り道したコードなのでご注意を。</p>

<ul class="simple">
<li>図1: 加筆した <tt class="docutils literal"><span class="pre">q1_1.hs</span></tt></li>
</ul>
```hs
ueda\@ubuntu:~$ cat q1_1.hs
main = getContents &amp;gt;&amp;gt;= putStr . main&amp;#39;

main&amp;#39; :: String -&amp;gt; String
main&amp;#39; cs = head ( lines cs )
```
<p>コンパイルして <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> の内容を入力すると、次のように最初の行が改行無しで出力されます。</p>
```bash
ueda\@ubuntu:~$ cat /etc/passwd | ./q1_1
root:x:0:0:root:/root:/bin/hsueda\@remote:~$
```
<p>さて、コードの説明をしていきます。まず、図1の4,5行目から。Haskellは「関数型言語」というだけあって、関数を並べてプログラムしていきますが、この4,5行目は関数 <tt class="docutils literal"><span class="pre">main'</span></tt> の定義です。2行目の <tt class="docutils literal"><span class="pre">main</span></tt> も関数ですが、ちと事情がややこしいのでかなり後から説明をします。</p>

<p>4行目は、関数 <tt class="docutils literal"><span class="pre">main'</span></tt> で「何が入力されて何が出力されるか」
を書いたものです。4行目によると、 <tt class="docutils literal"><span class="pre">main'</span></tt> では
「 <tt class="docutils literal"><span class="pre">String</span></tt> が入力されて <tt class="docutils literal"><span class="pre">String</span></tt> が出力される」
ということになっています。
<tt class="docutils literal"><span class="pre">String</span></tt> というのは文字列を表す「型」というものですが、
とりあえずそれだけ覚えて5行目に移ります。</p>
<p>5行目には、イコール（ <tt class="docutils literal"><span class="pre">=</span></tt> ）で挟まれて左辺と右辺がありますが、
左辺の <tt class="docutils literal"><span class="pre">main'</span> <span class="pre">cs</span></tt> は、
関数 <tt class="docutils literal"><span class="pre">main'</span></tt> がとる引数は <tt class="docutils literal"><span class="pre">cs</span></tt> であるという意味で、
<tt class="docutils literal"><span class="pre">cs</span></tt> は4行目の型の指定どおり、 <tt class="docutils literal"><span class="pre">String</span></tt> 、
つまり文字列です。</p>
<p>右辺には処理の内容が記述されます。まず、 <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> ですが、これは <tt class="docutils literal"><span class="pre">cs</span></tt> が <tt class="docutils literal"><span class="pre">lines</span></tt> という関数に入力するという意味になります。C言語ライクな言語だと <tt class="docutils literal"><span class="pre">lines(cs)</span></tt> と書くようなところですが、Haskellの場合、括弧がいりません。コマンドとオプションの関係に似ています。</p>
<p><tt class="docutils literal"><span class="pre">lines</span></tt> は文字列を行単位に分割してする関数で、今後も頻繁に登場します。
次に <tt class="docutils literal"><span class="pre">head</span> <span class="pre">(lines</span> <span class="pre">cs)</span></tt> ですが、これは <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt>
の出力を <tt class="docutils literal"><span class="pre">head</span></tt> に入力するという意味になります。
<tt class="docutils literal"><span class="pre">head</span></tt> 関数は、与えられた入力（この場合は行単位に分割された各行）の最初の一つを出力する関数です。</p>
<p>したがって、 <tt class="docutils literal"><span class="pre">main'</span></tt> を日本語にすると、「文字列を受け取って最初の一行を返す関数」ということになります。</p>
<p>というわけで、 <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> を入力すると、
<tt class="docutils literal"><span class="pre">main'</span> <span class="pre">cs</span></tt> の出力は <tt class="docutils literal"><span class="pre">/etc/passwd</span></tt> の先頭の一行ということになります。
それが2行目の <tt class="docutils literal"><span class="pre">putStr</span></tt> に渡って画面に出力されます
（脚注：くどいようですが2行目の説明は当分の間しません。）。</p>
</div>
<div class="section" id="id4">
<h3>1.2.2. そろそろ型の話をしないと説明が難しいので</h3>
<p>さて、最初からHaskellの初心者を完全に置いてきぼりにしている感が否めないので、今の部分を別の視点からもう一度説明します。</p>

<p>とりあえず今やったことを最もはしょって説明すると、<tt class="docutils literal"><span class="pre">main'</span></tt> に「何か文字列が入力されたらそれを加工して返す」という関数を書くと、 <tt class="docutils literal"><span class="pre">q1_1</span></tt>がその通り文字列を加工するプログラムになるということになります。したがって、我々は <tt class="docutils literal"><span class="pre">main'</span></tt> だけに集中すればよいことになります。</p>

<p>ということは、とりあえずシェル芸のように標準入出力を扱うだけの問題に対しては、今書いたコードをコピペして <tt class="docutils literal"><span class="pre">main'</span></tt> だけ書き換えればよいということになります。もっと複雑なことをするときは、何か別の関数を書いて <tt class="docutils literal"><span class="pre">main'</span></tt> の中で使えばよいことになります。</p>

<p>結局、Haskellでプログラムするということは、関数と関数をくっつけて別の関数を作っていくという作業にすぎません。このとき、関数にはくっつくものとくっつかないものがあります。それを決めるものが「型」です。型は <tt class="docutils literal"><span class="pre">ghci</span></tt> というHaskellのインタプリタで調べることができます。</p>

<p>例えば、 <tt class="docutils literal"><span class="pre">lines</span></tt> の型は</p>
<div class="highlight-none"><div class="highlight"><pre>Prelude&gt; :t lines
lines :: String -&gt; [String]
</pre></div>
</div>
<p>というように、 <tt class="docutils literal"><span class="pre">String</span></tt> を入力し、 <tt class="docutils literal"><span class="pre">[String]</span></tt>
を出力するものです。
<tt class="docutils literal"><span class="pre">[</span> <span class="pre">]</span></tt> は「リスト」というもので、ある型のものを順番に並べたものですが、いずれ詳しく説明します。</p>
<p>さて、これで図1の <tt class="docutils literal"><span class="pre">lines</span></tt> の型は
分かりました。では、 <tt class="docutils literal"><span class="pre">head</span></tt>
はどうでしょう？</p>
<div class="highlight-none"><div class="highlight"><pre>Prelude&gt; :t head
head :: [a] -&gt; a
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">a</span></tt> というもののリストが入力、
<tt class="docutils literal"><span class="pre">a</span></tt> の型のものが出力、と読めます。
この <tt class="docutils literal"><span class="pre">a</span></tt> ですが、実は <tt class="docutils literal"><span class="pre">String</span></tt> に化けることができます（脚注：型推論というやつです。本稿では難しい単語は全て脚注に追い出します。難しい言葉を並べて初心者を煙に巻く奴にこれまでいやというほど嫌な目に遭っているので。だいたい一ヶ月後には追い抜いてますが。）。ですので、 <tt class="docutils literal"><span class="pre">head</span> <span class="pre">(lines</span> <span class="pre">cs)</span></tt>
（脚注：この括弧は、 <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> というものを一つにとりまとめるだけの括弧で、
<tt class="docutils literal"><span class="pre">head</span> <span class="pre">()</span></tt> のようなC言語的な解釈をしてはいけません。）
と書いたときの <tt class="docutils literal"><span class="pre">head</span></tt>
の型は、</p>
<div class="highlight-none"><div class="highlight"><pre>head :: [String] -&gt; String
</pre></div>
</div>
<p>となります。そのため、 <tt class="docutils literal"><span class="pre">lines</span> <span class="pre">cs</span></tt> というものを受ける事ができるのです。
実は、 <tt class="docutils literal"><span class="pre">head</span> <span class="pre">(lines</span> <span class="pre">cs)</span></tt> は <tt class="docutils literal"><span class="pre">(head</span> <span class="pre">.</span> <span class="pre">lines)</span> <span class="pre">cs</span></tt>
とも書けます。この場合、解釈の上では、
「 <tt class="docutils literal"><span class="pre">cs</span></tt> を <tt class="docutils literal"><span class="pre">head</span> <span class="pre">.</span> <span class="pre">lines</span></tt> という関数に入力する」
という解釈になります。
<tt class="docutils literal"><span class="pre">head</span> <span class="pre">.</span> <span class="pre">lines</span></tt> は二つの関数をくっつけて一つにしたもの
（脚注：「合成関数」というものです。）で、
その証拠に、 <tt class="docutils literal"><span class="pre">ghci</span></tt> に聞いたら、</p>
<div class="highlight-bash"><div class="highlight"><pre>Prelude&gt; :t head . lines
head . lines :: String -&gt; String
</pre></div>
</div>
<p>とちゃんと型が返ってきます。</p>
<p>ここで、はっきり断っておきます。</p>
<blockquote>
<div>Haskellは難しくありません。
単に関数を型を合わせてパズルのように連結していくだけです。</div></blockquote>
<p>難しいと感じるのは、使うアルゴリズムがC言語系のものと違うからです。実際にはHaskell云々、関数型云々というよりも、こっちの方が本質的な問題です。</p>

</div>
<div class="section" id="id5">
<h3>1.2.3. では解答</h3>
<p>初回なので思いっきり回りくどくなりましたが、さっさと解答して本稿を締め殺します。</p>
<ul class="simple">
<li>図2: 問題1の解答</li>
</ul>
```hs
ueda\@remote:~$ cat q1_1.hs
main = getContents &amp;gt;&amp;gt;= putStr . main&amp;#39;

main&amp;#39; :: String -&amp;gt; String
main&amp;#39; cs = unlines $ map ( takeWhile (/= &amp;#39;:&amp;#39;) ) ( lines cs )
```
<p>実行してみましょう。</p>
```bash
ueda\@remote:~$ ghc q1_1.hs
[1 of 1] Compiling Main ( q1_1.hs, q1_1.o )
Linking q1_1 ...
ueda\@remote:~$ cat /etc/passwd | ./q1_1
...
ueda
mysql
postfix
```


<p>できました。さて、難しいものがまた出てきましたので、解説を・・・えっ？もうページが足りない？？なんと。では、次回ということで・・・。</p>

<p>さいならさいなら。</p>

<a href="http://blog.ueda.asia/?page_id=2944">各号の一覧へ</a>
