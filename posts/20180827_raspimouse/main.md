---
Keywords: Rasberry Pi Mouse,Raspberry Pi
Copyright: (C) 2018 Ryuichi Ueda
---

# Raspberry Pi MouseをRaspberry Pi Mouse 3 B+で動かす 

手順のメモです。

## 1. イメージをmicroSDに焼く

* https://www.asrobot.me/entry/2018/07/11/001603 の「アップグレード＆ROS Kinetic＆カーネルコンパイル済み」を使いましょう。
* [ラズパイマウス本](https://amzn.to/2wsBY75)の付録を見てパーティションを拡大。

## 2. デバイスドライバとか

* https://github.com/rt-net/RaspberryPiMouse をクローンして、`utils`ディレクトリに行き、`build_install.raspbian.bash`の方を実行します。`build_install.ubuntu14.bash`ではありません。（カーネルを独自ビルドしたイメージのため）
* https://github.com/ryuichiueda/pimouse_setup をクローンして`sudo make install` して再起動後もデバイスドライバが使えるようにする


## 3. ROSを乗っけるなりなんなり

これは従来と同じ方法で大丈夫です。


以上で問題なく動作することを確認済みです。

