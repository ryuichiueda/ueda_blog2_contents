# <!--:ja--> ファイル名にメモをとると便利だと思うんだが。<!--:-->
<!--:ja-->今朝、Facebookに、私がたまにやってしまう「ファイル名にメモをとる行為」について質問しました。<br />
<br />
<hr /><br />
こういうふうに、ファイル名でメモとる人います？？<br />
<br />
[bash]<br />
$ ls -l<br />
total 104<br />
-rwxr-xr-x 1 ueda staff 39887 2 17 10:17 20140301会合.xlsx<br />
-rw-r--r-- 1 ueda staff 58368 2 17 10:09 ○×会告Ver2.doc<br />
-rw-r--r-- 1 ueda staff 0 2 17 10:21 memo.参加費用は1万<br />
[/bash]<br />
<br />
<hr /><br />
<br />
関係者の心の琴線に触れたらしく、即以下のようなフィードバックがありました。<br />
<br />
<ul><br />
	<li>やっている。（by こわいおねーさん）</li><br />
	<li>特殊な記号等が混ざると面倒なので最近あまりしない。（by おじさん）</li><br />
 <li>ファイル名に日本語なんか使わない！（by おじさま）</li><br />
	<li>todoをよく書く（by おにいさま）</li><br />
</ul><br />
<br />
おじさまたちは(じゃあ特殊記号使うな|英語でメモ取れ)ということで、おおかたやっている人が多いという結論になりました。<br />
<br />
ちなみにやり方ですが、<br />
<br />
[bash]<br />
uedambp:SCI2014 ueda$ touch &quot;3月14日まで6ページか8ページ&quot;<br />
uedambp:SCI2014 ueda$ ls<br />
3月14日まで6ページか8ページ sci.sty sci2014.dvi sci2014.pdf<br />
Makefile sci2014.aux sci2014.log sci2014.tex<br />
[/bash]<br />
<br />
と、touchコマンドを使うのが普通かと。<br />
<br />
<br />
仕事中なので、これにて。肩が凝る。<!--:-->
