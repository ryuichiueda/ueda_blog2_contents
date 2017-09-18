---
Copyright: (C) Ryuichi Ueda
---


# dashのコード解読メモ
勉強のためのメモ。コードにツッコミを入れる感じで。<br />
<br />
注意: いちおう、私は「シェルの人」ということになってますが、使うのが中心なのでコード読み中のコメントは中途半端な知識でやってます。<br />
<br />
バージョンは2011-11-20.07です。<br />
<br />
<table><br />
 <tr><br />
 <th>ファイル名</th><br />
 <th>役割</th><br />
 <th>補足</th><br />
 </tr><br />
 <tr><br />
 <td><a href="http://blog.ueda.asia/?page_id=4223">main.h, main.c</a></td><br />
 <td>main関数がいる</td><br />
 <td>gotoがひでえ</td><br />
 </tr><br />
 <tr><br />
 <td><a href="http://blog.ueda.asia/?page_id=4276">shell.h</a></td><br />
 <td>全体で使う定義等が書いてある</td><br />
 <td>defineの嵐</td><br />
 </tr><br />
 <tr><br />
 <td><a href="http://blog.ueda.asia/?page_id=4346" title="dash/src/eval.h, eval.c">eval.h, eval.c</a></td><br />
 <td>main.cのcmdloop関数から呼ばれ、評価して実行する部分。</td><br />
 <td>重要。</td><br />
 </tr><br />
</table>
