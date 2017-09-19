---
Keywords: プログラミング,Haskell,備忘録
Copyright: (C) 2017 Ryuichi Ueda
---

# Macでcabalが使えるようにしたのでメモ
<!--:ja--><span style="color:red">2013/11/25追記：今は（このときもそうだったかもしれんが）この方がよい．</span>
```bash
$ brew install haskell-platform
```

<span style="color:red">以上．</span>
<hr />

<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS" target="_blank">Haskellでopen usp Tukubai のコマンドを置き換えるプロジェクト</a>をちまちま進めています。

いつも使っているFreeBSDの環境では日本語の環境をセットアップしてあったのですが、自分のローカルのMacでもできないかと作業しましたのでメモです。

コンパイルしたいのは次のコードですが・・・

```hs
uedamac:~ ueda$ cat cat.hs
import qualified Data.ByteString.Lazy.Char8 as BS
import Codec.Binary.UTF8.String as CBUS
import System.Environment
import System.IO

main :: IO ()
main = do BS.getContents &amp;gt;&amp;gt;= putBSLines

--UTF-8の出力のお約束
putBSLines :: BS.ByteString -&amp;gt; IO ()
putBSLines = putStr . CBUS.decodeString . BS.unpack
```

素のghcだと次のように叱られます。これが通らないと、このプロジェクトは頓挫します。どうしましょう。<span style="color: #ff0000;">（ちなみに、コードを説明してと言われても、今のところ、無理。）</span>

```bash
uedamac:~ ueda$ ghc cat.hs

cat.hs:2:8:
 Could not find module `Codec.Binary.UTF8.String'
 Use -v to see a list of the files searched for.
```

というわけで、次のサイトを参考に、もうちょっと環境を整えました。
<ul>
	<li><a href="http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html" target="_blank"><span style="line-height: 1.714285714; font-size: 1rem;">http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html</span></a></li>
</ul>
```bash
### brew install ghc は終わっている。
$ brew install haskell-platform
==&amp;gt; Downloading http://lambda.haskell.org/platform/download/2012.4.0.0/haskell-p
######################################################################## 100.0%
==&amp;gt; ./configure --prefix=/usr/local/Cellar/haskell-platform/2012.4.0.0 --enable-
==&amp;gt; make install
### 注：すげー時間がかかる。
==&amp;gt; Caveats
Run `cabal update` to initialize the package list.

If you are replacing a previous version of haskell-platform, you may want
to unregister packages belonging to the old version. You can find broken
packages using:
 ghc-pkg check --simple-output
You can uninstall them using:
 ghc-pkg check --simple-output | xargs -n 1 ghc-pkg unregister --force
==&amp;gt; Summary
uedamac:~ ueda$ cabal update
### 注：またすげー時間がかかる。
### おや、夕食ができたようだ・・・。早く席につかないとシバかれる・・・
Note: there is a new version of cabal-install available.
To upgrade, run: cabal install cabal-install
### 注：おのれをインストールしろと・・・
uedamac:~ ueda$ cabal install cabal-install
（略）
Linking dist/build/cabal/cabal ...
Installing executable(s) in /Users/ueda/.cabal/bin
###注：やっとこさutf8-stringをインストール。背後から殺気を感じるのである。
### さっきから、殺気を感じるのである。
uedamac:~ ueda$ cabal install utf8-string
（略）
uedamac:~ ueda$ ghc cat.hs
```

<span style="color: #ff0000;">通りました。</span>

```bash
uedamac:~ ueda$ echo へのへのもへじ | ./cat
へのへのもへじ
```

実行もできた。よかったよかった。

しかし、コード配って人にこんな作業させるのもドSの所業なので、そのうちバイナリでどう配布するか考えないといけませんね・・・。

<iframe style="width: 120px; height: 240px;" src="http://rcm-jp.amazon.co.jp/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=ryuichiueda-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4797336021" height="240" width="320" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><!--:--><!--:en--><a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS" target="_blank">Haskellでopen usp Tukubai のコマンドを置き換えるプロジェクト</a>をちまちま進めています。

いつも使っているFreeBSDの環境では日本語の環境をセットアップしてあったのですが、自分のローカルのMacでもできないかと作業しましたのでメモです。

コンパイルしたいのは次のコードですが・・・

```hs
uedamac:~ ueda$ cat cat.hs
import qualified Data.ByteString.Lazy.Char8 as BS
import Codec.Binary.UTF8.String as CBUS
import System.Environment
import System.IO

main :: IO ()
main = do BS.getContents &amp;gt;&amp;gt;= putBSLines

--UTF-8の出力のお約束
putBSLines :: BS.ByteString -&amp;gt; IO ()
putBSLines = putStr . CBUS.decodeString . BS.unpack
```

素のghcだと次のように叱られます。これが通らないと、このプロジェクトは頓挫します。どうしましょう。<span style="color: #ff0000;">（ちなみに、コードを説明してと言われても、今のところ、無理。）</span>

```bash
uedamac:~ ueda$ ghc cat.hs

cat.hs:2:8:
 Could not find module `Codec.Binary.UTF8.String'
 Use -v to see a list of the files searched for.
```

というわけで、次のサイトを参考に、もうちょっと環境を整えました。
<ul>
	<li><a href="http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html" target="_blank"><span style="line-height: 1.714285714; font-size: 1rem;">http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html</span></a></li>
</ul>
```bash
### brew install ghc は終わっている。
$ brew install haskell-platform
==&amp;gt; Downloading http://lambda.haskell.org/platform/download/2012.4.0.0/haskell-p
######################################################################## 100.0%
==&amp;gt; ./configure --prefix=/usr/local/Cellar/haskell-platform/2012.4.0.0 --enable-
==&amp;gt; make install
### 注：すげー時間がかかる。
==&amp;gt; Caveats
Run `cabal update` to initialize the package list.

If you are replacing a previous version of haskell-platform, you may want
to unregister packages belonging to the old version. You can find broken
packages using:
 ghc-pkg check --simple-output
You can uninstall them using:
 ghc-pkg check --simple-output | xargs -n 1 ghc-pkg unregister --force
==&amp;gt; Summary
uedamac:~ ueda$ cabal update
### 注：またすげー時間がかかる。
### おや、夕食ができたようだ・・・。早く席につかないとシバかれる・・・
Note: there is a new version of cabal-install available.
To upgrade, run: cabal install cabal-install
### 注：おのれをインストールしろと・・・
uedamac:~ ueda$ cabal install cabal-install
（略）
Linking dist/build/cabal/cabal ...
Installing executable(s) in /Users/ueda/.cabal/bin
###注：やっとこさutf8-stringをインストール。背後から殺気を感じるのである。
### さっきから、殺気を感じるのである。
uedamac:~ ueda$ cabal install utf8-string
（略）
uedamac:~ ueda$ ghc cat.hs
```

<span style="color: #ff0000;">通りました。</span>

```bash
uedamac:~ ueda$ echo へのへのもへじ | ./cat
へのへのもへじ
```

実行もできた。よかったよかった。

しかし、コード配って人にこんな作業させるのもドSの所業なので、そのうちバイナリでどう配布するか考えないといけませんね・・・。

<iframe style="width: 120px; height: 240px;" src="http://rcm-jp.amazon.co.jp/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=ryuichiueda-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4797336021" height="240" width="320" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><!--:-->
