---
Keywords:プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---
# <!--:ja-->pmat version 0.0014<!--:-->
<!--:ja-->まだ飽きてません。地味に進行中。<br />
<br />
<a href="https://github.com/ryuichiueda/PMAT/blob/0bdcba49010402c52ec24c06828e9ae114b60d1a/pmat.hs" target="_blank">https://github.com/ryuichiueda/PMAT/blob/0bdcba49010402c52ec24c06828e9ae114b60d1a/pmat.hs</a><br />
<br />
スカラと行列のかけ算を実装しました。スカラと行列の積は、<br />
<br />
[bash]<br />
ueda\@ubuntuX201:~$ ghci<br />
...<br />
Prelude&gt; import Numeric.LinearAlgebra<br />
...<br />
Prelude Numeric.LinearAlgebra&gt; let m = (2&gt;&lt;2) [1,2,3,4]<br />
...<br />
Prelude Numeric.LinearAlgebra&gt; m * 3.14<br />
(2&gt;&lt;2)<br />
 [ 3.14, 6.28<br />
 , 9.42, 12.56 ]<br />
[/bash]<br />
<br />
というように * で演算できるはずなんですが、ghcでコンパイルすると怒られます。<br />
<br />
仕方なく <スカラ値>*<行列> の演算時には、スカラ値を単位行列にかけた行列を作ってから、行列とかけ算するようにしました。Haskellなんで、問題が解決したら置き換えるのは簡単でしょう。<br />
<br />
実行してみます。<br />
<br />
[bash]<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data <br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;C=A*1.1&quot; | ./pmat &quot;D=B*3.14&quot;<br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
C 1.1 2.2 3.3000000000000003<br />
C 1.1 2.2 3.3000000000000003<br />
D -3.14<br />
D 3.14<br />
D 3.14<br />
[/bash]<br />
<br />
全然話違いますけど、パーサ書きの師匠がほしいなあ・・・。<br />
<br />
<br />
続く。<!--:-->
