# OS X 10.9 で Command Line Tools をインストールする方法
↓こちらにありますが、もっと簡単な方法を発見（と言っても1カ所違うだけですが。）。うーん。Xcodeは滅多に使わないのでうれしい。<br />
<br />
<a href="http://www.computersnyou.com/2025/" target="_blank">http://www.computersnyou.com/2025/</a><br />
<br />
ということでXcodeアンインストール！アプリケーションからXcodeのアイコンをゴミ箱にぽぽいぽい（でいいらしい・・・）。（ドキュメントとかアンインストールされるんかい？誰かおしえてください。）<br />
<br />
端末からgccを打つと・・・<br />
<br />
[bash]<br />
uedamac:~ ueda$ gcc<br />
xcode-select: note: no developer tools were found at '/Applications/Xcode.app', <br />
requesting install. Choose an option in the dialog to download the command line <br />
developer tools.<br />
[/bash]<br />
<br />
なんかダイアログ出た！迷わずインストール。<br />
<br />
<a href="スクリーンショット-2013-10-27-12.16.18.png"><img src="スクリーンショット-2013-10-27-12.16.18-300x120.png" alt="スクリーンショット 2013-10-27 12.16.18" width="300" height="120" class="aligncenter size-medium wp-image-1372" /></a><br />
<br />
[bash]<br />
uedamac:~ ueda$ gcc<br />
clang: error: no input files<br />
[/bash]<br />
<br />
大丈夫です。<br />
<br />
<br />
・・・さて、<span style="color:red">今書いているものを書き直さなければ・・・</span>とほほ・・・。
