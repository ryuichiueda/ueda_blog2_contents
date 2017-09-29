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
<!DOCTYPE html>
<html>
 <body>
 <a href="http://aho.aho" target="_blank">あほ</a>
 <img src="aho.jpg" alt="aho">エロい画像</a>
 </body>
</html>
uedamac:~ ueda$ cat hoge.html | grep -o 'href="[^"]*"'
href="http://aho.aho"
uedamac:~ ueda$ cat hoge.html | grep -o -E '(src|href)="[^"]*"'
href="http://aho.aho"
src="aho.jpg"
uedamac:~ ueda$ curl http://www.yahoo.co.jp | nkf -wLux | grep -o '<a href=[^<]*' | head
 % Total % Received % Xferd Average Speed Time Time Time Current
 Dload Upload Total Spent Left Speed
100 24930 0 24930 0 0 235k 0 --:--:-- --:--:-- --:--:-- 316k
<a href="r/mht">
<a href=s/192087>募金受付「ふなっしーがチャリティーラン」 
<a href=s/189191>遺伝子検査キットで、かかりやすい病気を知る 
<a href=s/192334>期間限定、人気中古車を総額込み特別価格で 
<a href="r/c1">ショッピング 
<a href="r/c2">ヤフオク!
<a href="r/c5">旅行、ホテル予約 
<a href="r/c12">ニュース 
<a href="r/c13">天気 
<a href="r/c14">スポーツ 
```

便利。以上。

<h3>2013年11月19日追記</h3>

<a href="http://blog.bsdhack.org/" target="_blank">\@bsdhackさんがPOSIXで頑張ってます。</a>知り合いなので敢えてツッコミますが、そこまで頑張る必要あるのかと。
