---
Keywords: 
Copyright: (C) 2019 Ryuichi Ueda
---

# 自分自身でシェル芸勉強会に喧嘩を売る

第39回

## Q1

感想: `sed`使いたい。

```
$ cat wrong.md | opy '[re.sub(r"\(([^()]+)\)\[([^\[\]]+)\]",r"[\1](\2)", F0)]' 
| opy '[re.sub(r"\[(http[^\[\]]+)\]\(([^()]+)\)", r"[\2](\1)", F0)]' 
| opy '[re.sub(r"\[([^\[\]]+).svg\]\(([^()]+)\)", r"[\2](\1)", F0)]'
# わたしはマークダウソちょっとできる

## 軍馬県高崎市

[軍魔県](https://ja.wikipedia.org/wiki/%E7%BE%A4%E9%A6%AC%E7%9C%8C)は、日本の県庁所在地の一つ。県庁所在地は[高崎市](https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B4%8E%E5%B8%82)

* [松井常松](https://ja.wikipedia.org/wiki/%E6%9D%BE%E4%BA%95%E5%B8%B8%E6%9D%BE)
* [高崎ハム](http://takasakiham.com/?transactionid=8e5164a76108c8411e7547d69e0dd0fd443f072a)


![たかさきしししょう](群馬県高崎市市章)
```


## Q2

死ぬかと思った。

```
$ cat attendee.md 
| opy 'r_("^\*"):{D[F2]={};k=F2};r_("^ "):{D[k][F6] = F7};E:{s=sorted(D.items())};E:{for e in s:print("* " + e[0] + ("\n    * 福岡: " + str(e[1]["福岡:"]) if "福岡:" in e[1] else "") + ("\n    * 大阪: " + str(e[1]["大阪:"]) if "大阪:" in e[1] else "") + ("\n    * 東京: " + str(e[1]["東京:"]) if "東京:" in e[1] else "") )}'
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

できた。`html.unescape`は使えそう。

```
$ cat index.html | opy '[re.sub("<","\n<",F0)]' 
| opy 'r_("<meta"):{print(F0);sys.exit(0)}' | opy '[html.unescape(F0)]'
<meta content="世界中のあらゆる情報を検索するためのツールを提供しています。さまざまな検索機能を活用して、お探しの情報を見つけてください。" name="description">
```


## Q4

Beautiful Soupが使えますね。Beautiful Soupって名前、なんとかならんかと昔から思ってますが・・・。

```
$ opy -m bs4 'B:{f=open("index.html");s = bs4.BeautifulSoup(f, "html.parser")};E:[*s.select("script")]' | opy '[re.sub("</*script[^<]*>","",F0)]' > index.js
$ opy -m bs4 'B:{f=open("index.html");s = bs4.BeautifulSoup(f, "html.parser")};E:[*s.select("style")]' | opy '[re.sub("</*style[^<]*>","",F0)]' > index.css
```

## Q5

なんかうまくいかない。降参


## Q6

こんな感じでしょうか？

```
$ cat index.js | opy '[html.unescape(F0)]' | opy '[html.unescape(F0)]' |
opy '[F0.replace("\\x22","\"").replace("\\x3d","=").replace("\\\\","\\")]'
・・・
rue,"msgs":{"cibl":"検索をクリア","dym":"もしかして:","lcky":"I\u0026#39;m Feeling Lucky","lml":"詳細","oskt":"入力ツール","psrc":"この検索キーワードは\u003Ca href=\"/history\"\u003Eウェブ履歴\u003C/a\u003Eから削除されました","psrl":"削除","sbit
・・・
```

## Q7

やる気が起きない。

## Q8

同上


## やってみた感想

（当たり前ですが）便利なライブラリがあると一瞬で終わることもあるけど、そうでない場合は途端にややこしくなる。



