---
Keywords: Haskell,Raspberry
Copyright: (C) 2017 Ryuichi Ueda
---

# 例のロボットを今度はHaskellで動かした
今日は某氏が取り仕切る<a href="http://makezine.jp/event/mft2015/" target="_blank">Maker Faire Tokyo 2015</a>に遊びに行きました。大いに啓蒙されたので、帰宅後、俺も何かやろうということで、「Raspberry Pi Mouseはどの言語でも動かせるアピール」の一環としてHaskellでRaspberry Pi Mouseを動かしてみました。

Raspberry Pi Mouseというのは日経Linuxの連載「<a href="/?page=05983" target="_blank">Raspberry Piで始めるかんたんロボット製作</a>」で作っているロボットです。よく「パソコンのカーソル動かす方のマウス」と間違われるのですが、ここで言っている「マウス」というのはロボット競技のマイクロマウスの「マウス」です。


このロボットをHaskellで動かすわけですが、そのためにはセンサの読み込みとモータの動作を非同期で行う必要があります。私みたいな阿呆でも分かる解説を探していたところ、

<span class="hatena-bookmark-title"><a href="http://qiita.com/myuon_myon/items/d0334317f220dfe05092" target="_blank">Haskellでマルチスレッド処理 - Qiita</a></span> 

が大変分かりやすかったので参考にさせていただきました。


ちゃんとやるにはこの本↓も参考になるかもしれません。（amazonに飛びます。）

<a href="https://www.amazon.co.jp/gp/product/4873116899/ref=as_li_ss_il?ie=UTF8&camp=247&creative=7399&creativeASIN=4873116899&linkCode=as2&tag=ryuichiueda-22"><img border="0" src="https://ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=4873116899&Format=_SL110_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=ryuichiueda-22" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=ryuichiueda-22&l=as2&o=9&a=4873116899" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />


コードの前に動いたロボットの様子をお見せすると、

<iframe width="420" height="315" src="https://www.youtube.com/embed/d9R8HCGDCbE" frameborder="0" allowfullscreen></iframe>

というように、前進して壁を検知したら止まるという動作ができました。たいしたことはやってませんが、滑らかに動きつつセンサの値を読んでいるのがミソです。

このムービーで使ったコードはミニマムなサンプルにして、<a href="https://github.com/ryuichiueda/RPiM/blob/master/sample/haskell/run.2.hs" target="_blank">GitHubにアップしてあります</a>。これで
<ul>
	<li>シェルスクリプト（bash）</li>
	<li>C/C++</li>
	<li>Python</li>
	<li>Haskell</li>
</ul>
と、自分がよく使う4大言語で動きました。デバイスファイルに字を出し入れするだけで動くので当たり前ですが・・・。たぶん、もうやらなくても十分アピールになるかなあ・・・。

Raspberry PiでHaskellを使うときはsudo apt-get install ghcします。

<h2>コード</h2>

コードは以下のような感じです。もう一度書いておくと、<span class="hatena-bookmark-title"><a href="http://qiita.com/myuon_myon/items/d0334317f220dfe05092">Haskellでマルチスレッド処理 - Qiita</a></span> <span class="hatena-bookmark-users">のコード（サンプルコードその2）の影響を色濃く受けています。

大雑把な説明ですが、モータを動かすforward関数と、センサ値を読み出すreadSensorという関数がロボットに直接関与しています（デバイスファイルを読み書きしている）。こいつらは両方最後に自分を呼び出していて、readSensorだけ、センサ値が閾値を超えると、その旨をputMVarという関数でrefに反映して処理を終わっています。

forwardとreadSensorを動かしているのはmain関数のにあるforkIOで、これが非同期に上記2つの関数を実行します。watchSensor関数はmainで呼ばれ、refの値を監視してTrueだったらforwardの処理を止め、そうでなかったら再度自分自身を呼び出しています。refの型はMVar Boolで、これは非同期で動くスレッド間で安全に読み書きできるそうです。間違ってたらアレなので、その筋の方のブログや書籍を参考にどうぞ。

```hs
import Control.Concurrent
import Control.Monad
import System.Posix.Unistd

-- 単純に前進する関数
forward :: IO ()
forward = do
 -- 車輪を400Hzで0.1秒回す
 writeFile "/dev/rtmotor0" "400 400 100"
 -- 無限ループ（・・・という言い方は不適切か？）
 forward

-- 距離センサを読み出す
readSensor :: MVar Bool -> IO ()
readSensor ref = do
 -- センサを休める
 threadDelay 200000
 cs <- readFile "/dev/rtlightsensor0"
 -- 4つのセンサの値を合計
 let v = sum [ read w :: Int | w <- words cs ]
 -- センサが反応していなかったら再度計測
 if v > 1000 then putMVar ref True else readSensor ref

-- センサに何か反応したらモータのスレッドを止める
watchSensor :: MVar Bool -> ThreadId -> IO ()
watchSensor ref w = do
 tf <- takeMVar ref
 if tf then killThread w else watchSensor ref w

main = do
 ref <- newMVar False
 w <- forkIO $ forward
 _ <- forkIO $ readSensor ref

 watchSensor ref w
```

この部分だけ見ると、Haskellなのに手続き的なのですが、ここにもっと高度な処理を関数で書いていけるのならば、Haskellで書くメリットも出てくるかもしれません。個人的にはシミュレーションで書いたHaskellの関数が使るという確実なメリットが。


ということでHaskellでロボットが動いたので、後はどなたか関数型言語でロボットを動かす講義をやって欲しい・・・。<span style="color:red">私はやりません。</span>

<h2>参考: Raspberry Pi Mouseって何？</h2>

<a href="/?page=05983">こちらのページで。</a>


