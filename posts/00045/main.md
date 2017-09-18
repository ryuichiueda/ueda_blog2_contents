---
Keywords:プログラミング,Haskell,備忘録
Copyright: (C) 2017 Ryuichi Ueda
---

# Macでcabalが使えるようにしたのでメモ
<!--:ja--><span style="color:red">2013/11/25追記：今は（このときもそうだったかもしれんが）この方がよい．</span><br />
[bash]<br />
$ brew install haskell-platform<br />
[/bash]<br />
<br />
<span style="color:red">以上．</span><br />
<hr /><br />
<br />
<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS" target="_blank">Haskellでopen usp Tukubai のコマンドを置き換えるプロジェクト</a>をちまちま進めています。<br />
<br />
いつも使っているFreeBSDの環境では日本語の環境をセットアップしてあったのですが、自分のローカルのMacでもできないかと作業しましたのでメモです。<br />
<br />
コンパイルしたいのは次のコードですが・・・<br />
<br />
[hs]<br />
uedamac:~ ueda$ cat cat.hs<br />
import qualified Data.ByteString.Lazy.Char8 as BS<br />
import Codec.Binary.UTF8.String as CBUS<br />
import System.Environment<br />
import System.IO<br />
<br />
main :: IO ()<br />
main = do BS.getContents &amp;gt;&amp;gt;= putBSLines<br />
<br />
--UTF-8の出力のお約束<br />
putBSLines :: BS.ByteString -&amp;gt; IO ()<br />
putBSLines = putStr . CBUS.decodeString . BS.unpack<br />
[/hs]<br />
<br />
素のghcだと次のように叱られます。これが通らないと、このプロジェクトは頓挫します。どうしましょう。<span style="color: #ff0000;">（ちなみに、コードを説明してと言われても、今のところ、無理。）</span><br />
<br />
[bash]<br />
uedamac:~ ueda$ ghc cat.hs<br />
<br />
cat.hs:2:8:<br />
 Could not find module `Codec.Binary.UTF8.String'<br />
 Use -v to see a list of the files searched for.<br />
[/bash]<br />
<br />
というわけで、次のサイトを参考に、もうちょっと環境を整えました。<br />
<ul><br />
	<li><a href="http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html" target="_blank"><span style="line-height: 1.714285714; font-size: 1rem;">http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html</span></a></li><br />
</ul><br />
[bash]<br />
### brew install ghc は終わっている。<br />
$ brew install haskell-platform<br />
==&amp;gt; Downloading http://lambda.haskell.org/platform/download/2012.4.0.0/haskell-p<br />
######################################################################## 100.0%<br />
==&amp;gt; ./configure --prefix=/usr/local/Cellar/haskell-platform/2012.4.0.0 --enable-<br />
==&amp;gt; make install<br />
### 注：すげー時間がかかる。<br />
==&amp;gt; Caveats<br />
Run `cabal update` to initialize the package list.<br />
<br />
If you are replacing a previous version of haskell-platform, you may want<br />
to unregister packages belonging to the old version. You can find broken<br />
packages using:<br />
 ghc-pkg check --simple-output<br />
You can uninstall them using:<br />
 ghc-pkg check --simple-output | xargs -n 1 ghc-pkg unregister --force<br />
==&amp;gt; Summary<br />
uedamac:~ ueda$ cabal update<br />
### 注：またすげー時間がかかる。<br />
### おや、夕食ができたようだ・・・。早く席につかないとシバかれる・・・<br />
Note: there is a new version of cabal-install available.<br />
To upgrade, run: cabal install cabal-install<br />
### 注：おのれをインストールしろと・・・<br />
uedamac:~ ueda$ cabal install cabal-install<br />
（略）<br />
Linking dist/build/cabal/cabal ...<br />
Installing executable(s) in /Users/ueda/.cabal/bin<br />
###注：やっとこさutf8-stringをインストール。背後から殺気を感じるのである。<br />
### さっきから、殺気を感じるのである。<br />
uedamac:~ ueda$ cabal install utf8-string<br />
（略）<br />
uedamac:~ ueda$ ghc cat.hs<br />
[/bash]<br />
<br />
<span style="color: #ff0000;">通りました。</span><br />
<br />
[bash]<br />
uedamac:~ ueda$ echo へのへのもへじ | ./cat<br />
へのへのもへじ<br />
[/bash]<br />
<br />
実行もできた。よかったよかった。<br />
<br />
しかし、コード配って人にこんな作業させるのもドSの所業なので、そのうちバイナリでどう配布するか考えないといけませんね・・・。<br />
<br />
<iframe style="width: 120px; height: 240px;" src="http://rcm-jp.amazon.co.jp/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=ryuichiueda-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4797336021" height="240" width="320" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><!--:--><!--:en--><a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/tree/master/COMMANDS.HS" target="_blank">Haskellでopen usp Tukubai のコマンドを置き換えるプロジェクト</a>をちまちま進めています。<br />
<br />
いつも使っているFreeBSDの環境では日本語の環境をセットアップしてあったのですが、自分のローカルのMacでもできないかと作業しましたのでメモです。<br />
<br />
コンパイルしたいのは次のコードですが・・・<br />
<br />
[hs]<br />
uedamac:~ ueda$ cat cat.hs<br />
import qualified Data.ByteString.Lazy.Char8 as BS<br />
import Codec.Binary.UTF8.String as CBUS<br />
import System.Environment<br />
import System.IO<br />
<br />
main :: IO ()<br />
main = do BS.getContents &amp;gt;&amp;gt;= putBSLines<br />
<br />
--UTF-8の出力のお約束<br />
putBSLines :: BS.ByteString -&amp;gt; IO ()<br />
putBSLines = putStr . CBUS.decodeString . BS.unpack<br />
[/hs]<br />
<br />
素のghcだと次のように叱られます。これが通らないと、このプロジェクトは頓挫します。どうしましょう。<span style="color: #ff0000;">（ちなみに、コードを説明してと言われても、今のところ、無理。）</span><br />
<br />
[bash]<br />
uedamac:~ ueda$ ghc cat.hs<br />
<br />
cat.hs:2:8:<br />
 Could not find module `Codec.Binary.UTF8.String'<br />
 Use -v to see a list of the files searched for.<br />
