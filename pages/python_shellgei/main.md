---
Keywords: シェル芸, advent calendar, クソ文体, Python, Pythonワンライナー, ベストプラクティスとかバッドプラクティスとかうるせーんだよ
Copyright: (C) 2019 Ryuichi Ueda
---

# シェル芸？なにそれ？時代はPythonワンライナー

* この記事は[シェル芸Advent Calendar 2019](https://qiita.com/advent-calendar/2019/shellgei)の22日目の記事です。

こんにちは。匿名のPythonistaです。最近、シェル芸って流行ってるらしいんですが、今時コマンドなんてレガシーでバッドプラクティスですよね？世界を席巻するPython<span style="font-size:50%">ワンライナー</span>が優れていることをお見せするために、[このページの問題](https://b.ueda.tech/?post=20181222_shellgei_39)をPython<span style="font-size:50%">ワンライナー</span>で解いてみましょう。簡単ですね。Python<span style="font-size:50%">ワンライナー</span>なら。


## Q1

`re.sub`で置換していきます。簡単ですね。

```
$ cat wrong.md | python -c 'import sys;import re;a=[re.sub(r"\(([^()]+
)\)\[([^\[\]]+)\]",r"[\1](\2)", s) for s in sys.stdin];a=[re.sub(r"\[(
http[^\[\]]+)\]\(([^()]+)\)", r"[\2](\1)", e) for e in a];a=[re.sub(r"
\[([^\[\]]+.svg)\]\(([^()]+)\)", r"[\2](\1)", e) for e in a];print("".
join(a))'
# わたしはマークダウソちょっとできる

## 軍馬県高崎市

[軍魔県](https://ja.wikipedia.org/wiki/%E7%BE%A4%E9%A6%AC%E7%9C%8C)は、日本の県庁所在地の一つ。県庁所在地は[高崎市](https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B4%8E%E5%B8%82)

* [松井常松](https://ja.wikipedia.org/wiki/%E6%9D%BE%E4%BA%95%E5%B8%B8%E6%9D%BE)
* [高崎ハム](http://takasakiham.com/?transactionid=8e5164a76108c8411e7547d69e0dd0fd443f072a)


![たかさきしししょう](群馬県高崎市市章.svg)
```

## Q2

各回のデータをリストと辞書に整理してからプリントしていきます。簡単ですね。

```
$ cat attendee.md | python3 -c 'import sys;a=[print(e.rstrip() if "    " 
in e else "\n" + e.rstrip(), end="") for e in sys.stdin]' | python3 -c 'i
mport sys;a=sorted([e.rstrip() for e in sys.stdin]);a=[e.split() for e in
 a if len(e) > 3];a=[ [*e[:2],{ e[3*i+3]: e[3*i+4] for i in range(len(e)/
/3)} ] for e in a];[print(" ".join(e[:2]) + ("\n    * " "福岡: " + e[2][
"福岡:"] if "福岡:" in e[2] else "") + ("\n    * " "大阪: " + e[2]["大阪
:"] if "大阪:" in e[2] else "") + + ("\n    * " "東京: " + e[2]["東京:"]
 if "東京:" in e[2] else ""))for e in a]'
* 第34回シェル芸勉強会
    * 大阪: 16
    * 東京: 19
* 第35回シェル芸勉強会
    * 大阪: 10
    * 東京: 27
* 第36回シェル芸勉強会
    * 東京: 38
* 第37回シェル芸勉強会
    * 福岡: 8
    * 大阪: 10
    * 東京: 21
* 第38回シェル芸勉強会
    * 福岡: 3
    * 大阪: 8
    * 東京: 26
```

## Q3

`nkf --numchar-input`ってなんですか？`html.unescape`で簡単ですね。

```
$ cat index.html | python3 -c 'import sys,html;[print(html.unescape(e.
replace("<","\n<"))) for e in sys.stdin]' | python3 -c 'import sys;a=[
e for e in sys.stdin if "meta" in e];print(a[0])'
<meta content="世界中のあらゆる情報を検索するためのツールを提供しています。さまざまな検索機能を活用して、お探しの情報を見つけてください。" name="description">
```


## Q4

`bs4`（Beautiful Soup）で簡単ですね。

```
$ python3 -c 'import bs4;f=open("index.html");s=bs4.BeautifulSoup(f,
"html.parser");print(*s.select("script"))' | python3 -c 'import sys,
re;a=[re.sub("</*script[^<]*>","",e) for e in sys.stdin];print("\n".
join(a))' > index.js
$ python3 -c 'import bs4;f=open("index.html");s=bs4.BeautifulSoup(f,
"html.parser");print(*s.select("style"))' | python3 -c 'import sys,r
e;a=[re.sub("</*style[^<]*>","",e) for e in sys.stdin];print("\n".jo
in(a))' > index.css
```


## Q5

Beautiful Soup、便利ですね。

```
python3 -c 'import bs4;f=open("index.html");s=bs4.BeautifulSoup(f,"h
tml.parser");[e.decompose() for e in s.find_all(["style","script"])]
;print(s)' > index.no_cssjs.html
```


## Q6

Q3同様、`html.unescape`を使いましょう。簡単ですね。

```
$ cat index.js | python3 -c 'import sys,html;[print(html.unescape(e))
 for e in sys.stdin]' | python3 -c 'import sys,html;[print(html.unesc
ape(e).replace("\\x22","\"").replace("\\x3d","=").replace("\\\\","\\
")) for e in sys.stdin]'
・・・
rue,"msgs":{"cibl":"検索をクリア","dym":"もしかして:","lcky":"I\u0026#39;m Feeling Lucky","lml":"詳細","oskt":"入力ツール","psrc":"この検索キーワードは\u003Ca href=\"/history\"\u003Eウェブ履歴\u003C/a\u003Eから削除されました","psrl":"削除","sbit
・・・
```


## Q7

`numpy`で転置ができるので簡単ですね。

```
$ cat table.md | python3 -c 'import sys,numpy as np;a=[e.strip().split
("|")[1:-1] for e in sys.stdin if "---" not in e];a=np.array(a).T;a=["
|"+"|".join(e)+"|" for e in a];import re;a[0]=a[0]+"\n"+re.sub("[^|]",
"-",a[0]);print("\n".join(a))'
|回       |38回     |37回     |36回     |35回     |34回     |33回     |32回     |31回     |30回     |29回     |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|年月    |201811  |201809  |201807  |201804  |201803  |201801  |201712  |201710  |201708  |201706  |
|人数   |37     |39     |38     |37     |35     |40    |39    |37     |46     |55    |
```

## Q8

`while`と`clear`を使ってしまったけど、`replace`7連結（本当は8個だけど手抜き）で簡単ですね。

```
$ while true ; do cat yabatanien | python3 -c 'import sys;a=[e.replace("
7m","0m").replace("6m","7m").replace("5m","6m").replace("4m","5m").repla
ce("3m","4m").replace("2m","3m").replace("1m","2m") for e in sys.stdin];
print("".join(a))' yabatanien ; sleep 1 ; clear ; cat yabatanien ; sleep
 1 ; clear ; done
```

![](/posts/20181222_shellgei_39/yabatanien.gif)

## 決め台詞

いかがでしたか？

## やってみた感想

簡単なわけないだろ💢半日かかったぞ💢なんだよ匿名のPythonistaって。上にデカデカと「上田ブログ」って書いてあるじゃねーか。うんこだうんこ。寝る。すんませんでした。
