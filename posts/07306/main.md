---
Keywords: どうでもいい,シェルスクリプト,Mac,top,寝る,日記
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記: 研究室の名前/AD○BE殺傷コマンドの作成
山なし、落ちなし、意味なし。

<h2>シェル芸研では無い</h2>

この前とったアンケート。違います。

<blockquote class="twitter-tweet" lang="ja"><p lang="ja" dir="ltr">私の主宰する研究室は</p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/677502473729212416">2015, 12月 17</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

正式名称は<a href="https://lab.ueda.asia/" target="_blank">コレ</a>ですので宜しくお願い致します。

<h2>Creative Cloudのjsのプロセス殺傷シェルスクリプト</h2>

AdobeのCreative Cloudが勝手にメモリを何ギガも食っていて、MacBookの8GBのメモリだとすぐ振り切れてしまう現象に見舞われており。

↓こいつらです。なんか、「JavaScript使っとけばいいんじゃね？」みたいな安易な実装で自爆しているんじゃないかと推測します。私のメモリは御社のプログラマに楽をさせるためにあるのではないのですが。

```bash
uedamb:~ ueda$ ps aux | grep js
ueda 512 100.0 4.4 3396884 369820 ?? R 11:20PM 2:50.36 
/Applications/Utilities/Adobe Creative 
Cloud/CCLibrary/CCLibrary.app/Contents/MacOS/../libs/node 
/Applications/Utilities/Adobe Creative 
Cloud/CCLibrary/CCLibrary.app/Contents/MacOS/../js/server.js
ueda 501 99.7 4.6 3428820 387152 ?? R 11:20PM 2:52.92 
/Applications/Utilities/Adobe Creative 
Cloud/CCXProcess/CCXProcess.app/Contents/MacOS/../libs/node 
/Applications/Utilities/Adobe Creative 
Cloud/CCXProcess/CCXProcess.app/Contents/MacOS/../js/main.js
ueda 606 0.0 0.0 2460396 336 s001 R+ 11:23PM 0:00.00 
grep js
```

Macのtopは次のようにオプションを入れるとメモリ食ってる順に表示してくれますが・・・ひどいですね。CPUもギンギンに使っています。しかも殺しても仕事に何の支障もなく、挙句ゾンビのように何度でも蘇るさ状態です。

```bash
uedamb:~ ueda$ top -o mem
...
PID COMMAND %CPU TIME #TH #WQ #PORT MEM PURG CMPRS PGRP PPID STATE BOOSTS %CPU_ME
501 node 90.3 13:57.49 11/1 2 72 913M+ 0B 239M 501 1 running *0[1] 0.00000
512 node 96.6 13:55.64 11/1 2 71 835M+ 0B 191M 512 1 running *0[1] 0.00000
...
```


蘇るたびにプロセス番号を調べて殺しているのも面倒なので殺しの呪文をシェルスクリプトにしました。例外処理も何にもありませんが。あと、名前が物騒ですが他意はないです。他意はないというのは、ファイル名の通りに行動するということではありません。

<script src="https://gist.github.com/ryuichiueda/d2c18dca992d446204aa.js"></script>


使ってみましょう。

```bash
uedamb:~ ueda$ ~/SYS/KILL_ADOBE 
uedamb:~ ueda$ ps aux | grep js
ueda 720 0.0 0.0 2434836 756 s001 S+ 11:42PM 0:00.01 grep js
```

いなくなりました。シェルスクリプト便利！万歳！<span style="color:red">超小手先感！</span>

とか書いてたら、なんだよ、解決しとったんかいというツイートを見つけてしまった・・・。いや、解決したならいいんですけど。


<blockquote class="twitter-tweet" lang="ja"><p lang="ja" dir="ltr">【速報】Creative CloudデスクトップアプリケーションのHot Fixがリリースされました。MacOS環境でプロセスのCPU使用率が増大する問題を修正しています。大変ご迷惑をおかけしました。詳細はフォーラムをご覧ください。<a href="https://t.co/iYMlBTpza1">https://t.co/iYMlBTpza1</a></p>&mdash; アドビ サポート担当 (@AdobeSupportJ) <a href="https://twitter.com/AdobeSupportJ/status/676210177289269249">2015, 12月 14</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


当該のパッチを当てたら寝る。
