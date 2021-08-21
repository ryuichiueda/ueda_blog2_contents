---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2021 Ryuichi Ueda
---

# 【問題と解答】jus共催 第55回TOKY 02020オフィシェルシェル芸勉強会KAWASAKI2021

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.55)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu 20.04 LTSで作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

## Q1

次の図形を描いてください。for文やwhile文は禁止とします。

```
* * * * * * * *
* *         * *
*   *     *   *
*     * *     *
*     * *     *
*   *     *   *
* *         * *
* * * * * * * *
```

### 解答例

```
$ echo -e '* * * *\n* *    \n*   *  \n*     *' |
sed 's/.*/echo -n "&";echo -n " ";echo "&" |
rev /e'  | pee cat tac
* * * * * * * *
* *         * *
*   *     *   *
*     * *     *
*     * *     *
*   *     *   *
* *         * *
* * * * * * * *
```

## Q2

次のおしゃれなUNKOを落ち着かせてASCIIコードのUNKOに戻してください。どんな変換方法でも構いませんが、`UNKO`の4個の大文字と、元の`𝒰𝒩𝒦𝒪`の4文字は使用禁止にします。元の`𝒰𝒩𝒦𝒪`由来のデータを使わない方法も禁止です。

```bash
$ echo 𝒰𝒩𝒦𝒪 
```

### 解答例

```bash
### 16進数で計算 ###
$ echo 𝒰𝒩𝒦𝒪 | xxd -px | fold -b8 | sed -n '/....../s/....../0x/gp' | mawk '{printf("%02x",$1 - 91)}' | xxd -r -p | awk 4
UNKO
### uninameを利用 ###
$ echo 𝒰𝒩𝒦𝒪 | uniname 2> /dev/null | sed 's/.* //' | sed -n '2,5p' | paste -sd ''
UNKO
```

## Q3

次のふたつの出力例のように、端末のフチに`@`を並べてください。for文やwhile文は禁止とします。

![](ex1.png)
![](ex2.png)

### 解答例

```bash
$ stty size | perl -anle '$a=$F[1]."\n";print $a x $F[0]' |awk NF |
perl -anle 'print " " x $F[0]' | sed '2s/ /@/g;$s/ /@/g;s/^ /@/;s/ $/@/'
```


## Q4 

端末上で次のような出力を得てください。

![](annihilation.mp4)

### 解答例

```bash
$ a='💩                                                        💩' ; clear;
echo -e "\n\n\n" ;tput cuu 1 ; while [[ ! "$a" =~ "💩💩" ]] ; do sleep 0.2;
a=$(sed -E 's/([^ ])  /\1/;s/^/ /' <<< $a) ; tput cuu 1 ; echo "$a"  ; done;
tput cuu 1; echo "${a/💩💩/ 🍣}" ; echo -e '\n\n\n'
```

## Q5

次の`words`について、同じ文字がちょうど3つ存在し、他に同じ文字がちょうど2つ存在する単語を抽出してください。

```bash
$ cat words 
metabolizes
Manuela
Kroger
purchasable
luster
clattering
mesh
campus
seating
giblet
・・・
```

### 解答例

```bash
$ cat words | awk -F '' '{delete a}{for(i=1;i<=NF;i++)a[$i]++}{for(k in a)if(a[k]==3)print $0}' |
awk -F '' '{delete a}{for(i=1;i<=NF;i++)a[$i]++}{for(k in a)if(a[k]==2)print $0}' | sort -u
Goolagong
antenna
constitutionals
multidimensional
nostalgically
sharecropper
$ cat words | opy '[(e,F0.count(e)) for e in F0]' | grep '2)' | grep '3)' | tr -dc 'a-zA-Z\n'
multidimensional
sharecropper
antenna
constitutionals
Goolagong
nostalgically
```

## Q6 

次のような模様を描いてください。

```bash
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　
　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　💩　
💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩　　　💩
```

### 解答例


```bash
$ echo -e '💩　　\n　💩　\n　　💩' | sed 's/.*/echo -n "&";echo "&" |rev /e' |
sed 's/.//3' | pee cat tac | uniq |
awk '{a=substr($0,2);print $0 a a a a a a a}' | pee cat{,,,,,,,} | uniq
```



## Q7

`words`について、しりとりになっている行を横一列に出力してください。大文字小文字は区別しません。出力は次のようになります。

```
campus seating giblet Tomas
lifeless secures
clews shove exhaust
orifice equivocal
```


### 解答例


```bash
$ grep --color=always -iPz '(.)\n\1' words | sed -zE 's/\n(.\x1b)/ \1/g'  | awk 'NF>1'
campus seating giblet Tomas
lifeless secures
clews shove exhaust
orifice equivocal
### 色を消す ###
$ grep --color=always -iPz '(.)\n\1' words | sed -zE 's/\n(.\x1b)/ \1/g'  |
awk 'NF>1' | tr -dc '[:print:]\n' | sed 's/\[01;31m\[K//g' | sed 's/\[m\[K//g'
campus seating giblet Tomas
lifeless secures
clews shove exhaust
orifice equivocal
### awkを使う場合 ###
$ cat words | awk -F '' 'tolower(e)==tolower($1){print w,$0}{e=$NF;w=$0}' |
awk 'w==$1{printf $0" "}w!=$1{print "\n";printf $0" "}{w=$2}'  | awk NF |
sed -E 's/([^ ]+) \1 /\1 /g'
campus seating giblet Tomas
lifeless secures
clews shove exhaust
orifice equivocal
```

