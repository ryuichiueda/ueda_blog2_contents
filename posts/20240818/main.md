---
Keywords: 自作シェル, 寿司シェル, sush
Copyright: (C) 2024 Ryuichi Ueda
---

# 自作シェルで浮動小数点の計算ができるようにしたった

　7/27以来の[自作シェル](/?page=rusty_bash)の開発の進捗報告です。何年も作り続けてものすごい時間かけてるのに全然ブログ書かないの、ほんと作ってればよくて人に使ってもらう気がないんだなと自分で呆れております。学生にはそういうのは良くないと日頃言ってるのになんですかこれは。

## 本題

　ということで、（次もまた1ヶ月後になりそうですが）ちょっとテンション高めにできたことを書くと、Bashでてきない「`$(( ))`のなかでの浮動小数点演算」を自作シェルに実装しました。

　こんな感じで使えます。

```bash
### 浮動小数点数どうしの足し算 ###
🍣 echo $(( 1.1 + 2.2 ))
3.3000000000000003
### 整数にも足せる ###
🍣 echo $(( 1 + 2.2 ))
3.2
### 浮動小数点数の浮動小数点数乗 ###
🍣 echo $(( 3.3**3.3 ))
51.415729444066585
### 割り算 ###
🍣 echo $(( 1.0/3 ))
0.3333333333333333
### 変数も使える ###
🍣 A=0.1111111111111111111 ; echo $(( A * 9 ))
1
```

　まだ自分で使っていて便利な場面はないのですが、たぶんそのうち来るでしょう。

## デモ動画

　前回YouTubeにのせたら海外からも反応来たので今回も真面目にのっけてみました。うちのﾈｺﾁｬﾝで釣るあざとさ。

<iframe width="560" height="315" src="https://www.youtube.com/embed/1DgArjRYzVk?si=kV7ocRT4gMb3Id7e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 他の更新

　ぜひ[リリースノート（適当）](https://github.com/shellgei/rusty_bash/releases)をみてくださいっ！なにかBashにない機能追加してって言われたら前向きに検討いたしますので[issue](https://github.com/shellgei/rusty_bash/issues)とかSNSとかで言ってみてください！いまなら好き勝手言っても対応できる可能性高いです。

## 今後

　ネイピア数とか円周率とかもなんかシェルの中に持っとくといいかもしんない。肥大化するけど。

以上！

