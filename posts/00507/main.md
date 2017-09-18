---
Keywords:プログラミング,C言語
Copyright: (C) 2017 Ryuichi Ueda
---

# C言語（C99）の variable length array というものを初体験
こちらを拝読してびっくりしたので検証しました。<br />
<br />
<a href="http://cpplover.blogspot.jp/2013/04/llvmclanglinuxgcc.html">http://cpplover.blogspot.jp/2013/04/llvmclanglinuxgcc.html</a><br />
<blockquote>variable length array自体は、GCCは大昔から拡張機能としてサポートしている。C99では正式に採用された。</blockquote><br />
<span style="color: #ff0000;">配列のサイズにconstでない変数をぶち込んでも良いとのこと・・・。</span>しかも大昔から。ほんまかい。<br />
<br />
こんなコードを書いて・・・<br />
<br />
[c]<br />
uedamac:~ ueda$ cat hoge.c<br />
#include<br />
<br />
void kidding_me(size_t size)<br />
{<br />
	int nums[size];<br />
<br />
	for(int i=0;i&lt;size;i++){<br />
		nums[i] = i;<br />
		printf(&quot;%d\\n&quot;,nums[i]);<br />
	}<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	kidding_me(4);<br />
	return 0;<br />
}<br />
[/c]<br />
<br />
こんぴゃーるして実行。-std=c99 というオプションが必要なのか？<br />
<br />
[bash]<br />
uedamac:~ ueda$ gcc ./hoge.c<br />
./hoge.c: In function ‘kidding_me’:<br />
./hoge.c:7: error: ‘for’ loop initial declaration used outside C99 mode<br />
uedamac:~ ueda$ gcc -std=c99 ./hoge.c<br />
uedamac:~ ueda$<br />
[/bash]<br />
<br />
あ、サイズが可変なことより、for(int ...の方が怒られているのね。<span style="color: #ff0000;">もしかしてオプション要らないんじゃないか？</span><br />
<br />
書き直してコンパイル・・・と。<br />
<br />
[bash]<br />
uedamac:~ ueda$ cat hoge.c<br />
#include<br />
<br />
void kidding_me(size_t size)<br />
{<br />
	int nums[size];<br />
<br />
	int i=0;<br />
	for(i=0;i&lt;size;i++){<br />
		nums[i] = i;<br />
		printf(&quot;%d\\n&quot;,nums[i]);<br />
	}<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	kidding_me(4);<br />
	return 0;<br />
}<br />
uedamac:~ ueda$ gcc ./hoge.c<br />
uedamac:~ ueda$ ./a.out<br />
0<br />
1<br />
2<br />
3<br />
[/bash]<br />
<br />
特に技術的にごちゃごちゃ書く元気はありませんが、一言言わせてください。<br />
<br />
<span style="color: #ff0000; font-size: 44pt;">気持ち悪い！</span><br />
<br />
以上です。これは・・・使わない方がよいと思う・・・。いや、オッサンだからそう思うだけか・・・。ポータビリティーというより、なんかメモリの使い方の前提が分からなくなりそうなので・・・。シェルスクリプトは動けばいいというのが持論なんだけど、Cのコードはちょっと違うのかなと。はたまた自分の頭が固いのか。<br />
<br />
これ知ってる人ってどれだけいるんだろ？
