---
Keywords: プログラミング,/dev/random,Haskell,乱数,種無し乱数
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->/dev/randomを利用してHaskellでタネの要らない乱数を作って使う方法考えたがどうだろう？<!--:-->
<!--:ja-->今，ちょっとしたシミュレーションを行うために，コマンドをHaskellで作ってシェルスクリプトでつなぐということをやっています．シミュレーションでは乱数を多用するのですが，こういう作りだとコマンドをまたいだ乱数が必要です．ただ，コマンドごとに乱数を作るとき，コマンドで毎回タネを設定してしまうと，私の用途ではいい乱数になりません．これはHaskellに限らず，他の言語でも同じ事です．

<!--:--><!--more--><!--:ja-->

ライブラリ（System.Random）を使うと良い方法があるのかもしれませんが，たぶん一つのHaskellのコードの中で完結するようなものしか用意されていないと思ったので，プロセスをまたいで作れるものを無理矢理作りました．

MacやLinuxには/dev/randomというランダムなバイナリを吐き出すスペシャルファイルがあるので，これを使います．次のように延々とデタラメなバイナリを吐き出してくれるので，こいつを使うとプロセスをまたいだ乱数が作れます．

```bash
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 
0000000 106344 044756 023733 140260 177213 027315 062304 067526
0000020 052530 027013 035715 141650 152404 061057 000501 017266
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 
0000000 012674 145055 120133 105037 072036 101040 175300 140334
0000020 130150 025500 126756 103743 153304 076113 077026 030177
uedamac:ETC ueda$ cat /dev/random | od | head -n 2 
0000000 061522 052751 052150 000712 132344 173433 106103 141366
0000020 100136 104107 024231 007442 110045 104074 171547 155126
```

んで，Haskellのコード．getUniformRandsは3バイトずつ/dev/randomの内容を読み込んで0以上1未満の数に直し，無限にリストを吐き出し続けます．mainの方は使いたいだけ乱数をtakeすればいいのですが，このコードでは10個だけ読んで表示しています．


```hs
uedamac:ETC ueda$ cat random_gen.hs 
import System.Environment
import System.IO
import Data.Char
import qualified Data.ByteString.Lazy.Char8 as BS (drop,unpack,readFile,ByteString)

main :: IO () 
main = do rs &lt;- BS.readFile &quot;/dev/random&quot;
 putStr $ unlines $ map show (take 10 $ getUniformRands rs)

-- 0以上1未満の乱数列発生関数 --
getUniformRands :: BS.ByteString -&gt; [Double]
getUniformRands bs = d : getUniformRands (BS.drop 3 bs)
 where f (a:b:c:bs) = (ord a) * 256 * 256 + (ord b) * 256 + (ord c)
 n = f (BS.unpack bs)
 d = (fromIntegral n :: Double) / (256*256*256)
```

出力です．検証していませんが，よさげです．

```bash
uedamac:ETC ueda$ ./random_gen 
0.3938910961151123
0.5829044580459595
0.9411583542823792
6.583511829376221e-3
0.9301748275756836
0.1724839210510254
0.5428040027618408
0.7543691992759705
0.35005688667297363
9.597879648208618e-2
uedamac:ETC ueda$ ./random_gen 
0.7122036218643188
1.972973346710205e-3
0.8503671884536743
0.6848877668380737
0.6994166374206543
0.6399250626564026
0.7801088094711304
0.19904005527496338
4.157662391662598e-2
0.6634286642074585
```

シミュレーションでは，こいつを12個ずつ足して6を引き，正規分布に従う乱数を作って使用する予定．


論文に戻ります．<!--:-->
