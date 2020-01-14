---
Keywords: 日記, 詳解確率ロボティクス, Ubuntu
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（〜2020年1月14日） 

　日記を完全にさぼっていた。

## 詳解確率ロボティクスが第3刷突入

　お陰様でまだ売れ続けています。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">【重版速報】<br>『詳解　確率ロボティクス』<br>上田隆一・著<a href="https://t.co/ZlzkrQbWyw">https://t.co/ZlzkrQbWyw</a><br><br>2/3重版出来予定 【3刷】<br><br>おかげさまで売れ行き好調につき、重版が決まりました。ありがとうございます！　電子書籍もあります。 <a href="https://t.co/IkBKSyvlHN">pic.twitter.com/IkBKSyvlHN</a></p>&mdash; 講談社サイエンティフィク (@kspub_kodansha) <a href="https://twitter.com/kspub_kodansha/status/1215486841673019392?ref_src=twsrc%5Etfw">January 10, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　Amazonよりも大学の生協で売れている印象です。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">大学生協「週刊 <a href="https://twitter.com/hashtag/%E6%96%B0%E5%88%8A%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0?src=hash&amp;ref_src=twsrc%5Etfw">#新刊ランキング</a>」理工書【1/13更新】にて<br><br>『日本人研究者のための論文の書き方・アクセプト術』が初登場で3位！<br>『統計モデルと推測』7位！<br>『Pythonで学ぶアルゴリズムとデータ構造』8位！<br>『詳解確率ロボティクス』10位！<br><br>Top10に4書目がランクインです！<a href="https://t.co/JfQd5LzZ5O">https://t.co/JfQd5LzZ5O</a> <a href="https://t.co/eFnVpToeek">pic.twitter.com/eFnVpToeek</a></p>&mdash; 講談社サイエンティフィク (@kspub_kodansha) <a href="https://twitter.com/kspub_kodansha/status/1217024081930813446?ref_src=twsrc%5Etfw">January 14, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## MacからThinkPadに変えた

　大した話でもないけど、メインのマシンを10年ぶりにMacからThinkPadに戻しました。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">Macを卒業しますた。<br><br>$ sudo dmidecode -s system-version<br>ThinkPad X1 Carbon 7th</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1214846598905098240?ref_src=twsrc%5Etfw">January 8, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


どうもこっちのほうがたくさん文章を書く人間にとってはよさそうだったので。それから、シェル芸botに投稿するときにいちいちコマンドを翻訳するのも面倒だったので・・・。

　OSはUbuntuなんですけど、一番困るのはAdobeのソフトが使えないことで、特に「論文に貼るepsをどう作るか」を自分が納得の行く方法で解決しないと、Windowsユーザになっちまいます（別にいいけど）。


　で、InkSpaceとGimpをとりあえずインストールしたんですけど、モニタの解像度が高すぎてアイコンの設定をどれだけいじっても大きくならない。しかもInkSpaceだとepsがいろいろめんどくさい。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">InkSpace、何をどう頑張ってもこれ以上アイコンが大きくならない問題。（左右両端にゴマみたいなアイコンがあるよ！） <a href="https://t.co/ZwZ23OPedX">pic.twitter.com/ZwZ23OPedX</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1217088578397696001?ref_src=twsrc%5Etfw">January 14, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　ということで、LibreOfficeのdrawを試したんですが、今度はどんな形状の図を保存してもA4サイズでしか保存されないという地獄。数日間断続的にいろいろ試したんですが、ものすごい微妙なところにチェックボックスを発見しますた。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">LibreOffice Drawで選択範囲だけepsで保存するの、こんなところ（左下）にチェックボックスがあったのね・・・何日間も悩んでしまった・・・ <a href="https://t.co/rbKrZevwfD">pic.twitter.com/rbKrZevwfD</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1217024950025932801?ref_src=twsrc%5Etfw">January 14, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


論文だとそんなに凝った作画はしないので、しばらくDrawで頑張ってみようと思います。

## jjを日本語で打ってしまう問題について対策

　VimでEscの代わりにjjと打つ設定を使っているのですが、よく日本語モードのまま打ってしまうので、日本語でもEscになるように設定ファイルを追記しました。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">これ、便利かな？？？ <a href="https://twitter.com/hashtag/%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E3%81%AB%E3%81%AF%E3%81%9F%E3%81%B6%E3%82%93%E3%82%8F%E3%81%8B%E3%82%8B?src=hash&amp;ref_src=twsrc%5Etfw">#わかる人にはたぶんわかる</a> <a href="https://t.co/lQNIOrCCSM">pic.twitter.com/lQNIOrCCSM</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1217089891902709760?ref_src=twsrc%5Etfw">January 14, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


ちゃんと動きます。


　日本語で「っｊ」と打った後は、英語に切り替えないといけませんが、慣れればもう一度「jj」と打つ手間が省けるはずなので、これもしばらくこのまま行ってみようと思います。


寝る。
