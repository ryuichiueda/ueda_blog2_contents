---
Keywords: どうでもいい,PID制御,上海総合指数,振動,株,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記 ---ちうごく株のPID制御
下のツイートのように <a href="http://nikkei225jp.com/china/" target="_blank">http://nikkei225jp.com/china/</a> で上海総合指数をしばしば確認するのが日課になっており。ちと図を拝借しました。

<blockquote class="twitter-tweet" lang="ja"><p lang="ja" dir="ltr"><a href="http://t.co/kRvO2rHyWT">http://t.co/kRvO2rHyWT</a> から&#10;&#10;・前半1時間と後半1時間で波形が違う&#10;・前半1時間はPID制御でいうところのP制御だけやっている感じに値が振動&#10;・後半は最後の10分が何か変だが波形は正常（下の日経の波形参照） <a href="http://t.co/s5iWRn7gD4">pic.twitter.com/s5iWRn7gD4</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/626964786249605120">2015, 7月 31</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

他のサイトのグラフだと目が粗いのか確認できないのですが、ツイートのグラフを見ると、明らかに前半1時間と後半1時間の波形が違います。

で、ツイートのようにこれは経済というよりは制御の点で非常に面白い。前半1時間の波形が丸く波打ってますが、これは下手な制御（ある目標値と現在値の差だけを見て力を加減する制御）をしたときに出る振動の形に似ているような気がします。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="http://t.co/kRvO2rHyWT">http://t.co/kRvO2rHyWT</a>&#10;より 7/29&#10;&#10;最後の1時間の波形が少し丸くて周期的&#10;&#10;<a href="https://twitter.com/hashtag/P%E5%88%B6%E5%BE%A1?src=hash">#P制御</a> <a href="http://t.co/XZKElHBsPJ">pic.twitter.com/XZKElHBsPJ</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/627251069677117441">July 31, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="http://t.co/kRvO2rHyWT">http://t.co/kRvO2rHyWT</a>&#10;より 7/30&#10;&#10;この日は一日中波形が丸いが、最後の一時間の周期的な波が印象的。&#10;&#10;<a href="https://twitter.com/hashtag/P%E5%88%B6%E5%BE%A1?src=hash">#P制御</a> <a href="http://t.co/LXC9VarVlp">pic.twitter.com/LXC9VarVlp</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/627251293816496128">July 31, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

制御・・・しているのか？？？（愚問）
