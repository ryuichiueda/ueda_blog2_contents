---
Keywords: プログラミング,Haskell,open,USP友の会,江頭
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->江頭問題の解決<!--:-->
<!--:ja-->以前、
<a href="http://www.usptomo.com/PAGE=20130326HSTARR" target="_blank">http://www.usptomo.com/PAGE=20130326HSTARR</a>
で、「Haskellでopen usp Tukubaiのコマンドを作ったけど、ByteStringを使うと『江頭』という単語が文字化けする」とで騒いでいました。このときはStringを使う事で回避したのですが、入力データが大きくなるとやはり激烈に遅い。

この問題、words関数を自作したらあっさり解決しましたのでここに書いておきます。

まず、だめな例。

[bash]
bsd /home/ueda$ cat egashira.hs 
import System.Environment
import System.IO
import Data.ByteString.Lazy.Char8 as BS hiding (length,take,drop,filter,head)

main :: IO ()
main = BS.getContents &gt;&gt;= BS.putStrLn . BS.unwords . BS.words

bsd /home/ueda$ echo &quot;栃木 江頭 江頭 栃木&quot; | ./egashira 
? ?木 江? ? 江? ? ? ?木
[/bash]

以下が小手先の修正。

[bash]
bsd /home/ueda$ cat egashira.hs
import System.Environment
import System.IO
import Data.ByteString.Lazy.Char8 as BS hiding (length,take,drop,filter,head)

main :: IO ()
main = BS.getContents &gt;&gt;= BS.putStr . BS.unwords . egaWords

egaWords :: BS.ByteString -&gt; [BS.ByteString]
egaWords str = split ' ' str
bsd /home/ueda$ echo &quot;栃木 江頭 江頭 栃木&quot; | ./egashira 
栃木 江頭 江頭 栃木
[/bash]


うーん。open usp Tukubai についてはとりあえずこれでいいか・・・。Python版をHaskell版のコマンドに置き換える作業、やる気がでてきた。<!--:-->
