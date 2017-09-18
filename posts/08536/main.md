---
Copyright: (C) Ryuichi Ueda
---

# JTF2016手順メモ
<h1 style="font-size:180%">ROS（robot operating system）を触ってみよう</h1><br />
　<br />
<br />
<p>千葉工業大学 上田隆一</p><br />
<br />
<!--nextpage--><br />
<br />
<h2>本日の内容</h2><br />
<br />
<p>あり合わせ or 他人の資料ですみません orz</p><br />
　<br />
<ul><br />
	<li>ROSとは（このスライド）</li><br />
	<li>あとは他のドキュメントに基づいて進めるところまで</li><br />
	<ul><br />
		<li><a href="http://www.slideshare.net/ryuichiueda/201512-56193642" target="_blank">インストールと動作確認</a></li><br />
		<li><a href="http://wiki.ros.org/ja/ROS/Tutorials/WritingPublisherSubscriber%28python%29" target="_blank">パブリッシャとサブスクライバ</a></li><br />
		<li><a href="http://wiki.ros.org/ja/ROS/Tutorials/CreatingMsgAndSrv" target="_blank">メッセージ・サービスを作る</a></li><br />
	</ul><br />
</ul><br />
　<br />
<br />
<!--nextpage--><br />
<br />
<h2>ROSとは</h2><br />
　<br />
<ul><br />
	<li>2007年からWillow Garage社にて公式に<br />
開発が始まったロボット用ミドルウェア</li><br />
	<li>主にUbuntu上で動く</li><br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>ROSの主たる機能</h2><br />
　<br />
<ul><br />
	<li>機能はいくつかあるが、主な機能はプロセス間通信</li><br />
　<br />
	<ul><br />
		<li>ロボットのプログラムを一つのプロセスに押し込まないで、複数のプロセスに分けて処理させる</li><br />
		<ul><br />
　<br />
			<li>例: モータに指令を出すプログラム、センサの値を読むプログラム、センサからモータの出力を決めるプログラム・・・</li><br />
		</ul><br />
	</ul><br />
<br />
</ul><br />
<br />
<!--nextpage--><br />
<br />
<h2>プロセスを分ける<br />
メリット・デメリット</h2><br />
<br />
<ul><br />
	<li>各プログラムで違う言語が使える</li><br />
	<ul><br />
		<li>例: モータの制御はC++で高速化、行動の場合分けはPythonで楽する</li><br />
		<li>別の言語で書かれたプログラムを連結しやすい</li><br />
		<li>コンポーネント化しやすい</li><br />
	</ul><br />
　<br />
	<li>プロセス間のリアルタイム性は保証されない</li><br />
	<ul><br />
		<li>これはしょうがない</li><br />
	</ul><br />
	<li>一貫性を保つのがむずかしくなる</li><br />
	<ul><br />
		<li>各プログラムのインタフェースはどうするのだろうか？</li><br />
	</ul><br />
</ul><br />
<br />
<br />
<!--nextpage--><br />
<br />
<h2>型の導入</h2><br />
　<br />
<ul><br />
	<li>ROSは、<span style="color:red">プロセス間通信に「型」を持ち込んでいる</span></li><br />
	<ul><br />
		<li>異なった原語でも型をつけてデータを渡せるようにすることで、整合性が保たれるようになっている。</li><br />
	</ul><br />
　<br />
	<li>以上の仕掛けで、ロボットの世界ではROSの仕組みでつながり合えるオープンソースが出揃うことになった</li><br />
	<ul><br />
		<li>ロボットでなくてもセンサやアクチュエータの制御に便利なので本日紹介</li><br />
	</ul><br />
</ul><br />
<br />
<br />
<!--nextpage--><br />
<br />
<h2>導入例</h2><br />
　<br />
<ul><br />
	<li><a href="http://opensource-robotics.tokyo.jp/?p=480" target="_blank">http://opensource-robotics.tokyo.jp/?p=480</a></li><br />
	<li><a href="http://www.honda.co.jp/news/2016/c160712.html" target="_blank">http://www.honda.co.jp/news/2016/c160712.html</a></li><br />
　<br />
	<li><a href="http://at-home.cit-brains.net/?p=365" target="_blank">千葉工大RoboCup\@homeチーム（CIT Brains \@home）</a></li><br />
</ul><br />
<br />

