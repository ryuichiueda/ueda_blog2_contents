---
Keywords: クラス,プログラミング,C++,C/C++,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# シェル芸でC++のクラスの関係を調べる
今日発表のスライドを作っており、調査のため。面白いのでメモ。

Gitのリポジトリの
<a href="https://github.com/ryuichiueda/GlueLang/tree/master/SRC" target="_blank">https://github.com/ryuichiueda/GlueLang/tree/master/SRC</a>
に相当するディレクトリでシェル芸をしています。

<h1>基本クラスの抽出</h1>

```bash
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' |
 grep -v '{' | awk 'NF==2'
class Data
class Element
class Environment
class Feeder
```


<h1>各基本クラスから派生したクラスを調査</h1>

```bash
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' |
 grep -v '{' | awk 'NF==5{print $NF,$2}' | sort
Arg ArgExtCom
Arg ArgIntCom
Arg ArgProc
Arg ArgVariable
Arg ArrayVariable
Arg Literal
Data DataFile
Data DataJob
Data DataProc
Data DataStr
...
```

Tukubaiのコマンドを使うとこんなリストもできる。

```bash
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' | grep -v '{' | awk 'NF==5{print $NF,$2}' | sort | yarr num=1 | sed 's/ /:/'
Arg:ArgExtCom ArgIntCom ArgProc ArgVariable ArrayVariable Literal
Data:DataFile DataJob DataProc DataStr
Element:Arg DefCond DefFile DefProc DefStr Exe IfBlock Import Job Pipeline Script Where
Exe:ExeEachline ExeExtCom ExeIntCom ExeProc ExeString
```

ただし、複数のクラスを継承しているとやり方を変えないといかん。


パワポ書きに戻る。

