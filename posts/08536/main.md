---
Copyright: (C) Ryuichi Ueda
---


# JTF2016手順メモ
<h1 style="font-size:180%">ROS（robot operating system）を触ってみよう</h1>
　

<p>千葉工業大学 上田隆一</p>

<!--nextpage-->

<h2>本日の内容</h2>

<p>あり合わせ or 他人の資料ですみません orz</p>
　
<ul>
	<li>ROSとは（このスライド）</li>
	<li>あとは他のドキュメントに基づいて進めるところまで</li>
	<ul>
		<li><a href="http://www.slideshare.net/ryuichiueda/201512-56193642" target="_blank">インストールと動作確認</a></li>
		<li><a href="http://wiki.ros.org/ja/ROS/Tutorials/WritingPublisherSubscriber%28python%29" target="_blank">パブリッシャとサブスクライバ</a></li>
		<li><a href="http://wiki.ros.org/ja/ROS/Tutorials/CreatingMsgAndSrv" target="_blank">メッセージ・サービスを作る</a></li>
	</ul>
</ul>
　

<!--nextpage-->

<h2>ROSとは</h2>
　
<ul>
	<li>2007年からWillow Garage社にて公式に
開発が始まったロボット用ミドルウェア</li>
	<li>主にUbuntu上で動く</li>
</ul>

<!--nextpage-->

<h2>ROSの主たる機能</h2>
　
<ul>
	<li>機能はいくつかあるが、主な機能はプロセス間通信</li>
　
	<ul>
		<li>ロボットのプログラムを一つのプロセスに押し込まないで、複数のプロセスに分けて処理させる</li>
		<ul>
　
			<li>例: モータに指令を出すプログラム、センサの値を読むプログラム、センサからモータの出力を決めるプログラム・・・</li>
		</ul>
	</ul>

</ul>

<!--nextpage-->

<h2>プロセスを分ける
メリット・デメリット</h2>

<ul>
	<li>各プログラムで違う言語が使える</li>
	<ul>
		<li>例: モータの制御はC++で高速化、行動の場合分けはPythonで楽する</li>
		<li>別の言語で書かれたプログラムを連結しやすい</li>
		<li>コンポーネント化しやすい</li>
	</ul>
　
	<li>プロセス間のリアルタイム性は保証されない</li>
	<ul>
		<li>これはしょうがない</li>
	</ul>
	<li>一貫性を保つのがむずかしくなる</li>
	<ul>
		<li>各プログラムのインタフェースはどうするのだろうか？</li>
	</ul>
</ul>


<!--nextpage-->

<h2>型の導入</h2>
　
<ul>
	<li>ROSは、<span style="color:red">プロセス間通信に「型」を持ち込んでいる</span></li>
	<ul>
		<li>異なった原語でも型をつけてデータを渡せるようにすることで、整合性が保たれるようになっている。</li>
	</ul>
　
	<li>以上の仕掛けで、ロボットの世界ではROSの仕組みでつながり合えるオープンソースが出揃うことになった</li>
	<ul>
		<li>ロボットでなくてもセンサやアクチュエータの制御に便利なので本日紹介</li>
	</ul>
</ul>


<!--nextpage-->

<h2>導入例</h2>
　
<ul>
	<li><a href="http://opensource-robotics.tokyo.jp/?p=480" target="_blank">http://opensource-robotics.tokyo.jp/?p=480</a></li>
	<li><a href="http://www.honda.co.jp/news/2016/c160712.html" target="_blank">http://www.honda.co.jp/news/2016/c160712.html</a></li>
　
	<li><a href="http://at-home.cit-brains.net/?p=365" target="_blank">千葉工大RoboCup@homeチーム（CIT Brains @home）</a></li>
</ul>


