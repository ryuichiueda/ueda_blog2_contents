---
Copyright: (C) Ryuichi Ueda
---


# 第28回基準値を超えるシェル芸勉強会
<h1 style="font-size: 180%;">第28回基準値を超える<br />シェル芸勉強会</h1>
&nbsp;

<strong>千葉工業大学 未来ロボティクス学科 上田 隆一</strong>
<p>　</p>
<p><strong style="font-size: 80%;">「タイトルのネタが風化しているんですけど。」
「すぐに忘れる都民が悪い。」</strong></p>

<!--nextpage-->
<h2>近況</h2>
<ul>
 	<li>某書籍発売</li>
 	<li>Pythonの本だけどシェル芸をやらないと先に進めない仕様
<ul>
 	<li>そういうものなんだからしょうがない
<a href="8a48c79e8da2ecbe7fd10fca9a06c6d8.jpeg"><img class="aligncenter size-full wp-image-9609" src="8a48c79e8da2ecbe7fd10fca9a06c6d8.jpeg" alt="" width="4032" height="1230" /></a></li>
</ul>
</li>
</ul>
<!--nextpage-->
<h2>シェル芸とは</h2>
<a href="/?page=01434" target="_blank" rel="noopener noreferrer">マウスも使わず、ソースコードも残さず、GUIツールを立ち上げる間もなく、あらゆる調査・計算・テキスト処理をCLI端末へのコマンド入力一撃で終わらすこと。あるいはそのときのコマンド入力のこと。</a>

<!--nextpage-->
<h2>今回の問題</h2>
<ul>
 	<li>原稿の編集
<ul>
 	<li>sed（普通の使い方）</li>
 	<li>awk</li>
</ul>
</li>
</ul>
<!--nextpage-->
<h2>動機</h2>
<ul>
 	<li>先ほどの書籍執筆の最後にこんなことがあった。
<ol>
 	<li>自分はレイアウトを見ながらでないと書けないのでLaTeXで原稿を書いていた。</li>
 	<li>提出はプレインテキストで</li>
 	<li>上田「シェル芸でやりますよ！」</li>
 	<li>地獄
<ul>
 	<li>sedとgrepのパイプライン16連結等</li>
</ul>
</li>
 	<li><span style="color: #ff0000;">地獄を皆様におすそ分け ←ｲﾏｺｺ!!</span></li>
</ol>
</li>
</ul>
<!--nextpage-->
<h2>ということで</h2>
<ul>
 	<li>地獄</li>
</ul>
<!--nextpage-->
<h2>進め方</h2>
<ul>
 	<li>1問に15分強
<ul>
 	<li>問題に対するアプローチを考える</li>
 	<li>それを実現するコマンドやオプションがないか調査</li>
 	<li>手を動かす</li>
</ul>
</li>
 	<li>チーム分け（6人くらい）
<ul>
 	<li>玄人は教える</li>
 	<li>素人は教わる</li>
</ul>
</li>
 	<li>manを見ながら考えましょう</li>
</ul>
<!--nextpage-->
<h2>ということで開始</h2>
