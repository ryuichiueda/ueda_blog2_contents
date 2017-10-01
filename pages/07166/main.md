---
Copyright: (C) Ryuichi Ueda
---


# Raspberry Piで作ろう お手軽ロボット教室 | 日経Linux
<h2>各号に関するリンク集</h2>

<ul>
	<li><a href="#readme">README（各号通じて）</a></li>
	<li><a href="#201601">2016年1月号</a></li>
	<li><a href="#201602">2016年2月号</a></li>
	<li><a href="#201603">2016年3月号</a></li>
	<li><a href="#201604">2016年4月号</a></li>
	<li><a href="#201605">2016年5月号</a></li>
	<li><a href="#201606">2016年6月号</a></li>
	<li><a href="#201607">2016年7月号</a></li>
	<li><a href="#201608">2016年8月号</a></li>
	<li><a href="#201609">2016年9月号</a></li>
</ul>


<h3 id="readme">README</h3>

ドライバをインストールして使う際は、

```bash
pi@raspberrypi ~ $ sudo raspi-config 
```

を実行して、「 8 Advanced Options Configure advanced settings」を選択し、
<ul>
	<li>Device Tree機能をOFF</li>
	<li>SPI機能をON</li>
</ul>
にしましょう。


<h3 id="201601">2016年1月号</h3>

[amazonjs asin="B017A61V4U" locale="JP" tmpl="Small" title="日経Linux(リナックス)2016年1月号"]

<ul>
 <li><a href="https://github.com/rt-net/RaspberryPiMouse/blob/master/supplement/201508/RPiMouse-schematic.pdf" target="_blank">配線図（PDF）</a></li>
 <li><a href="https://github.com/rt-net/RaspberryPiMouse/blob/master/src/drivers/rtmouse.c" target="_blank">デバイスドライバのコード</a></li>
	<li><a href="https://github.com/ryuichiueda/NikkeiRaspiMouse" target="_blank">誌面のコードの場所（筆者リポジトリ）</a></li>
<ul>
	<li>この下の201601にあります。</li>
</ul>
</ul>

<h4>サンプルプログラムの動作</h4>

ビデオの中のロボットには、上にカメラやセンサが乗っていますが、今回は不要です。

[video width="1280" height="720" mp4="MAH00063.mp4"][/video]



<h3 id="201602">2016年2月号</h3>

[amazonjs asin="B018R7G4XY" locale="JP" title="日経Linux(リナックス)2016年2月号"]

<h4>カメラ取り付けパーツ</h4>

<ul>
 <li><a href="http://www.amazon.co.jp/dp/B019804PXA" target="_blank">http://www.amazon.co.jp/dp/B019804PXA</a></li>
</ul>

<h4>完成したらこうなる</h4>

<iframe width="560" height="315" src="https://www.youtube.com/embed/YKaCVhc8O6Y" frameborder="0" allowfullscreen></iframe>


<h3 id="201603">2016年3月号</h3>

[amazonjs asin="B019T9FN7W" locale="JP" title="日経Linux 2016年 03 月号 雑誌"]

<h4>参考サイト</h4>

<ul>
 <li><a href="http://opencv.jp/opencv-2svn/c/objdetect_cascade_classification.html" target="_blank">カスケード型分類器 | opencv 2.2 documentation</a></li>
 <li><a href="http://opencv.jp/opencv-2svn/cpp/reading_and_writing_images_and_video.html">画像とビデオの読み込みと書き込み | opencv 2.2 documentation</a></li>
 <li><a href="http://www.vision.cs.chubu.ac.jp/cvtutorial/pdf/03objectdetection.pdf" target="_blank">中部大学の藤吉先生のスライド（局所特徴量と統計学習手法による物体検出）</a></li>
 <li><a href="https://www.raspberrypi.org/documentation/hardware/camera.md" target="_blank">カメラの公式情報</a></li>
 <li><a href="http://qiita.com/wwacky/items/98d8be2844fa1b778323" target="_blank">python+OpenCVで顔認識をやってみる</a></li>
 <li><a href="http://blog.livedoor.jp/tmako123-programming/archives/41536599.html" target="_blank">Raspberry Pi の PiCamera でリアルタイム画像処理</a></li>
</ul>

<h4>完成したらこうなる</h4>

<iframe width="560" height="315" src="https://www.youtube.com/embed/FgsJU4ApuY0" frameborder="0" allowfullscreen></iframe>



<h3 id="201604">2016年4月号</h3>



<h4>粗い制御</h4>

<iframe width="420" height="315" src="https://www.youtube.com/embed/L6Jd12ugboU" frameborder="0" allowfullscreen></iframe>

<h4>P制御</h4>

<iframe width="560" height="315" src="https://www.youtube.com/embed/gyD8Edgm1Eo" frameborder="0" allowfullscreen></iframe>

<h4>スリップしなかったパターン</h4>

速度を落とせばスリップは減ります。

<iframe width="420" height="315" src="https://www.youtube.com/embed/nWZPXAE-MmI" frameborder="0" allowfullscreen></iframe>

<h4>スリップからのリカバリー</h4>

