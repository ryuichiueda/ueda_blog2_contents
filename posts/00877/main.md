---
Keywords: Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.0020<!--:--><!--:en-->pmat version 0.0020<!--:-->
<!--:ja-->今日も酔っ払って帰って来てプログラミング。「アンタも好きね」と言われてもしょうがない状態。

コードがおかしかった（式の評価をやっている関数の射影先がすべて IO() だった）ので書き直した。
なんかしらないうちに多項式が自由に計算できるように実装していた。

<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/2c4c43c09805ee5728dabbc6e16fe6dcaee52296/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/2c4c43c09805ee5728dabbc6e16fe6dcaee52296/pmat.hs</a>

が、コードがもはやわけがわからん・・・。

```bash
uedamac:PMAT ueda$ cat data 
A 0 1
A 1 0
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A*2&quot; | ./pmat &quot;C=B+2*A+A*A*A&quot;
A 0 1
A 1 0
B 0.0 2.0
B 2.0 0.0
C 0.0 5.0
C 5.0 0.0
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A*2&quot; | ./pmat &quot;C=B+2*A*A+A*A*A&quot;
A 0 1
A 1 0
B 0.0 2.0
B 2.0 0.0
C 2.0 3.0
C 3.0 2.0
```

壁にぶつかっているかもしれん。ていうかコメント入れようぜ俺。


おやじ！もう一杯ビール！<!--:-->
