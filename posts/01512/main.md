---
Keywords: シェルスクリプト,DTP,reSt,reStructuredText,sed,Sphinx,編集者大満足
Copyright: (C) 2017 Ryuichi Ueda
---

# reStの一部の記号を消すシェルスクリプト作ったった
以前から燻りながら地味にページ数を稼いでいる「<a href="http://blog.ueda.asia/?p=1380" title="出版社に送る原稿には日本語と英単語の間にスペースを入れない方が良いらしいので贖罪のためにシェル芸やります。" target="_blank">これ</a>」と「<a href="http://blog.ueda.asia/?p=1486" title="出版社に送る原稿には日本語と英単語の間にスペースを入れない方が良いらしいのであるが、ではどうしろと？" target="_blank">これ</a>」ですが、あまり引っ張るのもよろしくないので私なりに解決しました。


\@tcsh氏からSphinx陣営に引き込まれそうになりましたが、私はそんなにでかいPythonのコードを書いた事も無ければ、研究しないと数年後に失職する身分なので<span style="color:red">逃げます</span>。

Python書かなくても、私については次のようなシェルスクリプトを原稿のディレクトリに置いておけば事足ります。reStの*前後の空白を*ごと潰し、2連バッククォートを取り去って標準出力に出します。適当ですが、何かあったらまた改造すりゃいいだけの話です。

```bash
uedamac:pub ueda$ cat remove_space 
#!/bin/bash

sed 's/ \\*//g'	|
sed 's/\\* //g'	|
sed 's/^\\*//'	|
sed 's/\\*$//'	|
sed 's/ *`` *//g'
```

つかってみましょう。

```bash
uedamac:pub ueda$ echo '``だっ`` *ふん* だ' | ./remove_space > ./for_pub.txt
uedamac:pub ueda$ cat for_pub.txt
だっふんだ
```

for_pub.txtとSphinxで作ったHTMLを編集様に送る事にします。数ヶ月後に、1ページにデカデカと「だっふんだ」と書かれた雑誌が出版されます。南無阿弥陀仏。

やっぱり、ライブラリの中にいろいろ書くよりも、こっちの方が私には性に合っています。Sphinxも、もっとコマンド仕立てにすればいいのに・・・（ボソ）。


だっふんだ。
