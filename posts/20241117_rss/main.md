---
Keywords: 自作シェル
Copyright: (C) 2024 Ryuichi Ueda
---

# このサイトにRSSの機能をつけた

　なんとなくついったーとかSNSの拡散能力が弱まってきたっぽいので、SNS以前のいにしえの機能であるRSSを自分のサイトに装備しました。
URLは https://b.ueda.tech/rss/rss20.xml です。RSS関係のなんらかのツールを使っている人はぜひご登録ください。更新頻度は低いのであまり目障りにはならんはずです。

## 技術的なこと

　このサイトがbashcms2というBash製のCMSでできていることは[一部界隈で有名な話](https://www.amazon.co.jp/dp/4048930699)ですが、RSSもBashのバッチ処理で吐き出しています。GitHubに記事をpushすると、GitHubに登録してあるCGIのBashスクリプトがリポジトリの中身をpullしに行き、そのあとにバッチ処理がまわって上記URLのRSSファイルができます。

　RSSのファイルはこのページのトップにある「最近の記事」のHTMLデータをsedでグリグリしてXMLにしています。コードは超やっつけなので見せたくありませんが、いちおう[bashcms2のリポジトリ](https://github.com/ryuichiueda/bashcms2)のueda_siteブランチのfetchというスクリプトの一番下に書いてあります。超絶適当なので見ないでください。

　ちょっと面白かったのは、RSSや各記事につけるタイムスタンプの時刻がGMTしかダメで、独自フォーマットでしかも一字一句間違えてはいけないという ~~クソ~~ 仕様だったので、各記事の作成日時のファイルのデータをこんな感じで変換しなければならなくなりました。

```bash
mtime=$(date -d "$(cat $datadir/$d/created_time) 9 hours ago" "+%a, %d %b %Y %H:%M:%S GMT")
                         #↑このファイルに記事の作成日付がJSTで入ってる
```

全然パイプつかってないのに長いワンライナーになってしまいました。
それから、副作用（＋ものぐさ）で、「最近の記事」の各項目の下に、GMTの時刻が中途半端なフォーマットで出るようになりました。直すのめんどくさい。


現場からは以上です。
