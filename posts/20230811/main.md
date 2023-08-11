---
Keywords: 日記, Misskey
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年8月11日。書きかけ）

　Misskeyのサーバーいじりと小銭稼ぎの話。

## Misskeyのアップデート

　さくらのVPS（メモリ1GB）、Docker不使用でなんとか運営している[しぇるげいすきー](https://mi.shellgei.org/)のバージョンアップ作業をしました。途中ビルドがコケて肝を冷やしました。


### トラブル

　[このページのアップデート方法](https://misskey-hub.net/docs/install/manual.html#misskey%E3%81%AE%E3%82%A2%E3%83%83%E3%83%95%E3%82%9A%E3%83%86%E3%82%99%E3%83%BC%E3%83%88%E6%96%B9%E6%B3%95)の`NODE_ENV=production pnpm run build`をしているときに、次のようなエラーが出ました。

<iframe src="https://embed.misskey.io/notes/9i9xcoi9kp"></iframe>
https://misskey.io/notes/9i9xcoi9kp


`FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory`ということなので、ビルドのためのメモリが足らないと。そりゃ最近のメモリバカ食いシステムだと1GBは辛いですね・・・。

　で https://github.com/vitejs/vite/issues/2433 に、このエラーに関する記述があったので、`export NODE_OPTIONS=--max-old-space-size=メモリの容量（単位: MB）`と打ってから`pnpm run build`すればよいと分かりました。

　で、512MBとか制限してやればいいのかなーと思って試したら駄目だったので、スワップ合わせてもそんなにメモリはないのに`export NODE_OPTIONS=--max-old-space-size=4000`（4GB弱）とハッタリをかましたら、ビルドがうまくいきました。なんじゃそりゃ。

### 他のメンテナンス作業

　SSDが100GBしかないので、キャッシュだけでストレージの使用率が50%くらいになってました。
[こちらの記事](https://blog.usuyuki.net/misskey_image_cache)を参考に既存のキャッシュをクリアしました。
キャッシュ自体はまだやめないで様子を見ようと思います。
キャッシュ自体は`misskey`のリポジトリの`files`の下にできます。


