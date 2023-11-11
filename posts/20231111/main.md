---
Keywords: 日記, 自作シェル
Copyright: (C) 2023 Ryuichi Ueda
---

# 日記（2023年11月11日）

　査読ばっかりで、あまりにも査読したくなくてこれを記しております。

## シェル芸勉強会

12月16日やります！スケジュールと墓穴を開けて待っててください！たぶん都内某所です。

## Rustでクレートを使ってシグナルを非同期で受けようとするとファイル記述子を使いやがる

　最近の一番の悩みで、[ctrlc](https://crates.io/crates/ctrlc)を使っても、[signal-hook](https://crates.io/crates/signal-hook)を使っても、非同期処理でパイプやソケットを使ってしまうため、本来ユーザーのために開けておく必要のある3番や4番のファイル記述子を使ってしまいます。[シェルを作っているのに](/page=sd_rusty_bash)、そんな若い番号のファイル記述子を勝手に使ってもらっては困るんですが、ほかによい方法が見つかりません。たぶん`main`に入ってすぐに3〜9を使い潰してからスレッドを動かして、3〜9を閉じればなんとかなりそうですが、それでもユーザーの知らないファイル記述子が`/proc/$$/fd`の下に見えたら嫌なわけで、どうしようかと。Rustだとどうしてもそうしないとだめなんですかね？

　一応、[これが](https://github.com/shellgei/rusty_bash/blob/sd/202405_async/src/main.rs)連載で作っているシェルを`SIGCHLD`に非同期で反応できるようにしたバージョンへのリンクです（正確には`main.rs`へのリンクで、ここに`SIGCHLD`を待っている記述があります。）。なにかピンと来たらご一報を。

### 追記

　先人が全く同じことで悩まれておりました。後追いで似たことをしてしまっておりいつも恐縮しておりますです。

* reddish-shell v0.11.0-beta4 開発進捗 | パイプライン、バックグラウンド実行、コマンド置換の実装 | ぶていのログでぶログ: https://tech.buty4649.net/entry/2021/11/11/000845

### 追記2

　上記の「たぶん`main`に入ってすぐに3〜9を使い潰してからスレッドを動かして、3〜9を閉じればなんとかなりそうですが、」をやってみました。

```rust
44 fn run_childcare(core: &mut ShellCore) { //SIGCHLDを補足するスレッドを立ち上げる関数
45     for fd in 3..10 { // FD3〜9を使って塞いでしまう。
46         unistd::dup2(2, fd).expect("sush(fatal): init error");
47     }
48
49     let jt = Arc::clone(&core.job_table);
50     thread::spawn(move || {
51         let mut signals = Signals::new(vec![SIGCHLD])
52                           .expect("sush(fatal): cannot prepare signal data");
53
54         for fd in 3..10 { // 無限ループに入る前にFD3〜9を開放
55             unistd::close(fd).expect("sush(fatal): init error");
56         }
57
58         loop {
59             thread::sleep(time::Duration::from_secs(1));
60             for signal in signals.pending() {
61                 check_signal(signal, &jt);
62             }
63         }
64     });
65 }
```


　できました。`signal-hook`のファイル記述子が10と11になってます。
しかし、これフォークしたらまずいんじゃなかろうか。（全くの未検証です。）

```bash
🍣 ls -l /proc/112159/fd
合計 0
lrwx------ 1 ueda ueda 64 11月 11 17:13 0 -> /dev/pts/2
lrwx------ 1 ueda ueda 64 11月 11 17:13 1 -> /dev/pts/2
lrwx------ 1 ueda ueda 64 11月 11 17:13 10 -> 'socket:[1070478]'
lrwx------ 1 ueda ueda 64 11月 11 17:13 11 -> 'socket:[1070479]'
lrwx------ 1 ueda ueda 64 11月 11 17:13 2 -> /dev/pts/2
lrwx------ 1 ueda ueda 64 11月 11 17:13 255 -> /dev/pts/2
```

パイプやソケットを使うというのは、あまり良くないアイデアなんじゃないかな〜と。（でも自分で解決しようとすると大変なので、あまり強くも言えず・・・）
