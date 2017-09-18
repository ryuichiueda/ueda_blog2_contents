---
Keywords:クラス,プログラミング,C++,C/C++,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---
# シェル芸でC++のクラスの関係を調べる
今日発表のスライドを作っており、調査のため。面白いのでメモ。<br />
<br />
Gitのリポジトリの<br />
<a href="https://github.com/ryuichiueda/GlueLang/tree/master/SRC" target="_blank">https://github.com/ryuichiueda/GlueLang/tree/master/SRC</a><br />
に相当するディレクトリでシェル芸をしています。<br />
<br />
<h1>基本クラスの抽出</h1><br />
<br />
[bash]<br />
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' |<br />
 grep -v '{' | awk 'NF==2'<br />
class Data<br />
class Element<br />
class Environment<br />
class Feeder<br />
[/bash]<br />
<br />
<br />
<h1>各基本クラスから派生したクラスを調査</h1><br />
<br />
[bash]<br />
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' |<br />
 grep -v '{' | awk 'NF==5{print $NF,$2}' | sort<br />
Arg ArgExtCom<br />
Arg ArgIntCom<br />
Arg ArgProc<br />
Arg ArgVariable<br />
Arg ArrayVariable<br />
Arg Literal<br />
Data DataFile<br />
Data DataJob<br />
Data DataProc<br />
Data DataStr<br />
...<br />
[/bash]<br />
<br />
Tukubaiのコマンドを使うとこんなリストもできる。<br />
<br />
[bash]<br />
uedambp:SRC ueda$ grep -h class *.h | grep -v ';' | grep -v '{' | awk 'NF==5{print $NF,$2}' | sort | yarr num=1 | sed 's/ /:/'<br />
Arg:ArgExtCom ArgIntCom ArgProc ArgVariable ArrayVariable Literal<br />
Data:DataFile DataJob DataProc DataStr<br />
Element:Arg DefCond DefFile DefProc DefStr Exe IfBlock Import Job Pipeline Script Where<br />
Exe:ExeEachline ExeExtCom ExeIntCom ExeProc ExeString<br />
[/bash]<br />
<br />
ただし、複数のクラスを継承しているとやり方を変えないといかん。<br />
<br />
<br />
パワポ書きに戻る。<br />

