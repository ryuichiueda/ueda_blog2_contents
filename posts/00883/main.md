---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.021<!--:--><!--:en-->pmat version 0.021<!--:-->
<!--:ja-->jusの総会・イベントで話を聞きながら手を自動的に動かしています。内職ではありません。一種のオートパイロットです。

<a href="https://github.com/ryuichiueda/PMAT/blob/9c173c8c2092b06a0acae54a060101ab6834bdeb/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/9c173c8c2092b06a0acae54a060101ab6834bdeb/pmat.hs</a>

コードの合理化、逆行列・ベキ乗の実装と一気に進んだのでバージョンを0.02に引き上げ。しかし、ポカをやっちまったので現在0.021。

```bash
uedamac:PMAT ueda$ cat data | ./pmat "B=A^-1" | ./pmat "B^2*A^2+A" | marume 2.1 3.1 4.1
A 1.0 2.0 1.0
A 2.0 1.0 0.0
A 1.0 1.0 2.0
B -0.4 0.6 0.2
B 0.8 -0.2 -0.4
B -0.2 -0.2 0.6
B^2*A^2+A 2.0 2.0 1.0
B^2*A^2+A 2.0 2.0 0.0
B^2*A^2+A 1.0 1.0 3.0
```

もうPCの電池がないのでさやうなら。<!--:-->
