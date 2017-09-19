---
Copyright: (C) Ryuichi Ueda
---


# 正誤表 | シェルスクリプト高速開発技術入門
通報先: <a href="https://twitter.com/ryuichiueda" target="_blank">\@ryuichiueda</a>まで！

<ul>
 <li><a href="#code">コードのまずいところ</a></li>
 <li><a href="#typo">typo</a></li>
 <li><a href="#additional">後日入った情報</a></li>
</ul>

<h1 id="code">コードのまずいところ</h1>
<ul>
 <li>p. 149のコード21行目
<p>grepにオプションをインジェクションできる。これで何か悪い事が起こるかは不明。もし攻撃できたらご一報を。言い訳にはなりませんが、友の会のサイトはもうちょっと慎重に作ってあります。近日中に解説を・・・。</p>
 <ul>

 <li>誤: 
[bash]
xargs grep -l &quot;$word&quot;
[/bash]
 </li>
 <li>正: 
[bash]
xargs grep -l -- &quot;$word&quot;
[/bash]
 </li>
 </ul>
 </li>
 <li>p. 152のコード28行目
<p>同上</p>
 <ul>
 <li>誤: 
[bash]
xargs grep -lF &quot;$word&quot;
[/bash]
 </li>
 <li>正: 
[bash]
xargs grep -lF -- &quot;$word&quot;
[/bash]
 </li>
 </ul>
 </li>
 <li>p. 198のtweetコマンドのコードの77行目
<p>余計なスペースが入っており、つい最近までは動いていたのについ最近ダメになった。（本書発売日と同日の7/1？ひどい・・・。いや、悪いのは自分だが・・・）</p>
 <ul>
 <li>誤: 
[bash]
curl -H &quot;Authorization : OAuth
[/bash]
 </li> 
 <li>正: 
[bash]
curl -H &quot;Authorization: OAuth
[/bash]
 </li> 
 <li>発見者: <a href="https://twitter.com/kanariya0922" target="_blank">かなりや</a>さん</li>
 </ul>
 </li>
</ul>



<h1 id="typo">typo等</h1>

<table>
 <tr>
 <th>場所</th>
 <th>誤</th>
 <th>正</th>
 <th>発見者</th>
 <th>コメント</th>
 </tr>
 <tr>
 <td>21ページ真ん中の箇条書き</td>
 <td>お手元のFreeBSD の/user/ports/devel/open-<span style="color:red">sup</span>-tukubai/</td>
 <td>お手元のFreeBSD の/user/ports/devel/open-<span style="color:red">usp</span>-tukubai/</td>
 <td>上田</td>
 <td>ああああああ！！！</td>
 </tr>
 <tr>
 <td>38ページの箇条書きの2番目</td>
 <td>● #PasswordAuthentication yes の#を外してno をyes に変更</td>
 <td>● #PasswordAuthentication yes の#を外してyes をno に変更</td>
 <td><a href="https://twitter.com/ttaniguti" target="_blank">\@ttaniguti</a>様</td>
 <td>文脈で誤り訂正できると信じております・・・</td>
 </tr>
 <tr>
 <td>136ページの図4-3</td>
 <td>解像度が低い</td>
 <td><a href="index4output.png">こちらでご確認を。</a></td>
 <td><a href="https://twitter.com/mutz0623" target="_blank">\@mutz0623</a>様</td>
 <td>なぜこうなった？</td>
 </tr>
 <tr>
 <td>277ページのconvert -auto-orientの索引</td>
 <td>-outo-orient</td>
 <td>-auto-orient</td>
 <td><a href="https://twitter.com/maripogoda" target="_blank">\@MaripoGoda</a>閣下</td>
 <td>これはAUTO（文字通り）</td>
 </tr>
 <tr>
 <td>271ページ最下行の「~/list」</td>
 <td>どこにも作った形跡がない</td>
 <td>これは記事のリストなので、「$ cat out | self 1 | sort | uniq > list」で作成します。</td>
 <td><a href="https://twitter.com/papiron" target="_blank">\@papiron</a>さん</td>
 <td>ごめんなさいごめんなさい。</td>
 </tr>
</table>

<h1 id="additional">後日入った情報</h1>

<ul>
 <li>p. 193でリンク切れしていると言及したTwitterクライアント
<p>作者様（<a href="https://twitter.com/mutuki" target="_blank">\@mutuki</a>さん）より連絡いただきました。現在は下記のURLから閲覧・利用可能です。</p>
 <ul>
 <li><a href="http://mutuki.github.io/Shellscriptter/" target="_blank">http://mutuki.github.io/Shellscriptter/</a></li>
 </ul>
 </li>
</ul>