[/bash]<br />
<br />
というわけで、次のサイトを参考に、もうちょっと環境を整えました。<br />
<ul><br />
	<li><a href="http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html" target="_blank"><span style="line-height: 1.714285714; font-size: 1rem;">http://fp.okeefecreations.com/2011/02/homebrew-for-haskell.html</span></a></li><br />
</ul><br />
[bash]<br />
### brew install ghc は終わっている。<br />
$ brew install haskell-platform<br />
==&amp;gt; Downloading http://lambda.haskell.org/platform/download/2012.4.0.0/haskell-p<br />
######################################################################## 100.0%<br />
==&amp;gt; ./configure --prefix=/usr/local/Cellar/haskell-platform/2012.4.0.0 --enable-<br />
==&amp;gt; make install<br />
### 注：すげー時間がかかる。<br />
==&amp;gt; Caveats<br />
Run `cabal update` to initialize the package list.<br />
<br />
If you are replacing a previous version of haskell-platform, you may want<br />
to unregister packages belonging to the old version. You can find broken<br />
packages using:<br />
 ghc-pkg check --simple-output<br />
You can uninstall them using:<br />
 ghc-pkg check --simple-output | xargs -n 1 ghc-pkg unregister --force<br />
==&amp;gt; Summary<br />
uedamac:~ ueda$ cabal update<br />
### 注：またすげー時間がかかる。<br />
### おや、夕食ができたようだ・・・。早く席につかないとシバかれる・・・<br />
Note: there is a new version of cabal-install available.<br />
To upgrade, run: cabal install cabal-install<br />
### 注：おのれをインストールしろと・・・<br />
uedamac:~ ueda$ cabal install cabal-install<br />
（略）<br />
Linking dist/build/cabal/cabal ...<br />
Installing executable(s) in /Users/ueda/.cabal/bin<br />
###注：やっとこさutf8-stringをインストール。背後から殺気を感じるのである。<br />
### さっきから、殺気を感じるのである。<br />
uedamac:~ ueda$ cabal install utf8-string<br />
（略）<br />
uedamac:~ ueda$ ghc cat.hs<br />
[/bash]<br />
<br />
<span style="color: #ff0000;">通りました。</span><br />
<br />
[bash]<br />
uedamac:~ ueda$ echo へのへのもへじ | ./cat<br />
へのへのもへじ<br />
[/bash]<br />
<br />
実行もできた。よかったよかった。<br />
<br />
しかし、コード配って人にこんな作業させるのもドSの所業なので、そのうちバイナリでどう配布するか考えないといけませんね・・・。<br />
<br />
<iframe style="width: 120px; height: 240px;" src="http://rcm-jp.amazon.co.jp/e/cm?lt1=_blank&amp;bc1=000000&amp;IS2=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=ryuichiueda-22&amp;o=9&amp;p=8&amp;l=as4&amp;m=amazon&amp;f=ifr&amp;ref=ss_til&amp;asins=4797336021" height="240" width="320" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><!--:-->
