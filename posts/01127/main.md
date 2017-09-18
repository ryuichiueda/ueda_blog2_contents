---
Keywords:コマンド,GNU,grep
Copyright: (C) 2017 Ryuichi Ueda
---
# grep -o
小ネタです。コマンドのオプションで感動するのは、何年シェルを叩いていても起こることで、本日はGNU grepに-oというのがあると知りました。<br />
<br />
manを読むと次のようにあります。<br />
<br />
[bash]<br />
 -o, --only-matching<br />
 Prints only the matching part of the lines.<br />
[/bash]<br />
<br />
試してみましょう。<br />
[bash]<br />
uedamac:~ ueda$ cat hoge.html<br />
&lt;!DOCTYPE html&gt;<br />
&lt;html&gt;<br />
 &lt;body&gt;<br />
 &lt;a href=&quot;http://aho.aho&quot; target=&quot;_blank&quot;&gt;あほ&lt;/a&gt;<br />
 &lt;img src=&quot;aho.jpg&quot; alt=&quot;aho&quot;&gt;エロい画像&lt;/a&gt;<br />
 &lt;/body&gt;<br />
&lt;/html&gt;<br />
uedamac:~ ueda$ cat hoge.html | grep -o 'href=&quot;[^&quot;]*&quot;'<br />
href=&quot;http://aho.aho&quot;<br />
uedamac:~ ueda$ cat hoge.html | grep -o -E '(src|href)=&quot;[^&quot;]*&quot;'<br />
href=&quot;http://aho.aho&quot;<br />
src=&quot;aho.jpg&quot;<br />
uedamac:~ ueda$ curl http://www.yahoo.co.jp | nkf -wLux | grep -o '&lt;a href=[^&lt;]*' | head<br />
 % Total % Received % Xferd Average Speed Time Time Time Current<br />
 Dload Upload Total Spent Left Speed<br />
100 24930 0 24930 0 0 235k 0 --:--:-- --:--:-- --:--:-- 316k<br />
&lt;a href=&quot;r/mht&quot;&gt;<br />
&lt;a href=s/192087&gt;募金受付「ふなっしーがチャリティーラン」 <br />
&lt;a href=s/189191&gt;遺伝子検査キットで、かかりやすい病気を知る <br />
&lt;a href=s/192334&gt;期間限定、人気中古車を総額込み特別価格で <br />
&lt;a href=&quot;r/c1&quot;&gt;ショッピング <br />
&lt;a href=&quot;r/c2&quot;&gt;ヤフオク!<br />
&lt;a href=&quot;r/c5&quot;&gt;旅行、ホテル予約 <br />
&lt;a href=&quot;r/c12&quot;&gt;ニュース <br />
&lt;a href=&quot;r/c13&quot;&gt;天気 <br />
&lt;a href=&quot;r/c14&quot;&gt;スポーツ <br />
[/bash]<br />
<br />
便利。以上。<br />
<br />
<h3>2013年11月19日追記</h3><br />
<br />
<a href="http://blog.bsdhack.org/" target="_blank">\@bsdhackさんがPOSIXで頑張ってます。</a>知り合いなので敢えてツッコミますが、そこまで頑張る必要あるのかと。
