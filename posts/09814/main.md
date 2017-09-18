---
Keywords:bash,SoftwareDesign,UNIX/Linuxサーバ,執筆,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Software Design7月号未掲載部分
本日発売です。bashのマニアック機能について<span style="color: #ff0000;">「使うなよ！絶対使うなよ！！」</span>というテイストで書きました。<br />
<blockquote class="twitter-tweet" data-lang="ja"><br />
<p dir="ltr" lang="ja">本日発売。8ページくらい書きました！！ | Software Design 2017年7月号 <a href="https://twitter.com/hashtag/gihyojp?src=hash">#gihyojp</a> <a href="https://t.co/U3DL5g10Ys">https://t.co/U3DL5g10Ys</a></p><br />
— Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/875863176432074752">2017年6月16日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
で、宣伝部分だと味気ないので、調子に乗って書きすぎて掲載できなかった部分をあまり加工せずに貼り付けておきまっす。bash3.2とbash4.4で挙動の違う例、4.0以降の新機能の例です。<br />
<h2>数字のブレース展開のゼロ埋め</h2><br />
ブレース展開においてゼロ埋めができるようになっています。<br />
<br />
[bash]<br />
bash-3.2$ echo {01..03}<br />
1 2 3<br />
bash-4.4$ echo {01..03}<br />
01 02 03<br />
[/bash]<br />
<br />
<h3>Unicodeのコードポイント指定</h3><br />
Unicodeのコードポイントを指定して文字を出力できます。<br />
<br />
<pre><br />
###UnicodeとUTF-8の16進数を指定してみる例###<br />
bash-3.2$ echo -e '\\U1F363' '\\xF0\\x9F\\x8D\\xA3'<br />
\\U1F363 🍣<br />
bash-4.4$ echo -e '\\U1F363' '\\xF0\\x9F\\x8D\\xA3'<br />
🍣 🍣<br />
</pre><br />
<br />
次の例は、<br />
この機能とxxdというコマンドを使ってUnicodeから<br />
UTF-8へ変換するワンライナーです。<br />
<br />
[bash]<br />
bash-4.4$ echo -en '\\U1F363' | xxd -ps<br />
f09f8da3<br />
[/bash]<br />
<br />
<h2>case文で使う「;;&amp;」</h2><br />
次のcase文は、SHELLという変数の文字列がbashで終わっている場合に<br />
「bash」と表示するものです。「\\*bash」というパターンにマッチして<br />
echoを実行し、次の「\\*」は評価されずに終わっています。<br />
<br />
[bash]<br />
bash-3.2$ case $SHELL in *bash ) echo bash ;; * ) echo defalut ;; esac<br />
bash<br />
[/bash]<br />
<br />
バージョン4.0ではこの挙動に加え、<br />
「;;&amp;」を用いて次のパターンも評価させることが可能となりました。<br />
<br />
[bash]<br />
bash-4.4$ case $SHELL in *bash ) echo bash ;; * ) echo defalut ;; esac<br />
bash<br />
bash-4.4$ case $SHELL in *bash ) echo bash ;;&amp; * ) echo defalut ;; esac<br />
bash<br />
defalut<br />
[/bash]<br />
<br />
<h2>大文字を小文字に強制変更する変数</h2><br />
declare -lで変数を宣言すると、代入した大文字が小文字に変換されます。<br />
<br />
[bash]<br />
bash-4.4$ declare -l yesno<br />
bash-4.4$ yesno=YeS<br />
bash-4.4$ echo $yesno<br />
yes #小文字になる<br />
[/bash]<br />
<br />
また、例は省略しますが、declare -uで宣言すると大文字に変換されます。<br />
<br />
普通の変数に対して後から小文字大文字を変換することもできます。<br />
変数の後ろに「^」や「,」をつけます。<br />
<br />
[bash]<br />
bash-4.4$ y=YeS<br />
bash-4.4$ echo ${y^^} #大文字に<br />
YES<br />
bash-4.4$ echo ${y,,} #小文字に<br />
yes<br />
bash-4.4$ echo ${y,} #1文字目だけ小文字に<br />
yeS<br />
[/bash]<br />
<br />
<h2>ということで</h2><br />
買って読んでいただければ幸いです。<br />
<br />
[amazonjs asin="B06ZY6PQKQ" locale="JP" title="ソフトウェアデザイン 2017年 07 月号 雑誌"]<br />
<br />
こちらもお願いしまっす！<br />
[amazonjs asin="B00XKU53U4" locale="JP" title="シェルプログラミング実用テクニック"]<br />

