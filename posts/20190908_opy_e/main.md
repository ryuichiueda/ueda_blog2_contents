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
$ seq 3 | awk '{print $1*3}'  # triple the number of the field one and output
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

  However, Python has the list data type. Then AWK also treats fields of each line as elements of a list. So I thought the action of AWK can be replaced to the list of Python.

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

When there are more than one elements in the list, the elements are joined with spaces.

```
$ seq 3 | opy 'F1%2:["%d:odd"%F1, F1*3]'
1:odd 3
3:odd 9
```

  `Opy` also has a normal action mode. When we use it, we need to put sentences in curly brackets. 


```
$ seq 3 | opy '{print(F1, end="")}'
123
```


### grammer

  Over the Python grammer, I defined `rule`. 


```
<rules> ::= <rule> | <rule> ";" <rules>
<rule> ::= <pattern> | <pattern> ":" <action> | <action>
<action> ::= <list action> | <normal action>
<pattern> ::= <boolean expression of Python> | "B" | "BEGIN" | "E" | "END" 
<normal action> ::= "{" <sentences of Python> "}"
<list action> ::= <a list of Python>
```

  `B, BEGIN, E` and `END` means the begin/end patterns, which are also seen in AWK. We can use BEGIN pattern for initialization and the other for post-processing. This is an example. 


```
$ seq 100 | opy 'B:{a=0};{a+=F1};E:[a]'
5050
```

### module

  We can use any modules in `opy`. There are three kinds of ways for import of modules. In a list action, modules are imported automatically. 

```
### obtaining the number of sin 1 ###
$ opy 'B:[math.sin(1)]'
0.8414709848078965
### calculation of sqrt(3*3 + 4*4) ###
$ opy 'B:[numpy.hypot(3,4)]'
5.0
```

Though it is crude implemntation, the module is imported when an NameError occurs. After that, `opy` evaluates the list again. Therefore, we must not write any procedure that has side effects in the list. Otherwise, a procedure runs twice. 

  We can import modules more safely with `-m` option.

```
$ opy -m numpy 'E:{print(numpy.pi)}'
3.141592653589793
### join module names with commas for multiple module import ###
$ opy -m math,numpy 'B:[math.e,numpy.e]'
2.718281828459045 2.718281828459045
```

　We can also use a begin pattern.

```
$ opy 'B:{import numpy};E:{print(numpy.pi)}'
3.141592653589793
$ opy 'B:{import numpy as np};E:{print(np.pi)}'
3.141592653589793
### -m オプション ###
```

### computational speed

  I put less importance on computational speed than convenience.


### repository

* https://github.com/ryuichiueda/opy



