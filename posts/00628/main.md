---
Keywords: プログラミング,Haskell
Copyright: (C) 2017 Ryuichi Ueda
---

# HaskellでStringを使う場合とByteStringを使う場合の速度比較
ここ数ヶ月、だれに頼まれたわけでもなく、<a target="_blank" href="https://github.com/usp-engineers-community/Open-usp-Tukubai">open usp Tukubai</a>をPython版からHaskell版に置き換える作業をだらだら続けていますが、最近ようやくHaskellを書くのに不自由さを感じなくなってきました。

そうなってくるとスピードのことが気になります。Haskell には文字列を扱う String と、それよりもう少し抽象度の低い ByteString がありますが、スピードは抽象度の低い ByteString の方が速いそうです。しかし、Haskell初心者の脳みそに負担をかけるのは学習速度が遅くなるという個人的な戦略のため、現在リリースされているコマンドでは String を使っていました。しかし、そろそろ挑戦するべきかと。

んで、さっきdelfというコマンド内部で扱う文字列を String から ByteString （Data.ByteString.Lazy.Char8）に変更したので、スピードを計ってみました。delf は、こんなコマンドです。

```bash
bsd /home/ueda$ head -n 3 ~/TESTDATA 
2377 高知県 -9,987,759 2001年1月5日
2910 鹿児島県 5,689,492 1992年5月6日
8458 大分県 1,099,824 2010年2月22日
###二列目をdelfで除去###
bsd /home/ueda$ head -n 3 ~/TESTDATA | delf 2
2377 -9,987,759 2001年1月5日
2910 5,689,492 1992年5月6日
8458 1,099,824 2010年2月22日
```

便利でしょ？え？使いみちが分からない？分かれば便利なんです。

delfが便利かどうかはおいておいて、String版（delf.normal）とByteString版（delf.bs）を作ったので、比較してみます。ByteString 版は<a target="_blank" href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/delf.hs">ココ</a>にアップしてあります。

```bash
###python版###
bsd /home/ueda/tmp$ time head -n 100000 ~/TESTDATA | delf 2 > /dev/null

real	0m3.804s
user	0m3.814s
sys	0m0.031s
###string版###
bsd /home/ueda/tmp$ time head -n 100000 ~/TESTDATA | ./delf.normal 2 > /dev/null

real	0m1.661s
user	0m1.627s
sys	0m0.079s
###ByteString版###
bsd /home/ueda/tmp$ time head -n 100000 ~/TESTDATA | ./delf.bs 2 > /dev/null

real	0m0.773s
user	0m0.741s
sys	0m0.083s
```

おー。二倍以上。

これは仕事用ハイスペックマッシーンでやったらもっと速いに違いない。・・・ということで仕事用のサーバ（CentOS5.9）で try。

```bash
[usp@demo1 ueda]$ uname -a
Linux demo1 2.6.18-308.8.1.el5 #1 SMP Tue May 29 14:57:25 EDT 2012 x86_64 x86_64 x86_64 GNU/Linux
###有償ビジネス版###
[usp@demo1 ueda]$ time head -n 1000000 TESTDATA | delf 2 > /dev/null

real	0m0.448s
user	0m0.482s
sys	0m0.085s
###String版###
[usp@demo1 ueda]$ time head -n 1000000 TESTDATA | ./delf.normal 2 > /dev/null

real	0m5.465s
user	0m5.476s
sys	0m0.096s
###ByteString版###
[usp@demo1 ueda]$ time head -n 1000000 TESTDATA | ./delf.bs 2 > /dev/null

real	0m13.397s
user	0m13.406s
sys	0m0.075s
```

<strong style="color:red">あれれれれ？？？？遅いやんけ！！！</strong>何回やっても遅い。

うーん。終わり。

<h3>appendix: 個人メモ</h3>

bsdなら一発コンパイルだったのに、CentOS 5.9でコンパイルしようと思ったらめちゃくちゃ叱られたので、以下のようにコンパイル。
なんか遅い原因はここらへんに関係するのか？どうなのか？

```bash
[usp@demo1 ueda]$ cat /etc/redhat-release 
CentOS release 5.9 (Final)
[root@demo1 ~]# cabal install parsec
...
[usp@demo1 ueda]$ ghc delf.bs.hs 
[usp@demo1 ueda]$ ghc --make -o delf.normal delf.normal.hs
Linking delf.normal ...
```
