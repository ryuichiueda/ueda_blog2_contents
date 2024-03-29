---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2019 Ryuichi Ueda
---

# 【問題】jus共催 jus共催 第45回せんせいがAIとかしんぎゅらりてぃーってタイトルにつけとくとべんきょうかいにひとがあつまるよっていってたかんけいないけどシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.45)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

　次のCSVファイル（Shift JIS）には、日ごとトマト、バナナ、ピーマンの売れた個数が書かれています。トマト、バナナ、ピーマンについて、記録されている最後の日の日付と個数を出力してください。

```
$ cat data.csv
2019/12/6,?g?}?g,3??
2019/11/23,?o?i?i,2??
2019/11/8,?s?[?}??,31??
2019/12/30,?g?}?g,4??
2019/11/2,?g?}?g,1??
2019/12/9,?o?i?i,4??
2019/12/21,?o?i?i,5??
2019/11/21,?s?[?}??,32??
2019/12/1,?g?}?g,7??
```

## Q2

　[日経のこのページ](https://indexes.nikkei.co.jp/nkave/index?type=download)（https://indexes.nikkei.co.jp/nkave/index?type=download ）
から日経平均株価の日次データをダウンロードして、毎月の終値の最高値と最安値を出力してください。


## Q3

　ファイル`flag_a, flag_b`には国旗が記録されていますが、何箇所か`flag_a`と`flag_b`で違いがあります。左上から数えて何番目の国旗が異なるかを出力してください（「何行目の何番目」ではなくて、1行目からの通算の個数で答えてください）。


```
$ head flags_*
==> flags_a <==
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇨🇳🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵

==> flags_b <==
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵
🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇰🇵🇮🇲🇰🇵
```

## Q4 

 次の`nabe`ファイルについて、一文字ごとに改行を入れてください。

```
$ cat nabe
部邊邊󠄓邊󠄓邉邉󠄊邉󠄂邊邊󠄓邊󠄓邉邉󠄆辺邉󠄄邊辺󠄀邉邉󠄈邉󠄊邉󠄌邊邊󠄓邊󠄓邉邉󠄆邉󠄊邊邊󠄓邊󠄓邉邉󠄆邉󠄘邊邊󠄓邊󠄓邉邉󠄆邉󠄕邊邊󠄓邊󠄓邉邉󠄊邉󠄓部
$ （ワンライナー）
部
邊
邊
邊
邉
邉
・・・
```

## Q5

　次のメッセージから、回文になっている部分をすべて抜き出してください。ある回文の中にある部分的な回文（例: 「きつつき」の場合「つつ」）を含んでも構いません。

```
$ cat message
きつつきとまとへんたいとまとたけやぶやけないたけやぶやけたでんぱゆんゆんおかしがすきすきすがしかお
```

## Q6

　Q5の答えが`message.ans`に入っています。この中から、部分的な回文を削除してください。



## Q7

`x/y`が割り切れない自然数の組`x,y (x<y)`について、`echo x y`からはじめて、計算結果（小数）を延々と出力するワンライナーを考えてください。

### 解答例


## Q8

　Q7で出力した小数は、いつか同じ数字の並びの繰り返しになります。繰り返しになったら小数の出力をてきとうなところで打ち切り、小数何桁目から何個の数字の繰り返しになるかを後ろにつけてください。（無限の桁まで対応する必要はありません。）

* 例

```
1/3 -> 0.3 1 1
1/7 -> 0.142857142857 1 6
```

