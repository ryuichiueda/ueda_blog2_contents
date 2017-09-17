# 正誤表 | シェルスクリプト高速開発技術入門
通報先: <a href="https://twitter.com/ryuichiueda" target="_blank">\@ryuichiueda</a>まで！<br />
<br />
<ul><br />
 <li><a href="#code">コードのまずいところ</a></li><br />
 <li><a href="#typo">typo</a></li><br />
 <li><a href="#additional">後日入った情報</a></li><br />
</ul><br />
<br />
<h1 id="code">コードのまずいところ</h1><br />
<ul><br />
 <li>p. 149のコード21行目<br />
<p>grepにオプションをインジェクションできる。これで何か悪い事が起こるかは不明。もし攻撃できたらご一報を。言い訳にはなりませんが、友の会のサイトはもうちょっと慎重に作ってあります。近日中に解説を・・・。</p><br />
 <ul><br />
<br />
 <li>誤: <br />
[bash]<br />
xargs grep -l &quot;$word&quot;<br />
[/bash]<br />
 </li><br />
 <li>正: <br />
[bash]<br />
xargs grep -l -- &quot;$word&quot;<br />
[/bash]<br />
 </li><br />
 </ul><br />
 </li><br />
 <li>p. 152のコード28行目<br />
<p>同上</p><br />
 <ul><br />
 <li>誤: <br />
[bash]<br />
xargs grep -lF &quot;$word&quot;<br />
[/bash]<br />
 </li><br />
 <li>正: <br />
[bash]<br />
xargs grep -lF -- &quot;$word&quot;<br />
[/bash]<br />
 </li><br />
 </ul><br />
 </li><br />
 <li>p. 198のtweetコマンドのコードの77行目<br />
<p>余計なスペースが入っており、つい最近までは動いていたのについ最近ダメになった。（本書発売日と同日の7/1？ひどい・・・。いや、悪いのは自分だが・・・）</p><br />
 <ul><br />
 <li>誤: <br />
[bash]<br />
curl -H &quot;Authorization : OAuth<br />
[/bash]<br />
 </li> <br />
 <li>正: <br />
[bash]<br />
curl -H &quot;Authorization: OAuth<br />
[/bash]<br />
 </li> <br />
 <li>発見者: <a href="https://twitter.com/kanariya0922" target="_blank">かなりや</a>さん</li><br />
 </ul><br />
 </li><br />
</ul><br />
<br />
<br />
<br />
<h1 id="typo">typo等</h1><br />
<br />
<table><br />
 <tr><br />
 <th>場所</th><br />
 <th>誤</th><br />
 <th>正</th><br />
 <th>発見者</th><br />
 <th>コメント</th><br />
 </tr><br />
 <tr><br />
 <td>21ページ真ん中の箇条書き</td><br />
 <td>お手元のFreeBSD の/user/ports/devel/open-<span style="color:red">sup</span>-tukubai/</td><br />
 <td>お手元のFreeBSD の/user/ports/devel/open-<span style="color:red">usp</span>-tukubai/</td><br />
 <td>上田</td><br />
 <td>ああああああ！！！</td><br />
 </tr><br />
 <tr><br />
 <td>38ページの箇条書きの2番目</td><br />
 <td>● #PasswordAuthentication yes の#を外してno をyes に変更</td><br />
 <td>● #PasswordAuthentication yes の#を外してyes をno に変更</td><br />
 <td><a href="https://twitter.com/ttaniguti" target="_blank">\@ttaniguti</a>様</td><br />
 <td>文脈で誤り訂正できると信じております・・・</td><br />
 </tr><br />
 <tr><br />
 <td>136ページの図4-3</td><br />
 <td>解像度が低い</td><br />
 <td><a href="index4output.png">こちらでご確認を。</a></td><br />
 <td><a href="https://twitter.com/mutz0623" target="_blank">\@mutz0623</a>様</td><br />
 <td>なぜこうなった？</td><br />
 </tr><br />
 <tr><br />
 <td>277ページのconvert -auto-orientの索引</td><br />
 <td>-outo-orient</td><br />
 <td>-auto-orient</td><br />
 <td><a href="https://twitter.com/maripogoda" target="_blank">\@MaripoGoda</a>閣下</td><br />
 <td>これはAUTO（文字通り）</td><br />
 </tr><br />
 <tr><br />
 <td>271ページ最下行の「~/list」</td><br />
 <td>どこにも作った形跡がない</td><br />
 <td>これは記事のリストなので、「$ cat out | self 1 | sort | uniq > list」で作成します。</td><br />
 <td><a href="https://twitter.com/papiron" target="_blank">\@papiron</a>さん</td><br />
 <td>ごめんなさいごめんなさい。</td><br />
 </tr><br />
</table><br />
<br />
<h1 id="additional">後日入った情報</h1><br />
<br />
<ul><br />
 <li>p. 193でリンク切れしていると言及したTwitterクライアント<br />
<p>作者様（<a href="https://twitter.com/mutuki" target="_blank">\@mutuki</a>さん）より連絡いただきました。現在は下記のURLから閲覧・利用可能です。</p><br />
 <ul><br />
 <li><a href="http://mutuki.github.io/Shellscriptter/" target="_blank">http://mutuki.github.io/Shellscriptter/</a></li><br />
 </ul><br />
 </li><br />
</ul><br />

