---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月1日）

　いつのまにか7月になってしまった。腕時計が6月31日を指している。パーペチュアルカレンダーのやつほしいそれは無理。仕事は下記研究のための作業と講義資料書き、仕事の斡旋等。M2の就活がめでたく完全終了。

## ROSいじり

　ウェイポイントナビゲーション的なことをやりたくてmove_baseをいじってたが、どうもtf関係のバグが取れない。（時刻が未来だのどうだのと）。信頼のおける学生さんに教えを乞うたら地味に問題を取り除くしかないという見解で、かつ必ずしもmove_baseのリッチな機能が不要なので、自分でナビゲーションのコードを書くことにした。明日やる。

　エラーはこれなんだけど、とりあえず放置。ここらへんの理解をちまちまと深めてからまた考える。

```
[ERROR] [1561957471.840473934]: Extrapolation Error: Lookup would require extrapolation into the future.  Requested time 1561957471.824147647 but the latest data is at time 1561957471.783358264, when looking up transform from frame [odom] to frame [map]
[ERROR] [1561957471.840533785]: Global Frame: odom Plan Frame size 20: map
[ WARN] [1561957471.840553351]: Could not transform the global plan to the frame of the controller
```

## 今日のシェル芸

　いらすとや風の文言がシュールさを増しております。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">女性プログラマーがノートパソコンを広げてシェル芸を書いているイラストです。<br> <a href="https://t.co/FO02QxBsj1">https://t.co/FO02QxBsj1</a> <a href="https://t.co/0epZxrWCyJ">pic.twitter.com/0epZxrWCyJ</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1145335136231149568?ref_src=twsrc%5Etfw">2019年6月30日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


洗濯しよう・・・。

