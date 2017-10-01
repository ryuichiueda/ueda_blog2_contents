---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.0014<!--:-->
<!--:ja-->まだ飽きてません。地味に進行中。

<a href="https://github.com/ryuichiueda/PMAT/blob/0bdcba49010402c52ec24c06828e9ae114b60d1a/pmat.hs" target="_blank">https://github.com/ryuichiueda/PMAT/blob/0bdcba49010402c52ec24c06828e9ae114b60d1a/pmat.hs</a>

スカラと行列のかけ算を実装しました。スカラと行列の積は、

```bash
ueda@ubuntuX201:~$ ghci
...
Prelude> import Numeric.LinearAlgebra
...
Prelude Numeric.LinearAlgebra> let m = (2><2) [1,2,3,4]
...
Prelude Numeric.LinearAlgebra> m * 3.14
(2><2)
 [ 3.14, 6.28
 , 9.42, 12.56 ]
```

というように * で演算できるはずなんですが、ghcでコンパイルすると怒られます。

仕方なく <スカラ値>*<行列> の演算時には、スカラ値を単位行列にかけた行列を作ってから、行列とかけ算するようにしました。Haskellなんで、問題が解決したら置き換えるのは簡単でしょう。

実行してみます。

```bash
ueda@ubuntuX201:~/GIT/PMAT$ cat data 
A 1 2 3
A 1 2 3
B -1
B 1
B 1
ueda@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat "C=A*1.1" | ./pmat "D=B*3.14"
A 1 2 3
A 1 2 3
B -1
B 1
B 1
C 1.1 2.2 3.3000000000000003
C 1.1 2.2 3.3000000000000003
D -3.14
D 3.14
D 3.14
```

全然話違いますけど、パーサ書きの師匠がほしいなあ・・・。


続く。<!--:-->
