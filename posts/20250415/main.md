---
Keywords: 自作シェル,rusty_bash,寿司シェル
Copyright: (C) 2025 Ryuichi Ueda
---

# 自作シェルの進捗（2025年4月15日）

　[前回](/?post=20250329)（3月29日）からの進捗です。

## macOSでの補完

　alphaブランチのコードでほぼ動くようになりました。ただし、bash-completionを読み込むときにいくつかエラーが出ます。これについてはもうちょっと整理してから改めてここに書きたいと思ってます。

## Bashの公式リポジトリのテスト

　とりあえずこんな感じでじわじわ対応中です。

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:eha6t6k5cy5oj33pvunkhdrg/app.bsky.feed.post/3lmtnnecgzk2c" data-bluesky-cid="bafyreicit7xgdrfwidtqdindhwawdjgq3hfxrxuh56cecfetf3aksbn24y" data-bluesky-embed-color-mode="system"><p lang="ja">current compatibility of #rusty_bash to #bash<br><br><a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg/post/3lmtnnecgzk2c?ref_src=embed">[image or embed]</a></p>&mdash; Ryuichi Ueda (<a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg?ref_src=embed">@ueda.tech</a>) <a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg/post/3lmtnnecgzk2c?ref_src=embed">2025年4月15日 17:24</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>

通ったテストは、

- run-invert: !で終了ステータスをひっくり返す機能のテスト
- run-precedence: `&&`、`||`の優先度のテスト
- run-ifs: IFSまわりのテスト
- run-globstar: globstar（ワイルドカード**）のテスト
- run-braces: ブレース展開のテスト
- run-extglob2: 拡張グロブのテスト 
- run-extglob3: 同上

です。あと、エラーメッセージが一致せず通ってませんが、`run-arith`（算術式展開のテスト）も標準出力はすべて一致してます。こういうテスト、アーキテクチャが悪いとあっちを直すとこっちがおかしくなり、ということが起こりがちですが、とりあえずいまのところは大丈夫そうです。ただ、あと76個通さないといけないので、辛いです。

　テストでおもしろかったのをいくつか挙げときます。[Bashの公式リポジトリ](https://savannah.gnu.org/git/?group=bash)内にあります。

### tests/arith3.subのなかのテスト

　`RANDOM`なのに毎回同じ結果にならないといけないそうです。いや、まあそうなんですが、それテストしなきゃいけないんでしょうか？合わせるの大変でした。

```bash

RANDOM=42

(( dice[RANDOM%6+1 + RANDOM%6+1]+=v )) #必ず6にならないといけない
echo ${dice[6]}

(( dice[RANDOM%6+1 + RANDOM%6+1]-=v )) #必ず7にならないといけない
echo ${dice[7]}

(( dice[RANDOM%6+1 + RANDOM%6+1]+=2 )) #以下同様
echo ${dice[8]}

(( dice[RANDOM%6+1 + RANDOM%6+1]*=2 ))
echo ${dice[5]}

### これ以上同じコードがあったらたぶん無理 ###
### （6, 7, 8, 5, ...という並びをあわせられない） ###
```

### tests/arith6.sub

　これが`run-arith`のラスボスでした。変数が数値になるまで何回も評価されることを利用した再起処理です。

```bash
n=0 a="(a[n]=++n)<7&&a[0]"; ((a[0])); echo "${a[@]:1}"
### 出力は「1 2 3 4 5 6 7」###
```

できました（死ぬ）

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:eha6t6k5cy5oj33pvunkhdrg/app.bsky.feed.post/3lmemzm7sm22d" data-bluesky-cid="bafyreifiy2igxseqgvumtrs4vk4puwy73vxacniswfibgkw7jrpha4fbvm" data-bluesky-embed-color-mode="system"><p lang="en">This is an example.  #bash #rusty_bash<br><br><a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg/post/3lmemzm7sm22d?ref_src=embed">[image or embed]</a></p>&mdash; Ryuichi Ueda (<a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg?ref_src=embed">@ueda.tech</a>) <a href="https://bsky.app/profile/did:plc:eha6t6k5cy5oj33pvunkhdrg/post/3lmemzm7sm22d?ref_src=embed">2025年4月9日 18:03</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>

### tests/dollar-at-star

　これは`IFS`に区切り文字をセットしたときの`$*`の挙動をテストするスクリプトです。技術的な面白さもそうなんですが、`set bob 'tom dick harry' joe`で間抜けな5人組の顔が思い浮かんで笑いが止まらなくなりました。

```bash

IFS='/'
set bob 'tom dick harry' joe
set $*
recho $#
recho $1
recho $2
recho $3
```

　ちなみに出力はこうならないといけません。

```bash

$ IFS='/'
$ set bob 'tom dick harry' joe
$ set $*
$ echo $1
bob
$ echo $2
tom dick harry
$ echo $3
joe
```

以上です。またなんか面白いのがあれば紹介します。

## クソバグのfix

　で、さっき`run-arith`の標準出力が一致して事実上テストが通ったみたいな話を書いたのですが、実は上に挙げたラスボスを倒して通ったにもかかわらず、自作シェルが小学生でもやらん計算間違いをすることが判明しました。

```bash

🍣 echo $(( 1 - 2 + 3 ))
-4   # 1 - (2 + 3) だと思っているっぽい
```

Bashのテストでも自分のテストでも漏れてたみたいです。いやーこわいですね。仕事だと思ったら背筋が凍ります。

　これは結局、計算式を逆ポーランド記法に直すときに、`-`より`+`を優先させてしまっていたという初歩的なミスでした。なんで全部テスト通ったんだろ・・・。

　もう一つ反省のために除去したクソバグを紹介しておくと、こういうのもありました。

<iframe src="https://mi.shellgei.org/embed/notes/a6hb9x6w2t" data-misskey-embed-id="v1_bef34f15-9099-42ea-b0c2-781d7619363d" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border: none; width: 100%; max-width: 500px; height: 300px; color-scheme: light dark;"></iframe>
<script defer src="https://mi.shellgei.org/embed.js"></script>

`read`が標準入力を読む前に、続きのシェルスクリプトを読んでしまうというアホみたいなバグで、すぐ除去しました。


　いやーこわいこわい。現場からは以上です。
