---
Keywords:コマンド,Haskell,Haskell芸,シェル芸,シェル芸は関数型,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---
# シェル芸とHaskellの対応を考える
<!--:ja-->どうも上田です。眠気1000%でお送り致します。<br />
<br />
かねてからシェル芸は関数型と主張しているので、主張の中身を一つ一つ具体的にしようとしております。眠いので。<br />
<br />
まずは、ワンライナーでよく出てくるコマンドとHaskellの関数の対応表を作ってみようと思います。眠いので。<br />
<br />
<!--:--><!--more--><!--:ja--><br />
<br />
<h2>データ</h2><br />
<br />
<ul><br />
 <li>n行のテキストデータ = Haskellのリスト（要素数n）に相当。<br />
[bash]<br />
###以下の「list」が等価###<br />
$ cat list<br />
a<br />
b<br />
c<br />
Prelude&gt; let list = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]<br />
Prelude&gt; list<br />
[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]<br />
[/bash]<br />
 </li><br />
 <li>n行m個のテキストデータ = m要素のリストがn個入っているリスト。<br />
[bash]<br />
###以下の「mat」が等価###<br />
uedambp:~ ueda$ cat mat<br />
a b<br />
c d<br />
Prelude&gt; let mat = [[&quot;a&quot;,&quot;b&quot;],[&quot;c&quot;,&quot;d&quot;]]<br />
Prelude&gt; mat<br />
[[&quot;a&quot;,&quot;b&quot;],[&quot;c&quot;,&quot;d&quot;]]<br />
[/bash]<br />
 </li><br />
</ul><br />
<br />
<h2>操作や演算子の対応表</h2><br />
<br />
上のようにデータ構造の対応をつけたとき、<br />
Haskellとシェルワンライナーで対応するものは次のようになる。<br />
<br />
<table><br />
 <tr><br />
 <th>操作・演算子</th><br />
 <th>Haskell</th><br />
 <th>コマンド</th><br />
 </tr><br />
 <tr><br />
 <td>コマンド、関数の連結</td><br />
 <td>バインド演算子</td><br />
 <td>パイプ</td><br />
 </tr><br />
 <tr><br />
 <td>文を単語に分ける</td><br />
 <td>words</td><br />
 <td>tr ' ' '¥n'（Tukubaiのtarr）</td><br />
 </tr><br />
 <tr><br />
 <td>リストを文にまとめる</td><br />
 <td>unwords</td><br />
 <td>xargsあるいはtr '¥n' ' '（Tukubaiのyarr）</td><br />
 </tr><br />
 <tr><br />
 <td>charまで分解</td><br />
 <td>String型では既に分解されている</td><br />
 <td>gsed 's/./&¥n/g' , grep -o .</td><br />
 </tr><br />
 <tr><br />
 <td>先頭のいくつかを取得</td><br />
 <td>take &lt;個数&gt;</td><br />
 <td>head -n &lt;個数&gt;</td><br />
 </tr><br />
 <tr><br />
 <td>先頭のいくつかを除去</td><br />
 <td>drop &lt;個数&gt;</td><br />
 <td>tail -n +&lt;個数+1&gt;</td><br />
 </tr><br />
 <tr><br />
 <td>各要素の操作（計算）</td><br />
 <td>map &lt;ラムダ式&gt;</td><br />
 <td>awk '{計算処理}'</td><br />
 </tr><br />
 <tr><br />
 <td>各要素の操作</td><br />
 <td>map &lt;関数&gt;</td><br />
 <td>xargs &lt;コマンド&gt;</td><br />
 </tr><br />
 <tr><br />
 <td>フィルタリング</td><br />
 <td>filter &lt;関数&gt;</td><br />
 <td>grep &lt;正規表現&gt;, awk &lt;パターン&gt;</td><br />
 </tr><br />
 <tr><br />
 <td>リストの反転</td><br />
 <td>reverse</td><br />
 <td>tac, tail -r</td><br />
 </tr><br />
 <tr><br />
 <td>足し算</td><br />
 <td>foldr (+) 0</td><br />
 <td>awk '{a+=$1}END{print a}'（Tukubaiのsm2, sm5）</td><br />
 </tr><br />
 <tr><br />
 <td>ソート</td><br />
 <td>Data.List.sort</td><br />
 <td>sort</td><br />
 </tr><br />
 <tr><br />
 <td>ある行まで抽出</td><br />
 <td>takeWhile</td><br />
 <td>sed -n '1,/正規表現/p'等</td><br />
 </tr><br />
 <tr><br />
 <td>ある行以降を抽出</td><br />
 <td>dropWhile</td><br />
 <td>sed -n '/正規表現/,$p'等</td><br />
 </tr><br />
</table><br />
<br />
・・・くっ・・・眠い・・・続きは<del>webで</del>また今度。なんか気づいたら<a href="https://twitter.com/ryuichiueda" target="_blank">\@ryuichiueda</a>まで・・・。謝辞つきで拝借して表に追加します。<br />
<br />
<h2>一応知見を書いておく</h2><br />
<br />
こうやって見てみると、Haskell風のコマンドがあるとスッキリしたワンライナーが書けそうだなというところ。<br />
<br />
<br />
まだまだ夜は遠い。<!--:-->
