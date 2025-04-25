---
Keywords: 自作シェル,rusty_bash,寿司シェル
Copyright: (C) 2025 Ryuichi Ueda
---

# 自作シェルの進捗（2025年4月25日）

　[前回](/?post=20250415)（4月15日）からの進捗。

## スクリプトと`read`の読み込みをバッファなしにする

　さっき取ったバグなんですが、こういう挙動の違いの差に悩んでました。

<iframe src="https://mi.shellgei.org/embed/notes/a6ym2hqylv" data-misskey-embed-id="v1_f27588c9-ce9f-40cb-a4a4-78e32995f587" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

Bashの場合、`cat改行OH`というスクリプトを標準入力から受け取ると、まず`bash`が`cat`をfork-execして実行します。そして、`cat`のプロセスが標準入力から文字を取り込むので、`cat`の出力として`OH`が出力されます。これが自作シェル（`sush`、寿司シェル）で動かない。

　いろいろ原因を探ってたのですが、結局`strace`してみたら、`sush`のプロセスが入力を2行まとめて`read`してしまってました。

<iframe src="https://mi.shellgei.org/embed/notes/a6ypdocro0" data-misskey-embed-id="v1_88fc84a1-5fe3-4d23-a2c9-9d8e364ef8f1" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

Rustの標準入力を1行読むやつ（`std::io::stdin().read_line()`）が勝手に何行も読んでバッファリングしてました。いや、勝手にって書きましたがちゃんと https://doc.rust-lang.org/std/io/fn.stdin.html に書いてありますごめんなさいごめんなさい。

　ということで、バッファしないようにしたら`sush`でもBashの挙動が再現できました。

<iframe src="https://mi.shellgei.org/embed/notes/a700zqafw3" data-misskey-embed-id="v1_f5a83526-a4d4-40b0-b6c9-9e0327f82c97" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

　ただ、Rustでバッファなしで標準入力を扱う方法がよくわからず、結局、[このクレート](https://crates.io/crates/io-streams)を使うことにしました。なんで便利でなくすためにクレートを追加せねばならぬのか分からん・・・のですが、過保護な言語にはよくある話ではあります。
