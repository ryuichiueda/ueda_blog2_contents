---
Keywords:USP,執筆,番号付け,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# rstのファイルでリストに通し番号を入れる（久々にシェル芸）
USP MagazineのHaskellの記事を書いていて、必要になって久しぶりにシェル芸が炸裂したのでメモ。<br />
<br />
<a href="http://www.amazon.co.jp/gp/product/490480709X/ref=as_li_ss_tl?ie=UTF8&camp=247&creative=7399&creativeASIN=490480709X&linkCode=as2&tag=ryuichiueda-22">広告: USP MAGAZINE vol.15</a><img src="http://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=490480709X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /><br />
<br />
<br />
まず、私の原稿ですが、次のようなrstのファイルです。図や表の番号を自動で振る機能がSphinxでは確かややこしかったので、私はaaa、bbbとダミーの番号を入れて書いています。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
uedambp:USPMAG ueda$ cat 201410.rst | less<br />
（略）<br />
　前回は ``/etc/`` 下のファイルの一覧を作るところまで作りました。<br />
コードをリストbbbに示します。このコードに追加していきます。<br />
<br />
* リストbbb: q1_3_4.hs<br />
<br />
.. code-block:: hs<br />
 :linenos: <br />
（略）<br />
[/bash]<br />
<br />
こいつを一気に1,2...と番号に変換してみます。<br />
<br />
まず、「* リストxxx」という行を抽出。<br />
<br />
[bash]<br />
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst<br />
* リストbbb: q1_3_4.hs<br />
* リストbbc: q1_3_4の実行結果（headで省略しています）<br />
* リストccc: FileTools.hs<br />
* リストddd: ``FileTools.hs`` を使う ``q1_3_5.hs``<br />
* リストeee: 使うモジュールもろともコンパイルして実行<br />
* リストfff: モジュールをGHCiから利用<br />
* リストggg: cat関数を実装<br />
* リストeee: readFileの型<br />
* リストhhh: catchIOErrorの型<br />
* リストiii: packの型<br />
* リストjjj: bashのシバンを発見するq1_3_6.hs<br />
* リストkkk: q1_3_6の実行（と若干のシェル芸）<br />
[/bash]<br />
<br />
このgrepの結果を掃除して番号をふります。<br />
<br />
[bash]<br />
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst |<br />
 sed 's/\\* リスト//' | sed 's/:.*//' | awk '{print $1,NR}'<br />
bbb 1<br />
bbc 2<br />
ccc 3<br />
ddd 4<br />
eee 5<br />
fff 6<br />
ggg 7<br />
eee 8<br />
hhh 9<br />
iii 10<br />
jjj 11<br />
kkk 12<br />
[/bash]<br />
<br />
んで、sedのスクリプトに変換します。<br />
<br />
[bash]<br />
uedambp:USPMAG ueda$ grep '^\\* リスト' 201410.rst |<br />
 sed 's/\\* リスト//' | sed 's/:.*//' | awk '{print $1,NR}' |<br />
 sed 's;^;s/;' | tr ' ' '/' | sed 's;$;/g;' &gt; hoge.sed<br />
uedambp:USPMAG ueda$ cat hoge.sed <br />
s/bbb/1/g<br />
s/bbc/2/g<br />
s/ccc/3/g<br />
s/ddd/4/g<br />
s/eee/5/g<br />
s/fff/6/g<br />
s/ggg/7/g<br />
s/eee/8/g<br />
s/hhh/9/g<br />
s/iii/10/g<br />
s/jjj/11/g<br />
s/kkk/12/g<br />
[/bash]<br />
<br />
これを原稿に適用して出来上がり。<br />
<br />
[bash]<br />
uedambp:USPMAG ueda$ sed -f hoge.sed 201410.rst | less<br />
（略）<br />
　前回は ``/etc/`` 下のファイルの一覧を作るところまで作りました。<br />
コードをリスト1に示します。このコードに追加していきます。<br />
<br />
* リスト1: q1_3_4.hs<br />
<br />
.. code-block:: hs<br />
 :linenos: <br />
（略）<br />
[/bash]<br />
<br />
実は今までVimでちまちま変換してましたが、ちょっと考えれば方法はありますね。<br />
<br />
sh行あるのみ。<br />
<br />
<br />
・・・原稿書きに戻ります。
