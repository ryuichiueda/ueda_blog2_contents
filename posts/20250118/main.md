---
Keywords: 日記
Copyright: (C) 2024 Ryuichi Ueda
---

# 日記（2025年1月18日）

　1月は期末の発表＆卒論シーズンなので各学年のポスターやスライド、卒論、修論の添削の毎日です。で、これはとても疲れる（<span style="color:red">まだ一人前とは言えない文章を精読して、様々な感情を抑えて、本人にとってためになるアドバイスをする~~という地獄のような~~</span>）作業なので、合間に現実逃避するようにコードを組んでます。んで、コード書くだけなのでリリースしたり作業記録をつけたりする作業がすべて後回しになってるのでメモしときます。

## 学会で発表した動く物体の位置予測アルゴリズムのROS 2移植

　↓このときに発表したアルゴリズムをROS 2で使えるようにしています。ロボットから見えてるものが数秒後にどこにいくか予測するアルゴリズムです。[写真中でモザイクかかってるポスターはこちらで公開中](https://www.docswell.com/s/ryuichiueda/ZEX11D-si2024)。


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">えーとですね、初心者すぎてポスター貼るところを間違えてて、本当の持ち主の方が貼り直してくださいました。<br><br>大変申し訳ございませんでした・・・ <a href="https://t.co/eelpATwUM6">https://t.co/eelpATwUM6</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1869205420386193502?ref_src=twsrc%5Etfw">December 18, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

C++で画像ファイルを読み込んで画像ファイルを出力するコマンドとして作っていたのを、[RustでROS 2のパッケージとして](https://github.com/ryuichiueda/ogm_flow_estimator_static)実装しなおしています。

READMEを作っていますが、まだちょっと直すのでついった上ではできたといってません。また、いまのところロボットが静止していることを前提にして作っています。ロボットが動けるものは別のパッケージにしようと思います。現状、出力はこんな感じ↓です。2〜10秒後に移動しているものがいそうな位置の分布がグレースケールで表示されています。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">仮想マシンの機嫌で計算時間が1msになったり10msになったりするけどたぶん1msで計算できとる <a href="https://t.co/1zogabgCtc">https://t.co/1zogabgCtc</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1879829299538297237?ref_src=twsrc%5Etfw">January 16, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

これでも歩いてる人に雪玉投げるときの目標位置の計算くらいには使えるような気がします。（ダメです。）

## 自作シェル

　自作シェルのほうは、年末辺りからBashのヘビー級補完機能パッケージの[bash-completion](https://heartbeats.jp/hbblog/2013/06/bash-completion.html)を動かそうと格闘中してました。この作業は遅いながらも少しずつ進んでいます。bash-completionはニッチな機能を使いまくってるシェルスクリプトの塊なので、ニッチな機能を少しずつ実装して動作確認しながら作業を進めています。

　もうひとつの作業として、エラーハンドリングをちゃんとしようということで、いままでboolで成否を返していたのをRustのResult型を真面目に使うように変更中です。例として、

```bash
$ ( echo abc ; echo def ) | rev
cba
fed
```

のような`()`で複数のコマンドをまとめるサブシェルをパースする関数を図1に示します。Resultを使う前は、図1のように、カッコの中身に文法エラーがあったら「`None`」を返すだけでしたが、これだと中身にどんなエラーがあったかまでは返せません。そのため、このコードの場合は`eat_inner_script`のなか（あるいはさらにそこから呼ばれている関数）でエラー処理せざるを得ず、エラー処理のコードが散らばってました。


* 図1: Result使う前（説明に不要な部分はカット）

```rust
//Result使ってないやつ
pub fn parse(feeder: &mut Feeder, core: &mut ShellCore, substitution: bool) -> Option<Self> {
    let mut ans = Self::default();
    if command::eat_inner_script(feeder, core, "(", vec![")"], &mut ans.script, substitution) { //カッコの中身を取り出す関数
        Some(ans) //中身に文法エラーがなかったら、パース結果をなにかあったという印のSomeにくるんで返す。
    }else{
        None //エラーがあったら「何もない」を返す。
    }
}
```

　これを図2のように関数の戻り値の型を変えました。元々の型`Option`は、結果（`ans`）がある場合に`Some(結果)`、ない場合に`None`を返す型ですが、それをさらに`Result`でくるんで、次の値を返すように変えています。`eat_inner_script`の戻り値の型も`Result`を使うように書き換えてあります。

* カッコの中身に文法エラーがない: `Ok(Some(ans))`
* カッコの中身に文法エラーがある: `Err(エラーの原因)`
* カッコの中身に文法エラーがないけど`eat_inner_script`が`None`（正確には`Ok(None)`）を返してきた: `Ok(None)`

これで、エラーがこのパースの関数の呼び出し元に伝わるようになります。コードについてはそんなに変更点がなく、返り値を`Ok`でくるみ、さらに`eat_inner_script`関数の呼び出しのうしろに`?`をつけるだけです。`?`があると、関数が`Err(...)`を返してきたときに、即座に関数が終わって`Err(...)`が返るようになります。`Ok(...)`の場合は`Ok`を剥がしてくれます。便利です。

* 図2: Result使った後

```rust
//Result使ったやつ
pub fn parse(feeder: &mut Feeder, core: &mut ShellCore, substitution: bool) -> Result<Option<Self>, ParseError> {
    let mut ans = Self::default();                                            //↑Result型の導入
    if command::eat_inner_script(feeder, core, "(", vec![")"], &mut ans.script, substitution)? { //?をつける
        Ok(Some(ans)) //Okで囲む
    }else{
        Ok(None) //Okで囲む
    }
}
```

　ただ、「コードについてはそんなに変更点がなく」と書きましたが、パーサーを構成する全部の関数の型を変更して、かつ整合性があるようにコードを書き換えなければならなかったので地獄でした。でしたというか継続中です。話がややこしくなると思って連載当初に使うのを躊躇したのを後悔してます。

　連載については、たぶん6月号あたりから`?`を使ったコードに移行すると思われます。


とりあえず現場からは以上です。
