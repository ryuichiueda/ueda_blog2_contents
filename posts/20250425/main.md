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

Bashの場合、`cat改行OH`というスクリプトを標準入力から受け取ると、まず`bash`が`cat`をfork-execして実行します。そして、`cat`のプロセスが標準入力から文字を取り込むので、`cat`の出力として`OH`が出力されます。これが自作シェル（`sush`、寿司シェル）で動かない。`OH`を`sush`が読み込んで、「そんなコマンドない」と叱ってきます。お前が読み込むからあかんのだが。

　いろいろ原因を探ってたのですが、`strace`してみたら、`sush`のプロセスが入力を2行まとめて`read`してしまってました。ファイルディスクリプタの操作を間違っているんじゃないかと思ってたら、案外単純でした。

<iframe src="https://mi.shellgei.org/embed/notes/a6ypdocro0" data-misskey-embed-id="v1_88fc84a1-5fe3-4d23-a2c9-9d8e364ef8f1" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

んで、さらに調べたらRustの標準入力を1行読むやつ（`std::io::stdin().read_line()`）が勝手に何行も読んでバッファリングしてました。いや、勝手にって書きましたがちゃんと https://doc.rust-lang.org/std/io/fn.stdin.html に書いてありますごめんなさいごめんなさい。

　ということで、バッファリングしないようにしたら`sush`でもBashの挙動が再現できました。パフォーマンスはちょっと落ちるような気がしますが、パイプ自体がバッファを持ってるのにシェル側でまたバッファを持つのもなんとなく変なので、これでいいと思います。

<iframe src="https://mi.shellgei.org/embed/notes/a700zqafw3" data-misskey-embed-id="v1_f5a83526-a4d4-40b0-b6c9-9e0327f82c97" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

　ただ、Rustでバッファなしで標準入力を扱う方法がよくわからず、結局、[このクレート](https://crates.io/crates/io-streams)を使うことにしました。なんで便利でなくすためにクレートを追加せねばならぬのか分からん・・・のですが、過保護な言語にはよくある話ではあります。


## インデックスを指定した配列、連想配列の初期化

　私は絶対に使わない機能ですが、こういう書式に対応しました。配列のどこにデータを入れるか指定して配列を初期化（or 追記）する方法です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">もう47歳なんだが楽しい <a href="https://t.co/xchbtJqwVy">pic.twitter.com/xchbtJqwVy</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1915697836676755952?ref_src=twsrc%5Etfw">April 25, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

　連想配列でも動きます。私は絶対に使わないですが。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">これは微妙にBashと違う順番になるな・・・ <a href="https://t.co/kCQssTrVhd">pic.twitter.com/kCQssTrVhd</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1915699543976427971?ref_src=twsrc%5Etfw">April 25, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## その他

　`${hoge[@]/a/b}`、`${hoge[@]%%a}`など、配列の各要素を置換したり、削除したりする機能を実装し忘れていたので、実装を追加しました。また、ヒアドキュメントの実装が雑だったので少しまともにしました。現在のBashとの互換性テストはこんな感じです。前回から通ったテストスクリプトの数が$7$から$14$に倍増しました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ここ数日実装漏れとかI/O関係の不備とかが次々と見つかって、Bashとの互換性テストの結果が一気に14/85（16%）まで向上しました <a href="https://twitter.com/hashtag/%E8%87%AA%E4%BD%9C%E3%82%B7%E3%82%A7%E3%83%AB?src=hash&amp;ref_src=twsrc%5Etfw">#自作シェル</a> <a href="https://twitter.com/hashtag/bash?src=hash&amp;ref_src=twsrc%5Etfw">#bash</a><a href="https://t.co/EmMlWYpeqi">https://t.co/EmMlWYpeqi</a> <a href="https://t.co/CYtO9eVA4s">pic.twitter.com/CYtO9eVA4s</a></p>&mdash; 上田隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1915670184528142632?ref_src=twsrc%5Etfw">April 25, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


ということで、地道にBashに近づけてますので、もしよろしければ応援お願いいたします。


現場からは以上です。

