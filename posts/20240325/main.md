---
Keywords: LaTeX, TDP
Copyright: (C) 2024 Ryuichi Ueda
---

# WindowsにWSLでLaTeX使う環境を整える

　なんかよう知らんのですが、IEEEでOverleafがタダで使えねーとかいうツイートがあふれたので、
そんなもん使わないロートルのわたくしが、ローカルでLaTeXで書き物する環境の設定方法を書いておきます。
WSLとTeX Liveとevinceを使います。evinceが快適に開発するキモです。
evinceがなにか分からない人は読むといいと思います。


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

## とりあえずpdfファイルを作ってみる


```bash
（platexは2回実行します。）
$ platex howtouse.tex
$ platex howtouse.tex
t$ dvipdfmx howtouse.dvi
howtouse.dvi -> howtouse.pdf
[1][2][3][4][5][6][7]
308238 bytes written
### pdfができた！！！###
$ ls howtouse.pdf
howtouse.pdf
```
