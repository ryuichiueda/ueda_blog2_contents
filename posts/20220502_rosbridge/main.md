---
Keywords: 日記, ROS, CMake
Copyright: (C) 2022 Ryuichi Ueda
---

# rosbridgeに生のJSONを送りつける

　やりたいことはこういう感じです。

* サーバ側にシミュレータのロボット（TurtleBot3）を用意して、rosbridgeと、ナビゲーションのノード一式を動かす。
* 別のPCからrosbridgeでロボットを制御したい。
* 別のPCには、できればWebSocketのライブラリ程度しかインストールしたくない。

で、以下の方法でとりあえずできそうな目処が立ちました。

## サーバ側でロボット一式を立ち上げておく

　`roslaunch`で立ち上げておきます。[今回使ったリポジトリ](https://github.com/ryuichiueda/turtlebot3_jupyter)（まだ未整備です）。[ローンチファイルはこんな感じ](https://github.com/ryuichiueda/turtlebot3_jupyter/blob/main/launch/run.launch)。

## クライアント側からrosbridgeと接続する

　wscatというツールを使いました。

* 参考: [WebSocket の動作確認に wscat が便利すぎる件 | tricknotesのぼうけんのしょ](https://tricknotes.hateblo.jp/entry/20120227/p1)

インストールの方法については、 **npmまるでわからん** という状況なので、ここには書きません。

　で、立ち上げます。

```
### ロボットのいるサーバのIPアドレスとrosbridgeのポート番号を指定してwscatを立ち上げ ###
$ wscat -c ws://192.168.1.25:8000
Connected (press CTRL+C to quit)
>              <- ここに送信したいデータを書くっぽい
```

サーバ側には、このようにログが出ます。

```bash
2022-05-02 15:41:37+0900 [-] [INFO] [1651473697.993877, 1363.184000]: Client connected.  1 clients total.
```


## JSONを書く

　[rosbridge v2.0](https://github.com/biobotus/rosbridge_suite/blob/master/ROSBRIDGE_PROTOCOL.md)準拠のJSONを書きます。v1.0ではアカンそうで、


```bash
Received a rosbridge v1.0 message.  Please refer to rosbridge.org for the correct format of rosbridge v2.0 messages. 
```

と怒られます。v2.0でのsubscribe、puslishの例を書いておきます。`wscat`の出すプロンプト「`>`」の横に書きます。例が見当たらず、正解を当てるまで疲れました・・・。

* subscribeの例

```json
{"op": "subscribe", "topic":"/rosout","type":"rosgraph_msgs/Log"}
```

* publishの例

```json
{"op": "publish", "topic":"/cmd_vel","msg":{"linear":{"x":0.1,"y":0,"z":0},"angular":{"x":0,"y":0,"z":0}},"type":"geometry_msgs/Twist"}
```

subscribeの場合はJSONでrosbridgeからデータが送られてきます。puslishの場合も、受け付けた内容をrosbridgeが返してきます。

　上のpublishを入力しているときの動画を掲載します。

<iframe width="560" height="315" src="https://www.youtube.com/embed/v1P_DOfXGYo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## 最後に一言

　プロトコルの仕様は、なるべくローレベルなワンライナーと共に説明してほしいなあ・・・。
