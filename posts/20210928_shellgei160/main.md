---
Keywords: シェル芸本, 日記
Copyright: (C) 2021 Ryuichi Ueda
---

# シェル・ワンライナー160本ノックのあとがきの代わり1（プログラミングの学習について）

（まだ書きかけですが、アップしながら書いていこうと思います。）

　[シェル・ワンライナー160本ノック](https://gihyo.jp/book/2021/978-4-297-12267-6)が昨日正式に出版日を迎えました。私の本はいつもクドすぎるあとがきがくっついているのですが、この本は

* 共著である
* 内容ぎっしりすぎてページ的にあとがきが入らなかった

という2点の理由から、あとがきがありません。ですので、思い入れの強いこの本について、あとがきの代わりにちょっとずつ何か書いていこうと思います。


## この本の最も簡潔な意図

　この本がどんな本かというと、普段からLinuxを使う人の場合、端末の上でいろいろできると便利なので、ちょっと難しい問題を解いて、自由自在に使えるようになろうという本です。例えば、`ls`を打って、

```
ueda@uedap1:~/ARCHIVE/PAPER_and_PRESENTATION$ ls
 20000425発表資料４.doc         IROS2005cam_ready                        jspe2003
 20000922研究会..doc            IROS2006                                 masterthesis
 20001130ミーティング資料       IROS2007JITSUKAWA                        mini2000.doc
 20001214ミーティング資料       ISCIE_PROBROBO                           mini2001
 20010508ミーティング資料.doc   JRSJ_SamplingQMDP                        mini2002
 20011023研究会資料             JSAI2015                                 mini2003
 20011207ミーティング資料       NikkeiLinux.tar.gz                       mini2004
 20011211研究会資料            'Playing Soccer with Legged Robots.ppt'   mini2005
 20020225勉強会資料             ROBOMEC2001                              mini2006
 20020423研究会資料             ROBOMEC2005                              mini2007
 20020529勉強会資料             ROBOMEC2006                              mini2008
 20020702研究会資料             RSJ2003                                  not_submitted
 20021022研究会資料             RSJ2004RESET                             ob2007
 20021023勉強会                 RSJ2004VQ                                rejected
 20021203研究会資料             RSJ2004ppt                               robosym2003
 20030218作業報告書             RSJ2005                                  rsj2003ppt
 20030409meeting                RSJ2006                                  rsj2007ppt
 20030422研究会資料             RSJ2007                                  smc2003abst
 20030611勉強会資料             RSJ2008                                  spie_ie_2004
 20030617研究会資料             RSJ2015                                  ssi2007_ppt
 ・・・
```

みたいにズラーッとファイルやディレクトリの名前が出てきたときに、「`ICRA`」か「`IROS`」で始まるディレクトリが見たいとします。このときに、

```
$ ls -d IROS* ICRA*
ICRA2002  ICRA2004     ICRA2005cam_ready  ICRA2008DP  IROS2003  IROS2004ppt        IROS2006
ICRA2003  ICRA2004ppt  ICRA2007DP         ICRA2015    IROS2004  IROS2005cam_ready  IROS2007JITSUKAWA
$ ls | grep -e ^ICRA -e ^IROS
ICRA2002
ICRA2003
ICRA2004
ICRA2004ppt
ICRA2005cam_ready
ICRA2007DP
ICRA2008DP
ICRA2015
IROS2003
IROS2004
IROS2004ppt
IROS2005cam_ready
IROS2006
IROS2007JITSUKAWA
```

みたいなコマンドが出てこないと、面倒くさいでしょうからできるようになりましょう、という単純な呼びかけのためにこの本を書いたり、シェル芸勉強会を開いたりしています。すごく単純な話です。勉強会ではこれよりも強烈に難しい問題が出ますが、それは、`ls -d IROS* ICRA*`や`ls | grep -e ^ICRA -e ^IROS`の便利さの先にさらなる便利さがあるからで、基本的にはまず`ls`からちょっと気の利いたことができれば十分という認識でいます。

　もちろん、GUIを使ってファイルやディレクトリを探してもいいのですが、