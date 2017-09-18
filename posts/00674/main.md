---
Keywords:プログラミング,数値計算,行列,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---
# こういう行列計算コマンドを考えついた
「行列をコマンドで計算したい」ということなのですが、なかなか標準入出力の考えになじむものが思いつかずにいました。<br />
<br />
これで解決？<br />
<br />
[bash]<br />
$ cat inputfile<br />
A 1 2<br />
A 3 4<br />
B 4 3<br />
B 2 1<br />
$ matcalc A*B inputfile<br />
A 1 2<br />
A 3 4<br />
B 4 3<br />
B 2 1<br />
A*B 8 5<br />
A*B 20 13<br />
$ matcalc C=A*B inputfile<br />
A 1 2<br />
A 3 4<br />
B 4 3<br />
B 2 1<br />
C 8 5<br />
C 20 13<br />
[/bash]<br />
<br />
地味に便利。自分には・・・<br />
<br />
もちろん入力した行列もそのまま出力するのはパイプで多段につなぐためです。
