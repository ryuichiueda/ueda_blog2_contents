---
Keywords: 
Copyright: (C) 2019 Ryuichi Ueda
---

# 自分自身でシェル芸勉強会に喧嘩を売る

第39回

## Q1

感想: `sed`使いたい。

```
$ cat wrong.md | opy '[re.sub(r"\(([^()]+)\)\[([^\[\]]+)\]",r"[\1](\2)", F0)]' | opy '[re.sub(r"\[(http[^\[\]]+)\]\(([^()]+)\)", r"[\2](\1)", F0)]' | opy '[re.sub(r"\[([^\[\]]+).svg\]\(([^()]+)\)", r"[\2](\1)", F0)]'
```


## Q2

降参。無理。

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
```

## Q7

やる気が起きない。

## Q8



## やってみた感想

* コマンドを封じられると`sed`で改行を入れたりしてデータを端末で見た出力にそのままパイプをつないで・・・みたいなことができなくなるので辛い
* ワンライナーで`sort`使わずにソートするの辛い
* いちいちPythonのライブラリの使い方を調べるのが面倒

つまり辛い

