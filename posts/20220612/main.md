---
Keywords: 日記, Rusty Bash
Copyright: (C) 2022 Ryuichi Ueda
---

# bashの代入とリダイレクトの変態挙動

　昨日、自作のbashクローンである[Rusty Bash](https://github.com/shellgei/rusty_bash)にパイプを実装しました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">パイプつかえるようになりましたー！<a href="https://twitter.com/hashtag/rusty_bash?src=hash&amp;ref_src=twsrc%5Etfw">#rusty_bash</a><a href="https://t.co/EmMlWYGhsi">https://t.co/EmMlWYGhsi</a> <a href="https://t.co/iwjaubInSR">pic.twitter.com/iwjaubInSR</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1535245265979854848?ref_src=twsrc%5Etfw">June 10, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

で、それはいいんですが、今日、コードを整理していて、bashのリダイレクトと変数の代入について気づいたことをメモしておきます。私の書いてるシェルじゃなくて、本家bashの話です。

## 変数の代入の行に無意味なリダイレクトを入れることが可能

・・・です。次のように、リダイレクトを入れるとファイルができます。

```bash
$ A=💩 > file
$ echo $A
💩
$ ls -l file
-rw-rw-r-- 1 ueda ueda 0  6月 11 22:15 file
```

途中にリダイレクトを入れることも可能です。

```bash
$ A=💩 > file B=🚽
$ echo $A$B
💩🚽
```

もしかしたら何かに使えるのかもしれませんが、わかりません。


## 変数の代入やリダイレクトをパイプにつなぐことが可能

ただし、データは吸い込まれます。そして、変数への代入はたぶんサブシェルで行われるので、反映されません。

```bash
$ echo 王様の耳はロバの耳 | A=B
$
$ echo 王様の耳はロバの耳 | A=B | echo 💩
💩
$ echo 王様の耳はロバの耳 | 2>aho | echo 💩
💩
```

これも・・・なにかに使えるんですかね？？？

## （おまけ）変数へ代入する値にはブレース展開が使えない

これはブレース展開を実装しているときに気づいたのですが・・・

```bash
$ A={a,b}{c,d}
$ echo $A
{a,b}{c,d}
$ A=$(echo {a,b}{c,d})   #これは展開される。
$ echo $A
ac ad bc bd
```

微妙に不便なような気がするけど、使う場面もないような・・・


## bashのコードを読めばいいじゃないか 

・・・と言われても、あのコードを読むのは・・・


## ということで

Rustできれいに（？）書き直してますので、ご声援おねがいいたします。


以上。
