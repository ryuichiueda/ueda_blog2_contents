---
Keywords: 頭の中だだ漏らし,どうでもよい,make

Copyright: (C) 2018 Ryuichi Ueda
---

# 🍣でmakeの挙動を雑に説明

　昨日は、絵文字を`make`と`Makefile`で使えることを発見したので色々遊んでいた。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">こういう感じのMakefileが書ける． <a href="https://twitter.com/hashtag/%E6%9B%B8%E3%81%8D%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84?src=hash&amp;ref_src=twsrc%5Etfw">#書きたくない</a> <a href="https://t.co/tdjl9hQucZ">pic.twitter.com/tdjl9hQucZ</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/969543815362093056?ref_src=twsrc%5Etfw">2018年3月2日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

`make`はCやC++のソースの処理に使うものというのが一般的な認識なのだが、シェルスクリプトのように使うこともできる。例えば、

```
sushi: 🐟
	echo 寿司が作れる
🐟:
	echo 魚を仕入れる
```

というmakeファイルを`Makefile`という名前で作り、そのディレクトリで`make`と打つと

```
$ make sushi
echo 魚を仕入れる
魚を仕入れる
echo 寿司が作れる
寿司が作れる
``` 

というような出力が得られる。`Makefile`の1行目の`sushi: 🐟`は、

* 右下に記述された処理（ここでは1行だがタブでインデントして何行でも書ける）にsushiという名前がついていること
* sushiの実行には🐟が必要であること

を意味している。「🐟」という処理は`🐟:`以下に書いてある。sushiには🐟が必要なので、`make`は🐟以下の処理から先に始め、その次にsushiの処理を実行するので上のような出力が得られる。

　ということで、`Makefile`に「xの処理にはyが必要」というルールを記述すると、それにしたがって動くコマンド操作を記述することができる。これが、「xxx.oを作るにはxxx.cが必要」というようなルールを記述する時に便利なので、`make`がビルドに使われる。

　ちなみに、上記の例では「寿司を作るのにご飯がない」という致命的な間違いを犯している。正しくは、次のツイートのようにご飯を作るためのルール、そして魚がどのように育つかというルールを追加する必要がある。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">こういうふうにMakefileを作ると・・・ <a href="https://t.co/ghLLXznykH">pic.twitter.com/ghLLXznykH</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/969753245764665344?ref_src=twsrc%5Etfw">March 3, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

すると、`make`は次のように、寿司が💩から作られることを、なんのためらいもなく理路整然と説明する。ここで`-s`は処理の手順の出力を省き、結果だけを出力するためのオプションである。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">🍣が💩からできていることがわかる。 <a href="https://t.co/iXl95wiPKX">pic.twitter.com/iXl95wiPKX</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/969753388672892929?ref_src=twsrc%5Etfw">March 3, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

なお、🍣から💩を作るプロセスを`Makefile`に書いてしまうと、おそらくエラーが出てしまう。輪廻を表現できるような拡張が、今後、必要と考えられる。

繰り返しになるが、🍣は💩からできている。大自然に感謝の念しかない。


以上。
