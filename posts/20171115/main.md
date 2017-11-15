---
Keywords: 頭の中だだ漏らし,日記
Copyright: (C) 2017 Ryuichi Ueda
---

# 雑記（2017年11月15日）

シェル芸の日だった。

### 講義でシェル芸

講義でLEDを光らせるデバイスドライバを書いてもらったので、応用で「誰かがツイートしたらLEDを光らせる」というのをワンライナーで即興で作った。この講義、淡々とやっているので今までで一番盛り上がる。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ツイート連動LED <a href="https://twitter.com/hashtag/robosys2017?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2017</a> <a href="https://t.co/7HmlWWvBlb">pic.twitter.com/7HmlWWvBlb</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/930632891154829312?ref_src=twsrc%5Etfw">2017年11月15日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


このときのワンライナー。ツイートするときに変なところにスペースが入っていて動きません。観賞用。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">n=0; while sleep 3 ; do w3m -dump <a href="https://t.co/Yv5tjG41qe">https://t.co/Yv5tjG41qe</a> 2&gt; /dev/null | grep ツイート ツイート | head -n 1 &gt; /tmp/$n ; diff /tmp/$((n-1)) /tmp/$n &amp;&gt; /dev/null &amp;&amp; echo 0 &gt; /dev/myled0 || echo 1 &gt; /dev/myled0 ; n=$(( n + 1 )) ; done <a href="https://twitter.com/hashtag/robosys2017?src=hash&amp;ref_src=twsrc%5Etfw">#robosys2017</a> <a href="https://twitter.com/hashtag/%E3%82%B7%E3%82%A7%E3%83%AB%E8%8A%B8?src=hash&amp;ref_src=twsrc%5Etfw">#シェル芸</a></p>&mdash; Ryuichi Ueda (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/930634659691507712?ref_src=twsrc%5Etfw">2017年11月15日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### 研究室でシェル芸

IMUの出力が変だという話になって、28バイトずつデータを出力して目視するワンライナーを記述。0xFF0xFFから始まらなければならないのに、そうなっていないデータがあるのは捨てれば良いので良いとして、たまに出力が何秒も途切れることがあって、これは死ぬという結論に。

```bash
$ cat ~/Dropbox/imu_log.txt
$ while sleep 1 ; do LANG=C date ; sudo cat /dev/ttyACM0 | head -c 28 | xxd -ps ; done
Wed Nov 15 19:18:50 JST 2017
ffff5254394110bca1007bfd5bf8870b0b0009001000a600e000fa00
Wed Nov 15 19:18:51 JST 2017
ffff5254394110e19b0077fd5df88e0b0a0007000c00ab00e0000801
Wed Nov 15 19:18:52 JST 2017
ffff5254394110069d0078fd62f8950b0a0007000e00a500e1000201
Wed Nov 15 19:18:54 JST 2017
01ffff525439411055990078fd68f8bc0b0b0005000a00a700e500f9
Wed Nov 15 19:18:55 JST 2017
ffff5254394110599e007cfd57f8ba0b0a001000a700e3000201ffff
Wed Nov 15 19:19:06 JST 2017
01ffff5254394110aa9a0077fd62f8de0b090006000f00a900e40001
Wed Nov 15 19:19:16 JST 2017
ffff5254394110ad93007dfd64f8d00b0b000c0c0005000f00aa00de
Wed Nov 15 19:19:17 JST 2017
ffff5254394110fb98007cfd5ef8470c0c00020000ad00e700ff00ff
Wed Nov 15 19:19:18 JST 2017
ffff5254394110fe960076fd5af85a0c0900000f00a900e7000501ff
Wed Nov 15 19:19:20 JST 2017
ffff525439411025940077fd66f8690c0b00020000ab00e4000801ff
Wed Nov 15 19:19:21 JST 2017
01ffff525439411071910072fd63f8410c090005000f00a900e4000a
Wed Nov 15 19:19:41 JST 2017
ffff5254394110978c0074fd68f8a60c0b0005000f00ab00dd00fc00
Wed Nov 15 19:19:42 JST 2017
ffff52543941109b910073fd5cf8af0c090008000e00a200e0000101
Wed Nov 15 19:20:01 JST 2017
ffff5254394110c594007afd67f8090a0b0007000a00ab00dd000a01
^C
```

こういうものって足元が緩いと上物のコードがぐちゃぐちゃになるので、本当に勘弁してもらいたいところ。


### グリーン車のアルコール禍

書類を書くためと、シェル芸疲れのためにグリーン車で帰宅。グリーン車というと世間一般ではお上品な雰囲気が想像されると認識しているが、実際の普通列車のグリーン車は、居酒屋で飲むくらいなら770円払って電車で飲んでやれというオッサンが山ほど乗っていて良い雰囲気ではない。朝にガチアル中の人を見たこともある。飲んでいるものも、ちゃんとしたビールではなく、8割が発泡酒か、アルコール9%のストロングゼロで、臭いもひどければ、明らかに体調が悪そうな人も多い。

自分も酒を飲んだ後に電車に乗る人間であり、年に1,2度、グリーン車でビールを飲むので文句は言えないんだけど、文句というより雰囲気の悪さと臭いに圧倒されており。

分煙の次は文酒が来るのだろうか。


疲れた。寝る。
