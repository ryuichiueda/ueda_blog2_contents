---
Keywords:プログラミング,マイナスゼロとはこれいかに？,Python,round
Copyright: (C) 2017 Ryuichi Ueda
---
# Pythonのround関数の-0.0はどうにかならんのでしょうか？
タイトルのままなんですが、負の数字を丸めてゼロになるときに -0 とか -0.0 とか出てきて微妙に困っております。<br />
<br />
[bash]<br />
Python 2.7.2 (default, Oct 11 2012, 20:14:37) <br />
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin<br />
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.<br />
&gt;&gt;&gt; round(-1.1,-1)<br />
-0.0<br />
&gt;&gt;&gt; round(-1.1,-1)*1.0<br />
-0.0<br />
[/bash]<br />
<br />
どーやったらマイナスでないゼロになる？<br />
<br />
<br />
情報乞う。<br />
<br />
※以下、追記<br />
<br />
こんなん見つけた。<a href="http://mail.python.org/pipermail/python-bugs-list/2006-October/035573.html">http://mail.python.org/pipermail/python-bugs-list/2006-October/035573.html</a>
