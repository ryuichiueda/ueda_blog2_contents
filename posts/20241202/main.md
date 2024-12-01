---
Keywords: sush, 自作シェル, 寿司シェル
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルの進捗

　自作シェル（寿司シェル）について以前ブログに書いたのが8月18日で、それ以降なんも書いてなかったのでまとめます。ふつう、こういうのは開発日記とか書いて読んでもらうもんじゃないのか・・・

## 7月〜10月まで

　10月までの進捗については10/26にシェル芸勉強会で話をしました。動画が残ってます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/97ROIIjrVuQ?si=9FBd58w107kmIyEK&amp;start=152" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## それ以降

　[リリースノート](https://github.com/shellgei/rusty_bash/releases)を見ると、こんな感じです（忘れてる）。


* v0.8.7: 動画にもありましたがcommand-not-found（インストールされていないコマンドを打つとインストール方法を教えてくれるアレ）が動くようになりました。
* v0.8.9: Bashで変数として実装されているRANDOMが寿司シェルでも使えるようになりました。
    * [きゃろさん](https://mi.shellgei.org/@caro)が実装してくださいました大感謝。たぶんBashよりも質の高い乱数になってるような気がします。
* v0.8.10: 変数の値の削除機能を実装
    * `${name/pattern/word}, ${name//pattern/word}, ${name/#pattern/word}, ${name/%pattern/word}`のことです。
* v0.8.11: `$@`に対して`$@[1]`などと要素を参照しようとしたらエラーが出るようにするという地味な改修をしました。
* v0.9.0: シェルスクリプトを読み込んで実行するときに、シェルスクリプトを標準入力から読んでしまっており、そのシェルスクリプトが標準入力を使えなくなるというクソ仕様にしてしまっていたので直しました。
* v0.9.2: 次の2点の実装をしました。
    * 変数`SECONDS, EPOCHSECONDS, EPOCHREALTIME`（きゃろさんによる）
    * グロブ（ワイルドカード）での`[0-9], [a-z], [A-Z]`などの範囲指定
* v0.9.4: `continue`コマンドを実装しました。

## 今後

　現在、Bashの標準の補完機能のプログラムbash-completionが動くことを目指しています。bash-completionを使うには3000行くらいの複雑なシェルスクリプト（結構激しい）を読み込む必要がありますが、とりあえず現在はパースできる状態になっており、パース後のプログラムが全部動くように細かい実装を加えている途中です。

　その一環として、リリースノートには書いていませんが、`[[ ]]`コマンドにおいて正規表現が使えるようにしたり、`complete`コマンドや`compgen`コマンドに機能追加しています。

　いまでも自分自身は自作シェルを普段使っていますが、やはり不満なのは補完機能が弱いことで、これではあんまり人に勧められんなと思っています。ということで、正月にはbash-completionが動くようにしたいなと考えています。


現場からは以上です。
