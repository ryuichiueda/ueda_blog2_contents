---
Copyright: (C) Ryuichi Ueda
---


# コンピュータとロボット（と生物）1/3
<h1 style="font-size:180%">コンピュータとロボット<br />（と生物）</h1>
<h2 style="font-size:150%">1/3</h2>
　
　
<strong>千葉工業大学 未来ロボティクス学科</strong>

<strong>上田 隆一</strong>

<!--nextpage-->

<h2>ロボット</h2>
　
<ul>
	<li>今日の話は「自律ロボット」</li>
 <ul>
	<li>起動、終了の時以外、人が操作しない</li>
	<li>例: ロボットサッカー</li>
 </ul>
</ul>

<iframe width="420" height="315" src="https://www.youtube.com/embed/7FZyurrHgHQ" frameborder="0" allowfullscreen></iframe>


<!--nextpage-->

<h2>ロボットの部品</h2>
　
<ul>
	<li>どんなものがあるでしょうか？</li>
 <ul>
	<li>モータ（アクチュエータ）</li>
	<li>センサ</li>
 <ul>
	<li>カメラ</li>
	<li>スイッチ</li>
 </ul>
	<li>電池・その他細かいもの</li>
	<li style="color:red">？？？</li>
 </ul>
</ul>
 　
<p style="color:red;font-size:150%">Q. なんでしょう？</p>

<!--nextpage-->

<h2>A. コンピュータ</h2>
　　
<ul>
	<li>普段我々がいじっているコンピュータ</li>
	<ul>
		<li>インターネット、LINE、Twitterをするもの</li>
		<li>YouTubeを見るもの</li>
	</ul>
　
	<li>機械（ロボットを含む）の中のコンピュータ</li>
	<ul>
		<li>「組み込み用コンピュータ」や「マイコン」と呼ばれる</li>
		<ul>
			<li><a href="https://www.google.co.jp/search?q=%E3%83%9E%E3%82%A4%E3%82%B3%E3%83%B3&espv=2&biw=1147&bih=584&site=webhp&tbm=isch&source=lnms&sa=X&ved=0ahUKEwixv6aI-bzLAhVmG6YKHbN2BogQ_AUIBygC" target="_blank">例</a></li>
		</ul>
		<li style="color:red">実はこっちも多い</li>
	</ul>
</ul>

<!--nextpage-->

<h2>Q. コンピュータは<br />何してんの？</h2>
　
例えばエアコンや電子レンジを考えてみましょう。
　
<ul>
	<li>センサとモータ（や電波を発生させる何か）を連携</li>
	<li>どうやって？</li>
	<ul>
		<li>時間を取るので「小学生相手に説明する方法」<br />を考えてみましょう。</li>
	</ul>
</ul>

<!--nextpage-->

<h2>説明できないので<br />話を変えます</h2>
　
<ul>
	<li>動物は？</li>
	<ul>
		<li>センサの代わりに目、耳、舌、・・・</li>
		<li>モータの代わりに筋肉</li>
	</ul>
　
	<li style="color:red">連携させているのは何？</li>
</ul>
　
<!--nextpage-->

<h2>今日の話</h2>
　　
<ul>
	<li>以下をごちゃまぜでお送りします</li>
	<ul>
		<li>ロボットからコンピュータを考える</li>
		<li>コンピュータからロボットを考える</li>
		<li>動物からロボットを考える</li>
		<li>動物からコンピュータを考える</li>
	</ul>
</ul>
　　　
<div style="text-align:left;font-size:80%">
出典: ニコライ A. ベルンシュタイン（著）、工藤和俊（訳）、佐々木正人（監訳）: <a href="http://www.kanekoshobo.co.jp/book/b184012.html" target="_blank">デクステリティ 巧みさとその発達</a>、金子書房、2003。<br /> （注意: 動物の分類が古いので現在のものとはズレがあります。）
</div>

<!--nextpage-->

<h2>動物がなぜ存在するか</h2>
　　
<ul>
	<li>動物（の原型）が誕生した理由は単純</li>
	<ul>
		<li>自身のコピーを作る仕組みを持ったもの<br />（たんぱく質の一種）が偶然できた</li>
		<li>コピーの速さが消滅する速さを上回ると増える</li>
	</ul>
　
	<li>手口が巧妙化（進化）</li>
	<ul>
		<li>増える: 自身や自身のコピーの材料を外から持ってくる（食べる）</li>
		<li>消滅を防ぐ: 自身を食べる物や過酷な状況から遠ざかる（逃げる）</li>
		<li style="color:red">→よりうまく食べ、よりうまく逃げる動物が増える</li>
	</ul>
</ul>

<!--nextpage-->

