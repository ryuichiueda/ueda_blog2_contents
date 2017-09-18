---
Keywords:CLI,Linux,シェルプログラミング実用テクニック,書評,シェル芸,シェル芸本
Copyright: (C) 2017 Ryuichi Ueda
---
# grepを読者に300回打たせる「シェルプログラミング実用テクニック」予約開始ということでシェル芸で紹介します。
<a href="http://blog.ueda.asia/?p=5768" title="AWKでビール区切りデータ（beer separated values, BSV）を作ってみる">ビール区切りデータ</a>で遊んで油断してたら拙著「<a href="http://www.amazon.co.jp/dp/4774173444" target="_blank">シェルプログラミング実用テクニック</a>」の予約がAmazonで始まりました。この本は前作「<a href="http://www.amazon.co.jp/dp/B00LBPGFJS" target="_blank">シェルスクリプト高速開発手法入門</a>」よりも「シェル芸」特化型です。<br />
<br />
<br />
<br />
ということで、TeXで書いた本書の原稿をシェル芸でいじくるという体裁で紹介していこうと思います。<br />
<br />
<ul><br />
 <li>補足1: 最初の原稿なので若干入れ替えや修正があります。</li><br />
 <li>補足2: かえって逆効果かもしれん。</li><br />
</ul><br />
<br />
<br />
目次はこんな感じです。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
uedambp:SD_BOOK ueda$ cat sdbook.tex | grep -h include |<br />
 sed 's/.*{//' | sed 's/}/.tex/' |<br />
 xargs grep -ho 'chapter{.[^}]*}' | sed 's/.*{//' | tr -d '}'<br />
はじめに<br />
準備運動<br />
不定型な文章や設定ファイルの検索と加工<br />
ファイルの取り扱いとシステムの操作<br />
ファイルシステムをデータベースにする<br />
大きなデータを処理する<br />
画像や表計算ソフトのワークシート、その他特殊なフォーマットを扱う<br />
CLI的インターネットとのつきあい方<br />
計算<br />
終わりに<br />
付録<br />
[/bash]<br />
<br />
個人的には「大きなデータを処理する」が必見かと。「はじめに」と「準備運動」のところはちょっと私感が入りすぎたような気がしておりツッコミ待ちです。<br />
<br />
また、この本がどれだけ「シェル芸」か、というと、<br />
<br />
[bash]<br />
uedambp:SD_BOOK ueda$ grep -o シェル芸 *.tex | wc -l<br />
 32<br />
[/bash]<br />
<br />
ということで32回「シェル芸」という単語が出てきます。本編が8章+はじめに+付録という構成なので、ざっくり言って1章に3回「シェル芸」という言葉が出てくるということです。<br />
<br />
<br />
他のキーワードでも検索をかけてみましょう。コマンド打ちまくりです。<span style="color:red">300回も読者にgrepを打たせる本って、たぶん他にないと思う。</span><br />
<br />
[bash]<br />
uedambp:SD_BOOK ueda$ grep -o 'awk ' *.tex | wc -l<br />
 331<br />
uedambp:SD_BOOK ueda$ grep -o 'grep ' *.tex | wc -l<br />
 326<br />
uedambp:SD_BOOK ueda$ grep -o 'cat ' *.tex | wc -l<br />
 643<br />
uedambp:SD_BOOK ueda$ grep -o 'sed ' *.tex | wc -l<br />
 327<br />
uedambp:SD_BOOK ueda$ grep -o 'rm ' *.tex | wc -l<br />
 58<br />
uedambp:SD_BOOK ueda$ grep -o 'rm -Rf' *.tex | wc -l<br />
 11<br />
uedambp:SD_BOOK ueda$ grep -o 'python ' *.tex | wc -l<br />
 12<br />
uedambp:SD_BOOK ueda$ grep -o 'ruby ' *.tex | wc -l<br />
 0<br />
uedambp:SD_BOOK ueda$ grep -o 'perl ' *.tex | wc -l<br />
 2<br />
uedambp:SD_BOOK ueda$ grep -o Haskell *.tex | wc -l<br />
 6<br />
uedambp:SD_BOOK ueda$ grep -o 毛 *.tex | wc -l<br />
 8<br />
[/bash]<br />
<br />
<br />
・・・ということで、あまり情報がない中、かえって混乱を招いたような気がしないでもないですが、<span style="color:red">とにかくCLIでコマンドを使い倒す本</span>ですので、端末をいじくる必要のある人、興味のある人には手前味噌ではございますがオススメでございます。<br />
<br />
<br />
<br />
以上、著者から報告でした。何卒よろしくお願いいたします。<br />
<br />
<br />
p.s. ちなみに私、IQで女子高生に負けました。
