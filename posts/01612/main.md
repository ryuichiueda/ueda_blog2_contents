---
Keywords: CLI,csv,Excel,Mac,nkf,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->Macの端末でcsvを作ってマウスを使わずにExcelで開く手順<!--:-->
<!--:ja-->上田です．絶賛逃避行動中です．

今，このようなCSVをvimで作ったのですが，これをマウスをクリクリしてインポートするのが馬場馬鹿しいので，端末で開こうとしています．折角なので手順をメモ．といっても2ステップですが．

```bash
uedamac:MEMO ueda$ cat hoge
978-4627826618,強化学習,Richard S.Sutton,森北出版 (2000/12)
978-4621061220,パターン認識と機械学習 上,C.M. ビショップ,丸善出版 (2012/4/5)
978-4621061244,パターン認識と機械学習 下,C.M. ビショップ,丸善出版 (2012/2/29)
978-4627000797,動的計画法（POD版）,鍋島 一郎,森北出版; POD版 (2005/5/1)
978-4434078750,ルベーグ積分入門-使うための理論と演習,吉田 伸生,遊星社 (2006/05)
978-4000078160,確率論,伊藤 清,岩波書店 (1991/5/30)
978-0471727828,Markov Decision Processes: Discrete Stochastic Dynamic Programming (Wiley Series in Probability and Statistics),Martin L. Puterman,Wiley-Interscience; 1版 (2005/3/3)
```

まず，nkfでShift_JISにしてファイルに書き出します．拡張子はcsvにします．

```bash
uedamac:MEMO ueda$ cat hoge | nkf -sLwx > hoge.csv
```

次に，openします．

```bash
uedamac:MEMO ueda$ open hoge.csv 
```

これでExcelが開きます．nkfでShift_JISにするのが肝ですね．

<a href="スクリーンショット-2013-11-20-13.01.14.png"><img src="スクリーンショット-2013-11-20-13.01.14-300x93.png" alt="スクリーンショット 2013-11-20 13.01.14" width="300" height="93" class="aligncenter size-medium wp-image-1614" /></a>


・・・論文書きに戻ります．
<!--:-->
