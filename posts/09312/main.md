---
Copyright: (C) Ryuichi Ueda
---


# 第27回sedこわいシェル芸勉強会
<h1 style="font-size: 180%;">第27回sedこわいシェル芸勉強会</h1>
&nbsp;

<strong>千葉工業大学 未来ロボティクス学科 上田 隆一</strong>

<strong style="font-size: 80%;">昨日、卒論の審査が終わりましたが</strong>

<!--nextpage-->
<h2>近況</h2>
<ul>
 	<li>某書籍がだいたい書き終わりました
<ul>
 	<li>3月末出版予定</li>
</ul>
</li>
 	<li>たくさんの言語を使う無茶な本です。<span style="color: #ff0000;">大丈夫か？</span>
<ul>
 	<li>シェルスクリプト</li>
 	<li>Python</li>
 	<li>JavaScript（一部jQuery）</li>
 	<li>C言語</li>
 	<li>他、HTML（Bootstrap）, YAML, JSON</li>
</ul>
</li>
 	<li>乞うご期待</li>
</ul>
<!--nextpage-->
<h2>シェル芸とは</h2>
<a href="https://blog.ueda.asia/?page_id=1434" target="_blank">マウスも使わず、ソースコードも残さず、GUIツールを立ち上げる間もなく、あらゆる調査・計算・テキスト処理をCLI端末へのコマンド入力一撃で終わらすこと。あるいはそのときのコマンド入力のこと。</a>

<!--nextpage-->
<h2>今回の問題</h2>
<span style="color: #ff0000;">sed（変態）</span>

<!--nextpage-->
<h2>動機</h2>
<ol>
 	<li>某Software Designで執筆陣が集まったときに
ebanさんの薫陶を受けた</li>
 	<li>自分以外みんな使い始めた</li>
 	<li>置いていかれた</li>
</ol>
<!--nextpage-->
<h2>ということで</h2>
<ul>
 	<li>自分自身を教育するためにsedの基本<span style="color: #ff0000;">（ただし置換を除く）</span>機能を調べて問題を作ってきました</li>
 	<li style="font-size: 50%;">基本ってなんだっけ？？？</li>
 	<li>解答はGNU sed限定です。特定方面の方ごめんなさい。</li>
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
