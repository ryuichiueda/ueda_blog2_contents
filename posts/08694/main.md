---
Keywords:ブチギレ,ICS,Raspberry,Windows,インターネット接続の共有
Copyright: (C) 2017 Ryuichi Ueda
---
# Raspberry Piを有線LANでWindows8に直結してWindows8経由でapt-getできるようにするまでの手順
講義のために慣れぬWindowsを触り、イライラで血圧が1000くらいになりながら分かった手順をまとめます。Windows8以降ならおそらく手順は同じです。タイトルにあるように、下の写真のようにラズパイとノートPCを接続して、ラズパイからインターネットに出られるようにします。（この写真のノートPCはWindowsではありませんが。）<br />
<br />
<a href="2016-09-06-14.01.24-e1473138838741.jpg"><img src="2016-09-06-14.01.24-e1473138838741-768x1024.jpg" alt="2016-09-06 14.01.24" width="660" height="880" class="aligncenter size-large wp-image-8699" /></a><br />
<br />
<h2>Raspberry Pi側の準備</h2><br />
<br />
有線LANがDHCPで使えるようにします。つまりデフォルトの状態にしておきます。<br />
<br />
<h2>Windows側の準備</h2><br />
<br />
Windowsマシンには無線LANと有線LANが必要です。上の写真のように有線側をラズパイに接続し、無線側でインターネットとやりとりします。<br />
<br />
<h2>接続の共有設定</h2><br />
<br />
Internet Connection Sharing（ICS）という機能らしいので、分からないことがあったらこのキーワードで調べるとよいかと。<br />
<br />
まず、下のようにお馴染みのネットワーク接続の一覧画面を出します。お馴染みと言っても、私はここにたどり着くまでにかなり時間を要しました。分からん。ここで一覧にブリッジ接続があったら次に進めないかもしれません。差し支えなければ削除します。<br />
<br />
<a href="8b194bf6e34de530ed6c5d03bdf93f1b.png"><img src="8b194bf6e34de530ed6c5d03bdf93f1b.png" alt="スクリーンショット 2016-09-06 11.30.53" width="861" height="502" class="aligncenter size-full wp-image-8702" /></a><br />
<br />
次に、Wi-Fiの方を右クリックし、「プロパティ」を選択します。で、タブに「共有」があることを確認し、選択します。<br />
<br />
<a href="3a08f3df59cc83974f92b7349c4c057e.png"><img src="3a08f3df59cc83974f92b7349c4c057e.png" alt="スクリーンショット 2016-09-06 13.24.23" width="435" height="519" class="aligncenter size-full wp-image-8705" /></a><br />
<br />
で、次のように「ネットワークのほかのユーザーに、このコンピューターのインターネット接続をとおしての接続を許可する」をチェックします。<br />
<br />
<a href="9e772a556f7565e0485d40c203fd0ee2.png"><img src="9e772a556f7565e0485d40c203fd0ee2.png" alt="スクリーンショット 2016-09-06 13.23.19" width="435" height="540" class="aligncenter size-full wp-image-8706" /></a><br />
<br />
で、右にある「設定」ボタンを押します。すると次のようにいくつかチェックボックスが出てきますので、HTTPとHTTPSをチェックしておきます。チェックの際、何かボックスが出てきますが、OKを押しておきます。<br />
<br />
<a href="f98465d7492d4d4aaf7dd45af11cd083.png"><img src="f98465d7492d4d4aaf7dd45af11cd083.png" alt="スクリーンショット 2016-09-06 13.23.38" width="435" height="519" class="aligncenter size-full wp-image-8707" /></a><br />
<br />
そして有線LAN同士でラズパイを接続し、ラズパイを再起動します。ちゃんとラズパイが立ち上がれば、Windows側のDHCPでIPアドレスが割り振られます。<br />
<br />
<br />
<h2>IPアドレスの確認</h2><br />
<br />
で、次にIPアドレスを調べます。まず、Windowsの有線LANのIPをipconfigで調べます。<br />
<a href="8abf4a44dadcdd944f1e330ccd948fff.png"><img src="8abf4a44dadcdd944f1e330ccd948fff.png" alt="スクリーンショット 2016-09-06 14.33.17" width="677" height="493" class="aligncenter size-full wp-image-8712" /></a><br />
<br />
192.168.137.1のようです。<br />
<br />
<br />
で、次にラズパイのIPアドレスを調べますが、これがなぜかひねくれたIPアドレスになってしまい、192.168.137.2,3,...と調べても見つかりませんでした・・・。ということで192.168.137.0をスキャンして調べる必要がありました。私は「<a href="http://forest.watch.impress.co.jp/library/software/advipscanner/" target="_blank">Advanced IP Scanner</a>」を使いました。<br />
<br />
このツールの画面にはIPアドレスの範囲を指定するテキストボックスがあるので、その中に範囲を指定してスキャンします。<br />
<br />
<a href="d09cac5d98f7da96c9f66ac77bbb1be2.png"><img src="d09cac5d98f7da96c9f66ac77bbb1be2.png" alt="スクリーンショット 2016-09-06 13.20.44" width="866" height="474" class="aligncenter size-full wp-image-8709" /></a><br />
<br />
なんで44なんでしょう・・・。<br />
<br />
<br />
ということで、<a href="https://osdn.jp/projects/ttssh2/" target="_blank">TeraTerm</a>で次のように192.168.137.44に接続し、ラズパイにログインできました。<br />
<br />
<a href="22819c9695f2d2091686ff5336b4498d.png"><img src="22819c9695f2d2091686ff5336b4498d.png" alt="スクリーンショット 2016-09-06 14.31.10" width="486" height="317" class="aligncenter size-full wp-image-8713" /></a><br />
<br />
<a href="266fdb2a1ac6f756ea0f4447e5996cb1.png"><img src="266fdb2a1ac6f756ea0f4447e5996cb1.png" alt="スクリーンショット 2016-09-06 13.22.38" width="470" height="455" class="aligncenter size-full wp-image-8710" /></a><br />
<br />
で、（ちゃんと/etc/resolv.confの設定が正しければ）apt-getできるようです。<br />
<br />
<a href="8d7ad0993e0a52982e592107c6ff03c7.png"><img src="8d7ad0993e0a52982e592107c6ff03c7.png" alt="スクリーンショット 2016-09-06 14.34.45" width="677" height="639" class="aligncenter size-full wp-image-8714" /></a><br />
<br />
おしまい。<br />
<br />
<span style="color:red">ってか、これだけのことを説明するためにこんなにスクリーンショットが必要なのはおかしい。</span><br />
<br />
<br />
おかしい。<br />
<br />
<br />
<br />
<br />

