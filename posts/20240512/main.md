---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記というか週報というか（〜2024年5月12日）

　ゴールデンウィークのしわ寄せで大学の事務が超絶溜まってます。査読も溜まってます。査読投げないで。

## [自作シェル](/?page=rusty_bash)

　もう普通に常用のシェルになりました（`!$`が使えなくてたまに困りますが）。先週からは補完の完成度が少しあがっているはずです（エイリアスとかも補完できます）。あと、下記のbash-completionはまだ使えませんが、自分でシェルスクリプトを書いて`source`すれば補完をカスタマイズできるところまできました。今度解説でも書きます。

　当然まだBashのほうが便利ですが、Gitのディレクトリ内でブランチがプロンプトに表示されるとかいろいろ便利なので、ぜひぜひmainブランチをビルドして使ってみていただければと。[リポジトリはここです](https://github.com/shellgei/rusty_bash)。

　いまは[bash-completion](https://blog.cybozu.io/entry/2016/09/26/080000)に対応するために文法を強化しています。`case`文とかグロブの拡張（`@(...)`みたいなやつ）とか、普段は全く使わないんですが、外部のシェルスクリプトで書かれたライブラリを読むときに必要になります。特に`bash-completion`のコードは圧巻なので大変です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">このコードを全部読み込めたとき、<a href="https://twitter.com/hashtag/SoftwareDesign?src=hash&amp;ref_src=twsrc%5Etfw">#SoftwareDesign</a> 連載中の <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> がほぼ完成する・・・（何年かかるんだ？？？）<a href="https://t.co/5RPEJSWgWU">https://t.co/5RPEJSWgWU</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1788801748276035725?ref_src=twsrc%5Etfw">May 10, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 研究

　[先日からやってたロボットのナビゲーションソフトのROS 2への移行](https://b.ueda.tech/?post=20240502#%E4%BE%A1%E5%80%A4%E5%8F%8D%E5%BE%A9%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%82%92ros-1%E3%81%8B%E3%82%89ros-2%E3%81%B8%E7%A7%BB%E8%A1%8C%E4%B8%AD)ですが、が大体終わりました。学生さんがこれつかって研究するということで慌てて[README](https://github.com/ryuichiueda/value_iteration2/blob/main/README.md)書きました。ディテールだめだめですが、いちおう次の動画のように動きます。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">value_iterations2のREADME用の動画つくった（障害物置いたり最初の猫みせたりしてつくりなおした）<a href="https://t.co/WWMRk1WxUK">https://t.co/WWMRk1WxUK</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1789111593412034858?ref_src=twsrc%5Etfw">May 11, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　また、ついでにROS 2のインストールスクリプトをUbuntu 24.04に対応しました（1行追加しただけ）。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">もっといいインストーラがあるかもしれませんが、ROS 2のインストールスクリプト、Ubuntu 24.04に対応しました<a href="https://t.co/bIAReImldF">https://t.co/bIAReImldF</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1788809885729304952?ref_src=twsrc%5Etfw">May 10, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 中部大での確率ロボティクスの講義

　[前の週](https://github.com/ryuichiueda/value_iteration2/blob/main/README.md)にひきつづき、水曜日に第二回がありました。なぜかスライドが人気です。1週目のスライドが9400viewとかいってますけどホントでしょうか。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">本日の講義資料です～～～～が、16ページまでしかいきませんでした懺悔 <a href="https://t.co/KF79CGEsMH">https://t.co/KF79CGEsMH</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1788104263660630105?ref_src=twsrc%5Etfw">May 8, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 次のシェル芸勉強会

　6/15にやりたいなあと考えてます。


以上です。

