---
Keywords: シェル芸
Copyright: (C) 2019 Ryuichi Ueda
---

# ラズパイマウスのRaspberry PiをB3からB3+にのっけ変える

　午後に研究の準備のために久しぶりに[ラズパイマウス](https://www.rt-shop.jp/index.php?main_page=product_info&products_id=3419)いじりをしたのメモ。やったことは

* Raspberry Pi 3Bを3B+にのっけかえ
* 3B+にUbuntu 16.04をセットアップ
* その他、自分の古い知識をアップデート

でした。なお、以前は3B+で使おうとすると大変だったUbuntu 18.04も今はすんなり使えるらしいということが、帰り際に[このブログの主](https://memoteki.net/archives/1686)と[このブログの主](https://www.asrobot.me/entry/2018/07/05/045832/)と話をして判明したんですけど、16.04のことをメモしておきます。細かい説明は他の方のブログに委ねています。


## GPG keyの変更

　まず、これはUbuntuのバージョンは関係ないのですが、ROSをインストールしたりアップデートしたりするときに使う鍵が変更になったとのこと。下のツイートのURLで新しい鍵の設定方法が書いてあります（`sudo apt-key adv ...`のコマンドを、ディレクトリはどこでもいいのでシェルから実行）。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">[status] Resolved: <a href="https://t.co/gji4g0EBuM">https://t.co/gji4g0EBuM</a> is back online. Please make sure to update your GPG keys: <a href="https://t.co/ocHyqwGJcP">https://t.co/ocHyqwGJcP</a> <a href="https://t.co/bQHmSLnynG">https://t.co/bQHmSLnynG</a></p>&mdash; ROS (@rosorg) <a href="https://twitter.com/rosorg/status/1139224563013713920?ref_src=twsrc%5Etfw">June 13, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## イメージの調達

　[こちらから](https://www.asrobot.me/entry/2018/07/11/001603/)、「カーネルコンパイル済み」のイメージをダウンロード。このイメージ、UbuntuなんだけどカーネルはRaspbian用という変態仕様です。また、無線LANとかもちゃんと使えます。

## イメージをmicroSDカードに

　`dd`に`conv=fsync`をつけないと失敗率がとても高いようです。必要と言われ始めてからしばらくはそこまで失敗する率は高くなかったんですが・・・。詳しくはあっきぃさんのブログにて。

* http://akkiesoft.hatenablog.jp/entry/20170815/1502725191


　あとはmicroSDカードをRaspberry Pi 3B+にさしてセットアップを続行しますが、これはもうそんなに特殊なことはないので割愛します。ただ、ラズパイマウスのドライバはUbuntuではなく、Raspbianの方法で作らなければなりませんが、リポジトリ内にあるこの[スクリプト](https://github.com/rt-net/RaspberryPiMouse/blob/master/utils/build_install.bash)を使えば勝手にやってくれます。


　以上、あんまり手順書らしくないメモ書きになってしまいましたが、ROSの本の読者のみなさまは[こちら](https://github.com/ryuichiueda/raspimouse_book_info)で遠慮なく聞いていただければと。たまにメールもいただくのですが、GitHubでご質問は共有したいです。また、この前、メールで名乗らないでUbuntu MATEの対応をお願いしてきた人がいたのですが、流石にご勘弁を・・・。
