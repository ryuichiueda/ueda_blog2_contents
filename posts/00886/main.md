---
Keywords: プログラミング,Haskell,open,USP友の会,江頭
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->江頭問題の解決<!--:-->
<!--:ja-->以前、<br />
<a href="http://www.usptomo.com/PAGE=20130326HSTARR" target="_blank">http://www.usptomo.com/PAGE=20130326HSTARR</a><br />
で、「Haskellでopen usp Tukubaiのコマンドを作ったけど、ByteStringを使うと『江頭』という単語が文字化けする」とで騒いでいました。このときはStringを使う事で回避したのですが、入力データが大きくなるとやはり激烈に遅い。<br />
<br />
この問題、words関数を自作したらあっさり解決しましたのでここに書いておきます。<br />
<br />
まず、だめな例。<br />
<br />
[bash]<br />
bsd /home/ueda$ cat egashira.hs <br />
import System.Environment<br />
import System.IO<br />
import Data.ByteString.Lazy.Char8 as BS hiding (length,take,drop,filter,head)<br />
<br />
main :: IO ()<br />
main = BS.getContents &gt;&gt;= BS.putStrLn . BS.unwords . BS.words<br />
<br />
bsd /home/ueda$ echo &quot;栃木 江頭 江頭 栃木&quot; | ./egashira <br />
? ?木 江? ? 江? ? ? ?木<br />
[/bash]<br />
<br />
以下が小手先の修正。<br />
<br />
[bash]<br />
bsd /home/ueda$ cat egashira.hs<br />
import System.Environment<br />
import System.IO<br />
import Data.ByteString.Lazy.Char8 as BS hiding (length,take,drop,filter,head)<br />
<br />
main :: IO ()<br />
main = BS.getContents &gt;&gt;= BS.putStr . BS.unwords . egaWords<br />
<br />
egaWords :: BS.ByteString -&gt; [BS.ByteString]<br />
egaWords str = split ' ' str<br />
bsd /home/ueda$ echo &quot;栃木 江頭 江頭 栃木&quot; | ./egashira <br />
栃木 江頭 江頭 栃木<br />
[/bash]<br />
<br />
<br />
うーん。open usp Tukubai についてはとりあえずこれでいいか・・・。Python版をHaskell版のコマンドに置き換える作業、やる気がでてきた。<!--:-->
