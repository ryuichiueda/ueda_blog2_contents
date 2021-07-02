---
Copyright: (C) Ryuichi Ueda
---

# opyの便利な使い方集

## opyって何？

opyは、ワンライナーでPythonを使うためのラッパーコマンドです。

* [インストールはこちらから](https://github.com/ryuichiueda/opy)

## 電卓として使う

　`eval`で文字列を評価するとできます。

```bash
$ echo '2**10' | opy '[eval(F0)]'
1024
$ echo 'math.cos(math.pi)' | opy '[eval(F0)]'
-1.0
```

若干補足すると、`F0`には、毎行読み込んだ文字列が入ります。`[ ]`はPythonのリストで、リストの中に処理を書いておくと、上の例のように処理結果がprintされます。`math`は自動で`import`されます。

## 基数変換（n進数→m進数）

### n進数→10進数

　接頭辞がついていれば、内部で自動的に整数に変換され、`print`すると10進数で表示されます。

```bash
$ echo 0b11 | opy '[F1]'
3
$ echo 0o10 | opy '[F1]'
8
$ echo 0x10 | opy '[F1]'
16
```

補足: `F1`は読み込んだ行の1列目の文字列が入ります。文字列が数字として解釈できる場合、自動的に数字に変換されます。

　接頭語がなければ、つけてから処理しましょう。（`sed`でやるべきですが。）

```bash
$ echo aaaaaaaaaa | opy '["0x"+F1]' | opy '[F1]'
733007751850
```

### 10進数→n進数

```bash
$ echo 16 | opy '[bin(F1)]'
0b10000
$ echo 16 | opy '[oct(F1)]'
0o20
$ echo 16 | opy '[hex(F1)]'
0x10
```

### n進数→m進数


上のふたつのパターンの組み合わせです。

```bash
$ echo 0x10 | opy '[oct(F1)]'
0o20
```

## YAML/JSON/XML形式のデータの読み込み/編集

　いずれも、入力全体を読み込んでパースし、辞書`T`にセットします。次は、JSONの処理の例です。


```bash
### 処理するJSONデータ ###
$ curl -s https://file.ueda.tech/eki/p/13.json
{"line":[{"line_cd":11301,"line_name":"JR東海道本線(東京～熱海)"},{"line_cd":11302,"line_name":"JR山手線"},（以下略）
### Tをリストに入れると全部出力できる ###
curl -s https://file.ueda.tech/eki/p/13.json | opy -t json '[T]'
{'line': [{'line_cd': 11301, 'line_name': 'JR東海道本線(東京～熱海)'},（以下略）
### 要素の参照 ###
$ curl -s https://file.ueda.tech/eki/p/13.json | opy -t json '[T["line"][0]]'
{'line_cd': 11301, 'line_name': 'JR東海道本線(東京～熱海)'}
### 路線のリストを出力する例 ###
$ curl -s https://file.ueda.tech/eki/p/13.json | opy -t json '[e["line_name"] for e in T["line"]]'
JR東海道本線(東京～熱海)
JR山手線
JR南武線
JR武蔵野線
JR横浜線
・・・
```

YAMLの例です。

```bash
$ cat ~/tmp/hoge.yml
aho:
  boke: ["a","b"]
### ahoの下のbokeの配列の0から数えて1番目の要素を取り出す ###
$ cat ~/tmp/hoge.yml | opy -t yaml '[T["aho"]["boke"][1]]'
b
### 改竄して出力 ###
$ cat ~/tmp/hoge.yml | opy -t yaml '{T["aho"]["boke"][1]="KAIZAN"};[yaml.dump(T)]'
aho:
  boke:
  - a
  - KAIZAN
```

XMLの例です。`xml.etree.ElementTree`を使っており、JSONやYAMLの場合とは少し扱いが異なります。

```bash
### Tにはオブジェクトが入っている ###
$ curl -s https://file.ueda.tech/eki/p/13.xml | opy -t xml '[e for e in T]' 
<Element 'pref' at 0x7fcea5286720>
<Element 'line' at 0x7fcea5286810>
<Element 'line' at 0x7fcea5286900>
・・・
### lineのタグを持つ要素だけ抽出 ###
$ curl -s https://file.ueda.tech/eki/p/13.xml | opy -t xml '[e for e in T if e.tag == "line"]'
<Element 'line' at 0x7fb1cb4347c0>
<Element 'line' at 0x7fb1cb4348b0>
<Element 'line' at 0x7fb1cb4349a0>
・・・
### 要素の内容を取り出す（名前でなく数字で要素を指定する） ###
$ curl -s https://file.ueda.tech/eki/p/13.xml | opy -t xml '[e[1].text for e in T if e.tag == "line"]'
JR東海道本線(東京～熱海)
JR山手線
JR南武線
・・・
```


## CSVファイルを扱う

　ふたつ方法があります。

### 毎行処理する

　`-c`を使います。

```
$ echo 'a,b,c' | opy -c '[F2]'
b
### エスケープだらけでも大丈夫 ###
$ echo 'a,"""b,,,,""""",c' | opy -c '[F2]'
"b,,,,""
```

この方法は、データの中に改行がある場合には使えません。


```
$ echo -e 'a,"b\nc",d'
a,"b                      <-「b改行c」がひとかたまりのデータ
c",d
$ echo -e 'a,"b\nc",d' | opy -c '[F2]'
b
d          <-ここはcと出なければならないが、出てこない
```


### 全体を読んで処理する

　`-t csv`を使います。`T[m][n]`で`m`行`n`列目のデータが取得できます。`m`、`n`は0から始まります。

```
$ echo -e 'a,"b\nc",d'
a,"b                      <- -cでは扱えなかったデータ
c",d
$ echo -e 'a,"b\nc",d' | opy -t csv '[T]'
{0: ['a', 'b\nc', 'd']}                            <- 改行がデータの一部として認識されている
$ echo -e 'a,"b\nc",d' | opy -t csv '[T[0][1]]'    <- 0行1列目を出力
b
c               <- -cのときと異なり、「b改行c」がデータとして出力される
### 改行を別の文字に置き換える例 ###
$ echo -e 'a,"b\nc",d' | opy -t csv '[T[0][1].replace("\n","@")]'
b@c
```

