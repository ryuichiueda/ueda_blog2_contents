---
Keywords:コマンド,csv2txt.py
Copyright: (C) 2017 Ryuichi Ueda
---
# CSVをスペース区切りに変換するコマンド
CSVをスペース区切りのデータにするコマンドを自作して持っていてたまに使っていたのですが、これをGitHubにアップしました。Pythonのコードです。これ、オートマトンからコードに落とす例として書いた物なので、Pythonですが何にでもあっという間に移植できると思います（関数型言語を除く）。<br />
<br />
<!--more--><br />
<br />
<a href="https://github.com/ryuichiueda/MyCommands/blob/master/csv2txt.py" target="_blank">https://github.com/ryuichiueda/MyCommands/blob/master/csv2txt.py</a><br />
<br />
どんな入出力かは、Excelで作ったCSVを通してみてご確認を・・・というのは不親切なので、2つだけ例を。<br />
<br />
[bash]<br />
ueda\@remote:~$ cat file2.csv <br />
&quot;apple&quot;,&quot;ban,ana&quot;,melon<br />
&quot;apple&quot;,melon<br />
melon,&quot;apple&quot;,&quot;ban,ana&quot;<br />
&quot;ban,ana&quot;,&quot;apple&quot;<br />
ueda\@remote:~$ cat file2.csv | python csv2txt.py <br />
apple ban,ana melon<br />
apple melon<br />
melon apple ban,ana<br />
ban,ana apple<br />
ueda\@remote:~$ cat file3.csv <br />
&quot;ap&quot;&quot;ple&quot;&quot;&quot;,&quot;ban,<br />
ana&quot;,melon<br />
&quot;ap&quot;&quot;ple&quot;,melon<br />
melon,&quot;apple&quot;,&quot;ban<br />
,ana&quot;<br />
&quot;ban,ana&quot;,&quot;apple&quot;<br />
ueda\@remote:~$ cat file3.csv | python csv2txt.py <br />
ap&quot;ple&quot; ban,\\nana melon<br />
ap&quot;ple melon<br />
melon apple ban\\n,ana<br />
ban,ana apple<br />
[/bash]<br />
<br />
あ、Shift JISのデータの場合、このコマンドの前にパイプでnkf -wLuxをつないでください。<br />
<br />
<br />
では。
