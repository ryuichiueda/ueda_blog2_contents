---
Keywords: コマンド,CLI,Haskell,Mac,Shelly,言語好きは面倒を問題としないのか
Copyright: (C) 2017 Ryuichi Ueda
---

# Haskellでコマンドを使えるShellyというものを試したのでメモ
始めてこの分野で論文を書くための調査メモです。はいはい、サーベイサーベイ・・・。

<a target="_blank" href="https://hackage.haskell.org/package/shelly">https://hackage.haskell.org/package/shelly</a>

理屈は使ってから考える人間なので、とりあえず理屈抜きで使ってみたので手順を磔の刑に処します。

<!--more-->

<h2>いんすとーる</h2>

試すのはMacの上です。Haskell入ってない場合は<a href="/?page=02944" target="_blank">ここ</a>を参考に。

```bash
uedambp:~ ueda$ cabal install shelly
（中略）
In-place registering shelly-1.5.5...
Installing library in /Users/ueda/.cabal/lib/shelly-1.5.5/ghc-7.6.3
Registering shelly-1.5.5...
Installed shelly-1.5.5
```

<h2>とりあえずほぼ最小のものを書いてみる</h2>

シェルの
```bash
$ echo aho
```
に相当するものを書いてみました。テキストをしかるべき型に変換しないと使えません。これは面倒だ。面倒というよりわけが分からなかったので<a target="_blank" href="http://stackoverflow.com/questions/21715781/shelly-convert-string-to-shelly-filepath">これ</a>を参考にしました。

```hs
uedambp:~ ueda$ cat echo.hs 
import Shelly
import Data.Text hiding (map)

main = shelly $ do run echo args
 where echo = (fromText . pack) "echo"
 args = map pack ["aho"]
```

はいはい、実行実行。

```bash
uedambp:~ ueda$ ghc echo.hs 
[1 of 1] Compiling Main ( echo.hs, echo.o )
Linking echo ...
uedambp:~ ueda$ ./echo 
aho
```


<h2>引数をコマンドラインから読み込めるようにする</h2>

```hs
uedambp:~ ueda$ cat echo-args.hs 
import System.Environment
import Shelly
import Data.Text hiding (map)

main = main' =<< getArgs

main' as = shelly $ do run echo args
 where echo = (fromText . pack) "echo"
 args = map pack as
```


はい実行。

```bash
uedambp:~ ueda$ ./echo-args This is a pen.
This is a pen.
```

<h2>感想</h2>

<span style="color:red;font-size:32px">面倒。</span>



以上。

<h2>その後</h2>

<a href="https://twitter.com/ruicc" target="_blank">\@ruicc</a>さんの親切なインストラクションで次のように書けば香具師の型ヌキみたいな酷い目に合わないとのことです。（もっと簡単になるかもしれません。）

プラグマ芸ですな・・・。

```hs
uedambp:~ ueda$ cat echo-args.hs 
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE ExtendedDefaultRules #-}
{-# OPTIONS_GHC -fno-warn-type-defaults #-}

import System.Environment
import Shelly
import qualified Data.Text as T
default (T.Text)

main = main' =<< getArgs

main' as = shelly $ do run "echo" (map T.pack as)
```

関数はスッキリします。ヘッダが・・・。


うーーーーーーーーん。
