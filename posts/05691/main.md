---
Keywords: コマンド,2進数,awk,助けて,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# gawkで2進数にしたときの桁数を求めたいんだがどうしたものか
「n種類のものを表現するには何ビット必要か？」というのをawk（gawk）で計算したいんですが、素直な方法が思い浮かばず、ちと困ってます。

例えば5種類についてこれを求めようとすると、次のようにlog($1)/log(2)して、この値を切り上げればよいのですが、awkには切り上げの関数がありません。

```bash
uedambp:~ ueda$ echo 5 | awk '{print log($1)/log(2)}'
2.32193
```

んで、思いついたのがこれ。要は小数点のピリオドがあったら切り捨てて1足せと。計算というより文字列処理ですな・・・

```bash
uedambp:~ ueda$ echo 5 | awk '{print log($1)/log(2)}' |
 awk '/\\./{print int($1)+1}!/\\./{print $1}'
3
uedambp:~ ueda$ echo 4 | awk '{print log($1)/log(2)}' |
 awk '/\\./{print int($1)+1}!/\\./{print $1}'
2
```

しかし、素直ではない・・・。Tukubaiのmarume使うか・・・。

別解、たぶんすぐ見つかると思うので絶賛受付中。


仕事に戻る。
