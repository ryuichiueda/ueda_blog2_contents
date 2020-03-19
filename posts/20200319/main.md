---
Keywords: 日記
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（2020年3月19日）

本日は大学でPCまわりのメンテナンスと新入生のオリエンテーションのスケジュール調整等でおわる。


## ノートPCのカーネルを少し戻す

ノートPC↓のUbuntu 19.10のカーネルをアップデートしたらハイバネートが効かなくなったので、`5.3.0-42-generic`から`5.3.0-40-generic`に戻した。


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

久しぶりにgrubをいじったが、なか設定ファイルがややこしくなっててGUIツール（`grub-customizer`）のお世話になった。システムがUnix的な考え方とはなんとなく合わない方法にいろいろ行ってないか心配。

## SoftwareDesign 4月号届く

**シェル芸人からの挑戦状が終わってしまうううううううううううう**

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">ついに最終回です今まで3年近くありがとうございました。今回のお題は「シェル芸人による珠玉（たまたま）」です。  <a href="https://twitter.com/hashtag/%E9%81%95%E3%81%86?src=hash&amp;ref_src=twsrc%5Etfw">#違う</a><a href="https://twitter.com/hashtag/gihyosd?src=hash&amp;ref_src=twsrc%5Etfw">#gihyosd</a> <a href="https://t.co/6EQxndmnkM">pic.twitter.com/6EQxndmnkM</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1240618536780750849?ref_src=twsrc%5Etfw">March 19, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


また逢う日まで。
