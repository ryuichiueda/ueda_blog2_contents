---
Keywords: LaTeX, TDP
Copyright: (C) 2024 Ryuichi Ueda
---

# WindowsにWSL（とevince）でLaTeX使う環境を整える

　なんかよう知らんのですが、IEEEでOverleafがタダで使えねーとかいうツイートがあふれたので、
そんなもん使わないロートルのわたくしが、ローカルでLaTeXで書き物する環境の設定方法を書いておきます。
WSLとTeX Liveとevinceを使います。evinceが快適に開発するキモです。
evinceがなにか分からない人は読むといいと思います。

　「効率わりーよ」という文句については、上田がどれだけ筆が早いか、何冊LaTeXで本を書いているのか、よく考えてから言ってください。（なんでけんか腰なんだ？？？）

　まじめな話、原稿は画面を開いたらすぐ書けるのが重要です。いちいち重たいアプリとかネットアプリを開くのは、気分が乗っていればいいのかもしれませんが、そうでないときは「やっぱ書くのやめておこう」という負の動機にしかなりません。


## 準備

　まず、WSLをインストールします。
[Microsoftのページ](https://learn.microsoft.com/ja-jp/windows/wsl/install)
の指示に従いましょう。字を読むのが面倒という究極のものぐさの人のために、過去動画を撮ったことがあるので、それも掲載しておきます。ただ、やり方が古くなっている可能性もあります。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Fm9uH5QH8QA?si=RCx42cTX5Skgx7iO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## TeX Liveをインストールする

　ラブライブ！ではありません。[TeX Live](https://texwiki.texjp.org/?TeX%20Live)です。
興奮しないでください。
落ち着いて次のように **全部インストールします** 。

```sh
（$マークは打たなくていいですよー）
$ sudo apt update
（パスワード打ってね）
$ sudo apt install texlive*
（なんか聞かれるのでYと答えましょう）
（もうひとつWSLでUbuntuを開いて、先に下の「テンプレートを落としてくる」をやってもいいです）
（ひたすら待つ）
・・・
Building format(s) --all.
        This may take some time... done.
Processing triggers for sgml-base (1.29.1) ...
Processing triggers for libgdk-pixbuf2.0-0:amd64 (2.40.0+dfsg-3ubuntu0.4) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link

ueda@uedaP1Gen6:~$
```


「全部インストールしたらSSDもったいない」は、
OverleafでネットワークとデータセンタのCPU無駄づかいしてた人が言ってはいけません。


## テンプレートを落としてくる

　[ロボット学会誌のテンプレートのページ](https://www.rsj.or.jp/pub/jrsj/info/stylefile.html)
から、「LaTeX2e クラスファイル（論文／一般記事両用）」にある

* クラスファイル (UTF)
* クラスファイルの解説 (UTF)
* 「一般記事」の見出しの飾り(eps)

をダウンロードします。
次のように操作して、`test`の下に3つのファイルを置きましょう。
```sh

$ mkdir test
$ cd test
$ wget https://www.rsj.or.jp/content/files/pub/jrsj/stylefile/JRSJ-latex2eutf/jrsj.cls
$ wget https://www.rsj.or.jp/content/files/pub/jrsj/stylefile/JRSJ-latex2eutf/howtouse.tex
$ wget https://www.rsj.or.jp/content/files/pub/jrsj/stylefile/JRSJ-latex2e/rsjarrow.eps
### lsして3つのファイルがあるか確認しましょう ###
$ ls
howtouse.tex  jrsj.cls  rsjarrow.eps
```


　また、

```sh
$ explorer.exe .
```

でWSLのホームをエクスプローラで開けますので、コマンドの操作が不安ならお使いください。
`wget`を使わず、エクスプローラ上で上記の3つのファイルを保存してもよいでしょう。

## とりあえずpdfファイルを作ってみる

　`test`の中で、次のようにコマンドを打ちます。
面倒なので、これをコマンド一発にする方法は、また後日説明します。

```bash
（platexは2回実行します。）
$ platex howtouse.tex        #dviファイルを作ります
$ platex howtouse.tex        #図版とか引用を正しくするにはもう1回必要
$ dvipdfmx howtouse.dvi      #これがpdfを作るコマンド
howtouse.dvi -> howtouse.pdf
[1][2][3][4][5][6][7]
308238 bytes written
### pdfができた！！！###
$ ls howtouse.pdf
howtouse.pdf
```

## evince

　これで「どうやってpdfファイル見るの？」となると思います。
ひとつの方法は`explorer.exe .`して、ダブルクリックでWindows側のビューワーを使うものです。
ただ、pdfが更新されても、自動的に表示を更新してくれないビューワーがほとんどだと思われます。

　そこで、WSLにevinceをインストールして使いましょう。

```bash

$ sudo apt install evince
（インストール作業）
$ evince howtouse.pdf
```

これで次のように、pdfが閲覧できるようになります。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">WSLでevinceを使っている図 <a href="https://t.co/VEC4x6zXLU">pic.twitter.com/VEC4x6zXLU</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1772206504189243438?ref_src=twsrc%5Etfw">March 25, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

これでhowtouse.texファイルを適当にいじって、再度`platex, platex, dvipdfmx`してみましょう。
自動的にpdfの表示が更新されるはずです。


## おわりに

　あとはフォントをごにょごにょしたりコマンドたくさん打つのを楽にしたりといろいろやることがありますが、それはまたあとでということにします。


現場からは以上です。


