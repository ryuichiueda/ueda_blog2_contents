---
Keywords: ROS 2, Rust
Copyright: (C) 2024 Ryuichi Ueda
---

# ros2_rustでスキャンデータと地図を扱ってみた

　この前学会（SI2024）で発表した[これ](https://www.docswell.com/s/ryuichiueda/ZEX11D-si2024)の[コード](https://github.com/ryuichiueda/flow_estimator)をROS 2のパッケージにしようということで、[ros2_rust](https://github.com/ros2-rust/ros2_rust)について調べて一昨日からいじってました。

　ros2_rustについての日本語の情報は、すでに

* https://qiita.com/MrBearing/items/caf427b23d65d6c085d7
* https://qiita.com/koichi_baseball/items/4e4d5892781683a64398

がありました。んで、移植のためにはさらにLiDARのデータをサブスクライブして地図をパブリッシュしないといけないので、その先をやってみました。できました。

## スキャンデータをサブスクライブする

　ros2_rustについては上で紹介した記事を読むとよいので続きを書くと、まず、TurtleBot3 Burger（シミュレータのやつ）の吐くスキャンデータをサブスクライバで読んで、別のパブリッシャからパブリッシュすることに挑戦しました。できました。

<iframe src="https://mi0.robotician.jp/embed/notes/a2dycyfksg?colorMode=light" data-misskey-embed-id="v1_2c100fd1-0841-4487-8a5a-7be11e456310" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi0.robotician.jp/embed.js"></script>


　コードはこうなりました。

* https://github.com/ryuichiueda/my_first_rclrs/blob/scan/src/main.rs

で、チュートリアルのコードのどこをいじったかというと、次の3点だけです。`main.rs`についてはVimの置換だけで済みました。

* main.rs
    * パブリッシャで傍受するトピックを`scan`に変更
    * トピックを受けるデータの型を`std_msgs::msg::String`から`sensor_msgs::msg::LaserScan`に変更
* Cargo.toml
    * dependenciesに`sensor_msgs = "*"`を追加

　「型を変えてコンパイルが通れば動く」というRustの良い面（悪い面もある）がモロに出ました。

## 地図のデータをパブリッシュする

　こちらはコードを書かなければいけないので数時間かかったのですが、どっちかというとROS 2のセットアップのほうが大変でした。

* コード: https://github.com/ryuichiueda/my_first_rclrs/blob/map/src/main.rs

　変更点は

* main.rs
    * いろんな型を`use`に追加（7〜12行目）
    * マップを送出するパブリッシャの追加（19、34、40行目）
    * 地図の作成（49〜92行目。スクラッチから構造体を組み合わせて作りました）
* Cargo.toml
    * `nav_msgs, builtin_interfaces, geometry_msgs`の追加

です。RVizでゴニョゴニョすると、こんな出力が得られます。

<iframe src="https://mi0.robotician.jp/embed/notes/a2folvyj5v?colorMode=light" data-misskey-embed-id="v1_4aacf173-bfd5-4bc9-8b48-27bbc0615d95" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi0.robotician.jp/embed.js"></script>

## 所感

　`main.rs`はパブリッシャ、サブスクライバをマルチスレッドで動かすために仰々しいプログラムになっていますが、基本、なにかサブスクライバからデータを取り込んでひとつのパブリッシャから加工したデータを出す処理は、ひとつのスレッドの中で完結するので、特にややこしいことはないかなと思いました。Rustのプログラムは不可解な挙動をしないので慣れてしまうと楽です。

　ただ、バージョンはhumble（Ubuntu 22.04）までのようです。24.04のがないか[リポジトリ](https://github.com/ros2-rust/ros2_rust)を探しに行ったら、ブランチがmainしかありませんでした。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ブランチがmainしかないの、お前、漢だな <a href="https://t.co/oEZJFLO8w2">pic.twitter.com/oEZJFLO8w2</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1873563826433802377?ref_src=twsrc%5Etfw">December 30, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



　明日は一気にC++のコードをRustにしてパッケージを作ってしまいたいところです。


　それではよいお年を〜
