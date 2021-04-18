---
Keywords: glueutils, GlueLang
Copyright: (C) 2021 Ryuichi Ueda
---

# glueutilsについて

この前から[glueutils](https://github.com/ryuichiueda/glueutils)という怪しげなコマンドパッケージを作っているのですが、解説を書いておこうと思います。

## なにをするパッケージか

標準入出力のリダイレクトなど、シェルでやるような処理をコマンドだけで可能にするためのパッケージ群です。

## なにが嬉しいか

* リダイレクト処理が貧弱なシェル（私の作ってる[GlueLang](/?page=GlueLang)など）でもリダイレクトが可能（もともとこの用途で作成してます。）
* シェルで`2>&1`とか`> /dev/null`とかリダイレクトを書くとゴチャゴチャするので、ゴチャゴチャしない方法を提供


## 使用例

コマンドは、いまのところ次のようなものがあります。

|コマンド|働き|
|:----|:----|
|flip12|標準出力と標準エラー出力を入れ替え|
|log2|標準エラー出力をファイルにリダイレクト|
|ign1|標準出力を`/dev/null`へ|
|ign2|標準エラー出力を`/dev/null`へ|
|ign12|標準出力、標準エラー出力を`/dev/null`へ|
|ignerr|終了ステータスを無視|

これらのコマンドに、引数として任意のコマンドを指定して使います。


### 例1: 標準出力を無視

`diff`の出力を捨てて終了ステータスだけ取る。

```
$ ign1 diff /etc/passwd /etc/group
$ echo $?
1
```

### 例2: `diff`の終了ステータスを無視

シェルで`-e`オプション（エラーが起こると止める）などを設定したときに止まらないようにできます。

```
$ ignerr diff /etc/passwd /etc/group > file
$ echo $?
0
### ignerrを使わない場合 ###
$ diff /etc/passwd /etc/group > file || true
$ echo $?
0
```

### 例3: 標準エラー出力をファイルに保存

`strace`と併用した例です。

```
$ log2 hoge strace ls /
bin  boot  cdrom  dev  etc  home  lib  lib32  lib64  ...
$ head -n 3 hoge
execve("/usr/bin/ls", ["ls"], 0x7fffde6beab0 /* 49 vars */) = 0
brk(NULL)                               = 0x5608bdf34000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffd2f7fa770) = -1 EINVAL (無効な引数です)
```



