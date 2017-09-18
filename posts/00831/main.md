---
Keywords:プログラミング,Haskell,pmat
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->pmat version 0.0015<!--:-->
<!--:ja-->行列演算コマンドの件です。やっと電卓らしくなってきました。計算結果が正しいかどうかすぐに判別できなくなってきました・・・。<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/00fbc2e60cfeb84f011da397a652633c7034954b/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/00fbc2e60cfeb84f011da397a652633c7034954b/pmat.hs</a><br />
<br />
なんとなく設計がおかしかったのでパーサの部分を大幅に書き換えました。これで多項式や逆行列の計算の実装に取りかかれます。<br />
<br />
[bash]<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data <br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
C 2 3<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=A*B*C*A&quot;<br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
C 2 3<br />
D 20.0 40.0 60.0<br />
D 20.0 40.0 60.0<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=2*A*B*C*A&quot;<br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
C 2 3<br />
D 40.0 80.0 120.0<br />
D 40.0 80.0 120.0<br />
ueda\@ubuntuX201:~/GIT/PMAT$ cat data | ./pmat &quot;D=A*B*C*A&quot; | ./pmat &quot;E=2*D&quot;<br />
A 1 2 3<br />
A 1 2 3<br />
B -1<br />
B 1<br />
B 1<br />
C 2 3<br />
D 20.0 40.0 60.0<br />
D 20.0 40.0 60.0<br />
E 40.0 80.0 120.0<br />
E 40.0 80.0 120.0<br />
[/bash]<br />
<br />
やっと「パーサを書く」というのはどういうことなのかうすらぼんやり分かってきました。機械屋さんから情報屋さんへの改造人間手術は続く・・・<!--:-->
