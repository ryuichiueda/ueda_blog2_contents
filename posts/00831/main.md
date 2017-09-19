---
Keywords: プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.0015<!--:-->
<!--:ja-->行列演算コマンドの件です。やっと電卓らしくなってきました。計算結果が正しいかどうかすぐに判別できなくなってきました・・・。

<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/00fbc2e60cfeb84f011da397a652633c7034954b/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/00fbc2e60cfeb84f011da397a652633c7034954b/pmat.hs</a>

なんとなく設計がおかしかったのでパーサの部分を大幅に書き換えました。これで多項式や逆行列の計算の実装に取りかかれます。

[bash]
ueda\@ubuntuX201:~/GIT/PMAT$ cat data 
A 1 2 3
A 1 2 3
B -1
B 1
B 1
C 2 3
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=A*B*C*A&quot;
A 1 2 3
A 1 2 3
B -1
B 1
B 1
C 2 3
D 20.0 40.0 60.0
D 20.0 40.0 60.0
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=2*A*B*C*A&quot;
A 1 2 3
A 1 2 3
B -1
B 1
B 1
C 2 3
D 40.0 80.0 120.0
D 40.0 80.0 120.0
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=A*B*C*A&quot; | ./pmat &quot;E=2*D&quot;
A 1 2 3
A 1 2 3
B -1
B 1
B 1
C 2 3
D 20.0 40.0 60.0
D 20.0 40.0 60.0
E 40.0 80.0 120.0
E 40.0 80.0 120.0
[/bash]

やっと「パーサを書く」というのはどういうことなのかうすらぼんやり分かってきました。機械屋さんから情報屋さんへの改造人間手術は続く・・・<!--:-->
