---
Keywords:パーティクルフィルタ,POMDP,Q-MDP,研究,確率ロボティクス,自己位置推定,自律ロボット
Copyright: (C) 2017 Ryuichi Ueda
---
# <!--:ja-->この前の発表資料（自律分散システムシンポジウム）<!--:-->
<!--:ja-->学会での発表はほぼ6年ぶりでした。こういう直接は何の役にも立たんことを大真面目に考えたのも6年ぶり。理論の空白地帯に踏み込んで行くのが私の仕事なので、10年後はサラリーマンに戻るのを覚悟しつつ、自分の気づいていることをひたすら紙に落とし続けて行かねばなりません。<br />
<br />
この発表は要は何かというと、例えば人間が真っ暗な家の中で何処かに行こうとすると、壁伝いになんとか行けてしまうわけですが、そのような「場所がわからんならわからんなりに動いてゴールまで行く」というのを確率モデルで再現できないかというのが動機になってます。<br />
<br />
ロボットは「あるゴール地点まで行け」と指令を受けているのに、今現在、自分のいる地点を知る目印が不十分で、自分の位置を一点に定めることができないという状況です。<br />
<br />
細かいことは抜きに結論だけ言うと、ロボットがゴール地点を効率よく探し出してゴール地点に向かう行動決定のモデルを作ることができました。<br />
<br />
<iframe src="http://www.slideshare.net/slideshow/embed_code/30567186" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px 1px 0; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/ryuichiueda/ss-30567186" title="第26回自律分散システムシンポジウムの講演資料" target="_blank">第26回自律分散システムシンポジウムの講演資料</a> </strong> from <strong><a href="http://www.slideshare.net/ryuichiueda" target="_blank">Ryuichi Ueda</a></strong> </div><br />
<br />
スライドにはgifアニメが二つありますが、slideshareでは動かないので下に貼り付けます。（動いてなくてもクリックすると動きます。）<br />
<br />
<br />
<a href="97211-animation.gif"><img src="97211-animation-300x300.gif" alt="97211-animation" width="300" height="300" class="aligncenter size-medium wp-image-1935" /></a><br />
<br />
<br />
点ランドマークが一つしか無いためロボットの位置が常に不定（ドーナッツ状の領域のどこかにいるということしか分からない状態）のままロボットは行動決定しますが、円状に分布したパーティクルを消し込むようにロボットが動くことで、ロボットはゴールを探し当てます。<br />
<br />
<br />
今後なんですが、違う環境で同じように位置が不定になる状況を作り、ロボットのゴール探し行動を作ろうと考えてますが、他の仕事に追い回されて・・・<br />
<br />
おしまい。<br />
<br />
出典：<br />
<br />
上田隆一:<br />
“タスクの到達度予測による信念状態の評価,”<br />
第26回自律分散システムシンポジウム, pp. 2A1-1, 2014.
