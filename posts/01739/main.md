---
Keywords: コマンド,Haskell,open
Copyright: (C) 2017 Ryuichi Ueda
---

# <!--:ja-->Haskell版のformhame<!--:-->
<!--:ja-->HTMLのフォームに値をはめ込むというマニアックコマンドformhameをHaskell化しました．

<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/1a7cf15c150f183002e0a883f7a95b1198e149c3/COMMANDS.HS/formhame.hs" target="_blank">GitHub | Open-usp-Tukubai / COMMANDS.HS / formhame.hs</a>

半日しか時間がなかったので半日なりにとても汚いコードになってしもうたのですが，htmlがformhameの想定している書式になっていれば，という非常にわがままな条件付きで<a href="https://uec.usp-lab.com/TUKUBAI_MAN/CGI/TUKUBAI_MAN.CGI?POMPA=MAN1_formhame" target="_blank">マニュアル通り</a>に動きます．ただし，まだ-iや-dには対応してません．

formhameの想定しない書式というのは，例えばinput要素で途中に改行を入れると動かないとか，最後が「/>」で終わっていないとか，そういう，HTMLでは許されているようなことですので，ちょっとこのままではいかんなーと思います．

その上，Tukubaiコマンドは伝統的にhtmlを扱うときには真面目にパースしないので，それに準じて真面目にパースしないコードになってます．若い人が見たら発狂しそうだ・・・．

こんなコードを晒すくらいならちゃんとParsecでパースした方がいいような気もする．まあ，何もアップしないよりはマシ．

収穫はHaskellで正規表現を使う方法をマスターしたこと．しかしこれ，Haskellっぽくない．乱用は禁物かも．

寝る．<!--:-->
