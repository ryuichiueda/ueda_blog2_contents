---
Keywords: コマンド,GNU,grep
Copyright: (C) 2017 Ryuichi Ueda
---

# grep -o
小ネタです。コマンドのオプションで感動するのは、何年シェルを叩いていても起こることで、本日はGNU grepに-oというのがあると知りました。

manを読むと次のようにあります。

```bash
 -o, --only-matching
 Prints only the matching part of the lines.
```

試してみましょう。
```bash
uedamac:~ ueda$ cat hoge.html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
 &lt;body&gt;
 &lt;a href=&quot;http://aho.aho&quot; target=&quot;_blank&quot;&gt;あほ&lt;/a&gt;
 &lt;img src=&quot;aho.jpg&quot; alt=&quot;aho&quot;&gt;エロい画像&lt;/a&gt;
 &lt;/body&gt;
&lt;/html&gt;
uedamac:~ ueda$ cat hoge.html | grep -o 'href=&quot;[^&quot;]*&quot;'
href=&quot;http://aho.aho&quot;
uedamac:~ ueda$ cat hoge.html | grep -o -E '(src|href)=&quot;[^&quot;]*&quot;'
href=&quot;http://aho.aho&quot;
src=&quot;aho.jpg&quot;
uedamac:~ ueda$ curl http://www.yahoo.co.jp | nkf -wLux | grep -o '&lt;a href=[^&lt;]*' | head
 % Total % Received % Xferd Average Speed Time Time Time Current
 Dload Upload Total Spent Left Speed
100 24930 0 24930 0 0 235k 0 --:--:-- --:--:-- --:--:-- 316k
&lt;a href=&quot;r/mht&quot;&gt;
&lt;a href=s/192087&gt;募金受付「ふなっしーがチャリティーラン」 
&lt;a href=s/189191&gt;遺伝子検査キットで、かかりやすい病気を知る 
&lt;a href=s/192334&gt;期間限定、人気中古車を総額込み特別価格で 
&lt;a href=&quot;r/c1&quot;&gt;ショッピング 
&lt;a href=&quot;r/c2&quot;&gt;ヤフオク!
&lt;a href=&quot;r/c5&quot;&gt;旅行、ホテル予約 
&lt;a href=&quot;r/c12&quot;&gt;ニュース 
&lt;a href=&quot;r/c13&quot;&gt;天気 
&lt;a href=&quot;r/c14&quot;&gt;スポーツ 
```

便利。以上。

<h3>2013年11月19日追記</h3>

<a href="http://blog.bsdhack.org/" target="_blank">\@bsdhackさんがPOSIXで頑張ってます。</a>知り合いなので敢えてツッコミますが、そこまで頑張る必要あるのかと。
