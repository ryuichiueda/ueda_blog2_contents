---
Keywords:CLI,docx,シェル芸,エクシェル芸,ワードシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# ワードシェル芸？の方法。
もう、やり方だけ。環境はUbuntu。hxselectで要素を指定するときに、コロンをエスケープするというのでちょっとはまった。<br />
<br />
[bash]<br />
###docxことzipファイルの中はこんな感じ。###<br />
###文章の内容はword/document.xml###<br />
###画像はjpegがそのまま入っている###<br />
Archive: self_introduction.docx<br />
 Length Date Time Name<br />
--------- ---------- ----- ----<br />
 1871 1980-01-01 00:00 [Content_Types].xml<br />
 590 1980-01-01 00:00 _rels/.rels<br />
 1484 1980-01-01 00:00 word/_rels/document.xml.rels<br />
 4835 1980-01-01 00:00 word/document.xml<br />
 1789 1980-01-01 00:00 word/footnotes.xml<br />
 1783 1980-01-01 00:00 word/endnotes.xml<br />
 21556 1980-01-01 00:00 word/media/image1.jpeg<br />
 7561 1980-01-01 00:00 word/theme/theme1.xml<br />
 4193 1980-01-01 00:00 word/settings.xml<br />
 49341 1980-01-01 00:00 word/stylesWithEffects.xml<br />
 48475 1980-01-01 00:00 word/styles.xml<br />
 1021 1980-01-01 00:00 docProps/app.xml<br />
 3484 1980-01-01 00:00 word/fontTable.xml<br />
 8773 1980-01-01 00:00 word/numbering.xml<br />
 871 1980-01-01 00:00 word/webSettings.xml<br />
 713 1980-01-01 00:00 docProps/core.xml<br />
--------- -------<br />
 158340 16 files<br />
###おりゃ###<br />
ueda\@remote:~$ unzip -p self_introduction.docx word/document.xml | hxselect 'w\\:t' | sed 's;&lt;/w:t&gt;;&amp;\\n;g'<br />
&lt;w:t&gt;自己紹介&lt;/w:t&gt;<br />
&lt;w:t xml:space=&quot;preserve&quot;&gt; &lt;/w:t&gt;<br />
&lt;w:t&gt;【氏名】漢字）上田　隆一&lt;/w:t&gt;<br />
&lt;w:t xml:space=&quot;preserve&quot;&gt;　　　　ローマ字）&lt;/w:t&gt;<br />
&lt;w:t&gt;Ryuichi Ueda&lt;/w:t&gt;<br />
###画像はふつうに抽出###<br />
ueda\@remote:~$ unzip self_introduction.docx word/media/image1.jpeg<br />
Archive: self_introduction.docx<br />
 extracting: word/media/image1.jpeg <br />
[/bash]<br />
<br />
<br />
以上。わーどうしましょう。
