---
Copyright: (C) Ryuichi Ueda
---

# opyの便利な使い方集

## opyって何？

opyは、ワンライナーでPythonを使うためのラッパーコマンドです。

* [インストールはこちらから](https://github.com/ryuichiueda/opy)

## 電卓として使う

`eval`で文字列を評価するとできます。

```
$ echo '2**10' | opy '[eval(F0)]'
1024
$ echo 'math.cos(math.pi)' | opy '[eval(F0)]'
-1.0
```

## 基数変換（n進数→m進数）

### n進数→10進数

接頭辞がついていれば、内部で自動的に整数に変換され、`print`すると10進数で表示されます。

```
$ echo 0b11 | opy '[F1]'
3
$ echo 0o10 | opy '[F1]'
8
$ echo 0x10 | opy '[F1]'
16
```

接頭語がなければ、つけてから処理しましょう。（`sed`でやるべきですが。）

```
$ echo aaaaaaaaaa | opy '["0x"+F1]' | opy '[F1]'
733007751850
```

### 10進数→n進数

```
$ echo 16 | opy '[bin(F1)]'
0b10000
$ echo 16 | opy '[oct(F1)]'
0o20
$ echo 16 | opy '[hex(F1)]'
0x10
```

### n進数→m進数


上のふたつのパターンの組み合わせです。

```
$ echo 0x10 | opy '[oct(F1)]'
0o20
```
