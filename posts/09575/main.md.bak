# 【問題と解答】第28回基準値を超えるシェル芸勉強会
<a href="https://blog.ueda.asia/?p=9602">問題のみのページはこちら</a><br />
<br />
<h2>問題で使うファイル等</h2><br />
GitHubにあります。ファイルは<br />
<br />
<a href="https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28" target="_blank">https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.28</a><br />
<br />
にあります。<br />
<br />
クローンは以下のようにお願いします。<br />
<br />
[bash]<br />
$ git clone https://github.com/ryuichiueda/ShellGeiData.git<br />
[/bash]<br />
<br />
<br />
<h2>環境</h2><br />
解答例はUbuntu Linux 16.04 で作成。Macの場合はcoreutilsをインストールの上、gsedをつかいましょう。BSD系の人は玄人なので各自対応のこと。<br />
<br />
<h2>注意</h2><br />
<br />
今回はいつにも増して一般解を出そうとすると死にますので、欲しい出力が得られればそれで良いということを心がけましょう。<br />
<br />
<h2>イントロ</h2><br />
<br />
<ul><br />
	<li><a href="https://blog.ueda.asia/?presenpress=%e7%ac%ac28%e5%9b%9e%e5%9f%ba%e6%ba%96%e5%80%a4%e3%82%92%e8%b6%85%e3%81%88%e3%82%8b%e3%82%b7%e3%82%a7%e3%83%ab%e8%8a%b8%e5%8b%89%e5%bc%b7%e4%bc%9a">こちら</a></li><br />
</ul><br />
<br />
<br />
<br />
<h2>Q1</h2><br />
<br />
<h3>Q1.1</h3><br />
<br />
<a href="https://github.com/ryuichiueda/commentary_on_graph-based_slam/blob/master/contents.tex" target="_blank">contents.txt</a>について、「\\begin{figure}と\\end{figure}」で囲まれた部分を全て抽出してください。<br />
<br />
<br />
<h3>Q1.2</h3><br />
<br />
次のようなリストを作ってください。<br />
<br />
[bash]<br />
世界座標系とロボットの姿勢 ./figs/coordinate.eps<br />
計測値 ./figs/observation.eps<br />
ランドマークの計測値から2点の相対姿勢を求める ./figs/two_poses.eps<br />
ランドマークの計測値の不確かさを表す共分散行列 ./figs/observation_noise.eps<br />
[/bash]<br />
<br />
<h3>解答</h3><br />
<br />
Q1.1については、次のようにsedの範囲指定を使います。<br />
[bash]<br />
$ cat contents.tex | sed -n '/\\\\begin{figure}/,/\\\\end{figure}/p'<br />
\\begin{figure}[htbp]<br />
	\\begin{center}<br />
		\\includegraphics[width=0.5\\linewidth]{./figs/coordinate.eps}<br />
		\\caption{世界座標系とロボットの姿勢}<br />
		\\label{fig:coordinate}<br />
	\\end{center}<br />
\\end{figure}<br />
（中略。略していないものも含めて全部で4つ）<br />
\\begin{figure}[htbp]<br />
	\\begin{center}<br />
		\\includegraphics[width=0.8\\linewidth]{./figs/observation_noise.eps}<br />
		\\caption{ランドマークの計測値の不確かさを表す共分散行列}<br />
		\\label{fig:observation_noise}<br />
	\\end{center}<br />
\\end{figure}<br />
[/bash]<br />
<br />
Q1.2については、不要なデータを削って最後に並び替えます。<br />
<br />
[bash]<br />
$ cat contents.tex | sed -n '/\\\\begin{figure}/,/\\\\end{figure}/p' |<br />
 grep -e include -e caption | sed 's/.*{//' |<br />
 xargs -n 2 | tr -d '}' | awk '{print $2,$1}'<br />
