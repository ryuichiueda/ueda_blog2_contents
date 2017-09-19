---
Keywords: コマンド,CLI,LaTeX,Linux,Mac,make,Makefile,pLaTeX,sed,執筆,横書きにおけるカンマピリオド問題
Copyright: (C) 2017 Ryuichi Ueda
---

# やっと論文の「, . 」と、その他原稿の「、。 」を使い分ける（自分にとっての）究極の方法を見つけた
ここ数年の問題が解決しました。こうやれば良かったんです。何故気付かなかったのか。
<blockquote class="twitter-tweet" lang="ja">
<p lang="ja" dir="ltr">Makefileにsedぶちこんで「、。」の問題を解決。</p>
rsj2015.dvi: *.tex
sed -i.bak -e 's/。/. /g' -e 's/、/, /g' rsj2015.tex
platex rsj2015.tex
...

— Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/614314872311037952">2015, 6月 26</a></blockquote>
<script async="" src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

研究者は普通、デフォルトで句読点を「, .」（カンマとピリオド）にしてますが、私のようなエセの場合、学術的な文章とそうでない文章が半々で使い分けないといけません。1日に何度も切り替えるのも馬鹿馬鹿しいので、普段は「、。」で書いて、論文もそのまま「、。」で書いて後でvimで変換してました。ただ、これだと論文を出すときに変換忘れをやらかしそうでなんか落ち着きません。

しかし考えてみたら、論文は必ずpLaTeXで書いてmakeしているので、上のツイートのようにMakefileに変換を仕込んでおけばよかったと。なぜ今の今まで考えつかなかったのかと。ということでMakefileを晒しておきます。コンパイル対象のファイル名を変えたらMacとかLinuxとかBSDとかで普通に使えると思います。

```bash
uedambp:RSJ2015 ueda$ cat Makefile 
rsj2015.pdf: rsj2015.dvi
	dvipdfmx -p a4 rsj2015.dvi

rsj2015.dvi: *.tex
	sed -i.bak -e 's/。/. /g' -e 's/、/, /g' rsj2015.tex
	platex rsj2015.tex
	pbibtex rsj2015.aux
	platex rsj2015.tex
	platex rsj2015.tex

clean:
	rm -f *.aux *.log *.dvi *.bbl *.blg *.pdf *.ilg *.idx *.toc *.ind
```

6行目のsedで、-i.bakで「ファイルの中身を出力で入れ替えて、拡張子.bakのバックアップファイルを作る」という意味になります。Vimから:!makeした場合だと、コンパイルが終わったらVimが「編集中にファイルが変わっちまった」とワーニングを出すので、再ロードして変更を読み込みます。

ところで、こういう話は「、。」と「, .」どっちが正しいという炎上案件になりがちですが、ここではそういう議論はしません。誰が何を言おうと論文のフォーマットとして句読点を「,.」で出せと言ってくるわけでして、それに従順に従っているにすぎません。

ところで、rst2015.texとう名前の通り、そういう学会に向けて何か書いておるわけですが、まだ書けてません。期限が延長されてよかったよかった・・・。
