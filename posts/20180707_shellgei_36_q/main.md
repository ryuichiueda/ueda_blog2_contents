---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2018 Ryuichi Ueda
---

# 【問題のみ】jus共催 第36回七夕・・・7は素数じゃないですか（しかも2つ）シェル芸勉強会

<!--[当日の様子はこちら](/?post=20180408_shellgei_35_summary)-->

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.36)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

<!-- もっと良い別解がたくさんありますので、 https://togetter.com/li/1216252 も参考に。-->

## Q1

`welcome.txt`に隠されたメッセージを読み取ってください。また、`welcome.txt`をワンライナーで作ってみてください。


## Q2

次のファイル群について、全てファイル名を`N年M組.doc`（`N`は半角数字、`M`は半角大文字）に揃えて徳を積んでください。

```
$ ls
1-B.doc     3年Ｃ組.doc  ３年A組.doc  １ーC.doc    ４年Ｃ組.doc
1A.doc      4年a組.doc   ３年B組.doc  １ーD.doc
3年D組.doc  5年A組.doc   ４年B組.doc  １年E組.doc
```

### 出典

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">これ最悪じゃないですか <a href="https://t.co/O2ezYAFMMK">pic.twitter.com/O2ezYAFMMK</a></p>&mdash; 漁師 (@6Lgug) <a href="https://twitter.com/6Lgug/status/1011529645559173120?ref_src=twsrc%5Etfw">June 26, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## Q3 

2018年のすべての日付について、2,3,5,7が4つ含まれる日付を列挙してください（例: 2018年3月22日など）。

## Q4

俳句を考え、次の短冊に縦書きで入れてください。

```
$ cat tanzaku
┏ ーー-┷-ーー┓
┃ 　　　　　 ┃
┃ 　　　　　 ┃
┃ 　　　　　 ┃
┃ 　　　　　 ┃
┃ 　　　　　 ┃
┃　　 　　　 ┃
┃　　 　　　 ┃
┗ーーーーーー┛
```

## Q5

`cowsay`の牛を右向きにして吹き出しの位置を調整して下さい。（万が一右向きオプションがあったら、それは使わずにお願いします。）

* 例

```
              ________________________________
             < あなたとJava今すぐダウンロード >
              --------------------------------
               ^__^   /
       _______/(oo)  /
   /\/(       /(__)
      | w----||
      ||     ||
```


## Q6

`seq 20`の出力について、次のように素数を丸囲みしてください。

```
1
②
③
4
⑤
6
⑦
8
9
10
⑪
12
⑬
14
15
16
⑰
18
⑲
20
```

## Q7

`text`には、文字や空白、改行として認識されないバイナリが含まれています。どの行にどんなものがあるか調査してください。

## Q8


```
$ echo 嘘は嘘であると見抜ける人でないと（掲示板を使うのは）難しい
```

から始めて、出力で次のようにルビを打ってください。多少ずれたりスペースが入っても構いません。

```
ｳｿ  ｳｿ        ﾐﾇ      ﾋﾄ          ｹｲｼﾞﾊﾞﾝ  ﾂｶ        ﾑｽﾞｶ
嘘は嘘であると見抜ける人でないと（掲示板 を使うのは）難しい
```
