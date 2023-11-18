---
Keywords: 日記
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年11月18日）

　なんか正念場という感じ

## 冬に出る本の初校のゲラが来ました

　あああ・・・始まる・・・。校正けっこうきびしめです・・・。今回のは「教科書ではなく教科書を読むための入門書」と断って書いているので、楽しく雑に書いたのですが・・・きびしいです。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">昭和の人間なので校正は紙でやるです<a href="https://t.co/9wYICDs5CZ">https://t.co/9wYICDs5CZ</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1725795477323718920?ref_src=twsrc%5Etfw">November 18, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## SoftwareDesign 12月号

　こちらも紙の雑誌が届きました。うさぎさん校正手伝って。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">うさぎさんがかわいいSoftwareDesignの12月号が店頭に並んでます <a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <br><br>ChatGPTとかAI（画像処理）とかロボット屋さんもびっくりの充実感<br><br>そして、かつてAIの研究者とは俺のことだろうと鼻息の荒い若手だった私の書いている記事は、自作シェル（とてもたのしい）<br><br>とりあえず読んでみてください <a href="https://t.co/lkSv2ZeqtD">pic.twitter.com/lkSv2ZeqtD</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1725799506816745679?ref_src=twsrc%5Etfw">November 18, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## シグナルやスレッドに頼らずに無限ループを止める

　自作シェル関係で、ビルトインコマンドだけで構成されたwhileをCtrl+Dで止める実験をやってました。実験をまとめたリポジトリはこちら。

https://github.com/ryuichiueda/stop_inf_loop_with_ctrl_d

このリポジトリの`main.rs`のコードはつぎのGistのとおりです。

<script src="https://gist.github.com/ryuichiueda/1bd19c9d7d63e4943e6b313878ff134f.js"></script>

これで、Ctrl+Dすると、ループを抜け出すことができます。

```bash
わはははは
わはははは
わはははは
わはははは
わはははは
^D
ループから出た
$
```

以上。
