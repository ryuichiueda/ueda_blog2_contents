---
Keywords: 日記, ROS, CMake
Copyright: (C) 2022 Ryuichi Ueda
---

# 最近のママ活ならぬシェル活について

　最近、妙に忙しくて全然ブログを更新してないんですが、忙しいながらも研究以外の活動もしているので、メモしておきます。

## シェルを書いている

　「あ？お前の書いているのはシェルスクリプトだろ？」と物議を醸す「シェルを書いている」発言ですが、本当にシェル（bash）を書いてます。BSDライセンスにして、GPLじゃないbashを目指してます。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">本日某所で手伝ってと泣きをいれましたが、「あんなぐちゃぐちゃなもの（bash）ちゃんと実装できるの？」とびっくりされました（）<br><br>いま、自分で使うためにaliasの実装をしてます。<a href="https://twitter.com/hashtag/rusty_bash?src=hash&amp;ref_src=twsrc%5Etfw">#rusty_bash</a><a href="https://t.co/EmMlWYGhsi">https://t.co/EmMlWYGhsi</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1534503116971732992?ref_src=twsrc%5Etfw">June 8, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

こういうのって、開発日誌とか言ってこまめにブログとかで説明を書いてチンタラ作るのがいいんですが、短気なので、一気に実装をすすめてます。ただ、bashはやっぱりややこしいのであと数ヶ月はかかりそうです。

　何がややこしいかというと引数です。引数というと、たとえば普通は`"hoge"`とか`'fuge'`、`$(ls)`、`${PATH}`というようなものを思い浮かべるわけですが、シェルのクオートって、途中から始まってもいいので、ちゃんとシェルを実装しようとすると、`echo {~,~ueda}/"aho"'unko'$(echo ${PATH})"${HOME}"`のような凶悪な引数も捌かなければなりません。

　で、がんばってbashを真似した結果がこれです・・・。たまたまうまくいっただけかもしれませんが。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">この努力を誰か買ってほしい💩<br><br>（上の出力が <a href="https://twitter.com/hashtag/rusty_bash?src=hash&amp;ref_src=twsrc%5Etfw">#rusty_bash</a> の出力で、下のが本家bashの出力。）<a href="https://twitter.com/hashtag/rusty_bash?src=hash&amp;ref_src=twsrc%5Etfw">#rusty_bash</a> <a href="https://t.co/CajIWopNnP">pic.twitter.com/CajIWopNnP</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1534505977768095744?ref_src=twsrc%5Etfw">June 8, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

以前にもC++でオレオレシェルを作ったことがあるんですが、 **そのときはパイプラインの実装ばっかりこだわっていたので、シェルの引数の凶悪さには気づいてませんでした** 。こういうのって、結局自分で実装しないと分かんないですよね・・・。

　bashの引数については、今度またシェル芸勉強会のLTででも話をしたいと思います。あと、一緒に作ってくれる人募集中です。今後とも、「シェル評論家」ではなく「シェル実践者」であるよう、精進するのみです。

## 次のシェル芸勉強会

　7/2に古巣のUSP研究所で行います。久しぶりのオンサイトで恐る恐るですが、よろしくお願いいたしますー。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">echo まだまだ募集中です。 <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a><br><br>jus共催 第60回記念帰ってきたシェル芸勉強会 <a href="https://t.co/BLtYEwq3q2">https://t.co/BLtYEwq3q2</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1534501693227880448?ref_src=twsrc%5Etfw">June 8, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


現場からは以上です。
