---
Keywords: プログラミング,C言語,ulimit,variable
Copyright: (C) 2017 Ryuichi Ueda
---

# variable length array で配列の要素数の限界を調べた（しかしvariable length arrayあまり関係ない）
前回の variable length array、なんでそんなに自分が気持ち悪いと感じるのかと考えてみました。結果、WindowsでVisual C++を昔（4.0~6.0あたり）使っていたときに、デフォルトのスタック領域の大きさがそんなに大きくなく、

[c]
int aho[100000];
[/c]

などとすると実行時エラーが起こっていたのが遠因のようです。スタック領域はビビりながら使う物で、variable length array などとんでもないと。

例えば、<a href="http://www.office-matsunaga.biz/evctips/evctips04.html" target="_blank">この</a>ページに Windows CEのケースが書いてあります。確か Windows 95, 97 で Visual C++ を使っても全く同じだったと記憶しています。

しかし、もう15年以上も経っているしOSも違うので、自分の感覚は調整しないといけません。実験しましょう。なぜこのクソ忙しいのにそんなことをするのか。それは、今出ている会合がもう休み無しでもうすぐ4時間経過しようとしているからです。息抜きしないと死ぬぞこれ。

まず、自分のマシーンのスタックの大きさを調べます。ulimitというコマンドで調査できます。

[bash]
uedamac:~ ueda$ ulimit -s
8192
//単位をバイトに直す。
uedamac:~ ueda$ ulimit -s | awk '{print $1*1024}'
8388608
[/bash]

ということで、int型だとだいたい 2百万くらいが配列の要素数の限界と言えそうです。

次に取り出しますのは前回の気持ち悪いコードをちょっと修正したもの。

[c]
uedamac:~ ueda$ cat hoge.c
#include &lt;stdio.h&gt;

void kidding_me(size_t size)
{
	int nums[size];//気持ち悪い

	int i;
	for(i=0;i&amp;amp;lt;size;i++){
		nums[i] = i;
		printf(&quot;%d\\n&quot;,nums[i]);
	}
}

int main(int argc, char const* argv[])
{
 int num = atoi(argv[1]);
 printf(&quot;%ld\\n&quot;,num*sizeof(int));
 kidding_me(num);

 return 0;
}
[/c]

オプションで配列の個数を指定すると、それだけスタックを確保してくれます気持ち悪いですねー。

コンパイルして、とりあえず200万を指定して実行してみます。

[bash]
uedamac:~ ueda$ gcc ./hoge.c
uedamac:~ ueda$ ./a.out 2000000 | tail -n 1
1999999
[/bash]

甲斐甲斐しく動いています。

じゃあ動かなくなるのはどれくらいなんだ、と。

いろいろ調べた結果、209万6105でSegmentation faultが発生しました。素直な結果でよかったよかった。

[bash]
uedamac:~ ueda$ ./a.out 2096104 | head
8384416
0
1
2
3
4
5
6
7
8
uedamac:~ ueda$ ./a.out 2096105
8384420
Segmentation fault: 11
[/bash]

ということで、私のMacだと100万レベルでガボッと配列を確保していいようです。これならいいか。

でも、自分で配列の個数の上限をチェックするコードを書く事になるんだから、決まった数の配列を作って、それを使った方がいいんじゃないのかなあ？？？

うーん。

続く。
