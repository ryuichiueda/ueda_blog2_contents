---
Keywords: プログラミング,マイナスゼロとはこれいかに？,Python,round
Copyright: (C) 2017 Ryuichi Ueda
---

# Pythonのround関数の-0.0はどうにかならんのでしょうか？
タイトルのままなんですが、負の数字を丸めてゼロになるときに -0 とか -0.0 とか出てきて微妙に困っております。

```bash
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> round(-1.1,-1)
-0.0
>>> round(-1.1,-1)*1.0
-0.0
```

どーやったらマイナスでないゼロになる？


情報乞う。

※以下、追記

こんなん見つけた。<a href="http://mail.python.org/pipermail/python-bugs-list/2006-October/035573.html">http://mail.python.org/pipermail/python-bugs-list/2006-October/035573.html</a>
