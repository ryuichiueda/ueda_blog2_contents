---
Keywords:||,シェルスクリプト,&amp;&amp;,bash,UNIX/Linuxサーバ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->シェルの&&||パズル<!--:-->
<!--:ja-->問題です。シェル（bashを使用）で次のコマンド列をたたいたとき、「OK」と出るのはどれとどれでしょうか？<br />
<br />
解説は後日。<br />
<br />
[bash]<br />
$ false &amp;&amp; true || true &amp;&amp; echo OK &lt;- 1<br />
$ true &amp;&amp; true || false || echo OK &lt;- 2<br />
$ true || true || true &amp;&amp; echo OK &lt;- 3<br />
$ false &amp;&amp; true || false || echo OK &lt;- 4<br />
[/bash]<!--:-->
