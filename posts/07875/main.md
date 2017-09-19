---
Copyright: (C) Ryuichi Ueda
---


# コンピュータとロボット（と生物）2/3
<h1 style="font-size:180%">コンピュータとロボット<br />（と生物）</h1>
<h2 style="font-size:150%">2/3</h2>
　
　
<strong>千葉工業大学 未来ロボティクス学科</strong>

<strong>上田 隆一</strong>

<!--nextpage-->

<h2>Q. もう一度考えましょう</h2>
　
<ul>
	<li>ロボットや機械におけるコンピュータの役割は？</li>
	<li>生物との違いは？</li>
</ul>

<!--nextpage-->

<h2>コンピュータ・ロボット</h2>
　
<ul>
	<li>コンピュータ: センサの情報をモータの動きに変換</li>
	<li>ロボット: センサ・モータ・コンピュータが連携したもの</li>
　
	<li>生物の神経系・脳と役割は同じ。</li>
	<li>情報の伝達に使うのも電気信号なので同じ。</li>
 <ul>
		<li>もちろん構造は異なる。</li>
 </ul>
　
	<li>人間の欲望と共に進化中</li>
 <ul>
		<li>（しかし、ロボットが自己増殖し始めたら、<br />どうなるんでしょうね？）</li>
 </ul>
</ul>



<!--nextpage-->

<h2>もっとも簡単な<br />「ロボット」</h2>
　
<ul>
	<li><a href="https://youtu.be/KWoufBRGIls?t=1m5s" target="_blank">自動ドア</a></li>
 <ul>
	<li>単機能ながら洗練されたロボット</li>
	<li>これ、どうなってるんでしょう？</li>
 </ul>
　
	<li>センサがある。ドアを開くモータがある。</li>
</ul>

<!--nextpage-->

<h2>単純な回路の例</h2>

このままだと色々問題がありますが・・・

<img width="100%" src="f368e705bc87cc8ceeb01a8f2f474a5d-1024x484.jpeg" />

<ul>
	<li><a target="_blank" href="https://www.google.co.jp/search?q=%E3%83%AA%E3%83%AC%E3%83%BC&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimlr6nw8HLAhVTA44KHe8kDGoQ_AUIBygB&biw=895&bih=880">リレーって何？</a></li>
</ul>

<!--nextpage-->

<h2>構成要素</h2>

<ul>
	<li>センサ側</li>
	<ul>
		<li>反応すると小さい電流をON/OFF</li>
	</ul>
	<li>モータ側</li>
	<ul>
		<li>リレーのON/OFFでモータに電力を送る・送らない</li>
	</ul>
	<li style="color:red">リレーが自動のスイッチになる</li>
	<ul>
		<li>人の手が介在しないスイッチ</li>
		<li>入力から出力を導く（コンピュータの本質）</li>
	</ul>
</ul>

<img width="40%" src="f368e705bc87cc8ceeb01a8f2f474a5d-1024x484.jpeg" />

<!--nextpage-->

<h2>もっと凝るとどうなる？</h2>
　　　　　　
<ul>
	<li>人を絶対に挟まないようにセンサを増やそう、等</li>
　
	<li>バリエーションが増える</li>
	<ul>
		<li>両方反応したらON</li>
		<li>どっちかが反応したらON</li>
	</ul>
　
	<li>バリエーションを考えてみましょう</li>
	<ul>
		<li>電流の強弱は考えずとりあえずONとOFFだけ考える</li>
		<li style="color:red">ディジタル回路</li>
	</ul>
</ul>

<!--nextpage-->

<h2>ANDの回路</h2>
　　　　
<ul>
	<li>両方ONならONの回路</li>
	<ul>
		<li>使用例: 小さな虫に反応しないように二つセンサが反応したらドアを開く</li>
		<li>（センサもスイッチなので話がややこしくなるため、<br />以後、センサとモータを取り払った回路で考えます）</li>
	</ul>
</ul>

<img width="100%" src="43a4607003e2c01b75d16fc267e7a207.jpeg" />

<!--nextpage-->

