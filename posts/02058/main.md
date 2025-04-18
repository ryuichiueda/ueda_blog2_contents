---
Keywords: ご報告,ご挨拶,グルー言語,誕生日,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 36歳の誕生日にグルー言語作る宣言をせざるを得なくなった
<!--:ja-->こんにちは誕生日です上田です。36になりました。定年二年目です。

昨日は<a href="/?post=01955" title="【本番資料】第9回寒中シェル芸勉強会" target="_blank">シェル芸勉強会</a>おつかれさまでした。参加者の方、お足下お悪いなかご来場いただき大変ありがとうございました。スタッフの皆様、無理言ってすいません。

近況ですが、<a href="http://www.sci14.org/specials.html" target="_blank">学会でパーティクルフィルタのチュートリアルをやること</a>になったり、<!--:--><!--:en-->こんにちは誕生日です上田です。36になりました。定年二年目です。

先日、とある方と会食する機会があって、<!--:--><!--more--><!--:ja-->大阪に勉強会の講師に出向くことになったり、<a href="http://www.robocup.or.jp/2014JP_OPEN_1/" target="_blank">ロボカップのSPLリーグのとりまとめ</a>をやったり、本を書いていたり、4月からの講義資料を書いていたり、研究のプログラムをC++で書いていたり、いろんなところから何か書けと依頼されたり、勉強会で裏方やったり表方やったり、子供のことで右往左往したりと、土日は料理を作ったりスーパー行ったりと、体がいくつあっても足りません。

最近、<a href="http://www.fourhourworkweek.com/" target="_blank">The 4-Hour Workweek（週4時間だけ働く）</a>という本を読んで感銘を受けているのですが、著作物を世に出すにはそれなりに時間をかけて考えたり、実証したりしないと人に伝わらないので、今のうちはまあ職種が違うんだよということで、時間をかけて仕事をしたいと考えております。（家で自由に仕事ができるという意味では、働きはじめた26歳からすでに達成しておりましたが・・・）

ところで数日前、皆さんもよくご存知のとある方と会食する機会があり、運良く斜め前の席になったのでからみまくっていたのですが、その会話の中で、一つプログラミング言語を作ると宣言してしまいました。

からんでいる最中に頭の中にあった構想について説明したのですが、私もその方も実戦実戦を重ねてきた人間なので、すぐに「動くものがないと議論にならないね」という話になり、「じゃあ私が何か手がけないといけませんね」と言ってしまって上記の宣言をしてしまった次第です。「完璧にやろうとしたらいけませんよ」とアドバイスいただいたので、今日から、ブログを書くことで頭を整理しながらプロトタイプを作ることにしました。

<h2>構想</h2>

今、グルー言語でメジャーな言語というと、言語としての各種シェルしかありません。一方で、シェルの文法というのは、私の好きなワンライナーや、ちょっとしたスクリプトを書くことに最適化されているので、あまり保存するプログラムを書くのには向いていません。

そこで、「きれいな文法」のグルー言語を一つ作ろうという発想になりました。ここで言う「きれいな」は、なんらかの指標があるわけでなく、私の主観から出発して、後から他の人が評価するくらいでいいんじゃないかと考えています。

<h2>どんな言語か</h2>

ファイル処理に特化したグルー言語です。フィルタコマンドをインポートして使います。DBやファイルシステムと親和性が高いことを目指します。

文法に矛盾があるかもしれませんが、ひとつだけ例を。例えば、こんなbashのコードを考えます（動作未確認）。

```bash
#!/bin/bash
tmp=/tmp/$$

cat ./file1 |
grep -v 'hoge' > $tmp-1

cat ./file1 |
grep -v 'huge' > $tmp-2

cat $tmp-1 $tmp-2 > ./file2
```

これをこんな風に書けないかと。型にfileとmemがあり、それぞれファイルと、シェル変数に相当します。型というより入れ物ですが。データはすべて文字列にするつもりですが、必要ならばint型とか作る可能性もあります。

```python
import coreutils

def main():
 file file1 = "./file1"

 tmpfile tmp1 = proc1 'hoge' file1
 tmpfile tmp2 = proc1 'huge' file1
 tmpfile ans = cat tmp1 tmp2

 commit ans "./file2"
 
def proc1(mem w,file f):
 cat $f
 grep -v $w
```

なぜこう書くかという意図ですがいろいろあって、

<ul>
	<li>構造化する</li>
	<li>中間ファイルの扱いをちゃんとする（パーミッションとか、ファイル名を陽に持たせないとか）</li>
 <li>中途半端にファイルを読み書きさせない。（上の例だと"./file2"にだらだら出力させず、中間ファイルをmvする。）</li>
	<li>コマンドについて、ディレクトリでPATHを指定するやり方ではなくパッケージ指定にする。（例えばシステム標準のコマンドではなく、コマンドのパッケージをgemやeggのようにダウンロードして使うようにして、環境の違いを吸収する）</li>
</ul>

それから、パイプは書くのが面倒なので、一行ずつコマンドをならべて表現しているのが、proc1関数の中身です。これはPythonのやり方を借りて、インデントで表現できないかと。

長くなりそうなので、とりあえず今度は動くものを作ります・・・


さあ昼飯の準備だ・・・。
<!--:-->
