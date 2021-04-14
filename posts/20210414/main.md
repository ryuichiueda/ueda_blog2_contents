---
Keywords: 日記
Copyright: (C) 2021 Ryuichi Ueda
---

# 日記（2021年4月14日）

本日は3年生の研究室見学の対応。ほかの研究室が学生総出で対応のところ、上田研は学生は対応せずで、らしさ全開（アカン）

## GlueLang

昨日今日は、コードを整理しつつ、おせっかい機能（echoなしで文字列をパイプに流せるとか）を削除してました。本業の妨げにならないように風呂で作業。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">意識が高いので風呂とプログラムと飲酒を同時に済ます。 <a href="https://t.co/2CTsN9rTcQ">pic.twitter.com/2CTsN9rTcQ</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1382255262279499778?ref_src=twsrc%5Etfw">April 14, 2021</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


あと、仕様上の決断として、標準入出力のファイルディスクリプタはリダイレクト記号で操作しないで、コマンドで対応することにしました。例えば次のように`dup`を使うと標準出力と標準エラー出力を入れ替えることができるので、`dup`のあとに任意コマンドを`exec`すると、そのコマンドの標準出力と標準エラー出力を入れ替えることができます（たぶん）。


```c
#include <unistd.h>
using namespace std;


int main(int argc, char const* argv[])
{
	dup2(1, 3);
	dup2(2, 1);
	dup2(3, 2);

	cout << "stdout" << endl;  //標準エラー出力から出てくる
	cerr << "stderr" << endl;  //標準出力から出てくる

	exit(0);
}
```


## 今日の猫

イカってました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">本日のSoftwareDesign代替イカ耳 <a href="https://t.co/B8ZMQyegyC">pic.twitter.com/B8ZMQyegyC</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1382278783273558026?ref_src=twsrc%5Etfw">April 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


寝る。
