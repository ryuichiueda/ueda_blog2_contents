---
Keywords: Linux,Ubuntu,疑似デバイス
Copyright: (C) 2017 Ryuichi Ueda
---

# Ubuntuで擬似デバイスをなんとかかんとか作って動かした
<!--:ja-->昨日はファイルシステムの説明で使おうかとUbuntuで擬似デバイス（/dev/nullとか/dev/zeroとかあれです。）を作ることに挑戦しました。やりっぱなしのもの（<a href="/?post=02133" title="グルー言語を作る作業を少し進めた" target="_blank">これとか</a>、あと研究）をたくさん差し置いてなんだかなーという感じですが、ちょっと必要になったので・・・

ソースからMakefileまで準備するのに3つサイトを参考にしました。

<ul>
 <li><a href="http://homepage3.nifty.com/rio_i/lab/driver24/00201chardev.html" target="_blank">http://homepage3.nifty.com/rio_i/lab/driver24/00201chardev.html</a></li>
 <li><a href="http://www.devdrv.co.jp/linux/kernel26-makefile.htm" target="_blank">http://www.devdrv.co.jp/linux/kernel26-makefile.htm</a></li>
 <li><a href="http://ledyba.org/2010/09/08233725.php" target="_blank">http://ledyba.org/2010/09/08233725.php</a></li>
</ul>

結局、ソースやらMakefileやらを揃えて、古くなった部分を書き換えて、コンパイルやビルドを通して・・・とやっているうちに若干ながら独自の部分ができたのでコードを晒しておきます。

<!--:--><!--:en-->昨日は講義で使おうかとUbuntuで擬似デバイスを作ることに挑戦しました。

ソースからMakefileまで準備するのに3つサイトを参考にしました。

結局、ソースやらMakefileやらを揃えてコンパイルやビルドを通しているうちに若干ながら独自の部分ができたのでコードを晒しておきます。

ソースが1ファイル、Makefileが1ファイルのミニマム構成でビルドできるようになってますので、コードをいじってくちゃくちゃにしているながらも何らかの役には立つかもしれません。尚、中身はまだ理解してないので何の責任もとれません。<!--:--><!--more--><!--:ja-->

私がそうなのですが、勉強する前に動かしてみないと不安で勉強できないというタイプの人間が世の中には多いので、（うまくいけば）何も考えなくてもmakeとmake installだけで動くようにしてます。（私の大学時代に受けた講義がそんなふうになっていれば、もっと真面目にやってたのになぁ・・・と5分ばかり茫然自失。）

baibai.cとMakefileが必要なファイルの全てです。あとはmakeとかが入ってない可能性があるのでapt-getしましょう。おそらく、比較的新しいバージョンのUbuntuならうまくいくはずです。

<a href="https://github.com/ryuichiueda/PseudoDevice/tree/master/BaiBaiDevice" target="_blank">https://github.com/ryuichiueda/PseudoDevice/tree/master/BaiBaiDevice</a>


動かしてみましょう。入力した数字を倍にして返します。ただ、このデバイスは少々不機嫌なのでちょっとでも入力がイレギュラーだと0を返してきます。あ、事故ってもごめんなさいしか言えませんのでご容赦ください。

```bash
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ make
make -C /usr/src/linux-headers-`uname -r` M=`pwd` V=1 modules
make[1]: ディレクトリ `/usr/src/linux-headers-3.2.0-53-generic' に入ります
（なんかすごいたくさんログ）
 ld -r -m elf_x86_64 -T /usr/src/linux-headers-3.2.0-53-generic/scripts/module-common.lds --build-id -o /home/ueda/GIT/PseudoDevice/BaiBaiDevice/baibai.ko /home/ueda/GIT/PseudoDevice/BaiBaiDevice/baibai.o /home/ueda/GIT/PseudoDevice/BaiBaiDevice/baibai.mod.o
make[1]: ディレクトリ `/usr/src/linux-headers-3.2.0-53-generic' から出ます
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ 
###make installでも設定できますが手動で###
###mknodでデバイスファイルを作る###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ sudo mknod /dev/baibai c 0x0123 0
###読み書きできるように###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ sudo chmod 0666 /dev/baibai
###モジュールをロード###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ sudo insmod ./baibai.ko
###使ってみる###
###入力###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ echo 12345 > /dev/baibai 
###出力###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ cat /dev/baibai 
24690
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ echo abc > /dev/baibai 
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ cat /dev/baibai 
0
###後始末（慎重に）make uninstallでもできます###
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ sudo rmmod ./baibai
ueda@remote:~/GIT/PseudoDevice/BaiBaiDevice$ sudo rm -f /dev/baibai
```

このエントリーでは動かすお手伝いをしたまでで、あとは上のURLのサイトに親切な解説があるので、そちらをご参考に。私も勉強になりましたので、感謝申し上げます。<!--:-->
