---
Keywords: バイナリ,AWKの％c,CLI,jpeg,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# バイナリをテキストに直してまたバイナリに戻すワンライナー
本当にたくさん働いている人は忙しいなんて自分から言いません．上田です．忙しい．

いつもお世話になっている@hasegawさんから<a href="/?post=01549" target="_blank">/?p=1549</a>の記事について，

<blockquote class="twitter-tweet" lang="ja"><p>ImageMagickとか使わずにシェル芸でEXIF除去ネタキター！と思ったけど普通に使ってた。。。。。。</p>&mdash; Takeshi HASEGAWA (@hasegaw) <a href="https://twitter.com/hasegaw/statuses/403387610220871681">2013, 11月 21</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

と言われてしまったので<del datetime="2013-11-21T12:17:47+00:00">根に持っています．</del>なんとかしたいと思います．

<!--more-->

と言ってもJPEGのバイナリをいじるなんてことをしたことがないので今回は準備だけ．いや，10年くらい前に一度やってるわ．忘れた．

それはいいとして，準備というのは，JPEGをAWK等でいじりやすい形式のテキストにして，またJPEGに復元するという試みです．これができれば，テキストを改ざんするのをsedやAWKで自在にできるわけです．たぶん．

まず，バイナリをテキストにして閲覧するのに使うodというコマンドにJPEGの画像を通します．od -xとやると16進数になります．

```bash
uedamac:~ ueda$ cat IMG_0007.JPG | od -x | head
0000000 d8ff e1ff a028 7845 6669 0000 4d4d 2a00
0000020 0000 0800 0b00 0f01 0200 0000 0600 0000
0000040 9200 1001 0200 0000 0900 0000 9800 1201
0000060 0300 0000 0100 0100 0000 1a01 0500 0000
0000100 0100 0000 a200 1b01 0500 0000 0100 0000
0000120 aa00 2801 0300 0000 0100 0200 0000 3101
0000140 0200 0000 0400 2e34 0031 3201 0200 0000
0000160 1400 0000 b200 1302 0300 0000 0100 0100
0000200 0000 6987 0400 0000 0100 0000 c600 2588
0000220 0400 0000 0100 0000 3802 0000 0203 7041
```

ところでJPEGは最初 0xffd8から始まるのですが，odの吐くテキストはひっくり返って0d8ffと出してしまいます．次の0xe1ffも本当は0xffe1です．詳しい話は省きますが，「エンディアン」というのがキーワードになります．

それを踏まえて，バイナリを1バイトごとに順番に並べてみます．

```bash
uedamac:~ ueda$ cat IMG_0007.JPG | od -x | sed 's/^[0-9]*//' | tr ' ' '\\n' | 
awk 'NF==1' | awk '{print substr($1,3,2),substr($1,1,2)}' | head
ff d8
ff e1
28 a0
45 78
69 66
00 00
4d 4d
00 2a
00 00
00 08
```

こんな感じで2列に並べてみました．

これをlessで見て，awkかなにかでExifの部分を別のバイナリに置き換えれば情報を消せそうです．

それはいつの日にかの目標にして，ここではこのテキストを一度保存しましょう．<span style="color:red">あ，忘れていましたが，odは出力が同じ行に＊を入れて省略する悪い癖があるので，かならずオプションvを指定してこの機能を消します．</span>

```bash
uedamac:~ ueda$ cat IMG_0007.JPG | od -xv | sed 's/^[0-9]*//' | 
tr ' ' '\\n' | awk 'NF==1' | 
awk '{print substr($1,3,2),substr($1,1,2)}' > text
```

今度はtextからjpegを復元します．このワンライナーですが，sedで16進数の頭に0xをつけ，次のgawkで16進数を10進数に変換し，最後のgawkで10進数をバイナリで出力します．gawkの%cがミソです．

```bash
uedamac:~ ueda$ cat text | sed 's/ / 0x/g' | sed 's/^/0x/' | 
gawk '{print strtonum($1),strtonum($2)}' | 
LANG=C gawk '{printf("%c%c",$1,$2)}' > hoge.jpg 
```

もとの画像と比較してみましょう．

```bash
uedamac:~ ueda$ cmp IMG_0007.JPG hoge.jpg 
uedamac:~ ueda$ 
```

大丈夫そうです．最後に，一度テキストに化けたJPEGを貼付けておきます．御犬様，テキストにしちゃってすいませんでした．

<a href="hoge.jpg"><img src="hoge-300x224.jpg" alt="hoge" width="300" height="224" class="aligncenter size-medium wp-image-1621" /></a>

バイナリもテキストも，落ち着いて扱えば大差のないものです．しかし，Exifを消すのはいつやろうかな・・・


寝る．
