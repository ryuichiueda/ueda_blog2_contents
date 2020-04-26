---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2020 Ryuichi Ueda
---

# 【問題のみ】jus共催 第47回引きこもりシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.47)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 19.10 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。
* 出典
    * [奥村晴彦: C言語による最新アルゴリズム事典, 技術評論社, 1991.](https://gihyo.jp/book/2018/978-4-7741-9690-9)


## Q1

次の`nums`ファイルについて、

```
$ cat nums
1, 3-5, 8, 10, 13-18, 20
```

次のようにハイフンで省略されている数字を復元してください。

```
1, 3, 4, 5, 8, 10, 13, 14, 15, 16, 17, 18, 20
```

## Q2

次のファイルについて、文字を並び替えるとちょうどウポポイになる行の行番号を出力してください。

```upopoi
ウポポイ
ウポイア
ウイポポポ
ワポイイ
ポパイ
ウホホイ
ウポイポ
ポウイポ
ポポウイ
ウンコ
ウポイいいいいポ
ポポウウ
ウポポポポ
```

## Q3

次の`noguruguru`ファイルについて、

```noguruguru
┃┃┗━━━┛┃┃
┗━━━━━━━┛
┃┃┏━━━━┓┃
┃┗━━━━━┛┃
┃┏━━━━━━┓
```

次のように並び替えてください。行番号は使わないでください。

```guruguru
┃┏━━━━━━┓
┃┃┏━━━━┓┃
┃┃┗━━━┛┃┃
┃┗━━━━━┛┃
┗━━━━━━━┛
```

## Q4


479は9つの連続した素数の和で表せます。この9つの素数を出力してください。
　
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="und" dir="ltr"><a href="https://t.co/wzilaKVKKi">https://t.co/wzilaKVKKi</a></p>&mdash; くおん (@qwertanus) <a href="https://twitter.com/qwertanus/status/1242016369324875781?ref_src=twsrc%5Etfw">March 23, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



## Q5

次のファイル`unko`について

```
$ cat unko 
💩

        💩  
      💩
　　　💩
🚽  　　　💩
🚽
  💩　　　
        　　
💩💩💩💩🚽💩　　

```

次のように、浮いている💩と🚽を落としてください。もしかしたら環境によって💩の位置がずれるかもしれませんので、端末の出力に基づいて各自の解釈でやってください。

```
💩　　　　　　　
🚽　　💩　　　　
🚽💩　💩💩💩　　
💩💩💩💩🚽💩
```

## Q6

次の画像のように、異なる種類の絵文字で画面を埋めてください。

![](./emojiterminal.png)

画像のように肌の色などの出力は乱れても構いません。必要なら

```
$ sudo apt install unicode-data
```

して`/usr/share/unicode/`下のデータを使ってください。


## Q7

次の`spaces`ファイルについて、どの種類のスペースがいくつずつ含まれるのか、リストを作ってください。

```
$ cat spaces
    　　　　　　
 
         
    
     
     
        


```

## Q8

次の文字列からアクセントをとってピュアなunkoにしてください。（単純にúをuに置換するという解はダメです。）

```
úńķô
```

