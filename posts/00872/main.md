---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.0019<!--:--><!--:en-->pmat version 0.0019<!--:-->
<!--:ja-->飲み会から帰り、酔っ払ってコードをいじっているうちに足し算引き算ができるようになりました。<br />
<br />
<a href="https://github.com/ryuichiueda/PMAT/blob/c71f5b9488c363b2bba5f9e370bf645c9e7c334a/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/c71f5b9488c363b2bba5f9e370bf645c9e7c334a/pmat.hs</a><br />
<br />
[bash]<br />
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A+A&quot; | ./pmat &quot;C=B+A&quot; | ./pmat &quot;D=B-A&quot;<br />
A 0 1<br />
A 1 0<br />
B 0.0 2.0<br />
B 2.0 0.0<br />
C 0.0 3.0<br />
C 3.0 0.0<br />
D 0.0 1.0<br />
D 1.0 0.0<br />
[/bash]<br />
<br />
でもコードが汚くなり、"2*A+B" みたいな計算もまだできません。<br />
<br />
<br />
局所的に設計しなおさないとスパゲッティーになるな・・・。<br />
<br />
<br />
しかし、もうアルコールで何がなんだかよく分からないので、寝る。<!--:-->
