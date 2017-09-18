---
Keywords:コマンド,CLI,Haskell,Mac,Shelly,言語好きは面倒を問題としないのか
Copyright: (C) 2017 Ryuichi Ueda
---
# Haskellでコマンドを使えるShellyというものを試したのでメモ
始めてこの分野で論文を書くための調査メモです。はいはい、サーベイサーベイ・・・。<br />
<br />
<a target="_blank" href="https://hackage.haskell.org/package/shelly">https://hackage.haskell.org/package/shelly</a><br />
<br />
理屈は使ってから考える人間なので、とりあえず理屈抜きで使ってみたので手順を磔の刑に処します。<br />
<br />
<!--more--><br />
<br />
<h2>いんすとーる</h2><br />
<br />
試すのはMacの上です。Haskell入ってない場合は<a href="http://blog.ueda.asia/?page_id=2944" target="_blank">ここ</a>を参考に。<br />
<br />
[bash]<br />
uedambp:~ ueda$ cabal install shelly<br />
（中略）<br />
In-place registering shelly-1.5.5...<br />
Installing library in /Users/ueda/.cabal/lib/shelly-1.5.5/ghc-7.6.3<br />
Registering shelly-1.5.5...<br />
Installed shelly-1.5.5<br />
[/bash]<br />
<br />
<h2>とりあえずほぼ最小のものを書いてみる</h2><br />
<br />
シェルの<br />
[bash]<br />
$ echo aho<br />
[/bash]<br />
に相当するものを書いてみました。テキストをしかるべき型に変換しないと使えません。これは面倒だ。面倒というよりわけが分からなかったので<a target="_blank" href="http://stackoverflow.com/questions/21715781/shelly-convert-string-to-shelly-filepath">これ</a>を参考にしました。<br />
<br />
[hs]<br />
uedambp:~ ueda$ cat echo.hs <br />
import Shelly<br />
import Data.Text hiding (map)<br />
<br />
main = shelly $ do run echo args<br />
 where echo = (fromText . pack) &quot;echo&quot;<br />
 args = map pack [&quot;aho&quot;]<br />
[/hs]<br />
<br />
はいはい、実行実行。<br />
<br />
[bash]<br />
uedambp:~ ueda$ ghc echo.hs <br />
[1 of 1] Compiling Main ( echo.hs, echo.o )<br />
Linking echo ...<br />
uedambp:~ ueda$ ./echo <br />
aho<br />
[/bash]<br />
<br />
<br />
<h2>引数をコマンドラインから読み込めるようにする</h2><br />
<br />
[hs]<br />
uedambp:~ ueda$ cat echo-args.hs <br />
import System.Environment<br />
import Shelly<br />
import Data.Text hiding (map)<br />
<br />
main = main' =&lt;&lt; getArgs<br />
<br />
main' as = shelly $ do run echo args<br />
 where echo = (fromText . pack) &quot;echo&quot;<br />
 args = map pack as<br />
[/hs]<br />
<br />
<br />
はい実行。<br />
<br />
[bash]<br />
uedambp:~ ueda$ ./echo-args This is a pen.<br />
This is a pen.<br />
[/bash]<br />
<br />
<h2>感想</h2><br />
<br />
<span style="color:red;font-size:32px">面倒。</span><br />
<br />
<br />
<br />
以上。<br />
<br />
<h2>その後</h2><br />
<br />
<a href="https://twitter.com/ruicc" target="_blank">\@ruicc</a>さんの親切なインストラクションで次のように書けば香具師の型ヌキみたいな酷い目に合わないとのことです。（もっと簡単になるかもしれません。）<br />
<br />
プラグマ芸ですな・・・。<br />
<br />
[hs]<br />
uedambp:~ ueda$ cat echo-args.hs <br />
{-# LANGUAGE OverloadedStrings #-}<br />
{-# LANGUAGE ExtendedDefaultRules #-}<br />
{-# OPTIONS_GHC -fno-warn-type-defaults #-}<br />
<br />
import System.Environment<br />
import Shelly<br />
import qualified Data.Text as T<br />
default (T.Text)<br />
<br />
main = main' =&lt;&lt; getArgs<br />
<br />
main' as = shelly $ do run &quot;echo&quot; (map T.pack as)<br />
[/hs]<br />
<br />
関数はスッキリします。ヘッダが・・・。<br />
<br />
<br />
うーーーーーーーーん。
