---
Keywords: プログラミング,C言語,ulimit,variable
Copyright: (C) 2017 Ryuichi Ueda
---

# variable length array で配列の要素数の限界を調べた（しかしvariable length arrayあまり関係ない）
前回の variable length array、なんでそんなに自分が気持ち悪いと感じるのかと考えてみました。結果、WindowsでVisual C++を昔（4.0~6.0あたり）使っていたときに、デフォルトのスタック領域の大きさがそんなに大きくなく、<br />
<br />
[c]<br />
int aho[100000];<br />
[/c]<br />
<br />
などとすると実行時エラーが起こっていたのが遠因のようです。スタック領域はビビりながら使う物で、variable length array などとんでもないと。<br />
<br />
例えば、<a href="http://www.office-matsunaga.biz/evctips/evctips04.html" target="_blank">この</a>ページに Windows CEのケースが書いてあります。確か Windows 95, 97 で Visual C++ を使っても全く同じだったと記憶しています。<br />
<br />
しかし、もう15年以上も経っているしOSも違うので、自分の感覚は調整しないといけません。実験しましょう。なぜこのクソ忙しいのにそんなことをするのか。それは、今出ている会合がもう休み無しでもうすぐ4時間経過しようとしているからです。息抜きしないと死ぬぞこれ。<br />
<br />
まず、自分のマシーンのスタックの大きさを調べます。ulimitというコマンドで調査できます。<br />
<br />
[bash]<br />
uedamac:~ ueda$ ulimit -s<br />
8192<br />
//単位をバイトに直す。<br />
uedamac:~ ueda$ ulimit -s | awk '{print $1*1024}'<br />
8388608<br />
[/bash]<br />
<br />
ということで、int型だとだいたい 2百万くらいが配列の要素数の限界と言えそうです。<br />
<br />
次に取り出しますのは前回の気持ち悪いコードをちょっと修正したもの。<br />
<br />
[c]<br />
uedamac:~ ueda$ cat hoge.c<br />
#include &lt;stdio.h&gt;<br />
<br />
void kidding_me(size_t size)<br />
{<br />
	int nums[size];//気持ち悪い<br />
<br />
	int i;<br />
	for(i=0;i&amp;amp;lt;size;i++){<br />
		nums[i] = i;<br />
		printf(&quot;%d\\n&quot;,nums[i]);<br />
	}<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
 int num = atoi(argv[1]);<br />
 printf(&quot;%ld\\n&quot;,num*sizeof(int));<br />
 kidding_me(num);<br />
<br />
 return 0;<br />
}<br />
[/c]<br />
<br />
オプションで配列の個数を指定すると、それだけスタックを確保してくれます気持ち悪いですねー。<br />
<br />
コンパイルして、とりあえず200万を指定して実行してみます。<br />
<br />
[bash]<br />
uedamac:~ ueda$ gcc ./hoge.c<br />
uedamac:~ ueda$ ./a.out 2000000 | tail -n 1<br />
1999999<br />
[/bash]<br />
<br />
甲斐甲斐しく動いています。<br />
<br />
じゃあ動かなくなるのはどれくらいなんだ、と。<br />
<br />
いろいろ調べた結果、209万6105でSegmentation faultが発生しました。素直な結果でよかったよかった。<br />
<br />
[bash]<br />
uedamac:~ ueda$ ./a.out 2096104 | head<br />
8384416<br />
0<br />
1<br />
2<br />
3<br />
4<br />
5<br />
6<br />
7<br />
8<br />
uedamac:~ ueda$ ./a.out 2096105<br />
8384420<br />
Segmentation fault: 11<br />
[/bash]<br />
<br />
ということで、私のMacだと100万レベルでガボッと配列を確保していいようです。これならいいか。<br />
<br />
でも、自分で配列の個数の上限をチェックするコードを書く事になるんだから、決まった数の配列を作って、それを使った方がいいんじゃないのかなあ？？？<br />
<br />
うーん。<br />
<br />
続く。
