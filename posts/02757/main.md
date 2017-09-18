---
Keywords:コマンド,ワンライナー,UNIX/Linuxサーバ,小ネタ,シェル芸,シェル芸というには短すぎる
Copyright: (C) 2017 Ryuichi Ueda
---
# ロードアベレージの記録を毎秒つけるワンライナー
小ネタですが。Ubuntuで検証。<br />
<br />
[bash]<br />
hoge\@hoge:~$ while sleep 1 ; do echo $(date &quot;+%Y%m%d %H%M%S&quot;) $(cat /proc/loadavg) ; done <br />
20140414 143624 0.00 0.01 0.05 1/133 8622<br />
20140414 143625 0.00 0.01 0.05 1/133 8625<br />
20140414 143626 0.00 0.01 0.05 1/133 8628<br />
20140414 143627 0.00 0.01 0.05 1/133 8631<br />
20140414 143628 0.00 0.01 0.05 1/133 8634<br />
...<br />
（Ctrl+cで止める。）<br />
[/bash]<br />
<br />
ファイルに溜めたきゃdoneの後ろでリダイレクト。<br />
<br />
[bash]<br />
hoge\@hoge:~$ while sleep 1 ; do echo $(date &quot;+%Y%m%d %H%M%S&quot;) $(cat /proc/loadavg) ;\\<br />
 done &gt; loadavg<br />
（Ctrl+cで止める。）<br />
hoge\@hoge:~$ cat loadavg <br />
20140414 143059 0.00 0.01 0.05 1/133 8586<br />
20140414 143100 0.00 0.01 0.05 1/133 8589<br />
20140414 143101 0.00 0.01 0.05 1/133 8592<br />
20140414 143102 0.00 0.01 0.05 1/133 8595<br />
[/bash]<br />
<br />
<br />
では。
