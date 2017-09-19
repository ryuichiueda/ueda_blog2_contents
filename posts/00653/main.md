---
Keywords: プログラミング,Haskell,Haskell中毒
Copyright: (C) 2017 Ryuichi Ueda
---

# Haskellのerror関数が型破りなんだが型破ってない。
Haskellでコマンドを書いていて、エラーの出し方がよく分からないのでゴマカシゴマカシしていたのですが、真面目にオライリーの本を読んでるとerrorという関数を見つけました。ちゃんと例外処理をやるにはモナド使えとかなんとか書いてありましたが、コマンドならこれが一番いいかと。

例えば、標準入力から文字列を読んで最初の単語だけ出力するプログラムを書きます。

[hs]
uedamac:~ ueda$ cat hoge.hs
import System.IO

main :: IO ()
main = getContents &gt;&gt;= putStrLn . firstWord

firstWord :: String -&gt; String
firstWord cs = head $ words cs
[/hs]

こいつをコンパイルして実行すると実行できる訳ですが、単語を入力しないという意地悪をするとエラーが発生します。

[hs]
uedamac:~ ueda$ ghc hoge.hs
[1 of 1] Compiling Main ( hoge.hs, hoge.o )
Linking hoge ...
uedamac:~ ueda$ echo This is a pen. | ./hoge
This
uedamac:~ ueda$ echo | ./hoge
hoge: Prelude.head: empty list
uedamac:~ ueda$ echo $?
1
[/hs]

そんな意地悪な入力にはちゃんと教育的指導を与えなければいけません。error関数を使うとちゃんと自分でエラーメッセージを作文できます。

[hs]
uedamac:~ ueda$ cat hoge2.hs 
import System.IO

main :: IO ()
main = getContents &gt;&gt;= putStrLn . firstWord

firstWord :: String -&gt; String
firstWord cs = if (length $ words cs) == 0
 then error &quot;no words&quot;
 else head $ words cs
[/hs]

はい実行。

[hs]
uedamac:~ ueda$ ghc hoge2.hs
[1 of 1] Compiling Main ( hoge2.hs, hoge2.o )
Linking hoge2 ...
uedamac:~ ueda$ echo This is a pen. | ./hoge2
This
uedamac:~ ueda$ echo | ./hoge2
hoge2: no words
uedamac:~ ueda$ echo $?
1
[/hs]

終了ステータスは1で固定なんでしょうか？まあ、今の時点ではよいでしょう。

んで、このerror関数を使うなとかなんだとかいろいろ議論はあるんですが、面白いのは型で、こんな定義になってます。

[hs]
error :: [Char] -&gt; a
[/hs]

出力が任意の型（a）になってるので、型のチェックに通るワケですね・・・。しかし、ずるいことにa型を返すと言いつつこいつは何も返しません。この関数が呼ばれると、他の処理を全部破棄して何も恐れるものの無い状態にしてからエラーを吐くだけなので、処理上、特に問題ないようです。

これ考えた人、これ考えたときどんな顔してたんでしょうね？



いろいろ興味が尽きませんが、寝るです。
