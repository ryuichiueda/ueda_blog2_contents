---
Keywords: Raspberry Pi, Ubuntu
Copyright: (C) 2017 Ryuichi Ueda
---

# Raspberry Pi 3用Ubuntu Server 16.04.3 LTSイメージを更新

https://wiki.ubuntu.com/ARM/RaspberryPi のイメージがバグを含んだままさっぱり更新されないので、勝手にバグフィックスしたものを公開しています。もちろんライセンスはGPLということになろうかと。今日作ったのは

* `/boot/firmware/config.txt`に書いてある`device_tree_address`が間違っているので修正（ひでえ）
* カーネルをLinux ubuntu 4.4.0-1080-raspi2にアップデート
* カーネルのアップデートでwifiが使えなくなる問題の修正
* その他ソフトウェアのアップデート

を施したものです。ダウンロードは以下から。

* http://file.ueda.tech/RPIM_BOOK/ubuntu-16.04-preinstalled-server-armhf+raspi3-upgradable-20171223.img.xz

後から気づいた小さいバグが一つあるんですが、`/var/log/lastlog`を消してしまったので`lastlog`が使えません。使いたい場合は自身で`/var/log/lastlog`を作る必要があります。

有効にお使いください。

