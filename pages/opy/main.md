---
Copyright: (C) Ryuichi Ueda
---

# opy: ワンライナー用Python

## ウェブページ

* パッケージ
    * snap: https://snapcraft.io/opy
* コード
    * リポジトリ: https://github.com/ryuichiueda/opy
    * [homebrew用リポジトリ](https://github.com/ryuichiueda/homebrew-oneliner-python)
    * [snap用リポジトリ](https://github.com/ryuichiueda/opy-snap)
* opyに関する記事 
    * [Pythonをコマンドラインで使いたいのでopyというコマンドを作った](/?post=20190908_opy)
    * [OPY command that makes Python easy on CLI](/?post=20190908_opy_e)
* [使用例 on シェル芸bot](https://twitter.com/search?q=%40minyoruminyon%20opy&src=typed_query&f=live)


## 以下は書きかけのドキュメント

## Introduction

Opy is an AWK like command that works on Python.
AWK is the representative line oriented programming language, and it is very powerful on one-liners.
This is an example. 

```
$ seq 3 | awk '{print $1*3}'  # triple the number of the field one and output
3
6
9
```

When we use another language like this, we must write the procedure for reading the standard input and a loop for processing each line. However, AWK does not require them. The code in the argument is automatically applied to each line. Then the result goes out through the standard output. We can also use Perl and Ruby with line oriented programming. However, awk codes are usually simpler than those of Perl and Ruby when tasks are not so complicated. 


Python is not a line oriented language. When we try to write the above code with Python, the code becomes much longer than it.

```
$ seq 3 | python3 -c 'import sys;print("\n".join([ str(int(x)*3) for x in sys.stdin ]))'
3
6
9
```

However, 
