---
Keywords: 日記, 自作シェル, 研究
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年9月23日）

　土日は特になんの用もないので自宅で仕事。
本当はつくばチャレンジの試走会なんだけど、それは学生さんに任せて（というよりは学生さん主体なので）今回は顔を出しませんでした。

## Software Design [魅惑の自作シェルの世界](/?page=rusty_bash)

　いま11月号の校正の途中なのですが、
校正は午前に済ませて12月号の原稿を書き上げました。
12月号の内容はerrnoによるエラーの表示とビルトインコマンドに対する（フォークしない）リダイレクトになります。
フォークしないでシェルの内部状態いじるの嫌すぎる・・・。

## 投稿論文通った

　自分が筆頭著者で血反吐を吐きながら書いた論文が通りました。

* 著者: Ryuichi Ueda, Leon Tonouchi, Tatsuhiro Ikebe, and Yasuo Hayashibara
* タイトル: Implementation of brute-force value iteration for mobile robot path planning and obstacle bypassing
* 掲載誌: Journal of Robotics and Mechatronics, Vol.35 No.6 に掲載予定（December 20, 2023）

となります。よろしくお願いいたします。内容は、[このリポジトリ](https://github.com/ryuichiueda/value_iteration)（移動ロボットの計算量がめっちゃ大きい経路計画器を無理やりオンラインプランニングに使う話）の解説と評価です。このプランナーでロボットが移動障害物をよけている動画です。

<iframe width="560" height="315" src="https://www.youtube.com/embed/tcrr6rOeC_A?si=zvBywifHXuhaDu7S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

また、こちらは白地図の状態から障害物を見つけて経路計画してゴールに行くというデモです。

<iframe width="560" height="315" src="https://www.youtube.com/embed/v-oTxhL60DQ?si=x-WOCE3Avd03YCsn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

ちょっとこれだけ見てもよく分からないと思いますので、論文が出たらぜひ読んでみてください。

