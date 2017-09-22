---
Copyright: (C) Ryuichi Ueda
---


# Tera TermをWindowsにインストールしてからssh接続するまで
なぜ書くか: 自分のいろんな書籍や記事から参照するためです。いちいち本や記事に書くとページがかさむので・・・

<h2>ダウンロード</h2>
Tera Termで検索をかけてダウンロードページに行きます。今回は窓の杜を使います。

<a href="http://forest.watch.impress.co.jp/library/software/utf8teraterm/" target="_blank" rel="noopener">http://forest.watch.impress.co.jp/library/software/utf8teraterm/</a>

Tera Termにはいろいろ系統が存在して、Tera TermとTera Term ProやTera Term ポータブル版というものがありますが、通常はTera Termを選択してダウンロードします。

<h2>インストール</h2>

インストーラ（今回はteraterm-4.95.exe）をダウンロードしたら、ダブルクリックします。インストールを許可するかどうか聞いてくるので、許可するとインストールが始まります。

<h3>言語の選択</h3>


日本語を選択し、次に進みます。

<a href="/wp-content/uploads/2017/08/453bc96d10f981af4516fcbbe445c51f.png"><img src="/wp-content/uploads/2017/08/453bc96d10f981af4516fcbbe445c51f.png" alt="" width="303" height="154" class="aligncenter size-full wp-image-10072" /></a>

<h3>使用許諾への同意</h3>

よく読んで同意でよければ同意して次に進みます。

<a href="/wp-content/uploads/2017/08/9ebd6f149e1318e4ade58a01569d1233.png"><img src="/wp-content/uploads/2017/08/9ebd6f149e1318e4ade58a01569d1233.png" alt="" width="503" height="389" class="aligncenter size-full wp-image-10075" /></a>

<h3>コンポーネントの選択</h3>

デフォルトで。

<a href="490e407d5ef61d99a4d6062162550a3f.png"><img src="490e407d5ef61d99a4d6062162550a3f.png" alt="" width="503" height="389" class="aligncenter size-full wp-image-10079" /></a>


<h3>言語の選択</h3>

また聞かれますが日本語で。


<h3>追加タスクの選択</h3>

お好みで、というところですが、デフォルトのままで大丈夫です。


<h3>インストール完了まで</h3>

あとは一本道です。

<h2>SSH接続</h2>

Tera Termを立ち上げると次のような画面が開きます。ホストにIPアドレス、サービスにSSHを選んで「OK」を押します。（以下、よく見るとスクリーンショットにあるIPアドレスがばらばらですが、気にしないでください。）

<a href="7dabc7aade40da8ca64cbc99873c7aac.png"><img src="7dabc7aade40da8ca64cbc99873c7aac.png" alt="" width="486" height="317" class="aligncenter size-full wp-image-10081" /></a>

OKを押すと、初めて接続する相手の場合、次のような画面がでます。ここで慌てず「続行」を押します。


<a href="09a547a286d739211afe1fd02a87d39a.png"><img src="09a547a286d739211afe1fd02a87d39a.png" alt="" width="396" height="478" class="aligncenter size-full wp-image-10082" /></a>

最後に、ユーザ名とパスワード（パスフレーズ）を聞いてきますので、正しく入力して「OK」を押します。

<a href="305153bf412bb8f43e72152d0374938d.png"><img src="305153bf412bb8f43e72152d0374938d.png" alt="" width="470" height="455" class="aligncenter size-full wp-image-10085" /></a>


うまくいけば次のようにログインできます。


<a href="6fb3a963ce7e8be0560aa20982d2e063.png"><img src="6fb3a963ce7e8be0560aa20982d2e063.png" alt="" width="677" height="495" class="aligncenter size-full wp-image-10084" /></a>



