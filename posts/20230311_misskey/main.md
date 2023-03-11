---
Keywords: 日記
Copyright: (C) 2023 Ryuichi Ueda
---

# MisskeyをUbunt22.04の入った手元のノートPC+Dockerで動かしたときのつまづきポイントのメモ

　なんでこんなことをしているかというと、
* 自分が運用している[mi.shellgei.org](https://mi.shellgei.org)のDBのデータを手元の環境で動かして、バックアップが完璧かどうか調べたい
* サーバーの爆発に備え、いつでもサーバーを復活させたいので訓練したい
* ノートPCの環境汚したくないので当然Dockerで動かしたい
からです。

## 環境

* OS: Ubuntu 22.04
* Docker version 20.10.21（ふつうに`apt install`でインストールしたもの）

標準環境ですが、Dockerに慣れてないと難しいです。

## 見ているマニュアル

https://misskey-hub.net/docs/install/docker.html の記述に沿ってやっていきます。

## つまづきポイント

