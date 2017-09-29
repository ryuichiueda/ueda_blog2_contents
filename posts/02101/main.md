---
Keywords: Haskell,名前はまだない,グルー言語,グルー言語を作る,おじさん頑張ったよ
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->グルー言語作成の最初の一歩<!--:-->
<!--:ja--><a href="http://blog.ueda.asia/?p=2058" title="36歳の誕生日にグルー言語作る宣言をせざるを得なくなった" target="_blank">こういう経緯</a>で、前々から作りたいと思っていたシェルスクリプトに代わりうるグルー言語を作ることになったわけですが、<!--:--><!--more--><!--:ja-->ブログの記事を見た方やその場にいた方から「有言実行すばらしい！」などとコメントをいただきました。しかし、冷静に考えれば記事書いただけじゃ有限実行じゃないので、本日午前中、筑波エクスプレスの社内とつくば駅前のミスタードーナツで最初のプロトタイプを書きました。

こういうのはいろんな人が参加できるべきですが、<span style="color:red">Haskellで書き始めてしまい、最初から人を拒むという、コミュニケーションに問題のある人格っぷり</span>を演出しております。でもパーサ書くの、これが一番簡単なので・・・。とりあえずやりたいことを表現するためのプロトタイプ作りは、当面Haskellで行います。

<h2>作ったもの</h2>

一つのパイプラインに相当するものを新言語で書き、それをbashのコードに変換するコンバータです。やりたいことがbashの範疇を超えない限りはこれをどんどん成長させていこうかと。もしかしたらコンバータだけで自分の欲しいものができてしまうかもしれない・・・。

<ul>
 <li>新言語のコード（関数みたいなもの一個だけ書いたもの）</li>
</ul>

```python
uedambp:GlueLang ueda$ cat PROTOTYPE/SAMPLE_SCRIPTS/findfilename.glue 
uedambp:PROTOTYPE ueda$ cat SAMPLE_SCRIPTS/findfilename.glue 
filter main word dir:
	find dir 
	grep word
```

dirで指定したディレクトリをfindして、その出力をwordで指定した文字列で検索するフィルタという意味です。

これを次のように変換するコマンド（langToBash）を作りました。

```bash
uedambp:PROTOTYPE ueda$ ./langToBash ./SAMPLE_SCRIPTS/findfilename.glue 
#!/bin/bash -e

function main(){
	find $2 | 	grep $1
}
main "$1" "$2"
```

ちゃんと動きます。

```bash
uedambp:PROTOTYPE ueda$ ./langToBash ./SAMPLE_SCRIPTS/findfilename.glue > hoge.bash
uedambp:PROTOTYPE ueda$ chmod +x hoge.bash 
uedambp:PROTOTYPE ueda$ ./hoge.bash "lang" "." 
./langToBash
./langToBash.hi
./langToBash.hs
./langToBash.o
```


<h2>書いたコード</h2>

とにかく動くものを。拙速に拙速に・・・ということで、Haskell分かる人にとっては拙速なコードでございます。電車とドーナツ屋で生まれました。あ、日付が違う・・・。

<a href="https://github.com/ryuichiueda/GlueLang/tree/develop" target="_blank">GitHubではここに置いてます。</a>

```hs
import System.Environment
import System.IO
import Text.Parsec
import Text.Parsec.String
import qualified Data.Text as D
--import Text.ParserCombinators.Parsec

showUsage :: IO ()
showUsage = do System.IO.hPutStr stderr
 ("Usage : langToBash <file>\\n" ++
		"Sun Feb 16 15:55:08 JST 2014\\n" )


type FilterName = String
type FilterArgs = (Int,String)
type FilterCode = String
data Filter = Filter FilterName [FilterArgs] [FilterCode] deriving Show
data Script = Script [Filter] | Err String deriving Show

main :: IO()
main = do args <- getArgs
 case args of
 [] -> showUsage
 [f] -> readF f >>= putStr . toBash . parseGlueLang
 _ -> showUsage

toBash :: Script -> String
toBash (Script fs) = unlines (header:(map toOneLiner fs) ++ [footer])
 where header = "#!/bin/bash -e\\n"
 footer = "main " ++ mainArgs fs

mainArgs :: [Filter] -> String
mainArgs ((Filter "main" args _):fs) = unwords $ [ "\\"" ++ ('$':(show n)) ++ "\\"" | n <- [1..len]]
 where len = length args
mainArgs _ = ""

toOneLiner :: Filter -> String
toOneLiner (Filter fname opts codes) = func fname ++ "\\n"
 ++ (pipeCon $ map (convArgs opts) codes) ++ "}"
 where func fname = "function " ++ fname ++ "(){"

pipeCon :: [String] -> String
pipeCon [s] = s ++ "\\n"
pipeCon (s:ss) = s ++ " | " ++ pipeCon ss

convArgs :: [FilterArgs] -> FilterCode -> String
convArgs [] str = str
convArgs ((n,op):ops) str = convArgs ops $ D.unpack (D.replace (D.pack op) (D.pack $ ('$':show n)) (D.pack str))

readF :: String -> IO String
readF "-" = getContents
readF f = readFile f

parseGlueLang :: String -> Script
parseGlueLang str = case parse code "" str of
 Right scr -> scr 
 Left err -> Err ( show err )

code = many1 langFilter >>= return . Script

langFilter = do string "filter "
 nm <- langWord
		args <- many langWord
 many langSpace
 char ':'
 many1 ( char '\\n' )
 lns <- many1 langFilterCode
 return $ Filter nm (zip [1..] args) lns

langWord = do w <- many1 (noneOf " :\\n\\t")
 many langSpace
 return w

langSpace = oneOf " \\t"

langFilterCode = do ln <- many (noneOf "\\n")
 char '\\n'
 return ln
```

以後はこのコードをピカピカにする一方、新言語の文法についてくどくど考察するつもりです。しかし、勤め人としてはちょっと休止せざるをえない事情がありまして、しばらく冬眠します・・・。


とりあえず動くものを作ったので許してちょえ。<!--:-->
