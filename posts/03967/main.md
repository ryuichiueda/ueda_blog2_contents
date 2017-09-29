---
Keywords: シャレにならん,シェルスクリプト,bash,脆弱性
Copyright: (C) 2017 Ryuichi Ueda
---

# 先程から騒ぎになっているbashの脆弱性について
確認しました（苦笑）

（追記: envを抜いてましたが、それだとCシェル系で確認できないので加えました）
```bash
ueda\@remote:~$ env x='() { :;}; echo vulnerable' bash -c 'echo this is a test'
vulnerable
this is a test
```

<!--more-->

最初のワンライナーでなにがおこってるかというと、xの値であるはずの「() { :;}; echo vulnerable」の、echo vulnerableの部分がなぜか実行されています。

bashの文法ではシングルクォートで囲んだ中のものは何がどう書いてあっても単なる文字列であって、evalとかshとかに突っ込まない限り実行されるわけはないので、これは実装ミスかと。（と、書いたのですが環境変数に関数を仕込めるという仕様があるという話を初めて聞いて愕然と・・・。いま慌てて調べてます。不勉強すんません。）

例えばこういうものをファイルに書いてcatしても、catの他に何かプログラムが立ち上がるということは理屈の上ではありませんが、それと同じようなことが起こっているということです。

あんまりローレベルのところを知っているわけでもないのですが、文法からすれば実装ミスです（いや、そうとも言えないかも。ということで今は疑いのあるものは止めてます。）。文法自体の問題ではないので、パッチがすぐに出ているようです。パッチを当てるとこうなります。

```bash
[ueda\@centos ~]$ x='() { :;}; echo vulnerable' bash -c 'echo this is a test'
bash: warning: x: ignoring function definition attempt
bash: error importing function definition for `x'
this is a test
```

文字列なんだからワーニング出すのどうなんだと思いますが、とりあえずはアップデートを。（あのディストリビューションがまだなんですけど・・・なんとかなりませんかね？？？みんな寝てるんですかね？？？地球の裏側は昼ですよね？？？）

↓あのディストリビューション

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>Ubuntu users can do this to fix the exploit:&#10;&#10;sudo apt-get update&#10;sudo apt-get --only-upgrade install bash</p>&mdash; kacy fortner (\@kacyf) <a href="https://twitter.com/kacyf/status/514813590348763136">September 24, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


<h2>以下余談</h2>

あとちょっと分かりませんが、shでも環境によっては？？？ちょっとこれは分かりません。あ、分かった。後ろのbashですね。失礼しました。

```bash
freebsd10 /home/ueda$ sh
$ x='() { :;}; echo vulnerable' bash -c &amp;amp;amp;quot;echo this is a test&amp;amp;amp;quot; #&amp;amp;amp;lt;-bashじゃんかwww（ごめんなさい）
vulnerable
this is a test
###大丈夫###
freebsd10 /home/ueda$ sh
$ x='() { :;}; echo vulnerable' sh -c &amp;amp;amp;quot;echo this&amp;amp;amp;quot;
this
```

dashも？？？と思ったけどこれもbashを後ろで呼び出しているからでした。アホです。

```bash
ueda\@ubuntu:~$ dash
$ x='() { :;}; echo vulnerable' bash -c &amp;amp;amp;quot;echo this is a test&amp;amp;amp;quot; 
vulnerable
this is a test
###これも大丈夫です###
ueda\@ubuntu:~$ dash
$ x='() { :;}; echo vulnerable' sh -c &amp;amp;amp;quot;echo this&amp;amp;amp;quot;
this
```

取り急ぎ。眠い。
