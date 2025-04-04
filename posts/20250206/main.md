---
Keywords: シェル芸勉強会
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルの端末まわりで困ってる問題についてメモ書き

　最近、自作シェルで端末から字を読む際のバグと格闘しているのでメモして頭を整理します。

## 経緯

　こんなかんじ

* 自作シェルに`trap`を実装した
* プロンプトが出ている時に`trap`を受信したいが、文字入力を非同期でやっていないので無理
* [termionの非同期入力](https://docs.rs/termion/latest/termion/struct.AsyncReader.html)を使って文字入力の受付を非同期に実装しなおし
* バグ出た

## バグ

* Linuxの場合
    * Vimを立ち上げると画面がバグったり、「指定の位置にカーソルがありません」と出る。（何かキーを押すと直る）
        * たぶんVimに`ESC+[+何か文字`が飛んでる（[参考](https://mattn.kaoriya.net/software/vim/20121119204213.htm)）
* macOSの場合
    * 何かコマンドを立ち上げると`SIGTTIN`が飛んできてシェルが終わる
        * 上の`ESC+[+文字`だと思われ（なぜかコマンドにフォアグラウンドを譲ってから飛ぶ）
        * 飛ばしているのは[cursor.rs](https://github.com/redox-os/termion/blob/master/src/cursor.rs)っぽい
    * 端末のサイズを変えるとtermionの`cursor.rs`でpanicが起こる
        * エラーを見るとカーソルの位置がとれてない
    * 端末にEnterを入力し続けると`cursor.rs`でpanicが起こる
        * 同上

## 対策

　とりあえず非同期入力を当面あきらめるとして、もし粘るなら、

* なんとかして`ESC+[+文字`がバックグラウンド中に飛ばないようにする。
* シェルのプログラムのしょっぱなに`SIGTTIN`を無効に。
* カーソルの位置をむやみにtermionから取らず、自分で計算する。
* termionにコントリビューションする。（少なくともパニックにしないことはできる。）

ですかねえ・・・


本業と並行してバグを除去するにはあまりにも辛いんですが、とりあえず現場からは以上です。
