---
Copyright: (C) Ryuichi Ueda
---

# opyの便利な使い方集

## 基数変換（n進数→m進数）

### n進数→10進数

接頭辞をつけると、内部で整数に変換され、`print`すると10進数で表示されます。

```
$ echo 0b11 | opy '[F1]'
3
$ echo 0o10 | opy '[F1]'
8
$ echo 0x10 | opy '[F1]'
16
```

