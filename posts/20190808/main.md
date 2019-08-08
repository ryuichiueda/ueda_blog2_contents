---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年8月8日）

　2年の実習のために[MoveIt!](https://moveit.ros.org/)をがちゃがちゃ動かす。[資料](https://ryuichiueda.github.io/manipulator_practice_b3/lesson2.html)、わずかに進む。GUIを使ったツールは資料にするのが面倒。その後、修士卒氏の残したコードのリファクタリング。


　MoveIt!については、とりあえずThinkPadの赤ポッチで↓のような行動を作ったけど、赤ポッチやタッチパッド、あるいはマウス使うくらいなら自分でプログラミングした方が楽なので、「マウスでロボットを動かしてみましょう」というナンパな資料はやめて、プログラミングゴリゴリの内容にしようと思った。学生にも各自のノートPCのタッチパッドをあらかじめ破壊の上、プログラムを書かせる予定（あくまで予定）。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">学生にラリアットをかますスタンハンセン型マニピュレータ <a href="https://twitter.com/hashtag/%E3%83%80%E3%83%A1?src=hash&amp;ref_src=twsrc%5Etfw">#ダメ</a> <a href="https://t.co/UslAq4YAan">pic.twitter.com/UslAq4YAan</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1159277698608271360?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## シェル芸bot界隈のひとたち

　シェル芸botのまわりでは、いろんな人がゆるく連携してコミュニティーを形成しています。私はGMOさんにコミュニティー支援の一環で貸していただいている[ConoHa](https://www.conoha.jp/)のVPSを解放して、サーバ管理しています。シェル芸botの作者は[@theoldmoon0602](https://twitter.com/theoldmoon0602)さんです。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">シェル芸botの開発と運用してるふるつき氏はほんと超ヤバいんだけど、サーバ貸してる上田さんとか、コンテナを超最適化したsoさん、textimgで表現の幅を広げた次郎さん、キングウンコでプロモーションしたblacknonさんとか色々な人の活動が今の活気に繋がっていると思うのです!</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1159400819638382592?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote>

<blockquote class="twitter-tweet" data-conversation="none"><p lang="ja" dir="ltr">今の活気への貢献という観点だと、echo-sd作者のふみやすさんの貢献もかなり大きい気がする。SGWeb作者の貢献も後々効いてくるように見える。というかそう考えると色々人絡んでるな。話題作りという観点だと難読化勢は忘れてはいけないし。。。（ついていけてない）。</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1159404622773202944?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

シェル芸botの作者が私とかいうツイートがあったのですが、ツイートの前に裏をとれるはずですので、慎重にしていただければと。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">多くの人が自然にからんでるの重要ですよねー。</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1159401639549100032?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-conversation="none"><p lang="ja" dir="ltr">一方私はojichatで民度を下げた（白目）</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1159401286946709504?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

↑は謙遜で、めっちゃ盛り上げ役です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">本日のLTで発表した資料です。<br>また皆様にお会い出来るのを楽しみにしています。<br><br>シェル芸始末書 - <a href="https://t.co/UGRGNPn3Wo">https://t.co/UGRGNPn3Wo</a><a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/982639011427639297?ref_src=twsrc%5Etfw">April 7, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

シェル芸界隈に💩をhoge代わりに使うことを持ち込んだ功績も加えたいところです。知り合いになるどころかシェル芸という言葉ができる以前からこういう感じだったし・・・（当時かなりの衝撃）


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/null?ref_src=twsrc%5Etfw">@null</a> んうここうこうんんこここうこんううこうんんうここうんうんこうんうこんんううこんんんこんうんこうんんうんんうこうんんんうこうんうんうここここううんうんこうこんんうここんこここうこんうんうんここううここうんうんううん<br>うんこは4個でてきました！<br>うこんは5個でてきました！</p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/173276836678205440?ref_src=twsrc%5Etfw">February 25, 2012</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

もっと見たい人はこのリンクをどうぞ（しろめ）。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">うん。 <a href="https://twitter.com/grethlen?ref_src=twsrc%5Etfw">@grethlen</a> 氏と初めて出会ったときは、こんな感じだった。（やばい）<a href="https://t.co/abEOROhekJ">https://t.co/abEOROhekJ</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1159468555034738689?ref_src=twsrc%5Etfw">August 8, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



寝る。
