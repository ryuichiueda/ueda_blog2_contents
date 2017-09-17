# 雑記（2017年9月2日）
<h3>シェル芸botの遷宮</h3><br />
<br />
諸事情により、シェル芸botのお父様のVPSから、ConoHaから提供いただいているUSP友の会のVPSへ。友の会のVPSはCentOSだったがUbuntuに入れ替え。運用停止して様子見状態だったメーリングリストは廃止。ウェブサイトはrsync等を駆使して存続。bash製なので移植は極めて簡単だった。<br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="zh" dir="ltr">多分遷宮完了！</p>&mdash; ふるつき (\@theoldmoon0602) <a href="https://twitter.com/theoldmoon0602/status/903791744155779073">2017年9月2日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="und" dir="ltr">💩<br>💩<br>💩<br>💩<br>💩<br>💩<br>💩<br>💩<br>💩<br>💩 <a href="https://t.co/EN3RCy7Us3">https://t.co/EN3RCy7Us3</a></p>&mdash; シェル芸bot (\@minyoruminyon) <a href="https://twitter.com/minyoruminyon/status/903794375393767424">2017年9月2日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
良かったです。<br />
<br />
<h3><a href="https://www.ospn.jp/osc2017-chiba/">OSC</a></h3><br />
<br />
苦手な事務を頑張って無事終了。102名というところで、もうちょいお呼びできたんでねえかと。どうも自分の押しの悪さが集客に微妙に効いているような気がしないでもない。シェル芸界隈にもっと呼びかければ良かったが・・・。<br />
<br />
[caption id="attachment_10264" align="aligncenter" width="300"]<a href="IMG_8471.jpg"><img src="IMG_8471-300x225.jpg" alt="" width="300" height="225" class="size-medium wp-image-10264" /></a> 秋のような清々しい天気でした。[/caption]<br />
<br />
<a href="IMG_8479.jpg"><img src="IMG_8479-300x225.jpg" alt="" width="300" height="225" class="aligncenter size-medium wp-image-10267" /></a><br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">謎設備TA <a href="https://twitter.com/hashtag/osc17cb?src=hash">#osc17cb</a> <a href="https://t.co/6Kch3EkVD6">pic.twitter.com/6Kch3EkVD6</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/903888174568443904">2017年9月2日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">とってもヘルシー <a href="https://twitter.com/hashtag/osc17cb?src=hash">#osc17cb</a> <a href="https://t.co/ZED5J2sRBW">pic.twitter.com/ZED5J2sRBW</a></p>&mdash; Ryuichi Ueda (\@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/903911411390193665">2017年9月2日</a></blockquote><br />
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><br />
<br />
自身の反省はさておき、会はとても良い雰囲気で進みました。お越しいただき有難うございました。<br />
<br />
<h3>本がよく売れる</h3><br />
<br />
夏休み終わるから？<br />
<br />
<h3>アサーション</h3><br />
<br />
前回のシェル芸勉強会で鳥海さんがPerlのアサーションの話をされた時に、アサーション is 何？と調べていたら、<a href="https://www.direct-commu.com/colums/relation/relation_012_02_asa-shyon.html">こういうページ</a>が引っかかった。とても大事だと思う。Perl関係ないけど。特に自分の場合、発言が攻撃的な人が苦手なので（生理的にもビビってダメなのと、腐っても研究者として、議論の方法について厳しい訓練を受けているのでちょっとありえないと思うので）、急に「もう一生話しかけるな」ということをさらっと言って本当に話をしなくなることがあるので、その前にこういうのを勧めれば良いのではないかなと考えたり。余計なお世話か。<br />
<br />
<h3>raspimouse_ros_2の手直し</h3><br />
<br />
本日<a href="https://github.com/ryuichiueda/raspimouse_ros_2">raspimouse_ros_2</a>（ラズパイマウスをROSで使うときの基本パッケージ）にプルリクエストをいただいて、<a href="https://blog.ueda.tech/?p=10115">この前のハッカソン</a>で作りっぱなしでテストが通っていないことを発見。tf2をTravisの環境にインストールしないといけなかったらしく、テストの環境構築スクリプトに1行追加。無事通った。<br />
<br />
<br />
早く寝たい。
