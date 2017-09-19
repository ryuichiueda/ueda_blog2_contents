---
Keywords: コマンド,CLI,ImageMagick,Linux,Mac
Copyright: (C) 2017 Ryuichi Ueda
---

# 【メモ】ImageMagick（convertコマンド）で3枚以上の画像を合成する
単なるメモですが日本語で手っ取り早いエントリーがなかったので。以下のドキュメントを読んでやってみました。

<a href="http://www.imagemagick.org/script/command-line-options.php?#evaluate-sequence" target="_blank">http://www.imagemagick.org/script/command-line-options.php?#evaluate-sequence</a>

バージョンはこれです。Macでやってます。

[bash]
$ convert --version
Version: ImageMagick 6.9.2-3 Q16 x86_64 2015-10-06 http://www.imagemagick.org
Copyright: Copyright (C) 1999-2015 ImageMagick Studio LLC
License: http://www.imagemagick.org/script/license.php
Features: Cipher DPC Modules 
Delegates (built-in): bzlib freetype jng jpeg ltdl lzma png tiff xml zlib
[/bash]

この5枚を合成します。これもImageMagickで連結しました。（$ convert +append *.png ../a.png）

<a href="b.png" rel="attachment wp-att-7465"><img src="b.png" alt="b" width="1000" height="113" class="aligncenter size-full wp-image-7465" /></a>

実行。maxのほかにmeanとかminとかあります。

[bash]
uedamb:tmp ueda$ convert *.png -evaluate-sequence max ../a.png
[/bash]

できたのがこれ。

<a href="a.png" rel="attachment wp-att-7457"><img src="a-1024x576.png" alt="a" width="660" height="371" class="aligncenter size-large wp-image-7457" /></a>


時間を食ってしまったけどこれで論文が完成する・・・。

