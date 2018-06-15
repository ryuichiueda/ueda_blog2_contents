---
Keywords: Raspberry Pi, Ubuntu, メモ
Copyright: (C) 2018 Ryuichi Ueda
---

# Raspberry Pi 3にUbuntu 18.04

https://wiki.ubuntu.com/ARM/RaspberryPi のUnofficial images
（ubuntu-18.04-preinstalled-server-armhf+raspi3.img.xz）を試したメモ。

## 起動

ddでイメージをmicroSDにコピーしたらすんなり起動。cloud-init関係のログが邪魔するので起動したかどうか紛らわしい。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ここで止まる <a href="https://t.co/MDQuLHycSE">pic.twitter.com/MDQuLHycSE</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1007472741463699457?ref_src=twsrc%5Etfw">June 15, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">あ、これ起動してたけどワーニングみたいなのが出てたのか・・・</p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1007473468206485504?ref_src=twsrc%5Etfw">June 15, 2018</a></blockquote>


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">起動した。 <a href="https://t.co/szht8TZzj1">pic.twitter.com/szht8TZzj1</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1007474157481648129?ref_src=twsrc%5Etfw">June 15, 2018</a></blockquote>


## アップデート

Ubuntu 16.04の時はアップデートするたびに起動しなかったりWiFi使えなかったりとトラブルがあったけど・・・普通に立ち上がる。ただ、ネットワークが死んでsshで入れないということが一回起こる。

```
$ sudo apt update 
### 自動アップデートをぶち殺して・・・ ###
$ sudo apt upgrade
$ sudo reboot
### 一度、ネットワークが死んでsshで入れず ###
$ sudo apt install wireless-tools #ワイヤレスツールを入れる
$ sudo apt purge cloud-init #こいつがUTF8でもないクソログを吐くので追い出し
```

で、wlan0がなくなる。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">あーやっぱり。wlan0がなくなる。 <a href="https://t.co/n6Bc27s5d8">pic.twitter.com/n6Bc27s5d8</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1007481979082715136?ref_src=twsrc%5Etfw">June 15, 2018</a></blockquote>

が、復活。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">これで復活。<a href="https://t.co/fACwYMJgXp">https://t.co/fACwYMJgXp</a> <a href="https://t.co/oRnPuewCRD">pic.twitter.com/oRnPuewCRD</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1007482970301607937?ref_src=twsrc%5Etfw">June 15, 2018</a></blockquote>


とりあえず今日はここまで。
