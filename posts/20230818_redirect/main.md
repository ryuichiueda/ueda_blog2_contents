---
Keywords: シェル芸, 自作シェル, bash
Copyright: (C) 2023 Ryuichi Ueda
---

# ビルトインコマンドをリダイレクトしてもフォークしない（そんなこと知らなかったよ・・・）

　[昨日](/?post=20230817_redirect)に引き続き[連載](/?page=sd_rusty_bash)のためにリダイレクトについてBashの重箱の隅を突っついて遊んでいますが、今日も発見しました。知ってる人は知ってるのかもしれませんが、知らなかった私は知らなかったです。（懺悔）

## 現象

　とりあえず事実を書いておくと、Bashでは`cd -`の出力をファイルにリダイレクトすると、`cd -`で前にいたディレクトリに移動でき、ファイルの中にも`cd -`の出力（移動先のディレクトリ）が記録されます。

```bash
ueda@uedap1:/tmp$ echo $BASH_VERSION
5.1.16(1)-release
ueda@uedap1:/tmp$ cd - > tmp
ueda@uedap1:~$ pwd 
/home/ueda                    # 元いたディレクトリ（この場合はホーム）に移動できる
ueda@uedap1:~$ cat /tmp/tmp   # リダイレクト先の/tmp/tmpには
/home/ueda                    # 移動後のディレクトリが記録される
```

ということは、`cd`はこのBashのプロセスで動いていることになります。

　それがどうしたというところですが、これがパイプだと挙動が変わります。
次のように、`cd`が子のプロセスで動作するので、ディレクトリを移動できません。

```bash
ueda@uedap1:~$ cd - | cat #cd -で元のディレクトリ（この場合は/tmp）に移動しようとする
/tmp                      #パイプを通って移動先のディレクトリが出力される
ueda@uedap1:~$ pwd        #けど
/home/ueda                #移動はできない（cdが子のプロセスで実行されるので）
```

## リダイレクトはどう実現されているのか？

　で、パイプなら必ずコマンドをフォークしてから、子のプロセスでファイル記述子を操作をするわけで、リダイレクトもそうしたほうが実装が楽なのですが、`cd - > tmp`の場合はフォークしません。どう実装されているのか気になります。
Bashのコードを読むのが一番いいのですが大変なので、`strace`で当該部分を見てみました。
次のように、プロセスをフォークせずに、ファイル記述子をやりくりしてリダイレクトしていることが分かりました。

```bash
$ strace -f bash -c 'cd - > tmp' &> b
$ cat b
・・・
openat(AT_FDCWD, "tmp", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3  #tmpファイルを作成（fd: 3)
fcntl(1, F_GETFD)                       = 0
fcntl(1, F_DUPFD, 10)                   = 10                 #標準出力の情報をfd10にバックアップ
fcntl(1, F_GETFD)                       = 0
fcntl(10, F_SETFD, FD_CLOEXEC)          = 0
dup2(3, 1)                              = 1                  #標準出力をファイルにつなげる
close(3)                                = 0
newfstatat(AT_FDCWD, "/home", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/ueda", {st_mode=S_IFDIR|0750, st_size=4096, ...}, 0) = 0
chdir("/home/ueda")                     = 0
newfstatat(1, "", {st_mode=S_IFREG|0664, st_size=0, ...}, AT_EMPTY_PATH) = 0
write(1, "/home/ueda\n", 11)            = 11
dup2(10, 1)                             = 1                  #fd10の情報を1に戻して復旧
fcntl(10, F_GETFD)                      = 0x1 (flags FD_CLOEXEC)
close(10)                               = 0                  #fd10を閉じる
・・・
```

## おわりに

　そんなこと知らんかったよ・・・ていうか自作シェルにこれ実装しなければならなくなりました・・・
