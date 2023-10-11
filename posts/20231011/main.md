---
Keywords: シェル, bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# リダイレクトのエラーの謎3

　Bashのリダイレクト記号の左側の数字は、32bit符号付き整数の値以内ならファイル記述子、それを超えるとコマンドの引数として扱われるっぽいです・・・。

```bash
$ echo $BASH_VERSION
5.1.16(1)-release
### これはファイル記述子扱い ###
$ echo 2147483647>aaaa
bash: 2147483647: 不正なファイル記述子です 
### これはechoの引数扱い ###
$ echo 2147483648>aaaa
$ cat aaaa
2147483648
```

えええ・・・
