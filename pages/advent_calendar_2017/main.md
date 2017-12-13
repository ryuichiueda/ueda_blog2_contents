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
* [解答例はこちら](/?page=advent_calendar_2017_a)

## 💩1

次のように💩を変換して得られる8桁の16進数について、10進数に変換後、素因数分解を行い、得られる素数のうち最大のものを求めよ。

```bash
$ echo -n 💩 | xxd -p
f09f92a9
```

## 💩2

次のバイナリが何であるか、何が得られるかを解析せよ。

```
H4sICL5zMFoAA/CfkqkAq3f1cWNkZGSAASYGZgYQLzrARMiEAQ
FMGBQYYKrgqoFqQFQtFLOCOAIMDHr6H+ZPWsm1gwXI3Q1SvDME
qHIXO5B1tmEHSGA3A5gNADcLsIJ9AAAA
```

## 💩3

lsをunkoと打ち間違える癖に悩む者は多い。そこで矯正のため、unkoと打つと、端末の幅いっぱいにうんこメッセージをスクロールさせるエイリアスを設定せよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q1.gif" >

## 💩4

次のように楽しげに💩をぐるぐるさせよ。

<img width="600" src="/pages/advent_calendar_2017/unko_q2.gif" >

## 💩5

次の文を「う」「ん」「こ」「ー」のみでエンコードする例を示し、デコード可能であることを示せ。

```
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

## 💩7 

これを電車の中で人に見られながら作成していた筆者の心境を説明せよ。

* [解答例はこちら](/?page=advent_calendar_2017_a)

