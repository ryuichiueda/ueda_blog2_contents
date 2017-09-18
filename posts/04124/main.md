---
Keywords:コマンド,iPhone,LaTeX,Mac,make,寝る,脱キーボード,腰痛持ちに捧ぐ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 布団の中でiPhoneを使ってLaTeXの文章を書く手法の提案
いつまで人類は机に向かってキーボードを叩いているんだ！ということで、布団でLaTeXの原稿を書く方法（Mac + iPhone）を。なんか有料のものもあるらしいですが・・・ここに書いてある方法はダーターです。<br />
<br />
こちらの記事の内容を参考にアレンジしたものです。<br />
<br />
<a href="http://tomhus.blogspot.jp/2011/02/ipadlatex.html" target="_blank">iPadでLaTeXを！！　| Another Tomhus</a><br />
<br />
<br />
まず、MacからDropBoxにLaTeX原稿一式を置きます。<span style="color:red">もう、研究者仲間には何を書いているのかバレバレですね。</span><br />
<br />
[bash]<br />
uedambp:Dropbox ueda$ ls -d H27_KAKEN/<br />
H27_KAKEN/<br />
uedambp:Dropbox ueda$ ls H27_KAKEN/*.tex<br />
H27_KAKEN/blahblah.tex H27_KAKEN/kiban_c_08_past_funds.tex<br />
...<br />
[/bash]<br />
<br />
このディレクトリの中にMakefileを準備します。ポイントは、platexのオプションに-halt-on-errorを書いておく事です。これが無いとエラーがあったらiPhone側からはどうする事もできません。<br />
<br />
[bash]<br />
uedambp:Dropbox ueda$ cat H27_KAKEN/Makefile <br />
h27_kiban_c.pdf: h27_kiban_c.dvi<br />
	dvipdfmx h27_kiban_c.dvi<br />
<br />
h27_kiban_c.dvi: *.tex<br />
	platex -halt-on-error h27_kiban_c.tex<br />
	platex -halt-on-error h27_kiban_c.tex<br />
<br />
clean:<br />
<br />
	rm -f *.dvi *.aux<br />
[/bash]<br />
<br />
ここでシェル芸。5秒に一回makeします。<br />
<br />
[bash]<br />
uedambp:Dropbox ueda$ cd H27_KAKEN/<br />
uedambp:H27_KAKEN ueda$ while sleep 5 ; do make ;done<br />
make: `h27_kiban_c.pdf' is up to date.<br />
make: `h27_kiban_c.pdf' is up to date.<br />
[/bash]<br />
<br />
あとは、<a href="https://itunes.apple.com/jp/app/plaintext-2/id769101727?mt=8" target="_blank">PlainText 2</a>か何かでtexファイルを編集します。pdfはiPhoneのDropBoxで確認すればよいでしょう。あ、iPhone側にもDropBoxが必要ですね。<br />
<br />
<s>問題は、「pdfが更新されない」ということからエラーを察知しなければならないことです。初心者には辛いかもしれません。何か改善策があれば\@ryuichiuedaまでご報告を。</s><br />
↑DropBoxからLaTeXの吐いたログ見ればいいですね。<br />
<br />
<br />
さて、寝る。書く。とほほ。<br />
<br />
<br />
<br />

