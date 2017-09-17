# LaTeXで論文を書くときに使ったシェル芸のメモ
一昨日提出したので息抜きにメモを書いておきます。来週から別テーマでシミュレータを作ります。たぶんC++で・・・。修行だ・・・。<br />
<br />
<h2>文字数カウント</h2><br />
<br />
ページ数でなくて単語数を制限するジャーナル（英文）だったので、手元のMacで作った原稿をLinuxのVPSにアップして、lessでテキストに変換し、wcでカウント。TeXの原稿をそのままwcするとコメントアウトしたものとかヘッダとかいろいろあるのでPDFから行った方が単語数が少なくなる。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
###アップロード###<br />
server:hoge_journal ueda$ scp hoge_journal.pdf test.usptomo.com:~/<br />
ar_prob_flow.pdf 100% 438KB 437.9KB/s 00:00<br />
###ログイン###<br />
server:hoge_journal ueda$ ssh test.usptomo.com<br />
Last login: Thu Aug 7 16:33:50 2014 from r.aiit.ac.jp<br />
###PDFをlessで読むためにpopplerをインストール###<br />
ueda\@remote:~$ sudo apt-get install poppler-utils<br />
###こうするとlessでPDFが読める###<br />
###そしてlessの後ろには実はパイプをつけることができる###<br />
ueda\@remote:~$ less ar_prob_flow.pdf | tail<br />
 [16] Lenser S, Veloso M. Sensor resetting localization for poorly modelled robots. In: Proc. of IEEE ICRA;<br />
 2000. p. 1225–1232.<br />
 [17] Ueda R, et al. Expansion Resetting for Recovery from Fatal Error in Monte Carlo Localization –<br />
 Comparison with Sensor Resetting Methods. In: Proc. of IROS; 2004. p. 2481–2486.<br />
<br />
<br />
<br />
<br />
 15<br />
###ということでwcで単語数がわかる###<br />
ueda\@remote:~$ less ar_prob_flow.pdf | wc<br />
 807 6065 50879<br />
[/bash]<br />
<br />
数式とかがあるのでざっくりとした計算になりますが・・・。<br />
<br />
<h2>LaTeXの原稿から表と図をコメントアウト</h2><br />
<br />
図を抜いたpdf作ってワード数をカウントしろと言われたので・・・。めんどくせー。<br />
<br />
sedで範囲指定の上、置換をします。どの記号をエスケープしなければいけないか、細かい知識が必要ですが、別にトライアンドエラーでやっても手でやるよりは早く終わるでしょう。<br />
<br />
[bash]<br />
uedambp:AR_PROB_FLOW ueda$ cat ar_prob_flow.tex |<br />
 sed '/\\\\begin{table/,/\\\\end{table/s/^/%/' |<br />
 sed '/\\\\begin{figure/,/\\\\end{figure/s/^/%/' | less<br />
...<br />
This distribution is obtained at a trial in Sec. \\ref{sub:behavior}.<br />
<br />
<br />
%\\begin{figure}[h]<br />
% \\begin{center}<br />
% \\includegraphics[width=0.5\\lin（略）<br />
% \\caption{A distribution of pa（略）<br />
% \\label{fig:particles}<br />
% \\end{center}<br />
%\\end{figure}<br />
<br />
At the beginning of each trial,<br />
...<br />
[/bash]<br />
<br />
<h2>aspellでスペルチェック</h2><br />
<br />
これはシェル芸ではありませんが・・・。<br />
<br />
英文のスペルチェックをするときは頭にLANG=Cをつけましょう。<br />
（なにかaspellの設定をいじれば扶養かもしれませんが。）<br />
<br />
[bash]<br />
server:hoge_journal ueda$ LANG=C aspell -c hoge_journal.tex<br />
[/bash]<br />
<br />
<br />
あんまり長いワンライナーではありませんが、こういう日常で使うものこそシェル芸ですので、特に研究者の皆さんは使えるようになっておきたいところです。
