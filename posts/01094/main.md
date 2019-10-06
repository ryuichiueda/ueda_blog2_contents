---
Keywords: ||,シェルスクリプト,&&,bash,UNIX/Linuxサーバ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルの&&||パズル

問題です。シェル（bashを使用）で次のコマンド列をたたいたとき、「OK」と出るのはどれとどれでしょうか？

解説は後日。

```bash
$ false && true || true && echo OK <- 1
$ true && true || false || echo OK <- 2
$ true || true || true && echo OK <- 3
$ false && true || false || echo OK <- 4
```
