---
Keywords:auto,C++,C/C++,POSIXスレッド,pthread
Copyright: (C) 2017 Ryuichi Ueda
---

# 【お盆の勉強にどうぞ】C++11はもはやLL
研究のために<a href="https://github.com/ryuichiueda/DP_TOOL2/tree/master/bin" target="_blank">科学計算のコマンド</a>をC++で作ってます。去年もちょっと使いましたが、自分がC++ばっかり書いていた頃（1997年から10年くらい）から何年もたっているので、<br />
<br />
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=B00DUW4BMS" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe><br />
<br />
を読みながらリハビリ中です。<br />
<br />
<br />
<h2>autoを使う</h2><br />
<br />
この本、1000ページ以上もあり、しかもKindle版で正直読みにくいのではなっから全部読むつもりはないのですが、私の知っているC++とあまりにも違って浦島太郎状態です。まず最初に、autoというものを見つけてひっくり返りました。昔のautoとは違います（昔のautoは使ったことないけど）。<br />
<br />
こんなふうに使います。<br />
<br />
[cpp]<br />
#そーす<br />
uedambp:tmp ueda$ cat hoge.cc <br />
#include &lt;iostream&gt;<br />
using namespace std;<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	double v = 1.0;<br />
	int n = 5;<br />
<br />
	//doubleとintのかけ算<br />
	auto x = v*n;<br />
	cout &lt;&lt; &quot;型:&quot; &lt;&lt; typeid(x).name() &lt;&lt; &quot; 値:&quot; &lt;&lt; x &lt;&lt; endl;<br />
<br />
	return 0;<br />
}<br />
[/cpp]<br />
<br />
実行すると、xの型はdoubleになっていることが分かります。<br />
<br />
[cpp]<br />
#こんぴゃーるして実行<br />
uedambp:tmp ueda$ g++ -O3 -std=c++11 hoge.cc -o hoge<br />
uedambp:tmp ueda$ ./hoge <br />
型:d 値:5<br />
[/cpp]<br />
<br />
要はHaskellみたいに型推論してくれるということかと。<br />
<br />
んで、これだと型に慣れている人はあまり有り難がらないと思いますが、私が感動したのはこういう書き方ができるということです。<br />
<br />
[cpp]<br />
int main(int argc, char const* argv[])<br />
{<br />
	vector&lt;string&gt; str;<br />
	str.push_back(&quot;abc&quot;);<br />
	str.push_back(&quot;あいう&quot;);<br />
	str.push_back(&quot;!?*&quot;);<br />
<br />
	//こう書ける<br />
	for(auto i=str.begin();i&lt;str.end();i++)<br />
		cout &lt;&lt; *i &lt;&lt; endl;<br />
<br />
	//昔の書き方（STLの便利さが90%減）<br />
	for(vector&lt;string&gt;::iterator i=str.begin();i&lt;str.end();i++)<br />
		cout &lt;&lt; *i &lt;&lt; endl;<br />
}<br />
[/cpp]<br />
<br />
「vector&lt;string&gt;::iterator」を初心者に教える自信は全くなく、そして何年もブランクのある今、私もなにがなんだか分からないし、書き方を忘れていて調べてしまったのですが、autoはそんな人々を温かく出迎えてくれます。<br />
<br />
STLを使えばポインタやデストラクタでいろいろ悩むこともなく、C++を使える人の人口をぐっと増やせると私は思っているのですが、これでまた間口が広がったような気がします。<br />
<br />
<h2>スレッドを使う方法がバカバカしいくらいに簡単になっている</h2><br />
<br />
んで、今私の書いている「価値反復」というアルゴリズムは、排他なしで並列処理ができます。できるということは並列化しないと笑われるので泣く泣くPOSIXスレッドの立て方を復習していたのですが、これもC++11だとすごく簡単ということが分かりました。threadというクラスのインスタンスを作るだけです。<br />
<br />
[cpp]<br />
ueda\@ubuntu:~$ cat multi.cc <br />
#include &lt;iostream&gt;<br />
#include &lt;thread&gt;<br />
using namespace std;<br />
<br />
void tfunc(string name)<br />
{<br />
	int num = 0;<br />
	for(int i=0;i&lt;10000000;i++){//ひたすら足し算<br />
		fprintf(stdout,&quot;\\n%s: %d&quot;,name.c_str(),num++);<br />
	}<br />
}<br />
<br />
int main(int argc, char const* argv[])<br />
{<br />
	thread th1(tfunc,&quot;th1&quot;);//実行したい関数と、その関数に渡したい引数を指定<br />
	thread th2(tfunc,&quot;th2&quot;);<br />
	thread th3(tfunc,&quot;th3&quot;);<br />
<br />
	th1.join();//これで終わるのを待つ<br />
	th2.join();<br />
	th3.join();<br />
}<br />
[/cpp]<br />
<br />
実行して途中の出力を見てみます。th1,2,3入り乱れています。<br />
[cpp]<br />
ueda\@ubuntu:~$ g++ -O3 -std=c++11 -pthread multi.cc -o multi<br />
ueda\@ubuntu:~$ ./multi | head -n 10000 | tail <br />
th1: 5102<br />
th3: 2605<br />
th2: 2282<br />
th1: 5103<br />
th3: 2606<br />
th1: 5104<br />
th3: 2607<br />
th1: 5105<br />
th3: 2608<br />
th3: 2609<br />
[/cpp]<br />
<br />
実行中にtopで見ると、CPUの使用率が300%近くになってます。<br />
<br />
<a href="スクリーンショット-2014-08-12-21.52.56.png"><img src="スクリーンショット-2014-08-12-21.52.56-1024x271.png" alt="スクリーンショット 2014-08-12 21.52.56" width="625" height="165" class="aligncenter size-large wp-image-3657" /></a><br />
<br />
ちなみに時間はこんなもん。30000000回の足し算と標準出力への吐き出しですが、なんかもうちょっと速いような気もしないでもありません。もし何かヘマをしていたら教えていただきたく。CPUの周波数は2.5GHzです。<br />
<br />
[cpp]<br />
ueda\@ubuntu:~$ time ./multi &gt; /dev/null<br />
<br />
real	0m24.254s<br />
user	0m34.824s<br />
sys	0m32.161s<br />
[/cpp]<br />
<br />
Macでもちゃんと動作しますが、topの出力がいまいちよく分からなかったのでUbuntuで実験しました。<br />
<br />
もちろん、排他制御は自分でやらなければいけませんので、そこはちょっと敷居が高くなるかと思います。<br />
<br />
<h2>おわりに</h2><br />
<br />
LLから入った人はC/C++にアレルギーがあるようなのですが、STLを落ち着いて勉強すればポインタを使ったり自分でメモリを解放したりということはほとんどしなくて良いので、あまり怖がる意味はないかと思います。SLTが満足に整備されていなかったときと比べると、格段に簡単になっています。<span style="color:red">生のCと比べるとLLと言っていいくらいです。</span><br />
<br />
自分で書いたプログラムが何の引っかかりも無く立ち上がって、すんごい速さで動く感覚を是非味わっていただきたく。と言いますかこれが普通の速さなのですが。<br />
<br />
<span style="color:red">ぜひC++でコマンドを書いてシェルスクリプトでシェル芸を。いや、これ書いておかないと自分がどこの会長か忘れてしまうので。</span><br />
<br />
<br />
よいお盆を。
