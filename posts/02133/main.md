---
Keywords: プログラミング,Haskell,愚痴,グルー言語,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# グルー言語を作る作業を少し進めた
<!--:ja-->留守番で子供を背負ってどん兵衛を立ち食いという悲惨な昼飯を執行した上田です。背中の子供が寝ているうちに例の言語の作業を進めました。このエントリーは、子供と添い寝しながらiPhoneで書いています。いったいなんなんでしょう？<br />
<br />
<!--:--><!--:en-->留守番で子供を背負ってどん兵衛を食べた上田です。背中の子供が寝ているうちに例の言語の作業を進めました。<br />
<br />
これは、子供と添い寝しながらiPhoneで書いています。いったいなんなんでしょう？<br />
<br />
とりあえずコードを掃除してテストを一つ作ってmasterブランチにマージしたくらいでたいしたことはしてません。<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/GlueLang?files=1">https://github.com/ryuichiueda/GlueLang?files=1</a><br />
<br />
今のところ、コードの本体は新言語をbashに変換するものですが、作ったbashを変換プログラムから直接起動することを試みた残骸がlangToBash.hsに残っています。<br />
<br />
この部分、動くことには動くのですが、標準入力をbashのコードに投げて、bashのコードから標準出力をもらうところが同時に動かないので使い物になりません。ちゃんとファイル記述子を操作しないとあかんのでありましょう。<br />
<br />
早めにCで書いた方がええんだろか？<br />
<br />
以上、愚痴でした。<br />
<br />
<br />
昼寝する。<!--:--><!--more--><!--:ja--><br />
<br />
とりあえずコードを掃除してテストを一つ作ってmasterブランチにマージしたくらいでたいしたことはしてません。<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/GlueLang?files=1">https://github.com/ryuichiueda/GlueLang?files=1</a><br />
<br />
今のところ、コードの本体は新言語をbashに変換するものですが、作ったbashを変換プログラムから直接起動することを試みた残骸がlangToBash.hsに残っています。<br />
<br />
[hs]<br />
main' :: [String] -&gt; IO ()<br />
main' (scr:as) = do cs &lt;- readF scr<br />
 pn &lt;- getProgName<br />
 let scrname = scr ++ &quot;.bash&quot;<br />
 writeFile scrname $ (Bash.toBash . parseGlueLang) cs<br />
{--<br />
an attempt of automatic execution of the generated bash script<br />
This function doesn't work well since<br />
the standard input is buffered before on memory. <br />
The amount of buffer is small.<br />
 let opts = [&quot;-evx&quot;,scrname] ++ as<br />
 (stdin, stdout, stderr ,procHandle) &lt;- runInteractiveProcess &quot;bash&quot; opts Nothing Nothing<br />
 hPutStr stdin =&lt;&lt; getContents<br />
 hFlush stdin<br />
 hClose stdin<br />
 putStr =&lt;&lt; hGetContents stdout<br />
--}<br />
[/hs]<br />
<br />
この部分、動くことには動くのですが、標準入力をbashのコードに投げて、bashのコードから標準出力をもらうところが同時に動かないので使い物になりません。ちゃんとファイル記述子を操作しないとあかんのでありましょう。<br />
<br />
早めにCで書いた方がええんだろか？<br />
<br />
以上、愚痴でした。<br />
<br />
<br />
昼寝する。<!--:-->
