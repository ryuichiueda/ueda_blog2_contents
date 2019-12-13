---
Keywords: 
Copyright: (C) 2019 Ryuichi Ueda
---

# サンプリングシェル芸

* この記事は[シェル芸Advent Calendar 2019](https://qiita.com/advent-calendar/2019/shellgei)の14日目の記事です。

　[難読化シェル芸](https://raintrees.net/news/95)の手法の一つに、思わぬところから文字を拾って（サンプリングして）コマンドの文字列にするというものがあります。[音楽のサンプリング](https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0)みたいなものです。文字を拾う方法にもいろいろあるので、まとめてみました。


## その前に、何に役立つか

　立ちません。

## オープニング曲

　これをループでかけながらシェル芸やると雰囲気出ます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/-Y_JRR3udEo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## コマンドのエラーやヘルプからのサンプリング

　まず最初に紹介するのは、コマンドの出力する文字列からのサンプリングです。例えば次の例は、難読化シェル芸の名付け親のkanataさんの示した方法をアレンジしたもので、「`ls --help`の出力から`date`コマンドを実行する」というものです。

```
### Macのlsで試しました ###
$ __=$(ls --- 2>&1) ; ${__:54:1}${__:51:1}${__:69:1}${__:55:1}
2019年 12月12日 木曜日 12時30分24秒 JST
```

　`ls ---`の出力は次のようなエラーメッセージです。このように、Macの`ls`でオプションのエラーを起こすと、使えるオプションの一覧が表示されますが、その中にd, a, t, eが含まれています。これを上のように変数（`__`）に代入し切り出すと`date`になります。


```
### Mac ###
$ ls ---
ls: illegal option -- -
usage: ls [-@ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1%] [file ...]
```

　Ubuntuの`ls`の場合は次のように`date`が実行できます。またUbuntuの場合、bashであらかじめ`ls`に`l`というエイリアスが設定されているので`l`で十分です。


```
### Ubuntu 18.04 ###
$ eval $(grep -oP "'....'(?=;)" <(l --help))
2019年 12月 12日 木曜日 12:25:11 JST
### Ubuntu 19.10 ###
$ $(grep -oP "[^ ']*(?=\()" <(l --help))
Thu 12 Dec 2019 12:22:05 PM JST
```

これの種明かしですが、Ubuntuの`ls`の場合、マニュアル中に`date`という単語がそのまま含まれているので、そこを切り出して実行しています。**簡単ですね。**

```
### Ubuntu 18.04 ###
$ ls --help | grep date
                               FORMAT is interpreted like in 'date'; if FORMAT
### Ubuntu 19.10 ###
$ ls --help | grep date
      --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
```

　同じテクニックで、`date`のmanから`time`コマンドを実行することもできます。

```
### Ubuntu 18.04 ###
$ $(man date | grep -m 1 -o ' ....$') sleep 1
0.00user 0.00system 0:01.00elapsed 0%CPU (0avgtext+0avgdata 2088maxresident)k
0inputs+0outputs (0major+72minor)pagefaults 0swaps
```

## ファイル名からのサンプリング 

　次に、ファイル名からサンプリングしてみます。

```
### Ubuntu 18.04 ###
__=(/*/*u?????);${__[-1]:13}
2019年 12月 12日 木曜日 17:48:03 JST
```

この例は、bashのファイルグロブでuがついて後ろに5文字で終わるファイル名を表示して、`○○update`というファイルをひっかけて`date`をサンプリングしています。

```
### Ubuntu 18.04 ###
$ echo /*/*u?????
/bin/bunzip2 /bin/busybox /bin/ntfstruncate ... /sbin/unix_update
```

## 乱数からのサンプリング

　乱数からも`date`をとってみましょう。`/dev/urandom`を使うとアルファベットをランダムに出力できます。

```
### Ubuntu ###
$ tr -dc a-z < /dev/urandom
yjqqtpypyogcuihascrrjshudcnhpjycqkjphxdyyzqxrnflrfztnvddwnkbeilvnigaflndpuohvauqquycttnjzdrljhcoqbvnfdzdvbkkjfqlmdyjnjlckvvodxkrfsb ...
```

ここから`date`を見つけて実行すればいいのですが、たぶん`date`が揃うのはかなり後のことになりそうです。


　ですので、`date`とバレないようにd, a, t, eを含む単語で`a-z`を置き換えます。（なんでバレたらダメなんだろうという疑問はさておき）

```
### Ubuntu ###
$ tr -dc andante < /dev/urandom | fold -b4 | head
entn
datt
natd
tada
nnda
eddn
tnda
aaat
dtna
dett
```

そしてこれを無造作にshに突っ込むと、わりと短時間で`date`が実行されます。**変なコマンドが起動してシステムを壊したりファイルを消したりするかもしれませんので注意が必要です。**


```
### Ubuntu ###
$ tr -dc andante < /dev/urandom | fold -b4 | sh 2>/dev/null | grep : 
2019年 12月 12日 木曜日 21:05:02 JST
2019年 12月 12日 木曜日 21:05:02 JST
・・・
```

## Pythonのunicodedataからのサンプリング

　闇豚さん（[@yami_buta](https://twitter.com/yami_buta)）のシェル芸で知ったんですが、Pythonにはunicodedataというパッケージがあり、unicodeの情報を見ることができます。

```
$ python3 -c 'import unicodedata;print(unicodedata.name("൹"))'
MALAYALAM DATE MARK
```

上の出力のように、説明文に「DATE」とある文字がたくさんあるので、これをサンプリングすると`date`が実行できます。

```
$ $(python3 -c 'import unicodedata;print(unicodedata.name("൹").split()[1].lower())')
2019年 12月12日 木曜日 21時20分00秒 JST
### 超絶便利Pythonラッパーコマンドopy（呼び方注意）を使う ###
$ $( echo ൹ | opy '[unicodedata.name(F1).split()[1].lower()]' )
2019年 12月12日 木曜日 21時21分09秒 JST
```

余談ですが、上で使った「超絶便利Pythonラッパーコマンドopy（呼び方注意）」は、https://github.com/ryuichiueda/opy にあるのでインストールしてStarをつけましょう。


## ウェブからのサンプリング

　最後に、インターーネッツからのスムーズな`date`の実行をやってみます。題材のウェブサイトは、終わってしまうと長女から聞かされてショックを受けている「[宮川賢のデートの時間でそ？！](https://www.tbsradio.jp/deso/)」のトップページとします。ただ、あんまりみんなでわーっとやると先方から叱られますので、試す場合は別のページを探してください。

```
$ curl https://www.tbsradio.jp/deso/ 2>/dev/null | grep -oP 'new [^(0]{4}' 
| sed 's/.*/\L&/;s/.* //e'
2019年 12月 13日 金曜日 09:57:41 JST
```

　これは特にこのページだからできることではなく、JavaScriptの`new Date()`が存在しているページならどれでも可能です。（切り取り方はアレンジする必要があります。）


```
### ページのHTMLのここから持ってきた ###
・・・
        <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
・・・
```

　ていうか長女よ、お前小学生だろ。なんでこの番組（ほぼ全編下ネタ）のリスナーなんだよ。

以上。


## 宣伝

　[SoftwareDesign](https://amzn.to/2RLWFag)にて連載3年目に入った「シェル芸人の挑戦状」では、もう少し実用的なシェル芸を勉強できます。ぜひぜひぜひぜひ。


　この記事と同じくらいの変態シェル芸を堪能したい場合は、12/28の[シェル芸勉強会](https://usptomo.doorkeeper.jp/events/100915)にぜひご参加ください。特に何もしてなくても叱られないので、初心者の方もどうぞー。みなさん親切です。


今度こそ以上。
