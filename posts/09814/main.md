---
Keywords: bash,SoftwareDesign,UNIX/Linuxサーバ,執筆,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Software Design7月号未掲載部分
本日発売です。bashのマニアック機能について<span style="color: #ff0000;">「使うなよ！絶対使うなよ！！」</span>というテイストで書きました。
<blockquote class="twitter-tweet" data-lang="ja">
<p dir="ltr" lang="ja">本日発売。8ページくらい書きました！！ | Software Design 2017年7月号 <a href="https://twitter.com/hashtag/gihyojp?src=hash">#gihyojp</a> <a href="https://t.co/U3DL5g10Ys">https://t.co/U3DL5g10Ys</a></p>
— Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/875863176432074752">2017年6月16日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

で、宣伝部分だと味気ないので、調子に乗って書きすぎて掲載できなかった部分をあまり加工せずに貼り付けておきまっす。bash3.2とbash4.4で挙動の違う例、4.0以降の新機能の例です。
<h2>数字のブレース展開のゼロ埋め</h2>
ブレース展開においてゼロ埋めができるようになっています。

```bash
bash-3.2$ echo {01..03}
1 2 3
bash-4.4$ echo {01..03}
01 02 03
```

<h3>Unicodeのコードポイント指定</h3>
Unicodeのコードポイントを指定して文字を出力できます。

<pre>
###UnicodeとUTF-8の16進数を指定してみる例###
bash-3.2$ echo -e '\\U1F363' '\\xF0\\x9F\\x8D\\xA3'
\\U1F363 🍣
bash-4.4$ echo -e '\\U1F363' '\\xF0\\x9F\\x8D\\xA3'
🍣 🍣
</pre>

次の例は、
この機能とxxdというコマンドを使ってUnicodeから
UTF-8へ変換するワンライナーです。

```bash
bash-4.4$ echo -en '\\U1F363' | xxd -ps
f09f8da3
```

<h2>case文で使う「;;&amp;」</h2>
次のcase文は、SHELLという変数の文字列がbashで終わっている場合に
「bash」と表示するものです。「\\*bash」というパターンにマッチして
echoを実行し、次の「\\*」は評価されずに終わっています。

```bash
bash-3.2$ case $SHELL in *bash ) echo bash ;; * ) echo defalut ;; esac
bash
```

バージョン4.0ではこの挙動に加え、
「;;&amp;」を用いて次のパターンも評価させることが可能となりました。

```bash
bash-4.4$ case $SHELL in *bash ) echo bash ;; * ) echo defalut ;; esac
bash
bash-4.4$ case $SHELL in *bash ) echo bash ;;& * ) echo defalut ;; esac
bash
defalut
```

<h2>大文字を小文字に強制変更する変数</h2>
declare -lで変数を宣言すると、代入した大文字が小文字に変換されます。

```bash
bash-4.4$ declare -l yesno
bash-4.4$ yesno=YeS
bash-4.4$ echo $yesno
yes #小文字になる
```

また、例は省略しますが、declare -uで宣言すると大文字に変換されます。

普通の変数に対して後から小文字大文字を変換することもできます。
変数の後ろに「^」や「,」をつけます。

```bash
bash-4.4$ y=YeS
bash-4.4$ echo ${y^^} #大文字に
YES
bash-4.4$ echo ${y,,} #小文字に
yes
bash-4.4$ echo ${y,} #1文字目だけ小文字に
yeS
```

<h2>ということで</h2>
買って読んでいただければ幸いです。

[amazonjs asin="B06ZY6PQKQ" locale="JP" title="ソフトウェアデザイン 2017年 07 月号 雑誌"]

こちらもお願いしまっす！
[amazonjs asin="B00XKU53U4" locale="JP" title="シェルプログラミング実用テクニック"]

