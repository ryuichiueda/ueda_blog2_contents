---
Copyright: (C) Ryuichi Ueda
---

# opyの便利な使い方集

[インストールはこちらから](https://github.com/ryuichiueda/opy)

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

