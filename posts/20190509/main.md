---
Keywords: AWK
Copyright: (C) 2019 Ryuichi Ueda
---

# `%`の入った文字列をawkで`printf $0`するとエラーに

　知ってる人は知ってることだと思いますが、10年AWKを使ってきて見落としていた仕様があり、あまり検索しても解説が引っかからなかったのでメモします。結論から言うと、どんな文字列が標準入力やファイルから来るか分からないときは、AWKでは`printf $0`と書かないで`printf("%s",$0)`とちゃんと書かないとエラーになることがあります。

## 例

　次のように、標準入力から読み込んだ`%`をフォーマット指定子を間違えて、指定子があるのに対象の文字列がないと叱られます。


* one true awkの場合

```
$ /usr/bin/awk --version
awk version 20070501
uedambp2:20190509 ueda$ echo 'aa%aa' | /usr/bin/awk '{printf $0}'
/usr/bin/awk: weird printf conversion %a
 input record number 1, file
 source line number 1
/usr/bin/awk: not enough args in printf(aa%aa)
 input record number 1, file
 source line number 1
```

* GNU Awkの場合

```
$ gawk --version
GNU Awk 5.0.0, API: 2.0 (GNU MPFR 4.0.2, GNU MP 6.1.2)
Copyright (C) 1989, 1991-2019 Free Software Foundation.
（略）
$ echo 'aa%aa' | gawk '{printf $0}'
gawk: コマンドライン:1: (FILENAME=- FNR=1) 致命的: 書式文字列を満たす十分な数の引数がありません
	`aa%aa'
	   ^ ここから足りません
```

## 対策

　めんどくさがらずに`printf("%s",$0)`と書く。

```
$ echo 'aa%aa' | /usr/bin/awk '{printf("%s\n",$0)}'
aa%aa
$ echo 'aa%aa' | gawk '{printf("%s\n",$0)}'
aa%aa
```

現場からは以上です。
