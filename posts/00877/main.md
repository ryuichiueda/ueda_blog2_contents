# <!--:ja-->pmat version 0.0020<!--:--><!--:en-->pmat version 0.0020<!--:-->
<!--:ja-->今日も酔っ払って帰って来てプログラミング。「アンタも好きね」と言われてもしょうがない状態。<br />
<br />
コードがおかしかった（式の評価をやっている関数の射影先がすべて IO() だった）ので書き直した。<br />
なんかしらないうちに多項式が自由に計算できるように実装していた。<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/2c4c43c09805ee5728dabbc6e16fe6dcaee52296/pmat.hs">https://github.com/ryuichiueda/PMAT/blob/2c4c43c09805ee5728dabbc6e16fe6dcaee52296/pmat.hs</a><br />
<br />
が、コードがもはやわけがわからん・・・。<br />
<br />
[bash]<br />
uedamac:PMAT ueda$ cat data <br />
A 0 1<br />
A 1 0<br />
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A*2&quot; | ./pmat &quot;C=B+2*A+A*A*A&quot;<br />
A 0 1<br />
A 1 0<br />
B 0.0 2.0<br />
B 2.0 0.0<br />
C 0.0 5.0<br />
C 5.0 0.0<br />
uedamac:PMAT ueda$ cat data | ./pmat &quot;B=A*2&quot; | ./pmat &quot;C=B+2*A*A+A*A*A&quot;<br />
A 0 1<br />
A 1 0<br />
B 0.0 2.0<br />
B 2.0 0.0<br />
C 2.0 3.0<br />
C 3.0 2.0<br />
[/bash]<br />
<br />
壁にぶつかっているかもしれん。ていうかコメント入れようぜ俺。<br />
<br />
<br />
おやじ！もう一杯ビール！<!--:-->
