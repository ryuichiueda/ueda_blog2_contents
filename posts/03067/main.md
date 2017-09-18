---
Keywords: どうでもいい,シェルスクリプト,CLI,小ネタ,紙のカレンダーは地球に優しくない
Copyright: (C) 2017 Ryuichi Ueda
---

# 一年分のカレンダーを表示するシェルスクリプト
なんとなく作ってしまった・・・<br />
<br />
<span style="color:red">（追記：cal 2014でいいじゃないか！！！！知らなかったじゃないか！！！！ということでpaste芸＆ <( )芸をお楽しみください。）</span><br />
<br />
[bash]<br />
ueda\@remote:~$ cat caly <br />
#!/bin/bash<br />
<br />
paste &lt;(cal 1 &quot;$1&quot;) &lt;(cal 2 &quot;$1&quot;) &lt;(cal 3 &quot;$1&quot;)<br />
paste &lt;(cal 4 &quot;$1&quot;) &lt;(cal 5 &quot;$1&quot;) &lt;(cal 6 &quot;$1&quot;)<br />
paste &lt;(cal 7 &quot;$1&quot;) &lt;(cal 8 &quot;$1&quot;) &lt;(cal 9 &quot;$1&quot;)<br />
paste &lt;(cal 10 &quot;$1&quot;) &lt;(cal 11 &quot;$1&quot;) &lt;(cal 12 &quot;$1&quot;)<br />
[/bash]<br />
<br />
制御構文使えよってくらいのベタ書きであるが・・・<br />
<br />
せっかくなので、スクリーンショットで。<br />
<br />
<a href="スクリーンショット-2014-04-29-21.36.42.png"><img src="スクリーンショット-2014-04-29-21.36.42-992x1024.png" alt="スクリーンショット 2014-04-29 21.36.42" width="625" height="645" class="aligncenter size-large wp-image-3068" /></a><br />
<br />
来年の正月が楽しみだ。<br />
<br />
<br />
寝る。
