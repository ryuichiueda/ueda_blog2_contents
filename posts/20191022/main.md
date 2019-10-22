---
Keywords: SoftwareDesign, シェル芸, シェル芸人からの挑戦状
Copyright: (C) 2019 Ryuichi Ueda
---

# 宣伝（おまけ問題つき）: SoftwareDesign 11月号

　発売中です。今回のシェル芸人からの挑戦状は実用本位です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">今月のSoftwareSesignのシェル芸人からの挑戦状はログファイルの解析です。実戦的です。<br><br>ところで、今までずっと疑問だったんですけど、背景の影になってる仁王立ちお兄さんお姉さん方は一体誰なんすかね？<br><br> <a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/nuXdDGdrTB">pic.twitter.com/nuXdDGdrTB</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1186264390657441792?ref_src=twsrc%5Etfw">October 21, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 幻の第4問

　実は今回は3問しか出題してません。前の3問の分量が多すぎて私の書いた4問目がボツになりました（涙）。せっかくなので、ここに掲載しておきます。


### 問題4: USBデバイスの監視

* 出題、解答、解説: 上田
* 難易度: 初級

　先月号で、USBの抜き差しを監視する次のような問題を出題しました。

```
/sys/を使い、USB機器の抜き差しを監視するワンライナーを書いてください。
周期は1秒おきで、1秒以内に2つ以上の機器は抜き差しがあることは
考慮しなくてもよいこととします。抜かれたら「抜かれました」、
挿されたら「挿されました」と表示してください。
```

今度は、これを`/var/log`下のファイルを使って実装してみてください。今度は1秒以内ではなく即時に出力し、複数の抜き差しがあっても対応してください。表示する文言は自由です。なお、何らかのシステムに組み込むようなものではなく、ちょっとした機会に小手先で使うことを想定しています。


### 解答

　とりあえずどのログファイルを見れば分からない場合は、USB機器を抜き差しした後、関連しそうなログが追加されたファイルがないか調べてみましょう。`grep`を使って探していきます。これは、筆者の環境の例です。

```
$ cd /var/log
### 今日のログを探す（9月8日の例） ###
$ sudo grep "Sep *8" ./ -R | head
./syslog:Sep  8 08:47:06 myserver ...
（他、9件）
```

この例では正規表現を使い、今日の日付を探して最初の10件を表示しています。`grep`の`-R`はディレクトリ下のファイルを全て再帰的に検索するためのオプションです。


　さらに件数を絞り込みましょう。`usb`で調べます。

```
### usbという文字列を探す ###
$ sudo grep "Sep *8" ./ -R | grep usb | head
./syslog:Sep  8 08:47:06 myserver ...
（まだ10件出る）
$ sudo grep "Sep *8" ./ -R | grep usb | uniq -w 20
./syslog:Sep  8 08:47:06 myserver kernel: [    0.034612] usbcore: ...
./syslog:Sep  8 08:50:17 myserver kernel: [  197.851221] usb 4-3: New USB device found, ...
./kern.log:Sep  8 08:47:06 myserver kernel: [    0.034612] usbcore: ...
./auth.log:Sep  8 09:01:58 myserver sudo:     ueda : ... COMMAND=/bin/grep -m 1 -i usb ./ -R
```

　最後の`uniq -w 20`は、「最初の20文字だけ比較して重複していないものを出力する」という意味になります。これで、筆者の環境では4件に絞り込めました。この4件の出力をよく見ると、`syslog`に`New USB device found ...`という文言が書かれています。`syslog`を監視すればよさそうです。

　もちろん、この例では検索漏れ（例えば大文字の`USB`など）があるかもしれませんが、とりあえずひとつ適切そうなログファイル`syslog`が見つかりました。Ubuntuの場合、`syslog`には、他の様々な機器の情報や起動、シャットダウンの際の情報が記録されます。


　次に、`syslog`の中身を調べましょう。`less syslog`でログを開いて、すぐにG（Shift+G）を押して下の方からさきほどのUSBの抜き差しの記録をみます。他のログに埋もれている場合はもう一度機器を抜き差ししてみましょう。

```
$ less syslog
（Shift+G） 
Sep  8 10:01:32 myserver kernel: [ 4473.226091] usb 4-3: new SuperSpeed USB device number 7 using xhci_hcd
Sep  8 10:01:32 myserver kernel: [ 4473.248351] usb 4-3: New USB device found, idVendor=0bda, idProduct=8153
（中略）
Sep  8 10:02:32 myserver kernel: [ 4533.157138] usb 4-3: USB disconnect, device number 7
```

ログを見ると、機器が挿されたときはいくつかログが記録されています。また、抜かれたは一行、その旨が記録されています。問題に対する解答としては、挿されたときの「`New USB device found`」と抜かれたときの「`USB disconnect`」を表示すればよさそうです。

　ということで、解答例を示します。これで十分でしょう。

```
$ tail -f syslog | grep -e 'New USB device found' -e 'USB disconnect'
Sep  8 10:28:52 Ubuntu18server kernel: [  188.863597] usb 4-5: New USB device found, idVendor=0bda, idProduct=8153
Sep  8 10:29:06 Ubuntu18server kernel: [  202.450685] usb 4-5: USB disconnect, device number 3
Sep  8 10:29:14 Ubuntu18server kernel: [  211.187090] usb 4-6: New USB device found, idVendor=0bda, idProduct=8153
Sep  8 10:29:16 Ubuntu18server kernel: [  213.072891] usb 4-6: USB disconnect, device number 4
```

`tail -f`で、追記されたログを逐次出力し、抜き差しを表すログを`grep`で選別します。検索語が二つあると正規表現を凝りたいと思うかもしれませんが、`grep`は`-e`をつけることで複数の正規表現を並べて書くことができます。


　以上、幻の第4問でした。

## その他

　それから、これは必読ですねー（棒）

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">出た。 <a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/7GkjyFMpma">pic.twitter.com/7GkjyFMpma</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1186599694329245696?ref_src=twsrc%5Etfw">October 22, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　ということで、よろしくお願いいたします。

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/B07Y1WQNCW/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/514xVSArQEL._SL160_.jpg" width="113" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/B07Y1WQNCW/ryuichiueda-22">ソフトウェアデザイン 2019年11月号</a></dt>
          <dd>[本間 咲来 山本 達也 武井 宜行 吉川 英一 山田 祥寛 神戸 康多 福田 鉄平 天地 知也 星 直史 安藤 幸央 結城 浩 武内 覚 宮原 徹 平林 純 くつなりょうすけ 坂井 恵 杉村 貴士 高橋 憲一 中島 明日香 伊藤 雄貴 職業「戸倉彩」 中村 壮一 山田 泰宏 田代 勝也 上田 隆一 mattn 青田 直大 中島 雅弘 あわしろいくや 法林 浩之 清水 俊之介 樽石 将人 やまねひでき 古守 花織 杉山 貴章]</dd>
          <dd>技術評論社 2019-10-18 (Release 2019-10-18)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>