<h2>ORの回路</h2>
　　　　
<ul>
	<li>どちらかがONならONの回路</li>
	<ul>
		<li>使用例: ドアの外と内のどちらかのセンサが反応したらドアを開く</li>
	</ul>
</ul>

<img width="100%" src="f031486ef7ba5daef919bb0698d061c5.jpeg" />

<!--nextpage-->

<h2>スイッチを小さく</h2>
　　　　
<ul>
	<li>リレーでANDやORなどの回路を組み合わせると<br />複数のセンサの反応から様々なモータの動かし方を<br />実現できそう</li>
	<ul>
		<li>回路を横に並べたり縦につないだり</li>
	</ul>
　
	<li>複雑な回路ではリレーの数が増える</li>
	<li>リレーは大きい、遅い、（昔は）壊れる</li>
</ul>

<!--nextpage-->

<h2>半導体への置き換え</h2>
　　　　
<ul>
	<li>より小さく、より低消費電力で、よりON/OFFを速く</li>
	<li>真空管→トランジスタ・電解効果トランジスタ（FET）</li>
　
	<li><a target="_blank" href="http://pc.watch.impress.co.jp/img/pcw/docs/541/584/html/10.jpg.html">例（MOSFET）</a></li>
</ul>

<!--nextpage-->

<h2>FET（MOSFET）</h2>
　　　　
<ul>
	<li>3本線が出ている（左図）</li>
　
	<li>N型: ゲートに電圧をかけるとスイッチON</li>
	<li>P型: ゲートに電圧をかけるとスイッチOFF</li>
	<li>右図: N型MOSとP型MOSの記号</li>
</ul>

