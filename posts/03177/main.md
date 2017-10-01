---
Keywords: コマンド,シェルスクリプト,UNIX/Linuxサーバ,VirtualBox,寝る,もっといい方法ないですか？
Copyright: (C) 2017 Ryuichi Ueda
---

# 【徒労だったか？】VirtualBoxの仮想マシーンのクローン作りをシェルスクリプトでやっちまう
<h2>あとから追記</h2>

現在、この記事がきっかけでVirtualBox clonevmでクローン簡単に作れないかという話になってます。Facebookで。

・・・で、次のようにクローンが作れると分かりました。

```bash
uedambp:VirtualBox VMs ueda$ VBoxManage clonevm コピー元 --mode machine --name コピー先 --register
```

とりあえずVMのクローンが作りたくてここを訪れた人はこれでお願いします。

ただ、tar.gzで固めてないとまっさらなOSかどうか分からないので、私は自分で書いたシェルスクリプト版を使います。

以上。


<hr />

こんばんは。シェル芸勉強会でないシェル勉強会に興味シンシンの上田です。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>シェル芸じゃないシェルの勉強会来たけどここ前にシェル芸勉強会やったとこだｗ <a href="https://twitter.com/search?q=%23nanapi_study&amp;src=hash">#nanapi_study</a></p>&mdash; Kei Iwasaki (@laugh_k) <a href="https://twitter.com/laugh_k/statuses/471959638506602496">May 29, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ややこしい。

<h2>本題</h2>

さて本題。本とかの検証でまっさらな環境を何回も作らなければならん状況になっております。（つまりやっと出版されそうだということなんですが・・・）。

世の中にはVagrantなんて便利なものもありますし、VirtualBoxでマウスをクリクリすればクローンは作れますが、私といたしましてはシェルスクリプトで済ませるものはシェルスクリプトで済ませたいので、シェルスクリプトで済ませました。環境はMacです。

まず、まっさらな仮想OSをtar.gzしておきます。

<!--more-->

```bash
uedambp:VirtualBox VMs ueda$ ls *Virgin.tar.gz
Ubuntu14.04DesktopVirgin.tar.gz Ubuntu14.04ServerVirgin.tar.gz
```

んで、次のようなシェルスクリプトでtar.gzファイルを展開することにしました。$1に展開したいtar.gzファイル、$2に新しい名前を指定します。単に解凍するだけだと二つ以上クローンしたときにUUIDがバッティングするので、UUIDを改ざんしています。エラー処理もショボく、力技なので解説するほどのものでもないですが、面白い所では、uuidgenコマンドでしょうか。あと、VirtualBox付属のVBoxManageコマンド。

```bash
uedambp:VirtualBox VMs ueda$ cat vmcp 
#!/bin/bash -xv

ORG=$(echo "$1" | sed 's;^./;;' | sed 's;\\.tar\\.gz$;;' | tr -d '/')

tar zxvf "$1"

###ディレクトリ名の変更###
mv "$ORG" "$2" || exit 1
cd "$2" || exit 1

###ファイル名の変更###
ls "$ORG"* |
while read f; do
 newfile=$(echo $f | sed "s;$ORG;$2;")
 mv "$f" "$newfile"
done
sed -i.bak1 "s;$ORG;$2;g" "$2".vbox

###HDDのUUID変更###
OLDUUID=$(cat $2.vbox | grep "HardDisk uuid" | sed 's/^.*{//' | sed 's/}.*//')
NEWUUID=$(VBoxManage internalcommands sethduuid "$2.vdi" | awk '{print $NF}')
sed -i.bak2 "s;$OLDUUID;$NEWUUID;g" "$2.vbox"

###本体のUUID変更###
OLDUUID=$(cat $2.vbox | grep "Machine uuid" | sed 's/^.*{//' | sed 's/}.*//')
NEWUUID=$(uuidgen)
sed -i.bak3 "s;$OLDUUID;$NEWUUID;g" "$2.vbox"
```

理屈はいらねえ使ってみやがれということで、使います。

```bash
uedambp:VirtualBox VMs ueda$ ./vmcp Ubuntu14.04ServerVirgin.tar.gz hoge
uedambp:VirtualBox VMs ueda$ ./vmcp Ubuntu14.04ServerVirgin.tar.gz huga
```

両方立ち上げてみましょう。

```bash
###Macの場合、こうやって開く###
uedambp:VirtualBox VMs ueda$ open hoge/hoge.vbox
uedambp:VirtualBox VMs ueda$ open huga/huga.vbox
```

実行！

<a href="スクリーンショット-2014-05-29-22.13.42.png"><img src="スクリーンショット-2014-05-29-22.13.42-1024x640.png" alt="スクリーンショット 2014-05-29 22.13.42" width="625" height="390" class="aligncenter size-large wp-image-3185" /></a>

<span style="color:red">でけた。</span>

たぶん、大量に仮想マシンを複製しなければいけないときは、この方法が有効でしょう。ネットワークカードのMACアドレスも変えた方が良いし、変えることもできそうですが、とりあえず私はこれで満足なのでこれでやめときます。


でけたので、寝る。

（後記：これ、VirtualBoxのコマンドで一発でできるんだったらかなり恥ずかしいな・・・）