<iframe width="420" height="315" src="https://www.youtube.com/embed/iyLtPzWcPpU" frameborder="0" allowfullscreen></iframe>

<h4>参考: P制御なし</h4>

ぶつかります。（注意: P制御ありでも最初に置いた向きが悪いとぶつかります。）

<iframe width="420" height="315" src="https://www.youtube.com/embed/wNm9dhWBqZM" frameborder="0" allowfullscreen></iframe>


<h3 id="201605">2016年5月号</h3>

<h4>各エージェントクラスの挙動</h4>

<ul>
 <li>AgentStopInFrontOfWall</li>
</ul>

<iframe width="420" height="315" src="https://www.youtube.com/embed/0U0IHIdhtoQ" frameborder="0" allowfullscreen></iframe>

<ul>
 <li>AgentGoAlongWall</li>
</ul>


<iframe width="420" height="315" src="https://www.youtube.com/embed/nNwKVeCqjus" frameborder="0" allowfullscreen></iframe>

<ul>
 <li>AgentAvoidWall</li>
</ul>

<iframe width="420" height="315" src="https://www.youtube.com/embed/DxztfZB8VQM" frameborder="0" allowfullscreen></iframe>



<h3 id="201606">2016年6月号</h3>

<h4>参考にしたサイト</h4>

<ul>
 <li>USBマイクの設定（alsa-base.confの設定はこちらの記述が確実なようです）</li>
 <ul>
	<li><span class="hatena-bookmark-title"><a href="//qiita.com/kinpira/items/75513eaab6eed19da9a3">RaspberryPiとdocomoAPIで簡易OHaN○Sを作って会話してみる - Qiita</a></span> <span class="hatena-bookmark-users"><a href="//b.hatena.ne.jp/entry/qiita.com/kinpira/items/75513eaab6eed19da9a3"><img title="RaspberryPiとdocomoAPIで簡易OHaN○Sを作って会話してみる - Qiita" alt="RaspberryPiとdocomoAPIで簡易OHaN○Sを作って会話してみる - Qiita" src="//b.hatena.ne.jp/entry/image/http://qiita.com/kinpira/items/75513eaab6eed19da9a3"></a></span></li>
 </ul>
 <li>USBマイクの設定からJuliusを使うまで</li>
 <ul>
	<li><span class="hatena-bookmark-title"><a href="http://hyottokoaloha.hatenablog.com/entry/2015/06/30/105906">Raspberry PiでJuliusを使った音声認識(1) - DesignAssembler</a></span> <span class="hatena-bookmark-users"><a href="http://b.hatena.ne.jp/entry/hyottokoaloha.hatenablog.com/entry/2015/06/30/105906"><img title="Raspberry PiでJuliusを使った音声認識(1) - DesignAssembler" alt="Raspberry PiでJuliusを使った音声認識(1) - DesignAssembler" src="//b.hatena.ne.jp/entry/image/http://hyottokoaloha.hatenablog.com/entry/2015/06/30/105906"></a></span></li>
	<li><span class="hatena-bookmark-title"><a href="http://qiita.com/t_oginogin/items/f0ba9d2eb622c05558f4">Julius - Raspberry Piで音声認識 - Qiita</a></span> <span class="hatena-bookmark-users"><a href="http://b.hatena.ne.jp/entry/qiita.com/t_oginogin/items/f0ba9d2eb622c05558f4"><img title="Julius - Raspberry Piで音声認識 - Qiita" alt="Julius - Raspberry Piで音声認識 - Qiita" src="http://b.hatena.ne.jp/entry/image/http://qiita.com/t_oginogin/items/f0ba9d2eb622c05558f4"></a></span></li>

 </ul>


</ul>

<h4>動作例</h4>

辞書の変更なしなので、ちと鈍い。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gx6TW4KO2YI" frameborder="0" allowfullscreen></iframe>



<h3 id="201607">2016年7月号</h3>

ブログに書くことは特にありません。


<h3 id="201608">2016年8月号</h3>

こちらもビデオの準備がなく・・・


<h3 id="201609">2016年9月号</h3>

[amazonjs asin="B01HIP2NX6" locale="JP" title="日経Linux(リナックス)2016年9月号"]

左手法っぽい方法でロボットを迷路で走らせています。改善の余地あり。

<iframe width="560" height="315" src="https://www.youtube.com/embed/yxiJ008K_0s" frameborder="0" allowfullscreen></iframe>

同じコードで廊下を走らせたもの。

<iframe width="420" height="315" src="https://www.youtube.com/embed/dfEJXWPUHRI" frameborder="0" allowfullscreen></iframe>

<h4>コード</h4>

<ul>
	<li>左手法のコード<a href="https://github.com/ryuichiueda/raspimouse_lefthand/tree/ForNikkeiLinux201609" target="_blank">https://github.com/ryuichiueda/raspimouse_lefthand/tree/ForNikkeiLinux201609</a></li>
	<li>ROSのベースシステム: <a href="https://github.com/ryuichiueda/raspimouse_ros" target="_blank">https://github.com/ryuichiueda/raspimouse_ros</a></li>

</ul>





