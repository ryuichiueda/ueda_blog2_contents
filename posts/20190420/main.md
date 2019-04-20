---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# ケツダイラコマンド作った

　本日は新しい言語に触ろうということでGoでぷよぐらみんぐしました。もう14年前に終わった企画ですが知る人ぞ知る「[けつだいらアウォード](http://sledge-hammer-web.my.coocan.jp/names.htm)」のトリビュートコマンドを作りました。まだ不完全ですが一応動きます。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ケツダイラコマンド整備中。家族に昼食を作るために中断。<a href="https://t.co/JW0E9KZZGD">https://t.co/JW0E9KZZGD</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1119430303108304898?ref_src=twsrc%5Etfw">2019年4月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

あと、Goはびっくりするぐらい分かりやすかったし、スクリプト言語としてもコンパイル言語としても動くのでちょっと力入れて勉強しようと思います。すぐ習得できそうですが。



## 動かし方

　READMEにも書きましたが、Ubuntuなら次の通りです。

```
$ sudo apt install golang
$ sudo apt install mecab mecab-ipadic-utf8 libmecab-dev
$ export CGO_LDFLAGS="`mecab-config --libs`"
$ export CGO_CFLAGS="-I`mecab-config --inc-dir`"
$ go get github.com/shogo82148/go-mecab
$ echo デーモン 小暮閣下 | go run ke2daira.go
コーモン デグレカッカ
```

コーモンがデグレます。

### 例

　元ネタはたぶんほぼすべてけつだいらアウォードからです（出尽くしている感）。

```
$ echo ピエール 瀧 | ke2daira
タエール ピキ
$ echo あとう かい | ke2daira
カトウ アイ
$ echo 横浜 ベイスターズ | ke2daira
ベコハマ ヨイスターズ
$ echo ジャイアント 馬場 | ke2daira
バャイアント ジバ
$ echo フジパン 本仕込 | ke2daira
ホジパン フンシコミ
$ echo 千葉県 | mecab -Owakati | ke2daira | tr -d ' ' | nkf -h
けばちん
```


　以上。これからシェル芸botに採用してもらうんだ・・・。でも眠い。


　追伸: シェル芸botに組み込んでもらえました！インパクトファクター高い！

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">しりもんいち <a href="https://t.co/5Wbp5SNaFP">https://t.co/5Wbp5SNaFP</a></p>&mdash; シェル芸bot (@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/1119602324983259136?ref_src=twsrc%5Etfw">2019年4月20日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

