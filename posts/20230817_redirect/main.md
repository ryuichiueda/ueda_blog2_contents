---
Keywords: シェル芸, 自作シェル, bash
Copyright: (C) 2023 Ryuichi Ueda
---

# リダイレクトのエラーの謎

　[連載](/?page=sd_rusty_bash)のためにリダイレクトについてBashの重箱の隅を突っついて遊んでいるんですが、なかなか意味不明です。Bashのコードを読めという話ではあるんですが、個人的に奇妙だと思ったエラーについてメモしておきます。

　もし理屈が分かったら、記事に謝辞を掲載するので情報ください！

## `>&`の前には`1`をつけてよい？

`>&`は通常、`>&2`みたいにファイル記述子を書いて使いますが、
`&>`の非推奨の書き方も兼ねています。
この非推奨の書き方の場合、`>& file`のようにファイル名を書くことできます。
ただ、下の例を見ると`1>& file`という書き方も許されているようです。
`2>& file`はダメみたいです。

```bash
$ echo aaaa 2>&f             #ダメ
bash: f: 曖昧なリダイレクトです
$ echo aaaa 1>&f             #これはOK
$ cat f
aaaa
```

## ファイル記述子に大きな数字を渡した場合

　`2>&ファイル記述子`としたときに、ファイル記述子の桁が多いと変なことが起こります。

```bash
$ echo 2>&1
                                     #OK
$ echo 2>&10
bash: 10: 不正なファイル記述子です   #10が悪い
$ echo 2>&10000
bash: 10000: 不正なファイル記述子です #10000が悪い
$ echo 2>&100000000000
bash: 2: 不正なファイル記述子です #なぜか2が悪いことになる
$ echo >&100000000000
bash: 100000000000: 不正なファイル記述子です #これは100000000000が悪いことになる
```

とりあえず以上です。また何か変な挙動があったら報告します。


## いただいた情報

　あとから実験していただきました。Misskeyのリンクを掲載しておきます。雑誌には謝辞書きます。

* https://mi.shellgei.org/notes/9iipbudn2i
* https://mi.shellgei.org/notes/9ijd299wzt

