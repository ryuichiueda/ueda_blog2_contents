---
Copyright: (C) Ryuichi Ueda
---


# 第28回基準値を超えるシェル芸勉強会
<h1 style="font-size: 180%;">第28回基準値を超える<br />シェル芸勉強会</h1><br />
&nbsp;<br />
<br />
<strong>千葉工業大学 未来ロボティクス学科 上田 隆一</strong><br />
<p>　</p><br />
<p><strong style="font-size: 80%;">「タイトルのネタが風化しているんですけど。」<br />
「すぐに忘れる都民が悪い。」</strong></p><br />
<br />
<!--nextpage--><br />
<h2>近況</h2><br />
<ul><br />
 	<li>某書籍発売</li><br />
 	<li>Pythonの本だけどシェル芸をやらないと先に進めない仕様<br />
<ul><br />
 	<li>そういうものなんだからしょうがない<br />
<a href="8a48c79e8da2ecbe7fd10fca9a06c6d8.jpeg"><img class="aligncenter size-full wp-image-9609" src="8a48c79e8da2ecbe7fd10fca9a06c6d8.jpeg" alt="" width="4032" height="1230" /></a></li><br />
</ul><br />
</li><br />
</ul><br />
<!--nextpage--><br />
<h2>シェル芸とは</h2><br />
<a href="https://blog.ueda.asia/?page_id=1434" target="_blank" rel="noopener noreferrer">マウスも使わず、ソースコードも残さず、GUIツールを立ち上げる間もなく、あらゆる調査・計算・テキスト処理をCLI端末へのコマンド入力一撃で終わらすこと。あるいはそのときのコマンド入力のこと。</a><br />
<br />
<!--nextpage--><br />
<h2>今回の問題</h2><br />
<ul><br />
 	<li>原稿の編集<br />
<ul><br />
 	<li>sed（普通の使い方）</li><br />
 	<li>awk</li><br />
</ul><br />
</li><br />
</ul><br />
<!--nextpage--><br />
<h2>動機</h2><br />
<ul><br />
 	<li>先ほどの書籍執筆の最後にこんなことがあった。<br />
<ol><br />
 	<li>自分はレイアウトを見ながらでないと書けないのでLaTeXで原稿を書いていた。</li><br />
 	<li>提出はプレインテキストで</li><br />
 	<li>上田「シェル芸でやりますよ！」</li><br />
 	<li>地獄<br />
<ul><br />
 	<li>sedとgrepのパイプライン16連結等</li><br />
</ul><br />
</li><br />
 	<li><span style="color: #ff0000;">地獄を皆様におすそ分け ←ｲﾏｺｺ!!</span></li><br />
</ol><br />
</li><br />
</ul><br />
<!--nextpage--><br />
<h2>ということで</h2><br />
<ul><br />
 	<li>地獄</li><br />
</ul><br />
<!--nextpage--><br />
<h2>進め方</h2><br />
<ul><br />
 	<li>1問に15分強<br />
<ul><br />
 	<li>問題に対するアプローチを考える</li><br />
 	<li>それを実現するコマンドやオプションがないか調査</li><br />
 	<li>手を動かす</li><br />
</ul><br />
</li><br />
 	<li>チーム分け（6人くらい）<br />
<ul><br />
 	<li>玄人は教える</li><br />
 	<li>素人は教わる</li><br />
</ul><br />
</li><br />
 	<li>manを見ながら考えましょう</li><br />
</ul><br />
<!--nextpage--><br />
<h2>ということで開始</h2>
