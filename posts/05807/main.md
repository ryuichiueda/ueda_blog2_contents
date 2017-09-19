---
Keywords: CLI,Linux,シェルプログラミング実用テクニック,書評,シェル芸,シェル芸本
Copyright: (C) 2017 Ryuichi Ueda
---

# grepを読者に300回打たせる「シェルプログラミング実用テクニック」予約開始ということでシェル芸で紹介します。
<a href="http://blog.ueda.asia/?p=5768" title="AWKでビール区切りデータ（beer separated values, BSV）を作ってみる">ビール区切りデータ</a>で遊んで油断してたら拙著「<a href="http://www.amazon.co.jp/dp/4774173444" target="_blank">シェルプログラミング実用テクニック</a>」の予約がAmazonで始まりました。この本は前作「<a href="http://www.amazon.co.jp/dp/B00LBPGFJS" target="_blank">シェルスクリプト高速開発手法入門</a>」よりも「シェル芸」特化型です。



ということで、TeXで書いた本書の原稿をシェル芸でいじくるという体裁で紹介していこうと思います。

<ul>
 <li>補足1: 最初の原稿なので若干入れ替えや修正があります。</li>
 <li>補足2: かえって逆効果かもしれん。</li>
</ul>


目次はこんな感じです。

<!--more-->

[bash]
uedambp:SD_BOOK ueda$ cat sdbook.tex | grep -h include |
 sed 's/.*{//' | sed 's/}/.tex/' |
 xargs grep -ho 'chapter{.[^}]*}' | sed 's/.*{//' | tr -d '}'
はじめに
準備運動
不定型な文章や設定ファイルの検索と加工
ファイルの取り扱いとシステムの操作
ファイルシステムをデータベースにする
大きなデータを処理する
画像や表計算ソフトのワークシート、その他特殊なフォーマットを扱う
CLI的インターネットとのつきあい方
計算
終わりに
付録
[/bash]

個人的には「大きなデータを処理する」が必見かと。「はじめに」と「準備運動」のところはちょっと私感が入りすぎたような気がしておりツッコミ待ちです。

また、この本がどれだけ「シェル芸」か、というと、

[bash]
uedambp:SD_BOOK ueda$ grep -o シェル芸 *.tex | wc -l
 32
[/bash]

ということで32回「シェル芸」という単語が出てきます。本編が8章+はじめに+付録という構成なので、ざっくり言って1章に3回「シェル芸」という言葉が出てくるということです。


他のキーワードでも検索をかけてみましょう。コマンド打ちまくりです。<span style="color:red">300回も読者にgrepを打たせる本って、たぶん他にないと思う。</span>

[bash]
uedambp:SD_BOOK ueda$ grep -o 'awk ' *.tex | wc -l
 331
uedambp:SD_BOOK ueda$ grep -o 'grep ' *.tex | wc -l
 326
uedambp:SD_BOOK ueda$ grep -o 'cat ' *.tex | wc -l
 643
uedambp:SD_BOOK ueda$ grep -o 'sed ' *.tex | wc -l
 327
uedambp:SD_BOOK ueda$ grep -o 'rm ' *.tex | wc -l
 58
uedambp:SD_BOOK ueda$ grep -o 'rm -Rf' *.tex | wc -l
 11
uedambp:SD_BOOK ueda$ grep -o 'python ' *.tex | wc -l
 12
uedambp:SD_BOOK ueda$ grep -o 'ruby ' *.tex | wc -l
 0
uedambp:SD_BOOK ueda$ grep -o 'perl ' *.tex | wc -l
 2
uedambp:SD_BOOK ueda$ grep -o Haskell *.tex | wc -l
 6
uedambp:SD_BOOK ueda$ grep -o 毛 *.tex | wc -l
 8
[/bash]


・・・ということで、あまり情報がない中、かえって混乱を招いたような気がしないでもないですが、<span style="color:red">とにかくCLIでコマンドを使い倒す本</span>ですので、端末をいじくる必要のある人、興味のある人には手前味噌ではございますがオススメでございます。



以上、著者から報告でした。何卒よろしくお願いいたします。


p.s. ちなみに私、IQで女子高生に負けました。
