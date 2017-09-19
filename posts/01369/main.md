---
Keywords: プログラミング,Mac,Mavericks,Xcode
Copyright: (C) 2017 Ryuichi Ueda
---

# OS X 10.9 で Command Line Tools をインストールする方法
↓こちらにありますが、もっと簡単な方法を発見（と言っても1カ所違うだけですが。）。うーん。Xcodeは滅多に使わないのでうれしい。

<a href="http://www.computersnyou.com/2025/" target="_blank">http://www.computersnyou.com/2025/</a>

ということでXcodeアンインストール！アプリケーションからXcodeのアイコンをゴミ箱にぽぽいぽい（でいいらしい・・・）。（ドキュメントとかアンインストールされるんかい？誰かおしえてください。）

端末からgccを打つと・・・

```bash
uedamac:~ ueda$ gcc
xcode-select: note: no developer tools were found at '/Applications/Xcode.app', 
requesting install. Choose an option in the dialog to download the command line 
developer tools.
```

なんかダイアログ出た！迷わずインストール。

<a href="スクリーンショット-2013-10-27-12.16.18.png"><img src="スクリーンショット-2013-10-27-12.16.18-300x120.png" alt="スクリーンショット 2013-10-27 12.16.18" width="300" height="120" class="aligncenter size-medium wp-image-1372" /></a>

```bash
uedamac:~ ueda$ gcc
clang: error: no input files
```

大丈夫です。


・・・さて、<span style="color:red">今書いているものを書き直さなければ・・・</span>とほほ・・・。
