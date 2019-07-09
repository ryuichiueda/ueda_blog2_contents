---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月9日）

　今日は午前が事務。午後が講義やらミーティングやら。合間をぬってらスパイマウスの設定やソフトを整理。

## Netplan時代のWiFi power managementの切り方

　ラズパイでWiFiを使うときに必要な作業に「WiFiのpower managementをoffにする」というのがある。Ubuntu 18.04になってネットワーク設定が変わってやり方がわからなくなってうやむやにしてたら、昨日、ついにそれが原因で何時間も無駄にする事態が発生。ということで調査したら、これが一番楽そうという結論に至る。

```
$ sudo apt install wireless-tools
$ sudo crontab -e
（エディタが開くので以下の一行を追加）
@reboot /sbin/iwconfig wlan0 power off
（保存して閉じる）
$ sudo reboot
### 再起動したらPower Managementがoffになっていることを確認 ###
$ iwconfig
....
wlan0     ...
         Power Management:off    <---- 確認
```

## rosdep

　自分のリポジトリのREADMEを書くにあたり、自分のROS本でもスルーしてしまった`rosdep`を調査。`rosdep`は`package.xml`に書いた依存関係のあるパッケージをインストールしてくれる便利ツール。例えばラズパイマウスの基本パッケージの[raspimouse_ros_2](https://github.com/ryuichiueda/raspimouse_ros_2)は次のように`rosdep`を使うと必要なROSパッケージが全部入る。便利。

```
$ echo $ROS_PACKAGE_PATH
/home/ueda/catkin_ws/src:/opt/ros/melodic/share   #catkinのワークスペースがパスに入っている必要あり
$ rosdep install raspimouse_ros_2
（package.xmlに書いたパッケージのインストールが始まる）
```

　しかし、`raspimouse_ros_2`を使うパッケージの場合、こう打たないといけないっぽい。これは[raspimouse_cartographer](https://github.com/ryuichiueda/raspimouse_cartographer)をダウンロードして`rosdep`する場合。


```
$ git clone https://github.com/ryuichiueda/raspimouse_cartographer.git
$ rosdep install --ignore-src raspimouse_ros_2 raspimouse_cartographer
（package.xmlに書いたパッケージのインストールが始まる）
```

`raspimouse_ros_2`が同じ場所にあっても標準のパッケージだと思ってどこかに探しにいくので、それを`--ignore-src`で止めないといけない。

　で、こう書いているけどほんまかいなという感じなので、もっと良い情報があれば教えていただければ幸いでっす。

## アールティさんの仕事

　唐揚げロボットのインパクトはでかい。自分も間接的に手伝っててうれしいんだけど、伝え方がむずかしいのでひねくれた伝え方になる。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">上田研の某氏が暗躍している案件です。上田研としても微粒子レベルで協力してますがアールティさんと上田研の某氏の仕事です。 <a href="https://twitter.com/hashtag/%E4%B8%8A%E7%94%B0%E7%A0%94%E3%81%AE%E6%9F%90%E6%B0%8F?src=hash&amp;ref_src=twsrc%5Etfw">#上田研の某氏</a><br><br>弁当の盛りつけもしてくれる！料理するロボットの展示会 | NHKニュース   <a href="https://t.co/Huei2pM3sw">https://t.co/Huei2pM3sw</a></p>&mdash; CIT未ロボ上田研 (@uedalaboratory) <a href="https://twitter.com/uedalaboratory/status/1148588181559762944?ref_src=twsrc%5Etfw">July 9, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">こちらも。唐揚げのやつ。 | 食品製造の最新技術 “やさしい”ロボットとは？ TBS NEWS <a href="https://t.co/oXxPY0fLtS">https://t.co/oXxPY0fLtS</a></p>&mdash; CIT未ロボ上田研 (@uedalaboratory) <a href="https://twitter.com/uedalaboratory/status/1148588881090162688?ref_src=twsrc%5Etfw">July 9, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


自分が引っ張ってないと気が済まないのでなぜかライバル心が燃え盛っており。他の案件頑張ろう。実はロボット学会では別件でマニピュレータの研究の発表がある。マニピュレーションに関しては、某ピッキングチャレンジのおかげでやっと普通の人たちにも限界が見えてブームがおさまってきた。そこからが自分の役目だ、などと。


寝る。
