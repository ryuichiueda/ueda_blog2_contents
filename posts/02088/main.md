---
Keywords: CLI,Mac,touch,ファイル名にメモをとる行為
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja--> ファイル名にメモをとると便利だと思うんだが。<!--:-->
<!--:ja-->今朝、Facebookに、私がたまにやってしまう「ファイル名にメモをとる行為」について質問しました。

<hr />
こういうふうに、ファイル名でメモとる人います？？

[bash]
$ ls -l
total 104
-rwxr-xr-x 1 ueda staff 39887 2 17 10:17 20140301会合.xlsx
-rw-r--r-- 1 ueda staff 58368 2 17 10:09 ○×会告Ver2.doc
-rw-r--r-- 1 ueda staff 0 2 17 10:21 memo.参加費用は1万
[/bash]

<hr />

関係者の心の琴線に触れたらしく、即以下のようなフィードバックがありました。

<ul>
	<li>やっている。（by こわいおねーさん）</li>
	<li>特殊な記号等が混ざると面倒なので最近あまりしない。（by おじさん）</li>
 <li>ファイル名に日本語なんか使わない！（by おじさま）</li>
	<li>todoをよく書く（by おにいさま）</li>
</ul>

おじさまたちは(じゃあ特殊記号使うな|英語でメモ取れ)ということで、おおかたやっている人が多いという結論になりました。

ちなみにやり方ですが、

[bash]
uedambp:SCI2014 ueda$ touch &quot;3月14日まで6ページか8ページ&quot;
uedambp:SCI2014 ueda$ ls
3月14日まで6ページか8ページ sci.sty sci2014.dvi sci2014.pdf
Makefile sci2014.aux sci2014.log sci2014.tex
[/bash]

と、touchコマンドを使うのが普通かと。


仕事中なので、これにて。肩が凝る。<!--:-->
