---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2019 Ryuichi Ueda
---

# 【問題と解答】jus共催 第44回シェル芸7周年で変態化が進みすぎなので実用的な問題しか出さないぞと宣言しておく勉強会（無保証）


* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.44)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```


* 環境: 解答例はUbuntu Linux 18.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

　次のようなナンバープレースの問題があります。（出典: https://commons.wikimedia.org/wiki/File:Sudoku-by-L2G-20050714.svg ）

```
$ cat sudoku
53**7****
6**195***
*98****6*
8***6***3
4**8*3**1
7***2***6
*6****28*
***419**5
****8**79
```

　このファイルを、次のように、第一フィールドが行番号、第二フィールドが列番号、第三フィールドが区画（3x3のグリッドに適当に番号をつけたもの）、第四フィールドが値のファイル`a`に変換してください。

```
$ head a
0 0 0 5
0 1 0 3
0 2 0 *
0 3 1 *
0 4 1 7
0 5 1 *
0 6 2 *
0 7 2 *
0 8 2 *
1 0 0 6
```

### 解答例

```
### awk ###
$ cat sudoku | sed 's;.;& ;g' 
| awk '{for(i=1;i<=NF;i++)print NR-1,i-1,$i}' 
| awk '{print $1,$2,int($1/3)%3*3+int($2/3),$3}' > a
### opy ###
$ cat sudoku 
| opy '{for n,v in enumerate(F1):print(NR-1,n,((NR-1)//3)*3+(n//3),v)}' > a
```

## Q2

　前の問題で作った`a`から、次のように5列目以降に入らない数字を書き込んだファイル`b`を作ってください。入らない数字は重複を除去しなくて構いません。

```
$ head b
0 0 0 5
0 1 0 3
0 2 0 * 5 3 7 6 9 8
0 3 1 * 5 3 7 1 9 5 8 4
0 4 1 7
0 5 1 * 5 3 7 1 9 5 3 9
0 6 2 * 5 3 7 6 2
0 7 2 * 5 3 7 6 8 7
0 8 2 * 5 3 7 6 3 1 6 5 9
1 0 0 6
```

### 解答例

```
$ cat a |
awk 'FILENAME!="-"{a=$0}FILENAME=="-"{print $0,a}' <(tr '\n' ' ' < a) - 
| awk '$4!="*"{print $1,$2,$3,$4}$4=="*"{for(i=5;i<=NF;i+=4){
if($1==$i || $2==$(i+1) || $3==$(i+2)){if($(i+3)!="*")$4=$4" "$(i+3)}
};print $1,$2,$3,$4}' > b
```

## Q3

　前の問題で作った`b`から、次のように、入る数字の候補を5列目以降に書き込んだファイル`c`を作ってください。

```
$ head c
0 0 0 5
0 1 0 3
0 2 0 * 1 2 4
0 3 1 * 2 6
0 4 1 7
0 5 1 * 2 4 6 8
0 6 2 * 1 4 8 9
0 7 2 * 1 2 4 9
0 8 2 * 2 4 8
1 0 0 6
```


### 解答例

```
$ cat b | awk 'NF==4;NF!=4{for(i=1;i<=9;i++){
for(j=5;j<=NF;j++){if(i==$j){j=NF+3}} if(j!=NF+4)$4=$4 " "i
};print $1,$2,$3,$4}' > c
```

## Q4

　`c`から元の`sudoku`のフォーマットで`sudoku_1`を作ってください。また、これまでの解答から、ナンバープレースの問題を解いてください。


```
$ cat sudoku_1
53**7****
6**195***
*98****6*
8***6***3
4**853**1
7***2***6
*6***7284
***419*35
****8**79
```

### 解答例


```
$ cat c | awk 'NF==5{print $5}NF!=5{print $4}' | tr -d '\n' | fold -9 | awk 4 > sudoku_1
```

```
$ for i in {1..10} ; do cat sudoku_1 | sed 's;.;& ;g' 
| awk '{for(i=1;i<=NF;i++)print NR-1,i-1,$i}' 
| awk '{print $1,$2,int($1/3)%3*3+int($2/3),$3}' > a; cat a 
| awk 'FILENAME!="-"{a=$0}FILENAME=="-"{print $0,a}' <(tr '\n' ' ' < a) - 
| awk '$4!="*"{print $1,$2,$3,$4}$4=="*"{
for(i=5;i<=NF;i+=4){if($1==$i || $2==$(i+1) || $3==$(i+2)){if($(i+3)!="*")$4=$4" "$(i+3)}}
;print $1,$2,$3,$4}'| awk 'NF==4;NF!=4{for(i=1;i<=9;i++){
for(j=5;j<=NF;j++){if(i==$j){j=NF+3}} if(j!=NF+4)$4=$4 " "i};print $1,$2,$3,$4}' 
| awk 'NF==5{print $5}NF!=5{print $4}' | tr -d '\n' | fold -9 
| awk 4 > tmp ; mv tmp sudoku_1 ; done 
```

注意: この方法で全ての問題が解ける保証はありません。


## Q5

　積分$$\int_0^{0.5} \log_e(\cos x) dx$$を計算してください。数値計算でかまいません。


### 解答例

```
$ seq 0 49 | awk '{print $1/100, $1/100+0.01}' | awk '{print log(cos($1)), log(cos($2))}' | awk '{print ($1+$2)/2*0.01}' | awk '{a+=$1}END{print a}'
-0.0213851
$ opy 'B:{from scipy import integrate;import math};B:{def f(x): return math.log(math.cos(x))};B:[integrate.quad(f,0,0.5)[0]]'
-0.021380536815408222
```

* 参考: https://reference.wolfram.com/language/tutorial/IntegralsThatCanAndCannotBeDone.html.ja?source=footer

## Q6

　次の`speech`の空行に、`speech2`から順番に行を拾って埋め込んで、結婚式のスピーチを完成させてください。


```
$ cat speech 
このうんこを作った
のは誰だあっ!!う


