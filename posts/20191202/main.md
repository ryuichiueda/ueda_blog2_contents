---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年12月2日）

日記をつけてないと（そして人に自分の仕事を話していないと）何やってるかわからなくなるので日記を再開します・・・。

## Raspberry Pi 4

https://wiki.ubuntu.com/ARM/RaspberryPi の「19.10: ubuntu-19.10-preinstalled-server-arm64+raspi3.img.xz (4G image, 631MB compressed)」を試してみました。起動がcloud-initのうしろで止まってしまい、一度電源をブチ切りしましたが2回目で起動しました。LANケーブルをささずに立ち上げたのがいけなかったんでしょうか？

で、立ち上がったあと、今度はキーボードが一切反応しない。外からsshしようとしたら手間取ってできなかったので、下記サイトを参考にmicroSDのルート直下に`ssh`という空ファイルを設置してログインできたけど、もしかして自分がIPアドレスをちゃんと探せなかったからという可能性の方が高いです。キーボード使わずにRaspbianをセットアップしたいなら参考になるかもしれません。

https://blog.maya2250.com/entry/setup-raspberrypi1

余談: イメージは`dd`を使わずEtcherを使って焼きました・・・。シェル芸人失格ですが、目的が明確なものは専門のソフトに任せてます。）

## MacBook Proを壊す（先月から2度目）

某メーカのポータブルモニタが犯人と分かりました。モニタにさわったら感電し、せっかく修理から戻ってきたMacBook Proの右側のUSB-Cのポートが死にました。またうん万円かかるので今度は修理に出しません・・・。前回は起動しなくなったので、今回のは不幸中の幸い。

犯人のポータブルモニタ、USB-Cで給電+モニタ信号出力せず、外部の電源とHDMIで使ったほうがいいようです・・・。

## 仕事

[学科のサイトに講義の記事を書きました](https://www.robotics.it-chiba.ac.jp/j/?p=594)。こんなムービーを掲載しています。

<blockquote class="twitter-tweet"><p lang="und" dir="ltr">wwwwwwwww <a href="https://t.co/YAAq9dcNFP">pic.twitter.com/YAAq9dcNFP</a></p>&mdash; 千葉工大 未来ロボティクス学科 (@robo_cit) <a href="https://twitter.com/robo_cit/status/1201399538541400064?ref_src=twsrc%5Etfw">December 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

