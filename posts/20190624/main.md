---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月24日） 

## [bashcms本](https://www.kadokawa.co.jp/product/301905000145/)がKADOKAWAさんから自宅に届いた

　昨日届きました。怖くて開いてません・・・。なんか内容が薄い気がしながら書いていたら初版よりずいぶん分厚くなってしまいました。長けりゃいいってもんでないので、あんまりよくないですが・・・よろしくおねがいします！

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">本が届いてたー！二版なのに初版と分厚さが全然違うーーー！！分厚いーーーー！！！ <a href="https://twitter.com/hashtag/%E3%81%94%E3%82%81%E3%82%93%E3%81%AA%E3%81%95%E3%81%84?src=hash&amp;ref_src=twsrc%5Etfw">#ごめんなさい</a> <a href="https://twitter.com/hashtag/bashcms%E6%9C%AC?src=hash&amp;ref_src=twsrc%5Etfw">#bashcms本</a> <a href="https://t.co/A960biMQda">pic.twitter.com/A960biMQda</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1142728553714208768?ref_src=twsrc%5Etfw">2019年6月23日</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/51T-SfWPsPL._SL160_.jpg" width="124" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>KADOKAWA 2019-06-28 (Release 2019-06-28)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>



## ラズパイいじり

　某外部講師の先で講義に使うラズパイをセットアップ（Raspberry Pi 3B+にUbuntu 18.04をインストールして使うソフトをセットアップ）していたがWiFiの設定で撃沈。自分のNetplanの設定がおかしいかWiFiのデバイスドライバがぶっ壊れていたかどっちかで18時になってしまい時間切れ。その後19時前に研究室に戻って慣れた環境でおさらい。研究室ではうまく設定できた。Netplanというのは今までのネットワーク設定の代わりに使うもので、Ubuntu 18.04からデフォルト。まだ解説ができないので、代わりに自分の書いた設定ファイルを晒す。パスフレーズ等はunkoに変更済み。

```
ubuntu@ubuntu:~$ cat /etc/netplan/50-cloud-init.yaml
# This file is generated from information provided by
# the datasource.  Changes to it will not persist across an instance.
# To disable cloud-init's network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
    version: 2
    ethernets:
        eth0:
            dhcp4: no
            addresses: [192.168.2.123/24]
            gateway4: 192.168.2.1
            nameservers:
                addresses: [8.8.8.8,8.8.4.4]
            optional: true
    wifis:
        wlan0:
            addresses: [192.168.2.124/24]
            gateway4: 192.168.2.1
            dhcp4: no
            optional: true
            nameservers:
                addresses: [8.8.8.8,8.8.4.4]
            access-points:
                "unko_x":
                    password: unkosuperunko
```


この設定で有線も無線も生かしたまま柔軟に使えるようになった。

## 帰り際に[つくばチャレンジ](https://tsukubachallenge.jp/2019/)チームのロボットと遭遇

　ここ数日帰ろうとしたらチームのロボットに会うのでがんばってるなと。本当はついて行きたいんだけど家のことがあるので帰宅せねばならず悔しい。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">林原研（当研究室もお手伝い）のつくばチャレンジのメンバーが夜9時になってもまだ頑張ってました。梅雨の間の晴れは貴重です。 <a href="https://t.co/Od3J4Srl6M">pic.twitter.com/Od3J4Srl6M</a></p>&mdash; CIT未ロボ上田研 (@uedalaboratory) <a href="https://twitter.com/uedalaboratory/status/1143139955591434240?ref_src=twsrc%5Etfw">June 24, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### その他

　いきりステーキの別バージョンが存在した。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">海浜幕張駅で、いなり寿司の店を見つけた。珍しい。 <a href="https://t.co/zIZNiHx9bf">pic.twitter.com/zIZNiHx9bf</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1142997150046887937?ref_src=twsrc%5Etfw">June 24, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



帰って寝る。
