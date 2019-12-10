---
Keywords: Raspberry Pi,Ubuntu
Copyright: (C) 2019 Ryuichi Ueda
---

# Raspberry Pi 3B+用Ubuntu 18.04+ROSイメージ

　作りました。

## 材料

* https://wiki.ubuntu.com/ARM/RaspberryPi の「Raspberry Pi 3B/3B+: ubuntu-18.04.2-preinstalled-server-armhf+raspi3.img.xz」
* https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server


## できたイメージ

* [ubuntu-18.04.2-preinstalled-server-armhf+raspi3-ROS-20190618.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-18.04.2-preinstalled-server-armhf+raspi3-ROS-20190618.img.xz)
    * Raspberry Pi 3B+用のUbuntu 18.04にROSをインストールしたもの
* [ubuntu-18.04.2-preinstalled-server-armhf+raspi3-ROS-raspimouse-20190618.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-18.04.2-preinstalled-server-armhf+raspi3-ROS-raspimouse-20190618.img.xz)
    * Raspberry Pi 3B+用のUbuntu 18.04にROSとラズパイマウスのドライバをインストールしたもの

## 有線LANの設定

イメージ内のネットワーク設定を少しいじらないと、有線LANが起動時に使えません。下記のツイートのようにmacアドレスの書き換えをお願いします。
（無線の方はなんにも設定してません。）

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">起動時にLANを生かす方法<br><br>1. ip l（える） show eth0でeth0のmacアドレスを調べる。<br><br>$ ip l show eth0<br>2: eth0: <br>・・・<br> link/ether b8:27:eb:d7:c2:e7 brd ff:ff:ff:ff:ff:ff<br><br>ということで、「b8:27:eb:d7:c2:e7」<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1204250890158268417?ref_src=twsrc%5Etfw">December 10, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">2. /etc/netplan/50-cloud-init.yamlのmacアドレスを書き換える。<br><br>$ sudo vi /etc/netplan/50-cloud-init.yaml<br><br>図のようにmacアドレスを書くところがあるので、これを書き換える。<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a> <a href="https://t.co/pLcibyjNe7">pic.twitter.com/pLcibyjNe7</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1204251304605863943?ref_src=twsrc%5Etfw">December 10, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">3. <br><br>$ sudo reboot<br><br>これでeth0にIPアドレスが割り振られる。<br>以上。l<a href="https://twitter.com/hashtag/CIT%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E5%AD%A6?src=hash&amp;ref_src=twsrc%5Etfw">#CITロボットシステム学</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1204251479936094208?ref_src=twsrc%5Etfw">December 10, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 注意

16GBのmicroSDで作ったので、他の16GBのmicroSDに`dd`したときに微妙にはみ出るかもしれません。

以上です。
