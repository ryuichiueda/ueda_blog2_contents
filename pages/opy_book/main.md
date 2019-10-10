---
Copyright: (C) Ryuichi Ueda
---

# the opy book

## 1. はじめに

* [1. はじめに](/?page=opy_intro)

## 2. レコードとアクション

* [2. レコードとアクション](/?page=opy_action)


## 3. パターンによる検索


　opyは、AWKのように`grep`の拡張版として利用することができます。たとえば、次の例は`seq 5`の結果から偶数の行を検索するものです。

```
$ seq 5
1
2
3
4
5
$ seq 5 | opy 'F1%2==0'
2
4
```


　`opy`に引数として与えた`F1%2==0`のことを「パターン」と呼びます。パターンにはboolを返す式を記述できます。いくつか例を示します。

```
### F1の文字列の長さが3のものを検索 ###
$ cat hoge
aaa bb
ccccc d
eeee fffff
$ cat hoge | opy 'len(F1)==3'
aaa bb
### 2以上4未満を検索 ###
$ seq 5 | opy '2<=F1<4'
2
3
### 5つの数字が全て異なる行を出力 ###
$ cat nums 
1 2 3 4 5
2 3 3 5 4
1 2 2 3 3
uedambp2:R2_KAKEN ueda$ cat nums | opy 'len(set(F[1:]))==5'
1 2 3 4 5
```

　最後の行の`F[1:]`は、1列目以降のデータが入ったリストです。

## 4. リストアクション
