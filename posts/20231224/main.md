---
Keywords: 自作シェル
Copyright: (C) 2023 Ryuichi Ueda
---

# 自作シェルのリポジトリの整理

　一人で更新を続けていた自作Bashクローンシェルの[Rusty Bash](https://github.com/shellgei/rusty_bash)にプルリクをいただいたので、リポジトリを整理しました。

## 整理の内容

　整理前まで、リポジトリの中に、次の2つの系統の実装が混在していました。

* 連載開始前に手探りで実装していたmainブランチ（コードがきたないのでいつか捨てるつもりだった）
* 人に説明しながら理路整然と実装している[連載](/?page=sd_rusty_bash)用のブランチ（sdで名前が始まるブランチ）

このふたつの系統、もうかなり乖離してマージが不可能になっていたんですが、mainのほうにプルリクをいただいて、これは混乱させているということで、連載のほうを新たにmainにして、いままでmainだったものをold_mainというブランチにしました。現在のmainは、2024年7月号で紹介予定の内容を反映したものになっています。

## 開発・プルリク用も準備しました

　この変更での問題は、新たなmainブランチは原稿を書きながら開発を続けないといけないことです。そうしないと、また連載と内容が乖離していきます。現在は来年の7月号まで進んでしまっており、8月号の原稿を書かないと先に進めません。そこで、

* dev-○○: というブランチで新たな開発や、プルリクを受ける

というルールを作りました。たとえば、dev-builtinsではビルトインコマンドを作るとか、dev-argsでは引数に関する実装を進めるとか。現在の一覧です。

<a href="https://github.com/shellgei/rusty_bash/branches"><img width="50%" src="https://mi.shellgei.org/files/fd605cc7-8c22-48a9-8a23-48402dcaa58e" /></a>

で、[きゃろさん](https://mi.shellgei.org/@caro)からdev-builtinsにさっそく2回プルリクをいただきました。ありがとうございます。早めに連載のコードに取り込んで謝辞を書きたいです。（7月号まで原稿が進んじゃっているんですが・・・）

　あと、プルリクいただいた方には、なるべくご飯おごります。

　他、dev-argsでブレース展開のきれいな実装を模索したり、dev-compoundsでifを実装したりと、将来の連載の内容を試しているので、先のことを知りたい人は、覗いてみると良いかと思います。


以上です。ご協力おねがいいたします！質問にはなるべくお答えします。