夜。秋は夕暮れ。冬
はうんこハァ　テレ

無ェ、生まれてこの

やつはとんでもない
ものを盗んでいきま



の？疲れからか、
$ cat speech2 
んこも休み休み言え
春はあけぼの。夏は
ビも無ェ、うんこも
かた見だごとア無ェ
した。あなたのうん
こですお前それうん
こでも同じ事言えん
```

### 解答例

```
$ awk 'FILENAME=="speech"{if(/^$/){print a[++n]}else{print}}
FILENAME=="speech2"{a[FNR]=$0}' speech2 speech
```


## Q7

　次のファイルはあるメッセージが暗号化されたものです。ASCIIコードの文字一つ一つを5乗して437で割った余りを10進数で記述しています。各十進数を何乗かして437で割った余りをASCIIコードとして解釈するとメッセージが読めますが、これを解読しようとしています。

``` 
$ cat message 
262 325 122 80 266 406 163 89 325 89 326
``` 

### 小問1

　まず、各数字を200乗して437で割った余りを出力してください。正解はこうなります。

```
35 308 26 282 399 87 349 55 308 55 85
```


### 解答例

　一回かけるごとに割っていくと桁落ちしません。

```
$ cat message | xargs -n 1 
| awk '{a=1;for(i=1;i<=200;i++){a*=$1;a=a%437};print a}' 
| xargs 
35 308 26 282 399 87 349 55 308 55 85
```

### 小問2

　指数乗する数を変えて力づくで暗号を解いてください。

### 解答例

```
$ for d in {1..1000} ; do cat message | xargs -n 1 
| awk -v d=$d '{a=1;for(i=1;i<=d;i++){a*=$1;a=a%437};print a}' 
| xargs 
| awk '{for(i=1;i<=NF;i++){if($i >= 256)exit(0)};print $0}' ; done 
| awk '{for(i=1;i<=NF;i++)printf("%c",$i);print ""}'
unko_jyanai
unko_jyanai
unko_jyanai
unko_jyanai
unko_jyanai
```


### 小問3

　もっと合理的に解いてください。

### 解答例

　RSA暗号だと考えると次のように指数乗する数を計算できます。（解説は・・・すんません・・・）

* 437を素因数分解する

```
$ echo 437 | factor
437: 19 23
```

* $(19 - 1)(23 - 1)$を計算

```
$ echo 437 | factor | awk '{print ($2-1)*($3-1)}'
396
```

* 求める数（指数乗する数）を`d`とすると、`5d`を396で割った余りが1となる`d`が秘密鍵になります。

```
$ n=$(echo 437 | factor | awk '{print ($2-1)*($3-1)}' ) ; seq inf | awk -v n=$n '5*$1%n==1' | head -n 1
317
```

最初の`d`は317なので、これを秘密鍵とします。

* 317で暗号を解いてみましょう。

```
$ cat message | xargs -n 1 
| awk '{a=1;for(i=1;i<=317;i++){a*=$1;a=a%437};print a}' 
| awk '{printf("%c",$1)}' | awk 4
unko_jyanai
```
