---
Keywords:CLI,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】第19回シェル芸3周年記念勉強会
<a href="https://blog.ueda.asia/?p=7068">解答はこちら。</a><br />
<br />
<h2>イントロ</h2><br />
<br />
<iframe src="//www.slideshare.net/slideshow/embed_code/key/5gJY11MIKKvqWa" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/19-54597865" title="第19回シェル芸勉強会イントロ" target="_blank">第19回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
<h2>問題で使うファイル等</h2><br />
<br />
前回からGitHubに置くようにしました。ファイルは<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.19">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.19</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<h2>環境</h2><br />
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。<br />
<br />
<table><br />
 <tr><br />
 <th>Mac,BSD系</th><br />
 <th>Linux</th><br />
 </tr><br />
 <tr><br />
 <td>gdate</td><br />
 <td>date</td><br />
 </tr><br />
 <tr><br />
 <td>gsed</td><br />
 <td>sed</td><br />
 </tr><br />
 <tr><br />
 <td>tail -r</td><br />
 <td>tac</td><br />
 </tr><br />
 <tr><br />
 <td>gtr</td><br />
 <td>tr</td><br />
 </tr><br />
 <tr><br />
 <td>gfold</td><br />
 <td>fold</td><br />
 </tr><br />
</table><br />
<br />
<br />
<h2>Q1</h2><br />
<br />
端末で実行すると「1ppm」と出力されて、シェルスクリプトに書いて実行すると「40ppm」」と出力されるコマンドの組み合わせを考案してみましょう。フォルクスワーゲンは関係ありません。<br />
<br />
<h2>Q2</h2><br />
<br />
二つの自然数を<br />
[bash]<br />
$ echo 1 4<br />
[/bash]<br />
というようにechoで出力したあと、<br />
[bash]<br />
4<br />
3<br />
2<br />
1<br />
2<br />
3<br />
4<br />
[/bash]<br />
というように間の数を埋めてみてください。<br />
<br />
<h2>Q3</h2><br />
<br />
「1234567890」を含む13桁の数字（0から始まる数字を含む）をすべて列挙してみましょう。マイナンバー？何それ？<br />
<br />
<h2>Q4</h2><br />
<br />
以下のデータについて、「すっとこどっこい」を「朴念仁」に変換しましょう。「すっとこどっこい」以外の部分の改行は除去してはいけません。<br />
<br />
[bash]<br />
$ cat Q4 <br />
この<br />
すっとこどっ<br />
こい<br />
すこっと<br />
どっこい<br />
すっとこすっとこど<br />
っこい<br />
どっこいどっこい<br />
すっとこどっこん<br />
すっ<br />
とこ<br />
どっ<br />
こい<br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
<a href="https://blog.ueda.asia/?page_id=7123" target="_blank">https://blog.ueda.asia/?page_id=7123</a><br />
から、画像を抜き出して保存しましょう。<br />
<br />
<h2>Q6</h2><br />
<br />
ファイルQ6は、Shift JISで記録された日本語を2進数にしたものです。ワンライナーで日本語に直してみましょう。<br />
<br />
[bash]<br />
$ cat Q6<br />
1000101001100101100100100110111010000010110010011001000110111101100011101110110110010001101111011001011101101100100000101100100010010011011100011001010010001110100000101010101010010001101101101000110111011101100000101011011110000010111010011000000101000010000011010000101010010011110000011000001011001001100101110100110010010110101111001000001011001000100000101110000010000010110011001000001011001101100101101110110010001011100001011001001101110001100101001000111010000010110001011000001010100000100000101110100110000001010000100000110100001010<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
bashでは変数SHLVLに、今使っているbashの深さ（子シェル:2, 孫シェル:3, ...）が入っています。echo $SHLVLで、100を出してみてください。<br />
<br />
<h2>Q8</h2><br />
<br />
以下のワンライナーに加筆して、1000プロセスぐらい立ち上げた後で止めてみてください。<span style="color:red">壊しても良い環境で行ってください。</span><br />
<br />
[bash]<br />
$ : (){ : | : &amp; }; :<br />
[/bash]<br />
<br />

