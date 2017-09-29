---
Keywords: コマンド,csv2txt.py
Copyright: (C) 2017 Ryuichi Ueda
---

# CSVをスペース区切りに変換するコマンド
CSVをスペース区切りのデータにするコマンドを自作して持っていてたまに使っていたのですが、これをGitHubにアップしました。Pythonのコードです。これ、オートマトンからコードに落とす例として書いた物なので、Pythonですが何にでもあっという間に移植できると思います（関数型言語を除く）。

<!--more-->

<a href="https://github.com/ryuichiueda/MyCommands/blob/master/csv2txt.py" target="_blank">https://github.com/ryuichiueda/MyCommands/blob/master/csv2txt.py</a>

どんな入出力かは、Excelで作ったCSVを通してみてご確認を・・・というのは不親切なので、2つだけ例を。

```bash
ueda\@remote:~$ cat file2.csv 
"apple","ban,ana",melon
"apple",melon
melon,"apple","ban,ana"
"ban,ana","apple"
ueda\@remote:~$ cat file2.csv | python csv2txt.py 
apple ban,ana melon
apple melon
melon apple ban,ana
ban,ana apple
ueda\@remote:~$ cat file3.csv 
"ap""ple""","ban,
ana",melon
"ap""ple",melon
melon,"apple","ban
,ana"
"ban,ana","apple"
ueda\@remote:~$ cat file3.csv | python csv2txt.py 
ap"ple" ban,\\nana melon
ap"ple melon
melon apple ban\\n,ana
ban,ana apple
```

あ、Shift JISのデータの場合、このコマンドの前にパイプでnkf -wLuxをつないでください。


では。
