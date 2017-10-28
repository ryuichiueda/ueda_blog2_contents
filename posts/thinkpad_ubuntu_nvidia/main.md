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

### 今までの失敗の理由（？）

UEFIのセキュアーブートを切るという試みを今までやってなかった。

### お断り

なにぶん謎が多く、何もしなくても`apt install nvidia-なんとか`でインストールされてしかるべきなものなので、うまくいかない場合もあると思います。


取り急ぎ。
