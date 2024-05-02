---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記というか週報というか（〜2024年5月2日）

　5月もいろいろある。

## 自作シェル

　[mainブランチ](https://github.com/shellgei/rusty_bash)のコードに

* Gitのリポジトリ内ではブランチが表示されるようにする
* ビルトインコマンドの`source`（`.`）、`alias`を実装
* ホーム（or リポジトリにある）`.sushrc`を読み込むようにする

という拡張をして、とうとう普段使いできるまでになりました。現在の外観↓

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

## ゴールデンウィークに読むといい本の案内

　私の本はとにかく読むのに時間がかかるので、休みのときにどうぞどうぞ

<p><a href="https://amzn.to/3JPeSgR"><img width="160px" src="https://images-na.ssl-images-amazon.com/images/P/4339046876.09.LZZZZZZZ"></a></p> <p><a href="https://amzn.to/3JPeSgR" target="_blank" rel="nofollow">ロボットの確率・統計: 製作・競技・知能研究で役立つ考え方と計算法 単行本（ソフトカバー） – 2024/3/4</a></p>

<p><a href="https://amzn.to/3Qt6rLU"><img width="160px" src="https://images-na.ssl-images-amazon.com/images/P/4297122677.09.LZZZZZZZ"></a></p> <p><a href="https://amzn.to/3Qt6rLU" target="_blank" rel="nofollow">1日1問、半年以内に習得 シェル・ワンライナー160本ノック (Software Design plusシリーズ) 単行本（ソフトカバー） – 2021/9/27</a></p>

<p><a href="https://amzn.to/3UEIdky"><img width="160px" src="https://images-na.ssl-images-amazon.com/images/P/4065170060.09.LZZZZZZZ"></a></p> <p><a href="https://amzn.to/3UEIdky" target="_blank" rel="nofollow">詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装 (KS理工学専門書) 単行本（ソフトカバー） – 2019/10/27</a></p>

<p><a href="https://amzn.to/3Qr6190"><img width="160px" src="https://images-na.ssl-images-amazon.com/images/P/B07TSZZPWN.09.LZZZZZZZ"></a></p> <p><a href="https://amzn.to/3Qr6190" target="_blank" rel="nofollow">フルスクラッチから1日でCMSを作る_シェルスクリプト高速開発手法入門 改訂2版 (アスキードワンゴ) Kindle版</a></p>

## 査読

　おわんねー

現場からは以上です。
