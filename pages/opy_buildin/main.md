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
### 何も定義しなくてもLが使える ###
$ seq 10 | shuf | opy '{L.append(F1)};E:[max(L)]'
10
### Lを使わないと面倒 ###
$ seq 10 | shuf | opy 'B:{a=0};{a=a if F1 < a else F1};E:[a]'
10
```

