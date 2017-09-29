---
Keywords: CLI,シェル芸,集合
Copyright: (C) 2017 Ryuichi Ueda
---

# シェル芸で部分集合を全通り求める方法（別解求む）
ちょっと質問というかお題なのですが、ある集合の部分集合を全通り求める（意味がわからなかったらブログの一番下の出力を見てみてください）必要があって、シェル芸でできないかと考えてみました。

私の解はこんな感じです。{a,b,c,d}の部分集合を全て求めてみます。a,b,c,dにはアルファベット一文字でなくて数文字入ることもあるとします。


まず、とりあえず要素をechoしてみます。

```bash
uedambp:~ ueda$ echo a b c d
a b c d
```

次にこうやって・・・

<!--more-->

```bash
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&\\},;g' | tr -d ' ' |
 awk '{print "echo",$0}'
echo {,a},{,b},{,c},{,d},
```

bashに突っ込みます。

```bash
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&\\},;g' | tr -d ' ' |
 awk '{print "echo",$0}' | bash
,,,, ,,,d, ,,c,, ,,c,d, ,b,,, ,b,,d, ,b,c,, ,b,c,d, a,,,, a,,,d, a,,c,, a,,c,d, a,b,,, a,b,,d, a,b,c,, a,b,c,d,
```

あとは適当に整形して終わり。

```bash
uedambp:~ ueda$ echo a b c d | gsed 's;[^ ]*;\\{,&\\},;g' | tr -d ' ' | awk '{print "echo",$0}' | bash | sed 's/,,*/,/g' | tr ' ' '\\n' | sed 's/,$/}/' | sed 's/^/{/'
{}
{,d}
{,c}
{,c,d}
{,b}
{,b,d}
{,b,c}
{,b,c,d}
{a}
{a,d}
{a,c}
{a,c,d}
{a,b}
{a,b,d}
{a,b,c}
{a,b,c,d}
```

なーんかもっと簡単な方法があるように思うのですが、思いつきません。シェル芸的にはできたからいいんですけど、もし別解があれば教えていただきたく。


寝る。

