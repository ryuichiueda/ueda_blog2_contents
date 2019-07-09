---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月9日）

　今日は午前が事務。午後が講義やらミーティングやら。合間をぬってらスパイマウスの設定やソフトを整理。

## Netplan時代のWiFi power managementの切り方

　ロボットに乗っけたラズパイでWiFiを使うときに絶対必要な作業に「WiFiのpower managementをoffにする」というのがある。Ubuntu 18.04になってネットワーク設定が変わってやり方がわからなくなってうやむやにしてたら、昨日、ついにそれが原因で何時間も無駄にする事態が発生。ということで調査したら、これが一番楽そうという結論に至る。

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
