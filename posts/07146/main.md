---
Keywords: CLI,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題】第19回シェル芸3周年記念勉強会
<a href="https://blog.ueda.asia/?p=7068">解答はこちら。</a>

<h2>イントロ</h2>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/5gJY11MIKKvqWa" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ryuichiueda/19-54597865" title="第19回シェル芸勉強会イントロ" target="_blank">第19回シェル芸勉強会イントロ</a> </strong> from <strong><a href="//www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div>

<h2>問題で使うファイル等</h2>

前回からGitHubに置くようにしました。ファイルは

<a target="_blank" href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.19">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.19</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
今回はLinuxで解答例を作りましたので、BSD系、Macな方は以下の表をご参考に・・・。

<table>
 <tr>
 <th>Mac,BSD系</th>
 <th>Linux</th>
 </tr>
 <tr>
 <td>gdate</td>
 <td>date</td>
 </tr>
 <tr>
 <td>gsed</td>
 <td>sed</td>
 </tr>
 <tr>
 <td>tail -r</td>
 <td>tac</td>
 </tr>
 <tr>
 <td>gtr</td>
 <td>tr</td>
 </tr>
 <tr>
 <td>gfold</td>
 <td>fold</td>
 </tr>
</table>


<h2>Q1</h2>

端末で実行すると「1ppm」と出力されて、シェルスクリプトに書いて実行すると「40ppm」」と出力されるコマンドの組み合わせを考案してみましょう。フォルクスワーゲンは関係ありません。

<h2>Q2</h2>

二つの自然数を
```bash
$ echo 1 4
```
というようにechoで出力したあと、
```bash
4
3
2
1
2
3
4
```
というように間の数を埋めてみてください。

<h2>Q3</h2>

「1234567890」を含む13桁の数字（0から始まる数字を含む）をすべて列挙してみましょう。マイナンバー？何それ？

<h2>Q4</h2>

以下のデータについて、「すっとこどっこい」を「朴念仁」に変換しましょう。「すっとこどっこい」以外の部分の改行は除去してはいけません。

```bash
$ cat Q4 
この
すっとこどっ
こい
すこっと
どっこい
すっとこすっとこど
っこい
どっこいどっこい
すっとこどっこん
すっ
とこ
どっ
こい
```


<h2>Q5</h2>

<a href="https://blog.ueda.asia/?page_id=7123" target="_blank">https://blog.ueda.asia/?page_id=7123</a>
から、画像を抜き出して保存しましょう。

<h2>Q6</h2>

ファイルQ6は、Shift JISで記録された日本語を2進数にしたものです。ワンライナーで日本語に直してみましょう。

```bash
$ cat Q6
1000101001100101100100100110111010000010110010011001000110111101100011101110110110010001101111011001011101101100100000101100100010010011011100011001010010001110100000101010101010010001101101101000110111011101100000101011011110000010111010011000000101000010000011010000101010010011110000011000001011001001100101110100110010010110101111001000001011001000100000101110000010000010110011001000001011001101100101101110110010001011100001011001001101110001100101001000111010000010110001011000001010100000100000101110100110000001010000100000110100001010
```


<h2>Q7</h2>

bashでは変数SHLVLに、今使っているbashの深さ（子シェル:2, 孫シェル:3, ...）が入っています。echo $SHLVLで、100を出してみてください。

<h2>Q8</h2>

以下のワンライナーに加筆して、1000プロセスぐらい立ち上げた後で止めてみてください。<span style="color:red">壊しても良い環境で行ってください。</span>

```bash
$ : (){ : | : & }; :
```


