# <!--:ja-->グルー言語作成の最初の一歩<!--:-->
<!--:ja--><a href="http://blog.ueda.asia/?p=2058" title="36歳の誕生日にグルー言語作る宣言をせざるを得なくなった" target="_blank">こういう経緯</a>で、前々から作りたいと思っていたシェルスクリプトに代わりうるグルー言語を作ることになったわけですが、<!--:--><!--more--><!--:ja-->ブログの記事を見た方やその場にいた方から「有言実行すばらしい！」などとコメントをいただきました。しかし、冷静に考えれば記事書いただけじゃ有限実行じゃないので、本日午前中、筑波エクスプレスの社内とつくば駅前のミスタードーナツで最初のプロトタイプを書きました。<br />
<br />
こういうのはいろんな人が参加できるべきですが、<span style="color:red">Haskellで書き始めてしまい、最初から人を拒むという、コミュニケーションに問題のある人格っぷり</span>を演出しております。でもパーサ書くの、これが一番簡単なので・・・。とりあえずやりたいことを表現するためのプロトタイプ作りは、当面Haskellで行います。<br />
<br />
<h2>作ったもの</h2><br />
<br />
一つのパイプラインに相当するものを新言語で書き、それをbashのコードに変換するコンバータです。やりたいことがbashの範疇を超えない限りはこれをどんどん成長させていこうかと。もしかしたらコンバータだけで自分の欲しいものができてしまうかもしれない・・・。<br />
<br />
<ul><br />
 <li>新言語のコード（関数みたいなもの一個だけ書いたもの）</li><br />
</ul><br />
<br />
[python]<br />
uedambp:GlueLang ueda$ cat PROTOTYPE/SAMPLE_SCRIPTS/findfilename.glue <br />
uedambp:PROTOTYPE ueda$ cat SAMPLE_SCRIPTS/findfilename.glue <br />
filter main word dir:<br />
	find dir <br />
	grep word<br />
[/python]<br />
<br />
dirで指定したディレクトリをfindして、その出力をwordで指定した文字列で検索するフィルタという意味です。<br />
<br />
これを次のように変換するコマンド（langToBash）を作りました。<br />
<br />
[bash]<br />
uedambp:PROTOTYPE ueda$ ./langToBash ./SAMPLE_SCRIPTS/findfilename.glue <br />
#!/bin/bash -e<br />
<br />
function main(){<br />
	find $2 | 	grep $1<br />
}<br />
main &quot;$1&quot; &quot;$2&quot;<br />
[/bash]<br />
<br />
ちゃんと動きます。<br />
<br />
[bash]<br />
uedambp:PROTOTYPE ueda$ ./langToBash ./SAMPLE_SCRIPTS/findfilename.glue &gt; hoge.bash<br />
uedambp:PROTOTYPE ueda$ chmod +x hoge.bash <br />
uedambp:PROTOTYPE ueda$ ./hoge.bash &quot;lang&quot; &quot;.&quot; <br />
./langToBash<br />
./langToBash.hi<br />
./langToBash.hs<br />
./langToBash.o<br />
[/bash]<br />
<br />
<br />
<h2>書いたコード</h2><br />
<br />
とにかく動くものを。拙速に拙速に・・・ということで、Haskell分かる人にとっては拙速なコードでございます。電車とドーナツ屋で生まれました。あ、日付が違う・・・。<br />
<br />
<a href="https://github.com/ryuichiueda/GlueLang/tree/develop" target="_blank">GitHubではここに置いてます。</a><br />
<br />
[hs]<br />
import System.Environment<br />
import System.IO<br />
import Text.Parsec<br />
import Text.Parsec.String<br />
import qualified Data.Text as D<br />
--import Text.ParserCombinators.Parsec<br />
<br />
showUsage :: IO ()<br />
showUsage = do System.IO.hPutStr stderr<br />
 (&quot;Usage : langToBash &lt;file&gt;\\n&quot; ++<br />
		&quot;Sun Feb 16 15:55:08 JST 2014\\n&quot; )<br />
<br />
<br />
type FilterName = String<br />
type FilterArgs = (Int,String)<br />
type FilterCode = String<br />
data Filter = Filter FilterName [FilterArgs] [FilterCode] deriving Show<br />
data Script = Script [Filter] | Err String deriving Show<br />
<br />
main :: IO()<br />
main = do args &lt;- getArgs<br />
 case args of<br />
 [] -&gt; showUsage<br />
 [f] -&gt; readF f &gt;&gt;= putStr . toBash . parseGlueLang<br />
 _ -&gt; showUsage<br />
<br />
toBash :: Script -&gt; String<br />
toBash (Script fs) = unlines (header:(map toOneLiner fs) ++ [footer])<br />
 where header = &quot;#!/bin/bash -e\\n&quot;<br />
 footer = &quot;main &quot; ++ mainArgs fs<br />
<br />
mainArgs :: [Filter] -&gt; String<br />
mainArgs ((Filter &quot;main&quot; args _):fs) = unwords $ [ &quot;\\&quot;&quot; ++ ('$':(show n)) ++ &quot;\\&quot;&quot; | n &lt;- [1..len]]<br />
 where len = length args<br />
mainArgs _ = &quot;&quot;<br />
<br />
toOneLiner :: Filter -&gt; String<br />
toOneLiner (Filter fname opts codes) = func fname ++ &quot;\\n&quot;<br />
 ++ (pipeCon $ map (convArgs opts) codes) ++ &quot;}&quot;<br />
 where func fname = &quot;function &quot; ++ fname ++ &quot;(){&quot;<br />
<br />
pipeCon :: [String] -&gt; String<br />
pipeCon [s] = s ++ &quot;\\n&quot;<br />
pipeCon (s:ss) = s ++ &quot; | &quot; ++ pipeCon ss<br />
<br />
convArgs :: [FilterArgs] -&gt; FilterCode -&gt; String<br />
convArgs [] str = str<br />
convArgs ((n,op):ops) str = convArgs ops $ D.unpack (D.replace (D.pack op) (D.pack $ ('$':show n)) (D.pack str))<br />
<br />
readF :: String -&gt; IO String<br />
readF &quot;-&quot; = getContents<br />
readF f = readFile f<br />
<br />
parseGlueLang :: String -&gt; Script<br />
parseGlueLang str = case parse code &quot;&quot; str of<br />
 Right scr -&gt; scr <br />
 Left err -&gt; Err ( show err )<br />
<br />
code = many1 langFilter &gt;&gt;= return . Script<br />
<br />
langFilter = do string &quot;filter &quot;<br />
 nm &lt;- langWord<br />
		args &lt;- many langWord<br />
 many langSpace<br />
 char ':'<br />
 many1 ( char '\\n' )<br />
 lns &lt;- many1 langFilterCode<br />
 return $ Filter nm (zip [1..] args) lns<br />
<br />
langWord = do w &lt;- many1 (noneOf &quot; :\\n\\t&quot;)<br />
 many langSpace<br />
 return w<br />
<br />
langSpace = oneOf &quot; \\t&quot;<br />
<br />
langFilterCode = do ln &lt;- many (noneOf &quot;\\n&quot;)<br />
 char '\\n'<br />
 return ln<br />
[/hs]<br />
<br />
以後はこのコードをピカピカにする一方、新言語の文法についてくどくど考察するつもりです。しかし、勤め人としてはちょっと休止せざるをえない事情がありまして、しばらく冬眠します・・・。<br />
<br />
<br />
とりあえず動くものを作ったので許してちょえ。<!--:-->
