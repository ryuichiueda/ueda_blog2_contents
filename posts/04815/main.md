---
Keywords: GlueLang,Haskell,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangをHaskell化していこうと
<a href="http://blog.ueda.asia/?p=4798" title="パイプラインを実装できた" target="_blank">昨日のGlueLangへのパイプライン実装</a>ですが、実装後、パイプは「>>=」で書いたほうが良いんじゃないかという行き当たりばったりなアイデアを思いついたので、やってみました。<br />
<br />
<br />
これがサンプルスクリプトです。<br />
[hs]<br />
uedambp:TEST ueda$ cat pipeline_mac4.glue <br />
/usr/bin/seq '1' '5' &gt;&gt;=<br />
/usr/bin/tail '-r' &gt;&gt;=<br />
/usr/bin/tr '\\n' ' ' &gt;&gt;=<br />
/usr/local/bin/awk '{print}'<br />
###実行###<br />
uedambp:TEST ueda$ ../main pipeline_mac4.glue <br />
5 4 3 2 1 <br />
[/hs]<br />
<br />
<span style="color:red">うん、「, . 」よりも見やすい（主観）。</span><br />
<br />
ということで、READMEのサンプルコードも次のように書き直しました。Haskellもどきです。<a href="https://github.com/ryuichiueda/GlueLang#gluelang" target="_blank">READMEはGitHub</a>で読めます。READMEには、コンパイルして試す方法も追記しましたので、ちょっと試していただけたらと。<br />
<br />
[hs]<br />
import /bin/ as b<br />
import /usr/bin/ as ub<br />
<br />
main infile = do<br />
 file tmp = cattac infile <br />
 b.cat tmp<br />
<br />
cattac file = b.cat file &gt;&gt;= ub.tail '-r'<br />
[/hs]<br />
<br />
型の考え方も、テーブルの列数とかちょっとしたデータの縛りを作るのに利用できそうです。<br />
<br />
Haskell風にしたことで数学のコワイお兄さんたちにトラップされそうですが、やっぱりシェルスクリプトは関数型だという持論を表現しやすいので、こっちの方向で開発を進めます。<br />

