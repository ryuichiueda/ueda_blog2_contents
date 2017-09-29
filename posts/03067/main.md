---
Keywords: どうでもいい,シェルスクリプト,CLI,小ネタ,紙のカレンダーは地球に優しくない
Copyright: (C) 2017 Ryuichi Ueda
---

# 一年分のカレンダーを表示するシェルスクリプト
なんとなく作ってしまった・・・

<span style="color:red">（追記：cal 2014でいいじゃないか！！！！知らなかったじゃないか！！！！ということでpaste芸＆ <( )芸をお楽しみください。）</span>

```bash
ueda\@remote:~$ cat caly 
#!/bin/bash

paste <(cal 1 "$1") <(cal 2 "$1") <(cal 3 "$1")
paste <(cal 4 "$1") <(cal 5 "$1") <(cal 6 "$1")
paste <(cal 7 "$1") <(cal 8 "$1") <(cal 9 "$1")
paste <(cal 10 "$1") <(cal 11 "$1") <(cal 12 "$1")
```

制御構文使えよってくらいのベタ書きであるが・・・

せっかくなので、スクリーンショットで。

<a href="スクリーンショット-2014-04-29-21.36.42.png"><img src="スクリーンショット-2014-04-29-21.36.42-992x1024.png" alt="スクリーンショット 2014-04-29 21.36.42" width="625" height="645" class="aligncenter size-large wp-image-3068" /></a>

来年の正月が楽しみだ。


寝る。
