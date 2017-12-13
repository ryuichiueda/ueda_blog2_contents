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

## お疲れ💩でした

[解答例はこちら](/?page=advent_calendar_2017_a)

## 宣伝

この内容で宣伝をすると叱られるのではないかという話はさておき、第一特集で記事を書きました。そして「シェル芸人からの挑戦状」好評連載中。

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B076M9MGDL/ryuichiueda-22/" target="_blank" ><img src="https://images-fe.ssl-images-amazon.com/images/I/61xVgsnyrIL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B076M9MGDL/ryuichiueda-22/" target="_blank" >ソフトウェアデザイン 2018年 01 月号 [雑誌]</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;"> 技術評論社 2017-12-18    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="margin:5px 0"><a href="http://www.amazon.co.jp/gp/search?keywords=%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&tag=ryuichiueda-22" target="_blank" >Amazon</a></div><div class="shoplinkrakuten" style="margin:5px 0"><a href="https://hb.afl.rakuten.co.jp/hgc/131cef76.deb3ed6a.131cef77.7335f681/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2582%25BD%25E3%2583%2595%25E3%2583%2588%25E3%2582%25A6%25E3%2582%25A7%25E3%2582%25A2%25E3%2583%2587%25E3%2582%25B6%25E3%2582%25A4%25E3%2583%25B3%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" target="_blank" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>



