---
Keywords: プログラミング,数値計算,行列,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# こういう行列計算コマンドを考えついた
「行列をコマンドで計算したい」ということなのですが、なかなか標準入出力の考えになじむものが思いつかずにいました。

これで解決？

```bash
$ cat inputfile
A 1 2
A 3 4
B 4 3
B 2 1
$ matcalc A*B inputfile
A 1 2
A 3 4
B 4 3
B 2 1
A*B 8 5
A*B 20 13
$ matcalc C=A*B inputfile
A 1 2
A 3 4
B 4 3
B 2 1
C 8 5
C 20 13
```

地味に便利。自分には・・・

もちろん入力した行列もそのまま出力するのはパイプで多段につなぐためです。
