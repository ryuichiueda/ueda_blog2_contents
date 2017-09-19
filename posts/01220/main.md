---
Keywords: nkf,UNIX/Linuxサーバ,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# URLエンコードを元に戻してくれる nkf --url-input
調べれば調べるほどザクザク出てくるnkfのオプションですが、今日はこんなのを発見しました。

URLエンコードを元に戻してくれる --url-input です。

[bash]
uedamac:~ ueda$ echo 'http://ja.wikipedia.org/wiki/%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%BB%E3%82%A6%E3%82%A7%E3%82%A4%E3%83%B4_(%E9%9F%B3%E6%A5%BD)' | nkf --url-input
http://ja.wikipedia.org/wiki/ニュー・ウェイヴ_(音楽)
[/bash]

俺的に超便利！
