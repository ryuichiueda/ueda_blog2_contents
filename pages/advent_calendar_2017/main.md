---
Keywords: うんこ,シェル芸,割とどうでもいい
Copyright: (C) 2017 Ryuichi Ueda
---

# うんこシェル芸ドリル

* 諸注意
    * これは[Shell Script Advent Calendar 2017](https://qiita.com/advent-calendar/2017/shellscript)の記事である。しかし、万が一「品位が問われる」みたいな話になるならば、全力でひり出したものであり大変残念ではあるが、全力で引っ込める。
    * 解答はMacの端末でUbuntu 16.04にSSH接続して作った。
    * 必要なコマンドは各自インストールのこと。
    * うんこ漢字ドリルではない。

## 💩1

次のバイナリが何であるか、何が得られるかを解析せよ。

```
H4sICL5zMFoAA/CfkqkAq3f1cWNkZGSAASYGZgYQLzrARMiEAQ
FMGBQYYKrgqoFqQFQtFLOCOAIMDHr6H+ZPWsm1gwXI3Q1SvDME
qHIXO5B1tmEHSGA3A5gNADcLsIJ9AAAA
```

### 解答

* 参考: http://d.hatena.ne.jp/yupo5656/20061112/p2

```bash
### とりあえずファイルに保存 ###
$ cat unko
H4sICL5zMFoAA/CfkqkAq3f1cWNkZGSAASYGZgYQLzrARMiEAQ
FMGBQYYKrgqoFqQFQtFLOCOAIMDHr6H+ZPWsm1gwXI3Q1SvDME
qHIXO5B1tmEHSGA3A5gNADcLsIJ9AAAA
### 文字列を見ると明らかにbase64 ###
$ cat unko | base64 -d > unko2
### unko2はgzファイル ###
$ file unko2
unko2: gzip compressed data, was "\360\237\222\251", last modified: Wed Dec 13 00:26:38 2017, from Unix
### "\360\237\222\251" を解析 ###
$ echo $'\360\237\222\251'
💩
### fileの出力通りにファイル名を復元 ###
$ mv unko2 💩.gz
$ gunzip 💩.gz
### fileで調査するとELF形式のバイナリと分かる ###
$ file 💩
💩: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, corrupted section header size
$ chmod +x ./💩
$ ./💩
./💩
```

ということで、自己言及型💩であることが判明。

## 💩2

lsをunkoと打ち間違える癖に悩んでいる諸氏の矯正のため、次のようにlsをunkoと打ち間違えると、端末の幅いっぱいにうんこメッセージをスクロールさせるエイリアスを設定せよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q1.gif" >

### 解答

* https://gist.github.com/Iruyan-Zak/186ce5d5cf8164744721dbf2f9326ef1


```bash
$ alias unko='echo -ne "@@unko@@yes" | perl -pe "\$_ x= 20" | head -c $(tput cols) | sed "s/@/💩/g" | sed -E ":b;p;s/(.)(.*)/\2\1/;bb" | xargs -i bash -c "sleep 0.2 && echo -ne \\\\r{}"'
```

## 💩3

次のように楽しげに💩をぐるぐるさせよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q2.gif" >

### 解答例

```bash
$ while sleep 0.02 ; do clear ; echo 💩  $(date +%N) |
awk '{t=2*3.14*$2/1000000000;c=cos(t)*5+5;s=sin(t)*10+13;
for(i=1;i<=c;i++)print "";for(j=1;j<=s;j++)printf " ";print $1}'; done
```

## 💩4

次の文を「う」「ん」「こ」「ー」のみでエンコードし、デコードせよ。

```
2017年はうんこの年でした。うんこうんこ氏のうんこの党がうんこアウフヘーベン発言で頓挫しました。
```

### 解答

* エンコード

```bash
$ echo 2017年はうんこの年でした。うんこうんこ氏のうんこの党がうんこアウフヘーベン発言で頓挫しました。|
xxd -b | awk '{$1="";$NF="";print}' | tr -d ' ' | sed 's/../ &/g' |
sed -e 's/ 00/う/g' -e 's/ 01/ん/g' -e 's/ 10/こ/g' -e 's/ 11/ー/g' > unko_yuriko
$ cat unko_yuriko 
うーうこうーうううーうんうーんーーこんんこーこん
こーんうーこうーこううんここーーーこうーこううん
こうんこーこうーこううここんうーーこうーこううん
こんうーーこうーこううんここーこーこんんこーこん
こーんうーこうーこううんここんーーこうーこううん
こんんーーこうーこううんこんーーーこうーこううう
こううこーこうーこううんこうんこーこうーこううこ
こんうーーこうーこううんこんうーーこうーこううん
こうんこーこうーこううここんうーーこうーこううん
こんうーーこんここーううこうーーーこうーこううん
ここーこーこうーこううんこうんこーこうーこううこ
こんうーーこうーこううんこんうーーこうーこううん
ここーこーこんんこうんんこんここーこうーこううん
こうーうーこうーこううんこうんこーこうーこううこ
こんうーーこうーこううんこんうーーこうーこううこ
ここうこーこうーこううこここんこーこうーこううー
こんんんーこうーこううーこんこうーこうーこううー
こーーうーこうーこううーこんこんーこうーこううー
こーうーーこんーこんこんこーここーここうこここう
こうううーこうーこううんここんーーここんここうう
こんうーーこんここうーうこここーーこうーこううん
こんんーーこうーこううんこーーこーこうーこううん
こんんーーこうーこううんこんーーーこうーこううう
こううこううここ
```

* デコード

```bash
$ cat unko_yuriko | sed -e 's/う/0 /g' -e 's/ん/1 /g' -e 's/こ/2 /g' -e 's/ー/3 /g' |
xargs -n 2 | awk '{print $1*4 + $2}' | xargs printf "%x" | xxd -p -r
2017年はうんこの年でした。うんこうんこ氏のうんこの党がうんこアウフヘーベン発言で頓挫しました。
```

## 💩5

`/dev/urandom`の出力から小文字大文字のアルファベットだけを残し、その中に流れるunkoの平均流速を概算せよ。なお、大文字小文字は区別しないものとする。

* 例
    * 次のように26文字に一つ「unko」とある場合は、38[unko/kb]となる。

    ```
    $ echo abadojfwejaiefUnkofawfewaf | awk '{print 1/length($0)}'
    0.0384615
    ```

### 解答

```bash
$ cat /dev/urandom | tr -dc 'A-Za-z' | tr a '\n' |
tee /tmp/unko | grep -oi -m 100 unko &&
wc -c /tmp/unko | awk '{print $1/(100*1000*1000)"[unko/MB]"}'
UNko
UnKO
UnKo
unKO
Unko
UNKO
UnKo
UNKO
UNKo
unKo
uNKo
unKO
Unko
unko
UnKo
uNko
UNKO
UNko
UnKO
Unko
Unko
UNKO
uNKo
Unko
uNKO
unKO
UnKO
UNKo
unko
uNkO
uNKO
unKo
unKo
unkO
UNkO
UnKo
uNko
uNKO
unko
unKO
unKO
UNKO
unKO
unko
unKo
uNko
UNKO
UNko
uNkO
uNko
UnkO
UnKo
UnKo
uNko
UNKO
uNKO
unko
unKo
uNko
uNkO
UnKo
UNko
UNkO
UNKo
uNkO
UnKo
UnkO
UNko
UNKO
UnkO
unko
unKO
unko
UNkO
Unko
unkO
unkO
unKo
unKo
UNko
unKO
UnKo
uNKO
UNko
unKo
UnKO
uNKO
UNKo
UnKO
UNKo
uNKO
unKo
UNKO
UNko
UNko
UnkO
UNKO
unKO
UnKO
UNko
0.48599[unko/MB]
```

ということで、0.5ウンコパーメガバイトだと分かる。



## 💩6 

これを電車の中で人に見られながら作成していた筆者の心境を説明せよ。
