---
Copyright: (C) Ryuichi Ueda
---


# dashのコード解読メモ
勉強のためのメモ。コードにツッコミを入れる感じで。

注意: いちおう、私は「シェルの人」ということになってますが、使うのが中心なのでコード読み中のコメントは中途半端な知識でやってます。

バージョンは2011-11-20.07です。

<table>
 <tr>
 <th>ファイル名</th>
 <th>役割</th>
 <th>補足</th>
 </tr>
 <tr>
 <td><a href="http://blog.ueda.asia/?page_id=4223">main.h, main.c</a></td>
 <td>main関数がいる</td>
 <td>gotoがひでえ</td>
 </tr>
 <tr>
 <td><a href="http://blog.ueda.asia/?page_id=4276">shell.h</a></td>
 <td>全体で使う定義等が書いてある</td>
 <td>defineの嵐</td>
 </tr>
 <tr>
 <td><a href="http://blog.ueda.asia/?page_id=4346" title="dash/src/eval.h, eval.c">eval.h, eval.c</a></td>
 <td>main.cのcmdloop関数から呼ばれ、評価して実行する部分。</td>
 <td>重要。</td>
 </tr>
</table>
