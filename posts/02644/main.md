---
Keywords: コマンド,Haskell,Haskell芸,シェル芸,シェル芸は関数型,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# シェル芸とHaskellの対応を考える
<!--:ja-->どうも上田です。眠気1000%でお送り致します。

かねてからシェル芸は関数型と主張しているので、主張の中身を一つ一つ具体的にしようとしております。眠いので。

まずは、ワンライナーでよく出てくるコマンドとHaskellの関数の対応表を作ってみようと思います。眠いので。

<!--:--><!--more--><!--:ja-->

<h2>データ</h2>

<ul>
 <li>n行のテキストデータ = Haskellのリスト（要素数n）に相当。
```bash
###以下の「list」が等価###
$ cat list
a
b
c
Prelude&gt; let list = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
Prelude&gt; list
[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
```
 </li>
 <li>n行m個のテキストデータ = m要素のリストがn個入っているリスト。
```bash
###以下の「mat」が等価###
uedambp:~ ueda$ cat mat
a b
c d
Prelude&gt; let mat = [[&quot;a&quot;,&quot;b&quot;],[&quot;c&quot;,&quot;d&quot;]]
Prelude&gt; mat
[[&quot;a&quot;,&quot;b&quot;],[&quot;c&quot;,&quot;d&quot;]]
```
 </li>
</ul>

<h2>操作や演算子の対応表</h2>

上のようにデータ構造の対応をつけたとき、
Haskellとシェルワンライナーで対応するものは次のようになる。

<table>
 <tr>
 <th>操作・演算子</th>
 <th>Haskell</th>
 <th>コマンド</th>
 </tr>
 <tr>
 <td>コマンド、関数の連結</td>
 <td>バインド演算子</td>
 <td>パイプ</td>
 </tr>
 <tr>
 <td>文を単語に分ける</td>
 <td>words</td>
 <td>tr ' ' '¥n'（Tukubaiのtarr）</td>
 </tr>
 <tr>
 <td>リストを文にまとめる</td>
 <td>unwords</td>
 <td>xargsあるいはtr '¥n' ' '（Tukubaiのyarr）</td>
 </tr>
 <tr>
 <td>charまで分解</td>
 <td>String型では既に分解されている</td>
 <td>gsed 's/./&¥n/g' , grep -o .</td>
 </tr>
 <tr>
 <td>先頭のいくつかを取得</td>
 <td>take &lt;個数&gt;</td>
 <td>head -n &lt;個数&gt;</td>
 </tr>
 <tr>
 <td>先頭のいくつかを除去</td>
 <td>drop &lt;個数&gt;</td>
 <td>tail -n +&lt;個数+1&gt;</td>
 </tr>
 <tr>
 <td>各要素の操作（計算）</td>
 <td>map &lt;ラムダ式&gt;</td>
 <td>awk '{計算処理}'</td>
 </tr>
 <tr>
 <td>各要素の操作</td>
 <td>map &lt;関数&gt;</td>
 <td>xargs &lt;コマンド&gt;</td>
 </tr>
 <tr>
 <td>フィルタリング</td>
 <td>filter &lt;関数&gt;</td>
 <td>grep &lt;正規表現&gt;, awk &lt;パターン&gt;</td>
 </tr>
 <tr>
 <td>リストの反転</td>
 <td>reverse</td>
 <td>tac, tail -r</td>
 </tr>
 <tr>
 <td>足し算</td>
 <td>foldr (+) 0</td>
 <td>awk '{a+=$1}END{print a}'（Tukubaiのsm2, sm5）</td>
 </tr>
 <tr>
 <td>ソート</td>
 <td>Data.List.sort</td>
 <td>sort</td>
 </tr>
 <tr>
 <td>ある行まで抽出</td>
 <td>takeWhile</td>
 <td>sed -n '1,/正規表現/p'等</td>
 </tr>
 <tr>
 <td>ある行以降を抽出</td>
 <td>dropWhile</td>
 <td>sed -n '/正規表現/,$p'等</td>
 </tr>
</table>

・・・くっ・・・眠い・・・続きは<del>webで</del>また今度。なんか気づいたら<a href="https://twitter.com/ryuichiueda" target="_blank">\@ryuichiueda</a>まで・・・。謝辞つきで拝借して表に追加します。

<h2>一応知見を書いておく</h2>

こうやって見てみると、Haskell風のコマンドがあるとスッキリしたワンライナーが書けそうだなというところ。


まだまだ夜は遠い。<!--:-->
