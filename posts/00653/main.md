---
Keywords:プログラミング,Haskell,Haskell中毒
Copyright: (C) 2017 Ryuichi Ueda
---
# Haskellのerror関数が型破りなんだが型破ってない。
Haskellでコマンドを書いていて、エラーの出し方がよく分からないのでゴマカシゴマカシしていたのですが、真面目にオライリーの本を読んでるとerrorという関数を見つけました。ちゃんと例外処理をやるにはモナド使えとかなんとか書いてありましたが、コマンドならこれが一番いいかと。<br />
<br />
例えば、標準入力から文字列を読んで最初の単語だけ出力するプログラムを書きます。<br />
<br />
[hs]<br />
uedamac:~ ueda$ cat hoge.hs<br />
import System.IO<br />
<br />
main :: IO ()<br />
main = getContents &gt;&gt;= putStrLn . firstWord<br />
<br />
firstWord :: String -&gt; String<br />
firstWord cs = head $ words cs<br />
[/hs]<br />
<br />
こいつをコンパイルして実行すると実行できる訳ですが、単語を入力しないという意地悪をするとエラーが発生します。<br />
<br />
[hs]<br />
uedamac:~ ueda$ ghc hoge.hs<br />
[1 of 1] Compiling Main ( hoge.hs, hoge.o )<br />
Linking hoge ...<br />
uedamac:~ ueda$ echo This is a pen. | ./hoge<br />
This<br />
uedamac:~ ueda$ echo | ./hoge<br />
hoge: Prelude.head: empty list<br />
uedamac:~ ueda$ echo $?<br />
1<br />
[/hs]<br />
<br />
そんな意地悪な入力にはちゃんと教育的指導を与えなければいけません。error関数を使うとちゃんと自分でエラーメッセージを作文できます。<br />
<br />
[hs]<br />
uedamac:~ ueda$ cat hoge2.hs <br />
import System.IO<br />
<br />
main :: IO ()<br />
main = getContents &gt;&gt;= putStrLn . firstWord<br />
<br />
firstWord :: String -&gt; String<br />
firstWord cs = if (length $ words cs) == 0<br />
 then error &quot;no words&quot;<br />
 else head $ words cs<br />
[/hs]<br />
<br />
はい実行。<br />
<br />
[hs]<br />
uedamac:~ ueda$ ghc hoge2.hs<br />
[1 of 1] Compiling Main ( hoge2.hs, hoge2.o )<br />
Linking hoge2 ...<br />
uedamac:~ ueda$ echo This is a pen. | ./hoge2<br />
This<br />
uedamac:~ ueda$ echo | ./hoge2<br />
hoge2: no words<br />
uedamac:~ ueda$ echo $?<br />
1<br />
[/hs]<br />
<br />
終了ステータスは1で固定なんでしょうか？まあ、今の時点ではよいでしょう。<br />
<br />
んで、このerror関数を使うなとかなんだとかいろいろ議論はあるんですが、面白いのは型で、こんな定義になってます。<br />
<br />
[hs]<br />
error :: [Char] -&gt; a<br />
[/hs]<br />
<br />
出力が任意の型（a）になってるので、型のチェックに通るワケですね・・・。しかし、ずるいことにa型を返すと言いつつこいつは何も返しません。この関数が呼ばれると、他の処理を全部破棄して何も恐れるものの無い状態にしてからエラーを吐くだけなので、処理上、特に問題ないようです。<br />
<br />
これ考えた人、これ考えたときどんな顔してたんでしょうね？<br />
<br />
<br />
<br />
いろいろ興味が尽きませんが、寝るです。
