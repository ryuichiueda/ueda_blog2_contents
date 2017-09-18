---
Keywords: マイコン,123D,ディジタル回路,寝る
Copyright: (C) 2017 Ryuichi Ueda
---

# 論理ゲートをシミュレータで地味に作る
本日は訳あって<a href="https://123d.circuits.io/">123D CIRCUITS</a>でちまちまと論理ゲートを作っていました。論理ゲートというのは2進数を電圧の高低で入力すると、同じく電圧の高低で2進数を出力する回路で、コンピュータとかはこれでできています。ネット上で動くサンプルというものも少ないので、NOTとNAND、NANDでできたANDとORの例を置いておきます。<br />
<br />
<h2>NOTゲート</h2><br />
<br />
まず最初に作ったのは、下の<a href="https://ja.wikipedia.org/wiki/NOT%E3%82%B2%E3%83%BC%E3%83%88">NOTゲート</a>と呼ばれるものです。NOTゲートはブレッドボードの上の回路で、左に電源と入力信号用の電池とスライドスイッチ、右に出力確認用のLEDがおまけで付いています。NOTゲートは信号の入出力をひっくり返すものです。信号の入力（黄色の線）が1（正の電圧）の時は出力（緑の線）が0（電圧がゼロ）、入力が0（電圧がゼロ）の時は出力が1（正の電圧）になります。<br />
<br />
<span style="color:red">左上の再生ボタンを押すと動きます。重たいけど。</span><br />
<br />
<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1713317-not-gate/embed#breadboard' width='650'></iframe><br />
<br />
この回路のPMOSとNMOSというのは<a href="https://ja.wikipedia.org/wiki/%E9%9B%BB%E7%95%8C%E5%8A%B9%E6%9E%9C%E3%83%88%E3%83%A9%E3%83%B3%E3%82%B8%E3%82%B9%E3%82%BF">電解効果トランジスタ</a>の一種の<a href="https://ja.wikipedia.org/wiki/MOSFET">MOSFET</a>（のシミュレートされたもの）で、要はスイッチです。手でスイッチを入れる代わりに3本足の真ん中（ゲート）に電圧をかけたりかけなかったりして操作します。真ん中の足に電圧がかかると両側の足に電流が流れる方がNMOS、電圧がかからないと電流が流れる方がPMOSです。本当は両側の足には違いがあるのですが、ここではあまり本質的な話ではありません。<br />
<br />
両方のトランジスタのゲートには、黄色の線を伝ってスイッチのつまみが上にあるときには3V、下にあるときには0Vの電圧がかかります。で、3Vの時は上のPMOSが絶縁、下のNMOSが通電して緑の線の電位が黒い線と同じになり、つまみが下にあるときは逆に上の赤い線と電位が同じになります。ということで、黄色と緑の線は逆の出力になることになります。<br />
<br />
<h2>NANDゲート</h2><br />
<br />
次に挙げるのはNANDゲートです。NANDゲートというのは二つの入力を受け入れ、その両方が0なら出力が1、それ以外なら出力が0になるという、直感的にはさっぱり分からんものですが、後で示すようにNANDゲートだけを組み合わせて他のゲートを作ることができるので、コンピュータの中でよく使われています。<br />
<br />
作ったのは次のような回路で、黄色とオレンジの線からそれぞれ電圧を入力すると、緑の線から出力が出てきます。スライドスイッチを操作すると、NANDになっていることが分かるはずです。<br />
<br />
<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1717541-nand-gate/embed#breadboard' width='650'></iframe><br />
<br />
回路を簡単に説明すると、上の二つのPMOSは並列に赤い線にぶら下がり、下の二つのNMOSは直列に黒い線にぶら下がっています。黄色、オレンジ色の線の両方の電圧が高いときだけ、下のNMOS直列つなぎが通電して、緑の線と黒い線の電位が同じになります。<br />
<br />
<br />
<h2>ANDゲート</h2><br />
<br />
ANDはNANDの出力をNOTゲートで反転すれば作れます。ただ、NANDゲートの黄色とオレンジの線を短絡してもNOTゲートになるので、下のようにNANDを二つ使っても作れます。NOTと組み合わせる場合よりトランジスタが2個多くなってしまいますが、同じもので作った方が単純で良いこともあるそうです。<br />
<br />
<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1718007-and-gate-composed-of-two-nand-gates/embed#breadboard' width='650'></iframe><br />
<br />
<h2>ORゲート</h2><br />
<br />
ORはNANDゲート3個で下の例のように作れます。入力側の2つのNANDは黄色の線とオレンジの線が短絡されてNOTになっています。NANDの「入力が両方1の時だけ出力が0」というのの二つの入力をひっくり返して、「入力が両方0の時だけ出力が0」にしてORを実現しているわけです。<br />
<br />
<iframe frameborder='0' height='448' marginheight='0' marginwidth='0' scrolling='no' src='https://123d.circuits.io/circuits/1718046-or-gate-composed-of-three-nand-gates/embed#breadboard' width='650'></iframe><br />
<br />
<h2>終わりに</h2><br />
<br />
NAND回路を丸ごとコピーしたら、絵面はそのままで基盤にトランジスタが刺さってない状態になってしまい、デバッグに1時間かかりました・・・。ソフトウェアのデバッグの何億倍も効率が悪いです・・・。<br />
<br />
<br />
<span style="color:red">それから、たかだか数ビットの計算をネットやらグラフィックやらシミュレータやら使ってやってるのって、どう考えても贅沢すぎじゃないのか？？</span><br />
<br />
<br />
寝る。
