---
Keywords: ||,シェルスクリプト,&amp;&amp;,bash,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->シェルの&&||パズル（解答編）<!--:-->
<!--:ja-->この前、<a href="http://blog.ueda.asia/?p=1094" title="シェルの&&||パズル" target="_blank">ここ</a>で、次の四つのコマンド列の出力を当てるクイズを無責任に出題しましたが、ちゃんと真面目に解答します。

[bash]
$ false &amp;&amp; true || true &amp;&amp; echo OK &lt;- 1
$ true &amp;&amp; true || false || echo OK &lt;- 2
$ true || true || true &amp;&amp; echo OK &lt;- 3
$ false &amp;&amp; true || false || echo OK &lt;- 4
[/bash]

<h2>考え方</h2>

シェルも一応言語ですが、基本、コマンドを起動するための道具なので、上から下、左から右に順にコマンドを起動していきます。それで、「&&」も「||」も、<strong style="color:red">左のコマンドの終了ステータスによって、右のコマンドを起動するかどうか決める</strong>ものですので、右側のコマンドが起動されるかどうかをまず考えます。例えば１の問題だと、最初の二つのコマンドは、falseが起動されてtrueが起動されません。

[bash]
$ false (&lt;-起動される) &amp;&amp; true (&lt;- 起動されない) || true &amp;&amp; echo OK 
[/bash]

次に考えなければいけないのは、&&や||が見ている終了ステータスは、<strong style="color:red">最後に起動したコマンドの終了ステータス</strong>だということです。ですから、１の問題では、次のように解釈できます。ですので、|| true のtrueは実行され、その次のecho も実行されます。

[bash]
$ false (&lt;-起動される) &amp;&amp; true (&lt;- 起動されない) || (&lt;- falseの終了ステータス) true &amp;&amp; echo OK 
[/bash]

これをおさえて左から右に慎重に考えて行けば、答えは特定できるかと思います。

[bash]
$ false &amp;&amp; true || true &amp;&amp; echo OK
OK
$ true &amp;&amp; true || false || echo OK
$ true || true || true &amp;&amp; echo OK
OK
$ false &amp;&amp; true || false || echo OK
OK
[/bash]

いかがだったでしょうか。<strong style="color:red">しかし、可読性に重大な問題が発生するので、ぜひ使わないようにしていただきたく。</strong>


おしまい。
<!--:-->
