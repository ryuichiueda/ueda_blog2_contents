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


「全部インストールしたらストレージもったいない」は、
OverleafでネットワークとデータセンタのCPU無駄づかいしてた人が言ってはいけません。
