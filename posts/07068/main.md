---
Keywords: USP友の会,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第19回シェル芸3周年記念勉強会
<a href="https://blog.ueda.asia/?p=7146">問題のみのページはこちら。</a>

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

<h2>解答</h2>

例えばbashであれば、シェルスクリプトではaliasが無効になることを利用できます。

```bash
$ alias hoge='echo 1ppm' &amp;&amp; hoge 2&gt; /dev/null || echo 40ppm
1ppm
###シェルスクリプトにすると挙動が変わる###
$ cat a
alias hoge='echo 1ppm' &amp;&amp; hoge 2&gt; /dev/null || echo 40ppm
$ ./a
40ppm
```

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

<h3>解答</h3>

```bash
$ echo 1 4 | while read a b ; do seq $a $b | tac ; seq $a $b ; done | uniq
4
3
2
1
2
3
4
###whileを使わない例###
$ echo 1 4 | xargs -n 2 seq | xargs | awk '{for(i=NF;i&gt;=1;i--)print $i;print}' | xargs -n 1 | uniq
4
3
2
1
2
3
4
###\@ebanさんの答え###
$ echo 1 4 | (read a b; seq $b -1 $a; seq $[a+1] $b)
```

<h2>Q3</h2>

「1234567890」を含む13桁の数字（0から始まる数字を含む）をすべて列挙してみましょう。マイナンバー？何それ？

<h3>解答</h3>

Macだと最初の答えば000や00が0に削られてうまく動かないようです。

```bash
$ echo 1234567890{000..999} {0..9}1234567890{00..99}
 {00..99}1234567890{0..9} {000..999}1234567890 | tr ' ' '\\n' 
$ seq -w 000 999 | sed 's/./&amp; /g' |
 awk '{a=&quot;1234567890&quot;; print $1$2$3a; print $1$2a$3; print $1a$2$3; print a$1$2$3}'
$ seq -w 000 999 |
 awk '{a=&quot;1234567890&quot;;for(i=0;i&lt;=3;i++)print substr($1,1,i)a substr($1,1+i)}'
```

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


<h3>解答</h3>

```bash
$ cat Q4 | tr '\\n' \@ |
sed 's/す\@*っ\@*と\@*こ\@*ど\@*っ\@*こ\@*い/朴念仁/g' | tr \@ '\\n' | awk '{print}'
この
朴念仁
すこっと
どっこい
すっとこ朴念仁
どっこいどっこい
すっとこどっこん
朴念仁
```


<h2>Q5</h2>

<a href="https://blog.ueda.asia/?page_id=7123" target="_blank">https://blog.ueda.asia/?page_id=7123</a>
から、画像を抜き出して保存しましょう。

<h3>解答</h3>

```bash
$ curl https://blog.ueda.asia/?page_id=7123 |
 grep -o '&lt;img src=&quot;data:[^&gt;]*/&gt;' | sed 's/^.*,//' |
 sed 's;&quot;/&gt;$;;' | base64 -d &gt; chinjyu.png
```

<h2>Q6</h2>

ファイルQ6は、Shift JISで記録された日本語を2進数にしたものです。ワンライナーで日本語に直してみましょう。

```bash
$ cat Q6
1000101001100101100100100110111010000010110010011001000110111101100011101110110110010001101111011001011101101100100000101100100010010011011100011001010010001110100000101010101010010001101101101000110111011101100000101011011110000010111010011000000101000010000011010000101010010011110000011000001011001001100101110100110010010110101111001000001011001000100000101110000010000010110011001000001011001101100101101110110010001011100001011001001101110001100101001000111010000010110001011000001010100000100000101110100110000001010000100000110100001010
```

<h3>解答</h3>

一例です。

```bash
$ echo -n &quot;obase=16;ibase=2;&quot; | cat - Q6 | sed 's/$/;\\n/' |
 bc | tr -d '\\\\\\n' | xxd -r -ps | nkf
各地に多種多様な賭博が存在する。
特に有名なものは野球賭博である。
```

<h2>Q7</h2>

bashでは変数SHLVLに、今使っているbashの深さ（子シェル:2, 孫シェル:3, ...）が入っています。echo $SHLVLで、100を出してみてください。

<h3>解答</h3>

自身を呼び出すシェルスクリプトを使って実行するのが一つの方法です。

```bash
$ echo 'echo $SHLVL &amp;&amp; [ $SHLVL -lt 100 ] &amp;&amp; ./a' &gt; a ; chmod +x a ; ./a
###\@papironさんの答え###
$ yes 'bash' | head -n 98 | (cat; echo 'echo $SHLVL') | bash
```

<h2>Q8</h2>

以下のワンライナーに加筆して、1000プロセスぐらい立ち上げた後で止めてみてください。<span style="color:red">壊しても良い環境で行ってください。</span>

```bash
$ : (){ : | : &amp; }; :
```

<h3>解答</h3>

変数を起動するたびにファイルに1行追記してやって条件を判定すれば、安心してください。止まりますよ。（失敗すると止まらないけど。）

```bash
###wc -l &lt; aをwc -l aとすると止まらないので注意###
$ : (){ echo a &gt;&gt; a ; [ &quot;$(wc -l &lt; a)&quot; -gt 1000 ] &amp;&amp; exit 0; : | : &amp; }; :
```



