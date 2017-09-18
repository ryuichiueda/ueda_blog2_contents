---
Keywords:USP友の会,勉強会,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第19回シェル芸3周年記念勉強会
<a href="https://blog.ueda.asia/?p=7146">問題のみのページはこちら。</a><br />
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
<h2>解答</h2><br />
<br />
例えばbashであれば、シェルスクリプトではaliasが無効になることを利用できます。<br />
<br />
[bash]<br />
$ alias hoge='echo 1ppm' &amp;&amp; hoge 2&gt; /dev/null || echo 40ppm<br />
1ppm<br />
###シェルスクリプトにすると挙動が変わる###<br />
$ cat a<br />
alias hoge='echo 1ppm' &amp;&amp; hoge 2&gt; /dev/null || echo 40ppm<br />
$ ./a<br />
40ppm<br />
[/bash]<br />
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
<h3>解答</h3><br />
<br />
[bash]<br />
$ echo 1 4 | while read a b ; do seq $a $b | tac ; seq $a $b ; done | uniq<br />
4<br />
3<br />
2<br />
1<br />
2<br />
3<br />
4<br />
###whileを使わない例###<br />
$ echo 1 4 | xargs -n 2 seq | xargs | awk '{for(i=NF;i&gt;=1;i--)print $i;print}' | xargs -n 1 | uniq<br />
4<br />
3<br />
2<br />
1<br />
2<br />
3<br />
4<br />
###\@ebanさんの答え###<br />
$ echo 1 4 | (read a b; seq $b -1 $a; seq $[a+1] $b)<br />
[/bash]<br />
<br />
<h2>Q3</h2><br />
<br />
「1234567890」を含む13桁の数字（0から始まる数字を含む）をすべて列挙してみましょう。マイナンバー？何それ？<br />
<br />
<h3>解答</h3><br />
<br />
Macだと最初の答えば000や00が0に削られてうまく動かないようです。<br />
<br />
[bash]<br />
$ echo 1234567890{000..999} {0..9}1234567890{00..99}<br />
 {00..99}1234567890{0..9} {000..999}1234567890 | tr ' ' '\\n' <br />
$ seq -w 000 999 | sed 's/./&amp; /g' |<br />
 awk '{a=&quot;1234567890&quot;; print $1$2$3a; print $1$2a$3; print $1a$2$3; print a$1$2$3}'<br />
$ seq -w 000 999 |<br />
 awk '{a=&quot;1234567890&quot;;for(i=0;i&lt;=3;i++)print substr($1,1,i)a substr($1,1+i)}'<br />
[/bash]<br />
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
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat Q4 | tr '\\n' \@ |<br />
sed 's/す\@*っ\@*と\@*こ\@*ど\@*っ\@*こ\@*い/朴念仁/g' | tr \@ '\\n' | awk '{print}'<br />
この<br />
朴念仁<br />
すこっと<br />
どっこい<br />
すっとこ朴念仁<br />
どっこいどっこい<br />
すっとこどっこん<br />
朴念仁<br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
<a href="https://blog.ueda.asia/?page_id=7123" target="_blank">https://blog.ueda.asia/?page_id=7123</a><br />
から、画像を抜き出して保存しましょう。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ curl https://blog.ueda.asia/?page_id=7123 |<br />
 grep -o '&lt;img src=&quot;data:[^&gt;]*/&gt;' | sed 's/^.*,//' |<br />
 sed 's;&quot;/&gt;$;;' | base64 -d &gt; chinjyu.png<br />
[/bash]<br />
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
<h3>解答</h3><br />
<br />
一例です。<br />
<br />
[bash]<br />
$ echo -n &quot;obase=16;ibase=2;&quot; | cat - Q6 | sed 's/$/;\\n/' |<br />
 bc | tr -d '\\\\\\n' | xxd -r -ps | nkf<br />
各地に多種多様な賭博が存在する。<br />
特に有名なものは野球賭博である。<br />
[/bash]<br />
<br />
<h2>Q7</h2><br />
<br />
bashでは変数SHLVLに、今使っているbashの深さ（子シェル:2, 孫シェル:3, ...）が入っています。echo $SHLVLで、100を出してみてください。<br />
<br />
<h3>解答</h3><br />
<br />
自身を呼び出すシェルスクリプトを使って実行するのが一つの方法です。<br />
<br />
[bash]<br />
$ echo 'echo $SHLVL &amp;&amp; [ $SHLVL -lt 100 ] &amp;&amp; ./a' &gt; a ; chmod +x a ; ./a<br />
###\@papironさんの答え###<br />
$ yes 'bash' | head -n 98 | (cat; echo 'echo $SHLVL') | bash<br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
以下のワンライナーに加筆して、1000プロセスぐらい立ち上げた後で止めてみてください。<span style="color:red">壊しても良い環境で行ってください。</span><br />
<br />
[bash]<br />
$ : (){ : | : &amp; }; :<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
変数を起動するたびにファイルに1行追記してやって条件を判定すれば、安心してください。止まりますよ。（失敗すると止まらないけど。）<br />
<br />
[bash]<br />
###wc -l &lt; aをwc -l aとすると止まらないので注意###<br />
$ : (){ echo a &gt;&gt; a ; [ &quot;$(wc -l &lt; a)&quot; -gt 1000 ] &amp;&amp; exit 0; : | : &amp; }; :<br />
[/bash]<br />
<br />
<br />

