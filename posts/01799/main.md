---
Keywords: CLI,Haskell,USP友の会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# シェル芸勉強会に対して自ら敢えてHaskellで他流試合を申し込む
昨日のシェル芸勉強会に対して、自分で喧嘩を売ってみます。書きなぐりのHaskellコードです。問題はコチラ↓。<br />
<br />
<iframe src="http://www.slideshare.net/slideshow/embed_code/29426544" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/ryuichiueda/20131222-8" title="20131222 第8回シェル芸勉強会スライド" target="_blank">20131222 第8回シェル芸勉強会スライド</a> </strong> from <strong><a href="http://www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h2>Q1（データのフリップ）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q1.hs<br />
main = getContents &gt;&gt;= putStrLn. unwords . f . words<br />
f [] = []<br />
f (a:b:c) = [b,a] ++ f c<br />
uedamac:tmp ueda$ echo {1..10} | ./q1<br />
2 1 4 3 6 5 8 7 10 9<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
<h2>Q2（文字列の個数カウント）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q2.hs<br />
main = getContents &gt;&gt;= print . g. (Count 0 0 0 0)<br />
data Count = Count Int Int Int Int String deriving Show<br />
g (Count a b c d []) = Count a b c d []<br />
g (Count a b c d ('ユ':'ニ':'ケ':'ー':'ジ':str)) = g (Count (a+1) b c d str)<br />
g (Count a b c d ('ユ':'ニ':'ゲ':'ー':'ジ':str)) = g (Count a (b+1) c d str)<br />
g (Count a b c d ('U':'S':'P':str)) = g (Count a b (c+1) d str)<br />
g (Count a b c d ('U':'P':'S':str)) = g (Count a b c (d+1) str)<br />
g (Count a b c d (_:str)) = g (Count a b c d str)<br />
uedamac:tmp ueda$ echo ユニゲージユニケージユニゲージUSP友の会USP友の会UPS友の会UPS友の会 | ./q2<br />
Count 1 2 2 2 &quot;&quot;<br />
[/bash]<br />
<br />
<h2>Q3（一致するファイルの検出）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q3.hs<br />
main = do a &lt;- readFile &quot;file1&quot;<br />
 b &lt;- readFile &quot;file2&quot;<br />
 c &lt;- readFile &quot;file3&quot;<br />
 d &lt;- readFile &quot;file4&quot;<br />
 g [(&quot;file1&quot;,a),(&quot;file2&quot;,b),(&quot;file3&quot;,c),(&quot;file4&quot;,d)]<br />
<br />
g [] = return ()<br />
g (a:ds) = f a ds &gt;&gt; g ds<br />
f a ds = putStrLn $ concat $ map (h a) ds<br />
h (f1,a) (f2,b) = if a == b then unwords [f1,f2] else []<br />
uedamac:tmp ueda$ ./q3<br />
file1 file3<br />
<br />
<br />
<br />
<br />
[/bash]<br />
<br />
<br />
<h2>Q4（変則ソート）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q4.hs<br />
main = getContents &gt;&gt;= print . f. map (\\x -&gt; read x :: Int) . words<br />
<br />
f ns = odd ++ eve<br />
 where odd = filter (\\x -&gt; x `mod` 2 == 0) ns<br />
 eve = filter (\\x -&gt; x `mod` 2 == 1) ns<br />
uedamac:tmp ueda$ echo 3 8 2 10 1 8 9 | ./q4<br />
[8,2,10,8,3,1,9]<br />
[/bash]<br />
<br />
<h2>Q5（ランレングス圧縮の一種）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q5.hs <br />
main = getContents &gt;&gt;= putStrLn . unwords . f . filter (\\x -&gt; x == '0' || x == '1')<br />
f (a:ss) = f' (a:ss) a<br />
f' [] _ = []<br />
f' str a = (a:lng) : f' (dropWhile (== a) str) c<br />
 where b = length $ takeWhile (== a) str<br />
 c = if a == '0' then '1' else '0'<br />
 lng = if b == 1 then &quot;&quot; else show b<br />
<br />
uedamac:tmp ueda$ echo 000001111111111001010 | ./q5 <br />
05 110 02 1 0 1 0<br />
[/bash]<br />
<br />
<h2>Q6（連続した数字の省略）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q6.hs<br />
import Data.List.Split<br />
main = getContents &gt;&gt;= putStrLn . unwords . g . splitWhen (== -1). f . map (\\x -&gt; read x :: Int) . words<br />
<br />
f (a:b:[]) = if a+1 == b then [a,b] else [a,-1,b]<br />
f (a:b:ns) = if a+1 == b then a : f (b:ns) else [a,-1] ++ f (b:ns)<br />
<br />
g [] = []<br />
g (a:as) = h a : g as<br />
<br />
h as = if a == b then a else a ++ &quot;-&quot; ++ b<br />
 where a = show $ head as<br />
 b = show $ last as<br />
uedamac:tmp ueda$ echo 1 2 3 5 6 8 10 11 12 15 | ./q6<br />
1-3 5-6 8 10-12 15<br />
[/bash]<br />
<br />
<h2>Q7（パスワード破り）</h2><br />
<br />
[bash]<br />
uedamac:tmp ueda$ cat q7.hs<br />
import Data.Digest.Pure.MD5<br />
import qualified Data.ByteString.Lazy.Char8 as B<br />
main = g $ f [000..999]<br />
<br />
g [] = return ()<br />
g ((n,a):as) = (if t `B.isPrefixOf` aa then print n else return () ) &gt;&gt; g as<br />
 where t = B.pack &quot;250&quot;<br />
 aa = B.pack $ show a<br />
<br />
f [] = []<br />
f (n:ns) <br />
 | n &lt; 10 = (n,(md5 $ B.pack (&quot;00&quot; ++ (show n)))) : f ns<br />
 | n &lt; 100 = (n,(md5 $ B.pack (&quot;0&quot; ++ (show n)))) : f ns<br />
 | otherwise = (n,(md5 $ B.pack (show n))) : f ns<br />
uedamac:tmp ueda$ ./q7 <br />
456<br />
[/bash]<br />
<br />
<h2>Q8（しりとり）</h2><br />
<br />
sort -R はインチキっぽいが、ソートしなくても一応できるので・・・<br />
[bash]<br />
uedamac:tmp ueda$ cat q8.hs<br />
main = getContents &gt;&gt;= putStrLn . unlines . f. f. f . lines <br />
<br />
f [] = [] <br />
f (a:[]) = [] <br />
f (a:b:lns) <br />
 | last a == head b = (a ++ &quot;-&gt;&quot; ++ b) : f lns<br />
 | otherwise = f lns<br />
uedamac:tmp ueda$ gsort -R /usr/share/dict/words | ./q8<br />
rhombogenic-&gt;cattiness-&gt;sarkar-&gt;rhamnaceous-&gt;swishing-&gt;geneticism-&gt;ministryship-&gt;pleonastical<br />
[/bash]<br />
<br />
<strong style="color:red;font-size:24pt">できた〜〜〜〜！！！</strong>けどやっぱりシェルワンライナーの方が気楽だ・・・
