---
Keywords: ||,シェルスクリプト,&&,bash,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# シェルの&&||パズル（解答編）
この前、<a href="/?post=01094" title="シェルの&&||パズル" target="_blank">ここ</a>で、次の四つのコマンド列の出力を当てるクイズを無責任に出題しましたが、ちゃんと真面目に解答します。

```bash
$ false && true || true && echo OK <- 1
$ true && true || false || echo OK <- 2
$ true || true || true && echo OK <- 3
$ false && true || false || echo OK <- 4
```

<h2>考え方</h2>

シェルも一応言語ですが、基本、コマンドを起動するための道具なので、上から下、左から右に順にコマンドを起動していきます。それで、「&&」も「||」も、<strong style="color:red">左のコマンドの終了ステータスによって、右のコマンドを起動するかどうか決める</strong>ものですので、右側のコマンドが起動されるかどうかをまず考えます。例えば１の問題だと、最初の二つのコマンドは、falseが起動されてtrueが起動されません。

```bash
$ false (<-起動される) && true (<- 起動されない) || true && echo OK 
```

次に考えなければいけないのは、&&や||が見ている終了ステータスは、<strong style="color:red">最後に起動したコマンドの終了ステータス</strong>だということです。ですから、１の問題では、次のように解釈できます。ですので、|| true のtrueは実行され、その次のecho も実行されます。

```bash
$ false (<-起動される) && true (<- 起動されない) || (<- falseの終了ステータス) true && echo OK 
```

これをおさえて左から右に慎重に考えて行けば、答えは特定できるかと思います。

```bash
$ false && true || true && echo OK
OK
$ true && true || false || echo OK
$ true || true || true && echo OK
OK
$ false && true || false || echo OK
OK
```

<strong style="color:red">しかし、可読性に重大な問題が発生するので、ぜひ使わないようにしていただきたく。</strong>


おしまい。
