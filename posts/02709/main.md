---
Keywords: コマンド,flock,Linux,排他処理
Copyright: (C) 2017 Ryuichi Ueda
---

# 排他を実現するコマンドflock(1)の使い方メモ
排他をかけるコマンドです。Ubuntuので試しました。

まず、排他区間を設けて処理したい内容をシェルスクリプトにします。ここでは、ひたすらプロセス番号をhogeというファイルに書き続けるシェルスクリプトchild.bashを準備しました。
```bash
ueda@remote:~$ cat child.bash 
#!/bin/bash

for i in {1..10000} ; do
	echo $$ >> hoge 
done
```

<!--more-->

次に、child.bashを同時に何本も走らすシェルスクリプトparent.bashを次のように準備します。100個並列で走らせます。flockの使い方ですが、最初に鍵となるファイル（これはディレクトリでもよい）を適当に指定して、その次に実行したいコマンド（スクリプトやその他プログラム）を指定します。
```bash
ueda@remote:~$ cat parent.bash 
#!/bin/bash

for i in {1..100} ; do
	flock /home/ueda/lock ./child.bash &
done
```

で、実行。無慈悲な攻撃をUbuntuに食らわせます。
```bash
ueda@remote:~$ ./parent.bash 
ueda@remote:~$ 
```

できたファイルhogeを見てみましょう。プロセス番号が入れ違いになってたら排他失敗となりますが・・・。
```bash
###プロセス番号が順番になっている###
ueda@remote:~$ uniq hoge | head
27465
27538
27547
27562
27565
27568
27569
27570
27571
27572
###（プロセス番号が一周しなければ）ちゃんと順番になっていることがsort -cで分かる###
ueda@remote:~$ cat hoge | sort 
c-ueda@remote:~$ echo $?
0
```
なんかうまくいってます。プロセス番号が順番になるのは、鍵の取れたchild.bashのプロセスから順番にプロセス番号をもらっていくからでしょう。

次に、もっと無慈悲なchild.bashを用意しました。echoに&をつけて、hogeへの書き込みを非同期にします。
```bash
ueda@remote:~$ cat child.bash 
#!/bin/bash

for i in {1..10000} ; do
	echo $$ >> hoge & 
done
```
hogeを一度消去して再実行！
```bash
ueda@remote:~$ ./parent.bash 
###この場合はプロセス番号が何周もするので、一度uniqをかけてからソートして重複チェックを行う。###
###ただ、運が悪いと別のプロセスのchild.bashに同じプロセスIDが渡る。###
ueda@remote:~$ cat hoge | uniq | sort | sort 
c-ueda@remote:~$
```
これもうまくいったようです。

ちなみにflockの部分を除くとこうなります。
```bash
ueda@remote:~$ sort -c hoge
sort: hoge:9680: 順序が不規則: 4507
```
が、<span style="color:red">この後、プロセスの立ち上げ過ぎでUbuntuがしばらく気絶しましたとさ。</span>


それはさておき、flock便利だ・・・。
