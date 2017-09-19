---
Keywords: コマンド,CLI,openssl,UNIX/Linuxサーバ,ファイルの暗号化
Copyright: (C) 2017 Ryuichi Ueda
---

# ファイルをopensslで暗号化し、復号する手順をまとめる。
こんにつわ。上田です。

ネットを探しまわってもopensslを使ったファイルの暗号、復号について、手順だけ書いた簡単なものがなかったので方法だけまとめます。ウンチク度ゼロでお送りします。

<h2>事前の準備</h2>

秘密鍵と公開鍵を準備します。

```bash
###秘密鍵を作る###
$ openssl genrsa -out seckey.pem -aes256 2048
&lt;パスフレーズを入力&gt;
###公開鍵を作る###
$ openssl rsa -in seckey.pem -pubout -out pubkey.pem
&lt;パスフレーズを入力&gt;
###できた###
$ ls
pubkey.pem seckey.pem
```

<h2>ファイルの暗号化（公開鍵を使う）</h2>

暗号の用途を考えると普通は他のマシンで暗号化するのだが、同じマシンで。

```bash
$ cat himitsu 
ここだけの話、部長の鼻毛、
付け鼻毛らしいよ。
$ openssl rsautl -pubin -inkey ./tmp/pubkey.pem -in himitsu -encrypt -out himitsu.secret
###暗号化される###
$ cat himitsu.secret 
?R??rj&gt;4ޣ+?K???:?v?K?&amp;?\\&amp;???M	+)?HE...
```

<h2>復号（秘密鍵を使う）</h2>

```bash
$ cat himitsu.secret | openssl rsautl -decrypt -inkey ./tmp/seckey.pem 
&lt;パスフレーズを入力&gt;
ここだけの話、部長の鼻毛、
付け鼻毛らしいよ。
```


以上。opensslさえインストールされていればそんなに難しくない！
