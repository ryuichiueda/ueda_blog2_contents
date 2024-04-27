---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記というか週報というか（〜2024年4月27日）

　4月はいろいろありすぎる。

## 自作シェル

　あいかわらず暇を見つけては作り続けており、原稿が2025年5月号分まで書き上がってしまいました。で、中身については掲載されたときということになりますが、昨日初めて知ったシェル（Bash）の関数の挙動についてメモしておきます。

```bash

### 関数をリダイレクト付きで定義する ###
$ hoge () { echo リダイレクトつき関数; } > /tmp/file
### 定義だけだとファイルはできない ###
$ ls /tmp/file
ls: '/tmp/file' にアクセスできません: そのようなファイルやディレクトリはありません
### 関数実行 ###
$ hoge
### リダイレクトも一緒に実行される ###
$ cat /tmp/file
リダイレクトつき関数
```

　ちなみに関数の実体は複合コマンドなので、`hoge () while true ; do echo yes ; done`みたいに、`()`のうしろには複合コマンドならなんでも書けます（連載第1回に書いたような気がする）。

## 価値反復パッケージをROS 1からROS 2へ移行

　[この論文](https://www.fujipress.jp/jrm/rb/robot003500061489/)のROSパッケージをROS 2に移行しています。科研費の作業としてやってます。移行の際にROS 2についていろいろ変というか変わった点が出てくるので、[これの前の記事](/?post=20240426)みたいにブログに書き留めています。パブリッシャの扱いとかも変わってるので、たぶん「その3」も書きます。

## kanataさんからサインもらた

　先日いただきました。また出版あるある話にお付き合いください。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">わたくしもいただきましたっ！（ご本人の人柄が出てて控えめ） <a href="https://t.co/XUS2X8sv8u">https://t.co/XUS2X8sv8u</a> <a href="https://t.co/zpNFKMIwUA">pic.twitter.com/zpNFKMIwUA</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1784065325841166446?ref_src=twsrc%5Etfw">April 27, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 某組織からキーボード届いた

　モニターやってとのこと。[ThinkPad教](https://news.mynavi.jp/techplus/kikaku/leaders_thinkpad-4/)から改宗させられるのかと思って最初反射的に抵抗したんですが、「そういうことではない落ち着け」となだめられて（？）、お引き受けしました。[お金はもらっておりません](https://ja.wikipedia.org/wiki/%E3%83%9A%E3%83%8B%E3%83%BC%E3%82%AA%E3%83%BC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E8%A9%90%E6%AC%BA%E4%BA%8B%E4%BB%B6)。ThinkPadの宣伝のほうはいただいております（書く必要があるのかどうかよくわかりませんが）。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">学生がキーボードの話してると「道具の話じゃなくて自分の作ってるものの話をしろ」と長年チクチク言ってたのがバレてて、某組織から悔い改めよと送付されてきたのでモニターやります・・・ステマじゃないです<br><br>当時、和田先生の影響なのか全部HHKBだった本郷の計算機センター以来ですね（👈トラウマ） <a href="https://t.co/o3CirLvUid">pic.twitter.com/o3CirLvUid</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1782329765229457727?ref_src=twsrc%5Etfw">April 22, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">昼休みなのでモニターしてるキーボードに合わせて環境構築しとる<br><br>mac側は自分が昔書いたウェブ記事を参考にしてて、とても参考になるので自分に感謝中 <a href="https://t.co/Q6bxT9s3jD">pic.twitter.com/Q6bxT9s3jD</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1782974316596097522?ref_src=twsrc%5Etfw">April 24, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
