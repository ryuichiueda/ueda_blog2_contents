---
Keywords: コマンド,awk,sed,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2017 Ryuichi Ueda
---

# 【問題と解答】第28回基準値を超えるシェル芸勉強会
<a href="/?post=09602">問題のみのページはこちら</a>

<h2>問題で使うファイル等</h2>
GitHubにあります。ファイルは

<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28</a>

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

<a href="https://github.com/ryuichiueda/commentary_on_graph-based_slam/blob/master/contents.tex" target="_blank">contents.tex</a>について、「\\begin{figure}と\\end{figure}」で囲まれた部分を全て抽出してください。


<h3>Q1.2</h3>

次のようなリストを作ってください。

```bash
世界座標系とロボットの姿勢 ./figs/coordinate.eps
計測値 ./figs/observation.eps
ランドマークの計測値から2点の相対姿勢を求める ./figs/two_poses.eps
ランドマークの計測値の不確かさを表す共分散行列 ./figs/observation_noise.eps
```

<h3>解答</h3>

Q1.1については、次のようにsedの範囲指定を使います。
```bash
$ cat contents.tex | sed -n '/\\\\begin{figure}/,/\\\\end{figure}/p'
\\begin{figure}[htbp]
	\\begin{center}
		\\includegraphics[width=0.5\\linewidth]{./figs/coordinate.eps}
		\\caption{世界座標系とロボットの姿勢}
		\\label{fig:coordinate}
	\\end{center}
\\end{figure}
（中略。略していないものも含めて全部で4つ）
\\begin{figure}[htbp]
	\\begin{center}
		\\includegraphics[width=0.8\\linewidth]{./figs/observation_noise.eps}
		\\caption{ランドマークの計測値の不確かさを表す共分散行列}
		\\label{fig:observation_noise}
	\\end{center}
\\end{figure}
```

Q1.2については、不要なデータを削って最後に並び替えます。

```bash
$ cat contents.tex | sed -n '/\\\\begin{figure}/,/\\\\end{figure}/p' |
 grep -e include -e caption | sed 's/.*{//' |
 xargs -n 2 | tr -d '}' | awk '{print $2,$1}'
世界座標系とロボットの姿勢 ./figs/coordinate.eps
計測値 ./figs/observation.eps
ランドマークの計測値から2点の相対姿勢を求める ./figs/two_poses.eps
ランドマークの計測値の不確かさを表す共分散行列 ./figs/observation_noise.eps
```


<h2>Q2</h2>

\\sectionから始まる部分を章としたとき、第2章の第1文を抽出してみましょう。ただし、各行の%以降はコメントアウトされた文なので無視してください。

<h3>解答</h3>

最初に段落番号をつけると簡単になります。

```bash
$ awk '/\\\\section/{a+=1}{print a,$0}' contents.tex | grep ^2 |
 grep -v '\\\\section' | grep -v '%.*' | sed 's/^..//' |
 sed -n '1,/。/p' | sed 's/。.*/。/'

平面上を移動し、向きを持ち、カメラでランドマーク観測ができるロボットで
graph-based SLAMを実行する方法を考える。
```



<h2>Q3</h2>

脚注（\\footnote{...}）の部分を全て抽出してください。一つだけ、脚注の中にも{}で囲まれた部分があるので注意してください。

<h3>解答</h3>

まずは脚注の終わりが必ず「。」で終わっているのを利用したズル解答から。grep -Pの最短一致を使います。

```bash
$ tr -d '\\n' < contents.tex | grep -oP '(\\\\footnote{.+?。})'
\\footnote{この仮定は実用上強すぎるが、実際には、後の計算式から分かるように、2つの姿勢間での値$\\psi_{c,t}, \\psi_{c,t'}$の差だけが分かれば良い。例えば、2点間で得られた画像の向きを画像処理から割り出すなどの処理で、この差は得られる。}
\\footnote{$「10$[\\%]」は変数にすべきだが、記号が増えて理解の妨げになるので固定値として説明する。}
\\footnote{おそらく$\\psi$は$\\theta$で置き換えられるので$\\psi$を使わない実装もできるが、まだ自分自身では検証していない。}
\\footnote{小さい角度なので、$\\sin(3\\pi/180)$は$3\\pi/180$に近似しても良い。}
\\footnote{固定しないと世界座標系が決まらない。}
```

そうでない解は、インデントをつけてから抽出する方法しか、今のところ思いついていません。

```bash
$ tr -d '\\n' < contents.tex | sed 's/[{}]/\\n&\\n/g' | sed 's/\\\\footnote/\\n&/' |
 awk '{for(a=0;a<i;a++)printf " "}/{/{i+=1}/}/{i-=1}{print}' |
 sed -n '/\\\\footnote/,/^ }/p' | tr -d '\\n' | sed 's/\\\\footnote/\\n&/g' |
 sed 's/ *} */}/g' | sed 's/ *{ */{/g' | awk '{print}'
```


<h2>Q4</h2>

各章（\\sectionから次の\\sectionまでの部分）を、ファイル名にタイトルをつけて個別のファイルに分けてください。ファイル名のスペースはアンダースコアに変えても構いません。

<h3>解答</h3>

```bash
$ cat contents.tex |
 awk '/\\\\section/{f=gensub(/ /,"_","g",$0);gsub(/\\\\section{/,"",f);
gsub(/}$/,"",f)}{print $0 > f}'
###このようにファイルができます###
$ ls
contents.tex graph-based_SLAMの実装例 はじめに 問題
```


<h2>Q5</h2>

このテキストには「○○座標系」という用語がいくつか出てきます。○○にはカタカナか漢字の単語が入ります。これらの「○○座標系」を全通り抽出してください。

<h3>解答</h3>

```bash
$ grep 座標系 contents.tex | mecab -O wakati |
 grep -oE '[^ あ-ん]+ 座標 系' | sort -u | tr -d " "
ロボット座標系
計測座標系
世界座標系
$ grep 座標系 contents.tex | grep -oE '[^ あ-ん{、「]+座標系' | sort -u
ロボット座標系
計測座標系
世界座標系
```

<h2>Q6</h2>

各段落の頭に全角スペースを入れてください。

<h3>解答</h3>

空行を見つけてフラグを立て、普通の文頭かどうか判断して全角スペースを差し込みます。

```bash
$ cat contents.tex |
 awk '/^ *$/{f=1}
{if(f && !/^ *$|section|begin|end|^%/){print "　"$0;f=0}else{print}}'
```


<h2>Q7</h2>

本文の余計な改行を取ってください。（段落内の余計な改行を取るということです。）

<h3>解答</h3>

q6の出力から続ける例を示します。ゴリ押しです。

```bash
$ cat q6 | sed 's/^%.*//' |
 awk '/begin/{if(!stop)print "";stop+=1}
 !stop && !/section/{printf($0)}
 stop || /section/{print}/end/{stop-=1}' |
 sed 's/　 /n　 /' | sed 's/\\\\[sub]*section/\\n\\n&/' 
```

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


<h3>解答</h3>

awkで章節項のカウンタを作ってうまく制御するのが一番素直な方法です。（二番目以降は思いつきませんが。）


```bash
$ grep section contents.tex | sed 's/{/ /' | grep -v ^% |
 sed 's/\\\\label.*//' | sed 's/}$//' |
 awk '/^\\\\se/{s+=1;$1=s;ss=0;print}/\\\\subse/{ss+=1;$1=s"."ss;sss=0;print}/
\\\\subsub/{sss+=1;$1=s"."ss"."sss;print}'
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
