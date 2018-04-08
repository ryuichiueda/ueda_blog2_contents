---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2018 Ryuichi Ueda
---

# 【問題と解答】jus共催 第35回またまためでたいシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.35)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

`curl parrot.live`で表示されるオウムをファイルに生け捕りにして、ファイルから再生してください。

### 解答

```
### 生け捕り###
$ curl parrot.live > a   #しばし待つ
### Macの場合はうまくリダイレクトできない模様なのでddの別解 ###
$ curl parrot.live | dd of=a
### 再生 ###
$ cat a | awk '{print;system("sleep 0.002")}'
```

## Q2

次のようなファイル`herohero`があります。
```
$ cat herohero 
１へ
７ろ
９へ
１３ろ
```
ひらがなを左側に書いてある数字の行に持って行き、次のような出力に変換してください。
```
へ





ろ

へ



ろ
```

### 解答

```
$ cat herohero | sed 'y/１３７９/1379/' | sed -r 's/[0-9]+/& /' |
awk '{printf("%02d %s\n",$1,$2)}' | sort -k1,1n -k2,2r - <(seq -w 12) |
uniq -w2 | awk '{print $2}'
へ





ろ

へ



ろ
```

## Q3

次のようなファイル`data`があります。
```
$ cat data 
1 A
1 B
2 C
2 C
1 B
3 C
4 C
3 B
3 B
3 D
3 B
1 B
2 A
1 A
2 C
```

集計して次のような出力を得てください。

```
1 A:2 B:3
2 A:1 C:3
3 B:3 C:1 D:1
4 C:1 
```

### 解答

```
$ cat data | sort -k1,2 | uniq -c | awk '{print $2,$3":"$1}' |
awk '{a[$1]=a[$1]" "$2}END{for(k in a){print k a[k]}}'
1 A:2 B:3
2 A:1 C:3
3 B:3 C:1 D:1
4 C:1
```

## Q4

ひらがなで名前っぽい単語をランダムに生成してみてください。

### 解答

```
$ while : ; do zsh -c 'echo {あ..ん}' | tr ' ' '\n' |
shuf ; done | xargs -n 100 | tr -d ' ' | mecab |
grep 人名 | sed 's/\t.*//'
ちれ
ひろ
りこ
おだ
みか
なを
りう
せつ
ゆみ
...
```

## Q5

`echo 響け！ユーフォニアム`からはじめて、次のような出力を得てください。なお、出題者はこのアニメを見たことがありません。

```
響け！ユーフォニアム
　響け！ユォニアム
　　響け！ニアム
　　　響けアム
　　　　響ム
　　　　　
　　　　　
　　　　ム響
　　　ムアけ響
　　ムアニ！け響
　ムアニォユ！け響
ムアニォフーユ！け響
```

### 解答

```
$ echo '響け！ユーフォニアム' |
awk '{a=$1;for(i=1;i<=6;i++)
	{print substr($1,1,length(a)/2-i+1)substr($1,length(a)/2+i)}}' |
pee cat 'rev | tac' | awk '{for(i=1;i<=5-length($0)/2;i++){printf "　"}print}'
響け！ユーフォニアム
　響け！ユォニアム
　　響け！ニアム
　　　響けアム
　　　　響ム
　　　　　
　　　　　
　　　　ム響
　　　ムアけ響
　　ムアニ！け響
　ムアニォユ！け響
ムアニォフーユ！け響
```


## Q6

素因数分解したときに23より大きい素因数を持たない自然数を1985個抽出してください。

### 解答

```
$ seq 100000 | factor | awk '{for(i=2;i<=NF;i++){if($i>23)next};print}' | head -n 1985 | sed 's/:.*//'
```


## Q7

素数番目の文字を抽出すると意味のある語句になっているような文字列を作成してください。例を示します。（素数番目でない文字は特に凝る必要はありません。同じ文字でも大丈夫です。）

```
うそすんうんだいうんいんすんこうき
```

その後、その語句を抽出してください。

### 解答

#### 作成

```
$ seq 100 | factor | awk 'NF==2{printf("%02d\n",$2)}' |
paste - <(echo そすう だいすき | grep -o .) | awk NF==2 |
cat - <(seq -w 17) | sort -k1,1n -k2,2r | uniq -w2 |
awk 'NF==1{print "う"}NF==2{print $2}' | tr -d '\n' | awk 4
うそすうううだううういうすうううき
```

#### 抽出

```
$ echo うそすうううだううういうすうううき | grep -o . |
nl | while read n c ; do factor $n | awk -v c=$c 'NF==2{print c}' ; done
```

## Q8 

Q6の方法で作成した自然数をファイル`a`に保存し、この中から4つ数字を選んで掛け算したとき、その値がある自然数の4乗になっている組み合わせを1個以上探してください。

### 解答

たぶんもっと効率の良い方法がありますが・・・。

```
$ while : ; do cat a | factor |
awk '{for(i=2;i<=23;i++)a[i]=0;for(i=2;i<=NF;i++)a[$i]++;
	print $1,a[2],a[3],a[5],a[7],a[11],a[13],a[17],a[19],a[23]}' |
shuf | awk '{for(i=2;i<=10;i++)a[i]+=$i;print $1}
	NR%4==0{for(i=2;i<=10;i++){printf a[i]%4" ";a[i]=0};print ""}' |
grep -B4 '0 0 0 0 0 0 0 0 0' ; done
363:
1650:
2750:
4500:
0 0 0 0 0 0 0 0 0 
1250:
208:
3744:
6084:
0 0 0 0 0 0 0 0 0 
18150:
7776:
9720:
14520:
0 0 0 0 0 0 0 0 0 
13:
1875:
432:
2197:
0 0 0 0 0 0 0 0 0 
^C
```
