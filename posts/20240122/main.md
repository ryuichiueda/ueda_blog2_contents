---
Keywords: bash
Copyright: (C) 2024 Ryuichi Ueda
---

# 「$$ブレース展開」の挙動（おしえてもらったので解決）

　[先日](/?post=20240120)のこの謎ですが、解決しました。[Stack Overflowに質問したら](https://stackoverflow.com/questions/77850130/bash-parse-of-x-y/)manに書いてあるぞ、とのことでした。

```bash

$ echo $${x,y}
4821{x,y}      #ブレースの部分が展開されない <-謎
```

## 結局なにか

　manを読むと、`パラメータ展開との衝突を避けるため、文字列 ${ はブレース展開の対象とは解釈されません。`とちゃんと書いてありました。 https://qiita.com/emasaka/items/a59335c74220b3641639 にもあるように、「ブレース展開」→「変数の展開」という順に処理が進むので、ブレース展開の段階では、まだ`${`の`$`がなんなのか確定してないので、そういうルールが導入されているみたいです。

## おまけ

　これだと教えてもらっただけでなんも貢献がないので、「ブレース展開」→「変数の展開」の順番が分かるワンライナーを提示しておきます。

```bash

$ echo $BASH{_VERSION,}
5.1.16(1)-release /usr/bin/bash
$ echo {$,}{SHELL,}
/bin/bash $ SHELL
$ echo {$PP,a}{ID,c}
2999 aID ac
$ echo {$,a}{{PPID},c}
2999 a{PPID} ac
```

以上です。
