---
Keywords:コマンド,CLI,寝る,研究,シェル芸,バイナリシェル芸,遊んでいるわけではない
Copyright: (C) 2017 Ryuichi Ueda
---
# 日記（シェル芸で1バイトより小さいデータを扱うことを強要されて死ぬ）
バイナリのファイルを縮めるという苦行をせざるを得なかったので、日記にしたためて自分を供養。シェル芸勉強会のような感じで。<br />
<br />
<h1>問題</h1><br />
次のようなバイナリの1バイトごとに「-1」、「0」、「1」、「2」という数字がchar型で入っています。<br />
<br />
-1, 0, 1, 2の4種類しかデータがないので、1バイト（8ビット）ではなくて2ビットで十分なので、1バイトを2ビットにしてデータを詰めてください。-1を00、0を01、1を10、2を11で表現します。<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | head<br />
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff<br />
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff<br />
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff<br />
ffffffffffffffffffffffffffffffffffffffffff01ffff0000ff010001<br />
ffff010001ffffffffffffffffffffffffffffffffffffffffffffffffff<br />
ffffffffffffffffffff01010100010101000000ff01ff00000000ffff01<br />
010101000000ffffffff01010100ffff000000ffffffffffffffffffff00<br />
ffffffffffffffff0000ff000100ffff0000ffff0000ffffffffffffffff<br />
ffffffffffffffffffff00ffff0000ffff0001010000ffff010100010100<br />
ffffff0101ff01010101ff01010101010001010101ffffff000101010101<br />
[/bash]<br />
<br />
うーん。プログラム書くほどでもないよなあ・・・。（いや、普通書くけど。）<br />
<br />
<!-- more --><br />
<h2>解答</h2><br />
<br />
ということでワンライナーで解答します。Macで作りました。coreutilsを使っています。<br />
<br />
とりあえずどんなデータがあるか確認。<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 | uniq | LANG=C sort -u <br />
00<br />
01<br />
02<br />
ff<br />
[/bash]<br />
<br />
整数に変換して（1を足して）また確認。<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 | <br />
sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' | uniq | LANG=C sort -u<br />
0<br />
1<br />
2<br />
3<br />
[/bash]<br />
<br />
こいつを<a href="https://www.google.co.jp/search?q=%E3%82%88%E3%82%93%E3%82%8C%E3%81%A4&espv=2&biw=1280&bih=728&tbm=isch&tbo=u&source=univ&sa=X&ei=r3PcVNuxA4bSmAXjq4LIAw&ved=0CCAQsAQ" target="_blank">よんれつ</a>に並べ・・・（xargs -n 4でもよいが遅い。）<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |<br />
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |<br />
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' | head<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
0 0 0 0<br />
[/bash]<br />
<br />
2ビットずつシフトさせながら足し・・・<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |<br />
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |<br />
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' | awk '{print $1 + $2*4 + $3*16 + $4*64}' | less<br />
...<br />
0<br />
0<br />
0<br />
106<br />
106<br />
133<br />
84<br />
129<br />
106<br />
5<br />
160<br />
...<br />
[/bash]<br />
<br />
16進数に再び変換。awkのprintfで"%x"でなく"%02x"としないと桁がずれるので注意。（というかちょっと嵌った。）<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |<br />
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |<br />
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' |<br />
 awk '{print $1 + $2*4 + $3*16 + $4*64}' | gawk '{printf(&quot;%02x&quot;,$1)}' | head -c 200<br />
000000000000000000000000000000000000000000000000000000805098600200000000000000006a6a<br />
8554816a05a006150000040050645050000000001014a4059a0628aaa89a2a90aa1a900615a056000000<br />
00000000000000000000000000000000uedambp:dat ueda$<br />
[/bash]<br />
<br />
最後にxxdで戻す。<br />
<br />
[bash]<br />
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |<br />
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |<br />
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' |<br />
 awk '{print $1 + $2*4 + $3*16 + $4*64}' | gawk '{printf(&quot;%02x&quot;,$1)}' |<br />
 xxd -r -ps &gt; policy.bin <br />
[/bash]<br />
<br />
・・・たぶんこれでOKか・・・。8ビットに戻してからパックしているので、データ読み出すときに<a href="http://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3" target="_blank">バイトオーダ</a>はたぶん気にしなくてよいだろう。たぶん。<br />
<br />
<span style="color:red">ね？簡単でしょ？</span><br />
<br />
・・・簡単じゃねーよ。すぐ終わったけど。<br />
<br />
<br />
寝る。
