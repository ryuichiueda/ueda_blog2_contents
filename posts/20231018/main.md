---
Keywords: 自作シェル, bash, 連載
Copyright: (C) 2023 Ryuichi Ueda
---

# 【ごめんなさい】連載の実装漏れとバグ

　連載[「魅惑の自作シェルの世界」](/?page=sd_rusty_bash)では、自作シェルのコードを書く手順を説明しながらシェルの仕組みを説明していますが、このスタイルだとどうしてもバグがまざってしまいます。で、それは覚悟でやっており、読者さんから報告があるとうれしいなとまで考えておりますが、それを超えるやらかしをやってしまいましたので報告いたします。あと、もうひとつバグを見つけたのでそれも報告しますので、報告事項は2点です。

## パイプライン処理の実装漏れ

　で、やらかしですが、2023年8月号の最後で、パイプラインが動作するか検証していますが、実はこのパイプラインは動いても、データが大きいとうまく動きません。[コマンドを実行している部分](https://github.com/shellgei/rusty_bash/blob/eea4e06473f9caf1a09be7428f53393007972cbc/src/elements/command/simple.rs#L21C1-L52C6)を見ると、次のように、子のプロセスで実行しているコマンドを、親のプロセスが待つというコードになっています。


```rust
fn exec(&mut self, core: &mut ShellCore, pipe: &mut PipeRecipe) {
    if core.run_builtin(&mut self.args) {
        return;
    }

    self.set_cargs();
    match unsafe{unistd::fork()} { //子のプロセス
        Ok(ForkResult::Child) => {
	   （コマンドを実行）
        },
        Ok(ForkResult::Parent { child } ) => { //親のプロセス
            pipe.parent_close();
            core.wait_process(child); //ここでコマンドの終了を待っているけどこれでは駄目
        },
        Err(err) => panic!("Failed to fork. {}", err),
    }
}
```

この書き方だと、今実行しているコマンドが終わらないとパイプラインにある次のコマンドが立ち上がりません。したがって、今実行しているコマンドが、パイプにバッファを超える量のデータを通そうとすると、次のコマンドがデータを読むのを待ってしまって、デッドロックが起こります。

　で、どうするかというところですが、いま連載中で実装しているリダイレクトが一旦おわったところで、改めて実装を説明します。待てない人には、[11月号のコードに対応策を施したブランチ](https://github.com/shellgei/rusty_bash/tree/sd/202311_pipe_fix)を作ったので、それで動作確認してみてください。`seq 10000000000 | rev`を実行すると、対策前のパイプラインは止まって、対策後のパイプラインは問題なく実行されます。
