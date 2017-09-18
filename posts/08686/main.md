---
Keywords: Sphinx,執筆
Copyright: (C) 2017 Ryuichi Ueda
---

# 【メモ】Sphinxを使ってpLaTeX経由でPDFを作る時にdvipdfmxで「Unknown token "SDict"」と警告が出る場合の対処
原稿のトップディレクトリで<br />
[bash]<br />
make latexpdfja<br />
[/bash]<br />
した後に、_build/latex下に行き、原稿を手直しして<br />
[bash]<br />
make all-pdf-ja<br />
[/bash]<br />
すると、<br />
[bash]<br />
dvipdfmx:warning: Unknown token &quot;SDict&quot;<br />
dvipdfmx:warning: Interpreting PS code failed!!! Output might be broken!!!<br />
dvipdfmx:warning: Interpreting special command ps: (ps:) failed.<br />
dvipdfmx:warning: &gt;&gt; at page=&quot;10&quot; position=&quot;(72, 586.048)&quot; (in PDF)<br />
dvipdfmx:warning: &gt;&gt; xxx &quot;ps:SDict begin [/View [/XYZ H.V]/Dest (section.1.3) cvn /DES...&quot;<br />
（延々と続く）<br />
[/bash]<br />
という風にガーッとエラーが出ておっそい。<br />
<br />
<br />
<h2>対策</h2><br />
<br />
<a href="http://www.hnagata.net/archives/142">こちら</a>を参考に、_build/latexのsphinx.styからhyperrefに関する部分を探す。<br />
<br />
[bash]<br />
436 % Include hyperref last.<br />
437 \\RequirePackage[colorlinks,breaklinks,<br />
438 linkcolor=InnerLinkColor,filecolor=OuterLinkColor,<br />
439 menucolor=OuterLinkColor,urlcolor=OuterLinkColor,<br />
440 citecolor=InnerLinkColor]{hyperref}<br />
[/bash]<br />
で、上のリンクのように、dvipdfmxをオプションに指定。下のように[]の最後にdvipdfmxを追加。<br />
[bash]<br />
436 % Include hyperref last.<br />
437 \\RequirePackage[colorlinks,breaklinks,<br />
438 linkcolor=InnerLinkColor,filecolor=OuterLinkColor,<br />
439 menucolor=OuterLinkColor,urlcolor=OuterLinkColor,<br />
440 citecolor=InnerLinkColor,dvipdfmx]{hyperref}<br />
[/bash]<br />
で、make all-pdf-jaするとエラーが出ない。<br />
<br />
<br />
<br />
以上、ニッチすぎるメモ。
