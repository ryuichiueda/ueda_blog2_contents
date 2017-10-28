---
Keywords: ThinkPad,Ubuntu,nvidia,UEFI
Copyright: (C) 2017 Ryuichi Ueda
---

# ThinkPad T450 + Ubuntu環境にやっとnvidiaのドライバが入った

手順のメモです。

### 環境

* ThinkPad T450 (GeForce 940M)
* Ubuntu 17.04 Desktop

### 手順

* BIOSの画面を開いてUEFIのセキュアブートを無効にする
* 端末で

```bash
$ sudo apt install nvidia-375
$ sudo reboot
```

これで大丈夫っぽい。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ThinkPad T450 + Ubuntu にnvidiaのドライバを入れることについに成功した。2年ごしの悲願・・・（何をやっているのか） <a href="https://t.co/GYdbwYmb2F">pic.twitter.com/GYdbwYmb2F</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/924242794922762240?ref_src=twsrc%5Etfw">October 28, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


### 今までの失敗の理由（？）

UEFIのセキュアーブートを切るという試みを今までやってなかった。

### お断り

なにぶん謎が多く、何もしなくても`apt install nvidia-なんとか`でインストールされてしかるべきなものなので、うまくいかない場合もあると思います。


取り急ぎ。
