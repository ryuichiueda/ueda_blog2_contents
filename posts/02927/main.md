---
Keywords: CLI,docx,シェル芸,エクシェル芸,ワードシェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# ワードシェル芸？の方法。
もう、やり方だけ。環境はUbuntu。hxselectで要素を指定するときに、コロンをエスケープするというのでちょっとはまった。

```bash
###docxことzipファイルの中はこんな感じ。###
###文章の内容はword/document.xml###
###画像はjpegがそのまま入っている###
Archive: self_introduction.docx
 Length Date Time Name
--------- ---------- ----- ----
 1871 1980-01-01 00:00 [Content_Types].xml
 590 1980-01-01 00:00 _rels/.rels
 1484 1980-01-01 00:00 word/_rels/document.xml.rels
 4835 1980-01-01 00:00 word/document.xml
 1789 1980-01-01 00:00 word/footnotes.xml
 1783 1980-01-01 00:00 word/endnotes.xml
 21556 1980-01-01 00:00 word/media/image1.jpeg
 7561 1980-01-01 00:00 word/theme/theme1.xml
 4193 1980-01-01 00:00 word/settings.xml
 49341 1980-01-01 00:00 word/stylesWithEffects.xml
 48475 1980-01-01 00:00 word/styles.xml
 1021 1980-01-01 00:00 docProps/app.xml
 3484 1980-01-01 00:00 word/fontTable.xml
 8773 1980-01-01 00:00 word/numbering.xml
 871 1980-01-01 00:00 word/webSettings.xml
 713 1980-01-01 00:00 docProps/core.xml
--------- -------
 158340 16 files
###おりゃ###
ueda\@remote:~$ unzip -p self_introduction.docx word/document.xml | hxselect 'w\\:t' | sed 's;</w:t&gt;;&amp;\\n;g'
<w:t&gt;自己紹介</w:t&gt;
<w:t xml:space=&quot;preserve&quot;&gt; </w:t&gt;
<w:t&gt;【氏名】漢字）上田　隆一</w:t&gt;
<w:t xml:space=&quot;preserve&quot;&gt;　　　　ローマ字）</w:t&gt;
<w:t&gt;Ryuichi Ueda</w:t&gt;
###画像はふつうに抽出###
ueda\@remote:~$ unzip self_introduction.docx word/media/image1.jpeg
Archive: self_introduction.docx
 extracting: word/media/image1.jpeg 
```


以上。わーどうしましょう。
