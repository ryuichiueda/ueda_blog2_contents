---
Keywords: CLI,PDFシェル芸,poppler,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# LaTeXで論文を書くときに使ったシェル芸のメモ
一昨日提出したので息抜きにメモを書いておきます。来週から別テーマでシミュレータを作ります。たぶんC++で・・・。修行だ・・・。

<h2>文字数カウント</h2>

ページ数でなくて単語数を制限するジャーナル（英文）だったので、手元のMacで作った原稿をLinuxのVPSにアップして、lessでテキストに変換し、wcでカウント。TeXの原稿をそのままwcするとコメントアウトしたものとかヘッダとかいろいろあるのでPDFから行った方が単語数が少なくなる。

<!--more-->

```bash
###アップロード###
server:hoge_journal ueda$ scp hoge_journal.pdf test.usptomo.com:~/
ar_prob_flow.pdf 100% 438KB 437.9KB/s 00:00
###ログイン###
server:hoge_journal ueda$ ssh test.usptomo.com
Last login: Thu Aug 7 16:33:50 2014 from r.aiit.ac.jp
###PDFをlessで読むためにpopplerをインストール###
ueda@remote:~$ sudo apt-get install poppler-utils
###こうするとlessでPDFが読める###
###そしてlessの後ろには実はパイプをつけることができる###
ueda@remote:~$ less ar_prob_flow.pdf | tail
 [16] Lenser S, Veloso M. Sensor resetting localization for poorly modelled robots. In: Proc. of IEEE ICRA;
 2000. p. 1225–1232.
 [17] Ueda R, et al. Expansion Resetting for Recovery from Fatal Error in Monte Carlo Localization –
 Comparison with Sensor Resetting Methods. In: Proc. of IROS; 2004. p. 2481–2486.




 15
###ということでwcで単語数がわかる###
ueda@remote:~$ less ar_prob_flow.pdf | wc
 807 6065 50879
```

数式とかがあるのでざっくりとした計算になりますが・・・。

<h2>LaTeXの原稿から表と図をコメントアウト</h2>

図を抜いたpdf作ってワード数をカウントしろと言われたので・・・。めんどくせー。

sedで範囲指定の上、置換をします。どの記号をエスケープしなければいけないか、細かい知識が必要ですが、別にトライアンドエラーでやっても手でやるよりは早く終わるでしょう。

```bash
uedambp:AR_PROB_FLOW ueda$ cat ar_prob_flow.tex |
 sed '/\\\\begin{table/,/\\\\end{table/s/^/%/' |
 sed '/\\\\begin{figure/,/\\\\end{figure/s/^/%/' | less
...
This distribution is obtained at a trial in Sec. \\ref{sub:behavior}.


%\\begin{figure}[h]
% \\begin{center}
% \\includegraphics[width=0.5\\lin（略）
% \\caption{A distribution of pa（略）
% \\label{fig:particles}
% \\end{center}
%\\end{figure}

At the beginning of each trial,
...
```

<h2>aspellでスペルチェック</h2>

これはシェル芸ではありませんが・・・。

英文のスペルチェックをするときは頭にLANG=Cをつけましょう。
（なにかaspellの設定をいじれば扶養かもしれませんが。）

```bash
server:hoge_journal ueda$ LANG=C aspell -c hoge_journal.tex
```


あんまり長いワンライナーではありませんが、こういう日常で使うものこそシェル芸ですので、特に研究者の皆さんは使えるようになっておきたいところです。
