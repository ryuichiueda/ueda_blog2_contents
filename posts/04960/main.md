---
Keywords: プログラミング,GlueLang,where,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangでとうとうwhereが使えるように
週末プログラマー上田Zです。（きもちわるい）


どうしても実装したかったwhereを本日ついに実装しました。まだスコープが分かれてませんが。

<h1>whereの使い方</h1>

例えばシェルスクリプトでこう書いたとします。ファイルaとbを作って、diffで比べています。
```bash
seq 8 > a
seq 10 > b

diff a b
```

<!--more-->

しかし、aとbをdiffでしか使わないとしたら、aとbをdiffのためだけに作っているようにコードを見せたほうがよいということで、Glueでは次のように書けます。

```hs
import PATH

? diff a b
 where file a = seq 8
 file b = seq 10
```

これならコードの他の部分を読んでいるときに目障りなaとbが視界に入りません（いや、右目にちょっと入るが・・・）。まだ実装してませんが、名前もローカルで定義でき、diffの処理が終わったらaとbの実体（中間ファイル）を消すこともでき、事故も減ります。<span style="color:red">ローカルスコープにするのも中間ファイルを消すのもまだ実装してませんが・・・。</span>

ちなみにdiffの頭につけた?（if）は、diffが0でない終了ステータスを返してもスクリプトが終了しないためのズルです。

<h1>環境変数PATHも使えるようにした</h1>

そして、上の例でも使いましたが、「import PATH」と書くと環境変数のパスを全部読み込んでくれるようにしました。

```hs
import PATH

echo 'もうフルパス指定もprefixも不要。'
echo 'ただ、指定して書いたほうが厳密なので指定した方がいいかも。'
```

<h1>MacとLinuxのパスの違いも吸収できるようにした</h1>

もう一つimportの規制緩和ですが、異なるパスに同じprefixをつけることができるようになりました。例えばawkはMacだと/usr/local/bin/、Linuxだと/usr/bin/にありますが、次のように書いておけばどっちでも動きます。

```hs
import /usr/local/bin/ as sys
import /usr/bin/ as sys

sys.awk 'BEGIN{print "hoge"}'
```


ようやく言語っぽくなってきました。
