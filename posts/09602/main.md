---
Keywords: コマンド,awk,CLI,sed,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題のみ】第28回基準値を超えるシェル芸勉強会
<a href="/?post=09575">解答例はこちら</a>
<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28" target="_blank" rel="noopener noreferrer">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28</a>

にあります。

クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

<h2>環境</h2>
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。BSD系の人は玄人なので各自対応のこと。
<h2>注意</h2>
今回はいつにも増して一般解を出そうとすると死にますので、欲しい出力が得られればそれで良いということを心がけましょう。
<h2>イントロ</h2>

<ul>
	<li><a href="/?presenpress=%e7%ac%ac28%e5%9b%9e%e5%9f%ba%e6%ba%96%e5%80%a4%e3%82%92%e8%b6%85%e3%81%88%e3%82%8b%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">こちら</a></li>
</ul>



<h2>Q1</h2>
<h3>Q1.1</h3>
<a href="https://github.com/ryuichiueda/commentary_on_graph-based_slam/blob/master/contents.tex" target="_blank" rel="noopener noreferrer">contents.txt</a>について、「\\begin{figure}と\\end{figure}」で囲まれた部分を全て抽出してください。
<h3>Q1.2</h3>
次のようなリストを作ってください。

```bash
世界座標系とロボットの姿勢 ./figs/coordinate.eps
計測値 ./figs/observation.eps
ランドマークの計測値から2点の相対姿勢を求める ./figs/two_poses.eps
ランドマークの計測値の不確かさを表す共分散行列 ./figs/observation_noise.eps
```

<h2>Q2</h2>
\\sectionから始まる部分を章としたとき、第2章の第1文を抽出してみましょう。ただし、各行の%以降はコメントアウトされた文なので無視してください。
<h2>Q3</h2>
脚注（\\footnote{...}）の部分を全て抽出してください。一つだけ、脚注の中にも{}で囲まれた部分があるので注意してください。
<h2>Q4</h2>
各章（\\sectionから次の\\sectionまでの部分）を、ファイル名にタイトルをつけて個別のファイルに分けてください。ファイル名のスペースはアンダースコアに変えても構いません。
<h2>Q5</h2>
このテキストには「○○座標系」という用語がいくつか出てきます。○○にはカタカナか漢字の単語が入ります。これらの「○○座標系」を全通り抽出してください。
<h2>Q6</h2>
各段落の頭に全角スペースを入れてください。
<h2>Q7</h2>
本文のところだけ改行を取ってください。
<h2>Q8</h2>
contents.texについて、次のように章節項のリストを作ってください。

```bash
1 はじめに
2 問題
2.1 ロボットの姿勢と座標系
2.2 観測
2.2.1 ランドマークの識別
2.2.2 ランドマークの姿勢計測
2.2.3 計測値の記録
2.2.4 計測値の誤差
2.3 完全SLAM問題
3 graph-based SLAMの実装例
3.1 グラフのエッジを作る
3.1.1 $\\V{\\mu}_{c,t,t'}, \\V{e}_{c,t,t'}$の計算
3.1.2 $\\Sigma_{c,t,t'}, \\Omega_{c,t,t'}$の計算
3.2 最適化問題を作る
3.2.1 マハラノビス距離
3.2.2 最適化する式
3.3 $\\V{e}_{c,t,t'}$の勾配を求める
3.4 問題を解く
```

