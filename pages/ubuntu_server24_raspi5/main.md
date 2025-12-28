---
Keywords: Linux, Ubuntu, Raspberry Pi 
Copyright: (C) Ryuichi Ueda 2025
---

# Ubuntu Server 24.04 LTSをラズパイ5にインストールする方法

　書籍のための情報です。基本、ラズパイ財団のツールを使うだけです。ユーザー情報やWiFiの設定もツールでできて便利です。

## 用意するもの

* microSDカード
    * （私はよくわかってないのですが）高速なもの
    * 容量は16GB以上
* 普段使っているPC（次に説明するRaspberry Pi Imagerをインストールします）
    * microSDカードが読み書きできるようにカードリーダーも用意しましょう
* Raspberry Pi（このページではRaspberry Pi 5を想定）
    * キーボードやケーブル類、モニタ（テレビ）も

## Raspberry Pi Imagerのインストール

　[Raspberry Pi 財団のページ](https://www.raspberrypi.com/software/)から、「Raspberry Pi Imager」をインストールします。macOS用、Windows用、Linux用がありますが、以下ではmacOS用をもとに説明します。Windows版もほとんど同じものと思われます。

## Raspberry Pi Imagerの立ち上げ+ラズパイの選択

　通常のアプリの立ち上げ方でRaspberry Pi Imagerを立ち上げると、次のような画面が出るので、セットアップ対象のRaspberry Piのバージョンを選択します。

![](./app_top.png)

## OSの選択

　右側の画面をスクロールして「Other general-purpose OS」を選び、さらに「Ubuntu」を選びます。そして、「Ubuntu Server 24.04.x LTS（64-bit）」を選びます。xの数字は変わるかもしれません。執筆時点では24.04.3が選べました。下の図は、当該のバージョンを選択しているところです。「コンピュータにキャッシュ」とありますが、初回は「Online xx GB download」となっているはずです。

![](./choose_ubuntu.png)
