---
Keywords: プログラミング,Haskell,愚痴,グルー言語,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# グルー言語を作る作業を少し進めた
<!--:ja-->留守番で子供を背負ってどん兵衛を立ち食いという悲惨な昼飯を執行した上田です。背中の子供が寝ているうちに例の言語の作業を進めました。このエントリーは、子供と添い寝しながらiPhoneで書いています。いったいなんなんでしょう？

<!--:--><!--:en-->留守番で子供を背負ってどん兵衛を食べた上田です。背中の子供が寝ているうちに例の言語の作業を進めました。

これは、子供と添い寝しながらiPhoneで書いています。いったいなんなんでしょう？

とりあえずコードを掃除してテストを一つ作ってmasterブランチにマージしたくらいでたいしたことはしてません。

<a target="_blank" href="https://github.com/ryuichiueda/GlueLang?files=1">https://github.com/ryuichiueda/GlueLang?files=1</a>

今のところ、コードの本体は新言語をbashに変換するものですが、作ったbashを変換プログラムから直接起動することを試みた残骸がlangToBash.hsに残っています。

この部分、動くことには動くのですが、標準入力をbashのコードに投げて、bashのコードから標準出力をもらうところが同時に動かないので使い物になりません。ちゃんとファイル記述子を操作しないとあかんのでありましょう。

早めにCで書いた方がええんだろか？

以上、愚痴でした。


昼寝する。<!--:--><!--more--><!--:ja-->

とりあえずコードを掃除してテストを一つ作ってmasterブランチにマージしたくらいでたいしたことはしてません。

<a target="_blank" href="https://github.com/ryuichiueda/GlueLang?files=1">https://github.com/ryuichiueda/GlueLang?files=1</a>

今のところ、コードの本体は新言語をbashに変換するものですが、作ったbashを変換プログラムから直接起動することを試みた残骸がlangToBash.hsに残っています。

```hs
main' :: [String] -&gt; IO ()
main' (scr:as) = do cs &lt;- readF scr
 pn &lt;- getProgName
 let scrname = scr ++ &quot;.bash&quot;
 writeFile scrname $ (Bash.toBash . parseGlueLang) cs
{--
an attempt of automatic execution of the generated bash script
This function doesn't work well since
the standard input is buffered before on memory. 
The amount of buffer is small.
 let opts = [&quot;-evx&quot;,scrname] ++ as
 (stdin, stdout, stderr ,procHandle) &lt;- runInteractiveProcess &quot;bash&quot; opts Nothing Nothing
 hPutStr stdin =&lt;&lt; getContents
 hFlush stdin
 hClose stdin
 putStr =&lt;&lt; hGetContents stdout
--}
```

この部分、動くことには動くのですが、標準入力をbashのコードに投げて、bashのコードから標準出力をもらうところが同時に動かないので使い物になりません。ちゃんとファイル記述子を操作しないとあかんのでありましょう。

早めにCで書いた方がええんだろか？

以上、愚痴でした。


昼寝する。<!--:-->
