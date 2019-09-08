---
Keywords: opy, Python, onelinar, shell-gei
Copyright: (C) 2019 Ryuichi Ueda
---

# OPY command that makes Python easy on CLI

## summary

Since I want to use Python on a shell, I have created [opy](https://github.com/ryuichiueda/opy) command.

## design and implementation

### works like a line-oriented language

  AWK (`awk` as a command) has been frequently used for one liners because it is a line-oriented language. When text data is given to `awk` from the standard input, it splits each line to a list of fields without any option or explicit code. This is an example. 


```
$ seq 3 | awk '{print $1*3}'  # 1列目に3をかける
3
6
9
```

Each number is set to `$1` automatically. This mechanism enables us to write a short one liner. 

  On the other hand, when we try to do the same thing with Python, we need a longer code. 

```
$ seq 3 | python3 -c 'import sys;print("\n".join([ str(int(x)*3) for x in sys.stdin ]))'
3
6
9
```

It is clearly unsuitable for oneliner. 

  However, Python has the list. Then AWK also treats fields of each line as an element of a list. So I thought the action of AWK can be replaced to the list operation of Python.

  I have implemented `opy` command, which works with this idea. This is an example.

```
$ seq 3 | opy '[F1*3]'
3
6
9
```

As an action, the code in the argument only gives the list. The command prints the list as `awk` does. 


　`Opy` also accepts the pattern. Differently from AWK, we need `:` between a pattern and an action.

```
### opy ###
$ seq 3 | opy 'F1%2:[F1*3]'
3
9
```

I also show equivalent codes with AWK and Python3. 

```
### AWK ###
$ seq 3 | awk '$1%2{print $1*3}'
3
9
### Python3 ###
$ seq 3 | python3 -c 'import sys;print("\n".join([ str(int(x)*3) for x in sys.stdin if int(x)%2 ]))'
3
9
```

When there are more than one elements in the list, the elements are joined with a space.

```
$ seq 3 | opy 'F1%2:["%d:odd"%F1, F1*3]'
1:odd 3
3:odd 9
```

  `Opy` also has a normal action. When we use it, we need to put sentences in curly brackets. 


```
$ seq 3 | opy '{print(F1, end="")}'
123
```


### grammer

  Over the Python grammer, I defined a rule. 


```
<rules> ::= <rule> | <rule> ";" <rules>
<rule> ::= <pattern> | <pattern> ":" <action> | <action>
<action> ::= <list action> | <normal action>
<pattern> ::= <boolean expression of Python> | "B" | "BEGIN" | "E" | "END" 
<normal action> ::= "{" <sentences of Python> "}"
<list action> ::= <a list of Python>
```


　`B, BEGIN, E, END`などの文字列はAWKのBEGINパターン、ENDパターンと同じもので、行を読み込む前の処理を書けます。次は一例です。

```
$ seq 100 | opy 'B:{a=0};{a+=F1};E:[a]'
5050
```

### モジュール

　モジュールの読み込み方は3通りあります。まず、リストアクションの中では、自動的にモジュールが読み込まれます。ちょっとした計算に便利なようにしました。

```
### sin 1を求める ###
$ opy 'B:[math.sin(1)]'
0.8414709848078965
### sqrt(3*3 + 4*4)の計算 ###
$ opy 'B:[numpy.hypot(3,4)]'
5.0
```

ただし、これは「PythonがNameErrorを起こしたときにモジュールの読み込みを試みる」という安直な実装で実現しています。ですので、リストの中で副作用のある計算をすると、モジュールを読み込む前にリストの中で行った計算が2度実行される可能性があります。

　もう一つは明示的にインポートする方法で、`-m`（モジュール）オプションを使う方法が簡単です。

```
$ opy -m numpy 'E:{print(numpy.pi)}'
3.141592653589793
### 二つ以上指定する時はカンマで ###
$ opy -m math,numpy 'B:[math.e,numpy.e]'
2.718281828459045 2.718281828459045
```

　最後の方法はBEGINパターンを使うものです。

```
$ opy 'B:{import numpy};E:{print(numpy.pi)}'
3.141592653589793
$ opy 'B:{import numpy as np};E:{print(np.pi)}'
3.141592653589793
### -m オプション ###
```

### スピード

　これはあまり重視していません。

### 変数のスコープ

　実装中に`exec`とか`eval`をたくさん使っていて正直把握しきれていませんが、BEGINパターンで作った変数は他のパターンでも利用できます。


### おわりに

　またいろいろ書き足らないことがありますが、とりあえずリポジトリは

* https://github.com/ryuichiueda/opy

ですので、とりあえずインストールしておいて、ここぞというときに思い出して使ってみていただければ幸いです。
