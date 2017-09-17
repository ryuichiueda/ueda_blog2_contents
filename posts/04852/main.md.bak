# 【問題】年末年始シェル芸問題集
12月の<a href="http://blog.ueda.asia/?p=4671" title="【問題のみ】第14回東京居残りシェル芸勉強会">シェル芸勉強会</a>よりもひどい問題を準備しましたので、時間をかけてお楽しみください。<br />
<br />
追記: <a href="http://blog.ueda.asia/?p=4821" title="【解答】年末年始シェル芸問題集" target="_blank">解答はコチラ</a><br />
<br />
解答はMacで作りました。ただし、Coreutilsが必要なので、<br />
[bash]<br />
$ brew install coreutils<br />
[/bash]<br />
をお願いします。Q1以外の解答は1/2頃に公開します（Q1は便利なので早めに公開しておきます）。解答はハッシュタグ「#シェル芸」でワイワイやっていただければと。<br />
<br />
良いお年を。<br />
<br />
<br />
<h1>Q1</h1><br />
<br />
<br />
年末年始はディレクトリの掃除をしましょう。ということで、ご自身のPCから重複しているデータを探してみてください。全てのファイルから探すのは大変なので、手始めに重複しているJPEG画像リストを作ってみてください。<br />
<br />
<!--more--><br />
<br />
<h1>解答</h1><br />
<br />
もし何も出てこなかったら適当なjpegファイルをコピーして検出できるか試してみてください。「sed 's/.*/"&"/'」はファイルに半角空白があるときのためにファイル名をダブルクォートで囲む処理です。sortのLANG=Cと-sオプションはファイル数が膨大なときに処理を速くするためにつけています。<br />
<br />
注意: 時間がかかるかもしれません。とりあえずsortの前に一度ファイルに出した方がよいかもしれません。<br />
<br />
[bash]<br />
###出力で1列目の数が同じものが重複の疑いのあるものです###<br />
uedambp:~ ueda$ find ~/ -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' |<br />
xargs -n 1 gmd5sum | LANG=C sort -s -k1,1 |<br />
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'<br />
###Linuxの場合（さらにルートから検索をかけてみる）###<br />
ueda\@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' | <br />
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | <br />
awk '{if(a==$1){print b;print $0}a=$1;b=$0}'<br />
...<br />
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/var/www/bashcms/pages/whats_bashCMS/chinjyu.jpg<br />
c2979e8ed193969aa9e6c2a1438b696b /home/ueda/chinjyu.jpg<br />
f1c3a09b784cc5a55bb820aaa873c79f /var/tmp/GIT/SD_BOOK/IMAGE/noodle.jpg<br />
f1c3a09b784cc5a55bb820aaa873c79f /home/ueda/GIT/SD_BOOK/IMAGE/noodle.jpg<br />
###Open usp Tukubai使用###<br />
ueda\@remote:~$ sudo find / -type f | grep -i '\\.jpg$' | sed 's/.*/&quot;&amp;&quot;/' | <br />
sudo xargs -n 1 md5sum | LANG=C sort -s -k1,1 | yarr num=1 | awk 'NF&gt;2'<br />
[/bash]<br />
<br />
<h1>Q2</h1><br />
<br />
羽田空港の緯度経度を求めてください。<br />
<br />
<h1>Q3</h1><br />
<br />
<br />
任意の級数からネイピア数（自然対数の底の数）を求めてください。精度が良いほど良いこととします。<br />
<br />
<a href="http://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%A4%E3%83%94%E3%82%A2%E6%95%B0%E3%81%AE%E8%A1%A8%E7%8F%BE" target="_blank">こちらを参考に。</a><br />
<br />
<h1>Q4</h1><br />
<br />
<a href="http://blog.ueda.asia/misc/message2015.txt" target="_blank">http://blog.ueda.asia/misc/message2015.txt</a>は、あるメッセージにbase64を多重にかけたものです。解読してください。ワンライナーでなくても構いません。<br />
<br />
<h1>Q5</h1><br />
<br />
円周率をなるべく精度よく求めてみてください。<br />
<br />
<h1>Q6</h1><br />
<br />
集合{a,b,c,d,e}から全ての組み合わせ（部分集合）を列挙してください。（ヒント: すごく簡単です）<br />
<br />
<h1>Q7</h1><br />
<br />
8128が完全数であることを確認してください。<br />
<br />
私はギブアップしてますが、挑戦したい人は<br />
[bash]<br />
14474011154664524427946373126085988481573677491474835889066354349131199152128<br />
[/bash]<br />
が完全数であることを確認してください。（解けても商品は出ないのでほどほどに・・・）<br />
<br />
<br />
<h1>Q8</h1><br />
<br />
「シェル芸」あるいは好きなキーワードを含んだツイートをなるべく集めてリストにしてみてください。<br />
<br />
ちなみに私は以下の解答で力尽きましたので、何か良いアイデアがあれば。<br />
<br />
[bash]<br />
uedambp:~ ueda$ w3m -dump 'https://twitter.com/search?f=realtime&amp;q=%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8&amp;src=typd' |<br />
sed -n '/ 1\\./,$p' | sed -n '1,/^No Tweet/p'<br />
[/bash]
