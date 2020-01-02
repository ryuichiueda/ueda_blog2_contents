---
Copyright: (C) Ryuichi Ueda
---

# the opy book / 7. 組込変数・関数


* [目次に戻る](/?page=opy_book)

* [1. はじめに](/?page=opy_intro)
* [2. レコードとアクション](/?page=opy_action)
* [3. パターンによる検索](/?page=opy_pattern)
* [4. ルール（パターン + アクション）](/?page=opy_rule)
* [5. モジュールの利用](/?page=opy_module)
* [6. オプション](/?page=opy_options)


## 7.1 NF、NR

　AWKと同様、`opy`は内部に`NF`という変数を持っており、
最後に読み込んだ行の列数を保持しています。
例を示します。

``` 
### 入力するデータ ###
$ seq 10 | xargs -n 7
1 2 3 4 5 6 7
8 9 10
### 列数を出力 ###
$ seq 10 | xargs -n 7 | opy '[NF]'
7
3
``` 

　また、これもAWK同様、行番号を記録するための`NR`
という変数も組み込まれています。
`NR`を使って上の例の出力に
行番号をつける例を示します。

```
$ seq 10 | xargs -n 7 | opy '[str(NR)+":",NF]' 
1: 7
2: 3
```

## 7.2 FILENAME、FNR

　現在読み込んでいるファイルの名前は`FILENAME`
という変数に入っています。
また、`FNR`は、読み込んだファイルごとに行番号を
カウントするための変数です。
これらの変数もAWKのものと共通しています。

　次の例は`grep`で複数のファイルを読み込んだときのように、
`FILENAME`を使って検索結果にファイル名をつけて出力するというものです。

```
### 文字「X」の検索結果の頭にファイル名をつける ###
$ opy 'r_("X"):[FILENAME+":",F0]' README.md LICENSE
README.md: * See [EXAMPLES.md](./EXAMPLES.md)
README.md: See [EXAMPLES.md](./EXAMPLES.md)
LICENSE: THE SOFTWARE IS PROVIDED "AS IS", WITH...
```

　`FNR`の例も示します。上の例を少し変えて、
検索結果代わりに`FNR`、`NR`を出力してみます。

```
$ opy 'r_("X"):[FILENAME,FNR,NR]' README.md LICENSE
README.md 16 16
README.md 37 37
LICENSE 15 65
```

これを見ると、`LICENSE`の15行目に`X`があったことが分かります。
また、`NR`と比較すると、`FNR`はファイルが変わるとリセットされている
ので値が小さくなっています。


## 7.3 組込リスト L

　`opy`には、初期化されたリスト`L`が組み込まれています。
これは、例えば次のように行を跨いだ処理をするときに便利です。

```
### 読み込んだ数字の最大値を求める ###
$ seq 10 | shuf | opy '{L.append(F1)};E:[max(L)]'
10
### Lを使わないと面倒 ###
$ seq 10 | shuf | opy 'B:{a=0};{a=a if F1 < a else F1};E:[a]'
10
```

## 7.4 組込辞書 D

　辞書も`D`という名前で同様に組み込まれています。
キーのあるデータの処理に便利です。

```
### サンプルデータ ###
$ echo -e 'a 1\nb 2\na 3\nb 4'
a 1
b 2
a 3
b 4
### キーごとに最大値を求める ###
$ echo -e 'a 1\nb 2\na 3\nb 4' 
| opy '{D[F1]=D[F1] if D[F1] > F2 else F2};E:[D]'
defaultdict(<class 'int'>, {'a': 3, 'b': 4})
```

辞書に登録されていないキーを与えると、
通常はエラーとなります。しかし、上の例をよく読むと分かるのですが、
`D`はPythonの`defaultdict`というクラスのオブジェクトで、
`opy`では0（int型）に初期化されています。
int型で初期化していますが、Pythonと同様、文字列などのデータで
書き換えることは可能です。


## 7.5 組込辞書 K

　`opy`にはもう一つ、`K`という辞書もあらかじめ準備されています。
`K`は空のリストで初期化されているので、
キーごとにデータを全て保存することを簡単にします。

```
### キーごとにデータを保存して最後にprint ###
$ echo -e 'a 1\nb 2\na 3\nb 4' | opy '{K[F1].append(F2)};E:[K]'
defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 4]})
### キーごとに最大値を求める ###
$ echo -e 'a 1\nb 2\na 3\nb 4' 
| opy '{K[F1].append(F2)};E:[{k:max(K[k]) for k in K}]'
{'a': 3, 'b': 4}
### 複数の値も保存可能 ###
$ echo -e 'a 1\nb 2 c\na 3\nb 4 e'
a 1
b 2 c
a 3
b 4 e
$ echo -e 'a 1\nb 2 c\na 3\nb 4 e' 
| opy '{K[F1].append(F[2:])};E:[K]'
defaultdict(<class 'list'>, {'a': [[1], [3]], 'b': [[2, 'c'], [4, 'e']]})
```

