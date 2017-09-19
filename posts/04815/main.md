---
Keywords: GlueLang,Haskell,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangをHaskell化していこうと
<a href="http://blog.ueda.asia/?p=4798" title="パイプラインを実装できた" target="_blank">昨日のGlueLangへのパイプライン実装</a>ですが、実装後、パイプは「>>=」で書いたほうが良いんじゃないかという行き当たりばったりなアイデアを思いついたので、やってみました。


これがサンプルスクリプトです。
[hs]
uedambp:TEST ueda$ cat pipeline_mac4.glue 
/usr/bin/seq '1' '5' &gt;&gt;=
/usr/bin/tail '-r' &gt;&gt;=
/usr/bin/tr '\\n' ' ' &gt;&gt;=
/usr/local/bin/awk '{print}'
###実行###
uedambp:TEST ueda$ ../main pipeline_mac4.glue 
5 4 3 2 1 
[/hs]

<span style="color:red">うん、「, . 」よりも見やすい（主観）。</span>

ということで、READMEのサンプルコードも次のように書き直しました。Haskellもどきです。<a href="https://github.com/ryuichiueda/GlueLang#gluelang" target="_blank">READMEはGitHub</a>で読めます。READMEには、コンパイルして試す方法も追記しましたので、ちょっと試していただけたらと。

[hs]
import /bin/ as b
import /usr/bin/ as ub

main infile = do
 file tmp = cattac infile 
 b.cat tmp

cattac file = b.cat file &gt;&gt;= ub.tail '-r'
[/hs]

型の考え方も、テーブルの列数とかちょっとしたデータの縛りを作るのに利用できそうです。

Haskell風にしたことで数学のコワイお兄さんたちにトラップされそうですが、やっぱりシェルスクリプトは関数型だという持論を表現しやすいので、こっちの方向で開発を進めます。

