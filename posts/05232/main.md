---
Keywords: コマンド,CLI,寝る,研究,シェル芸,バイナリシェル芸,遊んでいるわけではない
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記（シェル芸で1バイトより小さいデータを扱うことを強要されて死ぬ）
バイナリのファイルを縮めるという苦行をせざるを得なかったので、日記にしたためて自分を供養。シェル芸勉強会のような感じで。

<h1>問題</h1>
次のようなバイナリの1バイトごとに「-1」、「0」、「1」、「2」という数字がchar型で入っています。

-1, 0, 1, 2の4種類しかデータがないので、1バイト（8ビット）ではなくて2ビットで十分なので、1バイトを2ビットにしてデータを詰めてください。-1を00、0を01、1を10、2を11で表現します。

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | head
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffff01ffff0000ff010001
ffff010001ffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffff01010100010101000000ff01ff00000000ffff01
010101000000ffffffff01010100ffff000000ffffffffffffffffffff00
ffffffffffffffff0000ff000100ffff0000ffff0000ffffffffffffffff
ffffffffffffffffffff00ffff0000ffff0001010000ffff010100010100
ffffff0101ff01010101ff01010101010001010101ffffff000101010101
[/bash]

うーん。プログラム書くほどでもないよなあ・・・。（いや、普通書くけど。）

<!-- more -->
<h2>解答</h2>

ということでワンライナーで解答します。Macで作りました。coreutilsを使っています。

とりあえずどんなデータがあるか確認。

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 | uniq | LANG=C sort -u 
00
01
02
ff
[/bash]

整数に変換して（1を足して）また確認。

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 | 
sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' | uniq | LANG=C sort -u
0
1
2
3
[/bash]

こいつを<a href="https://www.google.co.jp/search?q=%E3%82%88%E3%82%93%E3%82%8C%E3%81%A4&espv=2&biw=1280&bih=728&tbm=isch&tbo=u&source=univ&sa=X&ei=r3PcVNuxA4bSmAXjq4LIAw&ved=0CCAQsAQ" target="_blank">よんれつ</a>に並べ・・・（xargs -n 4でもよいが遅い。）

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' | head
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
[/bash]

2ビットずつシフトさせながら足し・・・

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' | awk '{print $1 + $2*4 + $3*16 + $4*64}' | less
...
0
0
0
106
106
133
84
129
106
5
160
...
[/bash]

16進数に再び変換。awkのprintfで"%x"でなく"%02x"としないと桁がずれるので注意。（というかちょっと嵌った。）

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' |
 awk '{print $1 + $2*4 + $3*16 + $4*64}' | gawk '{printf(&quot;%02x&quot;,$1)}' | head -c 200
000000000000000000000000000000000000000000000000000000805098600200000000000000006a6a
8554816a05a006150000040050645050000000001014a4059a0628aaa89a2a90aa1a900615a056000000
00000000000000000000000000000000uedambp:dat ueda$
[/bash]

最後にxxdで戻す。

[bash]
uedambp:dat ueda$ xxd -ps policy.dat | gfold -b2 |
 sed -e 's/ff/0/' -e 's/00/1/' -e 's/01/2/' -e 's/02/3/' |
 awk 'NR%4==0{print $1}NR%4!=0{printf $1&quot; &quot;}' |
 awk '{print $1 + $2*4 + $3*16 + $4*64}' | gawk '{printf(&quot;%02x&quot;,$1)}' |
 xxd -r -ps &gt; policy.bin 
[/bash]

・・・たぶんこれでOKか・・・。8ビットに戻してからパックしているので、データ読み出すときに<a href="http://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3" target="_blank">バイトオーダ</a>はたぶん気にしなくてよいだろう。たぶん。

<span style="color:red">ね？簡単でしょ？</span>

・・・簡単じゃねーよ。すぐ終わったけど。


寝る。
