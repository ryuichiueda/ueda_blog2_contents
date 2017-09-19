---
Keywords: GlueLang
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangにループを実装
　帰省中に少し時間があったので、<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>にループを実装しました。次のように使います。この例は、dateにUnix時刻を吐かせて、5で割り切れる数になったらループを抜ける処理です。testコマンドが0でない終了ステータスを返したのを受けてループが終わって最終行のechoが実行されます。

```bash
$ cat hoge.glue 
import PATH

loop
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}'
 echo t
 test t -ne 0
 sleep 1

echo 'end'
```

　実行すると、ちゃんと動きます。これはMacで動かしましたが同じコードでLinuxでも動きます。

```bash
$ glue ./hoge.glue 
1
2
3
4
0
end
```

<h2>shのwhileのように書くには</h2>
　shやbashのように、 while &lt;コマンド&gt; ; do &lt;処理&gt; ; done と書く場合、つまりコマンドの終了ステータスで処理を実行するかしないかを決めるときは、1段ネストが深くなりますが、次のように記述できます。

```bash
$ cat hoge2.glue 
import PATH

loop
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}' #この行と
 test t -ne 0 &gt;&gt; do #この行のdoの前までが条件
 echo t #doのあとが繰り返したい処理
 sleep 1

echo 'end'
```

　ネストが2段になりますが、shやbashのwhileよりも長く条件となるコマンドが書けます。だいたい、while hogehoge ; do ...という書き方が、hogehogeという部分をコマンドだと気づかない初心者を量産しており悪い影響を与えているので、踏襲するわけにはいけません。
<h2>文法エラーの時に止める</h2>
で、シェルでループを作るとCtrl+Cやスクリプトにエラーが思うように止まらない場合がありますが、GlueLangでは止められるように工夫をしました。次の例は、コマンドが見つからない時にすぐにループを止めて、最終行の echo 'end' が実行されないことを確かめる例です。

```bash
$ cat hoge3.glue 
import PATH

loop
 str t = date '+%s' &gt;&gt;= awk '{print $1%5}'
 eho t #ここでエラーが起こって処理全体が止まる
 sleep 1
 test t -ne 0

echo 'end' #これは実行されない
```

　GlueLangでは（まだ実装が中途半端ですが）<span style="color: #ff0000;">「コマンドが実行されて返ってくる終了ステータス」と「コマンドが見つからない、あるいはGlueLangのスクリプト自体が出すエラー」を区別する</span>ことにしました。技術的には可能ですし、これは普通のシェルよりもエラーへの対応がかなりスマートになるのではないかと考えています。

```bash
$ glue ./hoge3.glue 

Parse error at line 2, char 1
	line2: eho t
	^

	Command eho not exist
	
	process_level 1
	exit_status 2
	pid 30839

	glue exit_status: 2

Execution error at line 3, char 1
	line3: loop
	^
	line4: str t = date '+%s' &gt;&gt;= awk '{print $1%5}'
	line5: eho t
	line6: sleep 1
	line7: test t -ne 0
	line8: 

	Command error
	
	process_level 0
	exit_status 2
	pid 30837
###echo 'end'が実行されずに終わる###
```

　ただ、現状で先ほどのように2段にネストした場合、止まらないのでまた来週末あたり改良します。また、readも実装しないといけません・・・。
