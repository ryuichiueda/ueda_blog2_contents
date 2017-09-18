---
Copyright: (C) Ryuichi Ueda
---

# コンピュータとロボット（と生物）1/3
<h1 style="font-size:180%">コンピュータとロボット<br />（と生物）</h1><br />
<h2 style="font-size:150%">1/3</h2><br />
　<br />
　<br />
<strong>千葉工業大学 未来ロボティクス学科</strong><br />
<br />
<strong>上田 隆一</strong><br />
<br />
<!--nextpage--><br />
<br />
<h2>ロボット</h2><br />
　<br />
<ul><br />
	<li>今日の話は「自律ロボット」</li><br />
 <ul><br />
	<li>起動、終了の時以外、人が操作しない</li><br />
	<li>例: ロボットサッカー</li><br />
 </ul><br />
</ul><br />
<br />
<iframe width="420" height="315" src="https://www.youtube.com/embed/7FZyurrHgHQ" frameborder="0" allowfullscreen></iframe><br />
<br />
<br />
<!--nextpage--><br />
<br />
<h2>ロボットの部品</h2><br />
　<br />
<ul><br />
	<li>どんなものがあるでしょうか？</li><br />
 <ul><br />
	<li>モータ（アクチュエータ）</li><br />
	<li>センサ</li><br />
 <ul><br />
	<li>カメラ</li><br />
	<li>スイッチ</li><br />
 </ul><br />
	<li>電池・その他細かいもの</li><br />
	<li style="color:red">？？？</li><br />
 </ul><br />
</ul><br />
 　<br />
<p style="color:red;font-size:150%">Q. なんでしょう？</p><br />
<br />
<!--nextpage--><br />
<br />
<h2>A. コンピュータ</h2><br />
　　<br />
<ul><br />
	<li>普段我々がいじっているコンピュータ</li><br />
	<ul><br />
		<li>インターネット、LINE、Twitterをするもの</li><br />
		<li>YouTubeを見るもの</li><br />
	</ul><br />
　<br />
	<li>機械（ロボットを含む）の中のコンピュータ</li><br />
	<ul><br />
		<li>「組み込み用コンピュータ」や「マイコン」と呼ばれる</li><br />
		<ul><br />
			<li><a href="https://www.google.co.jp/search?q=%E3%83%9E%E3%82%A4%E3%82%B3%E3%83%B3&espv=2&biw=1147&bih=584&site=webhp&tbm=isch&source=lnms&sa=X&ved=0ahUKEwixv6aI-bzLAhVmG6YKHbN2BogQ_AUIBygC" target="_blank">例</a></li><br />
		</ul><br />
		<li style="color:red">実はこっちも多い</li><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>Q. コンピュータは<br />何してんの？</h2><br />
　<br />
例えばエアコンや電子レンジを考えてみましょう。<br />
　<br />
<ul><br />
	<li>センサとモータ（や電波を発生させる何か）を連携</li><br />
	<li>どうやって？</li><br />
	<ul><br />
		<li>時間を取るので「小学生相手に説明する方法」<br />を考えてみましょう。</li><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>説明できないので<br />話を変えます</h2><br />
　<br />
<ul><br />
	<li>動物は？</li><br />
	<ul><br />
		<li>センサの代わりに目、耳、舌、・・・</li><br />
		<li>モータの代わりに筋肉</li><br />
	</ul><br />
　<br />
	<li style="color:red">連携させているのは何？</li><br />
</ul><br />
　<br />
<!--nextpage--><br />
<br />
<h2>今日の話</h2><br />
　　<br />
<ul><br />
	<li>以下をごちゃまぜでお送りします</li><br />
	<ul><br />
		<li>ロボットからコンピュータを考える</li><br />
		<li>コンピュータからロボットを考える</li><br />
		<li>動物からロボットを考える</li><br />
		<li>動物からコンピュータを考える</li><br />
	</ul><br />
</ul><br />
　　　<br />
<div style="text-align:left;font-size:80%"><br />
出典: ニコライ A. ベルンシュタイン（著）、工藤和俊（訳）、佐々木正人（監訳）: <a href="http://www.kanekoshobo.co.jp/book/b184012.html" target="_blank">デクステリティ 巧みさとその発達</a>、金子書房、2003。<br /> （注意: 動物の分類が古いので現在のものとはズレがあります。）<br />
</div><br />
<br />
<!--nextpage--><br />
<br />
<h2>動物がなぜ存在するか</h2><br />
　　<br />
<ul><br />
	<li>動物（の原型）が誕生した理由は単純</li><br />
	<ul><br />
		<li>自身のコピーを作る仕組みを持ったもの<br />（たんぱく質の一種）が偶然できた</li><br />
		<li>コピーの速さが消滅する速さを上回ると増える</li><br />
	</ul><br />
　<br />
	<li>手口が巧妙化（進化）</li><br />
	<ul><br />
		<li>増える: 自身や自身のコピーの材料を外から持ってくる（食べる）</li><br />
		<li>消滅を防ぐ: 自身を食べる物や過酷な状況から遠ざかる（逃げる）</li><br />
		<li style="color:red">→よりうまく食べ、よりうまく逃げる動物が増える</li><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>動物以前・原生動物</h2><br />
　　　<br />
<ul><br />
	<li>自己増殖するたんぱく質が発生</li><br />
	<ul><br />
		<li>（講師注）それがどんなタンパク質かを<br />講師は知りませんが、ウイルスは細胞を持たず、<br />タンパク質で、自己増殖できます。</li><br />
	</ul><br />
