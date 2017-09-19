---
Keywords: ||,シェルスクリプト,&amp;&amp;,bash,UNIX/Linuxサーバ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->シェルの&&||パズル<!--:-->
<!--:ja-->問題です。シェル（bashを使用）で次のコマンド列をたたいたとき、「OK」と出るのはどれとどれでしょうか？

解説は後日。

```bash
$ false &amp;&amp; true || true &amp;&amp; echo OK &lt;- 1
$ true &amp;&amp; true || false || echo OK &lt;- 2
$ true || true || true &amp;&amp; echo OK &lt;- 3
$ false &amp;&amp; true || false || echo OK &lt;- 4
```<!--:-->
