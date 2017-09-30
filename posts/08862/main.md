---
Keywords: コマンド,シェルスクリプト,Advent,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# SHELQ: 怪しいシェル芸キュレーションサイト
この記事は<a href="http://qiita.com/advent-calendar/2016/shell-script">Shell Script Advent Calendar 2016</a> 18日目の記事です。

本記事の趣旨は、今年を中心にTwitterやシェル芸勉強会上で出たこわいワンライナーを、巷にあふれるクソバイラル的なランキング形式でお届けしようというものです。人さまのワンライナーを紹介していきます。普段、自分のブログでは人のふんどしでほんだしをとる((　ふんどしを脱ぐと立派な鰹節が出現するイメージの下ネタです。))ようなことはなるべくしないことにしてますが、毎年謎に盛り上がるShell Script Advent Calendarに便乗してしれっとやります。あと、<a href="/?post=09029">先日せっかくこんなことを書いたのに</a>まるで自分で守ってないのは、やさぐれているからです。ご了承ください。


ということで、私、上田マリ（シェルガポール在住）の<strong>「シェル芸キュレーション」</strong>をお楽しみください。

<blockquote>今、私は、シェルガポールからのリモートシェル芸で、いかにshelqとシェル芸ヴェンキョウカイを成長させていくかしか考えていません。この新たな挑戦と新しい働き方へのトライに、シェルシェルシェルシェル、核シェルターですね。 ---上田マリ</blockquote>

