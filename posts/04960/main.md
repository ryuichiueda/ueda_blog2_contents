---
Keywords: プログラミング,GlueLang,where,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangでとうとうwhereが使えるように
週末プログラマー上田Zです。（きもちわるい）<br />
<br />
<br />
どうしても実装したかったwhereを本日ついに実装しました。まだスコープが分かれてませんが。<br />
<br />
<h1>whereの使い方</h1><br />
<br />
例えばシェルスクリプトでこう書いたとします。ファイルaとbを作って、diffで比べています。<br />
[bash]<br />
seq 8 &gt; a<br />
seq 10 &gt; b<br />
<br />
diff a b<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
しかし、aとbをdiffでしか使わないとしたら、aとbをdiffのためだけに作っているようにコードを見せたほうがよいということで、Glueでは次のように書けます。<br />
<br />
[hs]<br />
import PATH<br />
<br />
? diff a b<br />
 where file a = seq 8<br />
 file b = seq 10<br />
[/hs]<br />
<br />
これならコードの他の部分を読んでいるときに目障りなaとbが視界に入りません（いや、右目にちょっと入るが・・・）。まだ実装してませんが、名前もローカルで定義でき、diffの処理が終わったらaとbの実体（中間ファイル）を消すこともでき、事故も減ります。<span style="color:red">ローカルスコープにするのも中間ファイルを消すのもまだ実装してませんが・・・。</span><br />
<br />
ちなみにdiffの頭につけた?（if）は、diffが0でない終了ステータスを返してもスクリプトが終了しないためのズルです。<br />
<br />
<h1>環境変数PATHも使えるようにした</h1><br />
<br />
そして、上の例でも使いましたが、「import PATH」と書くと環境変数のパスを全部読み込んでくれるようにしました。<br />
<br />
[hs]<br />
import PATH<br />
<br />
echo 'もうフルパス指定もprefixも不要。'<br />
echo 'ただ、指定して書いたほうが厳密なので指定した方がいいかも。'<br />
[/hs]<br />
<br />
<h1>MacとLinuxのパスの違いも吸収できるようにした</h1><br />
<br />
もう一つimportの規制緩和ですが、異なるパスに同じprefixをつけることができるようになりました。例えばawkはMacだと/usr/local/bin/、Linuxだと/usr/bin/にありますが、次のように書いておけばどっちでも動きます。<br />
<br />
[hs]<br />
import /usr/local/bin/ as sys<br />
import /usr/bin/ as sys<br />
<br />
sys.awk 'BEGIN{print &quot;hoge&quot;}'<br />
[/hs]<br />
<br />
<br />
ようやく言語っぽくなってきました。