<h2>動物以前・原生動物</h2>
　　　
<ul>
	<li>自己増殖するたんぱく質が発生</li>
	<ul>
		<li>（講師注）それがどんなタンパク質かを<br />講師は知りませんが、ウイルスは細胞を持たず、<br />タンパク質で、自己増殖できます。</li>
	</ul>
　
	<li>やがて袋状の「細胞」が発生</li>
	<li>単細胞生物</li>
	<ul>
		<li>単体でなんでもこなす</li>
		<ul>
			<li>食事、運動、増殖</li>
		</ul>
	</ul>
</ul>

<!--nextpage-->

<h2>腔腸動物・棘皮動物</h2>
サンゴ、海綿、ウミユリ、ヒトデ、ウニ<br />（「腔腸動物」は古い用語）
　　

<ul>
	<li>多細胞: 細胞がまとまって生活</li>
	<li>細胞間に役割分担</li>
	<ul>
		<li>表面の細胞は外部からの刺激を受ける</li>
		<li>内側の細胞は変形・収縮等の運動を持つ</li>
	</ul>
</ul>


<div style="float:left;width:50%;font-size:50%;line-height:100%">
<a target="_blank" title="By Johan (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3ASponge-natural.jpg"><img width="280" alt="Sponge-natural" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Sponge-natural.jpg/512px-Sponge-natural.jpg"/></a><br />
モクヨクカイメン<br /><span style="font-size:20%">By Johan (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons</span>
</div>
<div style="float:left;width:50%;font-size:50%;line-height:100%">
<a title="By miya (miya&#039;s file) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AAsterina_pectinifera_ja01.jpg"><img width="200" alt="Asterina pectinifera ja01" src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Asterina_pectinifera_ja01.jpg"/></a><br />
イトマキヒトデ<br /><span style="font-size:20%">By miya (miya's file) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons</span>
</div>
　
<!--nextpage-->

<h2>情報の伝達が必要に</h2>
　
<ul>
	<li>表面の細胞が外で起こったことを内側に伝える</li>
	<ul>
		<li>最初は化学物質がじわっと伝達</li>
	</ul>
　
	<li style="color:red">次に電気刺激が使われるように</li>
	<ul>
		<li>化学物質より早く伝わる</li>
	</ul>
	<li style="color:red">神経系ができる</li>
	<ul>
		<li>電気信号を低損失で特定のところに届けやすい仕組み</li>
		<li style="color:red"><a href="https://commons.wikimedia.org/wiki/File:Complete_neuron_cell_diagram_en.svg" target="_blank">神経細胞・神経繊維</a></li>
	</ul>
</ul>

<!--nextpage-->

<h2>蠕虫</h2>
ヒル、サナダムシ（「蠕虫」は古い分類なので注意）
　　
<ul>
	<li>ソーセージ型</li>
	<ul>
		<li>「口側」・「肛門側」ができる。</li>
		<li style="color:red">この形がのちの進化に非常に重要</li>
	</ul>
　
	<li>「口側」の方が敏感に</li>
	<ul>
		<li>食べるために口側から動く。先に危険と出会う。</li>
	</ul>
</ul>

<img width="30%" src="c46d1e381484567e3e6a7eb26f16c351.jpeg" /><span style="font-size:50%">写真は自粛</span>

<!--nextpage-->

<h2>遠隔受容器の発達</h2>
　　

<ul>
	<li>口側の細胞が接触以外の刺激を受けるようになる</li>
	<ul>
		<li><span style="color:red">視覚</span>: 温度→熱射放（赤外線）→電磁波（可視光線）</li>
		<li><span style="color:red">嗅覚</span>: 化学物質との接触→飛散する化学物質</li>
		<li><span style="color:red">聴覚</span>: 物理的な接触→振動</li>
	</ul>
</ul>

<!--nextpage-->

<h2>移動運動の発達</h2>
　　
<ul>
	<li>遠隔受容器の発達で運動にも変化</li>
	<ul>
		<li>遠隔受容器前</li>
		<ul>
			<li>餌や危険と接触した部分を引っ込ませる。<br />のたうちまわる。</li>
		</ul>
		<li>遠隔受容器後</li>
		<ul>
			<li>体全体を餌に向かわせたり危険から遠ざけたり</li>
		</ul>
	</ul>
　

</ul>

<!--nextpage-->

<h2>その後</h2>
　　
<ul>
	<li>神経系の仕事が増えていく</li>
	<ul>
		<li>体の各部分の動きを<span style="color:red">統合</span>して意味のある動きにする</li>
		<li>餌や危険に対して動く時の<span style="color:red">計画</span>を立てる</li>
	</ul>
　
	<li>遠隔受容器の近くに神経の塊ができる<span style="color:red">（脳）</span></li>
	<ul>
		<li>脳が大きくなっていく</li>
		<ul>
			<li><a href="http://www.brain.riken.jp/jp/youth/know/evolution" target="_blank">脳の進化 | 理化学研究所</a></li>
		</ul>
	</ul>
</ul>


<div style="text-align:right;font-size:80%">
 <footer><a href="/?page=07863">戻る</a></footer>
</div>
