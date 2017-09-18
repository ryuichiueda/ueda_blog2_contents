---
Keywords:プログラミング,/dev/random,Haskell,乱数,種無し乱数
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->/dev/randomを利用してHaskellでタネの要らない乱数を作って使う方法考えたがどうだろう？<!--:-->
<!--:ja-->今，ちょっとしたシミュレーションを行うために，コマンドをHaskellで作ってシェルスクリプトでつなぐということをやっています．シミュレーションでは乱数を多用するのですが，こういう作りだとコマンドをまたいだ乱数が必要です．ただ，コマンドごとに乱数を作るとき，コマンドで毎回タネを設定してしまうと，私の用途ではいい乱数になりません．これはHaskellに限らず，他の言語でも同じ事です．<br />
<br />
<!--:--><!--more--><!--:ja--><br />
<br />
ライブラリ（System.Random）を使うと良い方法があるのかもしれませんが，たぶん一つのHaskellのコードの中で完結するようなものしか用意されていないと思ったので，プロセスをまたいで作れるものを無理矢理作りました．<br />
<br />
MacやLinuxには/dev/randomというランダムなバイナリを吐き出すスペシャルファイルがあるので，これを使います．次のように延々とデタラメなバイナリを吐き出してくれるので，こいつを使うとプロセスをまたいだ乱数が作れます．<br />
<br />
[bash]<br />
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 <br />
0000000 106344 044756 023733 140260 177213 027315 062304 067526<br />
0000020 052530 027013 035715 141650 152404 061057 000501 017266<br />
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 <br />
0000000 012674 145055 120133 105037 072036 101040 175300 140334<br />
0000020 130150 025500 126756 103743 153304 076113 077026 030177<br />
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 <br />
0000000 061522 052751 052150 000712 132344 173433 106103 141366<br />
0000020 100136 104107 024231 007442 110045 104074 171547 155126<br />
[/bash]<br />
<br />
んで，Haskellのコード．getUniformRandsは3バイトずつ/dev/randomの内容を読み込んで0以上1未満の数に直し，無限にリストを吐き出し続けます．mainの方は使いたいだけ乱数をtakeすればいいのですが，このコードでは10個だけ読んで表示しています．<br />
<br />
<br />
[hs]<br />
uedamac:ETC ueda$ cat random_gen.hs <br />
import System.Environment<br />
import System.IO<br />
import Data.Char<br />
import qualified Data.ByteString.Lazy.Char8 as BS (drop,unpack,readFile,ByteString)<br />
<br />
main :: IO () <br />
main = do rs &lt;- BS.readFile &quot;/dev/random&quot;<br />
 putStr $ unlines $ map show (take 10 $ getUniformRands rs)<br />
<br />
-- 0以上1未満の乱数列発生関数 --<br />
getUniformRands :: BS.ByteString -&gt; [Double]<br />
getUniformRands bs = d : getUniformRands (BS.drop 3 bs)<br />
 where f (a:b:c:bs) = (ord a) * 256 * 256 + (ord b) * 256 + (ord c)<br />
 n = f (BS.unpack bs)<br />
 d = (fromIntegral n :: Double) / (256*256*256)<br />
[/hs]<br />
<br />
出力です．検証していませんが，よさげです．<br />
<br />
[bash]<br />
uedamac:ETC ueda$ ./random_gen <br />
0.3938910961151123<br />
0.5829044580459595<br />
0.9411583542823792<br />
6.583511829376221e-3<br />
0.9301748275756836<br />
0.1724839210510254<br />
0.5428040027618408<br />
0.7543691992759705<br />
0.35005688667297363<br />
9.597879648208618e-2<br />
uedamac:ETC ueda$ ./random_gen <br />
0.7122036218643188<br />
1.972973346710205e-3<br />
0.8503671884536743<br />
0.6848877668380737<br />
0.6994166374206543<br />
0.6399250626564026<br />
0.7801088094711304<br />
0.19904005527496338<br />
4.157662391662598e-2<br />
0.6634286642074585<br />
[/bash]<br />
<br />
シミュレーションでは，こいつを12個ずつ足して6を引き，正規分布に従う乱数を作って使用する予定．<br />
<br />
<br />
論文に戻ります．<!--:-->
