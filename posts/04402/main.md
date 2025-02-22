---
Keywords: イラストで学ぶ人工知能概論,書評,薄口感想文
Copyright: (C) 2017 Ryuichi Ueda
---

# 「イラストで学ぶ人工知能概論」を拝読したので薄口感想文
ほんのちょっとだけお手伝いしてお駄賃にいただいた、谷口先生の「イラストで学ぶ人工知能概論」を、ようやく読みました。

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4061538233" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

<!--more-->

いくら研究者でも「人工知能」と言われたときにいろんな人がいろいろ思い浮かべる技術について、全部が全部分かっているわけでもありません。その点、本書では各理論や技術がバランス良く簡潔に紹介されており、勉強になりました。書き手側から見た感想は「これだけ広い範囲の用語を正確に記述するのはさぞかし神経を使ったことでしょう・・・。」に尽きます。

立命館ではこれを年に350人受講するというから、最初から人工知能に関してだいたいのことを網羅している学生が年に350人量産（これはちょっと言葉が悪いかも）されるということで、これは恐ろしいことです。

この本で勉強して、ロボットを自分でプログラムして動かせるようになれば、鬼に金棒です。ということで、本書の内容で実際にロボットをプログラムする方法の続編に期待したいところです。っていうかお前書けよとか言われそうです・・・。

んで、多少冗談も加えて各章の紹介を。ビブリオバトルの人たちに鼻で笑われそうですが。

<h2>1章</h2>

人工知能とは何か、人工知能研究の歴史と、ホイールダック2号の説明。特に赤いマフラーの説明。記号接地問題、フレーム問題の説明。

<h2>2章</h2>

系の説明と探索手法の説明。離散状態を取り扱う。離散状態しか取り扱わないのは問題を複雑にしないためによいかと。実際、よほどロボットのダイナミクスにこだわらないかぎり、離散状態sと有限個の行動aで物事を考えても結構動くので。

<h2>3章</h2>

最適経路の探索。A*。記憶の彼方から思い出した。感謝。

<h2>4章</h2>

ゲーム理論。ゲーム木。ミニマックス法等。古いロボカップ屋としては相手なんか認識できなかったのでノータッチだったけど最近はセンサがよくなってそうも言ってられないので大変だ。

これは本と関係なく個人的な呟きですが、産業用の自律移動機器に関しては（直接研究したことはありませんが）、「とにかく何か来たら止まる」あるいは「船舶のように衝突しないルールを決めておく」が原則なので、衝突回避の研究はあんまりしないつもり。だが、「マルチエージェントだとどうなる？」という査読コメントに「やりません！」と書くのも印象が悪いのでモニョモニョしている今日この頃。

<h2>5章</h2>

動的計画法。主に探索から見た動的計画法の話になっており、スタートから前向きにいく解法やダイクストラ法が主な手法として紹介されている。私はゴールから後ろ向きに価値関数を解く方法しか使わないので、視点が違うとこんなに違うんかという勉強になった。

<h2>6章</h2>

ベイズ理論。自分の計算が怪しかったらここを参考にしよう・・・（おい）

<h2>7章</h2>

強化学習。特にQ学習。本書でも紹介されているが実装にはSutton先生の本も読む必要あり。余談だが4章のナッシュ均衡等、所々に経済学の用語が出てきて面白い。

<h2>8, 9章</h2>

自己位置推定。ベイズフィルタ、パーティクルフィルタ。いきなりProbabilistic ROBOTICSを読むとほぼ全員、難しいという（というか大学の講義でやってないだけなんだが）アレルギー反応が出るのでここを読んでから挑戦するとよさそう。自分がこの考えに早く飛びつけたのは講義を真面目に受けてなかったからという理由もありそう。ただ、今や講義で扱われるようになったということなので、将来は明るいなあ（全くまとまりのない文章）。


ベイズフィルタは考え方さえわかればとても簡単なので、理解している人が一人でも増えることを草葉の陰から願っております。

<h2>10, 11章</h2>		
クラスタリング、パターン認識。K-means法、パーセプトロン、SVM、カーネル法と盛りだくさん。私が研究を中断してからブームになって浦島太郎感が凄まじい深層学習についても、少しだけ触れられています。	
 	
ここら辺はフリーソフトウェアでいろいろありそうなので使えるものの紹介があれば有用かなあと思います。
		
<h2>12章</h2>

自然言語処理の基礎が一通り。ここら辺は、私にとってはユーザーにしかなれない分野なので、基礎をおさえられて有難く。CaboChaは知らなかった。

<h2>13, 14章</h2>

記号理論と証明、質問応答。この世界はtrueとfalseだけ、あるいはファジーで語られることが多いけど、ベイズでやってる人もいるんだろうなーと思いながら読みました。

<h2>15章</h2>

まとめ。身体性、記号創発。自分もようやくこういうことを考える準備ができたので、コミットしていきたいなと。とりあえず文献読まないと・・・。ということで、巻末のブックガイドの本、まだ読んでないのを読むことから始めます。


以上。
