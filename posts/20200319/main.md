---
Keywords: 日記, Linux, シェル芸bot
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（2020年3月19日）

本日は大学でPCまわりのメンテナンスと新入生のオリエンテーションのスケジュール調整等でおわる。


## ノートPCのカーネルを少し戻す

ノートPC（機種等は下のコマンド参照）のUbuntu 19.10のカーネルをアップデートしたらハイバネートが効かなくなったので、`5.3.0-42-generic`から`5.3.0-40-generic`に戻した。


```
$ sudo dmidecode -t system | sed -n '1,/Version/p'
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 3.2.0 present.

Handle 0x0012, DMI type 1, 27 bytes
System Information
	Manufacturer: LENOVO
	Product Name: 20R1CTO1WW
	Version: ThinkPad X1 Carbon 7th
```

久しぶりにgrubをいじったが、なんか設定ファイルがややこしくなっててGUIツール（`grub-customizer`）のお世話になった。システムがUnix的な考え方とはなんとなく合わない方法にいろいろ行ってないか心配。

## [SoftwareDesign 4月号](https://amzn.to/33zA0BV)届く

**シェル芸人からの挑戦状が終わってしまうううううううううううう**

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ついに最終回です今まで3年近くありがとうございました。今回のお題は「シェル芸人による珠玉（たまたま）」です。  <a href="https://twitter.com/hashtag/%E9%81%95%E3%81%86?src=hash&amp;ref_src=twsrc%5Etfw">#違う</a><a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/6EQxndmnkM">pic.twitter.com/6EQxndmnkM</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1240618536780750849?ref_src=twsrc%5Etfw">March 19, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


また逢う日まで。


## プライベートシェル芸botを持った

よく落ちる割には全世界の暇のない成金が憧れるというプライベートジェット並に贅沢な、**プライベートシェル芸bot**のオーナーになりますた。
といってもシェル芸botのパパ（←本人はこう呼ばれたくないかもしれない）である[ふるつき氏](https://twitter.com/theoremoon)のリポジトリを持ってきて、Twitterからアプリケーションのキーをもらってゴニョゴニョやっただけです。
個人的に好き勝手に運用するつもりです。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">＿人人人人人人人＿<br>＞　ふはははは　＜<br>￣Y^Y^Y^Y^Y^Y^Y^￣<br>　　　　　　👑<br>　　　　（💩💩💩）<br>　　　（💩👁💩👁💩）<br>　　（💩💩💩👃💩💩💩）<br>　（💩💩💩💩👄💩💩💩💩） <a href="https://t.co/bHnKud64bA">https://t.co/bHnKud64bA</a></p>&mdash; uedashbot (@uedashbot) <a href="https://twitter.com/uedashbot/status/1239662466197381121?ref_src=twsrc%5Etfw">March 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


　シェル芸botの作り方、もう少し詳しく書いておくと、だいたいこんな感じです。

#. <span style="color:red">「任意のコマンドを実行するボットを作りたい！！！１１１」</span>とTwitterに申請してキーをもらう
#. https://github.com/theoremoon/ShellgeiBot-Image をクローンしてdockerのイメージをビルド
#. https://github.com/theoremoon/ShellgeiBot をクローンしてコンパイル
#. Twitterのキーを保存した設定ファイル、dockerの情報や反応するハッシュタグなどを書いた設定ファイル（下の例を参照のこと）を作る
#. `sudo nohup ./ShellgeiBot twconf.json ShellgeiConfig.json` （パスは適切に記述のこと）

で動きます。ただし、botがシェル芸を打つ方のアカウントをフォローしてないと動きません（これを見落としていて1時間くらい悩んでしまった・・・）。
それから、Twitterへの申請が今は結構めんどくさいことになってます。フォームに英作文して、不備があるとメールでもっと説明してくれと来て・・・と何日もかかります。もし必要であれば例文は提供いたします。

```
$ cat twconf.json
{
	"ConsumerKey": "unkounkounkounkounkounko",
	"ConsumerSecret": "unkounkounkounkounkounkounkounkounkounkounkounko",
	"AccessToken": "unkounkounkounko-unkounkounkounkounkounkounkounkounko",
	"AccessSecret": "unkounkounkounkounkounkounkounkounko"
}
$ cat ShellgeiConfig.json
{
	"dockerimage": "shellgeibot",
	"timeout": "10s",
	"workdir": ".",
	"memory": "100M",
	"mediasize": 250,
	"tags": ["shellgei3"]
}

```

　botはTwitterからハッシュタグを検索してツイートするという仕組みなので、
手元のLinuxのノートPCでも動きます。ハッシュタグの検索とツイートは
上のリポジトリの「ShellgeiBot」がやって、コマンドの実行は
「ShellgeiBot-Image」がやるという役割分担になっているので、
ShellgeiBotの方のコードを読んでみると面白いと思います。

　あとの細かいことは本家のリポジトリのREADME等におまかせします。
<span style="color:red">あ、一つ注意ですけど、自分のシェル芸botから他のシェル芸botをフォローすると、
互いに無限にコマンドを投げあうことができてしまい、最悪両方Twitterから退場になります。ご注意を。</span>


洗濯物干して寝る。
