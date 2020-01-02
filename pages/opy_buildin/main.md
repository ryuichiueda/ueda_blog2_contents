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


## 7.1 組込リスト

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

## 7.2 組込辞書 `D`

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


## 7.3 組込辞書 `K`

　`opy`にはもう一つ、`K`という辞書もあらかじめ準備されています。
`K`は空のリストで初期化されているので、
キーごとにデータを全て保存することを簡単にします。

```
$ echo -e 'a 1\nb 2\na 3\nb 4' | opy '{K[F1].append(F2)};E:[K]'
defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 4]})
```
