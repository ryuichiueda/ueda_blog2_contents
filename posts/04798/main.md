---
Keywords: パイプライン,GlueLang,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# パイプラインを実装できた
<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>の作業、休日にやるという禁を破って金曜日にやっちまいました。当初かなり難航することを覚悟していたのですが、<a href="http://blog.ueda.asia/?page_id=4346" title="dash/src/eval.h, eval.c" target="_blank">dashのコード読み</a>のおかげで、機械的に書いたら動きました。

こういうのを入力すると、
```bash
uedambp:GlueLang ueda$ cat TEST/pipeline_mac.glue 
/usr/bin/seq '1' '5', /usr/bin/tail '-r' .
```
<!--more-->
次のように動作します。
```bash
uedambp:GlueLang ueda$ ./main TEST/pipeline_mac.glue 
5
4
3
2
1
```

パイプライン処理は、<a href="https://github.com/ryuichiueda/GlueLang/blob/master/Pipeline.cc" target="_blank">Pipeline.cc</a>と<a href="https://github.com/ryuichiueda/GlueLang/blob/master/CommandLine.cc" target="_blank">CommandLine.cc</a>に実装されています。まだシグナル処理を入れておらず処理が単純なので、もし自分でシェルを書いている変態の皆さんに参考になるなら幸いです。あ、「シェルを書く」と言っても、異様に怒る人を量産している「シェルスクリプトを書くの略」ではありません。


当初の予定では所定の場所に1行に1コマンドを書くと勝手にパイプでつながるという仕様にしようとしてましたが、パイプを「, 」、パイプラインの終わりを「. 」で表現することにしました。なんかその方が言葉っぽいので、そうしました。「|」よりも目立たないので読みにくいと思いますが、「, 」の後ろには改行を入れるのをお作法にしたいと思います。こんな感じで・・・。
```bash
###まだ動きません###
uedambp:GlueLang ueda$ cat TEST/pipeline_mac.glue 
/usr/bin/seq '1' '5',
/usr/bin/tail '-r' .
```
しかし、まだ議論の余地がありそうです。

<span style="color:blue">そのうちに「、」「。」でも良いようしようかとも考えてます。そんなもんイランと言われそうですが。</span>日本語好きなので。

ところで、シグナル処理を全然書いていないので、パイプラインを実行しちまうとCtrl+Cが効きません。万が一試す人がいたらご注意を。シグナル処理をちゃんと実装しないといけませんが、それが済めばあとは難しいことはそんなにないので一気に進みそうです。

シグナルは一旦おいておいて、次はimportの実装。しかし、もっとコメントを入れないと誰も手伝ってくれない予感・・・。


寝る。
