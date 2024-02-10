---
Keywords: bash
Copyright: (C) 2024 Ryuichi Ueda
---

# Bashのブレース展開のルール

　[このまえ](/?post=20240128_bash)悩みまくってましたが、やっと解決したようなのでまとめます。その前に宣伝ですが、シェル芸勉強会やるのできてくださーい。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">大手町でやります〜 <br><br>jus共催第68回3月2日でございますシェル芸勉強会 <a href="https://t.co/7DRG4ygrAb">https://t.co/7DRG4ygrAb</a> <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1755915952439640318?ref_src=twsrc%5Etfw">February 9, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 基本ルール

　文字列を左から右に読んでいって、`{`があったら、次のルールで`{`がブレース展開の開始の括弧なのか（OK）、そうでないか（NG）を判別。詳しくないけどLR文法に属すっぽいです。スタックを使うと簡単に実装できます。

1. そこから右側に読んでいって`}`を探す。なかったらNG
2. `}`があったら、そこから左側に`{`を探す。
3. 見つけた`{`が最初の`{`でなければ見つけた`{`から`}`までをマスクして、1に戻る。
4. 見つけた`{`が最初の`{`で、途中に`,`があればOK
5. 見つけた`{`が最初の`{`で、4に該当しなければ`{`だけ残してあとをマスクし、1に戻る。


### 例1

```bash
{{a},b}     #一番左の{が対象
→{マスク,b} #手続き2と3
→OK
```

### 例2

```bash
a{}},b}            #aの隣の{が対象
→a{マスク},b}      #手続き2と5
→a{マスクマスク,b} #手続き2と5
→OK
```

### 例3

```bash
{a,b,c{d,e}f,g{h,i{j,k}}}     #一番左の{が対象
→{a,b,cマスクf,g{h,i{j,k}}}
→{a,b,cマスクf,g{h,iマスク}}
→{a,b,cマスクf,gマスク}
→OK
```

### 例3

```bash
{a,b,c{d,e}f,g{h,i{j,k}}     #一番左の{が対象
→{a,b,cマスクf,g{h,i{j,k}}
→{a,b,cマスクf,g{h,iマスク}
→{a,b,cマスクf,gマスク
→NG
```

## 例外1（冒頭・ブレース展開直後の`{}`）

　冒頭、あるいはブレース展開直後に`{}`がある場合、`{`はブレース展開の開始と **判定されない**

### 例

```bash
$ echo {},a} #最初の{}は文字列扱いでブレース展開が起こらない
{},a}
$ echo x{},a} #あたまにxを置くとブレース展開が起こる
x} xa
$ echo {a,b}{},a} #うしろの{},a}はブレース展開として扱われない
a{},a} b{},a}
```

## 例外2（手前の`$`）

　手前にエスケープされていない`$`があれば、なにがあってもブレース展開されない

### 例

```bash
$ echo ${a,b}  #これは変数とみなされる

$ echo $${a,b} #「$$」と{a,b}のように見えるがブレース展開しない
6813{a,b}
$ echo $\${a,b} #エスケープするとブレース展開する
$$a $$b
```

参考: https://stackoverflow.com/questions/77850130/bash-parse-of-x-y

現場からは以上です。