　<br />
	<li>やがて袋状の「細胞」が発生</li><br />
	<li>単細胞生物</li><br />
	<ul><br />
		<li>単体でなんでもこなす</li><br />
		<ul><br />
			<li>食事、運動、増殖</li><br />
		</ul><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>腔腸動物・棘皮動物</h2><br />
サンゴ、海綿、ウミユリ、ヒトデ、ウニ<br />（「腔腸動物」は古い用語）<br />
　　<br />
<br />
<ul><br />
	<li>多細胞: 細胞がまとまって生活</li><br />
	<li>細胞間に役割分担</li><br />
	<ul><br />
		<li>表面の細胞は外部からの刺激を受ける</li><br />
		<li>内側の細胞は変形・収縮等の運動を持つ</li><br />
	</ul><br />
</ul><br />
<br />
<br />
<div style="float:left;width:50%;font-size:50%;line-height:100%"><br />
<a target="_blank" title="By Johan (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3ASponge-natural.jpg"><img width="280" alt="Sponge-natural" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Sponge-natural.jpg/512px-Sponge-natural.jpg"/></a><br /><br />
モクヨクカイメン<br /><span style="font-size:20%">By Johan (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons</span><br />
</div><br />
<div style="float:left;width:50%;font-size:50%;line-height:100%"><br />
<a title="By miya (miya&#039;s file) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AAsterina_pectinifera_ja01.jpg"><img width="200" alt="Asterina pectinifera ja01" src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Asterina_pectinifera_ja01.jpg"/></a><br /><br />
イトマキヒトデ<br /><span style="font-size:20%">By miya (miya's file) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons</span><br />
</div><br />
　<br />
<!--nextpage--><br />
<br />
<h2>情報の伝達が必要に</h2><br />
　<br />
<ul><br />
	<li>表面の細胞が外で起こったことを内側に伝える</li><br />
	<ul><br />
		<li>最初は化学物質がじわっと伝達</li><br />
	</ul><br />
　<br />
	<li style="color:red">次に電気刺激が使われるように</li><br />
	<ul><br />
		<li>化学物質より早く伝わる</li><br />
	</ul><br />
	<li style="color:red">神経系ができる</li><br />
	<ul><br />
		<li>電気信号を低損失で特定のところに届けやすい仕組み</li><br />
		<li style="color:red"><a href="https://commons.wikimedia.org/wiki/File:Complete_neuron_cell_diagram_en.svg" target="_blank">神経細胞・神経繊維</a></li><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>蠕虫</h2><br />
ヒル、サナダムシ（「蠕虫」は古い分類なので注意）<br />
　　<br />
<ul><br />
	<li>ソーセージ型</li><br />
	<ul><br />
		<li>「口側」・「肛門側」ができる。</li><br />
		<li style="color:red">この形がのちの進化に非常に重要</li><br />
	</ul><br />
　<br />
	<li>「口側」の方が敏感に</li><br />
	<ul><br />
		<li>食べるために口側から動く。先に危険と出会う。</li><br />
	</ul><br />
</ul><br />
<br />
<img width="30%" src="c46d1e381484567e3e6a7eb26f16c351.jpeg" /><span style="font-size:50%">写真は自粛</span><br />
<br />
<!--nextpage--><br />
<br />
<h2>遠隔受容器の発達</h2><br />
　　<br />
<br />
<ul><br />
	<li>口側の細胞が接触以外の刺激を受けるようになる</li><br />
	<ul><br />
		<li><span style="color:red">視覚</span>: 温度→熱射放（赤外線）→電磁波（可視光線）</li><br />
		<li><span style="color:red">嗅覚</span>: 化学物質との接触→飛散する化学物質</li><br />
		<li><span style="color:red">聴覚</span>: 物理的な接触→振動</li><br />
	</ul><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>移動運動の発達</h2><br />
　　<br />
<ul><br />
	<li>遠隔受容器の発達で運動にも変化</li><br />
	<ul><br />
		<li>遠隔受容器前</li><br />
		<ul><br />
			<li>餌や危険と接触した部分を引っ込ませる。<br />のたうちまわる。</li><br />
		</ul><br />
		<li>遠隔受容器後</li><br />
		<ul><br />
			<li>体全体を餌に向かわせたり危険から遠ざけたり</li><br />
		</ul><br />
	</ul><br />
　<br />
<br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>その後</h2><br />
　　<br />
<ul><br />
	<li>神経系の仕事が増えていく</li><br />
	<ul><br />
		<li>体の各部分の動きを<span style="color:red">統合</span>して意味のある動きにする</li><br />
		<li>餌や危険に対して動く時の<span style="color:red">計画</span>を立てる</li><br />
	</ul><br />
　<br />
	<li>遠隔受容器の近くに神経の塊ができる<span style="color:red">（脳）</span></li><br />
	<ul><br />
		<li>脳が大きくなっていく</li><br />
		<ul><br />
			<li><a href="http://www.brain.riken.jp/jp/youth/know/evolution" target="_blank">脳の進化 | 理化学研究所</a></li><br />
		</ul><br />
	</ul><br />
</ul><br />
<br />
<br />
<div style="text-align:right;font-size:80%"><br />
 <footer><a href="/?page_id=7863">戻る</a></footer><br />
</div>
