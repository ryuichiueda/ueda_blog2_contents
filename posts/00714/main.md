---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# pmat version 0.0012
気づいたら少し進んでいた。→<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/658756a93c0716864bd275ac957bbeb9d9b8f608/pmat.hs" title="pmat.hs">GitHub晒しコード。ちょっとだけ奇麗にした。</a>

イコールで行列の名前を指示できるようになりました。これでパイプを使う利点が説明できます。

```bash
ueda\@ubuntuonmac:~/GIT/PMAT$ cat data 
A 1 2 3
A 1 2 3
B -1 2 3.0
B 1 -2 3.1
B 1 2 -3.2
ueda\@ubuntuonmac:~/GIT/PMAT$ cat data | ./pmat "C=B*B" |
./pmat "D=A*B" | ./pmat "E=D*C"
A 1 2 3
A 1 2 3
B -1 2 3.0
B 1 -2 3.1
B 1 2 -3.2
C 6.0 0.0 -6.400000000000001
C 0.10000000000000009 12.2 -13.120000000000001
C -2.2 -8.4 19.44
D 4.0 4.0 -0.40000000000000213
D 4.0 4.0 -0.40000000000000213
E 25.280000000000005 52.16000000000002 -85.85600000000005
E 25.280000000000005 52.16000000000002 -85.85600000000005
```

どんどん行列が増えていきますが、必要なものは grep か awk で取り出せます。そして消せます。便利。

```bash
ueda\@ubuntuonmac:~/GIT/PMAT$ cat data | ./pmat "C=B*B" 
| ./pmat "D=A*B" | ./pmat "E=D*C" | grep "^E "
E 25.280000000000005 52.16000000000002 -85.85600000000005
E 25.280000000000005 52.16000000000002 -85.85600000000005
```

続く。
