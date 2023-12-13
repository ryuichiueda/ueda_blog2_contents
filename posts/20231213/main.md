---
Keywords: Rust, thread, fork
Copyright: (C) 2023 Ryuichi Ueda
---

# RustでスレッドがMutexのロックをかけた状態でプロセスがフォークしたら？

・・・子のプロセスでロックが外れるのかどうか実験してみました。もう少し詳しく書くと、こういう実験です。

* 実験の内容
    * あるプログラムでサブのスレッドをひとつ作って、ある変数に対してロックをかけっぱなしにする（もとのスレッドは「メインのスレッド」と呼びましょう。）
    * メインのスレッドでフォークをかける
        * このとき、子のプロセスでサブのスレッドは止まる（[参考](https://amzn.to/3NkC0X2)） 
* <span style="color:red">疑念: 子のサブのスレッドがロックをかけたまま止まるので、子でロックが外れないのではないか？</span>

## 先に結論

下記の実験の結果を見ると、ロックは外れるみたいです。（コードを解読すれば完璧ですが、それはまだです。）


## 実験

### 使ったコード

こんな感じ。[リポジトリはここです](https://github.com/ryuichiueda/thread_fork/blob/main/src/main.rs)。8行目でArc（参照カウンタ）とMutex（排他制御のための型）にくるんだ文字列をひとつ作って、これを

* サブのスレッド
* 親のメインスレッド
* 子のメインスレッド

で読み書きしています。サブのスレッドが5秒間ロックをかけたあと、おもむろに`written`と書き込みます。嫌がらせです。メインスレッドの親子は、この嫌がらせが終わるまで、文字列を読み書きできなくなります。

<script src="https://gist.github.com/ryuichiueda/a05823182d1a0c8f09fb44ceaf3ad8ad.js"></script>


### コードの実行結果

```text
$ cargo run
・・・
1秒後 Child: ""  #親が
2秒後 Child: ""
3秒後 Child: ""
4秒後 Child: ""
5秒後 Parent { child: Pid(50794) }: "written"
5秒後 Child: ""
6秒後 Parent { child: Pid(50794) }: "written"
6秒後 Child: ""
・・・
```

