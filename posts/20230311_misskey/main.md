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

　ちょっと手こずったので、自分のためにメモしておすそ分けします。本家のドキュメントにプルリク出すべきかとも思ったのですが、バージョンの細かい話でお手を煩わせてもよくなさそうなので、こちらにメモということで。

## 環境

* OS: Ubuntu 22.04
* CPU: intel Core i9
* Docker version 20.10.21（ふつうに`apt install`でインストールしたもの）

標準環境ですが、Dockerに慣れてないと難しいです。あと`grep`に慣れてないと辛いとおもうので、ぜひ[シェル芸本](https://amzn.to/3T9tsDL)のご購入をご検討ください（宣伝）。

## 見ているマニュアル

https://misskey-hub.net/docs/install/docker.html の記述に沿ってやっていきます。

## つまづきポイント

### docker compose使えない

　まず、Ubuntu 22.04でも、`apt`で入れたDockerでは`docker compose`
（`docker-compose`ではない）が使えません。
そこで、

* [`docker compose`（docker コマンドのサブコマンドである compose）を全ユーザ向けにインストールする](https://qiita.com/JunkiHiroi/items/3bf722af3e77c73a1625#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)

の記述にしたがって、「全ユーザ向け」で`docker-compose`をインストールします。そのままコマンドを打っていけば大丈夫です。


### `COPY --link`

　GitHubからもってきたMisskeyの`Dockerfile`には、`COPY --link`という記述がありますが、たぶんPCのDockerのバージョンの関係からか、`--link`が使えません。こんなエラーが出ます。

```
$ sudo docker compose build
Sending build context to Docker daemon  149.6MB
1 error occurred:
	* Error response from daemon: dockerfile parse error line 22: Unknown flag: link
```

ということで、`--link`を消します。

```diff
$ git diff
・・・
-COPY --link ["pnpm-lock.yaml", "pnpm-workspace.yaml", "package.json", "./"]
・・・
+COPY  ["pnpm-lock.yaml", "pnpm-workspace.yaml", "package.json", "./"]
・・・
（他にもCOPY --linkの記述があるのでCOPYだけにする。）
```

たぶん大丈夫でしょう。たぶん・・・。だってビルドしないと先にすすめないんですもの・・・

### `ARG BUILDPLATFORM`

　次に、このようなエラーが出ました。

```bash
$ sudo docker compose build
[sudo] ueda のパスワード:
Sending build context to Docker daemon  149.6MB
Step 1/40 : ARG NODE_VERSION=18.13.0-bullseye
Step 2/40 : FROM --platform=$BUILDPLATFORM node:${NODE_VERSION} AS native-builder
1 error occurred:
	* Status: failed to parse platform : "" is an invalid component of "": platform specifier component must match "^[A-Za-z0-9_-]+$": invalid argument, Code: 1
```

これは、シェルスクリプトが読めれば分かりますが（←しつこい）、「`BUILDPLATFORM`がないから空になる」というエラーです。
ということで、`Dockerfile`に（x86_64のCPUなら）、`ARG NODE_VERSION`の下あたりに次のように追加します。なんとなく勘で`x86_64`と書いたら通りました。

```diff
ARG NODE_VERSION=18.13.0-bullseye    # <- もとからあるやつ
ARG BUILDPLATFORM=x86_64             # <- 追加
```

### `DOCKER_BUILDKIT=1`

　これでビルドが通るかな・・・と思ったら、次のようなエラーが出ました。

```bash
$ sudo docker compose build
（中略）
1 error occurred:
	* Status: the --mount option requires BuildKit. Refer to https://docs.docker.com/go/buildkit/ to learn how to build images with BuildKit enabled, Code: 1
```

「[BuildKit](https://docs.docker.jp/develop/develop-images/build_enhancements.html#to-enable-buildkit-builds)使え」ということのようです。次のように`docker`に変数を与えます。

```bash
$ sudo DOCKER_BUILDKIT=1 docker compose build
```

## そのほかのつまづきポイント

　この後は、設定ファイルのDBの名前やユーザー等が`example...`のままだったといったミスがありました。これはエラーログを読めば分かると思いますので、割愛します。


　現場からは以上です。これでまたなにか問題が起きたら追記します。
