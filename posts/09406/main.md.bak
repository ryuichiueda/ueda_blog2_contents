# GlueLangにループを実装
　帰省中に少し時間があったので、<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>にループを実装しました。次のように使います。この例は、dateにUnix時刻を吐かせて、5で割り切れる数になったらループを抜ける処理です。testコマンドが0でない終了ステータスを返したのを受けてループが終わって最終行のechoが実行されます。<br />
<br />
[bash]<br />
$ cat hoge.glue <br />
import PATH<br />
<br />
loop<br />
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}'<br />
 echo t<br />
 test t -ne 0<br />
 sleep 1<br />
<br />
echo 'end'<br />
[/bash]<br />
<br />
　実行すると、ちゃんと動きます。これはMacで動かしましたが同じコードでLinuxでも動きます。<br />
<br />
[bash]<br />
$ glue ./hoge.glue <br />
1<br />
2<br />
3<br />
4<br />
0<br />
end<br />
[/bash]<br />
<br />
<h2>shのwhileのように書くには</h2><br />
　shやbashのように、 while &lt;コマンド&gt; ; do &lt;処理&gt; ; done と書く場合、つまりコマンドの終了ステータスで処理を実行するかしないかを決めるときは、1段ネストが深くなりますが、次のように記述できます。<br />
<br />
[bash]<br />
$ cat hoge2.glue <br />
import PATH<br />
<br />
loop<br />
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}' #この行と<br />
 test t -ne 0 &gt;&gt; do #この行のdoの前までが条件<br />
 echo t #doのあとが繰り返したい処理<br />
 sleep 1<br />
<br />
echo 'end'<br />
[/bash]<br />
<br />
　ネストが2段になりますが、shやbashのwhileよりも長く条件となるコマンドが書けます。だいたい、while hogehoge ; do ...という書き方が、hogehogeという部分をコマンドだと気づかない初心者を量産しており悪い影響を与えているので、踏襲するわけにはいけません。<br />
<h2>文法エラーの時に止める</h2><br />
で、シェルでループを作るとCtrl+Cやスクリプトにエラーが思うように止まらない場合がありますが、GlueLangでは止められるように工夫をしました。次の例は、コマンドが見つからない時にすぐにループを止めて、最終行の echo 'end' が実行されないことを確かめる例です。<br />
<br />
[bash]<br />
$ cat hoge3.glue <br />
import PATH<br />
<br />
loop<br />
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}'<br />
 eho t #ここでエラーが起こって処理全体が止まる<br />
 sleep 1<br />
 test t -ne 0<br />
<br />
echo 'end' #これは実行されない<br />
[/bash]<br />
<br />
　GlueLangでは（まだ実装が中途半端ですが）<span style="color: #ff0000;">「コマンドが実行されて返ってくる終了ステータス」と「コマンドが見つからない、あるいはGlueLangのスクリプト自体が出すエラー」を区別する</span>ことにしました。技術的には可能ですし、これは普通のシェルよりもエラーへの対応がかなりスマートになるのではないかと考えています。<br />
<br />
[bash]<br />
$ glue ./hoge3.glue <br />
<br />
Parse error at line 2, char 1<br />
	line2: eho t<br />
	^<br />
<br />
	Command eho not exist<br />
	<br />
	process_level 1<br />
	exit_status 2<br />
	pid 30839<br />
<br />
	glue exit_status: 2<br />
<br />
Execution error at line 3, char 1<br />
	line3: loop<br />
	^<br />
	line4: str t = date '+%s' &gt;&gt;= awk '{print $1%5}'<br />
	line5: eho t<br />
	line6: sleep 1<br />
	line7: test t -ne 0<br />
	line8: <br />
<br />
	Command error<br />
	<br />
	process_level 0<br />
	exit_status 2<br />
	pid 30837<br />
###echo 'end'が実行されずに終わる###<br />
[/bash]<br />
<br />
　ただ、現状で先ほどのように2段にネストした場合、止まらないのでまた来週末あたり改良します。また、readも実装しないといけません・・・。
