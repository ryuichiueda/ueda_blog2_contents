---
Keywords: プログラミング,C言語
Copyright: (C) 2017 Ryuichi Ueda
---

# C言語（C99）の variable length array というものを初体験
こちらを拝読してびっくりしたので検証しました。

<a href="http://cpplover.blogspot.jp/2013/04/llvmclanglinuxgcc.html">http://cpplover.blogspot.jp/2013/04/llvmclanglinuxgcc.html</a>
<blockquote>variable length array自体は、GCCは大昔から拡張機能としてサポートしている。C99では正式に採用された。</blockquote>
<span style="color: #ff0000;">配列のサイズにconstでない変数をぶち込んでも良いとのこと・・・。</span>しかも大昔から。ほんまかい。

こんなコードを書いて・・・

[c]
uedamac:~ ueda$ cat hoge.c
#include

void kidding_me(size_t size)
{
	int nums[size];

	for(int i=0;i&lt;size;i++){
		nums[i] = i;
		printf(&quot;%d\\n&quot;,nums[i]);
	}
}

int main(int argc, char const* argv[])
{
	kidding_me(4);
	return 0;
}
[/c]

こんぴゃーるして実行。-std=c99 というオプションが必要なのか？

[bash]
uedamac:~ ueda$ gcc ./hoge.c
./hoge.c: In function ‘kidding_me’:
./hoge.c:7: error: ‘for’ loop initial declaration used outside C99 mode
uedamac:~ ueda$ gcc -std=c99 ./hoge.c
uedamac:~ ueda$
[/bash]

あ、サイズが可変なことより、for(int ...の方が怒られているのね。<span style="color: #ff0000;">もしかしてオプション要らないんじゃないか？</span>

書き直してコンパイル・・・と。

[bash]
uedamac:~ ueda$ cat hoge.c
#include

void kidding_me(size_t size)
{
	int nums[size];

	int i=0;
	for(i=0;i&lt;size;i++){
		nums[i] = i;
		printf(&quot;%d\\n&quot;,nums[i]);
	}
}

int main(int argc, char const* argv[])
{
	kidding_me(4);
	return 0;
}
uedamac:~ ueda$ gcc ./hoge.c
uedamac:~ ueda$ ./a.out
0
1
2
3
[/bash]

特に技術的にごちゃごちゃ書く元気はありませんが、一言言わせてください。

<span style="color: #ff0000; font-size: 44pt;">気持ち悪い！</span>

以上です。これは・・・使わない方がよいと思う・・・。いや、オッサンだからそう思うだけか・・・。ポータビリティーというより、なんかメモリの使い方の前提が分からなくなりそうなので・・・。シェルスクリプトは動けばいいというのが持論なんだけど、Cのコードはちょっと違うのかなと。はたまた自分の頭が固いのか。

これ知ってる人ってどれだけいるんだろ？
