---
Keywords: コマンド,シェルスクリプト,Linux,寝る,自宅サーバ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# ダイナミックDNSを使わずにシェル芸等々で自宅のサーバへアクセスするシステム作った
（追記: 早速「VPSに向かってトンネル掘っとけよ！とUSP友の会で尻を突かれております。トンネル掘られそうです。」。あと、cronの頻度が高いと先方のサービスに蹴られる可能性があるのと、かと言って頻度を下げるとケーブルテレビ系だとちと辛いという話になってます。NTT, AUはIPがほとんど変わらないというのが経験上、言えることですが、保証はないです。）

久しぶりにサーバいじりネタ。本当は今週学会1つと講義2つの準備があって、講義の準備が1つ済んでいないが、子供がギャーギャー言っている環境だと趣味ぐらいしか手が動かないので・・・

<h2>やりたいこと</h2>

自宅に外からアクセスできるGitサーバ、ファイルサーバが欲しい。個人情報は置かない。自宅には光回線。IPアドレスが変わるがダイナミックDNSを使うほどでもない。

<h2>自作自宅（と言っても仕事用）サーバ</h2>

（笑）

<a href="1f8ab99fd20d90552cea8cec5339ede9.jpeg" rel="attachment wp-att-7261"><img src="1f8ab99fd20d90552cea8cec5339ede9-1024x768.jpeg" alt="ファイル 2015-12-13 20 35 51" width="660" height="495" class="aligncenter size-large wp-image-7261" /></a>

ショートが怖いのでラズパイのケースは発注しました・・・。リビングの電話台という、排熱できない環境に置くので耐久テストも兼ねてます。昔は同じ場所にThinkPad x41を置いてCentOSをインストールしてNASにしていましたが、夏場に40度にもなる環境で何年もトラブルなく動いていました。恐るべし<span style="font-size:50%">昔の</span>ThinkPad。

<h2>最低限のセキュリティー</h2>

もちろん、デフォルトのラズパイはユーザpiとパスワードraspberryという<span style="color:red">公然のお約束</span>があるので、セキュリティーユルユルです。

とりあえず自分がやった作業を書いておくと、まず次のように自分のアカウントを作り、piユーザを消しました。

```bash
$ sudo useradd ueda
###/etc/gropuのpiユーザを全部uedaに置換###
$ sudo userdel pi
$ sudo reboot
```

そして、鍵を仕込んだらパスワードで入れないようにしておきました。今回のネタは鍵認証を使いこなせない人はちと難しいので先にそちらをお勉強願います。

```bash
$ vi /etc/ssh/sshd_config 
###以下のように変更###

# Change to no to disable tunnelled clear text passwords
PasswordAuthentication no
###説明が面倒くさいのでreboot###
$ sudo reboot
```

で、ルータのグローバルIPとポート番号をラズパイのローカルIPとポート番号と結びつけて転送できるようにします。これは・・・ルータ依存なので説明しませんが、難しいですよね・・・。

設定ができたらルータのグローバルIPを調べて、外からラズパイに向かってsshできるか試しました。

<h2>グローバルIPを調べて某所に転送するスクリプトを書いてcronに登録</h2>

で、DDNSが使えないのでこれからどうするかというところですが、とりあえずラズパイから一定時間間隔でグローバルIPを別のインターネット上のサーバ（自分のVPS）に飛ばします。

ルータの持っているグローバルIPをどう調べるかわからなかったので、グーグルで調べたら<a target="_blank" href="http://qiita.com/syrinx05p/items/55060ab2e3dead4a370d">すっきりしたQiitaのエントリー</a>が見つかったので、その通りにしました。

```bash
ueda\@raspberrypi ~ $ curl inet-ip.info
203.0.113.1
```

おお。

ということで、次のようなシェルスクリプトを書きました。必須の行は最終行だけで、curlでIPアドレスを調べ、test.example.comに飛ばし、test.example.com側の/tmp/homeipに保存するというワンライナーです。シェルスクリプトですが、シェル芸っぽいです。宣伝ですが、こういう小技がたくさん書いてある<a rel="nofollow" href="http://www.amazon.co.jp/gp/product/4774173444/ref=as_li_ss_tl?ie=UTF8&camp=247&creative=7399&creativeASIN=4774173444&linkCode=as2&tag=ryuichiueda-22">シェルプログラミング実用テクニック (Software Design plus)（アフィ）</a><img src="http://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=4774173444" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />もよろしくお願いいたします（最近、宣伝が少なくて出版社に報いてないので宣伝）。


```bash
ueda\@raspberrypi ~ $ cat ~/SYS/SENDIP 
#!/bin/bash -vx

exec 2&gt; /tmp/SENDIP.log

curl inet-ip.info | ssh test.example.com 'cat - &gt; /tmp/homeip'
```

で、これをcrontabにしかけます。

```bash
ueda\@raspberrypi ~ $ crontab -e
###以下のように1行書く###
*/10 * * * * /home/ueda/SYS/SENDIP
```

で、test.example.comに入って、10分後に更新されているか確認します。

```bash
ueda\@test:~$ cat /tmp/homeip 
203.0.113.1
```

更新されていなかったら、ラズパイの/tmp/SENDIP.logにログが残っているので、バグがないか確認します。当然、鍵は通してある必要があり、また、（回避の方法を知らなければ）1度だけ最初に手でログインしておく必要があります。

<h2>自分のPCの設定</h2>

（追記: Windowsガン無視すいません・・・）
まず、.ssh/configに次のように書いておきます。IPアドレスはダミーです。

```bash
Host home
 HostName 127.0.0.1
```

で、次のようなシェルスクリプトを書きます。sshでtext.example.comにある/tmp/homeipのIPアドレスを読み込んで、sedで.ssh/configを上書きするという乱暴なものです。

```bash
uedamb:~ ueda$ cat ~/SYS/HOMEIP 
#!/bin/bash -xv

IP=$(ssh test.example.com 'cat /tmp/homeip')

sed -i.bak &quot;/Host home/,/HostName/s/ HostName.*/ HostName $IP/&quot; ~/.ssh/config
```

なかなか一発でバグなくsedの文を書くのは大変ですが、うまくいったら、.ssh/configが次のように書き換わります。

```bash
Host home
 HostName 203.0.113.1
```

このシェルスクリプトもcronに仕掛けても良いですが、多分そんなにIPアドレスは変わらないので手動で良いでしょう。

これで自宅にssh接続できるはずです。この作業は自宅でやったので、iPhoneのテザリングに変えてやってみました。

```bash
uedamb:~ ueda$ ssh home

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Dec 13 12:07:41 2015 from 192.168.0.2
ueda\@raspberrypi ~ $ 
```

できました。

<h2>終わりに</h2>

サーバをセットしてから通信できるまで1時間くらいですが、手順を書くと結構いろんな小技が必要かなと思いました。別にwebサーバを立てているわけでもないのにDDNSを使っている人は、腕試しに試していただければと。

あと、ハマる点は、外づけHDDの電源がつくタイミングとラズパイが立ち上がるタイミングによってはマウントで止まってしまうので、fstabに情報を書くのはちと危険かもしれません。


とりあえずうまくいってよかった。寝る。
