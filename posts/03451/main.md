---
Keywords: USP,執筆,番号付け,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# rstのファイルでリストに通し番号を入れる（久々にシェル芸）
USP MagazineのHaskellの記事を書いていて、必要になって久しぶりにシェル芸が炸裂したのでメモ。

<a href="http://www.amazon.co.jp/gp/product/490480709X/ref=as_li_ss_tl?ie=UTF8&camp=247&creative=7399&creativeASIN=490480709X&linkCode=as2&tag=ryuichiueda-22">広告: USP MAGAZINE vol.15</a><img src="http://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=490480709X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />


まず、私の原稿ですが、次のようなrstのファイルです。図や表の番号を自動で振る機能がSphinxでは確かややこしかったので、私はaaa、bbbとダミーの番号を入れて書いています。

<!--more-->

```bash
uedambp:USPMAG ueda$ cat 201410.rst | less
（略）
　前回は ``/etc/`` 下のファイルの一覧を作るところまで作りました。
コードをリストbbbに示します。このコードに追加していきます。

* リストbbb: q1_3_4.hs

.. code-block:: hs
 :linenos: 
（略）
```

こいつを一気に1,2...と番号に変換してみます。

まず、「* リストxxx」という行を抽出。

```bash
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst
* リストbbb: q1_3_4.hs
* リストbbc: q1_3_4の実行結果（headで省略しています）
* リストccc: FileTools.hs
* リストddd: ``FileTools.hs`` を使う ``q1_3_5.hs``
* リストeee: 使うモジュールもろともコンパイルして実行
* リストfff: モジュールをGHCiから利用
* リストggg: cat関数を実装
* リストeee: readFileの型
* リストhhh: catchIOErrorの型
* リストiii: packの型
* リストjjj: bashのシバンを発見するq1_3_6.hs
* リストkkk: q1_3_6の実行（と若干のシェル芸）
```

このgrepの結果を掃除して番号をふります。

```bash
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst |
 sed 's/\\* リスト//' | sed 's/:.*//' | awk '{print $1,NR}'
bbb 1
bbc 2
ccc 3
ddd 4
eee 5
fff 6
ggg 7
eee 8
hhh 9
iii 10
jjj 11
kkk 12
```

んで、sedのスクリプトに変換します。

```bash
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst |
 sed 's/\\* リスト//' | sed 's/:.*//' | awk '{print $1,NR}' |
 sed 's;^;s/;' | tr ' ' '/' | sed 's;$;/g;' > hoge.sed
uedambp:USPMAG ueda$ cat hoge.sed 
s/bbb/1/g
s/bbc/2/g
s/ccc/3/g
s/ddd/4/g
s/eee/5/g
s/fff/6/g
s/ggg/7/g
s/eee/8/g
s/hhh/9/g
s/iii/10/g
s/jjj/11/g
s/kkk/12/g
```

これを原稿に適用して出来上がり。

```bash
uedambp:USPMAG ueda$ sed -f hoge.sed 201410.rst | less
（略）
　前回は ``/etc/`` 下のファイルの一覧を作るところまで作りました。
コードをリスト1に示します。このコードに追加していきます。

* リスト1: q1_3_4.hs

.. code-block:: hs
 :linenos: 
（略）
```

実は今までVimでちまちま変換してましたが、ちょっと考えれば方法はありますね。

sh行あるのみ。


・・・原稿書きに戻ります。