世界座標系とロボットの姿勢 ./figs/coordinate.eps<br />
計測値 ./figs/observation.eps<br />
ランドマークの計測値から2点の相対姿勢を求める ./figs/two_poses.eps<br />
ランドマークの計測値の不確かさを表す共分散行列 ./figs/observation_noise.eps<br />
[/bash]<br />
<br />
<br />
<h2>Q2</h2><br />
<br />
\\sectionから始まる部分を章としたとき、第2章の第1文を抽出してみましょう。ただし、各行の%以降はコメントアウトされた文なので無視してください。<br />
<br />
<h3>解答</h3><br />
<br />
最初に段落番号をつけると簡単になります。<br />
<br />
[bash]<br />
$ awk '/\\\\section/{a+=1}{print a,$0}' contents.tex | grep ^2 |<br />
 grep -v '\\\\section' | grep -v '%.*' | sed 's/^..//' |<br />
 sed -n '1,/。/p' | sed 's/。.*/。/'<br />
<br />
平面上を移動し、向きを持ち、カメラでランドマーク観測ができるロボットで<br />
graph-based SLAMを実行する方法を考える。<br />
[/bash]<br />
<br />
<br />
<br />
<h2>Q3</h2><br />
<br />
脚注（\\footnote{...}）の部分を全て抽出してください。一つだけ、脚注の中にも{}で囲まれた部分があるので注意してください。<br />
<br />
<h3>解答</h3><br />
<br />
まずは脚注の終わりが必ず「。」で終わっているのを利用したズル解答から。grep -Pの最短一致を使います。<br />
<br />
[bash]<br />
$ tr -d '\\n' &lt; contents.tex | grep -oP '(\\\\footnote{.+?。})'<br />
\\footnote{この仮定は実用上強すぎるが、実際には、後の計算式から分かるように、2つの姿勢間での値$\\psi_{c,t}, \\psi_{c,t'}$の差だけが分かれば良い。例えば、2点間で得られた画像の向きを画像処理から割り出すなどの処理で、この差は得られる。}<br />
\\footnote{$「10$[\\%]」は変数にすべきだが、記号が増えて理解の妨げになるので固定値として説明する。}<br />
\\footnote{おそらく$\\psi$は$\\theta$で置き換えられるので$\\psi$を使わない実装もできるが、まだ自分自身では検証していない。}<br />
\\footnote{小さい角度なので、$\\sin(3\\pi/180)$は$3\\pi/180$に近似しても良い。}<br />
\\footnote{固定しないと世界座標系が決まらない。}<br />
[/bash]<br />
<br />
そうでない解は、インデントをつけてから抽出する方法しか、今のところ思いついていません。<br />
<br />
[bash]<br />
$ tr -d '\\n' &lt; contents.tex | sed 's/[{}]/\\n&amp;\\n/g' | sed 's/\\\\footnote/\\n&amp;/' |<br />
 awk '{for(a=0;a&lt;i;a++)printf &quot; &quot;}/{/{i+=1}/}/{i-=1}{print}' |<br />
 sed -n '/\\\\footnote/,/^ }/p' | tr -d '\\n' | sed 's/\\\\footnote/\\n&amp;/g' |<br />
 sed 's/ *} */}/g' | sed 's/ *{ */{/g' | awk '{print}'<br />
[/bash]<br />
<br />
<br />
<h2>Q4</h2><br />
<br />
各章（\\sectionから次の\\sectionまでの部分）を、ファイル名にタイトルをつけて個別のファイルに分けてください。ファイル名のスペースはアンダースコアに変えても構いません。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ cat contents.tex |<br />
 awk '/\\\\section/{f=gensub(/ /,&quot;_&quot;,&quot;g&quot;,$0);gsub(/\\\\section{/,&quot;&quot;,f);<br />
gsub(/}$/,&quot;&quot;,f)}{print $0 &gt; f}'<br />
###このようにファイルができます###<br />
$ ls<br />
contents.tex graph-based_SLAMの実装例 はじめに 問題<br />
[/bash]<br />
<br />
<br />
<h2>Q5</h2><br />
<br />
このテキストには「○○座標系」という用語がいくつか出てきます。○○にはカタカナか漢字の単語が入ります。これらの「○○座標系」を全通り抽出してください。<br />
<br />
<h3>解答</h3><br />
<br />
[bash]<br />
$ grep 座標系 contents.tex | mecab -O wakati |<br />
 grep -oE '[^ あ-ん]+ 座標 系' | sort -u | tr -d &quot; &quot;<br />
