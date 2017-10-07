---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】jus共催 第31回朝からだと疲れるから午後からでええじゃろシェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.31)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。

<iframe src="//www.slideshare.net/slideshow/embed_code/key/EPiUqB6tfuEzRX" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/secret/EPiUqB6tfuEzRX" title="第31回シェル芸勉強会スライド" target="_blank">第31回シェル芸勉強会スライド</a> </strong> from <strong><a href="https://www.slideshare.net/ryuichiueda" target="_blank">隆一 上田</a></strong> </div>

## Q1 

次の[num.txt](num.txt)について、1の直前にある数字をすべて削除してください。このルールでは、改行を無視します。つまり、次の行の先頭が1のときは、前の行の最後の数字を削除します。

```bash
$ cat num.txt
1214235325231
325316321345
135326547361
414353515325
```

## Q2

次のファイル[indent.txt](indent.txt)について、インデントのついていない行を、上の行のインデントに合わせてください。

```indent.txt
$ cat indent.txt
  * aa
* bbb
         * cccccc
* ddd
      * eeeeeeeeee
* fff
   * gggg
* hhh
```

## Q3

次のような出力を作ってください。

```
********************
*@******************
**@*****************
********************
****@***************
********************
******@*************
********************
********************
********************
**********@*********
********************
************@*******
********************
********************
********************
****************@***
********************
******************@*
********************
```

## Q4

ASCIIコードだけを使ったワンライナーで「おはようございます」と出力してください。手段は問いません。


## Q5

2つの自然数の最小公倍数を求めるワンライナーを考えてください。


## Q6

`echo あいうえお` から始めて `ぁぃぅぇぉ` をワンライナーで出力してください。


## Q7

次のようなアニメーションを作ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/BChVPQNDNe0" frameborder="0" allowfullscreen></iframe>


## Q8

次のファイル[sd.txt](sd.txt)について、全角5文字で折り返してください。半角は0.5文字扱いで、ぴったり5文字で合わない時は4.5文字で折り返してください。

```sd.txt
Software Designの「シェル芸人からの
挑戦状」は絶好調なんですが、もう
ちょっとTwitterで読んだ感想を述べて
いただければと。
```

出力の例です。

```
Software D
esignの「
シェル芸人
からの挑戦
状」は絶好
調なんです
が、もうち
ょっとTwit
terで読ん
だ感想を述
べていただ
ければと。
```

## Q9

元素の周期表のCSVファイルを作ってください。

![](pt.png)

```csv
H,,,,,,,,,,,,,,,,,He
Li,Be,,,,,,,,,,,B,C,N,O,F,Ne
Na,Mg,,,,,,,,,,,Al,Si,P,S,Cl,Ar
K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr
Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe
Cs,Ba,L,Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn
Fr,Ra,A,Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og

L,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu
A,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr
```

