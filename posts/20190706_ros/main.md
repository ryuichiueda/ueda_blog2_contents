---
Keywords: ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 【ROS】一つのlaunchファイルで複数のロボット・PCを動かす

　このまえ、ロボットとPCで動かすノードのlaunchファイルを一つにまとめようとして、こちらの記事を参考にさせていただいたのですが、ネットワークで少しハマったので手順の実例を出しておきます。`.bashrc`を一切いじらなかったからかもしれません。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">あーなるほど。こうすればよいのか。<a href="https://t.co/tQVlJVseE0">https://t.co/tQVlJVseE0</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1146347445921579008?ref_src=twsrc%5Etfw">2019年7月3日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## やりたいこと

　PC側で動かすノードとロボット側で動かすノードを、PC側から一斉に立ち上げたい。

## 前提

　ロボット側、PC側の別々のlaunchファイルでちゃんとシステム全体が動くように、ネットワークが設定済み。


## launchファイル

　まず、こんな感じでlaunchファイルを用意します。この例はRaspberry Pi MouseでCartographerを利用してSLAMをするためのlaunchファイルです。

* https://github.com/ryuichiueda/raspimouse_cartographer/blob/master/launch/slam_remote_robot_and_pc.launch

大事なのは、ロボット側のノードを立ち上げている部分で、抜粋すると、

```
  <!-- ROBOT SIDE -->
  <machine name="raspimouse" address="raspimouse" env-loader="/home/ubuntu/env.bash" user="ubuntu" password="ubuntu" />

  <node machine="raspimouse" pkg="raspimouse_ros_2" name="motors" type="motors" required="true" />

  <node machine="raspimouse" pkg="joy" name="joy_node" type="joy_node" required="true">
    <param name="autorepeat_rate" value="3" />
  </node>

  ・・・以下略・・・
```

となります。詳しい話は私が参考にした上記ブログの記事に詳しいですが、要点は、

* `machine`というノードを準備して通信の設定
    * `address`のホスト名は`/etc/hosts`に書いた通りに
* `machine`の`env-loader`属性で、ノードを立ち上げる前に呼び出すスクリプトを指定
    * ロボット側で`source ~/.bashrc`をする操作に相当
* ロボット側（この例だと`raspimouse`）で立ち上げたいノードに、`machine`属性を加える


## ssh

　で、これで`roslaunch`してうまくいくこともありますが、最初に試したときはうまく通信できませんでした。次のようなエラーが出ます。

```
Unable to establish ssh connection to [ubuntu@raspimouse:22]: Server u'raspimouse' not found in known_hosts
```

ということで調べたら次のようなページに当たりました。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これも必要だそうです。known_hostsから一度ホストの情報を消して、マニュアルで-oHostKeyAlgorithms=&#39;ssh-rsa&#39;をつけてsshしなおす。<a href="https://t.co/S9kTLLaK3C">https://t.co/S9kTLLaK3C</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1147022173007011840?ref_src=twsrc%5Etfw">2019年7月5日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

どうやら`~/.ssh/known_hosts`に記録があるとダメなことがあるようで、ロボットのIPアドレスやホスト名に関する記録を全部消した上で、

```
ssh ubuntu@raspimouse -oHostKeyAlgorithms='ssh-rsa' 
```

と手でログインして、RSAアルゴリズムを使うように指定なおさないといけないとのことです。

## ロボット側で起動するシェルスクリプトを書く

　最後に、launchファイルで指定した`/home/ubuntu/env.bash`というスクリプトを書きます。

```
#!/bin/bash -xv

exec 2> /tmp/remote_kick_log.txt

source /opt/ros/melodic/setup.bash
source /home/ubuntu/catkin_ws/devel/setup.bash
export ROS_HOSTNAME="raspimouse"
exec "$@"
```


こちらを参考にしました。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">さらにこれも必要です。オレオレ<a href="https://t.co/7yUq3Soj4W">https://t.co/7yUq3Soj4W</a>を作る。<a href="https://t.co/MsOs69dmwq">https://t.co/MsOs69dmwq</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1147026855246983168?ref_src=twsrc%5Etfw">2019年7月5日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

これで、たぶんちゃんと立ち上がるようになります。

### もう少し詳しい解説

　こんなシェルスクリプトを書かなくても`~/catkin_ws/devel/env.sh`でよさそうなのですが、

```
error launching on [raspimouse-0, uri http://ubuntu:39355/]: Connection refused
Launch of the following nodes most likely failed: raspimouse_ros_2/motors, joy/joy_n
ode, raspimouse_game_controller/logicool_cmd_vel.py, urg_node/urg_node
```

というようにノードをうまく見つけてくれません。

　また、`env.bash`の最終行の`exec "$@"`は、`env.bash`に与えられた引数をそのまま実行して、さらにこのシェルスクリプト自体を実行したプログラムで`exec`して置き換えてしまうという意味を持ちます。

　PC側のログを見ていると、

```
launching remote roslaunch child with command: [env ROS_MASTER_URI=http://note:11311
/home/ubuntu/env.bash roslaunch -c raspimouse-0 -u http://note:43485/ --run_id 1639c
576-9f94-11e9-82c0-001c420e53eb]
```

と`env.bash`を呼び出しているところがありますが、`env.bash`の`$@`には、このログ中の「`roslaunch -c raspimouse-0 -u http://note:43485/ --run_id 1639c576-9f94-11e9-82c0-001c420e53eb`」という文字列が入ります。で、`exec "$@"`で`roslaunch -c ...`が実行されます。環境は`env.bash`で`source`したものが読み込まれているので、これが`roslaunch`に伝わって、`roslaunch`がノードを見つけてくれます。

　`env.bash`にしかけた`/tmp/remote_kick_log.txt`を見ると、

```
exec "$@"
+ exec roslaunch -c raspimouse-0 -u http://note:43485/ --run_id 1639c576-9f94-11e9-82c0-001c420e53eb
```

と、`roslaunch`が`exec`で実行されている様子が分かります。`exec`については、[私の講義資料](https://github.com/ryuichiueda/robosys2018/blob/master/04_process.md)をご参考ください。


## ということで

　ロボットをいじるのにはネットワークとシェルの知識が必要という典型的な例だと思います。これをロボットの人が勉強するのは大変なのですが・・・とてもいい本があります。bashでウェブサイトを作るという本で、シェルとネットワークの話が一緒に出てきます。


<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/B07TSZZPWN/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51H%2B4kUhbFL._SL160_.jpg" width="121" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/B07TSZZPWN/ryuichiueda-22">フルスクラッチから1日でCMSを作る_シェルスクリプト高速開発手法入門 改訂2版 (アスキードワンゴ)</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>ドワンゴ 2019-07-05 (Release 2019-07-05)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>


宣伝すみません！おしまい。
