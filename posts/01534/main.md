---
Keywords:コマンド,シェルスクリプト,ls,寝る
Copyright: (C) 2017 Ryuichi Ueda
---
# ls -fやls -Uをもっと布教したい。
皆さん、上田です。だからなんなんだ。なんなんでしょう？<br />
<br />
この前の<a href="http://blog.ueda.asia/?page_id=684" title="シェル芸勉強会スライド一覧" target="_blank">シェル芸勉強会</a>で扱ったls -fおよびls -Uについて今一度周知徹底を。<br />
<br />
lsはけしからんコマンドです。何がけしからんか。余計なことをしすぎです。例えば、普通にディレクトリをlsすると、次のようにファイル名を横に並べます。<br />
<br />
[bash]<br />
ueda\@remote:~/work$ ls<br />
agent calendar.tbl ip referer request status time<br />
[/bash]<br />
<br />
と出てきますが、これをパイプにつなげると、<br />
<br />
[bash]<br />
ueda\@remote:~/work$ ls | cat<br />
agent<br />
calendar.tbl<br />
ip<br />
referer<br />
request<br />
status<br />
time<br />
[/bash]<br />
<br />
と縦に出てきます。私はここらへんは詳しく無いですが、lsは出力か端末に何か変な細工をしているわけです。まあこれは分からんでもありません。他のコマンドに通せば細工は消えるようですし。<br />
<br />
そして、こっちの方が問題だと思うのですが、lsはファイル名を出力するときに、頼みもしないのにソートしくさります。これも端末で人が使うならば分かる気もしますが、ディレクトリにファイルがたくさんある場合に初心者を苦しめます。100万個ファイルを作ってlsしてみましょう。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ seq 1 1000000 | xargs touch<br />
ueda\@remote:~/tmp$ ls<br />
^C<br />
<br />
[/bash]<br />
<br />
これ、Ctrl+cやってもなかなか返ってきません。ファイルシステムが絡むとすぐ中断できないことがあるのです。<br />
<br />
ちなみにちゃんと最後までやると39秒もかかります（Ubuntu 12.04 on さくらのVPS 1G）。いや、昔なら終わらなかったので39秒で終わるの凄いというところですが・・・。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ time ls <br />
（中略）<br />
189997 279997 369997 459997 549997 639997 729997 819997 909997 999998<br />
189998 279998 369998 459998 549998 639998 729998 819998 909998 999999<br />
<br />
real	0m39.805s<br />
user	0m9.233s<br />
sys	0m11.809s<br />
[/bash]<br />
<br />
ディレクトリにファイルがたくさんある状態が、すでにあまりよい状態ではありませんが、いつもUNIXを弄っているような現場だと結構あります。さてどうしたものか。<br />
<br />
もったいぶらないでさっさと答えを言うと、まず、lsの結果をファイルに出力すると速くなります。端末に表示する方は、別に表示に手間取っているわけではありません。それにしては時間がかかり過ぎです。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ time ls &gt; ~/output<br />
<br />
real	0m6.474s<br />
user	0m5.976s<br />
sys	0m0.496s<br />
[/bash]<br />
<br />
出力先が端末とファイルの場合で挙動が変わるなんて最低です。<br />
<br />
さらに速くしたいときは、ls -fかls -Uです。これでソートが切れます。ls -fだと「.」と「..」も出力されます。<br />
ls -Uだと「.」と「..」は出力されません。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ time ls -f &gt; ~/output<br />
<br />
real	0m0.620s<br />
user	0m0.264s<br />
sys	0m0.344s<br />
ueda\@remote:~/tmp$ head ~/output <br />
.<br />
..<br />
90682<br />
691133<br />
935660<br />
814634<br />
45905<br />
682037<br />
89898<br />
51703<br />
ueda\@remote:~/tmp$ time ls -U &gt; ~/output<br />
<br />
real	0m0.605s<br />
user	0m0.248s<br />
sys	0m0.352s<br />
ueda\@remote:~/tmp$ head ~/output<br />
90682<br />
691133<br />
935660<br />
814634<br />
45905<br />
682037<br />
89898<br />
51703<br />
275023<br />
594034<br />
[/bash]<br />
<br />
ソートしたけりゃsortすればいいんです。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ time ls -U | LANG=C sort &gt; ~/output<br />
<br />
real	0m1.331s<br />
user	0m1.068s<br />
sys	0m0.380s<br />
[/bash]<br />
<br />
なんだかls -fよりls -Uの方が使い勝手がよさそうですが、ところがどっこい、<span style="color:red">端末上ではls -Uは遅いので注意してください</span>。<br />
<br />
[bash]<br />
ueda\@remote:~/tmp$ time ls -U<br />
...<br />
766920 230084 666666 934457 725634 803393 94237 773567 592212 504359<br />
362385 42211 614482 679702 127511 10382 897892 247139 228008 763314<br />
<br />
real	1m25.614s<br />
user	0m3.112s<br />
sys	0m12.073s<br />
ueda\@remote:~/tmp$ time ls -f<br />
...<br />
766920 42211 224326 380819 90130 876036 702813 845513 559273<br />
<br />
real	0m16.343s<br />
user	0m1.300s<br />
sys	0m1.016s<br />
[/bash]<br />
<br />
こういう挙動不審のコマンドはあまりよろしくありません。<br />
<br />
<br />
寝る。
