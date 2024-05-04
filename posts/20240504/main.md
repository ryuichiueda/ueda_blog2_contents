---
Keywords: ROS 2
Copyright: (C) 2024 Ryuichi Ueda
---

# C++で作ったROS 1のパッケージをROS 2に移植するときのつまづきポイント ―RVizのゴールの出力について

　https://github.com/ryuichiueda/value_iteration
を
https://github.com/ryuichiueda/value_iteration2
に移植中です（おわらねー）。今日は「ナビゲーションのコードを自前で書きたいのにRVizがゴールをトピックに吐いてくれない」という謎現象を解決しました。

　この記事の結論は「ROS 2でもActionを使わずに、設定次第でゴールをトピックからサブスクライブして`/cmd_vel`に出力してナビゲーションを試すことができる」です。ROS 2を教えるときにいきなり複雑な仕組みを学生さんに触ってもらうくらいなら、最初はこっちのほうがいいと思います。ROS 1はアクションはトピックを束ねたものでシェルから見えましたが、ROS 2では「ある種の潔癖さ」でそうではないようです。

## なにがどうしてどうなった

　RVizの画面の「ゴールを矢印を引いて指定するやつ」の出力を扱う正しい方法を探していたところ、「nav2_utilでActionサーバーを作れ」とのこと。ただ、それだとNav2にいろいろ縛られるのでやだなと思って、RVizからトピックをとって勝手にやろうと思いました。が、RVizがトピックを出している形跡がありません。

　で、何時間かいろいろ調べたんですが、たどり着いたのは、私の環境ではRVizにNav2用のプラグインが使われてて、それがトピックを出さないということでした。たどり着いたのは、中国語のサイトでした。英訳して読みました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ROS 2のRVizがトピックにゴールを出さない件、中国のページに助けられた。助かった・・・あざす！<a href="https://t.co/w9VhK93SP1">https://t.co/w9VhK93SP1</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1786667270162551153?ref_src=twsrc%5Etfw">May 4, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

理屈の説明は上のページ（の翻訳）に譲るとして、とりあえずRVizのconfigファイルをRVizから保存して、次のように書き換えるとトピックを吐くようになりました（[当該の箇所](https://github.com/ryuichiueda/value_iteration2/blob/9860c334a421f48f3f8f09d7ea54bfbcabc64ce5/config/config.rviz#L551-L553)）。

```yaml

#    - Class: nav2_rviz_plugins/GoalTool   #これコメントアウト
    - Class: rviz_default_plugins/SetGoal  #この2行追加
      Topic: /goal_pose
```

なるほど。


## 余計な一言

　ROS 2、必要以上にややこしくなっているのは学術的にというより政治的に、という感じなので、この先どうなるのかちょっと見ものかなと思います。みんなのために（じゃないかもしれないけど）仕組みを作ってたら知らないうちにしきたりまみれの平安貴族か強権な独裁者になってた、ということは歴史的によくあることなので、避けてほしい（し、第三者は従順にならずにいてほしい）なと草葉の陰から思いました。（直接関係ないですけど）某社も「evilになるな」とか言ってたんですけど今はあんな感じですし。

　RoboCupなどでちょっとやったり散々やられたりしましたが「みんなのため」を演説で主張して自分に利益を引っ張るのは国際的にはオッケーなやりかたなので、見かけのスマートさを盲信するの避けたいものです。

　現場からは以上です。
