---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.021<!--:--><!--:en-->pmat version 0.021<!--:-->
<!--:ja-->jusの総会・イベントで話を聞きながら手を自動的に動かしています。内職ではありません。一種のオートパイロットです。<br />
<br />
<a href="https://github.com/ryuichiueda/PMAT/blob/9c173c8c2092b06a0acae54a060101ab6834bdeb/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/9c173c8c2092b06a0acae54a060101ab6834bdeb/pmat.hs</a><br />
<br />
コードの合理化、逆行列・ベキ乗の実装と一気に進んだのでバージョンを0.02に引き上げ。しかし、ポカをやっちまったので現在0.021。<br />
<br />
[bash]<br />
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A^-1&quot; | ./pmat &quot;B^2*A^2+A&quot; | marume 2.1 3.1 4.1<br />
A 1.0 2.0 1.0<br />
A 2.0 1.0 0.0<br />
A 1.0 1.0 2.0<br />
B -0.4 0.6 0.2<br />
B 0.8 -0.2 -0.4<br />
B -0.2 -0.2 0.6<br />
B^2*A^2+A 2.0 2.0 1.0<br />
B^2*A^2+A 2.0 2.0 0.0<br />
B^2*A^2+A 1.0 1.0 3.0<br />
[/bash]<br />
<br />
もうPCの電池がないのでさやうなら。<!--:-->
