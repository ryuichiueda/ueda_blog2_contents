---
Copyright: (C) Ryuichi Ueda
---

# 第27回sedこわいシェル芸勉強会
<h1 style="font-size: 180%;">第27回sedこわいシェル芸勉強会</h1><br />
&nbsp;<br />
<br />
<strong>千葉工業大学 未来ロボティクス学科 上田 隆一</strong><br />
<br />
<strong style="font-size: 80%;">昨日、卒論の審査が終わりましたが</strong><br />
<br />
<!--nextpage--><br />
<h2>近況</h2><br />
<ul><br />
 	<li>某書籍がだいたい書き終わりました<br />
<ul><br />
 	<li>3月末出版予定</li><br />
</ul><br />
</li><br />
 	<li>たくさんの言語を使う無茶な本です。<span style="color: #ff0000;">大丈夫か？</span><br />
<ul><br />
 	<li>シェルスクリプト</li><br />
 	<li>Python</li><br />
 	<li>JavaScript（一部jQuery）</li><br />
 	<li>C言語</li><br />
 	<li>他、HTML（Bootstrap）, YAML, JSON</li><br />
</ul><br />
</li><br />
 	<li>乞うご期待</li><br />
</ul><br />
<!--nextpage--><br />
<h2>シェル芸とは</h2><br />
<a href="https://blog.ueda.asia/?page_id=1434" target="_blank">マウスも使わず、ソースコードも残さず、GUIツールを立ち上げる間もなく、あらゆる調査・計算・テキスト処理をCLI端末へのコマンド入力一撃で終わらすこと。あるいはそのときのコマンド入力のこと。</a><br />
<br />
<!--nextpage--><br />
<h2>今回の問題</h2><br />
<span style="color: #ff0000;">sed（変態）</span><br />
<br />
<!--nextpage--><br />
<h2>動機</h2><br />
<ol><br />
 	<li>某Software Designで執筆陣が集まったときに<br />
ebanさんの薫陶を受けた</li><br />
 	<li>自分以外みんな使い始めた</li><br />
 	<li>置いていかれた</li><br />
</ol><br />
<!--nextpage--><br />
<h2>ということで</h2><br />
<ul><br />
 	<li>自分自身を教育するためにsedの基本<span style="color: #ff0000;">（ただし置換を除く）</span>機能を調べて問題を作ってきました</li><br />
 	<li style="font-size: 50%;">基本ってなんだっけ？？？</li><br />
 	<li>解答はGNU sed限定です。特定方面の方ごめんなさい。</li><br />
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
