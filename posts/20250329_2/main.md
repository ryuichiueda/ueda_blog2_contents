---
Keywords: 自作シェル,rusty_bash,寿司シェル
Copyright: (C) 2025 Ryuichi Ueda
---

# 自作シェルの進捗（2025年3月29日その2）

　[前の記事](/?post=20250329)の続きです。

## Bashのテストへの対応

　Bashのテスト、エッジケースが多い上にテストスクリプト自体がbash-completion並みに変態なので、それに対応せねばならずいろいろ調べてました。

### functionと書けば`()`が省略できる

### Bashのglobstarは同じパスを何回も出す

### IFS地獄
