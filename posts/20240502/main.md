---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記というか週報というか（〜2024年5月2日）

　5月もいろいろある。

## 自作シェル

　[mainブランチ](https://github.com/shellgei/rusty_bash)のコードに

* Gitのリポジトリ内ではブランチが表示されるようにする
* ビルトインコマンドの`source`（`.`）を実装
* ホーム（or リポジトリにある）`.sushrc`を読み込むようにする
* aliasが使えるようにする

という拡張をして、とうとう普段遣いできるまでになりました。現在の外観↓

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">自作シェル、いい感じで使えてるんだけどbash-completionほしいなあ・・・（遠い道のり） <a href="https://t.co/YyvNQiBULL">pic.twitter.com/YyvNQiBULL</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1785985897458180437?ref_src=twsrc%5Etfw">May 2, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

おおむねいい感じで使えてるんですが、やっぱりbash-completionがないとですね・・・対応に何ヶ月かかるんだろうか・・・

## 価値反復パッケージをROS 1からROS 2へ移行中

　以前書いたとおり、[この論文](https://www.fujipress.jp/jrm/rb/robot003500061489/)のROSパッケージをROS 2に移行しているんですが、ROS 2の硬さで肩こりになってます。今日面食らったのは、ログを端末に出すの普通に標準エラー出力に出せばいいのに、わざわざメインのインスタンスのポインタがないと書けない仕様になっていることで、ブチ切れていました。これでは、任意のクラスのあるメソッドで気軽にログが出せないというクソみたいな状況になります。


　ただ、ポインタのいらない書き方もあるというのをブチ切れた後で発見しました。いったいなんなんでしょうか？

```cpp

/* ポインタいるやつ */
RCLCPP_INFO(this->get_logger(),"Global thread num: %d", thread_num);
/* ポインタいらないやつ */
RCUTILS_LOG_INFO("SET STATES START");
```

厳しすぎて規制緩和してるんでしょうか？スプロール現象みたいなことが起きてないでしょうか？心配です。

## 中部大での確率ロボティクスの講義

　ちまたではゴールデンウィークらしいのですが、水曜に講義で名古屋というか春日井に行ってきました。発表資料を掲載しておきます。大学に復帰したときは「私の話は古いので〜」とよく言ってましたが、最近は機械学習の勉強も進んで新しくできているかなと思ってます。ただ、まだまだですかね。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">はい。本日の講義資料です（アップしなおし）<br><br>どうやって確率ロボティクスを紹介するかいつも悩むんですが、今回は制御の延長線上にあるものとして紹介しました<a href="https://t.co/WXoLfSmLEI">https://t.co/WXoLfSmLEI</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1785586392875331791?ref_src=twsrc%5Etfw">May 1, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

現場からは以上です。
