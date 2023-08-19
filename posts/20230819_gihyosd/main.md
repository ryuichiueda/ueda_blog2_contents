---
Keywords: 自作シェル, bash, 連載, Software Design
Copyright: (C) 2023 Ryuichi Ueda
---

# Software Design 9月号

　[発売されました](https://www.amazon.co.jp/shop/ryuichiueda/list/7MLC9JANITU0?ref_=aip_sf_list_spv_ofs_mixed_d)。自分の連載「[魅惑の自作シェルの世界](/?page=sd_rusty_bash)」が載ってます。・・・と、いつもブログがこの程度の情報量で終わってるような気がするので、今回は真面目に記事の説明をします。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">「魅惑の自作シェルの世界」もちろん今月も載っています！（Software Design 2023年9月号）<br>前号につづき、パイプライン処理を実装していきます。<a href="https://t.co/Vtpd0ebk9v">https://t.co/Vtpd0ebk9v</a> <a href="https://t.co/lfY8PiGwku">https://t.co/lfY8PiGwku</a> <a href="https://t.co/r9jS9iPdhK">pic.twitter.com/r9jS9iPdhK</a></p>&mdash; SoftwareDesign (@gihyosd) <a href="https://twitter.com/gihyosd/status/1692356276611887474?ref_src=twsrc%5Etfw">August 18, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## どんな連載か

　Rustを使ってBashのクローンを作るという内容です。Rustをちょっと触ってみたい人にはシェルが題材になり、自作シェルに興味のある人は、シェルの実装のしかた（文法やOSとのやりとり）をチェックできるということで、ぜひ読んでみたい連載です！（主観）

　自作シェルのコードについては連載が進むにしたがって増えて複雑になっていくわけですが、途中からでも参入できるように、全段階でのコードがGitHubのブランチに保存されています。初めて読む人でも、その回の開始の時点でのブランチを取り出して、そこにコードを足して挙動を試して遊べる工夫をしてあります。とりあえず写経でオッケーで、しかもシェルに機能を付け足すという高度なことができるので、満足度は高いんじゃないかと思ってます。

　使っている言語のRustについては、自身はベタな書き方しかしませんし、できません。かえって初めての人にはいいかなと思ってます（達人がよい先生とは限らないという話もありますし）。Rustの話でよく語られるまだライフタイム付きの変数も、ジェネリックスも今のところ不使用です。


## 今月の内容

　今月はざっとこんな感じで盛りだくさんです。

* コードにコメントを入れられるようにする
* コードの途中でバックスラッシュで改行を入れられるようにする
* 改行を入れたパイプラインを解釈して実行できるようにする
* パイプライン中で複合コマンドを使えるようにする
* ビルトインコマンドをパイプでつなげられるようにフォークする

最初の2つは、今月最初のブランチに反映済みで、解説だけですが、あとの3つは解説しながら実装していきます。これを7ページのなかでやってます。濃密に書いていますので、ぜひ読んでみてください！

↓チラ見せして終わります。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Software Design、帰宅して記事が無事に載ってるの確認しました。<br><br>今月はパイプラインの他、変態バックスラッシュ改行やコメントも話題にしてます<a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/kaOVmgKJ0c">pic.twitter.com/kaOVmgKJ0c</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1692788556115448228?ref_src=twsrc%5Etfw">August 19, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

