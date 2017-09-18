---
Keywords:コマンド,CLI,sleep,字が・・・字が漏れちゃう・・・,シェル芸,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# sleep(1)で標準出力に栓をする
小ネタです。<a href="https://twitter.com/sleepcommand" target="_blank">私の手抜きbashボットでも活躍中のsleepコマンド</a>のアホな使い方です。<br />
<br />
あるソートのプログラムが出力直前に使っているメモリの量を調べるという、超ニッチな作業がありました。ニッチですが・・・確かにあったんですよ奥さん。<br />
<br />
んで、楽な方法をいろいろ探しているうちに、「出力する出口を塞いでしまえば出力直前でプログラムが止まるんじゃね？」という考えに至りました。<br />
<br />
readとかも試したのですが、sleep(1)がこの場合は一番手軽でした。例はyesの出力を止める例ですが、確かに指定した時間だけ止まります。<span style="color:red">1億秒待つのは大変でした。</span><br />
[bash]<br />
$ yes 高須クリニック | sleep 100000000<br />
###しばらく放置の後、別の端末で見てみる。###<br />
uedambp:RESULT ueda$ ps u <br />
USER PID %CPU %MEM VSZ RSS TT STAT STARTED TIME COMMAND<br />
ueda 97775 0.0 0.0 2442992 548 s005 S+ 10:55PM 0:00.00 sleep 100000000<br />
ueda 97774 0.0 0.0 2432752 536 s005 S+ 10:55PM 0:00.01 yes ?M^X?\\240M^H?M^B??M^C??M^CM^K?<br />
↑ｲﾀｰ!!!<br />
（以下略）<br />
[/bash]<br />
ちなみにsleepは読んだ入力を標準出力に出す訳ではないので、1億秒後には何も出てきません。<br />
<br />
<br />
ということで、次のように、作ったプログラム（input_string）が字をお漏らしする直前に使っているメモリの量が分かったのでした。<br />
[bash]<br />
$ seq 1 10000000 | ./input_string | sleep 10000000<br />
$ ps u | awk 'NR==1 || /input_string/' | grep -v awk<br />
 （略） VSZ RSS （略） COMMAND<br />
 （略） 6385120 3942652 （略） ./input_string<br />
[/bash]<br />
<br />
<br />
めでたしめでたし。しっかし、ニッチだ・・・。そして別のコマンドが出したい出したいと言っているのにそれを止めるsleep(1)に、ものすごいS属性があるような気がして妄想が止まらないのでした。<br />
<br />
<br />
アホくさいので寝る。<br />