すみません！ほんとすみません！((　かなりイキってるインタビューである <a href="https://m.newspicks.com/news/651502/body/?sentlog">https://m.newspicks.com/news/651502/body/?sentlog</a> を参考にさせていただきました。))


Ubuntu 16.04 LTSのGUI環境で、必要なものをインストールした上で動作を確認しています。しかし、何が起きても責任は負えません。

<h2>第10位 （2016年2月・微妙に危険）<pre>$ touch + ; echo 2 * 3 | bc
5</pre></h2>

まずは第10位。「<a href="http://togetter.com/li/938154">第21回未経験者大歓迎！誰でも働けるアットホームな職場ですシェル芸勉強会</a>」の午前の部で鳥海さんによって誘発された<span style="color: #ff0000;"><strong>「こんなミス誰もしないだろシェル芸」</strong></span>です。

上記のような計算間違いは<strong>「ディレクトリの中に『+』と言う名前のファイルがあり、そしてbcを使う時にアスタリスクのクオートを忘れると、アスタリスクがファイルのリストに変換（+だけなので+に変換）されて『2 + 3』がbcに渡る」</strong>という、ありがちな状況でよく起こります。ありがちではありません。

このバカバカしい計算間違い体験をどうしてもしたい方は、次のようにシェルとよろしくやっててください。

```bash
mery\@welq:~$ mkdir iemo
mery\@welq:~$ cd !$
cd hoge
mery\@welq:~/iemo$ touch +
mery\@welq:~/iemo$ echo 2 * 3 | bc
5
```

以上、第10位でした。

<h2>第9位（2015年10月・<span style="color:red">ちょっと危険</span>）<pre>$ echo {000000000..9999999999}</pre></h2>

第9位は<span style="color:red">「100億個の数字をメモリに書くまでbashとお前を家に帰さない危険シェル芸」</span>です。<a href="http://togetter.com/li/893396">マイナンバーシェル芸事件</a>((　マイナンバーに抜けがないか、みんなで仲良く<del datetime="2016-12-12T00:05:26+00:00">襲撃</del>検証した事件。))の際、とりあえず数字を全部列挙しようとしている最中に飛び出した危険なワンライナーです。

ナニがドーなるか説明しておきます。bashは
```bash
spotlight\@never:~$ echo {0..9}
0 1 2 3 4 5 6 7 8 9
```
というふうに、連番を略記して入力すると展開して、コマンド（この場合はecho）に渡してくれる機能があります。コマンドに展開したものを引数として渡すには・・・全部メモリの上で展開する必要があります。これを踏まえて、もう一度9位のコマンドを見てください。<span style="color:red">bashが可哀想に見えます。</span>

このときは、bashだけでなく、次の方々が犠牲になりました。尊い。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda">\@ryuichiueda</a> bashが大暴走しまつ・・マジで。</p>&mdash; クソッシェル芸エンジニアめ (\@papiron) <a href="https://twitter.com/papiron/status/659026666568617985">2015年10月27日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">また尊い犠牲が・・・ &gt; <a href="https://twitter.com/takion0">\@takion0</a> <a href="https://twitter.com/hashtag/%E5%8D%B1%E9%99%BA%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#危険シェル芸</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/659027630486720512">2015年10月27日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

尊い。

<h2>第8位 （2016年10月）（安全・迷惑）
<pre>$ echo 響け！ユーフォニアム | sed ':a;p;s/\\(.\\)\\(.*\\)/\\2\\1/;/^ム/!ba'
響け！ユーフォニアム
け！ユーフォニアム響
！ユーフォニアム響け
ユーフォニアム響け！
ーフォニアム響け！ユ
フォニアム響け！ユー
ォニアム響け！ユーフ
ニアム響け！ユーフォ
アム響け！ユーフォニ
ム響け！ユーフォニア</pre></h2>

第8位は、<a href="https://twitter.com/eban">\@eban</a>さんの<span style="color: #ff0000;"><strong>「響け！ユーフォニアム10段逆スライド方式シェル芸」</strong></span>です。ある日、上の出力のように<a href="http://togetter.com/li/1041621">1文字ずつずらして「響け！ユーフォニアム」という文字列を出力するだけの<del datetime="2016-12-09T13:42:03+00:00">不毛な</del>パズルがTwitter上で<del datetime="2016-12-09T13:46:01+00:00">暇な人たちによって</del>流行ったのですが</a>、みんながワイワイ長いワンライナーを捻り出している時にしれっと氏が出したものです。
<blockquote class="twitter-tweet" data-lang="ja">
<p dir="ltr" lang="ja">% echo 響け！ユーフォニアム | sed ':a;p;s/\\(.\\)\\(.*\\)/\\2\\1/;/^ム/!ba'<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a></p>
— eban (\@eban) <a href="https://twitter.com/eban/status/791624333210759170">2016年10月27日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

一応、ちゃんと解説をしておくと、これはsed（GNU sed）のbコマンドを用いたものです。sedの部分をsedのスクリプトファイルにしてコメントを入れると、次のようになります。

```bash
curazy\@grape:~$ cat ufo.sed 
#!/bin/sed -f
 
#aというラベルをつける。「b a」でここに戻る
:a 

#1行プリント
p

#一番最初の字を後ろにくっつける
s/\\(.\\)\\(.*\\)/\\2\\1/

#ムで始まらなければラベルaに戻る
/^ム/!b a
```

このスクリプトに「響け！ユーフォニアム」という文字列を入れると、頭の文字が「ム」になるまで同じ行に対してp（プリント）が実行されるので、上記のような出力が得られます。

実行は次のように行いましょう。

```bash
takagi\@buzznews:~$ chmod +x ./ufo.sed
takagi\@buzznews:~$ echo 響け！ユーフォニアム | ./ufo.sed 
響け！ユーフォニアム
け！ユーフォニアム響
！ユーフォニアム響け
ユーフォニアム響け！
ーフォニアム響け！ユ
フォニアム響け！ユー
ォニアム響け！ユーフ
ニアム響け！ユーフォ
アム響け！ユーフォニ
ム響け！ユーフォニア
```

ちなみに、やり出しっぺの人は
<blockquote class="twitter-tweet" data-lang="ja">
<p dir="ltr" lang="ja">（今更ながら響け！ユーフォニアムなるものを全く見たことがないなんて言えない。。。）</p>
— ぐれさん (\@grethlen) <a href="https://twitter.com/grethlen/status/791622617304223744">2016年10月27日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

だそうです。代わりに謝っておきます。私も見たことも食べたこともありません。ファンの人たちには本当に迷惑な話です。

<iframe width="560" height="315" src="https://www.youtube.com/embed/drRRxP8XrOQ" frameborder="0" allowfullscreen></iframe>

<h2>第7位 （2016年9月・安全）<pre>$ banner --help</pre></h2>

どうなるか？こうなります。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">おいbannerコマンド馬鹿にしてんのか。<a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash">#シェル芸</a> <a href="https://t.co/d9P3CzhoMs">pic.twitter.com/d9P3CzhoMs</a></p>&mdash; ぐれさん (\@grethlen) <a href="https://twitter.com/grethlen/status/778952287339163649">2016年9月22日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

以上、ぐれさんの<span style="color: #ff0000;"><strong>「コマンドに馬鹿にされるシェル芸」</strong></span>でした。


<h2>第6位（2014年8月他、破壊実績多数・<span style="color:red">試すな危険</span>）<pre>$ : () { : | : & } ; : </pre></h2>

第6位は、すこしリリース（？）から時間が経ってしまったのでランクダウンしましたが、未だに存在感抜群の<a style="color:red" href="https://ja.wikipedia.org/wiki/Fork%E7%88%86%E5%BC%BE">forkbomb</a>です。これをシェルに打ち込むと、なにも対策を立てる間も無くOSが死にます。

この入力の意味は「:という名前の関数を定義します。その関数は、自分自身をパイプで2つつないだものをバックグラウンドプロセスで実行するというものです。:を定義したら、さっそく実行します。」というものなので、:がひとつ実行するごとに、別の:が起動して、それらが再び:を２つ起動して・・・」と倍々になってすぐプロセスで一杯になってOSが死にます。どんどんプロセスを使うので他のコマンドも起動できず、大抵の場合シャットダウンもうまくいきません。

Dockerなら大丈夫だろうと試したらホストまで死んだという報告もあるので、<span style="color:red">試すなよ！絶対試すなよ！</span>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">危険シェル芸タグのコマンドをdocker上で打ってたらホストまで沈黙してしまった</p>&mdash; んきりも (\@nnikirom) <a href="https://twitter.com/nnikirom/status/502078085798178816">2014年8月20日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<ul>
 <li>参考: <a href="http://togetter.com/li/709172">【試さないで】危険シェル芸【違法(脱法)シェル芸を勧められたり、 身近な人が持っていたりしませんか？】</a></li>
</ul>

<h2>第5位（2014年9月・<span style="color:red">ある意味危険</span>）<pre>$ env x='() { :;}; echo vulnerable' bash -c 'echo this is a test'
vulnerable
this is a test
</pre></h2>

第5位は、これもちょっと古いのでランクを落としてしまった<span style="color: #ff0000;"><strong>「Shellshock調査用ワンライナー」</strong></span>です。<a href="https://ja.wikipedia.org/wiki/2014%E5%B9%B4%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF%E8%84%86%E5%BC%B1%E6%80%A7">Shellshock</a>は、「関数の定義を変数に代入しようとすると、関数の後ろに書いたコマンドが実行できてしまう。」というbashのバグ（と、その後の騒動）を指します。

これだけなら「ふーん」という感じですが、CGIでbashが立ち上がるようになっていると話は別です。webサーバがGETで送られてきた文字列を変数に保存しますので、そのときに<strong>文字列に仕込んだコマンドが実行される</strong>ことになって非常に危険です。次の例は、騒ぎの中、私のウェブサーバに飛んできたリクエストのログです。パスワードファイルを盗み見しようとしています。
```bash
xxx.yyy.zzz.aaa - - [25/Sep/2014:08:32:26 +0900] "GET / HTTP/1.1" 302 208
 "-" "() { :;}; echo Content-type:text/plain;echo;/bin/cat /etc/passwd"
```

ところで、「CGIでbashが立ち上がるなんて、<a href="https://www.amazon.co.jp/dp/4048660683">こんな本</a>を書いたお前のところだけだろ」という声も聞こえて来そうなんですが、<strong>CGIスクリプトからコマンドを読んでおり、shと打つとbashが代わりに立ち上がる環境でウェブサーバが動作している</strong>という場合、知らないうちにbashが立ち上がっていますので、ご注意ください。当然、最新のbashではこのバグは潰されています。

<h2>第4位 （2016年9月・<span style="color:red">悪用危険</span>）<pre>H4sICBmZ4lcAA2VsZgCrd/VxY2RkZIABJgZmBhAvMcBEyIQBAUwYFBhgquCqgWpAVDMUs4I4AgwMjxvbHjdNftw4mQuodgcLUHA3SMvOEKD6XbxA1tmGHSCB3QxgNgCMjcoWgwAAAA==</pre></h2>

これはワンライナーでなく、ワンライナーで解く対象となる暗号です。<a href="http://togetter.com/li/1027398">なぜかTwitter上でシェル芸暗号解読大会が開催された時</a>に私が考えた<span style="color: #ff0000;"><strong>「Twitterに実行ファイルをエンコーディングして乗っけようとして頑張ってたら乗ってしまったやつ」</strong></span>です。<a href="http://d.hatena.ne.jp/yupo5656/20061112/p2">こちらのサイト</a>からELF（実行バイナリ）を作り、それをzipやbase64で変換したものです。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="und" dir="ltr">H4sICBmZ4lcAA2VsZgCrd/VxY2RkZIABJgZmBhAvMcBEyIQBAUwYFBhgquCqgWpAVDMUs4I4AgwMjxvbHjdNftw4mQuodgcLUHA3SMvOEKD6XbxA1tmGHSCB3QxgNgCMjcoWgwAAAA==</p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/778604279594491904">2016年9月21日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">収まったああああああ</p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/778604312112930816">2016年9月21日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

次のように実行できます。

```bash
takeda\@jooy:~$ base64 -d hoge | gunzip > a ; chmod +x a ; ./a
うんこ
```

ところでこの問題、昨日発売された、<span style="color:red">Software Design 2017年1月号</span>に似た問題が出ています（ネタバレになったら申し訳なく）。Software Design 2017年1月号で、特集で「シェル30本ノック」というのをシェル芸勉強会周辺の方々と書きました。「ワンライナー((　いつもお世話になっている編集のYさんは、頑なに「シェル芸という言葉は使わないのです。ブームの火付け役なのに。たぶん、ブレーキかけないと暴走し出すと思ってるのではなかろうか。正解。))中心に40ページ」ということで、1人じゃ無理なので、シェル芸勉強会の周りの<del datetime="2016-12-08T14:24:11+00:00">変態さん</del>腕利きの方々に参加を募り、Slackでチームを作ってGitHubでわーっと書いていきました。SoftwareDesignのきっちりしているところと、シェル芸勉強会の奔放なところをうまく両立できていると思いますので、ぜひご一読を。

[amazonjs asin="B01MFBDOTV" locale="JP" title="ソフトウェアデザイン 2017年 01 月号 雑誌"]


以上、宣伝でした。

<h2>第3位（2014年8月・安全）<pre>$ eval eval \\''n='\\''{1..'$(dc -e 1000vp)'}'\\'' eval eval eval echo '\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\'\\\\\\'\\''$&#40;('\\'\\\\\\'\\\\\\\\\\\\\\'\\\\\\'\\''$n'\\'\\\\\\'\\\\\\\\\\\\\\'\\\\\\'\\''*'\\'\\\\\\'\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\'\\''{2..$&#40;(1000/n))}'\\'\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\'\\\\\\'\\''))'\\'\\\\\\'\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\'';'\\' | tr ' ' \\\\n | sort -n | uniq -u</pre></h2>

第3位、こちらも古いんですが、あまりにも変態すぎるので未だシェル芸界隈では語り草になっている鳥海師匠の<span style="color: #ff0000;"><strong>「変態素数ワンライナー」</strong></span>です。上のワンライナーをコピペして動かしてみてください。ちゃんと動きます。そして、安心・安全です。

```bash
cafy\@upin:~$ （変態すぎてSyntaxhilighterがうまく動かないので省略） | head
2
3
5
7
11
13
17
19
23
29
```

ちゃんと動く以外、詳細不明です。


<h2>第2位 （2016年4月30日・<span style="color:red">そこそこ危険</span>）<pre>
$ alias eval='eval eval'
$ eval</pre></h2>

さて第2位です。これも鳥海師匠の講義の最中に飛び出した<span style="color: #ff0000;"><strong>「イーバル！イーバルイーバル！！イーバル！！！」</strong></span>です。<strong>「ちょっと！ちょっとちょっと！」のニュアンスで1行目を読み込み、「バルズ！！」のニュアンスで2行目を実行すると、端末が死にます。</strong>コンソールでやるとPCがシャットダウンします。ちょっと、気持ちいいです。

死ぬ原理ですが、forkbombのマイルドバージョンで、2行目のevalを実行するとeval evalに置き換わってeval evalが実行され、さらにevalが二つに分裂し・・・ということでevalがたくさんになってbashがパンクして死にます。

端末で行う場合、被害としてはその端末が落ちるだけですので、皆さんもスタバ等でドヤリングする際は、exitの代わりに
```bash
cuta\@findtravel:~$ alias eval='eval eval'
cuta\@findtravel:~$ eval
```
と打って（キーボードは強打すること）、かっこよく端末を閉じるグッドプラクティスを身につけてはいかがでしょうか。何が起きても私は責任を取りませんが。

<h2>第1位 (2016年4月・安全)
<pre>$ l='L${r}FR${l}F${l}RF${r}L' r='R${l}FL${r}F${r}LF${l}R' eval eval eval eval eval eval l= r= eval echo '$l' | { read a; b=${a%%F*}; echo "from turtle import *;speed(0);pensize(2);ms=min(screensize())*0.8;l=2*ms/(2**${#b}-1);up();setpos(-ms,-ms);down();${a}done()"; } | sed 's/L/lt(90);/g;s/R/rt(90);/g;s/F/fd(l);/g' | python</pre>
</h2>


さて今回の第1位は、鳥海師匠の<span style="color: #ff0000;"><strong>「ヒルベルト曲線ワンライナー」</strong></span>です。デスクトップ環境でお楽しみください。以下は本人による実行例です。

<iframe src="https://www.youtube.com/embed/e3UPHCrOmzE" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

解説はこちらの<a href="https://twitter.com/hexomino">\@hexomino</a>さんのLT資料にあります。変数に再帰的に経路を埋め込んで行って、最後にPythonに食わせて実行するという手順のようです。ワンライナーもご本人の了承を得て\@hexominoさんの資料から拝借しました。

<iframe style="border: 1px solid #CCC; border-width: 1px; margin-bottom: 5px; max-width: 100%;" src="//www.slideshare.net/slideshow/embed_code/key/s46u6fLfVzxkFf" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen="allowfullscreen"> </iframe>
<div style="margin-bottom: 5px;"><strong> <a title="本日の怪物曲線 2016/6/18" href="//www.slideshare.net/HexominoHexomino/2016618-63204215" target="_blank">本日の怪物曲線 2016/6/18</a> </strong> from <strong><a href="//www.slideshare.net/HexominoHexomino" target="_blank">Hexomino Hexomino</a></strong></div>

うん。わからん。

<h2>最後に</h2>

ということで、鳥海師匠の1〜3位独占で終わりました。某サイト群と違って師匠には快諾を得て書いておりますが、こうやって人のやったことでブログを書いていると、やっぱり自分の手柄は本人が自分の言葉で書いた方がいいんじゃないかなあと思ってしまいます。

師匠におかれましては、ぜひ「今日から俺はシェル芸で飯を食うんだ」とご決心いただければ幸いです。


以上。

[amazonjs asin="B01MFBDOTV" locale="JP" title="ソフトウェアデザイン 2017年 01 月号 雑誌"]