ロボット座標系<br />
計測座標系<br />
世界座標系<br />
$ grep 座標系 contents.tex | grep -oE '[^ あ-ん{、「]+座標系' | sort -u<br />
ロボット座標系<br />
計測座標系<br />
世界座標系<br />
[/bash]<br />
<br />
<h2>Q6</h2><br />
<br />
各段落の頭に全角スペースを入れてください。<br />
<br />
<h3>解答</h3><br />
<br />
空行を見つけてフラグを立て、普通の文頭かどうか判断して全角スペースを差し込みます。<br />
<br />
[bash]<br />
$ cat contents.tex |<br />
 awk '/^ *$/{f=1}<br />
{if(f &amp;&amp; !/^ *$|section|begin|end|^%/){print &quot;　&quot;$0;f=0}else{print}}'<br />
[/bash]<br />
<br />
<br />
<h2>Q7</h2><br />
<br />
本文の余計な改行を取ってください。（段落内の余計な改行を取るということです。）<br />
<br />
<h3>解答</h3><br />
<br />
q6の出力から続ける例を示します。ゴリ押しです。<br />
<br />
[bash]<br />
$ cat q6 | sed 's/^%.*//' |<br />
 awk '/begin/{if(!stop)print &quot;&quot;;stop+=1}<br />
 !stop &amp;&amp; !/section/{printf($0)}<br />
 stop || /section/{print}/end/{stop-=1}' |<br />
 sed 's/　 /n　 /' | sed 's/\\\\[sub]*section/\\n\\n&amp;/' <br />
[/bash]<br />
<br />
<h2>Q8</h2><br />
<br />
contents.texについて、次のように章節項のリストを作ってください。<br />
<br />
<br />
[bash]<br />
1 はじめに<br />
2 問題<br />
2.1 ロボットの姿勢と座標系<br />
2.2 観測<br />
2.2.1 ランドマークの識別<br />
2.2.2 ランドマークの姿勢計測<br />
2.2.3 計測値の記録<br />
2.2.4 計測値の誤差<br />
2.3 完全SLAM問題<br />
3 graph-based SLAMの実装例<br />
3.1 グラフのエッジを作る<br />
3.1.1 $\\V{\\mu}_{c,t,t'}, \\V{e}_{c,t,t'}$の計算<br />
3.1.2 $\\Sigma_{c,t,t'}, \\Omega_{c,t,t'}$の計算<br />
3.2 最適化問題を作る<br />
3.2.1 マハラノビス距離<br />
3.2.2 最適化する式<br />
3.3 $\\V{e}_{c,t,t'}$の勾配を求める<br />
3.4 問題を解く<br />
[/bash]<br />
<br />
<br />
<h3>解答</h3><br />
<br />
awkで章節項のカウンタを作ってうまく制御するのが一番素直な方法です。（二番目以降は思いつきませんが。）<br />
<br />
<br />
[bash]<br />
$ grep section contents.tex | sed 's/{/ /' | grep -v ^% |<br />
 sed 's/\\\\label.*//' | sed 's/}$//' |<br />
 awk '/^\\\\se/{s+=1;$1=s;ss=0;print}/\\\\subse/{ss+=1;$1=s&quot;.&quot;ss;sss=0;print}/<br />
\\\\subsub/{sss+=1;$1=s&quot;.&quot;ss&quot;.&quot;sss;print}'<br />
1 はじめに<br />
2 問題<br />
2.1 ロボットの姿勢と座標系<br />
2.2 観測<br />
2.2.1 ランドマークの識別<br />
2.2.2 ランドマークの姿勢計測<br />
2.2.3 計測値の記録<br />
2.2.4 計測値の誤差<br />
2.3 完全SLAM問題<br />
3 graph-based SLAMの実装例<br />
3.1 グラフのエッジを作る<br />
3.1.1 $\\V{\\mu}_{c,t,t'}, \\V{e}_{c,t,t'}$の計算<br />
3.1.2 $\\Sigma_{c,t,t'}, \\Omega_{c,t,t'}$の計算<br />
3.2 最適化問題を作る<br />
3.2.1 マハラノビス距離<br />
3.2.2 最適化する式<br />
3.3 $\\V{e}_{c,t,t'}$の勾配を求める<br />
3.4 問題を解く<br />
[/bash]
