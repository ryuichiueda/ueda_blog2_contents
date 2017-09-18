---
Keywords:Haskell,Raspberry
Copyright: (C) 2017 Ryuichi Ueda
---

# 例のロボットを今度はHaskellで動かした
今日は某氏が取り仕切る<a href="http://makezine.jp/event/mft2015/" target="_blank">Maker Faire Tokyo 2015</a>に遊びに行きました。大いに啓蒙されたので、帰宅後、俺も何かやろうということで、「Raspberry Pi Mouseはどの言語でも動かせるアピール」の一環としてHaskellでRaspberry Pi Mouseを動かしてみました。<br />
<br />
Raspberry Pi Mouseというのは日経Linuxの連載「<a href="https://blog.ueda.asia/?page_id=5983" target="_blank">Raspberry Piで始めるかんたんロボット製作</a>」で作っているロボットです。よく「パソコンのカーソル動かす方のマウス」と間違われるのですが、ここで言っている「マウス」というのはロボット競技のマイクロマウスの「マウス」です。<br />
<br />
<br />
このロボットをHaskellで動かすわけですが、そのためにはセンサの読み込みとモータの動作を非同期で行う必要があります。私みたいな阿呆でも分かる解説を探していたところ、<br />
<br />
<span class="hatena-bookmark-title"><a href="http://qiita.com/myuon_myon/items/d0334317f220dfe05092" target="_blank">Haskellでマルチスレッド処理 - Qiita</a></span> <br />
<br />
が大変分かりやすかったので参考にさせていただきました。<br />
<br />
<br />
ちゃんとやるにはこの本↓も参考になるかもしれません。（amazonに飛びます。）<br />
<br />
<a href="https://www.amazon.co.jp/gp/product/4873116899/ref=as_li_ss_il?ie=UTF8&camp=247&creative=7399&creativeASIN=4873116899&linkCode=as2&tag=ryuichiueda-22"><img border="0" src="https://ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=4873116899&Format=_SL110_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=ryuichiueda-22" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=4873116899" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /><br />
<br />
<br />
コードの前に動いたロボットの様子をお見せすると、<br />
<br />
<iframe width="420" height="315" src="https://www.youtube.com/embed/d9R8HCGDCbE" frameborder="0" allowfullscreen></iframe><br />
<br />
というように、前進して壁を検知したら止まるという動作ができました。たいしたことはやってませんが、滑らかに動きつつセンサの値を読んでいるのがミソです。<br />
<br />
このムービーで使ったコードはミニマムなサンプルにして、<a href="https://github.com/ryuichiueda/RPiM/blob/master/sample/haskell/run.2.hs" target="_blank">GitHubにアップしてあります</a>。これで<br />
<ul><br />
	<li>シェルスクリプト（bash）</li><br />
	<li>C/C++</li><br />
	<li>Python</li><br />
	<li>Haskell</li><br />
</ul><br />
と、自分がよく使う4大言語で動きました。デバイスファイルに字を出し入れするだけで動くので当たり前ですが・・・。たぶん、もうやらなくても十分アピールになるかなあ・・・。<br />
<br />
Raspberry PiでHaskellを使うときはsudo apt-get install ghcします。<br />
<br />
<h2>コード</h2><br />
<br />
コードは以下のような感じです。もう一度書いておくと、<span class="hatena-bookmark-title"><a href="http://qiita.com/myuon_myon/items/d0334317f220dfe05092">Haskellでマルチスレッド処理 - Qiita</a></span> <span class="hatena-bookmark-users">のコード（サンプルコードその2）の影響を色濃く受けています。<br />
<br />
大雑把な説明ですが、モータを動かすforward関数と、センサ値を読み出すreadSensorという関数がロボットに直接関与しています（デバイスファイルを読み書きしている）。こいつらは両方最後に自分を呼び出していて、readSensorだけ、センサ値が閾値を超えると、その旨をputMVarという関数でrefに反映して処理を終わっています。<br />
<br />
forwardとreadSensorを動かしているのはmain関数のにあるforkIOで、これが非同期に上記2つの関数を実行します。watchSensor関数はmainで呼ばれ、refの値を監視してTrueだったらforwardの処理を止め、そうでなかったら再度自分自身を呼び出しています。refの型はMVar Boolで、これは非同期で動くスレッド間で安全に読み書きできるそうです。間違ってたらアレなので、その筋の方のブログや書籍を参考にどうぞ。<br />
<br />
[hs]<br />
import Control.Concurrent<br />
import Control.Monad<br />
import System.Posix.Unistd<br />
<br />
-- 単純に前進する関数<br />
forward :: IO ()<br />
forward = do<br />
 -- 車輪を400Hzで0.1秒回す<br />
 writeFile &quot;/dev/rtmotor0&quot; &quot;400 400 100&quot;<br />
 -- 無限ループ（・・・という言い方は不適切か？）<br />
 forward<br />
<br />
-- 距離センサを読み出す<br />
readSensor :: MVar Bool -&gt; IO ()<br />
readSensor ref = do<br />
 -- センサを休める<br />
 threadDelay 200000<br />
 cs &lt;- readFile &quot;/dev/rtlightsensor0&quot;<br />
 -- 4つのセンサの値を合計<br />
 let v = sum [ read w :: Int | w &lt;- words cs ]<br />
 -- センサが反応していなかったら再度計測<br />
 if v &gt; 1000 then putMVar ref True else readSensor ref<br />
<br />
-- センサに何か反応したらモータのスレッドを止める<br />
watchSensor :: MVar Bool -&gt; ThreadId -&gt; IO ()<br />
watchSensor ref w = do<br />
 tf &lt;- takeMVar ref<br />
 if tf then killThread w else watchSensor ref w<br />
<br />
main = do<br />
 ref &lt;- newMVar False<br />
 w &lt;- forkIO $ forward<br />
 _ &lt;- forkIO $ readSensor ref<br />
<br />
 watchSensor ref w<br />
[/hs]<br />
<br />
この部分だけ見ると、Haskellなのに手続き的なのですが、ここにもっと高度な処理を関数で書いていけるのならば、Haskellで書くメリットも出てくるかもしれません。個人的にはシミュレーションで書いたHaskellの関数が使るという確実なメリットが。<br />
<br />
<br />
ということでHaskellでロボットが動いたので、後はどなたか関数型言語でロボットを動かす講義をやって欲しい・・・。<span style="color:red">私はやりません。</span><br />
<br />
<h2>参考: Raspberry Pi Mouseって何？</h2><br />
<br />
<a href="https://blog.ueda.asia/?page_id=5983">こちらのページで。</a><br />
<br />