<div style="float:left;font-size:20%;line-height:100%;width:30%">
<a title="By No machine-readable author provided. CyrilB~commonswiki assumed (based on copyright claims). [GFDL (http://www.gnu.org/copyleft/fdl.html), CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/) or CC BY-SA 2.5-2.0-1.0 (http://creativecommons.org/licenses/by-sa/2.5-2.0-1.0)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AD2PAK.JPG"><img alt="D2PAK" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/D2PAK.JPG/512px-D2PAK.JPG"/></a>
By No machine-readable author provided. CyrilB~commonswiki assumed (based on copyright claims). [GFDL (http://www.gnu.org/copyleft/fdl.html), CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/) or CC BY-SA 2.5-2.0-1.0 (http://creativecommons.org/licenses/by-sa/2.5-2.0-1.0)], via Wikimedia Commons</div>
<div style="float:left;font-size:20%;width:30%">
<img src="8e54ab680c42972adc3dac868b9d2278.jpeg" />
</div>


<!--nextpage-->

<h2>MOSFETを使った<br />ディジタル回路</h2>
　　　　
<ul>
	<li>P型とN型を組み合わせて使う</li>
	<ul>
		<li>complementary MOS, CMOS</li>
	</ul>
	<li>下の例: 入力をひっくり返す回路（NOTゲート）</li>
</ul>

<img width="50%" src="008b03578b8a92e420d294da7e83b215.jpeg" />

<!--nextpage-->

<h2>NOTゲートの電子回路</h2>

<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1713317-not-gate/embed#breadboard' width='650'></iframe>

<!--nextpage-->

<h2>NANDゲート</h2>

<ul>
	<li>組み合わせると入出力のパターンを自在に作成可能</li>
</ul>

<img width="100%" src="83decebed43c6b3565104403e4eba98c.jpeg" />


<!--nextpage-->

<h2>NANDゲートの回路</h2>

<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1717541-nand-gate/embed#breadboard' width='650'></iframe>

<!--nextpage-->

<h2>NANDゲートの汎用性</h2>
　　
<ul>
	<li>回路がややこしいので次のような記号で表しましょう。</li>
</ul>
<img width="30%" src="ac6a7be2066cda06c252afdf6c4236b6.jpeg" />
<ul>
	<li>NOT, AND, ORが作れる</li>
</ul>
<img width="100%" src="acebbc506806de018630fbef767336ca.jpeg" />
<ul>
	<li>他、過去の入力を覚える機能も作れる（記憶）</li>
</ul>

<!--nextpage-->

<h2>二進数</h2>
　　　
<ul>
	<li>ON/OFFも書くのが面倒なので1と0で表しましょう</li>
	<li>ON/OFFを幾つかまとめると数が表現できる</li>
	<ul style="font-size:70%">
		<li>OFF OFF (00): 0</li>
		<li>OFF ON (01): 1</li>
		<li>ON OFF (10): 2</li>
		<li>ON ON (11): 3</li>
	</ul>
	<li>計算できる（下図: 足し算の回路）</li>
	<ul>
		<li>さらに複雑な入出力が作れる</li>
	</ul>
</ul>

<div style="font-size:50%;line-height:100%">
<a href="NandFullAdder.png" rel="attachment wp-att-7981"><img src="NandFullAdder.png" alt="NandFullAdder" /></a><br />（public domain）
</div>

<!--nextpage-->

<h2>小さく、多く</h2>
　　
<ul>
	<li>IC, LSI</li>
	<ul>
		<li><a href="https://ja.wikipedia.org/wiki/NAND%E3%82%B2%E3%83%BC%E3%83%88#/media/File:4011_Pinout.svg" target="_blank">NANDゲート4個（ゲート数4）のIC</a></li>
		<li><a href="http://www.electronickitsbychaneyelectronics.com/prodinfo.asp?number=C7514" target="_blank">ICの外見</a></li>
		<li><a href="http://pc.watch.impress.co.jp/docs/2008/0620/vlsi02.htm" target="_blank">ゲート数を増やす研究が日々行われている</a></li>
	</ul>
</ul>

<!--nextpage-->

<h2>CPU（中央演算装置）</h2>
　　
<ul>
	<li>入出力関係が複雑になると回路を作るのが大変</li>
	<ul>
		<li>複雑な出力の例: ディスプレイに絵を描く等</li>
	</ul>
	<li>いくつかの汎用的な回路を使い回して様々な出力</li>
	<ul>
		<li>計算の手順を記憶しておく（プログラム）</li>
		<li>少しずつ出力を作っていく</li>
	</ul>
</ul>

<div style="text-align:center;font-size:20%;line-height:100%">
<a title="By smial (Own work) [FAL or GFDL 1.2 (http://www.gnu.org/licenses/old-licenses/fdl-1.2.html)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AIntel_core_i7_940_top_R7309478_wp.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Intel_core_i7_940_top_R7309478_wp.jpg/512px-Intel_core_i7_940_top_R7309478_wp.jpg" width="25%" /></a><br />By smial (Own work) [<a href="http://artlibre.org/licence/lal/en">FAL</a> or <a href="http://www.gnu.org/licenses/old-licenses/fdl-1.2.html">GFDL 1.2</a>], <a href="https://commons.wikimedia.org/wiki/File%3AIntel_core_i7_940_top_R7309478_wp.jpg">via Wikimedia Commons</a>
</div>

<!--nextpage-->
　
<h2>このパートのまとめ</h2>
　　　
<ul>
	<li>人が機械により便利なことをさせようとして<br />コンピュータが進化してきた</li>
	<ul>
		<li>リレー→プログラムできるCPU</li>
		<ul>
			<li><a href="https://github.com/ryuichiueda/NikkeiRaspiMouse/blob/master/201605/agents.py" target="_blank">ロボットのプログラム</a>（講師によるもの）</li>
			<li><a href="https://www.youtube.com/watch?v=nNwKVeCqjus" target="_blank">このプログラムで動いているロボット</a></li>
			<ul>
				<li style="font-size:50%">（今日はロボット自体の話が少なかったですね・・・）</li>
			</ul>
		</ul>
	</ul>
　
	<li>生物が増殖のために脳を大きくしたのと似ている（？）</li>
	<ul>
		<li>でも基本はスイッチ・センサ・モータである</li>
	</ul>
</ul>
　

<div style="text-align:right;font-size:80%">
 <footer><a href="/?page_id=7863">戻る</a></footer>
</div>
