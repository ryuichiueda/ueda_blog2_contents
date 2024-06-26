---
Keywords: 
Copyright: (C) 2019 Ryuichi Ueda
---

# コマンドに感謝するためにPythonでシェル芸勉強会の問題に挑戦

[第39回のシェル芸勉強会](https://b.ueda.tech/?post=20181222_shellgei_39)の問題を、Pythonのワンライナーで解いてみました。ただ、生Pythonワンライナーだと死ぬので、`opy`を使っています。

## Q1


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

感想: `sed`に対する感謝が高まりました。

## Q2

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

感想: `sort`に対する感謝が高まりました。

## Q3


```
$ cat index.html | opy '[re.sub("<","\n<",F0)]' 
| opy 'r_("<meta"):{print(F0);sys.exit(0)}' | opy '[html.unescape(F0)]'
<meta content="世界中のあらゆる情報を検索するためのツールを提供しています。さまざまな検索機能を活用して、お探しの情報を見つけてください。" name="description">
```

あれ、これは`html.unescape`で簡単に終わった・・・。

## Q4


```
$ opy -m bs4 'B:{f=open("index.html");s = bs4.BeautifulSoup(f, "html.parser")};E:[*s.select("script")]' | opy '[re.sub("</*script[^<]*>","",F0)]' > index.js
$ opy -m bs4 'B:{f=open("index.html");s = bs4.BeautifulSoup(f, "html.parser")};E:[*s.select("style")]' | opy '[re.sub("</*style[^<]*>","",F0)]' > index.css
```

これもBeautiful Soup使うとすんなり終わる（簡単に入力できたとは言っていない）。Beautiful Soupって名前なんなんだと昔から思ってますが・・・。

## Q5


```
cat index.html 
| opy -m bs4 'B:{f=open("index.html");s = bs4.BeautifulSoup(f, "html.parser")};E:{[e.decompose() for e in s.find_all(["style","script"])];print(s)}'
```

Beautiful Soup、便利じゃないか。

## Q6

```
$ cat index.js | opy '[html.unescape(F0)]' | opy '[html.unescape(F0)]' |
opy '[F0.replace("\\x22","\"").replace("\\x3d","=").replace("\\\\","\\")]'
・・・
rue,"msgs":{"cibl":"検索をクリア","dym":"もしかして:","lcky":"I\u0026#39;m Feeling Lucky","lml":"詳細","oskt":"入力ツール","psrc":"この検索キーワードは\u003Ca href=\"/history\"\u003Eウェブ履歴\u003C/a\u003Eから削除されました","psrl":"削除","sbit
・・・
```

replace並べるのめんどくさい。`sed`万歳。

## Q7

```
$ cat table.md 
| opy -i '|' -m 'numpy as np' 'B:{a=np.array([])};r_("回"):{a = np.append(a,F[2:5],axis=0)};E:{[print("|" + "|".join(e) + "|") for e in a.reshape([-1,3]).T]}' 
| opy '[F0];NR==1:[re.sub("[^|]","-",F0)]'
|回       |38回     |37回     |36回     |35回     |34回     |33回     |32回     |31回     |30回     |29回     |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|年月    |201811|201809|201807|201804|201803|201801|201712|201710|201708|201706|
|人数   |37|39|38|37|35|40|39|37|46|55|
```

## Q8

さすがに`clear`と`while`は`opy`で代用できないので・・・

```
$ while true ; do opy '[F0.replace("7m","0m").replace("6m","7m").replace("5m","6m").replace("4m","5m").replace("3m","4m").replace("2m","3m").replace("1m","2m")]' yabatanien ; sleep 1 ; clear ; cat yabatanien ; sleep 1 ; clear ; done
```


## やってみた感想

（当たり前ですが）便利なモジュールがあると一瞬で終わることもあるけど、そうでない場合は途端にややこしくなるので、適度にコマンドを使えた方がいいですね。構造化されたデータに対してちゃんとプログラム書くときは、適切なモジュールを使ってパースしてからのほうがよいです。ただ、巨大データをPythonで取り込む場合は当然ながらメモリを食うので、シェル芸で前処理できると便利です。


## 結論

シェル芸できないとあかん。でもシェル芸だけでもあかん。



