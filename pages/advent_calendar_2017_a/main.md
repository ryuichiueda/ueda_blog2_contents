---
Keywords: うんこ,シェル芸,割とどうでもいい
Copyright: (C) 2017 Ryuichi Ueda
---

# うんこシェル芸ドリル

* 諸注意
    * これは[Shell Script Advent Calendar 2017](https://qiita.com/advent-calendar/2017/shellscript)の記事である。しかし、万が一「品位が問われる」みたいな話になるならば、全力でひり出したものであり大変残念ではあるが、全力で引っ込める。
    * 解答はMacの端末でUbuntu 16.04にSSH接続して作った。
    * 必要なコマンドは各自インストールのこと。環境の違いはクソ力で埋め合わせること。
    * 解答例を試すときは改行を除去のこと。また、周囲に人がいないことを確認すること。
    * うんこ漢字ドリルではない。

[問題のみのページはこちら](/?page=advent_calendar_2017)

## 💩1

次のように💩を変換して得られる8桁の16進数について、10進数に変換後、素因数分解を行い、得られる素数のうち最大のものを求めよ。

```bash
$ echo -n 💩 | xxd -p
f09f92a9
```

### 解答

💩には、大きな素数が含まれるため、大自然の何かを感じざるを得ない。

```bash
$ echo -n 💩  | xxd -p | sed 's/^/0x/' | xargs printf "%d" | factor |
awk '$1=" "' | xargs -n 1 | sort -n | tail -n 1
26385553
```

## 💩2

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

ということで、自己言及型💩であることが判明する。応用としては、二つ💩を出力してそれを再実行し、forkbomb（💩bomb）を起こすという手法が考えられるが、自分のマシンを壊したくないので割愛する。

## 💩3

lsをunkoと打ち間違える癖に悩む者は多い。そこで矯正のため、unkoと打つと、端末の幅いっぱいにうんこメッセージをスクロールさせるエイリアスを設定せよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q1.gif" >

### 解答

* https://gist.github.com/Iruyan-Zak/186ce5d5cf8164744721dbf2f9326ef1


```bash
$ alias unko='echo -ne "@@unko@@yes" | perl -pe "\$_ x= 20" |
head -c $(tput cols) | sed "s/@/💩/g" | sed -E ":b;p;s/(.)(.*)/\2\1/;bb" |
xargs -i bash -c "sleep 0.2 && echo -ne \\\\r{}"'
```

## 💩4

次のように楽しげに💩をぐるぐるさせよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q2.gif" >

### 解答例

```bash
$ while sleep 0.02 ; do clear ; echo 💩  $(date +%N) |
awk '{t=2*3.14*$2/1000000000;c=cos(t)*5+5;s=sin(t)*10+13;
for(i=1;i<=c;i++)print "";for(j=1;j<=s;j++)printf " ";print $1}'; done
```

## 💩5

次の文を「う」「ん」「こ」「ー」のみでエンコードする例を示し、デコード可能であることを示せ。

```
2017年はうんこの年でした。うんこうんこ氏のうんこの党がうんこアウフヘーベン発言で頓挫しました。
```

### 解答

#### ・エンコードの一例

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

出力に謎のリズムがあるが、理由が良く分からないので調査中。（嘘）

#### ・例に対応するデコード

```bash
$ cat unko_yuriko | sed -e 's/う/0 /g' -e 's/ん/1 /g' -e 's/こ/2 /g' -e 's/ー/3 /g' |
xargs -n 2 | awk '{print $1*4 + $2}' | xargs printf "%x" | xxd -p -r
2017年はうんこの年でした。うんこうんこ氏のうんこの党がうんこアウフヘーベン発言で頓挫しました。
```

## 💩6

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



## 💩7 

これを電車の中で人に見られながら作成していた筆者の心境を説明せよ。

### 解答

わりと楽しい。

## 宣伝

この内容で宣伝をすると叱られるのではないかという話はさておき、第一特集で記事を書きました。そして「シェル芸人からの挑戦状」好評連載中です。よろしくお願いしまーす！！

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B076M9MGDL/ryuichiueda-22/" target="_blank" ><img src="https://images-fe.ssl-images-amazon.com/images/I/61xVgsnyrIL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B076M9MGDL/ryuichiueda-22/" target="_blank" >ソフトウェアデザイン 2018年 01 月号 [雑誌]</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;"> 技術評論社 2017-12-18    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="margin:5px 0"><a href="http://www.amazon.co.jp/gp/search?keywords=%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&tag=ryuichiueda-22" target="_blank" >Amazon</a></div><div class="shoplinkrakuten" style="margin:5px 0"><a href="https://hb.afl.rakuten.co.jp/hgc/131cef76.deb3ed6a.131cef77.7335f681/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2582%25BD%25E3%2583%2595%25E3%2583%2588%25E3%2582%25A6%25E3%2582%25A7%25E3%2582%25A2%25E3%2583%2587%25E3%2582%25B6%25E3%2582%25A4%25E3%2583%25B3%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" target="_blank" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>



おしまい。
