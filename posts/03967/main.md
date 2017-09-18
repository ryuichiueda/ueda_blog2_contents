---
Keywords:シャレにならん,シェルスクリプト,bash,脆弱性
Copyright: (C) 2017 Ryuichi Ueda
---
# 先程から騒ぎになっているbashの脆弱性について
確認しました（苦笑）<br />
<br />
（追記: envを抜いてましたが、それだとCシェル系で確認できないので加えました）<br />
[bash]<br />
ueda\@remote:~$ env x='() { :;}; echo vulnerable' bash -c 'echo this is a test'<br />
vulnerable<br />
this is a test<br />
[/bash]<br />
<br />
<!--more--><br />
<br />
最初のワンライナーでなにがおこってるかというと、xの値であるはずの「() { :;}; echo vulnerable」の、echo vulnerableの部分がなぜか実行されています。<br />
<br />
bashの文法ではシングルクォートで囲んだ中のものは何がどう書いてあっても単なる文字列であって、evalとかshとかに突っ込まない限り実行されるわけはないので、これは実装ミスかと。（と、書いたのですが環境変数に関数を仕込めるという仕様があるという話を初めて聞いて愕然と・・・。いま慌てて調べてます。不勉強すんません。）<br />
<br />
例えばこういうものをファイルに書いてcatしても、catの他に何かプログラムが立ち上がるということは理屈の上ではありませんが、それと同じようなことが起こっているということです。<br />
<br />
あんまりローレベルのところを知っているわけでもないのですが、文法からすれば実装ミスです（いや、そうとも言えないかも。ということで今は疑いのあるものは止めてます。）。文法自体の問題ではないので、パッチがすぐに出ているようです。パッチを当てるとこうなります。<br />
<br />
[bash]<br />
[ueda\@centos ~]$ x='() { :;}; echo vulnerable' bash -c 'echo this is a test'<br />
bash: warning: x: ignoring function definition attempt<br />
bash: error importing function definition for `x'<br />
this is a test<br />
[/bash]<br />
<br />
文字列なんだからワーニング出すのどうなんだと思いますが、とりあえずはアップデートを。（あのディストリビューションがまだなんですけど・・・なんとかなりませんかね？？？みんな寝てるんですかね？？？地球の裏側は昼ですよね？？？）<br />
<br />
↓あのディストリビューション<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>Ubuntu users can do this to fix the exploit:&#10;&#10;sudo apt-get update&#10;sudo apt-get --only-upgrade install bash</p>&mdash; kacy fortner (\@kacyf) <a href="https://twitter.com/kacyf/status/514813590348763136">September 24, 2014</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<br />
<h2>以下余談</h2><br />
<br />
あとちょっと分かりませんが、shでも環境によっては？？？ちょっとこれは分かりません。あ、分かった。後ろのbashですね。失礼しました。<br />
<br />
[bash]<br />
freebsd10 /home/ueda$ sh<br />
$ x='() { :;}; echo vulnerable' bash -c &amp;amp;amp;amp;amp;amp;quot;echo this is a test&amp;amp;amp;amp;amp;amp;quot; #&amp;amp;amp;amp;amp;amp;lt;-bashじゃんかwww（ごめんなさい）<br />
vulnerable<br />
this is a test<br />
###大丈夫###<br />
freebsd10 /home/ueda$ sh<br />
$ x='() { :;}; echo vulnerable' sh -c &amp;amp;amp;amp;amp;amp;quot;echo this&amp;amp;amp;amp;amp;amp;quot;<br />
this<br />
[/bash]<br />
<br />
dashも？？？と思ったけどこれもbashを後ろで呼び出しているからでした。アホです。<br />
<br />
[bash]<br />
ueda\@ubuntu:~$ dash<br />
$ x='() { :;}; echo vulnerable' bash -c &amp;amp;amp;amp;amp;amp;quot;echo this is a test&amp;amp;amp;amp;amp;amp;quot; <br />
vulnerable<br />
this is a test<br />
###これも大丈夫です###<br />
ueda\@ubuntu:~$ dash<br />
$ x='() { :;}; echo vulnerable' sh -c &amp;amp;amp;amp;amp;amp;quot;echo this&amp;amp;amp;amp;amp;amp;quot;<br />
this<br />
[/bash]<br />
<br />
取り急ぎ。眠い。
