---
Keywords: 日記, Misskey
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年8月11日）

　Misskeyのサーバーいじりと小銭稼ぎの話。

## Misskeyのアップデート

　さくらのVPS（メモリ1GB）、Docker不使用でなんとか運営している[しぇるげいすきー](https://mi.shellgei.org/)のバージョンアップ作業をしました。途中ビルドがコケて肝を冷やしました。


### トラブル

　[このページのアップデート方法](https://misskey-hub.net/docs/install/manual.html#misskey%E3%81%AE%E3%82%A2%E3%83%83%E3%83%95%E3%82%9A%E3%83%86%E3%82%99%E3%83%BC%E3%83%88%E6%96%B9%E6%B3%95)の`NODE_ENV=production pnpm run build`をしているときに、次のようなエラーが出ました。

<iframe src="https://embed.misskey.io/notes/9i9xcoi9kp"></iframe>



### キャッシュのクリア

　SSDが100GBしかないので、キャッシュだけでストレージの使用率が50%くらいになってました。
[こちらの記事](https://blog.usuyuki.net/misskey_image_cache)を参考に既存のキャッシュをクリアしました。
キャッシュ自体はまだやめないで様子を見ようと思います。
