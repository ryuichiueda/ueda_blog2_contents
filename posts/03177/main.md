---
Keywords:コマンド,シェルスクリプト,UNIX/Linuxサーバ,VirtualBox,寝る,もっといい方法ないですか？
Copyright: (C) 2017 Ryuichi Ueda
---

# 【徒労だったか？】VirtualBoxの仮想マシーンのクローン作りをシェルスクリプトでやっちまう
<h2>あとから追記</h2><br />
<br />
現在、この記事がきっかけでVirtualBox clonevmでクローン簡単に作れないかという話になってます。Facebookで。<br />
<br />
・・・で、次のようにクローンが作れると分かりました。<br />
<br />
[bash]<br />
uedambp:VirtualBox VMs ueda$ VBoxManage clonevm コピー元 --mode machine --name コピー先 --register<br />
[/bash]<br />
<br />
とりあえずVMのクローンが作りたくてここを訪れた人はこれでお願いします。<br />
<br />
ただ、tar.gzで固めてないとまっさらなOSかどうか分からないので、私は自分で書いたシェルスクリプト版を使います。<br />
<br />
以上。<br />
<br />
<br />
<hr /><br />
<br />
こんばんは。シェル芸勉強会でないシェル勉強会に興味シンシンの上田です。<br />
<br />
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>シェル芸じゃないシェルの勉強会来たけどここ前にシェル芸勉強会やったとこだｗ <a href="https://twitter.com/search?q=%23nanapi_study&amp;src=hash">#nanapi_study</a></p>&mdash; Kei Iwasaki (\@laugh_k) <a href="https://twitter.com/laugh_k/statuses/471959638506602496">May 29, 2014</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
ややこしい。<br />
<br />
<h2>本題</h2><br />
<br />
さて本題。本とかの検証でまっさらな環境を何回も作らなければならん状況になっております。（つまりやっと出版されそうだということなんですが・・・）。<br />
<br />
世の中にはVagrantなんて便利なものもありますし、VirtualBoxでマウスをクリクリすればクローンは作れますが、私といたしましてはシェルスクリプトで済ませるものはシェルスクリプトで済ませたいので、シェルスクリプトで済ませました。環境はMacです。<br />
<br />
まず、まっさらな仮想OSをtar.gzしておきます。<br />
<br />
<!--more--><br />
<br />
[bash]<br />
uedambp:VirtualBox VMs ueda$ ls *Virgin.tar.gz<br />
Ubuntu14.04DesktopVirgin.tar.gz Ubuntu14.04ServerVirgin.tar.gz<br />
[/bash]<br />
<br />
んで、次のようなシェルスクリプトでtar.gzファイルを展開することにしました。$1に展開したいtar.gzファイル、$2に新しい名前を指定します。単に解凍するだけだと二つ以上クローンしたときにUUIDがバッティングするので、UUIDを改ざんしています。エラー処理もショボく、力技なので解説するほどのものでもないですが、面白い所では、uuidgenコマンドでしょうか。あと、VirtualBox付属のVBoxManageコマンド。<br />
<br />
[bash]<br />
uedambp:VirtualBox VMs ueda$ cat vmcp <br />
#!/bin/bash -xv<br />
<br />
ORG=$(echo &quot;$1&quot; | sed 's;^./;;' | sed 's;\\.tar\\.gz$;;' | tr -d '/')<br />
<br />
tar zxvf &quot;$1&quot;<br />
<br />
###ディレクトリ名の変更###<br />
mv &quot;$ORG&quot; &quot;$2&quot; || exit 1<br />
cd &quot;$2&quot; || exit 1<br />
<br />
###ファイル名の変更###<br />
ls &quot;$ORG&quot;* |<br />
while read f; do<br />
 newfile=$(echo $f | sed &quot;s;$ORG;$2;&quot;)<br />
 mv &quot;$f&quot; &quot;$newfile&quot;<br />
done<br />
sed -i.bak1 &quot;s;$ORG;$2;g&quot; &quot;$2&quot;.vbox<br />
<br />
###HDDのUUID変更###<br />
OLDUUID=$(cat $2.vbox | grep &quot;HardDisk uuid&quot; | sed 's/^.*{//' | sed 's/}.*//')<br />
NEWUUID=$(VBoxManage internalcommands sethduuid &quot;$2.vdi&quot; | awk '{print $NF}')<br />
sed -i.bak2 &quot;s;$OLDUUID;$NEWUUID;g&quot; &quot;$2.vbox&quot;<br />
<br />
###本体のUUID変更###<br />
OLDUUID=$(cat $2.vbox | grep &quot;Machine uuid&quot; | sed 's/^.*{//' | sed 's/}.*//')<br />
NEWUUID=$(uuidgen)<br />
sed -i.bak3 &quot;s;$OLDUUID;$NEWUUID;g&quot; &quot;$2.vbox&quot;<br />
[/bash]<br />
<br />
理屈はいらねえ使ってみやがれということで、使います。<br />
<br />
[bash]<br />
uedambp:VirtualBox VMs ueda$ ./vmcp Ubuntu14.04ServerVirgin.tar.gz hoge<br />
uedambp:VirtualBox VMs ueda$ ./vmcp Ubuntu14.04ServerVirgin.tar.gz huga<br />
[/bash]<br />
<br />
両方立ち上げてみましょう。<br />
<br />
[bash]<br />
###Macの場合、こうやって開く###<br />
uedambp:VirtualBox VMs ueda$ open hoge/hoge.vbox<br />
uedambp:VirtualBox VMs ueda$ open huga/huga.vbox<br />
[/bash]<br />
<br />
実行！<br />
<br />
<a href="スクリーンショット-2014-05-29-22.13.42.png"><img src="スクリーンショット-2014-05-29-22.13.42-1024x640.png" alt="スクリーンショット 2014-05-29 22.13.42" width="625" height="390" class="aligncenter size-large wp-image-3185" /></a><br />
<br />
<span style="color:red">でけた。</span><br />
<br />
たぶん、大量に仮想マシンを複製しなければいけないときは、この方法が有効でしょう。ネットワークカードのMACアドレスも変えた方が良いし、変えることもできそうですが、とりあえず私はこれで満足なのでこれでやめときます。<br />
<br />
<br />
でけたので、寝る。<br />
<br />
（後記：これ、VirtualBoxのコマンドで一発でできるんだったらかなり恥ずかしいな・・・）
