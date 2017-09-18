---
Keywords:コマンド,CLI,openssl,UNIX/Linuxサーバ,ファイルの暗号化
Copyright: (C) 2017 Ryuichi Ueda
---
# ファイルをopensslで暗号化し、復号する手順をまとめる。
こんにつわ。上田です。<br />
<br />
ネットを探しまわってもopensslを使ったファイルの暗号、復号について、手順だけ書いた簡単なものがなかったので方法だけまとめます。ウンチク度ゼロでお送りします。<br />
<br />
<h2>事前の準備</h2><br />
<br />
秘密鍵と公開鍵を準備します。<br />
<br />
[bash]<br />
###秘密鍵を作る###<br />
$ openssl genrsa -out seckey.pem -aes256 2048<br />
&lt;パスフレーズを入力&gt;<br />
###公開鍵を作る###<br />
$ openssl rsa -in seckey.pem -pubout -out pubkey.pem<br />
&lt;パスフレーズを入力&gt;<br />
###できた###<br />
$ ls<br />
pubkey.pem seckey.pem<br />
[/bash]<br />
<br />
<h2>ファイルの暗号化（公開鍵を使う）</h2><br />
<br />
暗号の用途を考えると普通は他のマシンで暗号化するのだが、同じマシンで。<br />
<br />
[bash]<br />
$ cat himitsu <br />
ここだけの話、部長の鼻毛、<br />
付け鼻毛らしいよ。<br />
$ openssl rsautl -pubin -inkey ./tmp/pubkey.pem -in himitsu -encrypt -out himitsu.secret<br />
###暗号化される###<br />
$ cat himitsu.secret <br />
?R??rj&gt;4ޣ+?K???:?v?K?&amp;?\\&amp;???M	+)?HE...<br />
[/bash]<br />
<br />
<h2>復号（秘密鍵を使う）</h2><br />
<br />
[bash]<br />
$ cat himitsu.secret | openssl rsautl -decrypt -inkey ./tmp/seckey.pem <br />
&lt;パスフレーズを入力&gt;<br />
ここだけの話、部長の鼻毛、<br />
付け鼻毛らしいよ。<br />
[/bash]<br />
<br />
<br />
以上。opensslさえインストールされていればそんなに難しくない！
