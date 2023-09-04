---
Keywords: Bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# Bashのリダイレクト（ニッチなもの含む）に関するメモ

　連載のための調べものです。

## 矢印の種類

| 種類             | 文字                     |
|:-----------------|:-------------------------|
| >, < | 書き出し/読み込み |
| >>, << | ファイルへの追記/ヒアドキュメント |
| <<< | ヒアストリング |
| <> | 読み書き |
| `>|` | -Cオプションが設定されているときにファイルを上書き |

### <>の使い方

[シェル・ワンライナー160本ノック](https://amzn.to/3P0UxaS)に、次のような利用例が示されている。

```bash
$ exec 3<> /dev/tcp/f.ueda.tech/80        #このBashのプロセスのFD3を読み書きモードで開く
$ echo -ne "GET /eki/ HTTP/1.0\\n\\n" >&3 # http://f.ueda.techにリクエストを送信
$ cat <&3                                 #送られてきたデータを表示
HTTP/1.1 200 OK
Server: nginx/1.19.6
（略）
<!DOCTYPE html>
（略。HTMLのデータが出力される）
```

## &の使い方

| 用法             | 文字                     | 例 |
|:-----------------|:-------------------------|-----|
| &n | n番のファイル記述子を指定 | >&2, >>&2, <&4 |
| &>ファイル名 | 標準出力と標準エラー出力をとりまとめてファイルへ出力 | `ls /etc/hostname jfoaoiae &>file` |
| >&ファイル名 | 上の`&>ファイル名`と同じだが非推奨 | |

### `<&n`の使い方

```
$ rev 9<<<abc <&9
cba
```

## -の使い方

| 用法             | 文字                     | 例 |
|:-----------------|:-------------------------|-----|
| n<&-, n>&- | n番のファイル記述子を閉じる | `>&-` |
| <<- | ヒアドキュメントで$のついた変数等を展開しない | |

### ファイル記述子を閉じる例

```bash
$ exec 9</etc/hostname
$ cat /dev/fd/9
uedap1
$ exec 9<&-
$ cat /dev/fd/9
cat: /dev/fd/9: そのようなファイルやディレクトリはありません
```

## {varname}の使い方

| 用法             | 文字                     |
|:-----------------|:-------------------------|
| {hoge}<file, {hoge}>file | fileにファイル記述子を与えてhogeにその番号を格納 |

### どういうこと？

* 既存のファイルに入力用のFD割当

```bash
$ exec {hoge}</etc/hostname #bashのプロセスで/etc/hostnameにFD割当て
$ echo $hoge                #hogeに番号が入る
13
$ cat /dev/fd/$hoge         #使ってみる
uedap1
$ exec {hoge}<&-            #閉じる
$ cat /dev/fd/$hoge
cat: /dev/fd/13: そのようなファイルやディレクトリはありません
```

* 出力用のファイルにFD割当

```bash
$ exec {fuge}>~/file  #~/fileというファイルにFD割当
$ echo $fuge          #fugeにFDが入る
13
$ echo aaaa >&$fuge  #FD使う
$ cat ~/file         #ファイルに字が入る
aaaa
```

* https://mi.shellgei.org/notes/9h0kg95jdv

参考: https://unix.stackexchange.com/questions/70963/difference-between-2-2-dev-null-dev-null-and-dev-null-21

## リダイレクト用疑似ファイル

| 種類             | 指している対象           |
|:-----------------|:-------------------------|
| /dev/fd/fd       | ファイルディスクリプタ   |
| /dev/stdin       | 標準入力                 |
| /dev/stdout      | 標準出力                 |
| /dev/stderr      | 標準エラー出力           |
| /dev/tcp/host/port | ネット上のポート番号（TCP）   | 
| /dev/udp/host/port | ネット上のポート番号（UDP）   | 

