---
Keywords: bash
Copyright: (C) 2024 Ryuichi Ueda
---

# 「$$ブレース展開」の挙動

　Bashの（[@eban](https://mi.shellgei.org/@eban)さんによるとZshも）なんだかよくわからない挙動にまたぶちあたってしまいました。
次の4つの例のexample 2の出力が私にはよくわかりません。$$が値に置き換わっているのに、そのうしろの`{x,y}`がブレース展開と解釈されていない点が不明です。

```bash
$ echo $BASH_VERSION
5.1.16(1)-release
example 1$ echo $?{x,y}
0x 0y          #ブレースの部分が展開される
example 2$ echo $${x,y}
4821{x,y}      #ブレースの部分が展開されない <-謎
example 3$ echo ${$}{x,y} 
4821x 4821y    #これは展開される（シェルスクリプトではこう書いたほうがいい）
example 4$ echo $PPID{x,y}
               #これは$PPIDと解釈されないのでなにも出ない（おそらくPPID{x,y}でひとかたまりの単語として解釈されている）
```

とりあえずこういう現象があるという報告だけですが、メモということで。
