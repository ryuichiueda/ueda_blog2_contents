---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2020 Ryuichi Ueda
---

# 【問題】jus共催 第51回いつもと違って日曜開催だよシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.51)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 20.04で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。
* 参考: kanata, 難読化シェル芸を発案した | A painter and a black cat, https://raintrees.net/news/95

## Q1

　次のファイルにはウンコが潜んでいます。ウンコを復元してください。
すぐ解けた人は、`pepo`ファイルのデータをワンライナーで作ってみてください。

```
$ cat pepo 
ぽぽぽぽぽぽぽぽぽ人ぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
ぽぽぽぽぽぽぽぽぽぺぺぺぺぺぺぺぺぺぺ
```

## Q2

　次の`q2`ファイルは、あるC言語のソースコードに何回か変換をかけて作ったデータです。ソースコードに戻してコンパイルして、実行してみてください。

```
$ cat q2 | fold -b80
fgcd94fgce90fgce9ffgce94fgce9dfgce06fgce95fgce96f49191fgcd0dfgce04fgce05fgce95fg
ce90fgce9gfgcd9ffgce99fgcd0f1bfgcd94fgce90fgce9ffgce94fgce9dfgce06fgce95fgce96f4
9191fgcd0dfgce04fgce05fgce95fgce9dfgce90fgce93fgcd9ffgce99fgcd0f1b1bfgce90fgce9f
fgce05f49191fgce9efgce92fgce90fgce9ffgcd99fgcd901bfgce0c1b10fgce94fgce99fgce92fg
ce03f49191fgce92fgcdccfgcdcef49191fgcd0ef49191fgce0cfgcd01fgce09fgcd08fgcd06fgcd
9dfgcd01fgce09fgcd07fgce96fgcd9dfgcd01fgce09fgcd07fgce93fgcd9dfgcd01fgce09fgcd07
fgce97fgcd9dfgcd01fgce09fgcd01fgcd01fgce0efgcd0c1b10fgce01fgce06fgce05fgce04fgcd
99fgce92fgcd90fgcd0c1b10fgce96fgce09fgce90fgce05fgcd99fgcd01fgcd90fgcd0c1bfgce0e
```


## Q3

　127が素数であることを、数字を使わないワンライナーで確認してください。
確認は、`factor`で因数分解して`awk`で2列であることを確認する方法を使ってください。

```
### 出力例（他に余計なものは出力しないこと） ###
127: 127
```

## Q4


　アルファベットを使わないコマンドあるいはワンライナーで、`q2`の中身を出力してください。
`q2`のあるディレクトリで試してください。
できる人は外部コマンドなしで出力してください。

## Q5

　`message`は、ある日本語のテキストを16進数に変換し、さらに、ある素数をかけたものです。テキストは全角文字だけで記述されています。

```
$ cat message
3CA0F7E029F79C8BAC0F2C87E02A36F3C4E227DF2154362BD529B3A
```

この数を、2から順番に素数で割って16進数で順に出力していってください。
余りについては切り捨てで構いません。


```
1E507BF014FBCE45D6079643F0151B79E27113EF90AA1B15EA94D9D    //2で割った数
1435A7F563528983E4050ED7F56367A696F60D4A60716763F1B8913    //3で割った数
C2031933B97EC1BEF363C1B2CD53E30C0FA07F96D10D7A25DD523E     //5で割った数
8A947FB73B5A8A63D26BD37FB73BEB51C204ED6BB9E50E1B0BCD08     //7で割った数
・・・                                                     //以下延々と
```

## Q6

Q5のワンライナーに続けて、`message`に仕込まれたメッセージを発見してください。
目視できれば完璧でなくてかまいません。

## Q7 

`ssh localhost`（あるいはどこかのサーバに`ssh`でログイン）したあとに、記号だけで`bash`を立ち上げてください。

```
$ ssh localhost
$ 数字もアルファベットも使わない
### 確認（レベルが2になっていると成功） ###
$ echo $SHLVL
2
```

## Q8

`echo evil`という文字列をランダムなアルファベットを書いたファイル`secret`の中に隠そうとしています。`secret`からは、次のように操作すると`echo evil`という文字列が作れます。

* 各文字を2進数にして一番下の桁のバイナリを残す。
* 残ったバイナリを8個ずつ組にして文字に戻す。

このようなファイル`secret`を作ってください。また、作ったら上の操作で`echo evil`が出現することを確認してください。

