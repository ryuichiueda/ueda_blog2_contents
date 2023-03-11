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

　まず、Ubuntu 22.04でも、`apt`で入れたDockerでは`docker compose`
（`docker-compose`ではない）が使えません。
そこで、

* [`docker compose`（docker コマンドのサブコマンドである compose）を全ユーザ向けにインストールする](https://qiita.com/JunkiHiroi/items/3bf722af3e77c73a1625#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)

の記述にしたがって、「全ユーザ向け」で`docker-compose`をインストールします。そのままコマンドを打っていけば大丈夫です。

