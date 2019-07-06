---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月6日）

## Cartographerいじり

　Cartographerをロボットで実行して、終わりに`map_saver`を実行し、軌跡をtsvファイルに保存するまでを、一つのローンチファイルを立ち上げたあと、PCを途中で触らないで実行できるようにした。SLAMが終わった後に`map_saver`を呼び出すというのがlaunchファイルでは表現できず、C++の中で`system`を使ってコマンドをそのまま与えた。ちゃんと動いた。

## Hadoop

　Hadoopのことを7,8年ぶりに思い出した。いったいあれはなんだったんだろ？

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ビッグデータという言葉が流行った時、プライド高い連中がシェルなどをロートルだと揶揄しながら、シェルなら数秒で終わるたかが数桁GB程度のデータ処理に、何十分もかけてHadoop使う珍事が全国的に多発していたであろうあの時期のことを俺は忘れないからな。<a href="https://t.co/eB2QmFp1oC">https://t.co/eB2QmFp1oC</a></p>&mdash; ぐれさん (@grethlen) <a href="https://twitter.com/grethlen/status/1147431442449874945?ref_src=twsrc%5Etfw">July 6, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

何十GBを数秒は計算機が1ノードでは辛いけど、たしかに10ノードあってうまく分散してあればシェル芸で数秒にはなります。「どんな速いストレージの話をしてるんだ？」というツッコミが入ってましたが、Unix系だとファイルがDRAMに乗ってることが想定できるんで、読み込みのコストはうまくやればほぼゼロで考えられます。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">10年くらい前、大手のベンダ各社がむりやりHadoopソリューション作ってお客さんに売ろうとしてたの、私も忘れられません・・・<br><br>Hadoop使うのにコンピュータたくさん必要で、たくさん売れるという本末転倒の・・・</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1147436586851659776?ref_src=twsrc%5Etfw">2019年7月6日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


あと、Hadpoopとミスタイプして叱られが生じるところだった。危ない。

　それから、私の見てきた業界の問題についてもちょっとツイートしたので残しておこうかと。
　
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">大企業のシステム部の部長さんって、10億のシステム導入したら、いろんなイベントよばれたり実績になったりするんですよね・・・（ほんとはPC2台で済むものであっても・・・）</p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1147436945888276481?ref_src=twsrc%5Etfw">July 6, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">で、こういうインセンティブで管理職が働いているので、なんとかペイみたいな問題は起こるべくして起こるという話なんですね・・・ <a href="https://t.co/EP6tS5Uaqt">https://t.co/EP6tS5Uaqt</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1147463952059662336?ref_src=twsrc%5Etfw">2019年7月6日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


寝る。
